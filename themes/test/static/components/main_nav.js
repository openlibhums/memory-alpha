export function handleScroll() {
  let lastScrollTop = 0;
  const header = document.querySelector('.sticky-header');
  const mainNav = document.getElementById('main-nav');
  let hideTimeout;

  window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      // Scrolling down
      clearTimeout(hideTimeout);
      hideTimeout = setTimeout(() => {
        header.classList.add('hidden');
        if (mainNav.classList.contains('open')) {
          mainNav.classList.remove('open');
        }
      }, 40);
    } else {
      // Scrolling up
      clearTimeout(hideTimeout);
      header.classList.remove('hidden');
      if (mainNav.classList.contains('was-open')) {
        mainNav.classList.add('open');
      }
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
  });
}

export function slideDrawer() {
  const slideDrawer = document.getElementById('slide-drawer');
  const mainNav = document.getElementById('main-nav');
  
  slideDrawer.addEventListener('click', function() {
    mainNav.classList.toggle('open');
    if (mainNav.classList.contains('open')) {
      mainNav.classList.add('was-open');
    } else {
      mainNav.classList.remove('was-open');
    }
  });
}