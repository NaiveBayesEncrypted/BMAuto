
(() => {
  if (window.location.pathname.endsWith("/index.html")) {
    const cleanPath = window.location.pathname.replace(/index\.html$/, "");
    window.history.replaceState(null, "", cleanPath + window.location.search + window.location.hash);
  }
})();
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-mobile-menu]");
  toggle?.addEventListener("click", () => {
    const isOpen = menu?.classList.toggle("open");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
});
