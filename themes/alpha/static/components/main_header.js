export function slideDrawer() {
  const slideDrawer = document.getElementById("slide-drawer");
  const mainHeader = document.getElementById("main-header");

  slideDrawer?.addEventListener("click", function () {
    mainHeader?.classList.toggle("open");
  });
}
