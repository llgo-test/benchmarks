const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const site = path.join(__dirname, '../llgo-size/site');
const source = fs.readFileSync(path.join(site, 'wasm.js'), 'utf8');
function page(baseline, code = source) {
  const elements = new Map();
  const context = vm.createContext({
    document: {
      body: { dataset: { wasmBaseline: baseline } },
      querySelector(selector) {
        if (!elements.has(selector)) elements.set(selector, {
          addEventListener() {}, classList: { add() {}, remove() {} }, style: {},
          value: '0', innerHTML: '', textContent: '', removeAttribute() {},
        });
        return elements.get(selector);
      },
    },
    fetch: async () => ({status: 404}),
  });
  vm.runInContext(code, context);
  return { run: code => vm.runInContext(code, context), context, elements };
}

test('failed WASM cells retain failure status and never rank as zero', () => {
  const p = page('Go');
  p.run('row = {values:{Go:100,LLGoNoLTO:null}, builds:{LLGoNoLTO:{status:"failed"}}}');
  assert.match(p.run('wasmCellHtml(row, "LLGoNoLTO")'), /Build failed/);
  assert.equal(p.run('wasmRank(row, "LLGoNoLTO")'), null);
});

test('native null measurements are gaps, including a missing Go baseline', () => {
  const p = page('Go', fs.readFileSync(path.join(site, 'app.js'), 'utf8'));
  p.run('row = {values:{Go:null,LLGoNoLTO:50},buildTimes:{Go:{cpuNs:null,wallNs:null}}}');
  for (const measure of ['size', 'wall', 'cpu']) {
    assert.ok(Number.isNaN(p.run(`measureValue(row, "Go", "${measure}")`)));
    assert.equal(p.run(`rankFor(row, "Go", "${measure}")`), null);
  }
  assert.equal(p.run('measureValue(row, "LLGoNoLTO", "size")'), 50);
});

for (const baseline of ['Go', 'TinyGo']) {
  test(`${baseline}: independent baseline, legacy values, nulls and ranks`, () => {
    const p = page(baseline);
    assert.equal(p.run('wasmCompilers.length'), 5);
    assert.equal(p.run('wasmCompilers[0]'), baseline);
    assert.equal(p.run(`wasmCompilers.includes('${baseline === 'Go' ? 'TinyGo' : 'Go'}')`), false);
    assert.equal(p.run('wasmValue({values:{LLGo:42}}, "LLGoNoLTO")'), 42);
    assert.ok(Number.isNaN(p.run('wasmValue({values:{LLGo:42}}, "LLGoFullLTOGlobalDCE")')));
    for (const raw of ['null', 'undefined', '0', '-1', '"42"']) {
      assert.ok(Number.isNaN(p.run(`wasmValue({values:{TinyGo:${raw}}}, 'TinyGo')`)));
    }
    p.run('row = {values:{Go:1000,TinyGo:10,LLGoNoLTO:20,LLGoDeadcodeDrop:15,LLGoFullLTONoGlobalDCE:12,LLGoFullLTOGlobalDCE:5}}');
    const cell = p.run('wasmCellHtml(row, "LLGoNoLTO")');
    assert.match(cell, new RegExp(`vs ${baseline}`));
    assert.match(cell, new RegExp(baseline === 'Go' ? '-98.0%' : '\\+100.0%'));
    assert.equal(p.run('wasmRank(row, "LLGoNoLTO").rank'), baseline === 'Go' ? 4 : 5);
    p.run(`row.values.${baseline} = null`);
    assert.equal(p.run('wasmRank(row, "LLGoNoLTO")'), null);
    const missing = p.run('wasmCellHtml(row, "LLGoNoLTO")');
    assert.match(missing, /20 B/);
    assert.match(missing, /— vs/);
    assert.doesNotMatch(missing, /#\d|rank-best|rank-worst/);
  });

  test(`${baseline}: history ratios and gaps do not synthesize zero-byte data`, () => {
    const p = page(baseline);
    const row = values => ({benchmarks: [{id:'sample', values}]});
    p.context.documents = [row({Go:100, TinyGo:10, LLGo:20}), row({Go:null, TinyGo:null, LLGo:40}), row({Go:100,TinyGo:20,LLGoNoLTO:40})];
    p.context.runs = [{key:'a'}, {key:'b'}, {key:'c'}];
    p.run('wasmState.activeCompilers = new Set(["LLGoNoLTO"])');
    const html = p.run('wasmChartHtml(documents, runs, "sample")');
    assert.match(html, new RegExp(`Size relative to ${baseline}`));
    assert.equal((html.match(/class="history-point"/g) || []).length, 2);
    assert.equal((html.match(/ M /g) || []).length, 2); // disconnected across the missing baseline
    assert.doesNotMatch(html, /NaN|Infinity/);
    p.run('wasmState.activeCompilers = new Set(["LLGoFullLTOGlobalDCE"])');
    assert.match(p.run('wasmChartHtml(documents, runs, "sample")'), /No binary-size history/);
  });
}

test('all pages have two WASM links and correct active navigation', () => {
  for (const file of ['index.html','wasm-tinygo.html','linux.html','performance.html','compatibility.html']) {
    const html = fs.readFileSync(path.join(site, file), 'utf8');
    assert.match(html, /href="index.html"[^>]*>WASM binary size \(vs\. Go\)/);
    assert.match(html, /href="wasm-tinygo.html"[^>]*>WASM binary size \(vs\. TinyGo\)/);
    assert.equal((html.match(/aria-current="page"/g) || []).length, 1);
  }
});

test('application toolchain metadata stays with its historical cell', () => {
  const p = page('Go');
  p.run('oldRow = {goVersion:"1.26.2",values:{Go:100}}; newRow = {goVersion:"1.27.0",values:{Go:120}}');
  assert.match(p.run('wasmCellHtml(oldRow, "Go")'), /Go toolchain 1\.26\.2/);
  assert.match(p.run('wasmCellHtml(newRow, "Go")'), /Go toolchain 1\.27\.0/);
  assert.doesNotMatch(p.run('wasmCellHtml({values:{Go:100}}, "Go")'), /Go toolchain/);
  const tiny = page('TinyGo');
  assert.match(tiny.run('wasmCellHtml({goVersion:"1.27.0",values:{TinyGo:null}}, "TinyGo")'), /Go toolchain 1\.27\.0/);
});


test('timeouts and runtime checks remain distinct from build size', () => {
  const p = page('Go');
  p.run('row = {values:{Go:100,LLGoNoLTO:null}, builds:{LLGoNoLTO:{status:"timeout"}}}');
  assert.match(p.run('wasmCellHtml(row, "LLGoNoLTO")'), /Build timed out/);
  assert.equal(p.run('wasmRank(row, "LLGoNoLTO")'), null);
  p.run('row.values.LLGoNoLTO = 80; row.validation = {LLGoNoLTO:{startup:{status:"failed"},functional:{status:"not_run"}}}');
  const cell = p.run('wasmCellHtml(row, "LLGoNoLTO")');
  assert.match(cell, /80 B/);
  assert.match(cell, /Startup: failed/);
  assert.match(cell, /TS compilation: not checked/);
});
