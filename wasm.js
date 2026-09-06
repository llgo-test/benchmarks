const wasmState = {
  index: null,
  runs: new Map(),
  applications: [],
  activeApplication: "",
  activeCompilers: new Set(["Go", "TinyGo", "LLGo"]),
  page: 1,
  pageSize: 8,
  query: "",
};

const wasmCompilers = ["Go", "TinyGo", "LLGo"];
const wasmCompilerColors = ["#64748b", "#7c3aed", "#2457d6"];
const wasmDom = {
  status: document.querySelector("#wasm-status"),
  sizeGrid: document.querySelector("#wasm-size-grid"),
  filter: document.querySelector("#wasm-commit-filter"),
  pageSize: document.querySelector("#wasm-page-size"),
  commitCount: document.querySelector("#wasm-commit-count"),
  pagination: document.querySelector("#wasm-pagination"),
  historyRange: document.querySelector("#wasm-history-range"),
  applicationSelect: document.querySelector("#wasm-application-select"),
  compilerFilter: document.querySelector("#wasm-compiler-filter"),
  trendChart: document.querySelector("#wasm-trend-chart"),
  runner: document.querySelector("#wasm-runner"),
  toolchains: document.querySelector("#wasm-toolchains"),
  llgo: document.querySelector("#wasm-llgo"),
  protocol: document.querySelector("#wasm-protocol"),
  workflow: document.querySelector("#wasm-workflow"),
  raw: document.querySelector("#wasm-raw"),
  tsv: document.querySelector("#wasm-tsv"),
};

function wasmEscape(value) {
  return String(value == null ? "" : value).replace(/[&<>"']/g, function (character) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character];
  });
}

