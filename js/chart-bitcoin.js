(function() {
  var canvas = document.getElementById("bitcoinChart");
  if (!canvas) return;
  if (canvas.dataset.chartInitialized) return;
  canvas.dataset.chartInitialized = "1";

  var API_URL = "https://api.blockchain.info/charts/market-price?timespan=1years&rollingAverage=24hours&format=json&cors=true";
  var CHART_JS_SRC = "/assets/js/chart.umd.js";
  var FETCH_TIMEOUT_MS = 10000;

  var container = canvas.closest(".bitcoin-chart-wrapper") || canvas.parentNode;
  var dateFormatter = new Intl.DateTimeFormat("da-DK", { day: "2-digit", month: "2-digit" });
  var numberFormatter = new Intl.NumberFormat("da-DK", { maximumFractionDigits: 2 });
  var axisFormatter = new Intl.NumberFormat("da-DK");

  function loadChartJs() {
    if (window.Chart) return Promise.resolve(window.Chart);
    return new Promise(function(resolve, reject) {
      var existing = document.querySelector('script[data-chartjs-loader="1"]');
      if (existing) {
        existing.addEventListener("load", function() { resolve(window.Chart); });
        existing.addEventListener("error", function() { reject(new Error("Chart.js failed to load")); });
        return;
      }
      var s = document.createElement("script");
      s.src = CHART_JS_SRC;
      s.async = true;
      s.dataset.chartjsLoader = "1";
      s.onload = function() { resolve(window.Chart); };
      s.onerror = function() { reject(new Error("Chart.js failed to load")); };
      document.head.appendChild(s);
    });
  }

  function fetchBitcoinData() {
    var controller = typeof AbortController !== "undefined" ? new AbortController() : null;
    var timeoutId = setTimeout(function() {
      if (controller) controller.abort();
    }, FETCH_TIMEOUT_MS);

    var fetchOpts = controller ? { signal: controller.signal } : {};
    return fetch(API_URL, fetchOpts).then(function(response) {
      clearTimeout(timeoutId);
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    }).then(function(data) {
      if (!data || !Array.isArray(data.values) || data.values.length === 0) {
        throw new Error("No data");
      }
      var rows = [];
      for (var i = 0; i < data.values.length; i++) {
        var row = data.values[i];
        if (row && isFinite(row.x) && isFinite(row.y)) rows.push(row);
      }
      if (rows.length === 0) throw new Error("No valid rows");
      return rows;
    });
  }

  function populateA11yTable(rows) {
    var tbody = container.querySelector(".bitcoin-chart-data tbody");
    if (!tbody) return;
    var html = "";
    for (var i = 0; i < rows.length; i++) {
      var d = new Date(rows[i].x * 1000);
      html += "<tr><td>" + dateFormatter.format(d) + "</td><td>" + numberFormatter.format(rows[i].y) + "</td></tr>";
    }
    tbody.innerHTML = html;
  }

  function renderChart(rows) {
    var skeleton = container.querySelector(".bitcoin-chart-skeleton");
    if (skeleton) skeleton.parentNode.removeChild(skeleton);

    var labels = [];
    var values = [];
    for (var i = 0; i < rows.length; i++) {
      labels.push(dateFormatter.format(new Date(rows[i].x * 1000)));
      values.push(rows[i].y);
    }

    populateA11yTable(rows);

    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { ticks: { autoSkip: true, maxTicksLimit: 12 } },
        y: { ticks: { callback: function(v) { return axisFormatter.format(v); } } }
      }
    };
    if (reduceMotion) chartOptions.animation = false;

    new window.Chart(canvas.getContext("2d"), {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: "Bitcoin værdi i USD",
          backgroundColor: "rgba(88, 147, 178, 0.3)",
          borderColor: "rgb(88, 147, 178)",
          data: values,
          fill: true,
          tension: 0.1,
          pointRadius: 0
        }]
      },
      options: chartOptions
    });
  }

  function renderError(err) {
    if (window.console && console.warn) console.warn("[bitcoin-chart]", err);
    var skeleton = container.querySelector(".bitcoin-chart-skeleton");
    if (skeleton) skeleton.parentNode.removeChild(skeleton);
    canvas.style.display = "none";
    var p = document.createElement("p");
    p.className = "bitcoin-chart-error";
    p.textContent = "Live Bitcoin data er ikke tilgængelig lige nu — prøv at genindlæse siden.";
    container.appendChild(p);
  }

  Promise.all([loadChartJs(), fetchBitcoinData()]).then(function(results) {
    renderChart(results[1]);
  }).catch(renderError);
})();
