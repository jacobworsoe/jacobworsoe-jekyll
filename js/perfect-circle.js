(function () {
  "use strict";

  var MIN_POINTS = 24;
  var MIN_RADIUS = 28;

  var canvas = document.getElementById("circle-canvas");
  var stage = document.getElementById("game-stage");
  var hud = document.getElementById("game-hud");
  var prompt = document.getElementById("game-prompt");
  var scoreEl = document.getElementById("game-score");
  var labelEl = document.getElementById("game-label");
  var actions = document.getElementById("game-actions");
  var tryAgainBtn = document.getElementById("try-again");

  if (!canvas || !stage) return;

  var ctx = canvas.getContext("2d");
  var dpr = 1;
  var width = 0;
  var height = 0;
  var points = [];
  var drawing = false;
  var scored = false;
  var fit = null;

  var strokeColor = "#5bb1ed";
  var idealColor = "rgba(147, 218, 138, 0.55)";
  var guideColor = "rgba(255, 255, 255, 0.08)";

  function resize() {
    var rect = stage.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 3);
    width = Math.max(1, Math.floor(rect.width));
    height = Math.max(1, Math.floor(rect.height));
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    render();
  }

  function clearHud() {
    hud.classList.remove("is-hidden");
    prompt.hidden = false;
    scoreEl.textContent = "";
    scoreEl.classList.remove("is-visible");
    labelEl.textContent = "";
    labelEl.classList.remove("is-visible");
    actions.classList.remove("is-visible");
  }

  function reset() {
    points = [];
    drawing = false;
    scored = false;
    fit = null;
    clearHud();
    render();
  }

  function getPoint(event) {
    var rect = canvas.getBoundingClientRect();
    var source = event.touches ? event.touches[0] : event;
    return {
      x: source.clientX - rect.left,
      y: source.clientY - rect.top
    };
  }

  function addPoint(point) {
    var last = points[points.length - 1];
    if (last) {
      var dx = point.x - last.x;
      var dy = point.y - last.y;
      if (dx * dx + dy * dy < 4) return;
    }
    points.push(point);
  }

  function onPointerDown(event) {
    if (scored) return;
    event.preventDefault();
    drawing = true;
    points = [getPoint(event)];
    hud.classList.add("is-hidden");
    render();
  }

  function onPointerMove(event) {
    if (!drawing || scored) return;
    event.preventDefault();
    addPoint(getPoint(event));
    render();
  }

  function onPointerUp(event) {
    if (!drawing || scored) return;
    event.preventDefault();
    drawing = false;
    finishStroke();
  }

  function fitCircle(pts) {
    var n = pts.length;
    var sumX = 0;
    var sumY = 0;

    for (var i = 0; i < n; i++) {
      sumX += pts[i].x;
      sumY += pts[i].y;
    }

    var cx = sumX / n;
    var cy = sumY / n;
    var radii = [];
    var sumR = 0;

    for (var j = 0; j < n; j++) {
      var r = Math.hypot(pts[j].x - cx, pts[j].y - cy);
      radii.push(r);
      sumR += r;
    }

    var avgR = sumR / n;
    return { cx: cx, cy: cy, r: avgR, radii: radii };
  }

  function closureScore(pts, radius) {
    var first = pts[0];
    var last = pts[pts.length - 1];
    var gap = Math.hypot(first.x - last.x, first.y - last.y);
    var tolerance = Math.max(18, radius * 0.35);
    return clamp(1 - gap / tolerance, 0, 1);
  }

  function coverageScore(pts, circle) {
    var angles = pts.map(function (p) {
      return Math.atan2(p.y - circle.cy, p.x - circle.cx);
    });
    angles.sort(function (a, b) { return a - b; });

    var maxGap = 0;
    for (var i = 0; i < angles.length; i++) {
      var next = angles[(i + 1) % angles.length];
      var current = angles[i];
      var gap = next - current;
      if (i === angles.length - 1) gap += Math.PI * 2;
      if (gap > maxGap) maxGap = gap;
    }

    var covered = Math.PI * 2 - maxGap;
    return clamp(covered / (Math.PI * 2), 0, 1);
  }

  function roundnessScore(circle) {
    var radii = circle.radii;
    var mean = circle.r;
    if (mean <= 0) return 0;

    var variance = 0;
    for (var i = 0; i < radii.length; i++) {
      var diff = radii[i] - mean;
      variance += diff * diff;
    }
    variance /= radii.length;

    var cv = Math.sqrt(variance) / mean;
    return clamp(Math.exp(-cv * 4.8), 0, 1);
  }

  function clamp(value, min, max) {
    return Math.min(max, Math.max(min, value));
  }

  function scoreStroke(pts) {
    if (pts.length < MIN_POINTS) {
      return { score: 1, message: "Too short — draw a bigger circle." };
    }

    var circle = fitCircle(pts);
    if (circle.r < MIN_RADIUS) {
      return { score: 1, message: "Circle too small — use more of the screen." };
    }

    var roundness = roundnessScore(circle);
    var closure = closureScore(pts, circle.r);
    var coverage = coverageScore(pts, circle);

    var quality = roundness * 0.62 + closure * 0.18 + coverage * 0.2;
    quality = Math.pow(quality, 1.15);
    var score = Math.round(clamp(1 + quality * 99, 1, 100));

    return {
      score: score,
      message: messageForScore(score),
      circle: circle
    };
  }

  function messageForScore(score) {
    if (score >= 97) return "Impossibly round!";
    if (score >= 90) return "Excellent circle!";
    if (score >= 75) return "Pretty good!";
    if (score >= 55) return "Not bad — keep practicing.";
    if (score >= 35) return "A bit wobbly.";
    return "That was… creative.";
  }

  function colorForScore(score) {
    if (score >= 90) return "#93da8a";
    if (score >= 70) return "#5bb1ed";
    if (score >= 45) return "#ffafaf";
    return "#ff9465";
  }

  function finishStroke() {
    var result = scoreStroke(points);
    scored = true;
    fit = result.circle || null;

    render();

    hud.classList.remove("is-hidden");
    prompt.hidden = true;
    scoreEl.textContent = String(result.score);
    scoreEl.style.color = colorForScore(result.score);
    labelEl.textContent = result.message;

    if (navigator.vibrate) {
      navigator.vibrate(result.score >= 75 ? [20, 40, 20] : 20);
    }

    requestAnimationFrame(function () {
      scoreEl.classList.add("is-visible");
      labelEl.classList.add("is-visible");
      actions.classList.add("is-visible");
    });
  }

  function drawGuide() {
    var size = Math.min(width, height);
    var cx = width / 2;
    var cy = height / 2;
    var r = size * 0.34;

    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.strokeStyle = guideColor;
    ctx.lineWidth = 2;
    ctx.setLineDash([6, 10]);
    ctx.stroke();
    ctx.setLineDash([]);
  }

  function drawStroke() {
    if (points.length < 2) return;

    ctx.beginPath();
    ctx.moveTo(points[0].x, points[0].y);
    for (var i = 1; i < points.length; i++) {
      ctx.lineTo(points[i].x, points[i].y);
    }
    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = 4;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.stroke();
  }

  function drawIdeal() {
    if (!fit) return;

    ctx.beginPath();
    ctx.arc(fit.cx, fit.cy, fit.r, 0, Math.PI * 2);
    ctx.strokeStyle = idealColor;
    ctx.lineWidth = 3;
    ctx.stroke();
  }

  function render() {
    ctx.clearRect(0, 0, width, height);
    drawGuide();
    drawStroke();
    if (scored) drawIdeal();
  }

  canvas.addEventListener("mousedown", onPointerDown);
  canvas.addEventListener("mousemove", onPointerMove);
  window.addEventListener("mouseup", onPointerUp);

  canvas.addEventListener("touchstart", onPointerDown, { passive: false });
  canvas.addEventListener("touchmove", onPointerMove, { passive: false });
  canvas.addEventListener("touchend", onPointerUp, { passive: false });
  canvas.addEventListener("touchcancel", onPointerUp, { passive: false });

  tryAgainBtn.addEventListener("click", reset);
  window.addEventListener("resize", resize);
  window.addEventListener("orientationchange", function () {
    setTimeout(resize, 100);
  });

  resize();
})();