function wasmFormatBytes(value) {
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

function wasmPercent(value) {
  if (!Number.isFinite(value)) return "—";
  return (value > 0 ? "+" : "") + value.toFixed(1) + "%";
}

function wasmPercentDelta(value, baseline) {
  const current = Number(value);
  const reference = Number(baseline);
  if (!Number.isFinite(current) || !Number.isFinite(reference) || reference === 0) return NaN;
  return (current / reference - 1) * 100;
}

function wasmDeltaClass(value) {
  return value > 0 ? "bad" : value < 0 ? "good" : "flat";
}

function wasmShortSha(value) {
  return value ? String(value).slice(0, 10) : "—";
}

function wasmDate(value, short) {
  if (!value) return "unknown";
  const options = short ? { month: "short", day: "numeric", year: "2-digit" } : { dateStyle: "medium", timeStyle: "short" };
  return new Date(value).toLocaleString(undefined, options);
}

function wasmSafeUrl(value) {
  const url = String(value || "");
  return /^https:\/\/github\.com\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\/(actions\/runs\/[0-9]+|commit\/[0-9a-fA-F]{40})$/.test(url) ? url : "";
}

function wasmSetLink(element, href) {
  if (href) {
    element.href = href;
    element.hidden = false;
  } else {
    element.removeAttribute("href");
    element.hidden = true;
  }
}

function wasmCommitUrl(run) {
  const repository = String(run.llgoRepository || "");
  const commit = String(run.llgoCommit || "");
  return wasmSafeUrl("https://github.com/" + repository + "/commit/" + commit);
}

function wasmCommitLabel(run) {
  return wasmShortSha(run.llgoCommit || run.key);
}

function wasmRunAsset(run) {
  const version = [run.id || run.key, run.attempt || 1, run.createdAt || ""].map(String).join("-");
  return "data/" + run.path + "?v=" + encodeURIComponent(version);
}

async function wasmLoadRun(run) {
  if (!run) return null;
  if (!wasmState.runs.has(run.key)) {
    wasmState.runs.set(run.key, (async function () {
      const response = await fetch(wasmRunAsset(run));
      if (!response.ok) throw new Error("Could not load " + run.path + " (HTTP " + response.status + ")");
      return response.json();
    })());
  }
  return wasmState.runs.get(run.key);
}

function wasmBenchmarkMap(documentData) {
  return new Map(((documentData && documentData.benchmarks) || []).map(function (benchmark) {
    return [benchmark.id || benchmark.command, benchmark];
  }));
}

function wasmValue(benchmark, compiler) {
  return Number(benchmark && benchmark.values && benchmark.values[compiler]);
}

function wasmFilteredRuns() {
  const query = wasmState.query.trim().toLowerCase();
  const runs = (wasmState.index && wasmState.index.runs) || [];
  if (!query) return runs;
  return runs.filter(function (run) {
    return [run.llgoCommit, run.sourceCommit, run.ref, run.createdAt, run.llgoCommittedAt, run.key]
      .some(function (value) { return String(value || "").toLowerCase().includes(query); });
  });
}

function wasmCurrentPageRuns() {
  const runs = wasmFilteredRuns();
  const pageCount = Math.max(1, Math.ceil(runs.length / wasmState.pageSize));
  wasmState.page = Math.min(Math.max(1, wasmState.page), pageCount);
  const start = (wasmState.page - 1) * wasmState.pageSize;
  return runs.slice(start, start + wasmState.pageSize);
}

function wasmPageNumbers(page, pageCount) {
  const values = new Set([1, pageCount, page - 1, page, page + 1]);
  return Array.from(values).filter(function (value) { return value >= 1 && value <= pageCount; }).sort(function (a, b) { return a - b; });
}

function wasmRenderPagination() {
  const runs = wasmFilteredRuns();
  const pageCount = Math.max(1, Math.ceil(runs.length / wasmState.pageSize));
  wasmState.page = Math.min(wasmState.page, pageCount);
  wasmDom.commitCount.textContent = runs.length + " commit" + (runs.length === 1 ? "" : "s") + " · page " + wasmState.page + "/" + pageCount;
  const numbers = wasmPageNumbers(wasmState.page, pageCount);
  let previous = 0;
  const buttons = ['<button type="button" data-page="' + (wasmState.page - 1) + '"' + (wasmState.page === 1 ? " disabled" : "") + '>←</button>'];
  numbers.forEach(function (page) {
    if (previous && page - previous > 1) buttons.push('<span class="page-gap">…</span>');
    buttons.push('<button type="button" data-page="' + page + '" class="' + (page === wasmState.page ? "active" : "") + '">' + page + "</button>");
    previous = page;
  });
  buttons.push('<button type="button" data-page="' + (wasmState.page + 1) + '"' + (wasmState.page === pageCount ? " disabled" : "") + '>→</button>');
  wasmDom.pagination.innerHTML = buttons.join("");
}

function wasmHeaderHtml(run) {
  const label = "<code>" + wasmEscape(wasmCommitLabel(run)) + "</code>";
  const url = wasmCommitUrl(run);
  const commit = url ? '<a class="commit-link" href="' + wasmEscape(url) + '" title="Open LLGo commit">' + label + "</a>" : label;
  return '<th class="commit-header"><div class="commit-header-content">' + commit + '<span class="commit-date">' + wasmEscape(wasmDate(run.llgoCommittedAt || run.createdAt, true)) + "</span></div></th>";
}

function wasmRank(benchmark, compiler) {
  const value = wasmValue(benchmark, compiler);
  if (!Number.isFinite(value)) return null;
  const values = wasmCompilers.map(function (name) { return wasmValue(benchmark, name); }).filter(Number.isFinite);
  const unique = Array.from(new Set(values)).sort(function (a, b) { return a - b; });
  const rank = unique.indexOf(value) + 1;
  const ties = values.filter(function (candidate) { return candidate === value; }).length;
  const tone = rank === 1 ? "rank-best" : rank === unique.length ? "rank-worst" : "rank-mid";
  return { rank: rank, ties: ties, tone: tone };
}

function wasmCellHtml(benchmark, compiler) {
  const value = wasmValue(benchmark, compiler);
  if (!Number.isFinite(value)) return '<td class="matrix-cell missing">—</td>';
  const rank = wasmRank(benchmark, compiler);
  const goValue = wasmValue(benchmark, "Go");
  const delta = compiler === "Go" ? 0 : wasmPercentDelta(value, goValue);
  const context = compiler === "Go"
    ? '<span class="comparison-context flat">Go reference</span>'
    : '<span class="comparison-context ' + wasmDeltaClass(delta) + '">' + wasmPercent(delta) + " vs Go</span>";
  return '<td class="matrix-cell ' + rank.tone + '"><span class="rank-number">#' + rank.rank + (rank.ties > 1 ? "=" : "") + "</span><strong>" + wasmFormatBytes(value) + '</strong><span class="secondary-value">' + value.toLocaleString() + " B</span>" + context + "</td>";
}

async function wasmRenderTable() {
  wasmRenderPagination();
  const runs = wasmCurrentPageRuns();
  const documents = await Promise.all(runs.map(wasmLoadRun));
  const maps = documents.map(wasmBenchmarkMap);
  const head = '<thead><tr><th class="matrix-label-cell">Application / compiler</th>' + runs.map(wasmHeaderHtml).join("") + "</tr></thead>";
  const rows = [];
  wasmState.applications.forEach(function (application) {
    wasmCompilers.forEach(function (compiler, compilerIndex) {
      const name = compilerIndex === 0 ? '<span class="benchmark-name">' + wasmEscape(application.command) + "</span>" : "";
      const source = compilerIndex === 0 ? '<span class="wasm-source-name">' + wasmEscape(application.provenance || application.kind || "") + "</span>" : "";
      const configClass = compilerIndex === 0 ? "config-name" : "config-name config-continuation";
      const label = '<th class="matrix-label-cell" aria-label="' + wasmEscape(application.command + " · " + compiler) + '">' + name + '<span class="' + configClass + '">' + wasmEscape(compiler) + "</span>" + source + "</th>";
      const cells = maps.map(function (map) { return wasmCellHtml(map.get(application.id), compiler); }).join("");
      rows.push('<tr class="' + (compilerIndex === 0 ? "benchmark-group-start" : "") + '">' + label + cells + "</tr>");
    });
  });
  wasmDom.sizeGrid.style.minWidth = (156 + runs.length * 132) + "px";
  wasmDom.sizeGrid.innerHTML = head + "<tbody>" + (rows.length ? rows.join("") : '<tr><td class="empty-state">No WASM application data.</td></tr>') + "</tbody>";
}

function wasmChartRuns() {
  const limit = Number(wasmDom.historyRange.value);
  const newest = limit > 0 ? wasmState.index.runs.slice(0, limit) : wasmState.index.runs.slice();
  return newest.reverse();
}

function wasmChartHtml(documents, runs, applicationId) {
  const width = 1120;
  const height = 265;
  const margin = { top: 17, right: 18, bottom: 32, left: 80 };
  const plotWidth = width - margin.left - margin.right;
  const plotHeight = height - margin.top - margin.bottom;
  const maps = documents.map(wasmBenchmarkMap);
  const selected = wasmCompilers.filter(function (compiler) { return wasmState.activeCompilers.has(compiler); });
  const series = selected.map(function (compiler) {
    return { compiler: compiler, values: maps.map(function (map) { return wasmValue(map.get(applicationId), compiler); }) };
  });
  const finite = series.flatMap(function (item) { return item.values.filter(Number.isFinite); });
  if (!finite.length) return '<div class="chart-band"><div class="empty-state">No binary-size history for this application and compiler selection.</div></div>';
  let minimum = Math.min.apply(null, finite);
  let maximum = Math.max.apply(null, finite);
  const padding = (maximum - minimum || Math.abs(maximum) * .1 || 1) * .09;
  minimum = Math.max(0, minimum - padding);
  maximum += padding;
  const x = function (index) { return margin.left + (runs.length <= 1 ? plotWidth / 2 : index * plotWidth / (runs.length - 1)); };
  const y = function (value) { return margin.top + (maximum - value) * plotHeight / (maximum - minimum); };
  const parts = [];
  for (let tick = 0; tick <= 4; tick++) {
    const value = maximum - (maximum - minimum) * tick / 4;
    const py = margin.top + plotHeight * tick / 4;
    parts.push('<line class="chart-grid-line" x1="' + margin.left + '" y1="' + py + '" x2="' + (width - margin.right) + '" y2="' + py + '"></line>');
    parts.push('<text class="chart-axis-label" x="' + (margin.left - 8) + '" y="' + (py + 3) + '" text-anchor="end">' + wasmEscape(wasmFormatBytes(value)) + "</text>");
  }
  const labelStep = Math.max(1, Math.ceil(runs.length / 8));
  runs.forEach(function (run, index) {
    if (index % labelStep !== 0 && index !== runs.length - 1) return;
    const text = '<text class="chart-axis-label" x="' + x(index) + '" y="' + (height - 9) + '" text-anchor="middle">' + wasmEscape(wasmCommitLabel(run).slice(0, 7)) + "</text>";
    const url = wasmCommitUrl(run);
    parts.push(url ? '<a class="chart-commit-link" href="' + wasmEscape(url) + '">' + text + "</a>" : text);
  });
  series.forEach(function (item) {
    const color = wasmCompilerColors[wasmCompilers.indexOf(item.compiler)];
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
      const title = wasmEscape(item.compiler + " · " + wasmCommitLabel(runs[index]) + " · " + wasmFormatBytes(value));
      const point = '<circle class="history-point" fill="' + color + '" cx="' + x(index) + '" cy="' + y(value) + '" r="3"><title>' + title + "</title></circle>";
      const url = wasmCommitUrl(runs[index]);
      parts.push(url ? '<a class="history-point-link" href="' + wasmEscape(url) + '">' + point + "</a>" : point);
    });
  });
  return '<div class="chart-band"><div class="chart-title"><span>Final module size</span><span>bytes</span></div><svg viewBox="0 0 ' + width + " " + height + '" role="img" aria-label="WASM binary-size trend">' + parts.join("") + "</svg></div>";
}

