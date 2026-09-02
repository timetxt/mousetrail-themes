/* Live Classic Rainbow cursor-trail demo — ported from the MouseTrail app's
   own rainbow-mode renderer, matching the shipped app's physics. */
(function () {
  var canvas = document.getElementById('trail');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  function resize() { canvas.width = innerWidth; canvas.height = innerHeight; }
  resize();
  addEventListener('resize', resize);

  var points = [];
  var hue = 0;
  var LIFETIME = 0.6, MAX_POINTS = 500, BASE_WIDTH = 7, GLOW_WIDTH = 2.2, GLOW_ALPHA = 0.35, HUE_STEP = 0.015;
  var reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  addEventListener('pointermove', function (e) {
    if (reduceMotion) return;
    hue = (hue + HUE_STEP) % 1;
    points.push({ x: e.clientX, y: e.clientY, t: performance.now(), hue: hue });
    if (points.length > MAX_POINTS) points.shift();
  }, { passive: true });

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var now = performance.now();
    while (points.length && (now - points[0].t) / 1000 > LIFETIME) points.shift();
    ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    for (var pass = 0; pass < 2; pass++) {
      var width = pass === 0 ? BASE_WIDTH * GLOW_WIDTH : BASE_WIDTH;
      var alphaMul = pass === 0 ? GLOW_ALPHA : 1;
      for (var i = 1; i < points.length; i++) {
        var a = points[i - 1], b = points[i];
        var age = (now - b.t) / 1000;
        var alpha = Math.max(0, 1 - age / LIFETIME) * alphaMul;
        if (alpha <= 0) continue;
        ctx.strokeStyle = 'hsla(' + (b.hue * 360).toFixed(1) + ',100%,55%,' + alpha + ')';
        ctx.lineWidth = width;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
    }
    requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();
