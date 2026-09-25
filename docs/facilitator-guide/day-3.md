# Day 3 — Wednesday 24 March 2027: Communicating Findings

*Theme: analysis is only half the job — findings must be structured (IMRAD), tabulated, visualized, and mapped so honestly that a busy policymaker cannot misunderstand them. Teams leave today with draft tables, figures, and an IMRAD outline.*

## Day 3 (Wed 24 Mar)  |  9:00–9:30

### Day 2 debrief

### Learning objectives

1. Resolve Day 2's unclear items.
1. Confirm every team has verified rates and pivots.
1. Preview Day 3's communication outputs.
### Key content and talking points

1. Re-teach top unclear items from Day 2 forms — typically pivot-table field placement and STDEV.S vs STDEV.P. Fresh 5-minute demos each.
1. Team stand-ups (60 seconds): rates done? pivots done? Any team still without sex-stratified rates gets facilitator help in the first team block today.
1. Preview: 'Today your numbers become a story — structure, tables, figures, maps.'
### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 9:00–9:12 | 12 | Re-teach unclear items with fresh demos. |
| 9:12–9:22 | 10 | Team stand-ups + unblocking. |
| 9:22–9:30 | 8 | Day 3 preview; Q&A. |

### Materials needed

- Tallied Day 2 evaluation forms
### Facilitator notes — pitfalls, pacing, contingencies

- **If any team lacks verified rates,** assign the co-facilitator to them during the first exercise block — do not let it slide another day.
> **TRAINER TIP** — Same debrief ritual as yesterday. Consistency is the point: trainees learn that feedback loops are daily, not end-of-course.


## Day 3 (Wed 24 Mar)  |  9:30–10:30

### IMRAD Structure

### Learning objectives

1. State the purpose of each IMRAD section.
1. Sort content correctly across the four sections (border policy).
1. Explain why Methods must be reproducible.
1. Draft an IMRAD outline for the team project.
### Key content and talking points

IMRAD — Introduction, Methods, Results, and Discussion — is the international standard skeleton of a technical report. Teach it as four rooms, each with one job and a strict border policy:

| **Section** | **Purpose — answers...** | **Contains** | **Never contains** |
| --- | --- | --- | --- |
| Introduction | Why does this analysis matter? | Background, policy context, and the analysis objectives. Ends with the objectives verbatim. | Results or methods detail. |
| Methods | What did you do, exactly? | Data sources (Demoland files, years), cleaning steps (the cleaning log!), indicator definitions and formulas, denominators, stratifications, software (Excel version), limitations of the data. | Any finding — no numbers that belong in Results. |
| Results | What did you find? | Text + tables + figures, ordered by the objectives. Every table/figure is introduced in text and has a takeaway sentence. No interpretation beyond describing. | Interpretation, recommendations, or new data. |
| (and) Discussion | What does it mean, and what should we do? | Interpretation of key findings, comparison with expectations, equity implications (who is left behind?), limitations, and recommendations. | New results that were never shown in Results. |

- **The border policy is the lesson:** results in Methods confuse; new data in Discussion destroys credibility. Reviewers check the borders first.
- **Methods must be reproducible:** a competent analyst reading only the Methods should be able to rebuild the analysis — that is why Monday's cleaning log and the exact rate formulas live here.
- **The Discussion earns its keep with two moves:** 'so what?' (interpretation for policy) and 'what now?' (recommendations). Thursday's sessions deepen both.
- **Abstract/executive summary comes last in writing,** first in reading — one paragraph per IMRAD section, written after the body is final.
Exercise (last 20 min): teams take yesterday's rate findings and sort pre-written finding/method/interpretation strips into the four IMRAD rooms on flipchart — fast, physical, and it exposes border violations instantly.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 9:30–9:50 | 20 | Mini-lecture: the four rooms + border policy; the table above as handout. |
| 9:50–10:10 | 20 | Sorting exercise: strips → four flipchart rooms; facilitators circulate. |
| 10:10–10:30 | 20 | Plenary: border violations found and fixed; teams draft their project's IMRAD outline (headings + 1 line each). |

