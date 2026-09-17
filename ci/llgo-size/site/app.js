const state = {
  index: null,
  runs: new Map(),
  trends: null,
  benchmarkNames: [],
  activeBenchmark: "",
  activeConfigs: new Set(),
  page: 1,
  pageSize: 8,
  query: "",
  comparisonMode: false,
  selectedKeys: [],
};

const configs = [
  "Go",
  "LLGoNoLTO",
  "LLGoDeadcodeDrop",
  "LLGoFullLTONoGlobalDCE",
  "LLGoFullLTOGlobalDCE",
  "LLGoFullLTOGlobalDCEPlugin",
];

const configLabels = {
  Go: "Go",
  LLGoNoLTO: "LLGo · no LTO",
  LLGoDeadcodeDrop: "LLGo · deadcode drop",
  LLGoFullLTONoGlobalDCE: "LLGo · full LTO",
  LLGoFullLTOGlobalDCE: "LLGo · LTO + GlobalDCE",
  LLGoFullLTOGlobalDCEPlugin: "LLGo · LTO + DCE + plugin",
};

const compactConfigLabels = {
  Go: "Go",
  LLGoNoLTO: "No LTO",
  LLGoDeadcodeDrop: "Deadcode drop",
  LLGoFullLTONoGlobalDCE: "Full LTO",
  LLGoFullLTOGlobalDCE: "LTO + DCE",
  LLGoFullLTOGlobalDCEPlugin: "LTO + DCE + P",
};

const seriesColors = ["#2457d6", "#7c3aed", "#4d7c0f", "#d97706", "#0f766e", "#c92a2a"];
const dom = {
  status: document.querySelector("#status"),
  sizeGrid: document.querySelector("#size-grid"),
  timeGrid: document.querySelector("#time-grid"),
  sizeWrap: document.querySelector("#size-wrap"),
  timeWrap: document.querySelector("#time-wrap"),
  filter: document.querySelector("#commit-filter"),
  pageSize: document.querySelector("#page-size"),
  commitCount: document.querySelector("#commit-count"),
  pagination: document.querySelector("#pagination"),
  compareToggle: document.querySelector("#compare-toggle"),
  compareHint: document.querySelector("#compare-hint"),
  comparisonStrip: document.querySelector("#comparison-strip"),
  compareA: document.querySelector("#compare-a"),
  compareB: document.querySelector("#compare-b"),
  compareSize: document.querySelector("#compare-size"),
  compareTime: document.querySelector("#compare-time"),
  clearComparison: document.querySelector("#clear-comparison"),
  historyRange: document.querySelector("#history-range"),
  benchmarkSelect: document.querySelector("#benchmark-select"),
  configFilter: document.querySelector("#config-filter"),
  trendChart: document.querySelector("#trend-chart"),
  envRunner: document.querySelector("#env-runner"),
  envToolchain: document.querySelector("#env-toolchain"),
  envLlgo: document.querySelector("#env-llgo"),
  envProtocol: document.querySelector("#env-protocol"),
};

function escapeHtml(value) {
  return String(value == null ? "" : value).replace(/[&<>"']/g, function (char) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char];
  });
}

function formatBytes(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "—";
  const units = ["B", "KiB", "MiB", "GiB"];
  let scaled = Math.abs(number);
  let unit = 0;
  while (scaled >= 1024 && unit < units.length - 1) {
    scaled /= 1024;
    unit++;
  }
  return (number < 0 ? "-" : "") + scaled.toFixed(unit ? 3 : 0) + " " + units[unit];
}

function formatDuration(value) {
  const nanoseconds = Number(value);
  if (!Number.isFinite(nanoseconds)) return "—";
  const seconds = Math.abs(nanoseconds) / 1e9;
  const sign = nanoseconds < 0 ? "-" : "";
  if (seconds >= 60) return sign + Math.floor(seconds / 60) + "m " + (seconds % 60).toFixed(1) + "s";
  if (seconds >= 10) return sign + seconds.toFixed(1) + "s";
  if (seconds >= 1) return sign + seconds.toFixed(2) + "s";
  return sign + (seconds * 1000).toFixed(1) + "ms";
}

