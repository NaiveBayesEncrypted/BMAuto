from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://bmautodetailing.ca"

BUSINESS = {
    "name": "B&M Auto Detailing",
    "phone": "(403) 454-0203",
    "email": "bookings@bmautodetailing.ca",
    "address": "1247 36 Ave NE, Calgary, AB T2E 6N6",
    "hours": "Mon-Sat, 9:00 AM-6:00 PM",
    "rating": "4.8 Google rating",
    "reviews": "21 reviews",
}

MAP_URL = "https://www.google.com/maps/search/?api=1&query=B%26M%20Auto%20Detailing%201247%2036%20Ave%20NE%20Calgary%20AB"
MAP_EMBED = "https://www.google.com/maps?q=B%26M%20Auto%20Detailing%201247%2036%20Ave%20NE%20Calgary%20AB&output=embed"

services = [
    ("window-tint.html", "Window Tint", "Automotive window tint for privacy, glare reduction, cabin comfort, UV protection, and a cleaner finished look.", ["Shade options explained", "Cleaner vehicle appearance", "Installed for daily drivers and premium vehicles"]),
    ("paint-protection-film.html", "PPF & Paint Protection", "Paint protection film and clear protection planning for front-end impact areas, rock chips, road debris, and Alberta driving.", ["Front-end impact zones", "Rock-chip protection", "Coverage chosen by driving use"]),
    ("car-stereo.html", "Car Stereo & Audio", "Stereo upgrades, audio installation, and practical in-vehicle electronics work for drivers who want better sound and cleaner functionality.", ["Audio upgrades", "Head unit installs", "Clean wiring approach"]),
    ("backup-camera.html", "Backup Camera", "Backup camera installation for better visibility, easier parking, and safer reversing in cars, trucks, SUVs, and work vehicles.", ["Rear visibility", "Parking support", "Factory-style integration where possible"]),
    ("remote-starter.html", "Remote Starter", "Remote starter installation for Calgary winters, daily convenience, and easier cold-weather starts.", ["Winter convenience", "Vehicle-specific setup", "Key fob and remote options"]),
    ("auto-detailing.html", "Auto Detailing", "Interior and exterior detailing for vehicles that need a cleaner cabin, fresher finish, or seasonal reset before or after accessory work.", ["Interior reset", "Exterior cleanup", "Add-on service option"]),
]

seo_service_links = [
    ("window-tint.html", "Window Tint"),
    ("paint-protection-film.html", "Paint Protection Film"),
    ("car-stereo.html", "Car Stereo"),
    ("backup-camera.html", "Backup Camera"),
    ("remote-starter.html", "Remote Starter"),
    ("interior-detailing.html", "Interior Detailing"),
    ("exterior-detailing.html", "Exterior Detailing"),
    ("new-vehicle-protection.html", "New Vehicle Protection"),
]

packages = [
    ("Window Tint Package", "Drivers who want privacy, glare reduction, and a cleaner look", "Tint consultation, shade selection, vehicle prep, installation, and aftercare guidance.", "Same day in many cases", "Quote required"),
    ("Front-End PPF Package", "New vehicles and highway drivers exposed to rock chips", "Coverage planning for bumper, hood, fenders, mirrors, and high-impact areas.", "By vehicle", "Custom quote"),
    ("Stereo Upgrade", "Drivers wanting better sound or a modern head unit", "Audio consultation, stereo/head unit options, install planning, and clean integration.", "By install", "Custom quote"),
    ("Backup Camera Install", "Vehicles needing better reversing visibility", "Camera selection, mounting plan, wiring, display integration, and function check.", "By vehicle", "Custom quote"),
    ("Remote Starter Install", "Calgary drivers wanting winter convenience", "Vehicle-specific remote starter planning, installation, setup, and basic handoff.", "By vehicle", "Custom quote"),
    ("Detailing Add-On", "Vehicles needing a clean reset before pickup or install", "Interior cleanup, exterior wash, windows, touch points, and seasonal reset options.", "By condition", "From $179"),
]

faqs = [
    ("What services does B&M offer?", "B&M offers window tint, PPF and paint protection, car stereo and audio installation, backup camera installation, remote starters, auto detailing, and related vehicle accessory services."),
    ("Can I book more than one service together?", "Yes. Customers can request a combined quote for tint, PPF, stereo, backup camera, remote starter, and detailing work. B&M confirms the right sequence and timing before the appointment."),
    ("How long does window tint take?", "Timing depends on vehicle size, glass layout, and film selection. Many tint installs can be completed the same day, but B&M confirms timing after reviewing the vehicle."),
    ("Does PPF stop rock chips?", "Paint protection film is designed for physical impact protection. It is commonly used on bumpers, hoods, fenders, mirrors, rocker panels, and other high-impact areas."),
    ("Can you install a backup camera on an older vehicle?", "In many cases, yes. The correct setup depends on the vehicle, display options, wiring path, and the look the customer wants."),
    ("Is a remote starter worth it in Calgary?", "For many Calgary drivers, yes. A remote starter can make winter mornings easier and more comfortable when installed with the right vehicle-specific setup."),
    ("Can packages be adjusted for vehicle size and condition?", "Yes. B&M scopes the recommendation around vehicle size, interior condition, paint condition, and protection goals before confirming the appointment."),
    ("Do you work on trucks, SUVs, and daily drivers?", "Yes. Packages can be adjusted for trucks, SUVs, family vehicles, commuter cars, luxury vehicles, lease returns, and sale-prep vehicles."),
    ("Can I send photos before booking?", "Yes. Photos of the vehicle, windows, dashboard/display, stereo area, rear hatch/trunk area, and protection zones help B&M give a clearer starting recommendation."),
]

google_reviews = [
    {"name": "Hikmatullah Sarwari", "rating": 5, "date": "6 months ago", "text": "\"I'm blown away by the exceptional service and attention to detail at B and M auto detailing From the moment I dropped off my car, the team was professional, courteous, and communicative. The detailing work was top-notch - my vehicle has never looked or felt cleaner. The exterior shine is incredible, and the interior detailing was meticulous. The shop's commitment to quality and customer satisfaction is evident. Highly recommended B and M auto detailing for anyone seeking premium auto detailing services. Five stars isn't enough - I'd give them ten stars if I could!\""},
    {"name": "Mansoor Safi", "rating": 5, "date": "3 months ago", "text": "Bilal at B&M Auto Detailing did an outstanding job on my vehicle. Very thorough, clean work, and the results were better than I expected. If you want your car looking like new, go here."},
    {"name": "Asgher Yousaf", "rating": 5, "date": "3 months ago", "text": "I had an amazing experience with B&M Auto Detailing. They paid attention to every small detail, inside and out. The car was spotless, smelled fresh, and the finish was excellent. Fair pricing and very professional service. I will definitely come back and recommend them to others."},
    {"name": "S \"shubert\" C", "rating": 5, "date": "4 months ago", "text": "Good experience, they are very responsible and professional, and did great job on my jeep, thanks will shop again!"},
    {"name": "Mustafa Fakhri", "rating": 5, "date": "5 months ago", "text": "I dropped my vehicle for detailing and they cleaned it perfectly. I highly recommend and good price."},
    {"name": "Bluw Shah", "rating": 5, "date": "7 months ago", "text": "Really great service , I been there a-few times , wonderful customer service, really good prices for all services,,, I would recommend everyone to try this place I'm sure you won't regret... 10/10"},
    {"name": "Wahidkhan Hashmy", "rating": 5, "date": "3 months ago", "text": "Really good guy . Fast and good work done yet"},
    {"name": "zahid sherzay", "rating": 5, "date": "7 months ago", "text": "One of the best detailing shop"},
    {"name": "Bilal ahmad Amiri", "rating": 5, "date": "5 months ago", "text": "Great servicing on time"},
    {"name": "Samim Samimi", "rating": 5, "date": "7 months ago", "text": "Great place , on time , supper clean"},
    {"name": "Shahidullah Sherzad", "rating": 5, "date": "2 days ago", "text": "Never see that awesome and amazing job that they did for me and they are friendly and wonderful service very happy and thanks guy B&M auto detailing"},
    {"name": "Khalid Amiri", "rating": 5, "date": "Edited 5 days ago", "text": "I recently had my vehicle detailed and protected with PPF at B&M Auto Detailing, and the experience exceeded my expectations. The team was professional, knowledgeable, and clearly takes pride in their work. They paid close attention to every detail, leaving my car looking better than when I first got it. The paint protection film was applied flawlessly, with clean edges and no visible imperfections. They took the time to explain the process and answer all my questions, which really gave me confidence in their service. If you're looking for high-quality detailing and paint protection, I'd definitely recommend B&M Auto Detailing. Great customer service and outstanding results."},
    {"name": "Romal Sadat", "rating": 5, "date": "a week ago", "text": "B&M auto detailing is one of the best shop i visited there i had a great experience with them they are very friendly and they do work very professional i must recommend it to you guys."},
]

areas = ["Calgary", "Airdrie", "Chestermere", "Cochrane", "Okotoks", "Balzac", "Bearspaw", "Springbank"]

