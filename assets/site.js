
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
    const currentLogin = document.querySelector("[data-current-login]");
    const loadAdminStats = async () => {
      const setText = (selector, value) => {
        const node = document.querySelector(selector);
        if (node && value !== undefined && value !== null) node.textContent = value;
      };
      try {
        const response = await fetch("/api/admin-stats", { cache: "no-store" });
        if (!response.ok) throw new Error("Stats endpoint unavailable");
        const data = await response.json();
        setText('[data-stat="visits"]', data.visits7d?.toLocaleString?.() || data.visits7d);
        setText('[data-stat="pageviews"]', data.pageViews7d?.toLocaleString?.() || data.pageViews7d);
        setText('[data-stat-note="visits"]', "Last 7 days" + (data.updatedAt ? " · updated " + new Date(data.updatedAt).toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }) : ""));
        setText('[data-stat-note="pageviews"]', "Last 7 days");
        setText('[data-stat="analytics-status"]', "Live Cloudflare data");
        if (Array.isArray(data.daily) && data.daily.length) {
          const max = Math.max(...data.daily.map((day) => day.visits || 0), 1);
          const bars = document.querySelector("[data-analytics-bars]");
          if (bars) bars.innerHTML = data.daily.map((day) => `<span title="${day.date}: ${day.visits || 0} visits" style="height:${Math.max(10, Math.round(((day.visits || 0) / max) * 100))}%"></span>`).join("");
        }
        if (Array.isArray(data.topPages) && data.topPages.length) {
          setText('[data-stat="top-pages"]', data.topPages.map((page) => `${page.path || "/"} (${page.views || 0})`).join(" · "));
        }
        if (data.leadActions) {
          setText('[data-stat="lead-actions"]', `Quote: ${data.leadActions.quote || 0} · Calls: ${data.leadActions.call || 0} · Maps: ${data.leadActions.maps || 0}`);
        }
      } catch (error) {
        setText('[data-stat="analytics-status"]', "Connect Cloudflare Worker");
      }
    };
    const showDashboard = () => {
      login.hidden = true;
      dashboard.hidden = false;
      if (currentLogin) currentLogin.textContent = "Last login: " + new Date().toLocaleString([], { dateStyle: "medium", timeStyle: "short" });
      sessionStorage.setItem("bmPortalSignedIn", "true");
      loadAdminStats();
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
  const trackLeadAction = (type) => {
    try {
      const body = JSON.stringify({ type, path: window.location.pathname, ts: new Date().toISOString() });
      if (navigator.sendBeacon) {
        navigator.sendBeacon("/api/lead-event", new Blob([body], { type: "application/json" }));
      } else {
        fetch("/api/lead-event", { method: "POST", headers: { "Content-Type": "application/json" }, body, keepalive: true }).catch(() => {});
      }
    } catch (error) {}
  };
  document.querySelectorAll('a[href*="contact.html"], .mobile-sticky-cta a:first-child').forEach((link) => link.addEventListener("click", () => trackLeadAction("quote")));
  document.querySelectorAll('a[href^="tel:"]').forEach((link) => link.addEventListener("click", () => trackLeadAction("call")));
  document.querySelectorAll('a[href*="google.com/maps"], a[href*="maps/search"]').forEach((link) => link.addEventListener("click", () => trackLeadAction("maps")));
});