function formatPercent(value, digits) {
  if (!Number.isFinite(value)) return "—";
  return (value > 0 ? "+" : "") + value.toFixed(digits == null ? 1 : digits) + "%";
}

function percentDelta(value, base) {
  const current = Number(value);
  const reference = Number(base);
  if (!Number.isFinite(current) || !Number.isFinite(reference) || reference === 0) return null;
  return ((current - reference) / reference) * 100;
}

function deltaClass(delta) {
  return delta > 0 ? "bad" : delta < 0 ? "good" : "flat";
}

function shortSha(value) {
  return value ? String(value).slice(0, 10) : "—";
}

function dateLabel(value) {
  if (!value) return "unknown time";
  return new Date(value).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

function commitLabel(run) {
  return shortSha(run && (run.llgoCommit || run.sourceCommit || run.key));
}

function commitHref(run) {
  const pullRequestUrl = String(run && run.pullRequestUrl || "");
  if (/^https:\/\/github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/pull\/[1-9][0-9]*$/.test(pullRequestUrl)) {
    return pullRequestUrl;
  }
  const commitUrl = String(run && run.commitUrl || "");
  if (/^https:\/\/github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/commit\/[0-9a-fA-F]{40}$/.test(commitUrl)) {
    return commitUrl;
  }
  const repository = String(run && run.llgoRepository || "xgo-dev/llgo");
  const commit = String(run && run.llgoCommit || "");
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository) || !/^[0-9a-fA-F]{40}$/.test(commit)) return "";
  return "https://github.com/" + repository + "/commit/" + commit;
}

function commitLinkTitle(run) {
  if (run && run.pullRequestUrl) {
    const number = Number(run.pullRequestNumber);
    return "Open the pull request that landed this commit" + (Number.isInteger(number) ? " (#" + number + ")" : "");
  }
  return "Open this LLGo commit";
}

function commitLinkHtml(run, content, className, ariaLabel) {
  const href = commitHref(run);
  if (!href) return content;
  return '<a class="' + className + '" href="' + escapeHtml(href) + '" target="_blank" rel="noopener noreferrer" aria-label="' + escapeHtml(ariaLabel || commitLinkTitle(run)) + '" title="' + escapeHtml(commitLinkTitle(run)) + '">' + content + "</a>";
}

function benchmarkMap(document) {
  return new Map((document && document.benchmarks || []).map(function (item) { return [item.name, item]; }));
}

function benchmarkNamesFromDocuments(documents) {
  const names = new Set();
  documents.forEach(function (document) {
    (document && document.benchmarks || []).forEach(function (benchmark) { names.add(benchmark.name); });
  });
  return sortedBenchmarkNames(names);
}

function sortedBenchmarkNames(names) {
  return Array.from(new Set(Array.from(names || []).filter(function (name) { return typeof name === "string" && name; })))
    .sort(function (a, b) { return a.localeCompare(b, undefined, { sensitivity: "base" }); });
}

function parseBuildTimes(text) {
  const lines = String(text || "").trim().split(/\r?\n/);
  if (lines.length < 2) return new Map();
  const header = lines[0].split("\t");
  const column = function (name) { return header.indexOf(name); };
  const benchmarkColumn = column("benchmark");
  const configColumn = column("configuration");
  const realColumn = column("real-ns");
  const userColumn = column("user-ns");
  const sysColumn = column("sys-ns");
  if ([benchmarkColumn, configColumn, realColumn, userColumn, sysColumn].some(function (index) { return index < 0; })) return new Map();
  const result = new Map();
  lines.slice(1).forEach(function (line) {
    if (!line) return;
    const fields = line.split("\t");
    const userNs = Number(fields[userColumn]);
    const sysNs = Number(fields[sysColumn]);
    const wallNs = Number(fields[realColumn]);
    if (![userNs, sysNs, wallNs].every(Number.isFinite)) return;
    const name = fields[benchmarkColumn];
    const config = fields[configColumn];
    if (!result.has(name)) result.set(name, {});
    result.get(name)[config] = { cpuNs: userNs + sysNs, userNs: userNs, sysNs: sysNs, wallNs: wallNs };
  });
  return result;
}

