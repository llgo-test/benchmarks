const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');
const source = fs.readFileSync(path.join(__dirname, 'site/app.js'), 'utf8');

function page(measure = "withoutDwarf") {
  const elements = new Map();
  const context = vm.createContext({
    document: { body: { dataset: { linuxMeasure: measure } }, querySelector(selector) {
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

test('historical totals join with-DWARF while missing paired measurements stay missing', () => {
  const p = page();
  p.run('old = {values: {Go: 900, LLGoNoLTO: 800}}');
  assert.equal(p.run("measureValue(old, 'Go', 'withDwarf')"), 900);
  assert.equal(p.run("rankFor(old, 'LLGoNoLTO', 'withDwarf').rank"), 1);
  assert.ok(Number.isNaN(p.run("measureValue(old, 'Go', 'withoutDwarf')")));
  assert.equal(p.run("rankFor(old, 'Go', 'withoutDwarf')"), null);
  p.run('old.sizes = null'); // compact historical trend records
  assert.equal(p.run("measureValue(old, 'Go', 'withDwarf')"), 900);
  p.run('paired = {values:{Go:900}, sizes:{withDwarf:{Go:900,LLGoNoLTO:1800},withoutDwarf:{Go:400,LLGoNoLTO:200}}}');
  assert.match(p.run("cellHtml(paired, 'LLGoNoLTO', 'withDwarf', 'a')"), /\+100\.0% vs Go/);
  assert.match(p.run("cellHtml(paired, 'LLGoNoLTO', 'withoutDwarf', 'a')"), /-50\.0% vs Go/);
  assert.equal(p.run("rankFor(paired, 'LLGoNoLTO', 'withoutDwarf').rank"), 1);
  p.run('paired.sizes.withoutDwarf.Go = null; paired.sizes.withDwarf.Go = null');
  assert.ok(Number.isNaN(p.run("measureValue(paired, 'Go', 'withDwarf')")));
  assert.doesNotMatch(p.run("cellHtml(paired, 'LLGoNoLTO', 'withoutDwarf', 'a')"), /vs Go/);
  assert.match(p.run("cellHtml(paired, 'Go', 'withoutDwarf', 'a')"), /missing/);
});

test('A/B comparisons include historical original sizes only in with-DWARF', () => {
  const p = page();
  p.run(`state.benchmarkNames = ['Hello']; state.selectedKeys = ['a', 'b'];
    a = {name:'Hello',values:{Go:999},sizes:{withDwarf:{Go:100},withoutDwarf:{Go:50}}};
    b = {name:'Hello',values:{Go:999},sizes:{withDwarf:{Go:200},withoutDwarf:{Go:40}}};`);
  assert.match(p.run("cellHtml(b, 'Go', 'withDwarf', 'b', a)"), /Δ A \+100\.0%/);
  assert.match(p.run("cellHtml(b, 'Go', 'withoutDwarf', 'b', a)"), /Δ A -20\.0%/);
  assert.equal(p.run("comparisonPairs({benchmarks:[{name:'Hello',values:{Go:999}}]}, {benchmarks:[b]}, 'withDwarf').length"), 1);
  assert.equal(p.run("comparisonPairs({benchmarks:[{name:'Hello',values:{Go:999}}]}, {benchmarks:[b]}, 'withoutDwarf').length"), 0);
});

test('with-DWARF trends include history while without-DWARF keeps historical gaps', () => {
  const p = page();
  p.run(`state.activeConfigs = new Set(['Go']);
    metas = [{key:'a'},{key:'old'},{key:'b'}];
    documents = [{benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:100},withoutDwarf:{Go:50}}}]},
      {benchmarks:[{name:'Hello',values:{Go:999}}]},
      {benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:200},withoutDwarf:{Go:40}}}]}];`);
  for (const metric of ['withDwarf', 'withoutDwarf']) {
    const chart = p.run(`chartBand(documents, metas, 'Hello', '${metric}', 'Size')`);
    assert.equal((chart.match(/class="history-point"/g) || []).length, metric === 'withDwarf' ? 3 : 2);
    assert.equal((chart.match(/ M /g) || []).length, metric === 'withDwarf' ? 1 : 2);
    assert.match(chart, /bytes/);
    assert.doesNotMatch(chart, /NaN|Infinity|wall time/);
  }
});

for (const measure of ['withoutDwarf', 'withDwarf']) {
  test(`${measure}: table, A/B summary and trend use only the page's size measure`, async () => {
    const p = page(measure);
    p.run(`state.index = {runs:[{key:'a'},{key:'b'}]};
      state.benchmarkNames = ['Hello']; state.activeBenchmark = 'Hello';
      state.activeConfigs = new Set(['Go']);
      state.comparisonMode = true; state.selectedKeys = ['a','b'];
      state.runs.set('a', Promise.resolve({benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:100},withoutDwarf:{Go:50}}}]}));
      state.runs.set('b', Promise.resolve({benchmarks:[{name:'Hello',sizes:{withDwarf:{Go:200},withoutDwarf:{Go:40}}}]}));
      loadTrends = async () => null;`);
    await p.run('renderTables()');
    const table = p.elements.get('#size-grid').innerHTML;
    assert.match(table, measure === 'withDwarf' ? /200 B/ : /40 B/);
    assert.doesNotMatch(table, measure === 'withDwarf' ? /40 B/ : /200 B/);
    await p.run('renderComparisonSummary()');
    assert.equal(p.elements.get('#compare-size').textContent, measure === 'withDwarf' ? '+100.0%' : '-20.0%');
    await p.run('renderTrend()');
    const trend = p.elements.get('#trend-chart').innerHTML;
    assert.match(trend, measure === 'withDwarf' ? /Binary size · with DWARF/ : /Binary size · without DWARF/);
    assert.doesNotMatch(trend, measure === 'withDwarf' ? /Binary size · without DWARF/ : /Binary size · with DWARF/);
    assert.equal((trend.match(/class="chart-band"/g) || []).length, 2);
  });
}
