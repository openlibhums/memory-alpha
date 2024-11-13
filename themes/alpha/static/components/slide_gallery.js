function setSelection(selector) {
  const selectableLink = document.querySelector(`.nav-link[href="${selector}"`);
  const gallery = selectableLink.closest('[data-slide-gallery]');
  const navLinks = gallery.querySelectorAll('[data-nav-link]');
  for (const otherLink of Array.from(navLinks)) {
    otherLink.classList.toggle('nav-selected', false);
    otherLink.setAttribute('aria-selected', "false");
  }
  selectableLink.classList.toggle('nav-selected', true);
  selectableLink.setAttribute('aria-selected', "true");
}

function makeSelectable(selectableLink) {
  const href = selectableLink.getAttribute('href');
  const linksToSameTarget = document.querySelectorAll(`[href="${href}"`)
  for (const link of Array.from(linksToSameTarget)) {
    link.addEventListener('click', () => {
      setSelection(link.getAttribute('href'));
    });
  }
}

const observerOptions = {
  root: document.querySelector("[data-scroll-container]"),
  threshold: 0.5,
}

function onIntersection(entries, _options) {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      let element = entry.target;
      setSelection(`#${element.id}`);
    }
  }
}

const observer = new IntersectionObserver(onIntersection, observerOptions);

export default function slideGallery() {
  const galleries = document.querySelectorAll('[data-slide-gallery]');
  for (const gallery of Array.from(galleries)) {
    const slides = gallery.querySelectorAll('[data-current-slide]');
    const navLinks = gallery.querySelectorAll('[data-nav-link]');
    for (const link of Array.from(navLinks)) {
      makeSelectable(link);
    }
    for (const slide of Array.from(slides)) {
      observer.observe(slide);
    }
  }
}