function runAssetUrl(meta, path) {
  const version = [meta.id || meta.key, meta.attempt || 1, meta.createdAt || ""]
    .map(String).join("-");
  return "data/" + path + "?v=" + encodeURIComponent(version);
}

async function loadLegacyBuildTimes(meta, document) {
  const nativePath = document.native && document.native.buildTimes;
  if (!nativePath) return;
  const incomplete = (document.benchmarks || []).some(function (benchmark) {
    return configs.some(function (config) {
      return !benchmark.buildTimes || !benchmark.buildTimes[config] || !Number.isFinite(Number(benchmark.buildTimes[config].wallNs));
    });
  });
  if (!incomplete) return;
  const basePath = meta.path.slice(0, meta.path.lastIndexOf("/") + 1);
  const response = await fetch(runAssetUrl(meta, basePath + nativePath));
  if (!response.ok) return;
  const timings = parseBuildTimes(await response.text());
  (document.benchmarks || []).forEach(function (benchmark) {
    benchmark.buildTimes = Object.assign({}, timings.get(benchmark.name) || {}, benchmark.buildTimes || {});
  });
}

async function loadRun(meta) {
  if (!meta) return null;
  if (!state.runs.has(meta.key)) {
    state.runs.set(meta.key, (async function () {
      const response = await fetch(runAssetUrl(meta, meta.path));
      if (!response.ok) throw new Error("Cannot load " + meta.path);
      const document = await response.json();
      await loadLegacyBuildTimes(meta, document);
      return document;
    })());
  }
  return state.runs.get(meta.key);
}

async function loadTrends() {
  if (!state.trends) {
    state.trends = (async function () {
      const version = encodeURIComponent(state.index.generatedAt || "latest");
      const response = await fetch("data/trends.json?v=" + version);
      if (!response.ok) return null;
      const document = await response.json();
      return new Map((document.runs || []).map(function (run) { return [run.key, run]; }));
    })();
  }
  return state.trends;
}

function findMeta(key) {
  return state.index && state.index.runs.find(function (run) { return run.key === key; });
}

function latestRun() {
  const runs = state.index && state.index.runs || [];
  return runs[0];
}

function measureValue(benchmark, config, measure) {
  if (!benchmark) return NaN;
  const timing = benchmark.buildTimes && benchmark.buildTimes[config];
  const value = measure === "size" ? benchmark.values && benchmark.values[config]
    : timing && (measure === "wall" ? timing.wallNs : timing.cpuNs);
  return value == null ? NaN : Number(value);
}

function formatMeasure(value, measure) {
  return measure === "size" ? formatBytes(value) : formatDuration(value);
}

function filteredRuns() {
  const query = state.query.trim().toLowerCase();
  if (!query) return state.index.runs;
  return state.index.runs.filter(function (run) {
    return [commitLabel(run), run.llgoCommit, run.sourceCommit, run.ref, run.llgoCommittedAt, run.createdAt, run.key]
      .some(function (value) { return String(value || "").toLowerCase().includes(query); });
  });
}

function currentPageRuns() {
  const runs = filteredRuns();
  const pageCount = Math.max(1, Math.ceil(runs.length / state.pageSize));
  state.page = Math.min(Math.max(1, state.page), pageCount);
  const start = (state.page - 1) * state.pageSize;
  return runs.slice(start, start + state.pageSize);
}

function pageNumbers(page, pageCount) {
  const values = new Set([1, pageCount, page - 1, page, page + 1]);
  return Array.from(values).filter(function (value) { return value >= 1 && value <= pageCount; }).sort(function (a, b) { return a - b; });
}

