export function animateGeorge() {

  // When page loads, play animations only if user is ok with motion
  const splash = document.querySelector('.george-space-splash');
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!prefersReduced.matches) {
    splash.classList.toggle('running');
  }

  function playOrPause() {
    splash.classList.toggle('running');
    splash.classList.toggle('showing-slide-1', false);
    splash.classList.toggle('showing-slide-2', false);
  }

  // When user clicks play or pause, play or pause
  const playPauseButton = document.querySelector('.george-space-splash .play-pause button');
  playPauseButton.addEventListener('click', playOrPause);

  // When user selects slide 1, go to beginning of animation duration and pause
  const selectSlide1 = document.querySelector('.george-space-splash .select-slide-1 button');
  selectSlide1.addEventListener('click', () => {
    splash.classList.toggle('running', false);
    splash.classList.toggle('showing-slide-1', true);
    splash.classList.toggle('showing-slide-2', false);
  });

  // When user selects slide 2, go to end of animation duration and pause
  const selectSlide2 = document.querySelector('.george-space-splash .select-slide-2 button');
  selectSlide2.addEventListener('click', () => {
    splash.classList.toggle('running', false);
    splash.classList.toggle('showing-slide-1', false);
    splash.classList.toggle('showing-slide-2', true);
  });
}
