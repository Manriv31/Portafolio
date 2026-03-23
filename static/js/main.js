// ============================================================
// Portfolio – Interactive Features
// ============================================================

document.addEventListener("DOMContentLoaded", () => {
    initScrollAnimations();
    initNavToggle();
    initLocalTime();
    initNavScroll();
    initCvDownloadButtons();
    initCvDownloadFetch();
    initThemeToggle();
    initI18n();
});

// --- Fade-in on scroll (Intersection Observer) ---
function initScrollAnimations() {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: "0px 0px -40px 0px" }
    );

    document.querySelectorAll(".fade-in").forEach((el) => observer.observe(el));
}

// --- Mobile nav toggle ---
function initNavToggle() {
    const toggle = document.getElementById("nav-toggle");
    const links = document.querySelector(".nav-links");

    if (!toggle || !links) return;

    toggle.addEventListener("click", () => {
        links.classList.toggle("open");
        toggle.classList.toggle("active");
    });

    // Close on link click
    links.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            links.classList.remove("open");
            toggle.classList.remove("active");
        });
    });
}

// --- Local time display ---
function initLocalTime() {
    const timeEl = document.getElementById("local-time");
    if (!timeEl) return;

    function updateTime() {
        const now = new Date();
        timeEl.textContent = now.toLocaleTimeString("es-MX", {
            hour: "2-digit",
            minute: "2-digit",
            hour12: true,
        });
    }

    updateTime();
    setInterval(updateTime, 30000);
}

// --- Nav background on scroll ---
function initNavScroll() {
    const nav = document.getElementById("nav");
    if (!nav) return;

    let ticking = false;
    window.addEventListener("scroll", () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                nav.classList.toggle("scrolled", window.scrollY > 50);
                ticking = false;
            });
            ticking = true;
        }
    });
}

// --- CV download with language selection ---
function initCvDownloadButtons() {
    const buttons = document.querySelectorAll(".js-cv-download");
    if (!buttons.length) return;
    // Replace prompt-based flow with an inline popover menu
    buttons.forEach((button) => {
        const wrapper = button.closest('.cv-download-wrapper');
        const menu = wrapper ? wrapper.querySelector('.cv-download-menu') : null;

        function closeMenu() {
            if (!wrapper) return;
            wrapper.classList.remove('open');
            button.setAttribute('aria-expanded', 'false');
            if (menu) menu.setAttribute('aria-hidden', 'true');
            if (menu) restoreMenu(menu);
        }

        function openMenu() {
            if (!wrapper) return;
            wrapper.classList.add('open');
            button.setAttribute('aria-expanded', 'true');
            if (menu) menu.setAttribute('aria-hidden', 'false');
            if (menu) mountMenuToBody(menu, button);
        }

        button.addEventListener('click', (e) => {
            e.stopPropagation();
            if (!wrapper) return;
            if (wrapper.classList.contains('open')) closeMenu();
            else openMenu();
        });

        // close on outside click — consider mounted menu (moved to body)
        document.addEventListener('click', (ev) => {
            if (!wrapper) return;
            const clickInsideWrapper = wrapper.contains(ev.target);
            const clickInsideMenu = menu && menu.dataset.mounted === 'true' ? menu.contains(ev.target) : false;
            if (!clickInsideWrapper && !clickInsideMenu) closeMenu();
        });

        // close on Escape
        document.addEventListener('keydown', (ev) => {
            if (ev.key === 'Escape') closeMenu();
        });

        // no-op for links (they will navigate normally)
        // reposition mounted menu on resize/scroll
        window.addEventListener('resize', () => {
            if (menu && menu.dataset.mounted === 'true') positionMountedMenu(menu, button);
        });
        window.addEventListener('scroll', () => {
            if (menu && menu.dataset.mounted === 'true') positionMountedMenu(menu, button);
        });
    });
}

// Helpers to mount menu to body and position it near the button
function mountMenuToBody(menu, button) {
    if (!menu || !button) return;
    if (menu.dataset.mounted === 'true') return;
    menu._origParent = menu.parentNode;
    menu._origNext = menu.nextSibling;
    document.body.appendChild(menu);
    menu.classList.add('cv-menu-mounted');
    menu.dataset.mounted = 'true';
    // ensure visible for measurement
    menu.style.display = 'block';
    positionMountedMenu(menu, button);
}

