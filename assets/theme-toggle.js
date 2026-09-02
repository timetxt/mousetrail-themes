(function () {
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem('mousetrail-theme'); } catch (e) {}
  if (stored === 'light' || stored === 'dark') root.setAttribute('data-theme', stored);
  var lightBtn = document.getElementById('theme-light');
  var darkBtn = document.getElementById('theme-dark');
  function apply(t) {
    root.setAttribute('data-theme', t);
    lightBtn.setAttribute('aria-pressed', String(t === 'light'));
    darkBtn.setAttribute('aria-pressed', String(t === 'dark'));
    try { localStorage.setItem('mousetrail-theme', t); } catch (e) {}
  }
  var effective = stored;
  if (effective !== 'light' && effective !== 'dark') {
    effective = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  lightBtn.setAttribute('aria-pressed', String(effective === 'light'));
  darkBtn.setAttribute('aria-pressed', String(effective === 'dark'));
  lightBtn.addEventListener('click', function () { apply('light'); });
  darkBtn.addEventListener('click', function () { apply('dark'); });
})();
