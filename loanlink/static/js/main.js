/**
 * LoanLink Hyderabad – Global JavaScript
 * Handles: loader, navbar scroll, AOS, scroll-to-top
 */

/* ── Page Loader ─────────────────────────────────────────────── */
window.addEventListener('load', () => {
  const loader = document.getElementById('pageLoader');
  if (loader) {
    setTimeout(() => loader.classList.add('hidden'), 800);
  }
});

/* ── Sticky Navbar – shrink on scroll ───────────────────────── */
const mainNav = document.getElementById('mainNav');
if (mainNav) {
  window.addEventListener('scroll', () => {
    mainNav.classList.toggle('scrolled', window.scrollY > 60);
  });
}

/* ── Scroll-to-Top Button ───────────────────────────────────── */
const scrollBtn = document.getElementById('scrollTopBtn');
if (scrollBtn) {
  window.addEventListener('scroll', () => {
    scrollBtn.classList.toggle('visible', window.scrollY > 400);
  });
  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ── Lightweight AOS (scroll reveal) substitute ─────────────── */
(function initAOS() {
  const targets = document.querySelectorAll('[data-aos]');
  if (!targets.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el  = entry.target;
        const delay = parseInt(el.dataset.aosDelay || 0);
        setTimeout(() => {
          el.classList.add('aos-animate');
          observer.unobserve(el);
        }, delay);
      }
    });
  }, { threshold: 0.12 });

  targets.forEach(el => {
    el.classList.add('aos-init');
    observer.observe(el);
  });

  // Inject minimal AOS CSS
  const style = document.createElement('style');
  style.textContent = `
    .aos-init[data-aos="fade-up"]    { opacity:0; transform:translateY(30px); }
    .aos-init[data-aos="fade-down"]  { opacity:0; transform:translateY(-30px); }
    .aos-init[data-aos="fade-left"]  { opacity:0; transform:translateX(30px); }
    .aos-init[data-aos="fade-right"] { opacity:0; transform:translateX(-30px); }
    .aos-init[data-aos="zoom-in"]    { opacity:0; transform:scale(.9); }
    .aos-init[data-aos]              { transition: opacity .6s ease, transform .6s ease; }
    .aos-animate { opacity:1 !important; transform:none !important; }
  `;
  document.head.appendChild(style);
})();

/* ── Active nav link highlight on page load ─────────────────── */
document.querySelectorAll('.nav-link').forEach(link => {
  if (link.href === window.location.href) link.classList.add('active');
});

/* ── Bootstrap tooltips init ────────────────────────────────── */
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
  new bootstrap.Tooltip(el);
});
