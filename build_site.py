from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://bmautodetailing.ca"

BUSINESS = {
    "name": "B&M Auto Detailing",
    "phone": "(403) 454-0203",
    "email": "bookings@bmautodetailing.ca",
    "address": "1247 36 Ave NE, Calgary, AB T2E 6N6",
    "hours": "Mon-Fri, 9:00 AM-6:00 PM; Sat, 10:00 AM-3:30 PM",
    "rating": "4.8 Google rating",
    "reviews": "21 reviews",
}

MAP_URL = "https://www.google.com/maps/search/?api=1&query=B%26M%20Auto%20Detailing%201247%2036%20Ave%20NE%20Calgary%20AB"
MAP_EMBED = "https://www.google.com/maps?q=B%26M%20Auto%20Detailing%201247%2036%20Ave%20NE%20Calgary%20AB&output=embed"

services = [
    ("auto-detailing.html", "Interior & Exterior Detailing", "Interior and exterior reset for vehicles dealing with salt, dust, spills, daily use, lease return needs, or seasonal cleanup.", ["Best for trucks, SUVs, commuters", "Interior reset plus exterior care", "Photos help scope heavy interiors"]),
    ("paint-correction.html", "Paint Correction", "Polishing work for swirl marks, haze, dull paint, and coating prep when the finish needs more than a wash.", ["Best for dark or marked paint", "Improves gloss and reflection", "Often needed before coating"]),
    ("ceramic-coating.html", "Ceramic Coating", "Hydrophobic protection for prepared paint that helps gloss last longer and makes careful washing easier.", ["Best after proper prep", "Easier maintenance", "Not a rock-chip solution"]),
    ("paint-protection-film.html", "Paint Protection Film", "Clear film planning for front-end impact zones, rock chips, road debris, and Alberta highway driving.", ["Best for new vehicles", "Front-end impact protection", "Coverage chosen by driving use"]),
]

seo_service_links = [
    ("complete-detailing.html", "Complete Detailing"),
    ("interior-detailing.html", "Interior Detailing"),
    ("exterior-detailing.html", "Exterior Detailing"),
    ("car-polishing-buffing.html", "Polishing & Buffing"),
    ("headlight-restoration.html", "Headlight Restoration"),
    ("new-vehicle-protection.html", "New Vehicle Protection"),
]

packages = [
    ("Essential Detail", "Daily drivers needing a clean reset", "Exterior wash, wheel cleaning, interior vacuum, wipe-down, windows, and light finishing protection.", "3-4 hours", "From $179"),
    ("Interior Reset", "Family vehicles, trucks, SUVs, lease returns, and seasonal cleanup", "Steam cleaning, extraction, stain attention, plastics, vents, glass, and odor-focused finishing.", "5-7 hours", "From $279"),
    ("Paint Refresh", "Vehicles with wash marks, dullness, or sale-prep needs", "Decontamination, clay treatment, one-step polish, sealant, and exterior finishing.", "1 day", "From $449"),
    ("Ceramic Protection", "Owners who want better gloss and easier maintenance", "Paint prep, correction as needed, ceramic coating, curing guidance, and maintenance advice.", "1-2 days", "From $899"),
    ("New Vehicle Protection", "New cars, trucks, and long-term ownership", "Inspection-first planning, front-end PPF options, coating recommendations, and practical protection sequencing.", "After vehicle review", "Custom quote"),
]

