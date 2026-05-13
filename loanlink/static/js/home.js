/**
 * LoanLink Hyderabad – Home Page JavaScript
 * EMI slider, hero card calculator, animated counters
 */

/* ── Hero Card EMI Calculator ────────────────────────────────── */
(function initHeroCard() {
  const slider  = document.getElementById('loanSlider');
  const display = document.getElementById('loanDisplay');
  const tenure  = document.getElementById('tenureSelect');
  const emiEl   = document.getElementById('emiValue');

  if (!slider) return;

  function formatINR(n) {
    return '₹ ' + Math.round(n).toLocaleString('en-IN');
  }

  function calcEMI(P, months, ratePA = 11.5) {
    const r = ratePA / (12 * 100);
    return (P * r * Math.pow(1 + r, months)) / (Math.pow(1 + r, months) - 1);
  }

  function update() {
    const P = parseInt(slider.value);
    const n = parseInt(tenure.value);
    display.textContent = formatINR(P);
    emiEl.textContent   = formatINR(calcEMI(P, n));
  }

  slider.addEventListener('input', update);
  tenure.addEventListener('change', update);
  update(); // Initial render
})();

/* ── Animated Counters ───────────────────────────────────────── */
(function initCounters() {
  // We re-animate when the stats section enters the viewport
  const statsSection = document.querySelector('.stats-section');
  if (!statsSection) return;

  let animated = false;

  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting && !animated) {
      animated = true;
      animateCounters();
    }
  }, { threshold: 0.4 });

  observer.observe(statsSection);

  function animateCounters() {
    // Stats are rendered with static text; no counters to re-run.
    // (Values already shown; animation handled by AOS)
  }
})();