### Materials needed

- Slides: IMRAD-Structure.pptx
- Sorting strips (prepared)
- Flipcharts (4)
- Workbook: IMRAD outline template
### Facilitator notes — pitfalls, pacing, contingencies

- **The sorting exercise is the session —** do not let the lecture eat it. Border violations discovered by hand stick forever.
- **Common confusion:** participants put recommendations in Results. Catch it in the exercise; it foreshadows Thursday.
- **Collect the IMRAD outlines at tea —** skim them during the break so afternoon feedback is specific.
> **TRAINER TIP** — Teach IMRAD with the 'four rooms' metaphor and the physical sorting exercise — it works even with low-literacy audiences and needs no technology. In cascade trainings, make trainees sort their own draft sentences; self-found border violations are never repeated.


## Day 3 (Wed 24 Mar)  |  10:30–11:00

### Tea

> **TRAINER TIP** — Skim the IMRAD outlines collected at 10:30. Note the two weakest for targeted coaching in the tables exercise.


## Day 3 (Wed 24 Mar)  |  11:00–12:00

### Best practices for creating tables

### Learning objectives

1. State the 10 table best-practice rules.
1. Write a self-contained table title with units.
1. Rebuild a default Excel output into a publication-quality table.
### Key content and talking points

Tables carry precise values; figures carry patterns. A table's job is to let a reader find any number in seconds and trust all of them. Teach the rules as a checklist — participants will apply it within the hour:

1. Title above the table, self-contained: 'Table 1. TB case notification rate per 100,000 population by district, Demoland, 2024.' A reader should understand it without the text.
1. One idea per table. If it needs two titles, it needs two tables.
1. Columns: variables across the top, categories down the rows; order rows meaningfully (highest to lowest rate, or chronological) — never alphabetical by default.
1. Units in the title or column header ('per 100,000'), never buried in a footnote the reader must hunt for.
1. Align numbers right (or on the decimal point); align text left. Same decimals throughout a column (e.g., 80.4, 112.0 — never 80.43 next to 112).
1. No vertical gridlines; minimal horizontal lines (top, under header, bottom). In Excel: strip the default gridlines, add borders only where the rule requires.
1. Totals where they aid interpretation — and label whether a total row is a sum or a weighted rate (a 'total' of rates is meaningless; show the national rate computed from national totals).
1. Footnotes for: data source, definitions, missing data (e.g., 'Riverside mortality data incomplete — see Methods'), and any suppression of small numbers.
1. Round sensibly: rates to 1 decimal, percentages to whole numbers in text. False precision (4 decimals) signals innumeracy, not rigor.
1. In Excel: build the table as values (Paste Special → Values) once calculations are final, so sorting and formatting cannot break formulas; keep the formula version on a separate 'working' sheet.
Demonstrate live: take an ugly default Excel dump of district rates and rebuild it rule by rule on the projector — participants audibly react when the same numbers become twice as readable. Before/after is the pedagogy.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 11:00–11:20 | 20 | Mini-lecture: the 10 rules with before/after examples in slides. |
| 11:20–11:40 | 20 | Live rebuild demo: ugly district-rate dump → clean Table 1, narrating each rule applied. |
| 11:40–12:00 | 20 | Q&A + teams pull up their own rate tables and self-score against the checklist (no rebuilding yet — that is next). |

### Materials needed

- Slides: Tables-Best-Practice.pptx
- Workbook: table checklist (1 page)
- District-rate tables from Day 2
### Facilitator notes — pitfalls, pacing, contingencies

