export default function timelineWheel() {
  const points = Array.from(document.querySelectorAll('[data-point]'));
  for (const selectedPoint of points) {
    selectedPoint.addEventListener('click', () => {
      for (const otherPoint of points) {
        otherPoint.classList.toggle('selected', false);
      }
      selectedPoint.classList.toggle('selected', true);
      selectedPoint.nextElementSibling.focus();
    });
  }
}
