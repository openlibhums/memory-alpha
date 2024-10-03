export function playPause() {
  const buttons = document.querySelectorAll('.george-space-splash button');
  const animations = document.querySelectorAll('.animated');
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