function restoreMenu(menu) {
    if (!menu) return;
    if (menu.dataset.mounted !== 'true') return;
    menu.style.left = '';
    menu.style.top = '';
    menu.style.right = '';
    menu.style.position = '';
    menu.style.zIndex = '';
    // allow CSS to control visibility again
    menu.style.display = '';
    menu.classList.remove('cv-menu-mounted');
    menu.dataset.mounted = 'false';
    if (menu._origParent) {
        if (menu._origNext) menu._origParent.insertBefore(menu, menu._origNext);
        else menu._origParent.appendChild(menu);
    }
}

function positionMountedMenu(menu, button) {
    if (!menu || !button) return;
    const rect = button.getBoundingClientRect();
    // measure menu width
    const menuRect = menu.getBoundingClientRect();
    const margin = 8;
    let left = rect.right - menuRect.width;
    if (left + menuRect.width > window.innerWidth - margin) left = window.innerWidth - menuRect.width - margin;
    if (left < margin) left = margin;
    let top = rect.bottom + margin;
    if (top + menuRect.height > window.innerHeight - margin) top = rect.top - menuRect.height - margin;
    if (top < margin) top = margin;
    menu.style.position = 'fixed';
    menu.style.left = `${Math.round(left)}px`;
    menu.style.top = `${Math.round(top)}px`;
    menu.style.right = 'auto';
    menu.style.zIndex = '9999';
}

    // --- CV download via fetch with spinner and error toast ---
    function initCvDownloadFetch() {
        document.querySelectorAll('.cv-download-link').forEach(link => {
            link.addEventListener('click', async (e) => {
                e.preventDefault();
                const url = link.getAttribute('href');
                const wrapper = link.closest('.cv-download-wrapper');
                if (wrapper) {
                    // ensure menu is restored and closed when a link is clicked
                    const menus = Array.from(document.querySelectorAll('.cv-download-menu'));
                    const myMenu = menus.find(m => m._origParent === wrapper || wrapper.contains(m));
                    if (myMenu) restoreMenu(myMenu);
                    wrapper.classList.remove('open');
                }

                const lang = (new URL(url, window.location.href)).searchParams.get('lang') || 'es';

                const langCode = (window.i18next && window.i18next.language) || localStorage.getItem('site-lang') || 'es';
                const messages = {
                    en: { generating: 'Generating PDF…', error: 'Could not generate PDF. Please try again.' },
                    es: { generating: 'Generando PDF…', error: 'No se pudo generar el PDF. Intenta nuevamente.' }
                };

                const msg = messages[langCode] || messages['en'];

                showCvSpinner(msg.generating);

                try {
                    const resp = await fetch(url, { method: 'GET' });
                    if (!resp.ok) {
                        hideCvSpinner();
                        showCvToast(msg.error);
                        return;
                    }

                    const blob = await resp.blob();

                    // Try to get filename from Content-Disposition
                    const cd = resp.headers.get('Content-Disposition') || '';
                    let filename = `CV_${lang}.pdf`;
                    const m = /filename\*=UTF-8''([^;\n]+)/i.exec(cd) || /filename="?([^";\n]+)"?/i.exec(cd);
                    if (m && m[1]) filename = decodeURIComponent(m[1]);

                    const blobUrl = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = blobUrl;
                    a.download = filename;
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                    window.URL.revokeObjectURL(blobUrl);
                    hideCvSpinner();
                } catch (err) {
                    hideCvSpinner();
                    showCvToast(msg.error);
                    console.error('CV download error', err);
                }
            });
        });
    }

    function showCvSpinner(text) {
        // avoid duplicate
        if (document.getElementById('cv-spinner-overlay')) return;
        const overlay = document.createElement('div');
        overlay.id = 'cv-spinner-overlay';
        overlay.innerHTML = `
            <div class="cv-spinner-card">
                <div class="cv-spinner"></div>
                <div class="cv-spinner-text">${text}</div>
            </div>`;
        document.body.appendChild(overlay);
    }

    function hideCvSpinner() {
        const el = document.getElementById('cv-spinner-overlay');
        if (el) el.remove();
    }

    function showCvToast(text) {
        // small toast at top-center
        let container = document.getElementById('cv-toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'cv-toast-container';
            document.body.appendChild(container);
        }
        const toast = document.createElement('div');
        toast.className = 'cv-toast';
        toast.textContent = text;
        container.appendChild(toast);
        setTimeout(() => { toast.classList.add('visible'); }, 10);
        setTimeout(() => { toast.classList.remove('visible'); setTimeout(() => toast.remove(), 300); }, 4500);
    }

