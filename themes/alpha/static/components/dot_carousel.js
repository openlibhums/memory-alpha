export function changeTab(dotCarousel, tab) {
  const allTabs = dotCarousel.querySelectorAll(`[role="tab"]`);
  for (const otherTab of Array.from(allTabs)) {
    otherTab.classList.toggle("selected", false);
    otherTab.setAttribute("aria-selected", false);
    otherTab.setAttribute("tabindex", -1);
  }

  const allTabPanels = dotCarousel.querySelectorAll(`[role="tabpanel"]`);
  for (const otherTabPanel of Array.from(allTabPanels)) {
    otherTabPanel.classList.toggle("selected", false);
    otherTabPanel.setAttribute("tabindex", -1);
  }

  tab.setAttribute("aria-selected", true);
  tab.setAttribute("tabindex", 0);

  const ariaControls = tab.getAttribute("aria-controls");
  const tabPanel = dotCarousel.querySelector(`#${ariaControls}`);
  tabPanel.classList.toggle("selected", true);
  tabPanel.setAttribute("tabindex", 0);
}

function remToPx(rem) {
  return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
}

function detectDirection() {
  const breakpointRem = 50;
  if (window.innerWidth <= remToPx(breakpointRem)) {
    return ["ArrowUp", "ArrowDown"];
  } else {
    return ["ArrowLeft", "ArrowRight"];
  }
}

function setArrowKeyEvents(dotCarousel) {
  const tabList = dotCarousel.querySelector('[role="tablist"]');
  tabList.addEventListener("keydown", (e) => {
    if (
      e.key === "ArrowRight" ||
      e.key === "ArrowLeft" ||
      e.key === "ArrowDown" ||
      e.key === "ArrowUp"
    ) {
      e.preventDefault();
      const [arrowDecrement, arrowIncrement] = detectDirection();
      const currentTab = dotCarousel.querySelector(
        `[role="tab"][aria-selected="true"]`,
      );
      if (e.key === arrowDecrement && currentTab.previousElementSibling) {
        changeTab(dotCarousel, currentTab.previousElementSibling);
        currentTab.previousElementSibling.focus();
      } else if (e.key === arrowIncrement && currentTab.nextElementSibling) {
        changeTab(dotCarousel, currentTab.nextElementSibling);
        currentTab.nextElementSibling.focus();
      }
    }
  });
}

function setClickEvents(dotCarousel) {
  const tabs = dotCarousel.querySelectorAll('[role="tab"]');
  for (const tab of Array.from(tabs)) {
    tab.addEventListener("click", () => {
      changeTab(dotCarousel, tab);
    });
  }
}

export function dotCarousel() {
  const dotCarousels = document.querySelectorAll(`[data-dot-carousel]`);
  for (const dotCarousel of Array.from(dotCarousels)) {
    setArrowKeyEvents(dotCarousel);
    setClickEvents(dotCarousel);
  }
}
