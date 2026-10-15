const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');
const source = fs.readFileSync(path.join(__dirname, 'site/app.js'), 'utf8');

function page() {
  const elements = new Map();
  const context = vm.createContext({
    document: { querySelector(selector) {
      if (!elements.has(selector)) elements.set(selector, {
        addEventListener() {}, classList: { add() {}, toggle() {} }, style: {},
        value: '0', innerHTML: '', textContent: '',
      });
      return elements.get(selector);
    } },
    fetch: async () => ({ ok: false }),
  });
  vm.runInContext(source.replace(/main\(\);\s*$/, ''), context);
  return { context, elements, run: code => vm.runInContext(code, context) };
}

test('verified size series never use old totals or missing values', () => {
  const p = page();
  p.run('old = {values: {Go: 900, LLGoNoLTO: 800}}');
  for (const metric of ['withDwarf', 'withoutDwarf']) {
    assert.ok(Number.isNaN(p.run(`measureValue(old, 'Go', '${metric}')`)));
    assert.equal(p.run(`rankFor(old, 'Go', '${metric}')`), null);
  }
  assert.equal(p.run("measureValue(old, 'Go', 'legacySize')"), 900);
  p.run('paired = {values:{Go:900}, sizes:{withDwarf:{Go:900,LLGoNoLTO:1800},withoutDwarf:{Go:400,LLGoNoLTO:200}}}');
  assert.ok(Number.isNaN(p.run("measureValue(paired, 'Go', 'legacySize')")));
  assert.match(p.run("cellHtml(paired, 'LLGoNoLTO', 'withDwarf', 'a')"), /\+100\.0% vs Go/);
  assert.match(p.run("cellHtml(paired, 'LLGoNoLTO', 'withoutDwarf', 'a')"), /-50\.0% vs Go/);
  assert.equal(p.run("rankFor(paired, 'LLGoNoLTO', 'withoutDwarf').rank"), 1);
  p.run('paired.sizes.withoutDwarf.Go = null');
  assert.doesNotMatch(p.run("cellHtml(paired, 'LLGoNoLTO', 'withoutDwarf', 'a')"), /vs Go/);
  assert.match(p.run("cellHtml(paired, 'Go', 'withoutDwarf', 'a')"), /missing/);
});

test('A/B deltas stay within the same variant and exclude historical gaps', () => {
  const p = page();
  p.run(`state.benchmarkNames = ['Hello']; state.selectedKeys = ['a', 'b'];
    a = {name:'Hello',values:{Go:999},sizes:{withDwarf:{Go:100},withoutDwarf:{Go:50}}};
    b = {name:'Hello',values:{Go:999},sizes:{withDwarf:{Go:200},withoutDwarf:{Go:40}}};`);
  assert.match(p.run("cellHtml(b, 'Go', 'withDwarf', 'b', a)"), /Δ A \+100\.0%/);
  assert.match(p.run("cellHtml(b, 'Go', 'withoutDwarf', 'b', a)"), /Δ A -20\.0%/);
  assert.equal(p.run("comparisonPairs({benchmarks:[{name:'Hello',values:{Go:999}}]}, {benchmarks:[b]}, 'withDwarf').length"), 0);
});

test('paired trend charts break across legacy runs', () => {
  const p = page();
  p.run(`state.activeConfigs = new Set(['Go']);
    metas = [{key:'a'},{key:'old'},{key:'b'}];
    documents = [{benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:100},withoutDwarf:{Go:50}}}]},
      {benchmarks:[{name:'Hello',values:{Go:999}}]},
      {benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:200},withoutDwarf:{Go:40}}}]}];`);
  for (const metric of ['withDwarf', 'withoutDwarf']) {
    const chart = p.run(`chartBand(documents, metas, 'Hello', '${metric}', 'Size')`);
    assert.equal((chart.match(/class="history-point"/g) || []).length, 2);
    assert.equal((chart.match(/ M /g) || []).length, 2);
    assert.match(chart, /bytes/);
    assert.doesNotMatch(chart, /NaN|Infinity|wall time/);
  }
});