function renderPagination() {
  const runs = filteredRuns();
  const pageCount = Math.max(1, Math.ceil(runs.length / state.pageSize));
  state.page = Math.min(state.page, pageCount);
  dom.commitCount.textContent = runs.length + " commit" + (runs.length === 1 ? "" : "s") + " · page " + state.page + "/" + pageCount;
  const numbers = pageNumbers(state.page, pageCount);
  let previous = 0;
  const buttons = ['<button type="button" data-page="' + (state.page - 1) + '"' + (state.page === 1 ? " disabled" : "") + '>←</button>'];
  numbers.forEach(function (page) {
    if (previous && page - previous > 1) buttons.push('<span class="page-gap">…</span>');
    buttons.push('<button type="button" data-page="' + page + '" class="' + (page === state.page ? "active" : "") + '">' + page + "</button>");
    previous = page;
  });
  buttons.push('<button type="button" data-page="' + (state.page + 1) + '"' + (state.page === pageCount ? " disabled" : "") + '>→</button>');
  dom.pagination.innerHTML = buttons.join("");
}

function rankFor(benchmark, config, measure) {
  const value = measureValue(benchmark, config, measure);
  if (!Number.isFinite(value)) return null;
  const values = configs.map(function (name) { return measureValue(benchmark, name, measure); }).filter(Number.isFinite);
  const unique = Array.from(new Set(values)).sort(function (a, b) { return a - b; });
  const rank = unique.indexOf(value) + 1;
  const ties = values.filter(function (candidate) { return candidate === value; }).length;
  const position = unique.length <= 1 ? 0 : (rank - 1) / (unique.length - 1);
  let tone = "rank-mid";
  if (rank === 1) tone = "rank-best";
  else if (rank === unique.length) tone = "rank-worst";
  else if (position <= .34) tone = "rank-good";
  else if (position >= .67) tone = "rank-slow";
  return { rank: rank, ties: ties, tone: tone };
}

function columnClass(key) {
  const index = state.selectedKeys.indexOf(key);
  return index === 0 ? "selected-a" : index === 1 ? "selected-b" : "";
}

function headerHtml(run) {
  const selected = state.selectedKeys.indexOf(run.key);
  const marker = selected >= 0 ? '<b class="pick-marker">' + (selected === 0 ? "A" : "B") + "</b>" : "";
  const commit = commitLinkHtml(run, "<code>" + escapeHtml(commitLabel(run)) + "</code>", "commit-link", commitLinkTitle(run) + ": " + commitLabel(run));
  const date = escapeHtml(dateLabel(run.llgoCommittedAt || run.createdAt));
  const detail = state.comparisonMode
    ? '<button class="commit-select" type="button" data-run-key="' + escapeHtml(run.key) + '" title="Select ' + escapeHtml(commitLabel(run)) + ' for comparison">' + marker + "<span>" + date + "</span></button>"
    : '<span class="commit-date">' + date + "</span>";
  return '<th class="commit-header ' + columnClass(run.key) + '"><div class="commit-header-content">' + commit + detail + "</div></th>";
}

function cellHtml(benchmark, config, measure, runKey, baselineBenchmark) {
  const value = measureValue(benchmark, config, measure);
  const selectedClass = columnClass(runKey);
  if (!Number.isFinite(value)) return '<td class="matrix-cell missing ' + selectedClass + '">—</td>';
  const rank = rankFor(benchmark, config, measure);
  const rankText = "#" + rank.rank + (rank.ties > 1 ? "=" : "");
  let secondary = "";
  if (measure === "wall") {
    const cpu = measureValue(benchmark, config, "cpu");
    if (Number.isFinite(cpu)) secondary = '<span class="secondary-value">CPU ' + formatDuration(cpu) + "</span>";
  }
  let context = "";
  if (state.selectedKeys.length === 2 && selectedClass) {
    const goValue = measureValue(benchmark, "Go", measure);
    if (config === "Go") context = '<span class="comparison-context flat">Go reference</span>';
    else {
      const vsGo = percentDelta(value, goValue);
      if (Number.isFinite(vsGo)) context = '<span class="comparison-context ' + deltaClass(vsGo) + '">' + formatPercent(vsGo) + " vs Go</span>";
    }
  }
  let comparison = "";
  if (state.selectedKeys.length === 2 && runKey === state.selectedKeys[1]) {
    const baseline = measureValue(baselineBenchmark, config, measure);
    const delta = percentDelta(value, baseline);
    if (Number.isFinite(delta)) comparison = '<span class="selected-delta ' + deltaClass(delta) + '">Δ A ' + formatPercent(delta) + "</span>";
  }
  return '<td class="matrix-cell ' + rank.tone + " " + selectedClass + '"><span class="rank-number">' + rankText + "</span><strong>" + formatMeasure(value, measure) + "</strong>" + secondary + context + comparison + "</td>";
}