faqs = [
    ("How long does a detail take?", "Most maintenance details take 3 to 5 hours. Heavier interiors, pet hair, salt staining, polishing, coating, or PPF work can require a full day or more."),
    ("Is ceramic coating worth it in Calgary?", "For many daily drivers, yes. Calgary vehicles face UV exposure, winter contamination, road salt, dust, and frequent washing. A coating makes maintenance easier and helps preserve gloss when installed over properly prepared paint."),
    ("What is the difference between wax and ceramic coating?", "Wax is a short-term gloss and protection layer. Ceramic coating bonds more durably to prepared paint, improves hydrophobic behavior, and can last years with correct maintenance."),
    ("Does PPF stop rock chips?", "Paint protection film is the strongest option for physical impact protection. It is commonly used on front bumpers, hoods, fenders, mirrors, rocker panels, and other high-impact areas."),
    ("Can packages be adjusted for vehicle size and condition?", "Yes. B&M scopes the recommendation around vehicle size, interior condition, paint condition, and protection goals before confirming the appointment."),
    ("Do you work on trucks, SUVs, and daily drivers?", "Yes. Packages can be adjusted for trucks, SUVs, family vehicles, commuter cars, luxury vehicles, lease returns, and sale-prep vehicles."),
    ("What should I do before my appointment?", "Remove personal items, child seats, and valuables where possible. For quotes, photos of paint condition, interior staining, pet hair, or rock-chip areas help scope the work accurately."),
    ("Do I need paint correction before ceramic coating?", "If the paint has swirl marks, haze, oxidation, or dealer wash marks, correction should be discussed before coating. Ceramic coating protects the finish underneath; it does not hide poor paint prep."),
    ("What PPF coverage makes sense for Calgary highways?", "Most Calgary highway drivers start with front bumper, hood, fenders, mirrors, and other high-impact zones. The best coverage depends on vehicle shape, mileage, winter driving, and how long you plan to keep it."),
    ("Can I send photos before booking?", "Yes. Photos of the interior, paint under light, rock-chip areas, wheels, and overall vehicle condition help B&M give a clearer starting recommendation before the appointment."),
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
    robots_meta = '  <meta name="robots" content="noindex,follow">\n' if active in {"404.html"} else ""
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
      <span class="brand-mark">B&M</span>
      <span><strong>Auto Detailing</strong><small>Calgary protection studio</small></span>
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
        <div class="brand footer-brand"><span class="brand-mark">B&M</span><span><strong>Auto Detailing</strong><small>Premium auto detailing and vehicle protection in Calgary.</small></span></div>
        <p class="footer-copy">Professional detailing, paint correction, ceramic coating, and PPF for Calgary drivers who want a cleaner vehicle, stronger protection, and a finish that is easier to maintain.</p>
      </div>
      <div class="footer-nav"><h3>Pages</h3>{nav}</div>
      <div class="footer-nav"><h3>Services</h3>{service_links}</div>
      <div class="footer-contact"><h3>Contact</h3><p>{BUSINESS['address']}<br>{BUSINESS['phone']}<br>{BUSINESS['email']}<br>{BUSINESS['hours']}</p><p>Serving {", ".join(areas[:5])} and nearby communities.</p></div>
    </div>
    <div class="footer-bottom"><span>© 2026 B&M Auto Detailing. All rights reserved.</span><span>Calgary detailing, ceramic coating, paint correction, and PPF.</span><a class="site-credit" href="https://nebrex.ca" target="_blank" rel="noopener" aria-label="Website by Nebrex">Site by <strong>Nebrex.ca</strong></a></div>
  </footer>
  <script src="assets/site.js" defer></script>
</body>
</html>"""

def cta(label="Request a Quote"):
    return f"""<section class="final-cta">
  <div><p class="eyebrow">Calgary vehicle protection</p><h2>Get a quote based on the vehicle, not a guess.</h2><p>Send the vehicle, service goal, and a few photos. B&M can recommend whether it needs interior detailing, polishing, coating, PPF, or a simpler reset.</p></div>
  <div class="cta-actions"><a class="btn primary" href="contact.html">{label}</a><a class="btn secondary" href="contact.html">Send Photos for Pricing</a><a class="btn glass" href="tel:14034540203">{BUSINESS['phone']}</a></div>
</section>"""

def map_embed(label="B&M Auto Detailing on Google Maps"):
    return f"""<div class="map-embed">
  <iframe title="{label}" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  <a href="{MAP_URL}" target="_blank" rel="noopener">Open official Google Maps listing</a>
</div>"""

def service_cards():
    return "".join(f"""<article class="service-card">
  <img src="{[img['detail'], img['correction'], img['coating'], img['ppf']][i]}" alt="{title} Calgary service example" loading="lazy">
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
        ("Essential Detail", "Daily drivers needing a clean reset", "Interior vacuum, wipe-down, glass, wheels, exterior wash", "Paint correction, coating, or heavy stain extraction unless added", "From $179"),
        ("Interior Reset", "Family vehicles, trucks, lease returns, winter interiors", "Steam cleaning, extraction, stain attention, plastics, vents, glass", "Exterior polishing or coating unless added", "From $279"),
        ("Paint Refresh", "Dull paint, wash marks, or sale prep", "Decontamination, clay, one-step polish, sealant, exterior finishing", "Deep multi-stage correction or ceramic coating unless added", "From $449"),
        ("Ceramic Protection", "Owners who want gloss and easier maintenance", "Paint prep, correction as needed, ceramic coating, curing guidance", "Rock-chip protection; PPF is quoted separately", "From $899"),
        ("New Vehicle Protection", "New vehicles before Calgary roads leave marks", "Inspection, PPF options, coating recommendations, sequencing plan", "Final scope depends on coverage and vehicle condition", "Custom quote"),
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
        ("Exterior results", google_reviews[1]),
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
  <a href="paint-correction.html"><strong>Paint correction first</strong><span>Finish condition is checked before coating work</span></a>
  <a href="paint-protection-film.html"><strong>PPF + coating guidance</strong><span>Protection recommendations based on how the vehicle is driven</span></a>
</section>"""

def home():
    body = f"""
<section class="hero home-hero">
  <img src="{img['hero']}" alt="Premium automotive detailing studio finish on a dark vehicle" fetchpriority="high" decoding="async">
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <p class="eyebrow">1247 36 Ave NE, Calgary</p>
    <h1>Calgary detailing for cleaner interiors, sharper paint, and protection that fits Alberta roads.</h1>
    <p>B&M Auto Detailing handles interior detailing, exterior detailing, paint correction, ceramic coating, and PPF planning for drivers who want clear recommendations before they spend money on protection.</p>
    <div class="hero-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="contact.html">Send Photos for Pricing</a></div>
    <div class="hero-points"><span>{BUSINESS['rating']} from {BUSINESS['reviews']}</span><span>Calgary shop</span><span>Paint correction before coating when needed</span><span>PPF guidance for rock-chip zones</span></div>
  </div>
</section>
{trust_bar()}
<section class="quick-paths">
  <a href="complete-detailing.html"><span>01</span><strong>Complete detailing</strong><em>Interior and exterior reset</em></a>
  <a href="interior-detailing.html"><span>02</span><strong>Interior detailing</strong><em>Salt, stains, pet hair, daily use</em></a>
  <a href="exterior-detailing.html"><span>03</span><strong>Exterior detailing</strong><em>Wash, decon, gloss, protection</em></a>
  <a href="paint-correction.html"><span>04</span><strong>Paint correction</strong><em>Swirls, haze, dull paint</em></a>
</section>
<section class="section"><div class="section-head"><p class="eyebrow">Services</p><h2>Choose by what the vehicle actually needs.</h2><p>Some vehicles need a full interior reset. Some need polishing before coating. Some new vehicles should get front-end PPF before anything else.</p></div><div class="service-grid">{service_cards()}</div><div class="section-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="services.html">Compare Services</a></div></section>
<section class="split-section">
  <div><p class="eyebrow">Why B&M</p><h2>Inspection-first advice before coating, polishing, or PPF.</h2><p>Premium work is not just a glossy final photo. The important part is choosing the right sequence: clean the interior properly, inspect the paint, correct defects before coating when needed, and protect the areas that actually take abuse on Calgary roads.</p><div class="proof-list"><span>Vehicle condition reviewed first</span><span>Paint-safe prep before protection</span><span>Realistic correction expectations</span><span>Aftercare guidance after pickup</span></div></div>
  <img src="{img['studio']}" alt="Clean premium automotive studio environment" loading="lazy">
</section>
<section class="section dark-band"><div class="section-head stacked"><p class="eyebrow">Proof of work</p><h2>Visual proof matters in detailing and protection.</h2><p>Interior condition, paint clarity, gloss, and front-end protection all need to be seen clearly before a customer trusts the process.</p></div><div class="before-grid">
  <article class="before-card"><img class="proof-image" src="{img['interior']}" alt="Interior detailing and seat cleaning example" loading="lazy"><h3>Interior reset</h3><p>Interior cleaning for high-use vehicles with dust, spills, salt, and daily wear.</p></article>
  <article class="before-card"><img class="proof-image" src="{img['correction']}" alt="Paint polishing and correction example" loading="lazy"><h3>Paint correction</h3><p>Polishing work for dull paint, wash marks, deeper reflection, and coating prep.</p></article>
  <article class="before-card"><img class="proof-image" src="{img['front']}" alt="Front end detailing and protection example" loading="lazy"><h3>Front-end protection</h3><p>PPF planning and protection guidance for rock-chip-prone Calgary driving.</p></article>
</div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Packages</p><h2>Starting prices with clear package logic.</h2><p>Pricing is shown as a starting point. Vehicle size, interior condition, paint defects, coating prep, and PPF coverage can change the final quote.</p></div>{package_comparison()}</section>
<section class="section seo-hub"><div class="section-head"><p class="eyebrow">Service paths</p><h2>High-intent Calgary service pages.</h2><p>Use these pages when you already know the service you are comparing or searching for.</p></div><div class="hub-grid">{''.join(f'<a href="{href}">{label} Calgary<span>View service page</span></a>' for href, label in seo_service_links)}</div></section>
<section class="process-section"><p class="eyebrow">Process</p><h2>Send details. Get a recommendation. Book the right work.</h2><div class="steps"><article><span>01</span><h3>Send vehicle details</h3><p>Share the vehicle, service goal, and photos of the interior, paint, or rock-chip areas.</p></article><article><span>02</span><h3>Get the right scope</h3><p>B&M recommends detailing, correction, coating, PPF, or a simpler reset based on condition.</p></article><article><span>03</span><h3>Confirm timing</h3><p>Appointment timing, prep notes, expected duration, and quote range are confirmed first.</p></article><article><span>04</span><h3>Pick up with aftercare</h3><p>Leave with maintenance guidance so the finish is easier to care for after the work.</p></article></div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Customer reviews</p><h2>Proof tied to what buyers care about.</h2><p>Interior cleanup, exterior results, and protection work each create a different kind of trust.</p></div><div class="review-grid">{intent_reviews()}</div><div class="section-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="reviews.html">Read Google Reviews</a></div></section>
<section class="local-section"><div><p class="eyebrow">Calgary location</p><h2>Visit B&M Auto Detailing in NE Calgary.</h2><p>B&M Auto Detailing serves Calgary drivers and nearby communities including Airdrie, Chestermere, Cochrane, and Okotoks.</p><div class="area-tags">{''.join(f'<span>{a}</span>' for a in areas)}</div></div>{map_embed("B&M Auto Detailing Calgary Google Maps location")}</section>
<section class="section faq-preview"><div class="section-head"><p class="eyebrow">FAQ</p><h2>Answers that affect the quote.</h2></div>{faq_block(6)}</section>
{cta()}
"""
    return page_shell("B&M Auto Detailing | Premium Auto Detailing Calgary", "Premium auto detailing, ceramic coating, paint protection film, and paint correction in Calgary, Alberta.", body, "index.html")

service_details = {
    "auto-detailing.html": ("Auto Detailing Calgary", "Interior and exterior detailing packages for Calgary cars, SUVs, trucks, lease returns, and seasonal refreshes.", ["Interior Detailing", "Exterior Detailing", "Full Detail Packages", "Pet hair, salt, stain, odor, and engine bay add-ons"], "Detailing is for vehicles that need a controlled reset rather than a quick wash. B&M builds packages around vehicle size, interior condition, exterior contamination, and whether the customer is preparing for sale, lease return, winter recovery, or regular upkeep.", img["detail"]),
    "ceramic-coating.html": ("Ceramic Coating Calgary", "Ceramic coating packages for gloss, hydrophobic protection, easier washing, UV resistance, and long-term vehicle care in Calgary.", ["Paint inspection and decontamination", "Correction before coating when needed", "Multi-year protection options", "Maintenance guidance after install"], "Ceramic coating is a durable protection layer installed over properly prepared paint. It is not a substitute for PPF against rock chips, but it is one of the strongest choices for gloss, hydrophobic behavior, UV exposure, contamination resistance, and easier maintenance.", img["coating"]),
    "paint-protection-film.html": ("Paint Protection Film Calgary", "PPF and clear bra packages for Calgary rock chips, road debris, winter driving, highways, and new vehicle protection.", ["Partial front", "Full front", "Full vehicle", "Rocker panels, mirrors, door cups, trunk ledges, and high-impact zones"], "PPF is the strongest service for physical paint protection. It is ideal for new vehicles, highway drivers, luxury vehicles, trucks, and owners who want to reduce rock-chip damage in Alberta conditions.", img["ppf"]),
    "paint-correction.html": ("Paint Correction Calgary", "Paint correction for swirl marks, haze, oxidation, light defects, and coating-ready gloss in Calgary.", ["Single-stage correction", "Multi-stage correction", "Gloss enhancement", "Coating preparation"], "Paint correction removes or reduces visible defects that make paint look dull under light. It is often the most important prep step before ceramic coating because coatings lock in the finish that sits underneath.", img["correction"]),
}

service_package_map = {
    "auto-detailing.html": [packages[0], packages[1], packages[2]],
    "ceramic-coating.html": [packages[2], packages[3], packages[4]],
    "paint-protection-film.html": [packages[4], packages[3]],
    "paint-correction.html": [packages[2], packages[3], packages[4]],
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
<section class="section"><div class="section-head"><p class="eyebrow">What is included</p><h2>Clear scope before the appointment.</h2><p>The final recommendation depends on vehicle size, paint condition, interior condition, coating or film selection, and the customer's ownership goals.</p></div><div class="feature-grid"><article><h3>Inspection</h3><p>Vehicle condition, finish goals, risk areas, and timing are reviewed before the work is confirmed.</p></article><article><h3>Preparation</h3><p>Paint-safe washing, decontamination, interior prep, correction, masking, or surface prep is sequenced according to the service.</p></article><article><h3>Service work</h3><p>Detailing, coating, PPF, or correction work is completed with a controlled process and clear expectations.</p></article><article><h3>Aftercare</h3><p>Customers receive practical maintenance guidance so the result lasts longer and avoids avoidable damage.</p></article></div></section>
<section class="section dark-band"><div class="section-head stacked"><p class="eyebrow">Packages</p><h2>Packages that fit this service.</h2><p>These are common starting points. The final recommendation is confirmed after B&M reviews the vehicle condition, finish goals, and protection needs.</p></div><div class="package-grid service-packages">{package_cards(items=service_packages)}</div></section>
<section class="section"><div class="section-head"><p class="eyebrow">Common questions</p><h2>Before you book.</h2></div>{faq_block(5)}</section>
{cta("Get a Quote")}
"""
    return page_shell(f"{h1} | B&M Auto Detailing", meta, body, filename)

def simple_page(filename, title, desc, body):
    return page_shell(title, desc, body, filename)

seo_pages = {
    "complete-detailing.html": {
        "title": "Complete Car Detailing Calgary | B&M Auto Detailing",
        "desc": "Complete interior and exterior car detailing in Calgary for daily drivers, SUVs, trucks, lease returns, and seasonal vehicle resets.",
        "h1": "Complete car detailing in Calgary.",
        "intro": "A complete detail is the right fit when the vehicle needs more than a quick interior wipe-down or exterior wash. It combines interior cleaning, exterior decontamination, glass, wheels, trim, and protection planning into one appointment path.",
        "items": ["Interior vacuum and surface cleaning", "Exterior hand wash and wheel cleaning", "Salt, dust, and road film attention", "Protection upgrade options"],
    },
    "interior-detailing.html": {
        "title": "Interior Detailing Calgary | B&M Auto Detailing",
        "desc": "Interior detailing in Calgary for salt stains, pet hair, spills, upholstery, leather, carpets, vents, and lease return cleanup.",
        "h1": "Interior detailing for Calgary daily use.",
        "intro": "Interior detailing should be scoped by condition. Winter salt, kids, pets, work vehicles, coffee spills, dust, and lease return expectations all change the amount of work needed.",
        "items": ["Carpet and mat cleaning", "Seat and upholstery attention", "Pet hair and salt-stain add-ons", "Glass, vents, plastics, and touch points"],
    },
    "exterior-detailing.html": {
        "title": "Exterior Detailing Calgary | B&M Auto Detailing",
        "desc": "Exterior detailing in Calgary for hand washing, decontamination, wheel cleaning, gloss enhancement, and paint protection.",
        "h1": "Exterior detailing for paint, glass, wheels, and trim.",
        "intro": "Calgary vehicles collect road film, mineral deposits, construction dust, tar, winter residue, and wash marks. Exterior detailing removes contamination safely and prepares the vehicle for sealant, polishing, coating, or film consultation.",
        "items": ["Paint-safe wash process", "Wheel and tire cleaning", "Chemical and clay decontamination where needed", "Sealant, polish, coating, or PPF upgrade paths"],
    },
    "car-polishing-buffing.html": {
        "title": "Car Polishing and Buffing Calgary | B&M Auto Detailing",
        "desc": "Car polishing and buffing in Calgary for dull paint, light wash marks, resale prep, and gloss enhancement before protection.",
        "h1": "Car polishing and buffing in Calgary.",
        "intro": "Polishing is for paint that looks tired even after a wash. It can improve gloss, reduce light wash marks, and create a better finish before sealant or ceramic coating.",
        "items": ["Paint inspection under light", "One-step gloss enhancement", "Defect reduction where appropriate", "Coating-ready prep options"],
    },
    "headlight-restoration.html": {
        "title": "Headlight Restoration Calgary | B&M Auto Detailing",
        "desc": "Headlight restoration in Calgary for cloudy, oxidized, yellowed, or hazy headlights that reduce appearance and visibility.",
        "h1": "Headlight restoration for cloudy or oxidized lenses.",
        "intro": "Cloudy headlights make an otherwise clean vehicle look older and can reduce night visibility. Restoration is a practical add-on for sale prep, lease return, or an exterior detail.",
        "items": ["Lens assessment", "Oxidation removal", "Clarity improvement", "Protection recommendation after restoration"],
    },
    "new-vehicle-protection.html": {
        "title": "New Vehicle Protection Calgary | B&M Auto Detailing",
        "desc": "New vehicle protection packages in Calgary with detailing, paint inspection, ceramic coating, PPF planning, and maintenance guidance.",
        "h1": "New vehicle protection before Calgary roads leave their mark.",
        "intro": "New vehicles still need inspection. Dealer wash marks, transport contamination, exposed front ends, and high-touch interiors are easier to manage early than after a winter of daily driving.",
        "items": ["Paint inspection before protection", "PPF coverage consultation", "Ceramic coating recommendations", "Maintenance guidance from day one"],
    },
}

pages = {
    "index.html": home(),
    "services.html": simple_page("services.html", "Services | B&M Auto Detailing Calgary", "Overview of B&M Auto Detailing services including detailing, ceramic coating, PPF, and paint correction in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Services</p><h1>Vehicle appearance and protection services in Calgary.</h1><p>Detailing, paint correction, ceramic coating, and paint protection film are connected services. The right plan depends on what the vehicle needs now and what it needs protection from next.</p></div></section><section class="section"><div class="service-grid">{service_cards()}</div></section>{cta()}"""),
    "packages.html": simple_page("packages.html", "Packages and Pricing Guide | B&M Auto Detailing", "Compare detailing, paint enhancement, ceramic protection, new vehicle protection, and seasonal protection packages in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Packages</p><h1>Packages and pricing guide.</h1><p>Use these packages as practical buying paths. Final pricing depends on vehicle size, condition, material selection, and the amount of correction or protection required.</p><div class="hero-actions"><a class="btn primary" href="contact.html">Get a Quote</a><a class="btn glass" href="contact.html">Send Photos for Pricing</a></div></div></section><section class="section">{package_comparison()}</section><section class="section dark-band"><div class="comparison"><h2>Quick comparison</h2><table><thead><tr><th>Package</th><th>Best for</th><th>Duration</th><th>Starting price</th></tr></thead><tbody>{''.join(f'<tr><td data-label="Package">{n}</td><td data-label="Best for">{b}</td><td data-label="Duration">{d}</td><td data-label="Starting price">{p}</td></tr>' for n,b,i,d,p in packages)}</tbody></table></div></section>{cta()}"""),
    "gallery.html": simple_page("gallery.html", "Gallery and Before After | B&M Auto Detailing", "Gallery and before-after examples for detailing, ceramic coating, PPF, and paint correction work in Calgary.", f"""<section class="subhero text-only"><div><p class="eyebrow">Gallery</p><h1>Detailing, protection, and finish examples.</h1><p>A visual overview of the service categories customers ask about most: interior resets, ceramic coating gloss, PPF coverage, correction work, and exterior detailing.</p></div></section><section class="section"><div class="filter-row"><button class="active">All</button><button>Detailing</button><button>Ceramic</button><button>PPF</button><button>Correction</button></div><div class="gallery-grid">{''.join(f'<figure><img src="{url}" alt="{cap}"><figcaption>{cap}</figcaption></figure>' for url, cap in [(img['interior'],'Full interior reset on SUV'),(img['coating'],'Ceramic coating on black sedan'),(img['ppf'],'Full front PPF package'),(img['correction'],'Paint correction before ceramic install'),(img['detail'],'Exterior detail and gloss enhancement')])}</div></section>{cta()}"""),
    "reviews.html": simple_page("reviews.html", "Customer Reviews | B&M Auto Detailing Calgary", "Customer reviews for B&M Auto Detailing in Calgary, including detailing, PPF, communication, pricing, and finished vehicle results.", f"""<section class="subhero text-only reviews-hero"><div><p class="eyebrow">Customer reviews</p><h1>Calgary drivers trust B&M with detailing and protection work.</h1><p>Customers mention clean interiors, strong exterior results, fair pricing, professional communication, PPF installation, and vehicles looking better than expected after service.</p><div class="hero-actions"><a class="btn primary" href="contact.html">Request a quote</a><a class="btn glass" href="https://www.google.com/search?q=bm+auto+detailing+calgary#lrd=0x5371650076e95fa9:0xb4fd3f6c4e98f878,1,,,," target="_blank" rel="noopener">View on Google</a></div></div></section><section class="review-stats"><article><strong>4.8</strong><span>Google rating</span></article><article><strong>21</strong><span>Public reviews</span></article><article><strong>Calgary</strong><span>1247 36 Ave NE</span></article></section><section class="section"><div class="section-head"><p class="eyebrow">Review highlights</p><h2>Detailing, PPF, communication, and clean results.</h2><p>Selected written Google reviews are shown in the customer's own words, with names and dates attached for credibility.</p></div><div class="review-grid large">{review_cards()}</div></section>{cta()}"""),
    "about.html": simple_page("about.html", "About B&M Auto Detailing | Calgary", "About B&M Auto Detailing, a Calgary automotive detailing and vehicle protection studio focused on prep, protection, and long-term vehicle care.", f"""<section class="subhero"><div><p class="eyebrow">About</p><h1>A Calgary studio built around careful prep and practical protection.</h1><p>B&M Auto Detailing exists for drivers who want more than a surface clean. The focus is on controlled process, honest recommendations, and protection plans that make sense for how each vehicle is used.</p></div><img src="{img['studio']}" alt="Premium detailing studio interior"></section><section class="split-section"><div><p class="eyebrow">Approach</p><h2>Specialist craftsmanship without inflated promises.</h2><p>The best detailing and protection work happens before the final gloss shot. Inspection, wash process, decontamination, correction, film selection, coating prep, and aftercare all affect the result. B&M keeps that process clear so customers know what is being recommended and why.</p></div><div class="info-panel"><h3>Why Calgary drivers choose specialist care</h3><ul><li>Road salt and winter contamination</li><li>Rock chips from highway and construction driving</li><li>UV exposure and frequent wash cycles</li><li>Lease return, resale, and new vehicle protection needs</li></ul></div></section>{cta()}"""),
    "faq.html": simple_page("faq.html", "FAQ | B&M Auto Detailing Calgary", "Answers to common Calgary auto detailing, ceramic coating, PPF, and paint correction questions.", f"""<section class="subhero text-only"><div><p class="eyebrow">FAQ</p><h1>Answers before the quote.</h1><p>Clear expectations help customers choose the right service and understand what affects timing, price, durability, and maintenance.</p></div></section><section class="section">{faq_block()}</section>{cta()}"""),
    "contact.html": simple_page("contact.html", "Contact and Book Now | B&M Auto Detailing Calgary", "Request a quote or book B&M Auto Detailing in Calgary for detailing, ceramic coating, PPF, and paint correction.", f"""<section class="subhero text-only"><div><p class="eyebrow">Book now</p><h1>Request a quote for detailing, coating, PPF, or correction.</h1><p>Send the vehicle details, preferred service, timing, and condition notes. Photos help scope interior condition, paint defects, rock-chip exposure, and film coverage needs.</p></div></section><section class="contact-layout"><form class="quote-form" action="mailto:{BUSINESS['email']}" method="post" enctype="text/plain"><label>Name<input name="name" autocomplete="name"></label><label>Phone<input name="phone" autocomplete="tel"></label><label>Email<input type="email" name="email" autocomplete="email"></label><label>Vehicle year<input name="year"></label><label>Vehicle make<input name="make"></label><label>Vehicle model<input name="model"></label><label>Service interested in<select name="service"><option>Auto detailing</option><option>Ceramic coating</option><option>Paint protection film / clear bra</option><option>Paint correction</option><option>New vehicle protection package</option></select></label><label>Preferred date<input type="date" name="date"></label><label>Upload photos<input type="file" name="photos" multiple></label><label>How did you hear about us?<input name="source"></label><label class="full">Message / notes<textarea name="message" rows="5"></textarea></label><button class="btn primary" type="submit">Send quote request</button></form><aside class="contact-card"><h2>Contact</h2><p>{BUSINESS['address']}</p><p><a href="tel:14034540203">{BUSINESS['phone']}</a><br><a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a></p><p>{BUSINESS['hours']}</p>{map_embed("B&M Auto Detailing Calgary Google Maps location")}</aside></section>"""),
    "service-areas.html": simple_page("service-areas.html", "Calgary Service Areas | B&M Auto Detailing", "B&M Auto Detailing serves Calgary, Airdrie, Chestermere, Cochrane, Okotoks, and nearby Alberta communities.", f"""<section class="subhero text-only"><div><p class="eyebrow">Service areas</p><h1>Calgary and nearby communities.</h1><p>Local pages can be expanded for detailing, ceramic coating, PPF, and correction searches in each service area.</p></div></section><section class="local-section"><div class="area-tags">{''.join(f'<span>{a}</span>' for a in areas)}</div></section>{cta()}"""),
    "care-tips.html": simple_page("care-tips.html", "Care Tips | B&M Auto Detailing", "Vehicle care tips for Calgary detailing, ceramic coating maintenance, PPF aftercare, and seasonal protection.", f"""<section class="subhero text-only"><div><p class="eyebrow">Care tips</p><h1>Practical vehicle care guidance for Calgary conditions.</h1><p>Focused guidance for coating maintenance, winter salt cleanup, PPF aftercare, and safe wash habits.</p></div></section><section class="section"><div class="feature-grid"><article><h3>How to maintain ceramic coating in Calgary</h3><p>Use pH-neutral wash products, avoid harsh automatic brushes, and schedule decontamination when hydrophobic behavior starts to weaken.</p></article><article><h3>Why new vehicles still need paint inspection</h3><p>Factory-new paint can still have dealer wash marks, transport contamination, or defects that should be corrected before coating.</p></article><article><h3>Winter salt cleanup</h3><p>Salt should be removed from carpets, pedals, lower panels, and exterior crevices before it hardens into long-term staining or corrosion risk.</p></article></div></section>{cta()}"""),
    "404.html": simple_page("404.html", "Page Not Found | B&M Auto Detailing Calgary", "The requested B&M Auto Detailing page could not be found.", """<section class="subhero text-only"><div><p class="eyebrow">Page not found</p><h1>This page is not available.</h1><p>The service may have moved, or the old link may no longer be used. Start from the homepage or request a quote for detailing, paint correction, ceramic coating, or PPF.</p><div class="hero-actions"><a class="btn primary" href="/">Back to homepage</a><a class="btn glass" href="contact.html">Request a quote</a></div></div></section>"""),
}

for filename, data in seo_pages.items():
    body = f"""<section class="subhero text-only"><div><p class="eyebrow">Calgary detailing service</p><h1>{data['h1']}</h1><p>{data['intro']}</p><div class="hero-actions"><a class="btn primary" href="contact.html">Request a quote</a><a class="btn glass" href="tel:14034540203">Call {BUSINESS['phone']}</a></div></div></section>
<section class="section"><div class="section-head"><p class="eyebrow">What customers ask for</p><h2>Clear service scope, plain language.</h2><p>This page supports a specific search intent while still moving the customer toward the right quote instead of a generic booking form.</p></div><div class="feature-grid">{''.join(f'<article><h3>{item}</h3><p>B&M confirms vehicle size, current condition, timing, and any add-ons before the appointment is booked.</p></article>' for item in data['items'])}</div></section>
<section class="section dark-band"><div class="section-head"><p class="eyebrow">Related services</p><h2>Often booked together.</h2></div><div class="hub-grid"><a href="auto-detailing.html">Auto detailing<span>Interior and exterior</span></a><a href="paint-correction.html">Paint correction<span>Swirls and gloss</span></a><a href="ceramic-coating.html">Ceramic coating<span>Gloss and maintenance</span></a><a href="paint-protection-film.html">Paint protection film<span>Rock-chip defence</span></a></div></section>{cta()}"""
    pages[filename] = simple_page(filename, data["title"], data["desc"], body)

for filename in service_details:
    pages[filename] = service_page(filename)

CSS = r"""
:root{--black:#080a0c;--graphite:#0d1114;--panel:#14191d;--line:#273039;--text:#f4f1eb;--muted:#a7adb1;--soft:#d8d2c8;--accent:#a8875d;--accent2:#5c7374;--max:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:112px}body{margin:0;background:var(--black);color:var(--text);font-family:"Manrope","Aptos","Segoe UI",Arial,sans-serif;line-height:1.58;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.skip-link{position:absolute;left:-999px;top:1rem;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}.skip-link:focus{left:1rem;width:auto;height:auto;clip-path:none;z-index:99;background:#fff;color:#000;padding:.8rem 1rem;min-height:44px}.site-header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:1.4rem;padding:2.55rem clamp(1rem,3vw,2.25rem) 1rem;background:rgba(8,10,12,.83);border-bottom:1px solid rgba(255,255,255,.08);backdrop-filter:blur(18px)}.top-line{position:absolute;left:0;right:0;top:0;display:flex;justify-content:center;gap:1.2rem;padding:.45rem 1rem;border-bottom:1px solid rgba(255,255,255,.07);color:var(--muted);font-size:.78rem}.top-line a{color:var(--soft);font-weight:760}.brand{display:flex;align-items:center;gap:.75rem;min-width:max-content}.brand-mark{display:grid;place-items:center;width:2.6rem;height:2.6rem;border:1px solid rgba(168,135,93,.55);color:var(--soft);font-weight:700;letter-spacing:.02em}.brand strong{display:block;font-size:.9rem;letter-spacing:.035em;text-transform:uppercase;font-weight:700}.brand small{display:block;color:var(--muted);font-size:.72rem}.desktop-nav{display:flex;gap:1.1rem;margin-left:auto}.desktop-nav a,.site-footer a{color:var(--muted);font-size:.9rem}.desktop-nav a:hover,.desktop-nav .active,.site-footer a:hover{color:var(--text)}.header-cta,.btn{border:1px solid rgba(168,135,93,.7);background:var(--accent);color:#111;padding:.82rem 1.05rem;font-weight:720;letter-spacing:.035em;text-transform:uppercase;font-size:.76rem}.btn{display:inline-flex;justify-content:center;align-items:center;min-height:46px}.btn.secondary,.btn.glass{background:transparent;color:var(--text);border-color:rgba(255,255,255,.24)}.btn.small{padding:.65rem .8rem;min-height:auto}.menu-toggle{display:none;background:none;border:0;padding:.6rem;min-width:44px;min-height:44px}.menu-toggle span{display:block;width:24px;height:2px;background:var(--text);margin:5px 0}.mobile-panel{display:none}.hero{position:relative;min-height:92vh;display:grid;align-items:end;overflow:hidden;background:#050607}.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.hero-overlay{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.93),rgba(0,0,0,.62),rgba(0,0,0,.26)),linear-gradient(0deg,rgba(8,10,12,.98),rgba(8,10,12,.25) 46%,transparent)}.hero-content{position:relative;z-index:1;width:min(var(--max),calc(100% - 2rem));margin:0 auto;padding:10rem 0 6.5rem}.eyebrow{color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.16em;font-size:.74rem;margin:0 0 .9rem}h1,h2,h3{line-height:1.07;margin:0;color:var(--text);font-weight:700;letter-spacing:0}h1{font-size:clamp(2.35rem,5.45vw,5.35rem);max-width:1060px}h2{font-size:clamp(1.75rem,3vw,2.85rem)}h3{font-size:1.18rem;font-weight:700}.hero p,.subhero p,.section-head p{max-width:780px;color:var(--soft);font-size:1.02rem}.hero-actions,.cta-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem}.hero-points{display:flex;flex-wrap:wrap;gap:.65rem;margin-top:2.2rem}.hero-points span,.proof-list span,.area-tags span{border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);padding:.55rem .75rem;color:var(--soft);font-size:.86rem}.trust-strip{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#0b0e10}.trust-strip div{padding:1.35rem clamp(1rem,3vw,2rem);border-right:1px solid var(--line)}.trust-strip strong{display:block;color:#fff}.trust-strip span{color:var(--muted);font-size:.9rem}.quick-paths{display:grid;grid-template-columns:repeat(4,1fr);width:min(var(--max),calc(100% - 2rem));margin:2rem auto 0;border:1px solid var(--line);background:#0d1114}.quick-paths a{padding:1.2rem;border-right:1px solid var(--line)}.quick-paths span{display:block;color:var(--accent);font-weight:760}.quick-paths strong{display:block;font-size:1.05rem}.quick-paths em{display:block;color:var(--muted);font-style:normal;font-size:.9rem}.section,.split-section,.process-section,.local-section,.contact-layout,.subhero{width:min(var(--max),calc(100% - 2rem));margin:0 auto;padding:7.4rem 0;scroll-margin-top:112px}.reviews-hero{padding-bottom:3rem}.review-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;width:min(var(--max),calc(100% - 2rem));margin:0 auto 2rem}.review-stats article{border:1px solid var(--line);background:var(--panel);padding:1.2rem}.review-stats strong{display:block;font-size:2rem}.review-stats span{color:var(--muted)}.section-head{display:block;max-width:820px;margin-bottom:2rem}.section-head>p:not(.eyebrow){margin-top:1rem}.section-head h2{max-width:760px}.section-head.stacked{display:block}.service-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.15rem}.service-card{background:linear-gradient(180deg,#171d21,#101417);border:1px solid var(--line);min-height:100%;display:flex;flex-direction:column;box-shadow:0 18px 55px rgba(0,0,0,.18)}.service-card img{height:225px;width:100%;object-fit:cover;filter:saturate(.9) contrast(1.08)}.service-card-body{padding:1.35rem;display:flex;flex-direction:column;flex:1}.card-kicker{color:var(--accent)!important;text-transform:uppercase;letter-spacing:.12em;font-size:.7rem;font-weight:760;margin:.05rem 0 .7rem}.service-card-body ul{margin-bottom:1.2rem}.service-link{margin-top:auto;padding-top:1rem;border-top:1px solid var(--line);display:inline-flex;align-self:flex-start}.service-card p,.package-card p,.feature-grid p,.before-card p,.review-grid p,.site-footer p,.info-panel li,.faq-list p,.contact-card p{color:var(--muted)}.service-card ul{padding-left:1.1rem;color:var(--soft);font-size:.92rem}.service-card a,.text-link{color:var(--accent);font-weight:760}.split-section{display:grid;grid-template-columns:1.05fr .95fr;gap:3rem;align-items:center}.split-section>img{height:560px;width:100%;object-fit:cover}.proof-list{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.5rem}.info-panel{border:1px solid var(--line);background:linear-gradient(180deg,#171d21,#101417);padding:2rem}.dark-band{width:100%;max-width:none;background:#0c1013;border-block:1px solid var(--line);padding-inline:max(1rem,calc((100vw - var(--max))/2))}.before-grid,.review-grid,.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.before-card,.review-grid article,.feature-grid article,.package-card{border:1px solid var(--line);background:var(--panel);padding:1.1rem}.package-card{display:flex;flex-direction:column;min-height:100%;padding:1.45rem;background:linear-gradient(180deg,#161c20,#11161a)}.package-card h3{font-size:1.12rem}.package-card p{margin:.75rem 0}.package-card .btn{align-self:flex-start;margin-top:auto;min-height:42px;padding:.72rem .9rem;white-space:nowrap}.google-review{display:flex;flex-direction:column;gap:.75rem;min-height:100%;background:linear-gradient(180deg,#151a1e,#101417)!important}.review-top{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start}.review-top strong{line-height:1.2}.review-top span{color:var(--accent);font-weight:760;white-space:nowrap;letter-spacing:.08em}.review-date{font-size:.92rem;margin:0}.proof-image{width:100%;height:340px;object-fit:cover;margin-bottom:1rem;filter:saturate(.92) contrast(1.08)}.package-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.1rem}.package-grid.wide{grid-template-columns:repeat(3,minmax(0,1fr))}.package-price{color:var(--accent)!important;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:.88rem}.package-meta{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin:1.2rem 0}.package-meta span{border-top:1px solid var(--line);padding-top:.7rem}.package-meta small{display:block;color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.04em}.package-meta strong{display:block;color:var(--soft);font-weight:720;margin-top:.15rem;font-size:.96rem}.service-packages{grid-template-columns:repeat(2,minmax(260px,1fr));max-width:820px}.hub-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.hub-grid a{border:1px solid var(--line);background:var(--panel);padding:1.1rem;font-weight:760}.hub-grid span{display:block;color:var(--muted);font-weight:500;margin-top:.35rem}.process-section{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:2rem}.steps article{padding:1.2rem;border-left:1px solid var(--line)}.steps span{color:var(--accent);font-weight:760}.local-section{display:grid;grid-template-columns:.9fr 1.1fr;gap:2rem;align-items:center}.area-tags{display:flex;flex-wrap:wrap;gap:.7rem}.faq-list{display:grid;gap:.65rem}.faq-list details{background:var(--panel);border:1px solid var(--line);padding:1.1rem}.faq-list summary{cursor:pointer;font-weight:760}.final-cta{width:min(var(--max),calc(100% - 2rem));margin:0 auto 6rem;padding:3rem;border:1px solid rgba(168,135,93,.4);background:linear-gradient(135deg,#171b1d,#0d1012);display:flex;align-items:center;justify-content:space-between;gap:2rem}.subhero{display:grid;grid-template-columns:1fr .8fr;gap:3rem;align-items:center;padding-top:5rem}.subhero.text-only{display:block;max-width:930px}.subhero img{height:480px;width:100%;object-fit:cover}.filter-row{display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:1.5rem}.filter-row button{border:1px solid var(--line);background:var(--panel);color:var(--soft);padding:.7rem 1rem}.filter-row .active{border-color:var(--accent);color:#fff}.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.gallery-grid figure{margin:0;background:var(--panel);border:1px solid var(--line)}.gallery-grid img{height:300px;width:100%;object-fit:cover}.gallery-grid figcaption{padding:1rem;color:var(--soft)}.comparison{width:min(var(--max),100%);max-width:100%;margin:auto;overflow-x:auto}.comparison h2{margin:0 0 1.4rem}.comparison table{width:100%;border-collapse:collapse}.comparison th,.comparison td{border-bottom:1px solid var(--line);padding:1rem;text-align:left}.comparison th{color:var(--accent);text-transform:uppercase;font-size:.8rem}.contact-layout{display:grid;grid-template-columns:1.35fr .65fr;gap:2rem}.quote-form{display:grid;grid-template-columns:1fr 1fr;gap:1rem;background:var(--panel);border:1px solid var(--line);padding:1.2rem}.quote-form label{display:grid;gap:.4rem;color:var(--soft);font-weight:700}.quote-form input,.quote-form select,.quote-form textarea{width:100%;background:#0b0e10;border:1px solid var(--line);color:var(--text);padding:.85rem;font:inherit}.quote-form .full,.quote-form button{grid-column:1/-1}.contact-card{background:linear-gradient(180deg,#171d21,#101417);border:1px solid var(--line);padding:1.4rem;align-self:start;position:sticky;top:6rem}.map-embed{border:1px solid var(--line);background:#0b0e10;margin-top:1rem;overflow:hidden}.map-embed iframe{width:100%;height:260px;border:0;filter:grayscale(.75) contrast(1.05) invert(.9)}.map-embed a{display:block;padding:.85rem 1rem;color:var(--accent);font-weight:760;border-top:1px solid var(--line)}.site-footer{border-top:1px solid var(--line);padding:4rem clamp(1rem,3vw,2rem) 2rem;background:#090b0d}.footer-grid{display:grid;grid-template-columns:1.3fr .7fr .9fr 1fr;gap:2rem;width:min(var(--max),100%);margin:auto}.site-footer h3{font-size:.9rem;text-transform:uppercase;color:var(--accent)}.site-footer a{display:block;margin:.42rem 0}.footer-bottom{width:min(var(--max),100%);margin:2rem auto 0;padding-top:1.2rem;border-top:1px solid var(--line);display:flex;justify-content:space-between;color:var(--muted);font-size:.85rem}
@media (max-width:1050px){html{scroll-padding-top:74px}.top-line{display:none}.site-header{padding:.8rem 1rem}.desktop-nav{display:none}.header-cta{display:inline-flex;margin-left:auto;padding:.65rem .78rem;font-size:.7rem}.menu-toggle{display:block;margin-left:.25rem}.mobile-panel{position:fixed;inset:62px 0 auto 0;z-index:40;background:#090b0d;border-bottom:1px solid var(--line);padding:1rem;transform:translateY(-130%);transition:.25s}.mobile-panel.open{display:block;transform:translateY(0)}.mobile-panel nav{display:grid;gap:.9rem}.mobile-book{background:var(--accent);color:#111;padding:1rem;text-align:center;font-weight:760}.service-grid,.package-grid,.package-grid.wide,.quick-paths,.hub-grid{grid-template-columns:repeat(2,1fr)}.trust-strip,.steps,.review-stats{grid-template-columns:repeat(2,1fr)}.section-head,.final-cta{display:block}.before-grid,.review-grid,.feature-grid,.gallery-grid{grid-template-columns:1fr 1fr}.split-section,.subhero,.local-section,.contact-layout,.footer-grid{grid-template-columns:1fr}.contact-card{position:static}}@media (max-width:680px){h1{font-size:2.18rem}.hero{min-height:91vh}.hero-content{padding:7.5rem 0 5.25rem}.section,.split-section,.process-section,.local-section,.contact-layout,.subhero{padding:4.8rem 0}.reviews-hero{padding-bottom:2rem}.service-grid,.package-grid,.package-grid.wide,.quick-paths,.hub-grid,.trust-strip,.steps,.review-stats,.before-grid,.review-grid,.feature-grid,.gallery-grid{grid-template-columns:1fr}.quote-form{grid-template-columns:1fr}.final-cta{padding:1.5rem}.proof-image{height:230px}.footer-bottom{display:block}.brand small{display:none}.site-header{padding:.8rem 1rem}.subhero img,.split-section>img{height:330px}.contact-layout{padding-top:2rem}.comparison{overflow:visible;padding-inline:1rem}.comparison table,.comparison thead,.comparison tbody,.comparison tr,.comparison th,.comparison td{display:block;width:100%}.comparison thead{display:none}.comparison tr{border:1px solid var(--line);background:var(--panel);margin-bottom:.8rem}.comparison td{display:grid;grid-template-columns:8.5rem 1fr;gap:1rem;border-bottom:1px solid var(--line);padding:.85rem 1rem}.comparison td:last-child{border-bottom:0}.comparison td::before{content:attr(data-label);color:var(--accent);font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;font-weight:760}}
.footer-bottom{align-items:center;gap:1rem;flex-wrap:wrap}.site-credit{display:inline-flex!important;align-items:center;gap:.35rem;margin:0!important;padding:.5rem .72rem;border:1px solid rgba(168,135,93,.28);background:rgba(168,135,93,.08);color:var(--soft)!important;text-transform:uppercase;letter-spacing:.08em;font-size:.72rem;font-weight:760}.site-credit strong{color:var(--accent);font-weight:800}.site-credit:hover{border-color:rgba(168,135,93,.55);background:rgba(168,135,93,.13);color:#fff!important}@media (max-width:680px){.footer-bottom{display:grid;gap:.75rem}.site-credit{justify-self:start}}
.header-cta{white-space:nowrap}
.site-footer{padding:3.6rem clamp(1rem,3vw,2rem) 1.8rem}.footer-grid{grid-template-columns:minmax(260px,1.15fr) minmax(120px,.55fr) minmax(190px,.82fr) minmax(230px,.9fr);gap:clamp(1.5rem,4vw,4rem);align-items:start}.footer-brand{margin-bottom:1rem}.footer-brand .brand-mark{width:2.45rem;height:2.45rem}.footer-brand strong{font-size:.88rem}.footer-brand small{font-size:.7rem}.site-footer h3{font-size:.74rem;line-height:1;letter-spacing:.05em;margin:0 0 .8rem}.site-footer p,.site-footer a{font-size:.86rem;line-height:1.52}.site-footer a{margin:.38rem 0}.footer-copy{max-width:360px;margin:.8rem 0 0}.footer-contact p{max-width:280px;margin:.2rem 0 1.05rem}.footer-bottom{font-size:.8rem}.footer-bottom span{line-height:1.45}.site-footer .site-credit{font-size:.72rem;line-height:1}@media (max-width:1120px){.footer-grid{grid-template-columns:1.1fr .8fr;row-gap:2.3rem}.footer-contact p{max-width:360px}}@media (max-width:680px){.site-footer{padding:3rem 1rem 1.7rem}.footer-grid{grid-template-columns:1fr;gap:2rem}.footer-copy,.footer-contact p{max-width:100%}.site-footer p,.site-footer a{font-size:.88rem}.site-footer h3{margin-bottom:.65rem}.footer-bottom{font-size:.82rem}.site-footer .site-credit{font-size:.74rem}}
.trust-strip a{display:block;padding:1.35rem clamp(1rem,3vw,2rem);border-right:1px solid var(--line)}.trust-strip a:hover{background:rgba(255,255,255,.035)}.section-actions{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem}.package-compare-cards{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:1rem}.package-compare-cards article{display:flex;flex-direction:column;gap:1rem;border:1px solid var(--line);background:linear-gradient(180deg,#161c20,#101417);padding:1.2rem;min-height:100%}.package-compare-cards h3{font-size:1.08rem}.package-compare-cards p{color:var(--muted);margin:.45rem 0 0}.package-compare-cards dl{display:grid;gap:.65rem;margin:0;color:var(--soft);font-size:.9rem}.package-compare-cards dt{color:var(--accent);font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;font-weight:760}.package-compare-cards dd{margin:0}.package-compare-cards .btn{align-self:flex-start;margin-top:auto}.intent-review p:last-child{display:-webkit-box;-webkit-line-clamp:6;-webkit-box-orient:vertical;overflow:hidden}.mobile-sticky-cta{display:none}.mobile-sticky-cta a{display:grid;place-items:center;min-height:48px;font-size:.74rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em}.mobile-sticky-cta a:first-child{background:var(--accent);color:#111}.mobile-sticky-cta a:last-child{background:#0e1215;color:var(--text);border-left:1px solid var(--line)}
@media (max-width:1180px){.package-compare-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.package-compare-cards article:last-child{grid-column:1/-1}}@media (max-width:680px){body{padding-bottom:56px}.package-compare-cards{grid-template-columns:1fr}.package-compare-cards article:last-child{grid-column:auto}.section-actions .btn,.hero-actions .btn,.cta-actions .btn{width:100%}.mobile-sticky-cta{position:fixed;left:0;right:0;bottom:0;z-index:60;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--line);box-shadow:0 -18px 50px rgba(0,0,0,.35)}}
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
sitemap_pages = [name for name in pages if name != "404.html"]
def sitemap_loc(name):
    return "https://bmautodetailing.ca/" if name == "index.html" else f"https://bmautodetailing.ca/{name}"
(ROOT / "sitemap.xml").write_text("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(f"  <url><loc>{sitemap_loc(name)}</loc></url>" for name in sitemap_pages) + "\n</urlset>\n", encoding="utf-8")

print(f"Built {len(pages)} pages in {ROOT}")