async function wasmRenderTrend() {
  const runs = wasmChartRuns();
  const documents = await Promise.all(runs.map(wasmLoadRun));
  const legend = wasmCompilers.filter(function (compiler) { return wasmState.activeCompilers.has(compiler); }).map(function (compiler) {
    const color = wasmCompilerColors[wasmCompilers.indexOf(compiler)];
    return '<span class="history-legend-item"><i style="--series:' + color + '"></i>' + wasmEscape(compiler) + "</span>";
  }).join("");
  wasmDom.trendChart.innerHTML = wasmChartHtml(documents, runs, wasmState.activeApplication) + '<div class="history-legend">' + legend + "</div>";
}

function wasmRenderCompilerFilter() {
  wasmDom.compilerFilter.innerHTML = wasmCompilers.map(function (compiler, index) {
    return '<button type="button" class="choice-button config-choice ' + (wasmState.activeCompilers.has(compiler) ? "active" : "") + '" data-compiler="' + compiler + '" style="--series:' + wasmCompilerColors[index] + '">' + compiler + "</button>";
  }).join("");
}

function wasmNormalizeRunner(run) {
  let image = run.runnerImage || "Ubuntu 24.04";
  image = String(image).replace(/^ubuntu(\d{2})$/i, "Ubuntu $1.04");
  const arch = String(run.runnerArch || "x86_64").replace(/^X64$/i, "x86_64");
  return image + " · " + arch;
}

