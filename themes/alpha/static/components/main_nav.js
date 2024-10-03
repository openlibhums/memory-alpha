export function slideDrawer() {
  const slideDrawer = document.getElementById('slide-drawer');
  const mainNav = document.getElementById('main-nav');
  
  slideDrawer.addEventListener('click', function() {
    mainNav.classList.toggle('open');
  });
}
