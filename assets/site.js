
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
  const portal = document.querySelector("[data-admin-portal]");
  const form = document.querySelector("[data-admin-form]");
  if (portal && form) {
    const login = document.querySelector("[data-admin-login]");
    const dashboard = document.querySelector("[data-admin-dashboard]");
    const error = document.querySelector("[data-admin-error]");
    const email = document.querySelector("[data-admin-email]");
    const password = document.querySelector("[data-admin-password]");
    const showDashboard = () => {
      login.hidden = true;
      dashboard.hidden = false;
      sessionStorage.setItem("bmPortalSignedIn", "true");
    };
    if (sessionStorage.getItem("bmPortalSignedIn") === "true") showDashboard();
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const ok = email.value.trim().toLowerCase() === "admin@bmautodetailing.ca" && password.value === "BMAdmin-2026!";
      if (ok) showDashboard();
      else error.hidden = false;
    });
    document.querySelector("[data-admin-logout]")?.addEventListener("click", () => {
      sessionStorage.removeItem("bmPortalSignedIn");
      dashboard.hidden = true;
      login.hidden = false;
      form.reset();
    });
  }
});
