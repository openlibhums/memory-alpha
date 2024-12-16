function setKeyEvents(timeline) {
  const tabList = timeline.querySelector('[role="tablist"]');
  const tabs = tabList.querySelectorAll('[role="tab"]');
  let tabFocus = 0;
  tabList.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
      tabs[tabFocus].setAttribute("tabindex", -1);
      if (e.key === "ArrowRight") {
        tabFocus++;
        // If we're at the end, go to the start
        if (tabFocus >= tabs.length) {
          tabFocus = 0;
        }
      } else if (e.key === "ArrowLeft") {
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

function setClickEvents(timeline) {
  const points = timeline.querySelectorAll('[data-point]');
  for (const point of Array.from(points)) {
    point.addEventListener('click', () => {
      for (const otherPoint of Array.from(points)) {
        otherPoint.setAttribute("tabindex", -1);
        otherPoint.classList.toggle('selected', false);
      }
      point.setAttribute("tabindex", 0);
      point.classList.toggle('selected', true);
      const year = point.dataset.point;
      const textBlock = timeline.querySelector(`[data-block="${year}"]`);
      const blocks = timeline.querySelectorAll('[data-block]');
      for (const otherBlock of Array.from(blocks)) {
        otherBlock.classList.toggle('selected', false);
      }
      textBlock.classList.toggle('selected', true);
    });
  }
}

export default function timelineWheel() {
  const timelineWheels = document.querySelectorAll('[data-timeline-wheel]');
  for (const timeline of Array.from(timelineWheels)) {
    setKeyEvents(timeline);
    setClickEvents(timeline);
  }
}
