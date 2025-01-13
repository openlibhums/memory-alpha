function clearPointSelections(timeline) {
  const points = timeline.querySelectorAll('[data-point]');
  for (const point of Array.from(points)) {
    point.setAttribute("tabindex", -1);
    point.classList.toggle('selected', false);
  }
}

function clearTextSelections(timeline) {
  const blocks = timeline.querySelectorAll('[data-block]');
  for (const block of Array.from(blocks)) {
    block.classList.toggle('selected', false);
    block.setAttribute("tabindex", -1);
  }
}

function changeSelection(timeline, point) {
  clearPointSelections(timeline);
  point.setAttribute("tabindex", 0);
  point.classList.toggle('selected', true);
  const year = point.dataset.point;
  const textBlock = timeline.querySelector(`[data-block="${year}"]`);
  clearTextSelections(timeline);
  textBlock.classList.toggle('selected', true);
  textBlock.setAttribute("tabindex", 0);
}

function remToPx(rem) {
  return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
}

function detectDirection() {
  const breakpointRem = 50;
  if (window.innerWidth <= remToPx(breakpointRem)) {
    return ["ArrowUp", "ArrowDown"]
  } else {
    return ["ArrowLeft", "ArrowRight"]
  }
}

function setArrowKeyEvents(timeline) {
  const tabList = timeline.querySelector('[role="tablist"]');
  tabList.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight" || e.key === "ArrowLeft" || e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      const [arrowDecrement, arrowIncrement] = detectDirection();
      const currentTab = document.querySelector('.point.selected');
      if (e.key === arrowDecrement && currentTab.previousElementSibling) {
        changeSelection(timeline, currentTab.previousElementSibling);
        currentTab.previousElementSibling.focus();
      } else if (e.key === arrowIncrement && currentTab.nextElementSibling) {
        changeSelection(timeline, currentTab.nextElementSibling);
        currentTab.nextElementSibling.focus();
      }
    }
  });
}

function setClickEvents(timeline) {
  const points = timeline.querySelectorAll('[data-point]');
  for (const point of Array.from(points)) {
    point.addEventListener('click', () => {
      changeSelection(timeline, point);
    });
  }
}

export default function timelineWheel() {
  const timelineWheels = document.querySelectorAll('[data-timeline-wheel]');
  try {
    for (const timeline of Array.from(timelineWheels)) {
      setArrowKeyEvents(timeline);
      setClickEvents(timeline);
    }
  } catch (e) {
    alert(e);
  }
}
