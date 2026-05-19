# B&M Admin Analytics Worker

This worker powers real admin dashboard data for `bmautodetailing.ca/admin.html`.

It provides:

- `GET /api/admin-stats`
  - 7-day visits from Cloudflare GraphQL Analytics
  - 7-day page views
  - daily visit bars
  - top page paths
  - lead action counts from KV

- `POST /api/lead-event`
  - stores quote/call/maps clicks in Workers KV

## Required Cloudflare Setup

1. Put `bmautodetailing.ca` behind Cloudflare DNS with the orange proxy enabled.
2. Create a Cloudflare API token with Analytics read access for the B&M zone.
3. Deploy `admin-stats-worker.js` as a Worker.
4. Add Worker secrets:
   - `CF_API_TOKEN`
   - `CF_ZONE_TAG`
5. Create a Workers KV namespace named `LEAD_EVENTS`.
6. Add Worker routes:
   - `bmautodetailing.ca/api/admin-stats`
   - `bmautodetailing.ca/api/lead-event`

## Security Note

For the admin page itself, also protect `/admin.html` with Cloudflare Access so only the approved admin email can open it.
