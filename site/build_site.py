"""Build the Data Analysis TOT static site (D2P-style design) from docs/*.md.

Generates at repo root: index.html, agenda.html, guide.html, workbook.html,
materials.html, styles.css. Run: python3 site/build_site.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE_NAME = "Data Analysis & Report Writing TOT"

NAV = [
    ("index.html", "Home"),
    ("agenda.html", "Agenda"),
    ("guide.html", "Facilitator Guide"),
    ("workbook.html", "Participant Workbook"),
    ("materials.html", "Materials"),
]

# ---------------------------------------------------------------- CSS
CSS = """:root {
  --purple: #5B2A6F;
  --purple-deep: #3E1C4D;
  --orange: #F2994A;
  --orange-deep: #D97B2A;
  --cream: #FAF7F2;
  --ink: #2B2530;
  --ink-soft: #5A5260;
  --line: #E6DFD6;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--cream);
  color: var(--ink);
  line-height: 1.65;
}
h1, h2, h3, h4 {
  font-family: 'Fraunces', Georgia, serif;
  color: var(--purple-deep);
  font-weight: 500;
  line-height: 1.3;
}
a { color: var(--orange-deep); }
.container { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }

/* ---------- Navigation ---------- */
.navbar {
  background: #FFFFFF;
  border-bottom: 1px solid var(--line);
  position: sticky; top: 0; z-index: 10;
}
.nav-container {
  max-width: 1100px; margin: 0 auto; padding: 1rem 1.5rem;
  display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: 0.75rem;
}
.logo {
  font-family: 'Fraunces', serif; font-weight: 600; font-size: 1.02rem;
  color: var(--purple-deep); letter-spacing: 0.01em; text-decoration: none;
}
.nav-menu { list-style: none; display: flex; gap: 1.6rem; flex-wrap: wrap; }
.nav-menu a {
  text-decoration: none; font-size: 0.92rem; font-weight: 500;
  color: var(--ink-soft); padding-bottom: 0.25rem;
  border-bottom: 2px solid transparent;
  transition: border-color 0.2s, color 0.2s;
}
.nav-menu a:hover, .nav-menu a.active {
  color: var(--orange-deep); border-bottom-color: var(--orange);
}

/* ---------- Hero / page header ---------- */
.hero {
  background: linear-gradient(160deg, var(--purple-deep) 0%, var(--purple) 65%, var(--orange-deep) 130%);
  color: #FFF; padding: 5.5rem 1.5rem 4.5rem; text-align: center;
}
.hero-content { max-width: 800px; margin: 0 auto; }
.hero h1 {
  color: #FFF; font-size: clamp(2rem, 4.2vw, 3rem);
  font-weight: 500; line-height: 1.2; margin-bottom: 1.25rem;
}
.hero-subtitle {
  font-size: 1.1rem; font-weight: 600; letter-spacing: 0.06em;
  text-transform: uppercase; color: #FBD9B0; margin-bottom: 0.9rem;
}
.hero-description { font-size: 1.05rem; color: #EFE4F1; max-width: 620px; margin: 0 auto; }
.page-header {
  background: linear-gradient(160deg, var(--purple-deep) 0%, var(--purple) 65%, var(--orange-deep) 130%);
  color: #FFF; padding: 3.5rem 1.5rem 3rem; text-align: center;
}
.page-header h1 {
  color: #FFF; font-size: clamp(1.8rem, 3.6vw, 2.5rem);
  font-weight: 500; margin-bottom: 0.6rem;
}
.page-header p { color: #EFE4F1; font-size: 1.05rem; max-width: 700px; margin: 0 auto; }
main { padding: 3rem 0 4rem; }

/* ---------- Welcome / intro ---------- */
.welcome-section { max-width: 780px; margin: 0 auto 2.5rem; padding: 3.5rem 1.5rem 1rem; text-align: center; }
.welcome-section h2 { margin-bottom: 1rem; font-size: 1.6rem; }
.welcome-section p { color: var(--ink-soft); margin-bottom: 1rem; }
.welcome-banner {
  max-width: 900px; margin: 0 auto 1rem; border-radius: 12px; overflow: hidden;
  border: 1px solid var(--line);
}
.welcome-banner img { width: 100%; display: block; }

/* ---------- Info cards ---------- */
.info-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; padding-top: 1rem; }
.info-card {
  background: #FFF; border: 1px solid var(--line);
  border-top: 3px solid var(--orange); border-radius: 10px; padding: 1.75rem;
}
.info-card h3 { font-size: 1.15rem; margin-bottom: 0.85rem; }
.info-card p, .info-card li { color: var(--ink-soft); }
.info-card p { margin-bottom: 0.6rem; }
.info-card ul, .info-card ol { padding-left: 1.2rem; }
.info-card li { margin-bottom: 0.4rem; }

/* ---------- Key details ---------- */
.key-details h2 { text-align: center; margin-bottom: 2rem; font-size: 1.6rem; }
.details-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }
.detail-item {
  text-align: center; padding: 1.5rem 1rem; background: #FFF;
  border: 1px solid var(--line); border-radius: 10px;
}
.detail-item h4 {
  font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--orange-deep); font-family: 'Inter', sans-serif;
  font-weight: 700; margin-bottom: 0.6rem;
}
.detail-item p { color: var(--ink-soft); font-size: 0.95rem; }
section { padding: 3.5rem 0; }
section.tight { padding: 1.5rem 0 3.5rem; }

