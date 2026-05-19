const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "access-control-allow-origin": "https://bmautodetailing.ca",
      "access-control-allow-methods": "GET,POST,OPTIONS",
      "access-control-allow-headers": "content-type",
    },
  });

const todayMinus = (days) => {
  const date = new Date();
  date.setUTCDate(date.getUTCDate() - days);
  return date.toISOString().slice(0, 10);
};

async function readClicks(env) {
  if (!env.LEAD_EVENTS) return { quote: 0, call: 0, maps: 0 };
  const raw = await env.LEAD_EVENTS.get("lead-actions-7d");
  return raw ? JSON.parse(raw) : { quote: 0, call: 0, maps: 0 };
}

async function writeClick(request, env) {
  if (!env.LEAD_EVENTS) return json({ ok: true, stored: false });
  const payload = await request.json().catch(() => ({}));
  const type = ["quote", "call", "maps"].includes(payload.type) ? payload.type : "quote";
  const current = await readClicks(env);
  current[type] = (current[type] || 0) + 1;
  current.updatedAt = new Date().toISOString();
  await env.LEAD_EVENTS.put("lead-actions-7d", JSON.stringify(current));
  return json({ ok: true, stored: true });
}

async function cloudflareAnalytics(env) {
  if (!env.CF_API_TOKEN || !env.CF_ZONE_TAG) {
    return {
      visits7d: null,
      pageViews7d: null,
      daily: [],
      topPages: [],
      configured: false,
    };
  }

  const since = todayMinus(7);
  const until = todayMinus(0);
  const query = `
    query ZoneStats($zoneTag: string, $since: Date, $until: Date) {
      viewer {
        zones(filter: { zoneTag: $zoneTag }) {
          totals: httpRequestsAdaptiveGroups(
            limit: 1
            filter: { date_geq: $since, date_leq: $until }
          ) {
            count
            uniq { uniques }
          }
          daily: httpRequestsAdaptiveGroups(
            limit: 7
            filter: { date_geq: $since, date_leq: $until }
            orderBy: [date_ASC]
          ) {
            dimensions { date }
            count
            uniq { uniques }
          }
          topPages: httpRequestsAdaptiveGroups(
            limit: 5
            filter: { date_geq: $since, date_leq: $until, clientRequestPath_neq: "/admin.html" }
            orderBy: [count_DESC]
          ) {
            dimensions { clientRequestPath }
            count
          }
        }
      }
    }
  `;

  const response = await fetch("https://api.cloudflare.com/client/v4/graphql", {
    method: "POST",
    headers: {
      "authorization": `Bearer ${env.CF_API_TOKEN}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({ query, variables: { zoneTag: env.CF_ZONE_TAG, since, until } }),
  });
  const result = await response.json();
  if (!response.ok || result.errors) throw new Error(JSON.stringify(result.errors || result));

  const zone = result.data?.viewer?.zones?.[0] || {};
  const totals = zone.totals?.[0] || {};
  return {
    visits7d: totals.uniq?.uniques || 0,
    pageViews7d: totals.count || 0,
    daily: (zone.daily || []).map((day) => ({
      date: day.dimensions?.date,
      visits: day.uniq?.uniques || 0,
      pageViews: day.count || 0,
    })),
    topPages: (zone.topPages || []).map((page) => ({
      path: page.dimensions?.clientRequestPath || "/",
      views: page.count || 0,
    })),
    configured: true,
  };
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") return json({ ok: true });
    const url = new URL(request.url);

    if (url.pathname === "/api/lead-event" && request.method === "POST") {
      return writeClick(request, env);
    }

    if (url.pathname === "/api/admin-stats" && request.method === "GET") {
      try {
        const analytics = await cloudflareAnalytics(env);
        const leadActions = await readClicks(env);
        return json({ ...analytics, leadActions, updatedAt: new Date().toISOString() });
      } catch (error) {
        return json({ error: "Unable to load analytics", detail: String(error), updatedAt: new Date().toISOString() }, 502);
      }
    }

    return json({ error: "Not found" }, 404);
  },
};