function renderMatrix(target, runs, documents, baselineDocument, measure) {
  const maps = documents.map(benchmarkMap);
  const baselineMap = benchmarkMap(baselineDocument);
  const head = '<thead><tr><th class="matrix-label-cell">Benchmark / mode</th>' + runs.map(headerHtml).join("") + "</tr></thead>";
  const rows = [];
  state.benchmarkNames.forEach(function (benchmarkName) {
    configs.forEach(function (config, configIndex) {
      const benchmarkLabel = configIndex === 0 ? '<span class="benchmark-name">' + escapeHtml(benchmarkName) + "</span>" : "";
      const configClass = configIndex === 0 ? "config-name" : "config-name config-continuation";
      const label = '<th class="matrix-label-cell" aria-label="' + escapeHtml(benchmarkName + " · " + compactConfigLabels[config]) + '">' + benchmarkLabel + '<span class="' + configClass + '">' + escapeHtml(compactConfigLabels[config]) + "</span></th>";
      const cells = runs.map(function (run, index) {
        return cellHtml(maps[index].get(benchmarkName), config, measure, run.key, baselineMap.get(benchmarkName));
      }).join("");
      const groupClass = configIndex === 0 ? "benchmark-group-start" : "";
      rows.push('<tr class="' + groupClass + '">' + label + cells + "</tr>");
    });
  });
  target.classList.toggle("comparison-mode", state.comparisonMode);
  target.style.minWidth = (136 + runs.length * 132) + "px";
  target.innerHTML = head + "<tbody>" + (rows.length ? rows.join("") : '<tr><td class="empty-state">No benchmark data.</td></tr>') + "</tbody>";
}

function geometricMeanDelta(values) {
  const ratios = values.filter(function (pair) { return pair[0] > 0 && pair[1] > 0; }).map(function (pair) { return pair[1] / pair[0]; });
  if (!ratios.length) return NaN;
  return (Math.exp(ratios.reduce(function (sum, ratio) { return sum + Math.log(ratio); }, 0) / ratios.length) - 1) * 100;
}

function comparisonPairs(aDocument, bDocument, measure) {
  const aMap = benchmarkMap(aDocument);
  const bMap = benchmarkMap(bDocument);
  const pairs = [];
  state.benchmarkNames.forEach(function (name) {
    configs.forEach(function (config) {
      const a = measureValue(aMap.get(name), config, measure);
      const b = measureValue(bMap.get(name), config, measure);
      if (Number.isFinite(a) && Number.isFinite(b)) pairs.push([a, b]);
    });
  });
  return pairs;
}

async function renderComparisonSummary() {
  const complete = state.comparisonMode && state.selectedKeys.length === 2;
  dom.compareHint.hidden = !state.comparisonMode || complete;
  dom.comparisonStrip.hidden = !complete;
  if (!complete) return;
  const aMeta = findMeta(state.selectedKeys[0]);
  const bMeta = findMeta(state.selectedKeys[1]);
  const documents = await Promise.all([loadRun(aMeta), loadRun(bMeta)]);
  dom.compareA.textContent = "A " + commitLabel(aMeta);
  dom.compareB.textContent = "B " + commitLabel(bMeta);
  const sizeDelta = geometricMeanDelta(comparisonPairs(documents[0], documents[1], "size"));
  const timeDelta = geometricMeanDelta(comparisonPairs(documents[0], documents[1], "wall"));
  dom.compareSize.textContent = formatPercent(sizeDelta);
  dom.compareSize.className = deltaClass(sizeDelta);
  dom.compareTime.textContent = formatPercent(timeDelta);
  dom.compareTime.className = deltaClass(timeDelta);
}