/* ---------- CTA ---------- */
.cta-section { text-align: center; }
.cta-section h2 { margin-bottom: 1.5rem; font-size: 1.6rem; }
.cta-buttons { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }
.btn {
  display: inline-block; padding: 0.8rem 1.6rem; border-radius: 6px;
  text-decoration: none; font-weight: 600; font-size: 0.95rem;
  transition: transform 0.15s, box-shadow 0.15s;
}
.btn:hover { transform: translateY(-1px); }
.btn-primary { background: var(--orange); color: #FFF; }
.btn-primary:hover { box-shadow: 0 6px 16px rgba(217,123,42,0.35); }
.btn-secondary { background: #FFF; color: var(--purple-deep); border: 1px solid var(--line); }
.btn-secondary:hover { border-color: var(--purple); }

/* ---------- Agenda ---------- */
.agenda-intro { max-width: 780px; margin: 0 auto 2.5rem; text-align: center; }
.agenda-intro h2 { margin-bottom: 1rem; font-size: 1.4rem; }
.agenda-intro p { color: var(--ink-soft); margin-bottom: 1rem; }
.agenda-day { margin-bottom: 2.75rem; }
.day-header { font-size: 1.3rem; margin-bottom: 0.4rem; padding-bottom: 0.6rem; border-bottom: 2px solid var(--orange); }
.day-theme { color: var(--ink-soft); margin-bottom: 1.25rem; font-size: 0.98rem; }
.agenda-table { background: #FFF; border: 1px solid var(--line); border-radius: 10px; overflow: hidden; margin-bottom: 1.5rem; }
.agenda-row { display: grid; grid-template-columns: 110px 60px 1fr; border-bottom: 1px solid var(--line); }
.agenda-row:last-child { border-bottom: none; }
.agenda-row > div { padding: 0.85rem 1.1rem; border-right: 1px solid var(--line); font-size: 0.93rem; }
.agenda-row > div:last-child { border-right: none; }
.agenda-row.header {
  background: var(--purple-deep); color: #FFF; font-weight: 600;
  font-family: 'Inter', sans-serif; font-size: 0.85rem;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.agenda-row.header > div { border-right: 1px solid rgba(255,255,255,0.15); }
.agenda-row.break { background: #FDF3E7; color: var(--orange-deep); font-weight: 600; }
.agenda-row.block-label { background: #F3EAF6; }
.agenda-row.block-label > div { grid-column: 1 / -1; border-right: none; font-weight: 600; color: var(--purple-deep); font-size: 0.9rem; }
.session-type {
  display: inline-block; font-size: 0.78rem; font-weight: 600;
  padding: 0.2rem 0.6rem; border-radius: 20px;
  background: #F3EAF6; color: var(--purple); margin-right: 0.5rem;
}

/* ---------- Materials ---------- */
.materials-section { margin-bottom: 3rem; }
.materials-section h2 { font-size: 1.4rem; margin-bottom: 1.5rem; padding-bottom: 0.6rem; border-bottom: 2px solid var(--orange); }
.materials-category {
  background: #FFF; border: 1px solid var(--line);
  border-top: 3px solid var(--orange); border-radius: 10px;
  padding: 1.75rem; margin-bottom: 1.5rem;
}
.materials-category h3 { font-size: 1.15rem; margin-bottom: 0.6rem; }
.materials-category > p { color: var(--ink-soft); margin-bottom: 1rem; }
.materials-list ul { padding-left: 1.2rem; color: var(--ink-soft); }
.materials-list li { margin-bottom: 0.45rem; }
.materials-list a { color: var(--orange-deep); font-weight: 500; }
.file-tag {
  display: inline-block; font-size: 0.72rem; font-weight: 700;
  padding: 0.12rem 0.5rem; border-radius: 4px; margin-left: 0.5rem;
  background: #F3EAF6; color: var(--purple); vertical-align: middle;
}

/* ---------- Prose (converted markdown) ---------- */
.prose { max-width: 860px; margin: 0 auto; }
.prose h2 {
  font-size: 1.45rem; margin: 2.5rem 0 1rem; padding-bottom: 0.6rem;
  border-bottom: 2px solid var(--orange);
}
.prose h2:first-child { margin-top: 0; }
.prose h3 { font-size: 1.18rem; margin: 1.8rem 0 0.7rem; }
.prose h4 { font-size: 1.02rem; margin: 1.4rem 0 0.5rem; font-family: 'Inter', sans-serif; font-weight: 700; }
.prose p { color: var(--ink-soft); margin-bottom: 0.9rem; }
.prose ul, .prose ol { padding-left: 1.3rem; color: var(--ink-soft); margin-bottom: 0.9rem; }
.prose li { margin-bottom: 0.35rem; }
.prose strong { color: var(--ink); }
.prose table {
  width: 100%; border-collapse: collapse; background: #FFF;
  border: 1px solid var(--line); border-radius: 10px; overflow: hidden;
  margin: 1.2rem 0; font-size: 0.92rem; display: block; overflow-x: auto;
}
.prose thead { background: var(--purple-deep); color: #FFF; }
.prose th {
  padding: 0.7rem 0.9rem; text-align: left; font-family: 'Inter', sans-serif;
  font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.04em;
  border-right: 1px solid rgba(255,255,255,0.15); white-space: nowrap;
}
.prose td { padding: 0.7rem 0.9rem; border-bottom: 1px solid var(--line); border-right: 1px solid var(--line); color: var(--ink-soft); vertical-align: top; }
.prose tr:last-child td { border-bottom: none; }
.prose blockquote {
  background: #F3EAF6; border-left: 4px solid var(--purple);
  padding: 1.1rem 1.4rem; border-radius: 8px; margin: 1.2rem 0;
}
.prose blockquote p { color: var(--ink-soft); font-size: 0.95rem; margin-bottom: 0.5rem; }
.prose blockquote p:last-child { margin-bottom: 0; }
.prose blockquote strong { color: var(--purple-deep); }
.prose code {
  font-family: ui-monospace, monospace; font-size: 0.88em;
  background: #F1ECE4; padding: 0.15rem 0.4rem; border-radius: 4px;
}
.prose pre {
  background: var(--purple-deep); color: #EFE4F1; padding: 1.2rem;
  border-radius: 10px; overflow-x: auto; margin: 1.2rem 0;
}
.prose pre code { background: none; padding: 0; color: inherit; }
.prose hr { border: none; border-top: 1px solid var(--line); margin: 2rem 0; }

/* ---------- Note banner ---------- */
.note-banner {
  background: #F3EAF6; border-left: 4px solid var(--purple);
  padding: 1.25rem 1.5rem; border-radius: 8px;
  color: var(--ink-soft); font-size: 0.95rem;
  max-width: 780px; margin: 0 auto 2rem;
}
.note-banner strong { color: var(--purple-deep); }

/* ---------- Footer ---------- */
.footer { background: var(--purple-deep); color: #E9DEEC; padding: 2.5rem 0; margin-top: 1rem; }
.footer-content { text-align: center; }
.footer-text p { font-size: 0.85rem; color: #C9B6CE; max-width: 760px; margin: 0 auto 0.4rem; }
.footer-text a { color: #FBD9B0; }

/* ---------- Responsive ---------- */
@media (max-width: 768px) {
  .agenda-row { grid-template-columns: 1fr; }
  .agenda-row > div { border-right: none; border-bottom: 1px solid var(--line); }
  .agenda-row > div:last-child { border-bottom: none; }
}
@media (max-width: 720px) {
  .info-grid, .details-grid { grid-template-columns: 1fr; }
  .nav-menu { gap: 1rem; }
  .hero { padding: 4rem 1.5rem 3.5rem; }
}
"""

# ---------------------------------------------------------------- template
FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

def page(title, active, header_html, body_html):
    nav_items = "\n".join(
        f'<li><a href="{href}" class="{ "active" if href == active else ""}">{label}</a></li>'
        for href, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {SITE_NAME}</title>
<meta name="description" content="Data Analysis and Report Writing Training of Trainers — Data for Health Initiative, Kigali, Rwanda, 22–26 March 2027.">
{FONTS}
<link rel="stylesheet" href="styles.css">
</head>
<body>
<nav class="navbar">
  <div class="nav-container">
    <a class="logo" href="index.html">📊 Data Analysis TOT</a>
    <ul class="nav-menu">
      {nav_items}
    </ul>
  </div>
</nav>
{header_html}
<main>
{body_html}
</main>
<footer class="footer">
  <div class="container footer-content">
    <div class="footer-text">
      <p><strong style="color:#FBD9B0">Data Analysis &amp; Report Writing TOT</strong> · Data for Health Initiative · Bloomberg Philanthropies · CDC Foundation</p>
      <p>Kigali, Rwanda · 22–26 March 2027 · All datasets on this site are 100% synthetic demo data for training only.</p>
      <p><a href="https://github.com/datatopolicy/Data_Analysis_TOT">View source on GitHub</a></p>
    </div>
  </div>
</footer>
</body>
</html>
"""

def hero(subtitle, title, description):
    return f"""<header class="hero">
  <div class="hero-content">
    <p class="hero-subtitle">{subtitle}</p>
    <h1>{title}</h1>
    <p class="hero-description">{description}</p>
  </div>
</header>"""

def page_header(title, subtitle):
    return f"""<header class="page-header">
  <h1>{title}</h1>
  <p>{subtitle}</p>
</header>"""

# ---------------------------------------------------------------- markdown
import markdown as md_lib

MD = md_lib.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

def md_to_html(text):
    # demote headings one level so page <h1> stays unique
    text = re.sub(r"^#### ", "##### ", text, flags=re.M)
    text = re.sub(r"^### ", "#### ", text, flags=re.M)
    text = re.sub(r"^## ", "### ", text, flags=re.M)
    text = re.sub(r"^# ", "## ", text, flags=re.M)
    MD.reset()
    html = MD.convert(text)
    # fix asset links: pages live at root, docs used ../assets
    html = html.replace('href="../assets/', 'href="assets/')
    html = html.replace('src="../assets/', 'src="assets/')
    return html

def md_file(name):
    return (DOCS / name).read_text(encoding="utf-8")

# ---------------------------------------------------------------- agenda parsing
def parse_md_table(lines):
    """Parse consecutive markdown table lines into (headers, rows)."""
    headers, rows = [], []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if re.fullmatch(r"[:\- ]+", "".join(cells).replace(" ", "")) and set("".join(cells)) <= set(":- "):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows

def find_tables(text):
    """Yield (heading_context, headers, rows) for each markdown table."""
    lines = text.splitlines()
    out, i, last_h2, last_h3 = [], 0, "", ""
    while i < len(lines):
        line = lines[i]
        m2 = re.match(r"^##\s+(.*)", line)
        m3 = re.match(r"^###\s+(.*)", line)
        if m2: last_h2, last_h3 = m2.group(1).strip(), ""
        elif m3: last_h3 = m3.group(1).strip()
        if line.strip().startswith("|"):
            tbl = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i]); i += 1
            h, r = parse_md_table(tbl)
            if h:
                ctx = last_h3 or last_h2
                out.append((ctx, h, r))
            continue
        i += 1
    return out

def is_break(text):
    t = text.lower()
    return any(k in t for k in ["break", "lunch", "tea &", "tea+", "coffee"])

DAY_META = [
    ("Day 1 — Mon 22 Mar", "From data to decisions", "Opening, D4H overview and course objectives. Why analysis objectives come first; drafting objectives on the Demoland TB dataset. Country teams meet; diagnostic pre-test."),
    ("Day 2 — Tue 23 Mar", "Rates, denominators & descriptive analysis", "Census denominators and rate calculation; descriptive statistics in Excel; data-quality checks on the TB register and CRVS extracts."),
    ("Day 3 — Wed 24 Mar", "Cleaning data & communicating results", "Reproducible Excel cleaning workflows; honest tables, charts and maps; equity-focused disaggregation."),
    ("Day 4 — Thu 25 Mar", "From findings to recommendations", "IMRAD report writing; specific, actionable, audience-targeted recommendations; templates and SOPs; group project work."),
    ("Day 5 — Fri 26 Mar", "Presentations & trainer preparation", "Country-team presentations with peer feedback; 10-minute Excel micro-teach; cascade planning and country action plans; post-test and close."),
]

def build_agenda_days():
    sections = []
    for n, (day_title, theme, desc) in enumerate(DAY_META, start=1):
        text = md_file(f"facilitator-guide/day-{n}.md")
        tables = [t for t in find_tables(text) if any("clock" in h.lower() for h in t[1])]
        blocks = []
        for ctx, headers, rows in tables:
            trs = ['<div class="agenda-row header"><div>Time</div><div>Min</div><div>Session</div></div>']
            for r in rows:
                time = r[0] if len(r) > 0 else ""
                mins = r[1] if len(r) > 1 else ""
                sess = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", r[2] if len(r) > 2 else "")
                cls = "agenda-row break" if is_break(sess) else "agenda-row"
                trs.append(f'<div class="{cls}"><div>{time}</div><div>{mins}</div><div>{sess}</div></div>')
            label = f'<div class="agenda-row block-label"><div>{ctx}</div></div>' if ctx else ""
            blocks.append(f'{label}<div class="agenda-table">{"".join(trs)}</div>')
        sections.append(f"""<div class="agenda-day">
  <h2 class="day-header">{day_title}: {theme}</h2>
  <p class="day-theme">{desc}</p>
  {"".join(blocks)}
</div>""")
    return "\n".join(sections)

# ---------------------------------------------------------------- materials
DATASETS = [
    ("DA-TOT_Demo_TB-Register_2021-2025.xlsx", "TB notification register, Demoland 2021–2025 — the running course dataset."),
    ("DA-TOT_Demo_Mortality-CRVS_2021-2025.xlsx", "Cause-of-death extracts from the civil registration system."),
    ("DA-TOT_Demo_Census-Population.xlsx", "Census population denominators by district, age and sex."),
    ("DA-TOT_Exercise_Messy-DHIS2-Extract.xlsx", "Deliberately messy DHIS2-style extract for the Day 2 cleaning exercise."),
    ("DA-TOT_Exercise-Workbook_Day2.xlsx", "Guided Day 2 exercise workbook (rates & descriptive analysis)."),
    ("DA-TOT_Exercise-Workbook_Day3.xlsx", "Guided Day 3 exercise workbook (tables, figures & maps)."),
]
DECKS = [
    ("Day1-Slides_Foundations-and-Data-Preparation.pptx", "31 slides" ),
    ("Day2-Slides_Rates-and-Descriptive-Analysis.pptx", "41 slides"),
    ("Day3-Slides_Communicating-with-Tables-Figures-Maps.pptx", "33 slides"),
    ("Day4-Slides_Recommendations-Templates-Project-Work.pptx", "29 slides"),
    ("Day5-Slides_Presentations-and-Trainer-Preparation.pptx", "31 slides"),
]
TEMPLATES = [
    ("Report-Template_IMRAD.docx", "Structured IMRAD report template with a completed example."),
    ("Analysis-Objectives-Worksheet.docx", "Worksheet for drafting policy-relevant analysis objectives."),
    ("Data-Dictionary-Template.xlsx", "Data dictionary template for documenting datasets."),
    ("SOP-Template_Data-Access-and-Analysis.docx", "Data access and analysis standard operating procedure."),
    ("Group-Presentation-Template.pptx", "12-slide country-team presentation template."),
    ("Pre-Post-Test.docx", "25 MCQs + 2 short-answer questions for the diagnostic pre/post test."),
    ("Pre-Post-Test_Answer-Key.docx", "Answer key for facilitators."),
    ("Daily-Evaluation-Form.docx", "End-of-day feedback form."),
    ("Final-Workshop-Evaluation.docx", "End-of-course evaluation form."),
    ("Country-Action-Plan-Template.docx", "Cascade training and institutionalization action plan."),
]

def file_list(items, folder, ext_label):
    lis = []
    for fname, desc in items:
        ext = fname.rsplit(".", 1)[-1].upper()
        lis.append(
            f'<li><a href="assets/{folder}/{fname}" download>{fname}</a>'
            f'<span class="file-tag">{ext}</span><br><span style="font-size:0.88rem">{desc}</span></li>'
        )
    return '<div class="materials-list"><ul>\n' + "\n".join(lis) + "\n</ul></div>"

# ---------------------------------------------------------------- pages
def build():
    # styles
    (ROOT / "styles.css").write_text(CSS, encoding="utf-8")

    # ---- index ----
    index_body = """<div class="container">
  <div class="welcome-banner"><img src="assets/img/banner.jpg" alt="Public health data training workshop"></div>
  <div class="welcome-section">
    <h2>Welcome to the Data Analysis &amp; Report Writing TOT</h2>
    <p>The Data for Health (D4H) Initiative, supported by Bloomberg Philanthropies and implemented with the CDC Foundation, partners with governments to strengthen the collection and use of public health data for policy and program decision-making.</p>
    <p>Too often, routine surveillance and program data are under-analyzed and under-used: reports are delayed, findings are not disaggregated to reveal inequities, and recommendations are too vague to act on. This five-day Training of Trainers course closes that gap — building a cadre of national trainers who can produce rigorous analyses <em>and</em> teach these skills to others.</p>
  </div>
  <section class="tight">
    <div class="info-grid">
      <div class="info-card">
        <h3>🎯 Course Objectives</h3>
        <p>By the end of the course, participants will be able to:</p>
        <ul>
          <li>Formulate clear, policy-relevant analysis objectives</li>
          <li>Assess data quality and document limitations transparently</li>
          <li>Clean, validate and combine datasets in Excel</li>
          <li>Calculate rates with correct population denominators</li>
          <li>Design honest tables, charts and maps</li>
          <li>Write structured IMRAD reports with actionable recommendations</li>
          <li>Apply adult-learning principles to train others</li>
          <li>Develop a country action plan for cascade training</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>📚 How the Course Works</h3>
        <p>Every concept is practiced on a single running synthetic dataset — tuberculosis notifications for the fictional country of <strong>Demoland (2021–2025)</strong> — so skills build on realistic, policy-relevant material.</p>
        <ul>
          <li><strong>Days 1–2:</strong> Foundations, data preparation, rates &amp; denominators</li>
          <li><strong>Day 3:</strong> Data cleaning, tables, figures &amp; maps</li>
          <li><strong>Day 4:</strong> IMRAD reporting &amp; recommendations</li>
          <li><strong>Day 5:</strong> Team presentations &amp; trainer preparation</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>👥 Participant Profile</h3>
        <ul>
          <li>24 government health professionals — 6 per country team</li>
          <li>Bangladesh, Côte d'Ivoire, Rwanda &amp; Tanzania</li>
          <li>M&amp;E officers, surveillance officers, health statisticians, program managers, HIS focal points</li>
          <li>Prerequisites: routine work with health data, basic Excel, commitment to deliver an in-country cascade training within 6 months</li>
        </ul>
      </div>
      <div class="info-card">
        <h3>✅ Deliverables</h3>
        <ul>
          <li>Daily group analysis outputs — tables, figures, draft report sections</li>
          <li>A complete country-team analysis presentation</li>
          <li>Country action plan for cascade training (due 30 Apr 2027)</li>
          <li>In-country 4-day cascade training for 10–15 staff (by Sep 2027)</li>
          <li>One peer-reviewed IMRAD country report (by Mar 2028)</li>
        </ul>
      </div>
    </div>
  </section>
  <section class="tight key-details">
    <h2>Key Details</h2>
    <div class="details-grid">
      <div class="detail-item"><h4>Dates</h4><p>Monday 22 – Friday 26 March 2027<br>(5 days)</p></div>
      <div class="detail-item"><h4>Location</h4><p>Kigali, Rwanda</p></div>
      <div class="detail-item"><h4>Format</h4><p>In-person TOT: practicals, group analysis project &amp; micro-teaching</p></div>
      <div class="detail-item"><h4>Working Language</h4><p>English<br><span style="font-size:0.85rem">(French support materials available)</span></p></div>
    </div>
  </section>
  <section class="tight cta-section">
    <h2>Get Started</h2>
    <div class="cta-buttons">
      <a class="btn btn-primary" href="agenda.html">View the Agenda</a>
      <a class="btn btn-secondary" href="guide.html">Facilitator Guide</a>
      <a class="btn btn-secondary" href="materials.html">Download Materials</a>
    </div>
  </section>
</div>"""
    (ROOT / "index.html").write_text(
        page("Home", "index.html",
             hero("Bloomberg Philanthropies · Data for Health Initiative",
                  "Data Analysis &amp; Report Writing TOT",
                  "A five-day Training of Trainers course that turns routine health data into rigorous analysis, clear communication, and equitable decisions."),
             index_body), encoding="utf-8")

    # ---- agenda ----
    agenda_body = f"""<div class="container">
  <div class="agenda-intro">
    <h2>Five days, from raw data to trainer-ready</h2>
    <p>Each day runs 9:00 AM – 5:00 PM with a working group analysis project threaded throughout. Sessions marked in orange are breaks.</p>
    <div class="note-banner" style="text-align:left"><strong>Note:</strong> Timings below are the facilitator's detailed run-of-show. All practicals use the synthetic Demoland datasets — no real patient data is used at any point.</div>
  </div>
  {build_agenda_days()}
</div>"""
    (ROOT / "agenda.html").write_text(
        page("Agenda", "agenda.html",
             page_header("Course Agenda", "22–26 March 2027 · Kigali, Rwanda — detailed run-of-show for all five days."),
             agenda_body), encoding="utf-8")

    # ---- guide ----
    guide_md = "\n\n".join(md_file(f"facilitator-guide/{f}") for f in
                            ["front-matter.md", "day-1.md", "day-2.md", "day-3.md", "day-4.md", "day-5.md", "annexes.md"])
    guide_body = f'<div class="container"><div class="prose">\n{md_to_html(guide_md)}\n</div></div>'
    (ROOT / "guide.html").write_text(
        page("Facilitator Guide", "guide.html",
             page_header("Facilitator Guide", "Session-by-session instructions, timings, trainer tips and annexes — 83 pages in print."),
             guide_body), encoding="utf-8")

    # ---- workbook ----
    wb_md = "\n\n".join(md_file(f"participant-workbook/{f}") for f in
                         ["introduction.md", "day-1.md", "day-2.md", "day-3.md", "day-4.md", "day-5.md", "reference.md"])
    wb_body = f'<div class="container"><div class="prose">\n{md_to_html(wb_md)}\n</div></div>'
    (ROOT / "workbook.html").write_text(
        page("Participant Workbook", "workbook.html",
             page_header("Participant Workbook", "Exercises, worksheets and reference sheets for all five days — 57 pages in print."),
             wb_body), encoding="utf-8")

    # ---- materials ----
    materials_body = f"""<div class="container">
  <div class="agenda-intro">
    <h2>Everything needed to run the course</h2>
    <p>All datasets are <strong>100% synthetic demo data</strong>, generated for training — clearly labeled and safe to share. Slide decks are ready to present; templates are ready to adapt.</p>
  </div>
  <div class="materials-section">
    <h2>Demo Datasets</h2>
    <div class="materials-category">
      <h3>📊 Excel workbooks (synthetic — for training only)</h3>
      <p>The Demoland TB register is the running dataset used across all five days; the census file provides denominators for rate calculations.</p>
      {file_list(DATASETS, "datasets", "XLSX")}
    </div>
  </div>
  <div class="materials-section">
    <h2>Session Slide Decks</h2>
    <div class="materials-category">
      <h3>📽️ PowerPoint decks with speaker notes (185 slides)</h3>
      <p>One deck per day, covering every official session.</p>
      {file_list(DECKS, "slides", "PPTX")}
    </div>
  </div>
  <div class="materials-section">
    <h2>Templates &amp; Instruments</h2>
    <div class="materials-category">
      <h3>📝 Ready-to-adapt originals</h3>
      <p>IMRAD report template, data dictionary, SOP, worksheets, tests and evaluation forms.</p>
      {file_list(TEMPLATES, "templates", None)}
    </div>
  </div>
</div>"""
    (ROOT / "materials.html").write_text(
        page("Materials", "materials.html",
             page_header("Course Materials", "Datasets, slide decks and templates — free to download and adapt."),
             materials_body), encoding="utf-8")

    print("site built:",
          [p.name for p in [ROOT/"index.html", ROOT/"agenda.html", ROOT/"guide.html",
                            ROOT/"workbook.html", ROOT/"materials.html", ROOT/"styles.css"] if p.exists()])

if __name__ == "__main__":
    build()
