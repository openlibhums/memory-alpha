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

function setKeyEvents(timeline) {
  const tabList = timeline.querySelector('[role="tablist"]');
  const tabs = tabList.querySelectorAll('[role="tab"]');
  let tabFocus = 0;
  for (const tab of tabs) {
    tab.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === "ArrowLeft" || e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        tab.setAttribute("tabindex", -1);
        if (e.key === "ArrowRight" || e.key === "ArrowDown") {
          tabFocus++;
          // If we're at the end, go to the start
          if (tabFocus >= tabs.length) {
            tabFocus = 0;
          }
        } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
          tabFocus--;
          // If we're at the start, move to the end
          if (tabFocus < 0) {
            tabFocus = tabs.length - 1;
          }
        }

        tabs[tabFocus].setAttribute("tabindex", 0);
        tabs[tabFocus].focus();
      }
    });
  }
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
    setKeyEvents(timeline);
    setClickEvents(timeline);
  }
  } catch (e) {
    alert(e);
  }
}