function normalizeRunner(run) {
  let image = run.runnerImage || "Ubuntu 24.04";
  image = String(image).replace(/^ubuntu(\d{2})$/i, "Ubuntu $1.04");
  const arch = String(run.runnerArch || "x86_64").replace(/^X64$/i, "x86_64");
  const os = run.runnerOS && !String(image).toLowerCase().includes(String(run.runnerOS).toLowerCase()) ? run.runnerOS + " · " : "";
  return os + image + " · " + arch;
}

function goVersionLabel(value) {
  const version = String(value || "—");
  return /^go\s/i.test(version) ? version : "Go " + version;
}

async function renderEnvironment() {
  const newest = latestRun();
  const key = state.selectedKeys.length === 2 ? state.selectedKeys[1] : newest.key;
  const meta = findMeta(key) || newest;
  const document = await loadRun(meta);
  const run = document.run || {};
  dom.envRunner.textContent = normalizeRunner(run);
  dom.envToolchain.textContent = goVersionLabel(run.goVersion || meta.goVersion) + " · LLVM " + (run.llvmVersion || meta.llvmVersion || "—");
  dom.envLlgo.textContent = commitLabel(meta) + " · " + (run.ref || meta.ref || "main");
  const runNumber = run.number || meta.number || meta.key;
  dom.envProtocol.textContent = "Bent · run #" + runNumber;
}

async function renderTables() {
  renderPagination();
  const runs = currentPageRuns();
  const documents = await Promise.all(runs.map(loadRun));
  const baselineDocument = state.selectedKeys.length === 2 ? await loadRun(findMeta(state.selectedKeys[0])) : null;
  renderMatrix(dom.sizeGrid, runs, documents, baselineDocument, "size");
  renderMatrix(dom.timeGrid, runs, documents, baselineDocument, "wall");
}

function chartRuns() {
  const limit = Number(dom.historyRange.value);
  const newest = limit > 0 ? state.index.runs.slice(0, limit) : state.index.runs.slice();
  return newest.reverse();
}

