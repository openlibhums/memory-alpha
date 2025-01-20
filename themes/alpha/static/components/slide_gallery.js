function setArrowButton(buttonSelector, targetId, gallery) {
  const arrowButton = gallery.querySelector(buttonSelector);
  if (document.getElementById(targetId)) {
    arrowButton?.setAttribute("data-target", targetId);
    arrowButton?.classList.toggle("hidden", false);
  } else {
    arrowButton?.classList.toggle("hidden", true);
  }
}

function setSelection(targetId) {
  const selectableButton = document.querySelector(
    `.tablist-button[data-target="${targetId}"`,
  );
  const gallery = selectableButton?.closest("[data-slide-gallery]");
  const tablistButtons = gallery?.querySelectorAll("[data-tablist-button]");
  for (const otherButton of Array.from(tablistButtons)) {
    otherButton.classList.toggle("selected", false);
  }
  selectableButton?.classList.toggle("selected", true);

  const previousNum = Number(targetId.slice(-1)) - 1;
  const previousTargetId = targetId.slice(0, -1) + previousNum;
  setArrowButton("[data-previous-button]", previousTargetId, gallery);

  const nextNum = Number(targetId.slice(-1)) + 1;
  const nextTargetId = targetId.slice(0, -1) + nextNum;
  setArrowButton("[data-next-button]", nextTargetId, gallery);
}

function setScrollDestination(button) {
  button.addEventListener("click", () => {
    const target = document.getElementById(button.getAttribute("data-target"));
    target?.scrollIntoView({
      block: "nearest",
    });
  });
}

const observerOptions = {
  root: document.querySelector("[data-scroll-container]"),
  threshold: 0.5,
};

function onIntersection(entries, _options) {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      setSelection(entry.target?.id);
    }
  }
}

const observer = new IntersectionObserver(onIntersection, observerOptions);

export default function slideGallery() {
  const galleries = document.querySelectorAll("[data-slide-gallery]");
  for (const gallery of Array.from(galleries)) {
    const slides = gallery.querySelectorAll("[data-current-slide]");
    for (const slide of Array.from(slides)) {
      observer.observe(slide);
    }
    const tablistButtons = gallery.querySelectorAll("[data-tablist-button]");
    for (const button of Array.from(tablistButtons)) {
      setScrollDestination(button);
    }
    const previousButton = gallery.querySelector("[data-previous-button]");
    setScrollDestination(previousButton);
    const nextButton = gallery.querySelector("[data-next-button]");
    setScrollDestination(nextButton);
  }
}
