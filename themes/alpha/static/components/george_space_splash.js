export function playPause() {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const animations = document.querySelectorAll('.animated');
  const buttons = document.querySelectorAll('.george-space-splash button');

  // Play animations when page loads only if user is ok with motion
  for (const animation of Array.from(animations)) {
    if (!prefersReduced.matches) {
      animation.classList.toggle('paused');
    }
  }

  // On click, change out the buttons and change the play state
  for (const button of Array.from(buttons)) {
    button.addEventListener('click', () => {
      for (const button of Array.from(buttons)) {
        button.classList.toggle('displayed');
      }
      for (const animation of Array.from(animations)) {
        animation.classList.toggle('paused');
      }
    });
  }
}