function chartBand(documents, metas, benchmarkName, measure, title) {
  const width = 1120;
  const height = 225;
  const margin = { top: 17, right: 18, bottom: 32, left: 75 };
  const plotWidth = width - margin.left - margin.right;
  const plotHeight = height - margin.top - margin.bottom;
  const selectedConfigs = configs.filter(function (config) { return state.activeConfigs.has(config); });
  const series = selectedConfigs.map(function (config) {
    const values = documents.map(function (document) { return measureValue(benchmarkMap(document).get(benchmarkName), config, measure); });
    return { config: config, values: values };
  });
  const finite = series.flatMap(function (item) { return item.values.filter(Number.isFinite); });
  if (!finite.length) return '<div class="chart-band"><div class="empty-state">No ' + escapeHtml(title.toLowerCase()) + " data for this benchmark.</div></div>";
  let min = Math.min.apply(null, finite);
  let max = Math.max.apply(null, finite);
  const padding = (max - min || Math.abs(max) * .1 || 1) * .09;
  min = Math.max(0, min - padding);
  max += padding;
  const x = function (index) { return margin.left + (metas.length <= 1 ? plotWidth / 2 : index * plotWidth / (metas.length - 1)); };
  const y = function (value) { return margin.top + (max - value) * plotHeight / (max - min); };
  const parts = [];
  for (let tick = 0; tick <= 4; tick++) {
    const value = max - (max - min) * tick / 4;
    const py = margin.top + plotHeight * tick / 4;
    parts.push('<line class="chart-grid-line" x1="' + margin.left + '" y1="' + py + '" x2="' + (width - margin.right) + '" y2="' + py + '"></line>');
    parts.push('<text class="chart-axis-label" x="' + (margin.left - 8) + '" y="' + (py + 3) + '" text-anchor="end">' + escapeHtml(formatMeasure(value, measure)) + "</text>");
  }
  const labelStep = Math.max(1, Math.ceil(metas.length / 8));
  metas.forEach(function (meta, index) {
    if (index % labelStep === 0 || index === metas.length - 1) {
      const label = '<text class="chart-axis-label" x="' + x(index) + '" y="' + (height - 9) + '" text-anchor="middle">' + escapeHtml(shortSha(meta.llgoCommit || meta.key).slice(0, 7)) + "</text>";
      parts.push(commitLinkHtml(meta, label, "chart-commit-link", commitLinkTitle(meta) + ": " + commitLabel(meta)));
    }
  });
  if (state.selectedKeys.length === 2) {
    state.selectedKeys.forEach(function (key, markerIndex) {
      const index = metas.findIndex(function (meta) { return meta.key === key; });
      if (index < 0) return;
      const px = x(index);
      parts.push('<line class="selection-marker" x1="' + px + '" y1="' + margin.top + '" x2="' + px + '" y2="' + (height - margin.bottom) + '"></line>');
      parts.push('<text class="marker-label" x="' + (px + 5) + '" y="' + (margin.top + 10) + '">' + (markerIndex === 0 ? "A" : "B") + "</text>");
    });
  }
  series.forEach(function (item) {
    const color = seriesColors[configs.indexOf(item.config)];
    let path = "";
    let drawing = false;
    item.values.forEach(function (value, index) {
      if (!Number.isFinite(value)) { drawing = false; return; }
      path += (drawing ? " L " : " M ") + x(index).toFixed(2) + " " + y(value).toFixed(2);
      drawing = true;
    });
    parts.push('<path class="history-series" stroke="' + color + '" d="' + path + '"></path>');
    item.values.forEach(function (value, index) {
      if (!Number.isFinite(value)) return;
      const point = '<circle class="history-point" fill="' + color + '" cx="' + x(index) + '" cy="' + y(value) + '" r="3"><title>' + escapeHtml(configLabels[item.config] + " · " + commitLabel(metas[index]) + " · " + formatMeasure(value, measure) + " · " + commitLinkTitle(metas[index])) + "</title></circle>";
      parts.push(commitLinkHtml(metas[index], point, "history-point-link", commitLinkTitle(metas[index]) + ": " + commitLabel(metas[index])));
    });
  });
  return '<div class="chart-band"><div class="chart-title"><span>' + escapeHtml(title) + '</span><span>' + escapeHtml(measure === "size" ? "bytes" : "wall time") + '</span></div><svg viewBox="0 0 ' + width + " " + height + '" role="img" aria-label="' + escapeHtml(title + " trend") + '">' + parts.join("") + "</svg></div>";
}

async function renderTrend() {
  const metas = chartRuns();
  const trends = await loadTrends();
  const documents = trends
    ? await Promise.all(metas.map(function (meta) { return trends.get(meta.key) || loadRun(meta); }))
    : await Promise.all(metas.map(loadRun));
  const benchmarkName = state.activeBenchmark || state.benchmarkNames[0];
  const legend = configs.filter(function (config) { return state.activeConfigs.has(config); }).map(function (config) {
    return '<span class="history-legend-item"><i style="--series:' + seriesColors[configs.indexOf(config)] + '"></i>' + escapeHtml(configLabels[config]) + "</span>";
  }).join("");
  dom.trendChart.innerHTML = chartBand(documents, metas, benchmarkName, "size", "Binary size") + chartBand(documents, metas, benchmarkName, "wall", "Build wall time") + '<div class="history-legend">' + legend + "</div>";
}

function renderConfigFilter() {
  dom.configFilter.innerHTML = configs.map(function (config, index) {
    return '<button type="button" class="choice-button config-choice ' + (state.activeConfigs.has(config) ? "active" : "") + '" data-config="' + config + '" style="--series:' + seriesColors[index] + '">' + escapeHtml(compactConfigLabels[config]) + "</button>";
  }).join("");
}

async function refreshAll() {
  await Promise.all([renderTables(), renderComparisonSummary(), renderEnvironment(), renderTrend()]);
}