- **The live rebuild is non-negotiable —** rules without the demo feel abstract; the demo makes them obvious.
- **Emphasize rule 10 (values vs. formulas)** before the exercise hour — it prevents the afternoon's most common catastrophe.
- **Keep 5 minutes spare:** the next session starts building immediately.
> **TRAINER TIP** — The before/after rebuild is your most reusable teaching asset: record your screen while doing it once, and you have a 10-minute video for cascade trainings and for analysts who missed the session. The 1-page checklist becomes a permanent desk reference — print it on card stock.


## Day 3 (Wed 24 Mar)  |  12:00–13:00

### Tables exercise

### Learning objectives

1. Apply the 10 table rules to real project outputs.
1. Critique a peer table constructively against the checklist.
1. Produce two draft publication-quality tables for the team report.
### Key content and talking points

Teams rebuild two tables for their Friday deck from their own Day 2 outputs, applying all 10 rules: (1) the district-rate table (their 'Table 1'), and (2) a second table of their choice (e.g., sex/age stratification or yearly trend). Facilitators circulate with the checklist, scoring each table against the 10 rules and giving one correction at a time.

Mid-exercise (12:30): 5-minute plenary pause — show one team's in-progress table anonymously on the projector and let the room apply the checklist aloud. Peer critique in plenary teaches faster than facilitator correction at tables.

Deliverable by 13:00: two titled, formatted tables pasted into the team's draft slide deck, plus the checklist self-score.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 12:00–12:30 | 30 | Team build: two tables per team; facilitators circulate with checklists. |
| 12:30–12:35 | 5 | Plenary peer critique of one in-progress table. |
| 12:35–12:55 | 20 | Continue building; finalize titles, footnotes, rounding. |
| 12:55–13:00 | 5 | Deliverable check: tables in draft deck; self-scores recorded. |

### Materials needed

- Table checklist (1 page per participant)
- Draft slide decks
- Projector for peer critique
### Facilitator notes — pitfalls, pacing, contingencies

- **One correction at a time —** listing all 10 violations crushes morale; fix the title first, then alignment, then the rest.
- **Watch for alphabetical district ordering —** the commonest leftover default; ask 'what story does this order tell?'
- **If a team has no rates yet (behind from Day 2),** the co-facilitator sits with them for 15 minutes while the lead covers the room — escalate, don't abandon.
> **TRAINER TIP** — Peer critique of one anonymous table in plenary is the highest-leverage 15 minutes of a cascade training: everyone learns the checklist by applying it, and the presenting team gets 24 editors for free. Always ask permission before projecting a team's work.


## Day 3 (Wed 24 Mar)  |  13:00–14:00

### Lunch

> **TRAINER TIP** — Review the two weakest IMRAD outlines over lunch; prepare one targeted question for each team for the afternoon.


## Day 3 (Wed 24 Mar)  |  14:00–15:00

### Best practices for creating figures

### Learning objectives

1. Match chart type to the message using the message→chart table.
1. Write takeaway titles and honest axes (zero baseline for bars).
1. Apply decluttering and color-blind-safe design in Excel.
1. State the accessibility requirements for figures.
### Key content and talking points

Figures show patterns; tables show values. Choose the chart from the message, not from habit:

| **Message** | **Chart type** | **Rule** |
| --- | --- | --- |
| Trend over time | Line chart | One line per group max 3–4; label lines directly (no legend hunt); y-axis labeled with units |
| Compare categories | Bar chart (or column) | Y-axis starts at ZERO — truncated bars lie about differences; order bars meaningfully |
| Part of a whole | Bar chart (avoid pie) | Pies fail beyond 2–3 slices; a sorted bar shows the ~60–65% male share more honestly |
| Distribution/shape | Histogram | Bin sensibly; label axes; never a 3D effect |
| Two variables' relationship | Scatter plot | No connecting lines unless time-ordered |