async function wasmRenderEnvironment() {
  const latest = wasmState.index.runs[0];
  const documentData = await wasmLoadRun(latest);
  const run = documentData.run || {};
  wasmDom.runner.textContent = wasmNormalizeRunner(run);
  wasmDom.toolchains.textContent = "Go " + (run.goVersion || latest.goVersion || "—") + " · TinyGo " + (run.tinygoVersion || latest.tinygoVersion || "—") + " · LLVM " + (run.llvmVersion || latest.llvmVersion || "—");
  wasmDom.llgo.textContent = wasmCommitLabel(latest) + " · " + (run.llgoRepository || latest.llgoRepository || "unknown");
  wasmDom.protocol.textContent = "wasip1/wasm · final .wasm bytes";
  const rawPath = "data/" + latest.path;
  wasmSetLink(wasmDom.workflow, wasmSafeUrl(run.workflowUrl || latest.workflowUrl));
  wasmSetLink(wasmDom.raw, rawPath);
  wasmSetLink(wasmDom.tsv, rawPath.replace(/results\.json$/, "sizes.tsv"));
}

async function wasmRefresh() {
  await Promise.all([wasmRenderTable(), wasmRenderTrend(), wasmRenderEnvironment()]);
  wasmDom.status.classList.remove("error");
  wasmDom.status.textContent = wasmState.index.runs.length + " revisions · " + wasmState.applications.length + " applications";
}

