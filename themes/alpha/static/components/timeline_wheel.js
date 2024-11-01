function goToYear(event) {
  console.log(event.currentTarget);
}

function getAngle(point) {
  const styleValue = point.getAttribute('style');
  return Number(styleValue.match(/[-]{0,1}[0-9]{2,3}/)[0]);
}

function isDownUnder(point) {
  const angle = getAngle(point);
  return (angle >= 180) || (angle <= 0);
}

export default function timelineWheel() {
  const wheel = document.querySelector('[data-wheel]')
  const points = Array.from(document.querySelectorAll('[data-point]'));
  const increment = 20;
  for (const point of Array.from(points)) {
    point.addEventListener('click', () => {
      const selectedPoint = wheel.querySelector('[style="--angle: 090deg;"]');
      const selectedPosition = points.indexOf(selectedPoint);
      const previousPosition = points.indexOf(point);
      const rotation = increment * (previousPosition - selectedPosition);
      for (const pointToChange of points) {
        const angle = getAngle(pointToChange);
        const newAngle = String(angle + rotation).padStart(3, '0');
        pointToChange.classList.toggle('selected', false);
        pointToChange.setAttribute('style', `--angle: ${newAngle}deg;`)
        if (isDownUnder(pointToChange)) {
          pointToChange.classList.toggle('hidden', true)
        } else {
          pointToChange.classList.toggle('hidden', false)
        }
        if (newAngle === '090') {
          pointToChange.classList.toggle('selected', true);
        }
      }
    });
  }
}