img = {
    "logo": "assets/images/bm-logo-official.svg",
    "logo_header": "assets/images/bm-logo-header.svg",
    "logo_mark": "assets/images/bm-logo-mark.svg",
    "hero": "assets/images/hero-premium-car-detail.jpg",
    "studio": "assets/images/studio-premium-vehicles.jpg",
    "detail": "assets/images/interior-detailing.jpg",
    "coating": "assets/images/ceramic-gloss-detail.jpg",
    "ppf": "assets/images/ppf-premium-vehicle.jpg",
    "correction": "assets/images/paint-correction-polishing.jpg",
    "interior": "assets/images/work-interior-reset.jpg",
    "front": "assets/images/work-front-end-protection.jpg",
    "og": "assets/images/og-bm-auto-detailing.jpg",
}

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("gallery.html", "Gallery"),
    ("packages.html", "Packages"),
    ("reviews.html", "Reviews"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

def page_shell(title, desc, body, active="", extra_schema=""):
    def public_href(href):
        return "/" if href == "index.html" else href
    nav = "".join(f'<a class="{ "active" if href == active else "" }" href="{public_href(href)}">{label}</a>' for href, label in NAV)
    service_links = "".join(f'<a href="{href}">{title}</a>' for href, title, *_ in services) + "".join(f'<a href="{href}">{label}</a>' for href, label in seo_service_links)
    canonical_path = "" if active == "index.html" else active
    canonical_url = f"{SITE_URL}/{canonical_path}"
    og_image_url = f"{SITE_URL}/{img['og']}"
    hero_preload = f'  <link rel="preload" as="image" href="{img["hero"]}" fetchpriority="high">\n' if active == "index.html" else ""
    robots_meta = '  <meta name="robots" content="noindex,follow">\n' if active in {"404.html", "admin.html"} else ""
    schema = f"""
    <script type="application/ld+json">{{
      "@context": "https://schema.org",
      "@type": "AutoRepair",
      "name": "{BUSINESS['name']}",
      "image": "{og_image_url}",
      "telephone": "{BUSINESS['phone']}",
      "email": "{BUSINESS['email']}",
      "address": {{"@type":"PostalAddress","streetAddress":"1247 36 Ave NE","addressLocality":"Calgary","addressRegion":"AB","postalCode":"T2E 6N6","addressCountry":"CA"}},
      "areaServed": "Calgary, Airdrie, Chestermere, Cochrane, Okotoks",
      "aggregateRating": {{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"21"}},
      "url": "{canonical_url}"
    }}</script>{extra_schema}
    """
    return f"""<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#0b0d0f">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og_image_url}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image_url}">
{robots_meta}  <meta name="theme-color" content="#080a0c">
  <link rel="canonical" href="{canonical_url}">
  <link rel="icon" href="{img['logo_mark']}" type="image/svg+xml">
{hero_preload.rstrip()}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">
  {schema}
</head>
<body class="page-{active.replace('.html','') or 'home'}">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <div class="top-line"><a href="tel:14034540203">{BUSINESS['phone']}</a><span>{BUSINESS['address']}</span><span>{BUSINESS['rating']} from {BUSINESS['reviews']}</span></div>
    <a class="brand" href="/" aria-label="B&M Auto Detailing home">
      <span class="brand-wordmark"><strong>B&amp;M</strong><span><b>Auto Detailing</b><small>Calgary vehicle protection</small></span></span>
    </a>
    <nav class="desktop-nav" aria-label="Main navigation">{nav}</nav>
    <a class="header-cta" href="contact.html">Book Now</a>
    <button class="menu-toggle" data-menu-toggle aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </header>
  <div class="mobile-panel" data-mobile-menu>
    <nav>{nav}<a class="mobile-book" href="contact.html">Book Now</a></nav>
  </div>
  <div class="mobile-sticky-cta"><a href="contact.html">Get a Quote</a><a href="tel:14034540203">Call Now</a></div>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="footer-grid">
      <div class="footer-about">
        <div class="brand footer-brand"><img class="brand-logo footer-logo" src="{img['logo']}" alt="B&M Auto Detailing" width="1350" height="280"></div>
        <p class="footer-copy">Window tint, PPF and paint protection, stereo upgrades, backup cameras, remote starters, and detailing support for Calgary drivers.</p>
      </div>
      <div class="footer-nav"><h3>Pages</h3>{nav}</div>
      <div class="footer-nav"><h3>Services</h3>{service_links}</div>
      <div class="footer-contact"><h3>Contact</h3><p>{BUSINESS['address']}<br>{BUSINESS['phone']}<br>{BUSINESS['email']}<br>{BUSINESS['hours']}</p><p>Serving {", ".join(areas[:5])} and nearby communities.</p></div>
    </div>
    <div class="footer-bottom"><span>© 2026 B&M Auto Detailing. All rights reserved.</span><span>Calgary window tint, PPF, stereo, backup camera, remote starter, and detailing services.</span><a class="site-credit" href="https://nebrex.ca" target="_blank" rel="noopener" aria-label="Website by Nebrex">Site by <strong>Nebrex.ca</strong></a></div>
  </footer>
  <script src="assets/site.js" defer></script>
</body>
</html>"""

def cta(label="Request a Quote"):
    return f"""<section class="final-cta">
  <div><p class="eyebrow">Calgary vehicle services</p><h2>Get a quote based on the vehicle, not a guess.</h2><p>Send the vehicle, service goal, and a few photos. B&M can recommend the right tint, PPF, paint protection, stereo, backup camera, remote starter, or detailing option.</p></div>
  <div class="cta-actions"><a class="btn primary" href="contact.html">{label}</a><a class="btn secondary" href="contact.html">Send Photos for Pricing</a><a class="btn glass" href="tel:14034540203">{BUSINESS['phone']}</a></div>
</section>"""

def map_embed(label="B&M Auto Detailing on Google Maps"):
    return f"""<div class="map-embed">
  <iframe title="{label}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  <a href="{MAP_URL}" target="_blank" rel="noopener">Open official Google Maps listing</a>
</div>"""

def admin_portal():
    return f"""<section class="admin-shell" data-admin-portal>
  <div class="admin-login" data-admin-login>
    <div>
      <p class="eyebrow">Admin portal</p>
      <h1>B&M website control centre.</h1>
      <p>Secure client access for website status, update requests, business links, and Nebrex-managed website support.</p>
    </div>
    <form class="portal-card" data-admin-form>
      <div class="brand portal-brand"><img class="brand-logo portal-logo" src="{img['logo']}" alt="B&M Auto Detailing" width="1350" height="280"></div>
      <label>Admin email<input type="email" data-admin-email autocomplete="email" placeholder="admin@bmautodetailing.ca" required></label>
      <label>Password<input type="password" data-admin-password autocomplete="current-password" placeholder="Enter portal password" required></label>
      <p class="portal-hint">Authorized B&M admin access only.</p>
      <p class="portal-error" data-admin-error hidden>Incorrect admin email or password.</p>
      <button class="btn primary" type="submit">Sign in</button>
    </form>
  </div>
  <div class="admin-dashboard" data-admin-dashboard hidden>
    <div class="admin-layout">
      <aside class="admin-sidebar">
        <div class="brand portal-brand"><img class="brand-logo admin-logo" src="{img['logo_mark']}" alt="B&M Auto Detailing admin" width="420" height="260"><span><strong>Admin</strong><small>Control panel</small></span></div>
        <a href="#overview">Overview</a>
        <a href="#analytics">Analytics</a>
        <a href="#content">Content</a>
        <a href="#requests">Requests</a>
        <a href="#settings">Settings</a>
      </aside>
      <div class="admin-main">
        <div class="dashboard-hero" id="overview">
          <div>
            <p class="eyebrow">Welcome, admin</p>
            <h1>B&M Auto Detailing control panel.</h1>
            <p>Website ownership, traffic visibility, update requests, service content, and Nebrex support are organized here so the public site stays clean, current, and professional.</p>
          </div>
          <button class="btn glass" type="button" data-admin-logout>Sign out</button>
        </div>
        <div class="admin-topbar">
          <span>Role: Website Admin</span>
          <span>Status: Live</span>
          <span data-current-login>Last login: Active session</span>
        </div>
        <div class="metric-grid">
          <article class="metric-card"><span>Website status</span><strong>Online</strong><p>Public website is published.</p></article>
          <article class="metric-card"><span>Google rating</span><strong>4.8</strong><p>21 public reviews shown on site.</p></article>
          <article class="metric-card"><span>Page views</span><strong data-stat="pageviews">Connect</strong><p data-stat-note="pageviews">Waiting for Cloudflare analytics.</p></article>
          <article class="metric-card attention"><span>Visits</span><strong data-stat="visits">Connect</strong><p data-stat-note="visits">Waiting for Cloudflare analytics.</p></article>
        </div>
        <section class="portal-section" id="analytics">
          <div class="section-head"><p class="eyebrow">Analytics</p><h2>Traffic dashboard ready for live visitor data.</h2><p>Once Cloudflare Web Analytics is connected, this area can show visits, top pages, device split, search traffic, and quote-button activity.</p></div>
          <div class="analytics-panel">
            <div class="chart-card">
              <div class="chart-head"><span>Visits preview</span><strong data-stat="analytics-status">Awaiting analytics connection</strong></div>
              <div class="bar-chart" data-analytics-bars aria-label="Analytics preview bars"><span style="height:38%"></span><span style="height:62%"></span><span style="height:48%"></span><span style="height:74%"></span><span style="height:56%"></span><span style="height:82%"></span><span style="height:68%"></span></div>
            </div>
            <div class="admin-list compact">
              <article><h3>Top pages</h3><p data-stat="top-pages">Home, Services, Packages, Contact, and Admin are ready to track after analytics setup.</p></article>
              <article><h3>Lead actions</h3><p data-stat="lead-actions">Get Quote, Call Now, Google Maps, and Request Website Edit buttons are ready for click tracking.</p></article>
            </div>
          </div>
        </section>
        <div class="dashboard-grid">
          <article class="portal-card status-good"><span>Live site</span><strong>bmautodetailing.ca</strong><p>Published and connected to the Calgary business website.</p><a class="text-link" href="/" target="_blank" rel="noopener">Open website</a></article>
          <article class="portal-card"><span>Business phone</span><strong>{BUSINESS['phone']}</strong><p>Visible on the website header, contact page, and mobile call button.</p><a class="text-link" href="tel:14034540203">Call shop</a></article>
          <article class="portal-card"><span>Google listing</span><strong>Calgary location</strong><p>{BUSINESS['address']}</p><a class="text-link" href="{MAP_URL}" target="_blank" rel="noopener">Open Maps</a></article>
        </div>
        <section class="portal-section" id="content">
          <div class="section-head"><p class="eyebrow">Content controls</p><h2>Website areas B&M can request updates for.</h2><p>The portal keeps common website updates organized without exposing the layout or SEO structure to accidental changes.</p></div>
          <div class="control-grid">
            <article><span>Services</span><strong>6 active</strong><p>Tint, PPF, stereo, backup camera, remote starter, and detailing.</p><a href="services.html">View services</a></article>
            <article><span>Packages</span><strong>Pricing guide</strong><p>Quote paths and starting points can be updated when services change.</p><a href="packages.html">View packages</a></article>
            <article><span>Gallery</span><strong>Photo ready</strong><p>New project photos can be sent for upload and replacement.</p><a href="gallery.html">View gallery</a></article>
            <article><span>Reviews</span><strong>4.8 rating</strong><p>Selected Google reviews are visible for trust and conversion.</p><a href="reviews.html">View reviews</a></article>
          </div>
        </section>
        <section class="portal-section" id="requests">
          <div class="section-head"><p class="eyebrow">Request changes</p><h2>Send updates without editing the website directly.</h2><p>Use these actions for service changes, photos, pricing, hours, or review updates. Nebrex can update the site so the layout stays consistent.</p></div>
          <div class="portal-actions">
            <a class="btn primary" href="mailto:bookings@bmautodetailing.ca?subject=Website%20Update%20Request&body=Please%20describe%20the%20website%20change%20needed%3A%0A%0AService%2Fpage%3A%0AChange%3A%0APhotos%20attached%3A%20Yes%2FNo">Request website edit</a>
            <a class="btn glass" href="mailto:bookings@bmautodetailing.ca?subject=Upload%20New%20Website%20Photos">Send new photos</a>
            <a class="btn glass" href="contact.html">View customer quote form</a>
          </div>
        </section>
        <section class="portal-section" id="settings">
          <div class="admin-list">
            <article><h3>Editable with Nebrex support</h3><p>Services, prices, photos, reviews, hours, phone, address, gallery work, and page copy.</p></article>
            <article><h3>Protected from accidental changes</h3><p>Website layout, mobile design, SEO structure, speed setup, and core navigation remain managed.</p></article>
            <article><h3>Security recommendation</h3><p>Use Cloudflare Access on /admin.html so only the approved admin email can open this portal.</p></article>
          </div>
        </section>
      </div>
    </div>
  </div>
</section>"""

def service_cards():
    service_images = [img["detail"], img["ppf"], img["studio"], img["interior"], img["front"], img["detail"]]
    return "".join(f"""<article class="service-card">
  <img src="{service_images[i]}" alt="{title} Calgary service example" loading="lazy">
  <div class="service-card-body"><p class="card-kicker">Calgary service</p><h3>{title}</h3><p>{desc}</p><ul>{''.join(f'<li>{b}</li>' for b in bullets)}</ul><a class="service-link" href="{href}">View {title}</a></div>
</article>""" for i, (href, title, desc, bullets) in enumerate(services))

def package_cards(limit=None, items=None):
    source = packages if items is None else items
    items = source if limit is None else source[:limit]
    return "".join(f"""<article class="package-card">
  <p class="package-price">{price}</p><h3>{name}</h3><p class="muted">Best for: {best}</p><p>{included}</p><div class="package-meta"><span><small>Time</small><strong>{duration}</strong></span><span><small>Price</small><strong>{price}</strong></span></div><a class="btn small" href="contact.html">Request package</a>
</article>""" for name, best, included, duration, price in items)

def package_comparison():
    rows = [
        ("Window Tint Package", "Drivers wanting privacy, glare reduction, and a cleaner look", "Film consultation, shade selection, vehicle prep, installation, and aftercare", "Final shade and film type are confirmed before install", "Quote required"),
        ("Front-End PPF Package", "New vehicles and highway drivers exposed to road debris", "Coverage planning for bumper, hood, fenders, mirrors, and impact areas", "Detailing or accessories are quoted separately unless bundled", "Custom quote"),
        ("Stereo Upgrade", "Drivers wanting better sound or modern media controls", "Audio/head unit options, installation planning, wiring, and function check", "Speaker, amp, or subwoofer scope changes final price", "Custom quote"),
        ("Backup Camera Install", "Vehicles needing better rear visibility", "Camera selection, mounting, wiring, display integration, and testing", "Display or head unit upgrades may be separate", "Custom quote"),
        ("Remote Starter Install", "Calgary drivers wanting winter convenience", "Vehicle-specific starter planning, installation, setup, and handoff", "Final price depends on vehicle, remote range, and module needs", "Custom quote"),
        ("Detailing Add-On", "Vehicles needing a clean reset", "Interior/exterior cleanup options before pickup or after install work", "Heavy stains, pet hair, or large vehicles may change pricing", "From $179"),
    ]
    return """<div class="package-compare-cards">""" + "".join(
        f"""<article><div><p class="package-price">{price}</p><h3>{name}</h3><p>{best}</p></div><dl><dt>Expected outcome</dt><dd>{outcome}</dd><dt>Not included unless added</dt><dd>{not_included}</dd></dl><a class="btn small" href="contact.html">Get a Quote</a></article>"""
        for name, best, outcome, not_included, price in rows
    ) + "</div>"

def faq_block(limit=None):
    items = faqs if limit is None else faqs[:limit]
    return '<div class="faq-list">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def review_cards(limit=None):
    display_reviews = [
        review for review in google_reviews
        if review["rating"] >= 5 and not review["text"].startswith("5-star Google rating")
    ]
    items = display_reviews if limit is None else display_reviews[:limit]
    return "".join(
        f"""<article class="google-review">
  <div class="review-top"><strong>{review['name']}</strong><span aria-label="{review['rating']} star Google review">★★★★★</span></div>
  <p class="review-date">Google review · {review['date']}</p>
  <p>{review['text']}</p>
</article>"""
        for review in items
    )

def intent_reviews():
    items = [
        ("Interior detailing", google_reviews[2]),
        ("Detailing results", google_reviews[1]),
        ("PPF and protection", google_reviews[11]),
    ]
    return "".join(
        f"""<article class="google-review intent-review"><p class="card-kicker">{label}</p><div class="review-top"><strong>{review['name']}</strong><span aria-label="{review['rating']} star Google review">★★★★★</span></div><p class="review-date">Google review · {review['date']}</p><p>{review['text']}</p></article>"""
        for label, review in items
    )

def trust_bar():
    return f"""<section class="trust-strip">
  <a href="contact.html"><strong>Calgary shop</strong><span>{BUSINESS['address']}</span></a>
  <a href="reviews.html"><strong>{BUSINESS['rating']}</strong><span>{BUSINESS['reviews']} on the public listing</span></a>
  <a href="window-tint.html"><strong>Window tint</strong><span>Privacy, glare reduction, and cleaner vehicle appearance</span></a>
  <a href="paint-protection-film.html"><strong>PPF + paint protection</strong><span>Coverage recommendations based on how the vehicle is driven</span></a>
</section>"""

def home():
    body = f"""
<section class="hero home-hero">
  <img src="{img['hero']}" alt="Premium automotive detailing studio finish on a dark vehicle" fetchpriority="high" decoding="async">
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <p class="eyebrow">1247 36 Ave NE, Calgary</p>
    <h1>Window tint, PPF, stereo, backup camera, remote starter, and detailing in Calgary.</h1>
    <p>B&M Auto Detailing helps Calgary drivers add protection, comfort, visibility, sound, and convenience with practical vehicle services under one roof.</p>
    <div class="hero-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="contact.html">Send Photos for Pricing</a></div>
    <div class="hero-points"><span>{BUSINESS['rating']} from {BUSINESS['reviews']}</span><span>Calgary shop</span><span>Window tint and paint protection</span><span>Vehicle electronics and accessories</span></div>
  </div>
</section>
{trust_bar()}
<section class="quick-paths">
  <a href="window-tint.html"><span>01</span><strong>Window tint</strong><em>Privacy, glare, UV, appearance</em></a>
  <a href="paint-protection-film.html"><span>02</span><strong>PPF protection</strong><em>Rock chips and front-end coverage</em></a>
  <a href="backup-camera.html"><span>03</span><strong>Backup camera</strong><em>Rear visibility and parking support</em></a>
  <a href="remote-starter.html"><span>04</span><strong>Remote starter</strong><em>Calgary winter convenience</em></a>
</section>
<section class="section"><div class="section-head"><p class="eyebrow">Services</p><h2>Vehicle protection, accessories, electronics, and detailing.</h2><p>Choose tint for comfort and privacy, PPF for paint protection, electronics for function, and detailing when the vehicle needs a cleaner reset.</p></div><div class="service-grid">{service_cards()}</div><div class="section-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="services.html">Compare Services</a></div></section>
<section class="split-section">
  <div><p class="eyebrow">Why B&M</p><h2>One shop for practical upgrades and protection.</h2><p>Some customers need tint and front-end protection. Some need a remote starter before winter. Some want a cleaner stereo setup, a backup camera, or a detail before pickup. B&M scopes the job around the vehicle and the result the customer actually wants.</p><div class="proof-list"><span>Vehicle reviewed before quoting</span><span>Tint, PPF, and accessory planning</span><span>Clean install approach</span><span>Aftercare and handoff guidance</span></div></div>
  <img src="{img['studio']}" alt="Clean premium automotive studio environment" loading="lazy">
</section>
<section class="section dark-band"><div class="section-head stacked"><p class="eyebrow">Proof of work</p><h2>Visual proof matters in detailing and protection.</h2><p>Interior condition, paint clarity, gloss, and front-end protection all need to be seen clearly before a customer trusts the process.</p></div><div class="before-grid">
  <article class="before-card"><img class="proof-image" src="{img['interior']}" alt="Interior detailing and seat cleaning example" loading="lazy"><h3>Interior reset</h3><p>Interior cleaning for high-use vehicles with dust, spills, salt, and daily wear.</p></article>
  <article class="before-card"><img class="proof-image" src="{img['ppf']}" alt="Paint protection film and vehicle protection example" loading="lazy"><h3>PPF and paint protection</h3><p>Front-end protection planning for rock-chip-prone Calgary driving.</p></article>
  <article class="before-card"><img class="proof-image" src="{img['studio']}" alt="Vehicle electronics and accessories service example" loading="lazy"><h3>Vehicle accessories</h3><p>Stereo, backup camera, remote starter, and practical upgrade planning.</p></article>
</div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Packages</p><h2>Quote paths for the services customers ask about most.</h2><p>Final pricing depends on vehicle model, film or accessory selection, wiring/integration needs, coverage area, and vehicle condition.</p></div>{package_comparison()}</section>
<section class="section seo-hub"><div class="section-head"><p class="eyebrow">Service paths</p><h2>High-intent Calgary service pages.</h2><p>Use these pages when you already know the service you are comparing or searching for.</p></div><div class="hub-grid">{''.join(f'<a href="{href}">{label} Calgary<span>View service page</span></a>' for href, label in seo_service_links)}</div></section>
<section class="process-section"><p class="eyebrow">Process</p><h2>Send details. Confirm the service. Book the right install.</h2><div class="steps"><article><span>01</span><h3>Send vehicle details</h3><p>Share the year, make, model, requested service, and helpful photos.</p></article><article><span>02</span><h3>Get the right scope</h3><p>B&M confirms tint, PPF, stereo, camera, starter, detailing, or accessory requirements.</p></article><article><span>03</span><h3>Confirm timing</h3><p>Appointment timing, product options, and quote range are confirmed first.</p></article><article><span>04</span><h3>Pick up with handoff</h3><p>Leave with the work completed and basic use or aftercare guidance.</p></article></div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Customer reviews</p><h2>Proof tied to what buyers care about.</h2><p>Interior cleanup, exterior results, and protection work each create a different kind of trust.</p></div><div class="review-grid">{intent_reviews()}</div><div class="section-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="reviews.html">Read Google Reviews</a></div></section>
<section class="local-section"><div><p class="eyebrow">Calgary location</p><h2>Visit B&M Auto Detailing in NE Calgary.</h2><p>B&M Auto Detailing serves Calgary drivers and nearby communities including Airdrie, Chestermere, Cochrane, and Okotoks.</p><div class="area-tags">{''.join(f'<span>{a}</span>' for a in areas)}</div></div>{map_embed("B&M Auto Detailing Calgary Google Maps location")}</section>
<section class="section faq-preview"><div class="section-head"><p class="eyebrow">FAQ</p><h2>Answers that affect the quote.</h2></div>{faq_block(6)}</section>
{cta()}
"""
    return page_shell("B&M Auto Detailing | Window Tint, PPF, Stereo & Remote Starter Calgary", "Window tint, PPF, paint protection, car stereo, backup camera, remote starter, and detailing services in Calgary, Alberta.", body, "index.html")

service_details = {
    "auto-detailing.html": ("Auto Detailing Calgary", "Interior and exterior detailing packages for Calgary cars, SUVs, trucks, lease returns, and seasonal refreshes.", ["Interior Detailing", "Exterior Detailing", "Full Detail Packages", "Pet hair, salt, stain, odor, and engine bay add-ons"], "Detailing is for vehicles that need a controlled reset rather than a quick wash. B&M builds packages around vehicle size, interior condition, exterior contamination, and whether the customer is preparing for sale, lease return, winter recovery, or regular upkeep.", img["detail"]),
    "window-tint.html": ("Window Tint Calgary", "Window tint installation in Calgary for privacy, glare reduction, UV protection, comfort, and vehicle appearance.", ["Shade and film consultation", "Vehicle glass preparation", "Clean installation process", "Aftercare guidance"], "Window tint is one of the most requested upgrades for Calgary drivers who want a cleaner look, more privacy, less glare, and better cabin comfort. B&M confirms vehicle type, shade goals, and film options before booking.", img["studio"]),
    "paint-protection-film.html": ("PPF and Paint Protection Calgary", "Paint protection film and clear bra packages for Calgary rock chips, road debris, winter driving, highways, and new vehicle protection.", ["Partial front", "Full front", "High-impact zones", "Rocker panels, mirrors, door cups, and trunk ledges"], "PPF is a strong option for physical paint protection. It is ideal for new vehicles, highway drivers, luxury vehicles, trucks, and owners who want to reduce rock-chip damage in Alberta conditions.", img["ppf"]),
    "car-stereo.html": ("Car Stereo Installation Calgary", "Car stereo, audio, and head unit installation in Calgary for cleaner sound, updated controls, and practical in-vehicle upgrades.", ["Stereo and head unit options", "Audio upgrade planning", "Clean wiring approach", "Function check before pickup"], "Stereo work depends on the vehicle, existing system, desired sound, and integration needs. B&M confirms the setup before recommending a simple head unit install, speaker upgrade, or broader audio path.", img["front"]),
    "backup-camera.html": ("Backup Camera Installation Calgary", "Backup camera installation in Calgary for better rear visibility, parking support, and safer reversing.", ["Camera selection", "Mounting plan", "Wiring and display integration", "Function test"], "Backup camera installs are useful for older vehicles, trucks, SUVs, work vehicles, and daily drivers that need better reversing visibility. The correct setup depends on the vehicle and display options.", img["interior"]),
    "remote-starter.html": ("Remote Starter Installation Calgary", "Remote starter installation in Calgary for winter convenience, comfort, and vehicle-specific setup.", ["Vehicle-specific planning", "Remote range options", "Install and setup", "Basic handoff guidance"], "Remote starters are practical for Calgary winters. B&M reviews the vehicle and remote options before confirming the install path, timing, and quote.", img["studio"]),
}

service_package_map = {
    "window-tint.html": [packages[0], packages[5]],
    "paint-protection-film.html": [packages[1], packages[5]],
    "car-stereo.html": [packages[2]],
    "backup-camera.html": [packages[3]],
    "remote-starter.html": [packages[4]],
    "auto-detailing.html": [packages[5], packages[0], packages[1]],
}

def service_page(filename):
    h1, meta, includes, intro, image_url = service_details[filename]
    service_packages = service_package_map.get(filename, packages[:3])
    body = f"""
<section class="subhero">
  <div><p class="eyebrow">B&M Auto Detailing</p><h1>{h1}</h1><p>{meta}</p><div class="hero-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="contact.html">Send Photos for Pricing</a></div></div>
  <img src="{image_url}" alt="{h1} professional result" loading="eager" decoding="async">
</section>
{trust_bar()}
<section class="split-section"><div><p class="eyebrow">Service overview</p><h2>Scoped by condition, not by a generic menu.</h2><p>{intro}</p><div class="proof-list">{''.join(f'<span>{item}</span>' for item in includes)}</div></div><div class="info-panel"><h3>Best for</h3><ul><li>Daily drivers that need easier maintenance</li><li>New vehicles needing early protection</li><li>Luxury and European vehicles</li><li>Trucks, SUVs, lease returns, and sale prep</li></ul></div></section>
<section class="section"><div class="section-head"><p class="eyebrow">What is included</p><h2>Clear scope before the appointment.</h2><p>The final recommendation depends on vehicle model, product selection, installation needs, wiring/integration requirements, protection coverage, and vehicle condition.</p></div><div class="feature-grid"><article><h3>Review</h3><p>Vehicle details, requested service, product options, and timing are reviewed before the work is confirmed.</p></article><article><h3>Preparation</h3><p>Glass, panels, interior trim, wiring paths, or service areas are prepared according to the job.</p></article><article><h3>Install or service</h3><p>Tint, PPF, stereo, backup camera, remote starter, detailing, or accessory work is completed with a controlled process.</p></article><article><h3>Handoff</h3><p>Customers receive practical use, care, or aftercare guidance before pickup.</p></article></div></section>
<section class="section dark-band"><div class="section-head stacked"><p class="eyebrow">Packages</p><h2>Packages that fit this service.</h2><p>These are common starting points. The final recommendation is confirmed after B&M reviews the vehicle condition, finish goals, and protection needs.</p></div><div class="package-grid service-packages">{package_cards(items=service_packages)}</div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Common questions</p><h2>Before you book.</h2></div>{faq_block(5)}</section>
{cta("Get a Quote")}
"""
    return page_shell(f"{h1} | B&M Auto Detailing", meta, body, filename)

def simple_page(filename, title, desc, body):
    return page_shell(title, desc, body, filename)

seo_pages = {
    "interior-detailing.html": {
        "title": "Interior Detailing Calgary | B&M Auto Detailing",
        "desc": "Interior detailing in Calgary for salt stains, pet hair, spills, upholstery, leather, carpets, vents, and lease return cleanup.",
        "h1": "Interior detailing for Calgary daily use.",
        "intro": "Interior detailing should be scoped by condition. Winter salt, kids, pets, work vehicles, coffee spills, dust, and lease return expectations all change the amount of work needed.",
        "items": ["Carpet and mat cleaning", "Seat and upholstery attention", "Pet hair and salt-stain add-ons", "Glass, vents, plastics, and touch points"],
    },
    "exterior-detailing.html": {
        "title": "Exterior Detailing Calgary | B&M Auto Detailing",
        "desc": "Exterior detailing in Calgary for hand washing, decontamination, wheel cleaning, glass, and vehicle cleanup.",
        "h1": "Exterior detailing for paint, glass, wheels, and trim.",
        "intro": "Calgary vehicles collect road film, mineral deposits, construction dust, tar, winter residue, and wash buildup. Exterior detailing helps reset the outside of the vehicle before or after tint, PPF, accessory, or protection work.",
        "items": ["Paint-safe wash process", "Wheel and tire cleaning", "Glass and trim attention", "Add-on cleanup before pickup"],
    },
    "new-vehicle-protection.html": {
        "title": "New Vehicle Protection Calgary | B&M Auto Detailing",
        "desc": "New vehicle protection and accessory planning in Calgary with PPF, window tint, detailing, remote starter, backup camera, and stereo options.",
        "h1": "New vehicle protection before Calgary roads leave their mark.",
        "intro": "New vehicles are easier to protect and upgrade early. B&M can help plan window tint, front-end PPF, remote starter, backup camera, stereo upgrades, and detailing before daily driving takes over.",
        "items": ["PPF coverage consultation", "Window tint planning", "Remote starter and camera options", "Detailing and pickup cleanup"],
    },
}

pages = {
    "index.html": home(),
    "services.html": simple_page("services.html", "Services | B&M Auto Detailing Calgary", "Overview of B&M Auto Detailing services including window tint, PPF, paint protection, stereo, backup camera, remote starter, and detailing in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Services</p><h1>Window tint, protection, accessories, electronics, and detailing.</h1><p>B&M offers practical vehicle services for Calgary drivers: window tint, PPF and paint protection, stereo upgrades, backup camera installation, remote starters, and detailing support.</p></div></section><section class="section"><div class="service-grid">{service_cards()}</div></section>{cta()}"""),
    "packages.html": simple_page("packages.html", "Packages and Pricing Guide | B&M Auto Detailing", "Compare window tint, PPF, stereo, backup camera, remote starter, and detailing quote paths in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Packages</p><h1>Quote paths and service guide.</h1><p>Use these service paths as a starting point. Final pricing depends on vehicle model, product selection, installation needs, wiring/integration requirements, coverage area, and vehicle condition.</p><div class="hero-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="contact.html">Send Photos for Pricing</a></div></div></section><section class="section">{package_comparison()}</section><section class="section dark-band"><div class="comparison"><h2>Quick comparison</h2><table><thead><tr><th>Service</th><th>Best for</th><th>Timing</th><th>Starting point</th></tr></thead><tbody>{''.join(f'<tr><td data-label="Service">{n}</td><td data-label="Best for">{b}</td><td data-label="Timing">{d}</td><td data-label="Starting point">{p}</td></tr>' for n,b,i,d,p in packages)}</tbody></table></div></section>{cta()}"""),
    "gallery.html": simple_page("gallery.html", "Gallery and Work Examples | B&M Auto Detailing", "Gallery and work examples for window tint, PPF, detailing, and vehicle accessory services in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Gallery</p><h1>Vehicle service and protection examples.</h1><p>A visual overview of the service categories customers ask about most: detailing resets, PPF coverage, window tint, and vehicle accessory work.</p></div></section><section class="section"><div class="filter-row"><button class="active">All</button><button>Tint</button><button>PPF</button><button>Accessories</button><button>Detailing</button></div><div class="gallery-grid">{''.join(f'<figure><img src="{url}" alt="{cap}"><figcaption>{cap}</figcaption></figure>' for url, cap in [(img['interior'],'Interior detailing reset'),(img['ppf'],'Paint protection film planning'),(img['studio'],'Vehicle accessory service'),(img['front'],'Backup camera and electronics planning'),(img['detail'],'Exterior cleanup and detailing')])}</div></section>{cta()}"""),
    "reviews.html": simple_page("reviews.html", "Customer Reviews | B&M Auto Detailing Calgary", "Customer reviews for B&M Auto Detailing in Calgary, including detailing, PPF, communication, pricing, and finished vehicle results.", f"""<section class="subhero text-only reviews-hero"><div><p class="eyebrow">Customer reviews</p><h1>Calgary drivers trust B&M with detailing and protection work.</h1><p>Customers mention clean interiors, strong exterior results, fair pricing, professional communication, PPF installation, and vehicles looking better than expected after service.</p><div class="hero-actions"><a class="btn primary" href="contact.html">Request a quote</a><a class="btn glass" href="https://www.google.com/search?q=bm+auto+detailing+calgary#lrd=0x5371650076e95fa9:0xb4fd3f6c4e98f878,1,,,," target="_blank" rel="noopener">View on Google</a></div></div></section><section class="review-stats"><article><strong>4.8</strong><span>Google rating</span></article><article><strong>21</strong><span>Public reviews</span></article><article><strong>Calgary</strong><span>1247 36 Ave NE</span></article></section><section class="section"><div class="section-head"><p class="eyebrow">Review highlights</p><h2>Detailing, PPF, communication, and clean results.</h2><p>Selected written Google reviews are shown in the customer's own words, with names and dates attached for credibility.</p></div><div class="review-grid large">{review_cards()}</div></section>{cta()}"""),
    "about.html": simple_page("about.html", "About B&M Auto Detailing | Calgary", "About B&M Auto Detailing, a Calgary vehicle service shop for tint, PPF, stereo, backup camera, remote starter, and detailing services.", f"""<section class="subhero"><div><p class="eyebrow">About</p><h1>A Calgary shop for practical vehicle upgrades and protection.</h1><p>B&M Auto Detailing helps drivers with window tint, PPF and paint protection, stereo upgrades, backup cameras, remote starters, detailing, and related vehicle service work.</p></div><img src="{img['studio']}" alt="B&M Auto Detailing Calgary service shop"></section><section class="split-section"><div><p class="eyebrow">Approach</p><h2>Clear service planning without inflated promises.</h2><p>The right install starts with the vehicle. B&M reviews the year, make, model, requested service, product choices, and integration needs before confirming the quote and appointment.</p></div><div class="info-panel"><h3>Why Calgary drivers book</h3><ul><li>Window tint for comfort, privacy, and appearance</li><li>PPF for rock-chip and road-debris protection</li><li>Remote starters for winter convenience</li><li>Backup camera, stereo, and accessory upgrades</li></ul></div></section>{cta()}"""),
    "faq.html": simple_page("faq.html", "FAQ | B&M Auto Detailing Calgary", "Answers to common Calgary window tint, PPF, stereo, backup camera, remote starter, and detailing questions.", f"""<section class="subhero text-only"><div><p class="eyebrow">FAQ</p><h1>Answers before the quote.</h1><p>Clear expectations help customers choose the right service and understand what affects timing, product selection, install requirements, and pricing.</p></div></section><section class="section">{faq_block()}</section>{cta()}"""),
    "contact.html": simple_page("contact.html", "Contact and Book Now | B&M Auto Detailing Calgary", "Request a quote or book B&M Auto Detailing in Calgary for window tint, PPF, stereo, backup camera, remote starter, and detailing.", f"""<section class="subhero text-only"><div><p class="eyebrow">Book now</p><h1>Request a quote for tint, PPF, stereo, camera, starter, or detailing.</h1><p>Send the vehicle details, preferred service, timing, and condition notes. Photos of the windows, dashboard, stereo area, rear camera area, paint protection zones, or interior help scope the job.</p></div></section><section class="contact-layout"><form class="quote-form" action="mailto:{BUSINESS['email']}" method="post" enctype="text/plain"><label>Name<input name="name" autocomplete="name"></label><label>Phone<input name="phone" autocomplete="tel"></label><label>Email<input type="email" name="email" autocomplete="email"></label><label>Vehicle year<input name="year"></label><label>Vehicle make<input name="make"></label><label>Vehicle model<input name="model"></label><label>Service interested in<select name="service"><option>Window tint</option><option>Paint protection film / PPF</option><option>Paint protection</option><option>Car stereo / audio</option><option>Backup camera</option><option>Remote starter</option><option>Auto detailing</option><option>Other vehicle service</option></select></label><label>Preferred date<input type="date" name="date"></label><label>Upload photos<input type="file" name="photos" multiple></label><label>How did you hear about us?<input name="source"></label><label class="full">Message / notes<textarea name="message" rows="5"></textarea></label><button class="btn primary" type="submit">Send quote request</button></form><aside class="contact-card"><h2>Contact</h2><p>{BUSINESS['address']}</p><p><a href="tel:14034540203">{BUSINESS['phone']}</a><br><a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a></p><p>{BUSINESS['hours']}</p>{map_embed("B&M Auto Detailing Calgary Google Maps location")}</aside></section>"""),
    "service-areas.html": simple_page("service-areas.html", "Calgary Service Areas | B&M Auto Detailing", "B&M Auto Detailing serves Calgary, Airdrie, Chestermere, Cochrane, Okotoks, and nearby Alberta communities.", f"""<section class="subhero text-only"><div><p class="eyebrow">Service areas</p><h1>Calgary and nearby communities.</h1><p>B&M serves Calgary and nearby communities for window tint, PPF, paint protection, stereo, backup camera, remote starter, and detailing services.</p></div></section><section class="local-section"><div class="area-tags">{''.join(f'<span>{a}</span>' for a in areas)}</div></section>{cta()}"""),
    "care-tips.html": simple_page("care-tips.html", "Care Tips | B&M Auto Detailing", "Vehicle care tips for Calgary window tint, PPF, remote starter, backup camera, stereo, and detailing services.", f"""<section class="subhero text-only"><div><p class="eyebrow">Care tips</p><h1>Practical vehicle service guidance for Calgary drivers.</h1><p>Focused guidance for tint aftercare, PPF care, remote starter planning, backup camera installs, stereo upgrades, and seasonal detailing.</p></div></section><section class="section"><div class="feature-grid"><article><h3>After window tint installation</h3><p>Follow the installer guidance before rolling windows down and allow the film to cure properly based on conditions.</p></article><article><h3>Choosing PPF coverage</h3><p>High-impact areas such as front bumper, hood, mirrors, and rockers are common starting points for Calgary driving.</p></article><article><h3>Before an electronics install</h3><p>Share the year, make, model, current screen or stereo setup, and photos of the dashboard or rear camera area.</p></article></div></section>{cta()}"""),
    "admin.html": simple_page("admin.html", "Client Portal | B&M Auto Detailing", "Private B&M Auto Detailing client portal for website status, edit requests, business links, and Nebrex support.", admin_portal()),
    "404.html": simple_page("404.html", "Page Not Found | B&M Auto Detailing Calgary", "The requested B&M Auto Detailing page could not be found.", """<section class="subhero text-only"><div><p class="eyebrow">Page not found</p><h1>This page is not available.</h1><p>The service may have moved, or the old link may no longer be used. Start from the homepage or request a quote for tint, PPF, stereo, backup camera, remote starter, or detailing.</p><div class="hero-actions"><a class="btn primary" href="/">Back to homepage</a><a class="btn glass" href="contact.html">Request a quote</a></div></div></section>"""),
}

for filename, data in seo_pages.items():
    body = f"""<section class="subhero text-only"><div><p class="eyebrow">Calgary vehicle service</p><h1>{data['h1']}</h1><p>{data['intro']}</p><div class="hero-actions"><a class="btn primary" href="contact.html">Request a quote</a><a class="btn glass" href="tel:14034540203">Call {BUSINESS['phone']}</a></div></div></section>
<section class="section"><div class="section-head"><p class="eyebrow">What customers ask for</p><h2>Clear service scope, plain language.</h2><p>This page supports a specific search intent while still moving the customer toward the right quote instead of a generic booking form.</p></div><div class="feature-grid">{''.join(f'<article><h3>{item}</h3><p>B&M confirms vehicle size, current condition, timing, and any add-ons before the appointment is booked.</p></article>' for item in data['items'])}</div></section>
<section class="section dark-band"><div class="section-head"><p class="eyebrow">Related services</p><h2>Often booked together.</h2></div><div class="hub-grid"><a href="window-tint.html">Window tint<span>Privacy and glare reduction</span></a><a href="paint-protection-film.html">PPF and paint protection<span>Rock-chip defence</span></a><a href="backup-camera.html">Backup camera<span>Rear visibility</span></a><a href="remote-starter.html">Remote starter<span>Winter convenience</span></a><a href="car-stereo.html">Car stereo<span>Audio and head unit upgrades</span></a><a href="auto-detailing.html">Auto detailing<span>Interior and exterior cleanup</span></a></div></section>{cta()}"""
    pages[filename] = simple_page(filename, data["title"], data["desc"], body)

for filename in service_details:
    pages[filename] = service_page(filename)

CSS = r"""
:root{--black:#080a0c;--graphite:#0d1114;--panel:#14191d;--line:#273039;--text:#f4f1eb;--muted:#a7adb1;--soft:#d8d2c8;--accent:#a8875d;--accent2:#5c7374;--max:1180px}
*{box-sizing:border-box}[hidden]{display:none!important}html{scroll-behavior:smooth;scroll-padding-top:112px}body{margin:0;background:var(--black);color:var(--text);font-family:"Manrope","Aptos","Segoe UI",Arial,sans-serif;line-height:1.58;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.skip-link{position:absolute;left:-999px;top:1rem;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}.skip-link:focus{left:1rem;width:auto;height:auto;clip-path:none;z-index:99;background:#fff;color:#000;padding:.8rem 1rem;min-height:44px}.site-header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:1.4rem;padding:2.55rem clamp(1rem,3vw,2.25rem) 1rem;background:rgba(8,10,12,.83);border-bottom:1px solid rgba(255,255,255,.08);backdrop-filter:blur(18px)}.top-line{position:absolute;left:0;right:0;top:0;display:flex;justify-content:center;gap:1.2rem;padding:.45rem 1rem;border-bottom:1px solid rgba(255,255,255,.07);color:var(--muted);font-size:.78rem}.top-line a{color:var(--soft);font-weight:760}.brand{display:flex;align-items:center;gap:.75rem;min-width:max-content}.brand-logo{display:block;width:clamp(12.5rem,18vw,19.5rem);height:auto}.footer-logo{width:min(21rem,100%)}.portal-logo{width:min(24rem,100%)}.admin-logo{width:3.25rem;max-width:none}.brand strong{display:block;font-size:.9rem;letter-spacing:.035em;text-transform:uppercase;font-weight:700}.brand small{display:block;color:var(--muted);font-size:.72rem}.desktop-nav{display:flex;gap:1.1rem;margin-left:auto}.desktop-nav a,.site-footer a{color:var(--muted);font-size:.9rem}.desktop-nav a:hover,.desktop-nav .active,.site-footer a:hover{color:var(--text)}.header-cta,.btn{border:1px solid rgba(168,135,93,.7);background:var(--accent);color:#111;padding:.82rem 1.05rem;font-weight:720;letter-spacing:.035em;text-transform:uppercase;font-size:.76rem}.btn{display:inline-flex;justify-content:center;align-items:center;min-height:46px}.btn.secondary,.btn.glass{background:transparent;color:var(--text);border-color:rgba(255,255,255,.24)}.btn.small{padding:.65rem .8rem;min-height:auto}.menu-toggle{display:none;background:none;border:0;padding:.6rem;min-width:44px;min-height:44px}.menu-toggle span{display:block;width:24px;height:2px;background:var(--text);margin:5px 0}.mobile-panel{display:none}.hero{position:relative;min-height:92vh;display:grid;align-items:end;overflow:hidden;background:#050607}.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.hero-overlay{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.93),rgba(0,0,0,.62),rgba(0,0,0,.26)),linear-gradient(0deg,rgba(8,10,12,.98),rgba(8,10,12,.25) 46%,transparent)}.hero-content{position:relative;z-index:1;width:min(var(--max),calc(100% - 2rem));margin:0 auto;padding:10rem 0 6.5rem}.eyebrow{color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.16em;font-size:.74rem;margin:0 0 .9rem}h1,h2,h3{line-height:1.07;margin:0;color:var(--text);font-weight:700;letter-spacing:0}h1{font-size:clamp(2.35rem,5.45vw,5.35rem);max-width:1060px}h2{font-size:clamp(1.75rem,3vw,2.85rem)}h3{font-size:1.18rem;font-weight:700}.hero p,.subhero p,.section-head p{max-width:780px;color:var(--soft);font-size:1.02rem}.hero-actions,.cta-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem}.hero-points{display:flex;flex-wrap:wrap;gap:.65rem;margin-top:2.2rem}.hero-points span,.proof-list span,.area-tags span{border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);padding:.55rem .75rem;color:var(--soft);font-size:.86rem}.trust-strip{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#0b0e10}.trust-strip div{padding:1.35rem clamp(1rem,3vw,2rem);border-right:1px solid var(--line)}.trust-strip strong{display:block;color:#fff}.trust-strip span{color:var(--muted);font-size:.9rem}.quick-paths{display:grid;grid-template-columns:repeat(4,1fr);width:min(var(--max),calc(100% - 2rem));margin:2rem auto 0;border:1px solid var(--line);background:#0d1114}.quick-paths a{padding:1.2rem;border-right:1px solid var(--line)}.quick-paths span{display:block;color:var(--accent);font-weight:760}.quick-paths strong{display:block;font-size:1.05rem}.quick-paths em{display:block;color:var(--muted);font-style:normal;font-size:.9rem}.section,.split-section,.process-section,.local-section,.contact-layout,.subhero{width:min(var(--max),calc(100% - 2rem));margin:0 auto;padding:7.4rem 0;scroll-margin-top:112px}.reviews-hero{padding-bottom:3rem}.review-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;width:min(var(--max),calc(100% - 2rem));margin:0 auto 2rem}.review-stats article{border:1px solid var(--line);background:var(--panel);padding:1.2rem}.review-stats strong{display:block;font-size:2rem}.review-stats span{color:var(--muted)}.section-head{display:block;max-width:820px;margin-bottom:2rem}.section-head>p:not(.eyebrow){margin-top:1rem}.section-head h2{max-width:760px}.section-head.stacked{display:block}.service-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.15rem}.service-card{background:linear-gradient(180deg,#171d21,#101417);border:1px solid var(--line);min-height:100%;display:flex;flex-direction:column;box-shadow:0 18px 55px rgba(0,0,0,.18)}.service-card img{height:225px;width:100%;object-fit:cover;filter:saturate(.9) contrast(1.08)}.service-card-body{padding:1.35rem;display:flex;flex-direction:column;flex:1}.card-kicker{color:var(--accent)!important;text-transform:uppercase;letter-spacing:.12em;font-size:.7rem;font-weight:760;margin:.05rem 0 .7rem}.service-card-body ul{margin-bottom:1.2rem}.service-link{margin-top:auto;padding-top:1rem;border-top:1px solid var(--line);display:inline-flex;align-self:flex-start}.service-card p,.package-card p,.feature-grid p,.before-card p,.review-grid p,.site-footer p,.info-panel li,.faq-list p,.contact-card p{color:var(--muted)}.service-card ul{padding-left:1.1rem;color:var(--soft);font-size:.92rem}.service-card a,.text-link{color:var(--accent);font-weight:760}.split-section{display:grid;grid-template-columns:1.05fr .95fr;gap:3rem;align-items:center}.split-section>img{height:560px;width:100%;object-fit:cover}.proof-list{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.5rem}.info-panel{border:1px solid var(--line);background:linear-gradient(180deg,#171d21,#101417);padding:2rem}.dark-band{width:100%;max-width:none;background:#0c1013;border-block:1px solid var(--line);padding-inline:max(1rem,calc((100vw - var(--max))/2))}.before-grid,.review-grid,.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.before-card,.review-grid article,.feature-grid article,.package-card{border:1px solid var(--line);background:var(--panel);padding:1.1rem}.package-card{display:flex;flex-direction:column;min-height:100%;padding:1.45rem;background:linear-gradient(180deg,#161c20,#11161a)}.package-card h3{font-size:1.12rem}.package-card p{margin:.75rem 0}.package-card .btn{align-self:flex-start;margin-top:auto;min-height:42px;padding:.72rem .9rem;white-space:nowrap}.google-review{display:flex;flex-direction:column;gap:.75rem;min-height:100%;background:linear-gradient(180deg,#151a1e,#101417)!important}.review-top{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start}.review-top strong{line-height:1.2}.review-top span{color:var(--accent);font-weight:760;white-space:nowrap;letter-spacing:.08em}.review-date{font-size:.92rem;margin:0}.proof-image{width:100%;height:340px;object-fit:cover;margin-bottom:1rem;filter:saturate(.92) contrast(1.08)}.package-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.1rem}.package-grid.wide{grid-template-columns:repeat(3,minmax(0,1fr))}.package-price{color:var(--accent)!important;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:.88rem}.package-meta{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin:1.2rem 0}.package-meta span{border-top:1px solid var(--line);padding-top:.7rem}.package-meta small{display:block;color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.04em}.package-meta strong{display:block;color:var(--soft);font-weight:720;margin-top:.15rem;font-size:.96rem}.service-packages{grid-template-columns:repeat(2,minmax(260px,1fr));max-width:820px}.hub-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.hub-grid a{border:1px solid var(--line);background:var(--panel);padding:1.1rem;font-weight:760}.hub-grid span{display:block;color:var(--muted);font-weight:500;margin-top:.35rem}.process-section{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:2rem}.steps article{padding:1.2rem;border-left:1px solid var(--line)}.steps span{color:var(--accent);font-weight:760}.local-section{display:grid;grid-template-columns:.9fr 1.1fr;gap:2rem;align-items:center}.area-tags{display:flex;flex-wrap:wrap;gap:.7rem}.faq-list{display:grid;gap:.65rem}.faq-list details{background:var(--panel);border:1px solid var(--line);padding:1.1rem}.faq-list summary{cursor:pointer;font-weight:760}.final-cta{width:min(var(--max),calc(100% - 2rem));margin:0 auto 6rem;padding:3rem;border:1px solid rgba(168,135,93,.4);background:linear-gradient(135deg,#171b1d,#0d1012);display:flex;align-items:center;justify-content:space-between;gap:2rem}.subhero{display:grid;grid-template-columns:1fr .8fr;gap:3rem;align-items:center;padding-top:5rem}.subhero.text-only{display:block;max-width:930px}.subhero img{height:480px;width:100%;object-fit:cover}.filter-row{display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:1.5rem}.filter-row button{border:1px solid var(--line);background:var(--panel);color:var(--soft);padding:.7rem 1rem}.filter-row .active{border-color:var(--accent);color:#fff}.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.gallery-grid figure{margin:0;background:var(--panel);border:1px solid var(--line)}.gallery-grid img{height:300px;width:100%;object-fit:cover}.gallery-grid figcaption{padding:1rem;color:var(--soft)}.comparison{width:min(var(--max),100%);max-width:100%;margin:auto;overflow-x:auto}.comparison h2{margin:0 0 1.4rem}.comparison table{width:100%;border-collapse:collapse}.comparison th,.comparison td{border-bottom:1px solid var(--line);padding:1rem;text-align:left}.comparison th{color:var(--accent);text-transform:uppercase;font-size:.8rem}.contact-layout{display:grid;grid-template-columns:1.35fr .65fr;gap:2rem}.quote-form{display:grid;grid-template-columns:1fr 1fr;gap:1rem;background:var(--panel);border:1px solid var(--line);padding:1.2rem}.quote-form label{display:grid;gap:.4rem;color:var(--soft);font-weight:700}.quote-form input,.quote-form select,.quote-form textarea{width:100%;background:#0b0e10;border:1px solid var(--line);color:var(--text);padding:.85rem;font:inherit}.quote-form .full,.quote-form button{grid-column:1/-1}.contact-card{background:linear-gradient(180deg,#171d21,#101417);border:1px solid var(--line);padding:1.4rem;align-self:start;position:sticky;top:6rem}.map-embed{border:1px solid var(--line);background:#0b0e10;margin-top:1rem;overflow:hidden}.map-embed iframe{width:100%;height:260px;border:0;filter:grayscale(.75) contrast(1.05) invert(.9)}.map-embed a{display:block;padding:.85rem 1rem;color:var(--accent);font-weight:760;border-top:1px solid var(--line)}.site-footer{border-top:1px solid var(--line);padding:4rem clamp(1rem,3vw,2rem) 2rem;background:#090b0d}.footer-grid{display:grid;grid-template-columns:1.3fr .7fr .9fr 1fr;gap:2rem;width:min(var(--max),100%);margin:auto}.site-footer h3{font-size:.9rem;text-transform:uppercase;color:var(--accent)}.site-footer a{display:block;margin:.42rem 0}.footer-bottom{width:min(var(--max),100%);margin:2rem auto 0;padding-top:1.2rem;border-top:1px solid var(--line);display:flex;justify-content:space-between;color:var(--muted);font-size:.85rem}
@media (max-width:1050px){html{scroll-padding-top:74px}.top-line{display:none}.site-header{padding:.8rem 1rem}.desktop-nav{display:none}.header-cta{display:inline-flex;margin-left:auto;padding:.65rem .78rem;font-size:.7rem}.menu-toggle{display:block;margin-left:.25rem}.mobile-panel{position:fixed;inset:62px 0 auto 0;z-index:40;background:#090b0d;border-bottom:1px solid var(--line);padding:1rem;transform:translateY(-130%);transition:.25s}.mobile-panel.open{display:block;transform:translateY(0)}.mobile-panel nav{display:grid;gap:.9rem}.mobile-book{background:var(--accent);color:#111;padding:1rem;text-align:center;font-weight:760}.service-grid,.package-grid,.package-grid.wide,.quick-paths,.hub-grid{grid-template-columns:repeat(2,1fr)}.trust-strip,.steps,.review-stats{grid-template-columns:repeat(2,1fr)}.section-head,.final-cta{display:block}.before-grid,.review-grid,.feature-grid,.gallery-grid{grid-template-columns:1fr 1fr}.split-section,.subhero,.local-section,.contact-layout,.footer-grid{grid-template-columns:1fr}.contact-card{position:static}}@media (max-width:680px){h1{font-size:2.18rem}.hero{min-height:91vh}.hero-content{padding:7.5rem 0 5.25rem}.section,.split-section,.process-section,.local-section,.contact-layout,.subhero{padding:4.8rem 0}.reviews-hero{padding-bottom:2rem}.service-grid,.package-grid,.package-grid.wide,.quick-paths,.hub-grid,.trust-strip,.steps,.review-stats,.before-grid,.review-grid,.feature-grid,.gallery-grid{grid-template-columns:1fr}.quote-form{grid-template-columns:1fr}.final-cta{padding:1.5rem}.proof-image{height:230px}.footer-bottom{display:block}.brand small{display:none}.site-header{padding:.8rem 1rem}.subhero img,.split-section>img{height:330px}.contact-layout{padding-top:2rem}.comparison{overflow:visible;padding-inline:1rem}.comparison table,.comparison thead,.comparison tbody,.comparison tr,.comparison th,.comparison td{display:block;width:100%}.comparison thead{display:none}.comparison tr{border:1px solid var(--line);background:var(--panel);margin-bottom:.8rem}.comparison td{display:grid;grid-template-columns:8.5rem 1fr;gap:1rem;border-bottom:1px solid var(--line);padding:.85rem 1rem}.comparison td:last-child{border-bottom:0}.comparison td::before{content:attr(data-label);color:var(--accent);font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;font-weight:760}}
.footer-bottom{align-items:center;gap:1rem;flex-wrap:wrap}.site-credit{display:inline-flex!important;align-items:center;gap:.35rem;margin:0!important;padding:.5rem .72rem;border:1px solid rgba(168,135,93,.28);background:rgba(168,135,93,.08);color:var(--soft)!important;text-transform:uppercase;letter-spacing:.08em;font-size:.72rem;font-weight:760}.site-credit strong{color:var(--accent);font-weight:800}.site-credit:hover{border-color:rgba(168,135,93,.55);background:rgba(168,135,93,.13);color:#fff!important}@media (max-width:680px){.footer-bottom{display:grid;gap:.75rem}.site-credit{justify-self:start}}
.header-cta{white-space:nowrap}
.site-footer{padding:3.6rem clamp(1rem,3vw,2rem) 1.8rem}.footer-grid{grid-template-columns:minmax(260px,1.15fr) minmax(120px,.55fr) minmax(190px,.82fr) minmax(230px,.9fr);gap:clamp(1.5rem,4vw,4rem);align-items:start}.footer-brand{margin-bottom:1rem}.footer-brand .brand-mark{width:2.45rem;height:2.45rem}.footer-brand strong{font-size:.88rem}.footer-brand small{font-size:.7rem}.site-footer h3{font-size:.74rem;line-height:1;letter-spacing:.05em;margin:0 0 .8rem}.site-footer p,.site-footer a{font-size:.86rem;line-height:1.52}.site-footer a{margin:.38rem 0}.footer-copy{max-width:360px;margin:.8rem 0 0}.footer-contact p{max-width:280px;margin:.2rem 0 1.05rem}.footer-bottom{font-size:.8rem}.footer-bottom span{line-height:1.45}.site-footer .site-credit{font-size:.72rem;line-height:1}@media (max-width:1120px){.footer-grid{grid-template-columns:1.1fr .8fr;row-gap:2.3rem}.footer-contact p{max-width:360px}}@media (max-width:680px){.site-footer{padding:3rem 1rem 1.7rem}.footer-grid{grid-template-columns:1fr;gap:2rem}.footer-copy,.footer-contact p{max-width:100%}.site-footer p,.site-footer a{font-size:.88rem}.site-footer h3{margin-bottom:.65rem}.footer-bottom{font-size:.82rem}.site-footer .site-credit{font-size:.74rem}}
.trust-strip a{display:block;padding:1.35rem clamp(1rem,3vw,2rem);border-right:1px solid var(--line)}.trust-strip a:hover{background:rgba(255,255,255,.035)}.section-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem}.package-compare-cards{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:1rem}.package-compare-cards article{display:flex;flex-direction:column;gap:1rem;border:1px solid var(--line);background:linear-gradient(180deg,#161c20,#101417);padding:1.2rem;min-height:100%}.package-compare-cards h3{font-size:1.08rem}.package-compare-cards p{color:var(--muted);margin:.45rem 0 0}.package-compare-cards dl{display:grid;gap:.65rem;margin:0;color:var(--soft);font-size:.9rem}.package-compare-cards dt{color:var(--accent);font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;font-weight:760}.package-compare-cards dd{margin:0}.package-compare-cards .btn{align-self:flex-start;margin-top:auto}.intent-review p:last-child{display:-webkit-box;-webkit-line-clamp:6;-webkit-box-orient:vertical;overflow:hidden}.mobile-sticky-cta{display:none}.mobile-sticky-cta a{display:grid;place-items:center;min-height:48px;font-size:.74rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em}.mobile-sticky-cta a:first-child{background:var(--accent);color:#111}.mobile-sticky-cta a:last-child{background:#0e1215;color:var(--text);border-left:1px solid var(--line)}
@media (max-width:1180px){.package-compare-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.package-compare-cards article:last-child{grid-column:1/-1}}@media (max-width:680px){body{padding-bottom:56px}.package-compare-cards{grid-template-columns:1fr}.package-compare-cards article:last-child{grid-column:auto}.section-actions .btn,.hero-actions .btn,.cta-actions .btn{width:100%}.mobile-sticky-cta{position:fixed;left:0;right:0;bottom:0;z-index:60;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line);box-shadow:0 -18px 50px rgba(0,0,0,.35)}}
.admin-shell{width:min(var(--max),calc(100% - 2rem));margin:0 auto;padding:6.5rem 0}.admin-login{display:grid;grid-template-columns:1.05fr .95fr;gap:3rem;align-items:center;min-height:62vh}.admin-login h1,.dashboard-hero h1{max-width:760px}.admin-login>div>p:not(.eyebrow),.dashboard-hero p{max-width:720px;color:var(--soft)}.portal-card{border:1px solid var(--line);background:linear-gradient(180deg,#171d21,#101417);padding:1.45rem;box-shadow:0 22px 70px rgba(0,0,0,.18)}form.portal-card{display:grid;gap:1rem}.portal-brand{margin-bottom:.35rem}.portal-card label{display:grid;gap:.42rem;color:var(--soft);font-weight:760}.portal-card input{width:100%;background:#090d10;border:1px solid var(--line);color:var(--text);padding:.9rem;font:inherit}.portal-hint,.portal-error{margin:0;color:var(--muted);font-size:.9rem}.portal-error{color:#f0a39a}.admin-dashboard{display:grid;gap:2rem}.dashboard-hero{display:flex;justify-content:space-between;gap:2rem;align-items:flex-start}.dashboard-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.dashboard-grid .portal-card span{display:block;color:var(--accent);font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;font-weight:800}.dashboard-grid .portal-card strong{display:block;font-size:1.45rem;line-height:1.15;margin:.45rem 0;color:var(--text)}.dashboard-grid .portal-card p{color:var(--muted)}.status-good{border-color:rgba(168,135,93,.55)}.portal-section{border-top:1px solid var(--line);padding-top:2.2rem}.portal-actions{display:flex;gap:.8rem;flex-wrap:wrap}.admin-list{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.admin-list article{border:1px solid var(--line);background:var(--panel);padding:1.25rem}.admin-list p{color:var(--muted)}@media (max-width:900px){.admin-login,.dashboard-grid,.admin-list{grid-template-columns:1fr}.dashboard-hero{display:grid}.admin-shell{padding:4.8rem 0}}@media (max-width:680px){.admin-shell{padding:3.5rem 0}.portal-actions .btn{width:100%}.dashboard-grid .portal-card strong{font-size:1.22rem}}
.admin-layout{display:grid;grid-template-columns:230px 1fr;gap:1.35rem;align-items:start}.admin-sidebar{position:sticky;top:6rem;border:1px solid var(--line);background:#0b0f12;padding:1rem;display:grid;gap:.35rem}.admin-sidebar .portal-brand{padding-bottom:1rem;border-bottom:1px solid var(--line);margin-bottom:.55rem}.admin-sidebar a{color:var(--muted);padding:.72rem .75rem;border:1px solid transparent;font-weight:720;font-size:.9rem}.admin-sidebar a:hover{color:var(--text);border-color:var(--line);background:rgba(255,255,255,.035)}.admin-main{display:grid;gap:1.35rem;min-width:0}.admin-topbar{display:flex;flex-wrap:wrap;gap:.7rem}.admin-topbar span{border:1px solid var(--line);background:#0d1114;color:var(--soft);padding:.55rem .72rem;font-size:.82rem}.metric-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}.metric-card,.control-grid article,.chart-card{border:1px solid var(--line);background:linear-gradient(180deg,#171d21,#101417);padding:1.15rem}.metric-card span,.control-grid span,.chart-head span{display:block;color:var(--accent);font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;font-weight:820}.metric-card strong{display:block;margin:.35rem 0;font-size:1.9rem;line-height:1.05}.metric-card p,.control-grid p,.chart-card p{color:var(--muted);margin:.4rem 0 0}.metric-card.attention{border-color:rgba(168,135,93,.45);background:linear-gradient(180deg,rgba(168,135,93,.11),#101417)}.analytics-panel{display:grid;grid-template-columns:1.3fr .7fr;gap:1rem}.chart-head{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start}.chart-head strong{color:var(--soft);font-size:.95rem}.bar-chart{height:210px;display:flex;align-items:end;gap:.7rem;margin-top:1.4rem;padding:1rem;border:1px solid var(--line);background:#0a0d10}.bar-chart span{flex:1;min-width:18px;background:linear-gradient(180deg,var(--accent),rgba(168,135,93,.28));border:1px solid rgba(185,149,98,.28)}.admin-list.compact{grid-template-columns:1fr;gap:1rem}.control-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}.control-grid strong{display:block;margin:.4rem 0;font-size:1.22rem}.control-grid a{display:inline-flex;margin-top:.7rem;color:var(--accent);font-weight:760}.page-admin .site-footer{margin-top:2rem}@media (max-width:1100px){.admin-layout{grid-template-columns:1fr}.admin-sidebar{position:static;display:flex;flex-wrap:wrap}.admin-sidebar .portal-brand{width:100%;margin-bottom:.35rem}.metric-grid,.control-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.analytics-panel{grid-template-columns:1fr}}@media (max-width:680px){.admin-sidebar a{flex:1 1 44%;text-align:center}.metric-grid,.control-grid{grid-template-columns:1fr}.metric-card strong{font-size:1.55rem}.chart-head{display:grid}.bar-chart{height:160px}}
.page-admin .mobile-sticky-cta{display:none!important}@media (max-width:680px){body.page-admin{padding-bottom:0}}
.site-header .brand{min-width:0;flex:0 0 auto}.brand-wordmark{display:flex;align-items:center;gap:.72rem}.brand-wordmark strong{font-size:1.55rem;line-height:.92;letter-spacing:-.02em;font-weight:850;color:var(--text)}.brand-wordmark span{display:grid;gap:.18rem;padding-left:.72rem;border-left:1px solid rgba(185,149,98,.48)}.brand-wordmark b{display:block;font-size:.78rem;line-height:1;letter-spacing:.08em;text-transform:uppercase;color:var(--text);font-weight:850;white-space:nowrap}.brand-wordmark small{display:block;font-size:.58rem;line-height:1;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);white-space:nowrap}.site-header .brand-logo{width:clamp(10.5rem,17vw,19rem);max-width:100%}.footer-brand{display:block;min-width:0;width:auto}.portal-brand{min-width:0}.brand-logo.footer-logo{width:min(21rem,100%)}@media (max-width:680px){.brand-wordmark{gap:.5rem}.brand-wordmark strong{font-size:1.18rem}.brand-wordmark span{padding-left:.5rem}.brand-wordmark b{font-size:.62rem;letter-spacing:.06em}.brand-wordmark small{display:none}.footer-logo{width:18rem}.portal-logo{width:100%}.admin-logo{width:3rem}}
"""

JS = r"""
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
"""

for stale_page in ROOT.glob("*.html"):
    if stale_page.name not in pages:
        stale_page.unlink()

for name, html in pages.items():
    deploy_html = (
        html
        .replace('  <link rel="stylesheet" href="assets/styles.css">', f"  <style>\n{CSS}\n  </style>")
        .replace('  <script src="assets/site.js" defer></script>', f"  <script>\n{JS}\n  </script>")
    )
    (ROOT / name).write_text(deploy_html, encoding="utf-8")

(ROOT / "assets" / "styles.css").write_text(CSS, encoding="utf-8")
(ROOT / "assets" / "site.js").write_text(JS, encoding="utf-8")
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
(ROOT / "CNAME").write_text("bmautodetailing.ca\n", encoding="utf-8")
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://bmautodetailing.ca/sitemap.xml\n", encoding="utf-8")
sitemap_pages = [name for name in pages if name not in {"404.html", "admin.html"}]
def sitemap_loc(name):
    return "https://bmautodetailing.ca/" if name == "index.html" else f"https://bmautodetailing.ca/{name}"
(ROOT / "sitemap.xml").write_text("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(f"  <url><loc>{sitemap_loc(name)}</loc></url>" for name in sitemap_pages) + "\n</urlset>\n", encoding="utf-8")

print(f"Built {len(pages)} pages in {ROOT}")














