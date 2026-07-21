// ─── NAV SCROLL ───
const nav = document.querySelector('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 50);
});

// ─── HAMBURGER ───
const hamburger = document.querySelector('.nav-hamburger');
const navLinks = document.querySelector('.nav-links');

function closeMenu() {
  if (!navLinks) return;
  navLinks.classList.remove('open');
  document.body.style.overflow = '';
  const spans = hamburger.querySelectorAll('span');
  spans[0].style.transform = '';
  spans[1].style.opacity = '';
  spans[2].style.transform = '';
}

function openMenu() {
  navLinks.classList.add('open');
  document.body.style.overflow = 'hidden'; // prevent scroll behind menu
  const spans = hamburger.querySelectorAll('span');
  spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
  spans[1].style.opacity = '0';
  spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
}

if (hamburger) {
  // Toggle on hamburger tap
  hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    navLinks.classList.contains('open') ? closeMenu() : openMenu();
  });

  // Close when any nav link is tapped
  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', closeMenu);
  });

  // Close when tapping outside the menu
  document.addEventListener('click', (e) => {
    if (navLinks.classList.contains('open') &&
        !navLinks.contains(e.target) &&
        !hamburger.contains(e.target)) {
      closeMenu();
    }
  });

  // Close on scroll (feels natural on mobile)
  window.addEventListener('scroll', () => {
    if (navLinks.classList.contains('open')) closeMenu();
  }, { passive: true });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

// ─── ACTIVE NAV ───
const path = window.location.pathname.replace(/\/$/, '').split('/').pop() || '';
document.querySelectorAll('.nav-links a').forEach(a => {
  const href = a.getAttribute('href').replace(/^\//, '').replace(/\/$/, '');
  const current = path.replace('.html', '');
  if ((current === '' && href === '') || (href && current === href)) {
    a.classList.add('active');
  }
});

// ─── COUNTDOWN TO NEXT FIXTURE ───
const fixtures = [
  { date: new Date('2026-06-14T10:00:00'), opponent: 'Iganmu Giants', venue: 'GRA Marine Road Pitch' },
  { date: new Date('2026-06-28T10:00:00'), opponent: 'Mushin Central', venue: 'Isolo Barracks Pitch' },
    { date: new Date('2026-07-19T10:00:00'), opponent: 'Recovery House', venue: '721 Field' },
  { date: new Date('2026-08-02T10:00:00'), opponent: 'Catholic Church', venue: '721 Field' },
  { date: new Date('2026-08-16T10:00:00'), opponent: 'Rising Stars FC', venue: 'Abule-Ado Field' },
];

function getNextFixture() {
  const now = new Date();
  return fixtures.find(f => f.date > now) || null;
}

function updateCountdown() {
  const cdDays = document.getElementById('cd-days');
  const cdHours = document.getElementById('cd-hours');
  const cdMins = document.getElementById('cd-mins');
  const cdSecs = document.getElementById('cd-secs');
  const cdOpponent = document.getElementById('cd-opponent');
  const cdVenue = document.getElementById('cd-venue');

  if (!cdDays) return;

  const next = getNextFixture();
  if (!next) {
    document.getElementById('countdown-wrap')?.remove();
    return;
  }

  if (cdOpponent) cdOpponent.textContent = next.opponent;
  if (cdVenue) cdVenue.textContent = next.venue;

  function tick() {
    const now = new Date();
    const diff = next.date - now;
    if (diff <= 0) { clearInterval(timer); return; }

    const d = Math.floor(diff / 86400000);
    const h = Math.floor((diff % 86400000) / 3600000);
    const m = Math.floor((diff % 3600000) / 60000);
    const s = Math.floor((diff % 60000) / 1000);

    cdDays.textContent = String(d).padStart(2, '0');
    cdHours.textContent = String(h).padStart(2, '0');
    cdMins.textContent = String(m).padStart(2, '0');
    cdSecs.textContent = String(s).padStart(2, '0');
  }

  tick();
  const timer = setInterval(tick, 1000);
}

updateCountdown();

// ─── FADE UP ON SCROLL ───
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.animation = 'fadeUp 0.6s ease forwards';
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.observe').forEach(el => observer.observe(el));