async function selectCommit(key) {
  if (!state.comparisonMode) return;
  const existing = state.selectedKeys.indexOf(key);
  if (existing >= 0) state.selectedKeys.splice(existing, 1);
  else if (state.selectedKeys.length < 2) state.selectedKeys.push(key);
  else state.selectedKeys = [state.selectedKeys[1], key];
  await refreshAll();
}

function clearSelection() {
  state.selectedKeys = [];
}

function attachEvents() {
  dom.filter.addEventListener("input", async function () {
    state.query = dom.filter.value;
    state.page = 1;
    clearSelection();
    await refreshAll();
  });
  dom.pageSize.addEventListener("change", async function () {
    state.pageSize = Number(dom.pageSize.value);
    state.page = 1;
    clearSelection();
    await refreshAll();
  });
  dom.pagination.addEventListener("click", async function (event) {
    const button = event.target.closest("button[data-page]");
    if (!button || button.disabled) return;
    state.page = Number(button.dataset.page);
    clearSelection();
    await refreshAll();
  });
  [dom.sizeGrid, dom.timeGrid].forEach(function (table) {
    table.addEventListener("click", function (event) {
      const button = event.target.closest("button.commit-select[data-run-key]");
      if (button) selectCommit(button.dataset.runKey);
    });
  });
  dom.compareToggle.addEventListener("click", async function () {
    state.comparisonMode = !state.comparisonMode;
    clearSelection();
    dom.compareToggle.setAttribute("aria-pressed", String(state.comparisonMode));
    dom.compareToggle.textContent = state.comparisonMode ? "Exit comparison" : "Compare commits";
    await refreshAll();
  });
  dom.clearComparison.addEventListener("click", async function () {
    clearSelection();
    await refreshAll();
  });
  dom.historyRange.addEventListener("change", renderTrend);
  dom.benchmarkSelect.addEventListener("change", function () {
    state.activeBenchmark = dom.benchmarkSelect.value;
    renderTrend();
  });
  dom.configFilter.addEventListener("click", function (event) {
    const button = event.target.closest("button[data-config]");
    if (!button) return;
    const config = button.dataset.config;
    if (state.activeConfigs.has(config) && state.activeConfigs.size > 1) state.activeConfigs.delete(config);
    else state.activeConfigs.add(config);
    renderConfigFilter();
    renderTrend();
  });
  let syncing = false;
  function syncScroll(source, target) {
    source.addEventListener("scroll", function () {
      if (syncing) return;
      syncing = true;
      target.scrollLeft = source.scrollLeft;
      requestAnimationFrame(function () { syncing = false; });
    });
  }
  syncScroll(dom.sizeWrap, dom.timeWrap);
  syncScroll(dom.timeWrap, dom.sizeWrap);
}

async function main() {
  try {
    const response = await fetch("data/index.json", { cache: "no-store" });
    if (!response.ok) throw new Error("Cannot load the run index");
    state.index = await response.json();
    if (!state.index.runs || !state.index.runs.length) throw new Error("No benchmark runs are available");
    state.benchmarkNames = sortedBenchmarkNames(state.index.benchmarkNames);
    if (!state.benchmarkNames.length) {
      state.benchmarkNames = benchmarkNamesFromDocuments([await loadRun(latestRun())]);
    }
    state.activeBenchmark = state.benchmarkNames[0] || "";
    configs.forEach(function (config) { state.activeConfigs.add(config); });
    dom.benchmarkSelect.innerHTML = state.benchmarkNames.map(function (name) { return '<option value="' + escapeHtml(name) + '">' + escapeHtml(name) + "</option>"; }).join("");
    dom.pageSize.value = String(state.pageSize);
    renderConfigFilter();
    attachEvents();
    await refreshAll();
    dom.status.textContent = "Updated " + dateLabel(state.index.generatedAt || latestRun().createdAt);
  } catch (error) {
    dom.status.textContent = error.message;
    dom.status.classList.add("error");
    dom.sizeGrid.innerHTML = '<tbody><tr><td class="empty-state">Unable to load benchmark history.</td></tr></tbody>';
  }
}

main();
