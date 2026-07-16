(function () {
  "use strict";

  var MIN_POINTS = 24;
  var MIN_RADIUS = 28;
  var MIN_LIVE_POINTS = 10;
  var MIN_LIVE_RADIUS = 16;
  var HUE_STEP = 6;
  var FX_DURATION = 3000;
  var FX_HARD_STOP = 4500;

  var canvas = document.getElementById("circle-canvas");
  var stage = document.getElementById("game-stage");
  var hud = document.getElementById("game-hud");
  var prompt = document.getElementById("game-prompt");
  var scoreEl = document.getElementById("game-score");
  var labelEl = document.getElementById("game-label");
  var actions = document.getElementById("game-actions");
  var tryAgainBtn = document.getElementById("try-again");
  var fxCanvas = document.getElementById("fx-canvas");

  if (!canvas || !stage) return;

  var ctx = canvas.getContext("2d");
  var fxCtx = fxCanvas ? fxCanvas.getContext("2d") : null;
  var dpr = 1;
  var width = 0;
  var height = 0;
  var points = [];
  var drawing = false;
  var scored = false;
  var fit = null;

  var particles = [];
  var fxRafId = null;
  var fxLastTs = null;
  var fxStartTs = null;
  var fxGeneration = 0;

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

    if (fxCanvas) {
      fxCanvas.width = Math.floor(width * dpr);
      fxCanvas.height = Math.floor(height * dpr);
      fxCanvas.style.width = width + "px";
      fxCanvas.style.height = height + "px";
      fxCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    render();
  }

  function clearHud() {
    hud.classList.remove("is-drawing");
    prompt.hidden = false;
    scoreEl.textContent = "";
    scoreEl.classList.remove("is-visible");
    scoreEl.style.color = "";
    labelEl.textContent = "";
    labelEl.classList.remove("is-visible");
    actions.classList.remove("is-visible");
    stopCelebration();
  }

  function reset() {
    stopCelebration();
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
    hud.classList.add("is-drawing");
    scoreEl.classList.add("is-visible");
    updateLiveScore();
    render();
  }

  function onPointerMove(event) {
    if (!drawing || scored) return;
    event.preventDefault();
    addPoint(getPoint(event));
    updateLiveScore();
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

  function computeCircleQuality(pts) {
    if (pts.length < 3) return null;

    var circle = fitCircle(pts);
    var roundness = roundnessScore(circle);
    var closure = closureScore(pts, circle.r);
    var coverage = coverageScore(pts, circle);

    var quality = roundness * 0.62 + closure * 0.18 + coverage * 0.2;
    quality = Math.pow(quality, 1.15);

    return { quality: quality, circle: circle };
  }

  function scoreFromQuality(quality) {
    return Math.round(clamp(quality * 100, 0, 100));
  }

  function liveScore(pts) {
    if (pts.length < MIN_LIVE_POINTS) return 0;
    var result = computeCircleQuality(pts);
    if (!result || result.circle.r < MIN_LIVE_RADIUS) return 0;
    return scoreFromQuality(result.quality);
  }

  function updateLiveScore() {
    var score = liveScore(points);
    scoreEl.textContent = String(score);
    scoreEl.style.color = colorForScore(score);
  }

  function scoreStroke(pts) {
    if (pts.length < MIN_POINTS) {
      return { score: 0, message: "Too short — draw a bigger circle." };
    }

    var result = computeCircleQuality(pts);
    if (result.circle.r < MIN_RADIUS) {
      return { score: 0, message: "Circle too small — use more of the screen." };
    }

    var score = scoreFromQuality(result.quality);

    return {
      score: score,
      message: messageForScore(score),
      circle: result.circle
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

    hud.classList.remove("is-drawing");
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

    if (result.circle) {
      triggerCelebration(result.score);
    }
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

    ctx.lineWidth = 4;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";

    for (var i = 1; i < points.length; i++) {
      ctx.beginPath();
      ctx.moveTo(points[i - 1].x, points[i - 1].y);
      ctx.lineTo(points[i].x, points[i].y);
      ctx.strokeStyle = "hsl(" + ((i * HUE_STEP) % 360) + ", 85%, 65%)";
      ctx.stroke();
    }
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

  function stopCelebration() {
    fxGeneration++;
    if (fxRafId !== null) {
      cancelAnimationFrame(fxRafId);
      fxRafId = null;
    }
    particles = [];
    if (fxCtx) fxCtx.clearRect(0, 0, width, height);
  }

  function spawnFirework(x, y, hueBase, count) {
    for (var i = 0; i < count; i++) {
      var angle = Math.random() * Math.PI * 2;
      var speed = 60 + Math.random() * 140;
      particles.push({
        type: "spark",
        x: x, y: y, px: x, py: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        hue: (hueBase + (Math.random() - 0.5) * 50 + 360) % 360,
        size: 1.5 + Math.random() * 2,
        life: 0,
        maxLife: 900 + Math.random() * 500
      });
    }
  }

  function spawnBalloon(x, hue) {
    var rx = 18 + Math.random() * 6;
    particles.push({
      type: "balloon",
      x: x, y: height + 30,
      rx: rx, ry: rx * 1.25,
      vy: -(30 + Math.random() * 25),
      hue: hue,
      swayPhase: Math.random() * Math.PI * 2,
      swaySpeed: 1.2 + Math.random() * 1.0,
      swayAmp: 8 + Math.random() * 10,
      life: 0,
      maxLife: 3200 + Math.random() * 1400,
      popTargetY: height * (0.12 + Math.random() * 0.15),
      popped: false
    });
  }

  function drawBalloon(p) {
    fxCtx.save();
    fxCtx.translate(p.x, p.y);
    fxCtx.fillStyle = "hsla(" + p.hue + ", 80%, 65%, 0.9)";
    fxCtx.beginPath();
    fxCtx.ellipse(0, 0, p.rx, p.ry, 0, 0, Math.PI * 2);
    fxCtx.fill();
    fxCtx.beginPath();
    fxCtx.moveTo(-3, p.ry);
    fxCtx.lineTo(3, p.ry);
    fxCtx.lineTo(0, p.ry + 6);
    fxCtx.closePath();
    fxCtx.fill();
    fxCtx.strokeStyle = "rgba(255,255,255,0.35)";
    fxCtx.lineWidth = 1;
    fxCtx.beginPath();
    fxCtx.moveTo(0, p.ry + 6);
    fxCtx.lineTo(Math.sin(p.swayPhase * 0.6) * 4, p.ry + 26);
    fxCtx.stroke();
    fxCtx.restore();
  }

  function fxTick(timestamp) {
    if (fxStartTs === null) fxStartTs = timestamp;
    var dt = fxLastTs === null ? 16 : Math.min(timestamp - fxLastTs, 48);
    fxLastTs = timestamp;
    var dtSec = dt / 1000;
    var elapsed = timestamp - fxStartTs;

    fxCtx.clearRect(0, 0, width, height);

    var next = [];
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.life += dt;

      if (p.type === "spark") {
        p.px = p.x; p.py = p.y;
        p.vy += 220 * dtSec;
        p.x += p.vx * dtSec;
        p.y += p.vy * dtSec;
        var alpha = clamp(1 - p.life / p.maxLife, 0, 1);
        if (alpha > 0 && p.life < p.maxLife) {
          fxCtx.strokeStyle = "hsla(" + p.hue + ", 90%, 60%, " + alpha + ")";
          fxCtx.lineWidth = p.size;
          fxCtx.beginPath();
          fxCtx.moveTo(p.px, p.py);
          fxCtx.lineTo(p.x, p.y);
          fxCtx.stroke();
          next.push(p);
        }
      } else if (p.type === "balloon") {
        if (!p.popped) {
          p.swayPhase += p.swaySpeed * dtSec;
          p.y += p.vy * dtSec;
          p.x += Math.sin(p.swayPhase) * p.swayAmp * dtSec;
          if (p.y <= p.popTargetY || p.life >= p.maxLife) {
            p.popped = true;
            spawnFirework(p.x, p.y, p.hue, 10);
          } else {
            drawBalloon(p);
            next.push(p);
          }
        }
      }
    }
    particles = next;

    if (elapsed < FX_HARD_STOP && (elapsed < FX_DURATION || particles.length > 0)) {
      fxRafId = requestAnimationFrame(fxTick);
    } else {
      stopCelebration();
    }
  }

  function triggerCelebration(score) {
    if (!fxCtx) return;
    stopCelebration();
    var myGeneration = fxGeneration;

    var intensity = clamp(score / 100, 0.25, 1);
    var burstCount = Math.round(3 + intensity * 5);
    var balloonCount = Math.round(4 + intensity * 8);

    for (var i = 0; i < burstCount; i++) {
      (function (index) {
        setTimeout(function () {
          if (myGeneration !== fxGeneration) return;
          spawnFirework(
            width * (0.2 + Math.random() * 0.6),
            height * (0.15 + Math.random() * 0.35),
            Math.random() * 360,
            18 + Math.round(intensity * 22)
          );
        }, index * 220 + Math.random() * 150);
      })(i);
    }

    for (var j = 0; j < balloonCount; j++) {
      spawnBalloon(Math.random() * width, Math.random() * 360);
    }

    fxStartTs = null;
    fxLastTs = null;
    fxRafId = requestAnimationFrame(fxTick);
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