// --- Theme toggle (dark / light) ---
function initThemeToggle() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;

    // helper to swap theme-dependent assets (images)
    function updateThemeAssets() {
        const imgs = document.querySelectorAll('[data-src-dark][data-src-light]');
        imgs.forEach(img => {
            const isLight = document.documentElement.classList.contains('light-theme');
            const src = isLight ? img.getAttribute('data-src-light') : img.getAttribute('data-src-dark');
            if (src && img.getAttribute('src') !== src) img.setAttribute('src', src);
        });
    }

    // load preference
    const stored = localStorage.getItem('site-theme');
    if (stored === 'light') document.documentElement.classList.add('light-theme');
    // ensure assets match initial theme
    updateThemeAssets();

    btn.addEventListener('click', () => {
        const isLight = document.documentElement.classList.toggle('light-theme');
        localStorage.setItem('site-theme', isLight ? 'light' : 'dark');
        updateThemeAssets();
    });
}

// --- i18n initialization and language toggle ---
function initI18n() {
    if (typeof i18next === 'undefined') return;

    const resources = {
        en: {
            translation: {
                nav: { projects: 'Projects', experience: 'Experience', contact: 'Contact' },
                hero: { greeting: "Hi, I'm", tagline: '{{tagline}}' },
                projects: { title: 'Projects', featured: 'Featured projects', see_all: 'See all projects →' },
                experience: { title: 'Experience', detail: 'See detailed experience' },
                freelance: { title: 'Freelance Services' },
                connect: { title: "Let's connect" }
            }
        },
        es: {
            translation: {
                nav: { projects: 'Proyectos', experience: 'Experiencia', contact: 'Contacto' },
                hero: { greeting: 'Hola, soy', tagline: '{{tagline}}' },
                projects: { title: 'Proyectos', featured: 'Proyectos destacados', see_all: 'Ver todos los proyectos →' },
                experience: { title: 'Experiencia', detail: 'Ver experiencia detallada' },
                freelance: { title: 'Servicios freelance' },
                connect: { title: 'Conectemos' }
            }
        }
    };

    i18next.init({ lng: localStorage.getItem('site-lang') || 'en', resources }, function(err, t) {
        // apply translations
        applyTranslations();
        applyDataTranslations();
    });

    function applyTranslations() {
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            let text = i18next.t(key, { tag: el.getAttribute('data-tag') || '' });
            // allow fallback to element content when using template values
            if (text && text.indexOf('{{tagline}}') !== -1) {
                text = text.replace('{{tagline}}', document.querySelector('.hero-tagline')?.textContent || '');
            }
            el.textContent = text;
        });
        // update language button
        const langBtn = document.getElementById('lang-toggle');
        if (langBtn) langBtn.textContent = i18next.language.toUpperCase();
    }

    // apply translations coming from `data.py` rendered as data-text-en / data-text-es
    function applyDataTranslations() {
        const lang = i18next.language || localStorage.getItem('site-lang') || 'en';
        document.querySelectorAll('[data-text-en], [data-text-es]').forEach(el => {
            const en = el.getAttribute('data-text-en');
            const es = el.getAttribute('data-text-es');
            if (lang === 'en' && en !== null) el.textContent = en;
            else if (lang === 'es' && es !== null) el.textContent = es;
        });
    }

    // language toggle button
    const langBtn = document.getElementById('lang-toggle');
    if (langBtn) {
        langBtn.addEventListener('click', () => {
            const next = i18next.language === 'en' ? 'es' : 'en';
            i18next.changeLanguage(next, () => {
                localStorage.setItem('site-lang', next);
                applyTranslations();
                applyDataTranslations();
            });
        });
    }
}