1. Title as takeaway: 'Figure 1. TB notification rates declined nationally but rose in Westbrook, Demoland, 2021–2025.' The title states the finding; the subtitle or footnote carries the method detail.
1. Zero baseline for bars; labeled, unbroken axes for lines. Truncation is the commonest visual lie — demonstrate with Westbrook vs. national bars at y=0 vs. y=50 and let the room feel the deception.
1. Direct labeling beats legends; data labels only where they add information (endpoints of lines, not every bar).
1. Color with purpose: one accent color for the finding (Westbrook's line), grey for context; color-blind-safe palettes (blue/orange, not red/green); every figure must survive black-and-white printing.
1. Declutter: remove gridlines or fade them, kill 3D effects, no chart junk. In Excel: Chart Design → Add Chart Element sparingly; set gridlines to light grey or none.
1. Source footnote on every figure: 'Source: Demoland synthetic TB notifications, 2021–2025.'
1. Excel mechanics: select the data → Insert → chart type; right-click axis → Format Axis to set bounds (force 0 for bars); Chart Title → type the takeaway; use Paste Special → Picture into slides so the figure cannot shift.
Accessibility is non-negotiable: sufficient color contrast, never color as the only encoding (add labels or patterns), minimum 10pt axis text. A figure a policymaker cannot read is a finding that does not exist.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 14:00–14:20 | 20 | Mini-lecture: message→chart table; the 7 rules. |
| 14:20–14:35 | 15 | Live demo: build the Westbrook-vs-national trend line (takeaway title, direct labels, grey context) + the truncated-bar deception demo. |
| 14:35–14:55 | 20 | Spot-the-violation: 6 flawed charts on slides; tables call out violations rapid-fire. |
| 14:55–15:00 | 5 | Q&A; preview of the figures exercise. |

### Materials needed

- Slides: Figures-Best-Practice.pptx (incl. 6 flawed charts)
- Workbook: figure checklist (1 page)
### Facilitator notes — pitfalls, pacing, contingencies

- **The truncated-bar demo** produces the week's biggest gasp — do not skip it. It inoculates against the commonest visual lie.
- **Limit the demo to two charts;** the exercise hour is for building, not watching.
- **Remind: values read live from files —** describe the Westbrook rise qualitatively; never quote numbers from memory.
> **TRAINER TIP** — The 'spot-the-violation' rapid-fire game ports directly to cascade trainings and needs no computers — collect bad charts from real national reports (anonymized) and your trainees will never make those mistakes. Keep the truncated-bar demo; it converts skeptics instantly.


## Day 3 (Wed 24 Mar)  |  15:00–16:00

### Figures exercise

### Learning objectives

1. Build two project figures that pass the figure checklist.
1. Critique peer figures for honesty and clarity.
1. Draft takeaway sentences linking each figure to Results text.
### Key content and talking points

Teams build two figures for Friday from their own outputs: (1) a trend figure (e.g., national vs. Westbrook TB notifications 2021–2025, or their topic's core trend), and (2) a comparison figure (e.g., district rate bar chart or sex-distribution bars). Both must pass the figure checklist: takeaway title, honest axes, direct labels, color-blind-safe, source footnote.

Same pedagogy as the tables hour: circulate with the checklist, one correction at a time; mid-exercise plenary peer critique of one anonymous figure (15:30). Deliverable by 16:00: two figures pasted as pictures into the draft deck.

Stretch for fast teams: draft the one-sentence Results-text takeaway that will accompany each figure ('Figure 1 shows...').

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 15:00–15:30 | 30 | Team build; facilitators circulate with checklists. |
| 15:30–15:35 | 5 | Plenary peer critique of one anonymous figure. |
| 15:35–15:55 | 20 | Finish figures; paste as pictures into deck; draft takeaway sentences. |
| 15:55–16:00 | 5 | Deliverable check. |

### Materials needed

- Figure checklist (1 page)
- Draft decks
- Projector
### Facilitator notes — pitfalls, pacing, contingencies

- **Pasting as pictures** prevents the #1 slide-deck catastrophe: linked charts that reflow or vanish on another laptop. Insist on it.
- **Watch axis bounds obsessively this hour —** one truncated bar chart in Friday's presentations undermines the week's credibility.
- **Slow teams:** one excellent figure beats two mediocre ones; grant permission to drop the second.
> **TRAINER TIP** — Insist on 'paste as picture' in cascade trainings too — it is a 10-second habit that prevents the most embarrassing presentation failures. And keep the rule: no figure enters a deck without its takeaway sentence written first.


## Day 3 (Wed 24 Mar)  |  16:00–17:00

### Creating maps in Excel

### Learning objectives

1. Build a Filled Map chart from a district-rate table.
1. Build an offline choropleth-style grid using conditional formatting.
1. Apply map honesty rules (rates not counts, sequential scale, legend, source).
1. Annotate data-quality caveats (Riverside) on maps.
### Key content and talking points

Maps answer 'where?' — and for district-level health data, 'where' drives resource allocation. Two Excel routes, taught in order:

### Route 1 — Filled Map chart (Excel 2019 / Microsoft 365)

1. Prepare a two-column table: district name | value (e.g., TB notification rate per 100,000, 2024). Names must match Bing's geography recognition — verify each district resolves.
1. Select the table → Insert → Charts → Maps → Filled Map.
1. Right-click the map → Format Data Series → Map projection and color scale: choose a sequential single-hue scale (light→dark blue), never rainbow; set the scale to the data range.
1. Add a takeaway title ('Figure 3. TB burden concentrates in western districts, Demoland, 2024'), a legend with units, and the source footnote.
1. Caveat: Filled Map needs internet (Bing geocoding) and only knows real geographies — Demoland's fictional districts may not resolve, in which case use Route 2. Test this before the course!
### Route 2 — Choropleth-style grid with conditional formatting (works everywhere, offline)

1. Arrange district names in a rough geographic grid on a worksheet (provide the template grid in the workbook — facilitator pre-arranges the 12 districts approximately).
1. Enter each district's rate in its cell; select the grid → Home → Conditional Formatting → Color Scales (3-color, light→dark blue).
1. Format cells large, centered, with district name above the value (use Alt+Enter line breaks).
1. Screenshot/paste as picture into the deck with title, legend ('darker = higher rate per 100,000'), and source footnote.
- **Map honesty rules:** same rules as figures — sequential color scale, no rainbow, legend with units, and never map raw counts when rates are the question (big pale districts mislead).
- **Equity use:** a district map of TB rates makes geographic inequity instantly visible to non-technical leaders — it is often the slide that moves a budget.
- **Riverside caution:** do not map mortality rates for Riverside without a visual 'data incomplete' annotation — mapping under-registered deaths as low mortality is exactly how bad maps kill good policy.
### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 16:00–16:20 | 20 | Demo: Route 1 Filled Map on district rates; show the geocoding check. |
| 16:20–16:35 | 15 | Demo + practice: Route 2 conditional-formatting grid using the template. |
| 16:35–16:55 | 20 | Team build: each team produces its map figure for the deck. |
| 16:55–17:00 | 5 | Close: maps pasted into decks; evaluation forms; preview Thursday (templates + recommendations). |

### Materials needed

- District-rate tables
- Workbook: 12-district map grid template
- Slides: Maps-in-Excel.pptx
- Evaluation forms (Day 3)
### Facilitator notes — pitfalls, pacing, contingencies

- **TEST Filled Map with Demoland names before the course.** Fictional districts often fail Bing geocoding — know in advance whether you are teaching Route 1, Route 2, or both, and say so upfront.
- **Internet dependence:** if venue Wi-Fi is unreliable, teach Route 2 as primary without apology — it works offline forever.
- **End-of-day energy is low;** keep demos snappy and get teams building within 20 minutes.
> **TRAINER TIP** — In countries with real district shapefiles, graduate trainees to QGIS later — but teach the Excel grid-map first. An analyst who can make an honest map in Excel this week will make an honest map in GIS next quarter; the honesty rules transfer, the software doesn't teach them.