function wasmRenderEmpty(message) {
  wasmDom.status.classList.add("error");
  wasmDom.status.textContent = "No published data";
  wasmDom.sizeGrid.innerHTML = '<tbody><tr><td class="empty-state">' + wasmEscape(message) + "</td></tr></tbody>";
  wasmDom.trendChart.innerHTML = '<div class="empty-state">' + wasmEscape(message) + "</div>";
}

async function wasmInitialize() {
  try {
    const response = await fetch("data/wasm/index.json", { cache: "no-store" });
    if (response.status === 404) {
      wasmRenderEmpty("The WASM benchmark has not published its first run yet.");
      return;
    }
    if (!response.ok) throw new Error("Could not load the WASM run index (HTTP " + response.status + ")");
    wasmState.index = await response.json();
    if (!(wasmState.index.runs || []).length) {
      wasmRenderEmpty("The WASM benchmark has not published its first run yet.");
      return;
    }
    const latest = await wasmLoadRun(wasmState.index.runs[0]);
    wasmState.applications = latest.benchmarks || [];
    wasmState.activeApplication = wasmState.applications.length ? wasmState.applications[0].id : "";
    wasmDom.applicationSelect.innerHTML = wasmState.applications.map(function (application) {
      return '<option value="' + wasmEscape(application.id) + '">' + wasmEscape(application.command + " · " + application.kind) + "</option>";
    }).join("");
    wasmRenderCompilerFilter();
    await wasmRefresh();
  } catch (error) {
    wasmRenderEmpty(error.message || String(error));
  }
}

wasmDom.filter.addEventListener("input", function () {
  wasmState.query = wasmDom.filter.value;
  wasmState.page = 1;
  wasmRenderTable().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmDom.pageSize.addEventListener("change", function () {
  wasmState.pageSize = Number(wasmDom.pageSize.value);
  wasmState.page = 1;
  wasmRenderTable().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmDom.pagination.addEventListener("click", function (event) {
  const button = event.target.closest("button[data-page]");
  if (!button || button.disabled) return;
  wasmState.page = Number(button.dataset.page);
  wasmRenderTable().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmDom.historyRange.addEventListener("change", function () {
  wasmRenderTrend().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmDom.applicationSelect.addEventListener("change", function () {
  wasmState.activeApplication = wasmDom.applicationSelect.value;
  wasmRenderTrend().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmDom.compilerFilter.addEventListener("click", function (event) {
  const button = event.target.closest("button[data-compiler]");
  if (!button) return;
  const compiler = button.dataset.compiler;
  if (wasmState.activeCompilers.has(compiler)) wasmState.activeCompilers.delete(compiler);
  else wasmState.activeCompilers.add(compiler);
  wasmRenderCompilerFilter();
  wasmRenderTrend().catch(function (error) { wasmRenderEmpty(error.message || String(error)); });
});

wasmInitialize();
