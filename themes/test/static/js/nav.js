document.addEventListener('DOMContentLoaded', function() {
  const slide_drawer = document.getElementById('slide-drawer');
  const main_nav = document.getElementById('main-nav');
  let scrollTimeout;

  slide_drawer.addEventListener('click', function() {
    main_nav.classList.toggle('open');
  });

  window.addEventListener('scroll', function() {
    if (main_nav.classList.contains('open')) {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(function() {
        main_nav.classList.remove('open');
      }, 50);
    }
  });
});
