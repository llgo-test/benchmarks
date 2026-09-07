const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const site = path.join(__dirname, '../llgo-size/site');
const source = fs.readFileSync(path.join(site, 'wasm.js'), 'utf8');
function page(baseline) {
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
  vm.runInContext(source, context);
  return { run: code => vm.runInContext(code, context), context, elements };
}

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
