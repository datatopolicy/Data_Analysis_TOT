# Day 3 — Wednesday 24 March

**Tables, Figures & Maps**

## 9:00–9:30 · Day 2 debrief

> **KEY POINTS** — Teams share one computed rate and one interpretation each — facilitators check that denominators match numerators.
> Recurring errors reviewed: rates computed from counts without population, sex not disaggregated, and pivot Values set to Count instead of Sum.
> Preview: today’s outputs (tables, figures, maps) become the Results section your team drafts tomorrow.


## 9:30–10:30 · IMRAD Structure

> **KEY POINTS** — IMRAD = Introduction, Methods, Results, and Discussion — the international standard skeleton for analytical reports. Readers know exactly where to look for each kind of information.
> Introduction: why this analysis was done — background, the policy problem, and the 3–5 analysis objectives. Ends where the data begins.
> Methods: what you did, in enough detail to reproduce — data sources (file names, periods, coverage), cleaning steps (cite your Cleaning_Log approach), how rates and statistics were calculated, and limitations (e.g. Riverside’s incomplete mortality registration).
> Results: what you found — text plus tables, figures, and maps. No interpretation here, just findings in logical order (national picture first, then disaggregated). Every table/figure is numbered, titled, and referenced in the text.
> Discussion: what it means — interpret findings, compare with expectations, acknowledge limitations, and lead into recommendations. This is where the equity lens speaks loudest.
> Front matter: a one-page executive summary (objectives, key findings, recommendations — written last) and a table of contents. Back matter: annexes with detailed tables and the data dictionary.
> Your team report (4–6 pages) will follow IMRAD exactly — assign each section an owner today.


## 11:00–12:00 · Best practices for creating tables

> **KEY POINTS** — One table, one message. If you need two messages, you need two tables.
> Every table needs: a number (Table 1, 2, 3…), a self-contained title stating what, where, and when (“TB notification rate per 100,000 by district, Demoland, 2025”), and units in the column headers — never buried in a footnote hunt.
> Numbers: right-align, use consistent decimal places (one decimal for rates, whole numbers for counts), and use thousands separators. Never show four decimals on a count of people.
> Structure: no vertical text, no merged header cells, minimal gridlines (header rule + bottom rule is enough), zebra shading only if it aids reading — never rainbow fills.
> Sort with intent: by magnitude (highest rate first) when ranking matters, chronologically for trends, alphabetically only when readers must find one row fast.
> Footnotes explain: definitions (e.g. “treatment success = cured + treatment completed”), data sources, and symbols. Denominators belong in the table or its notes — a percentage without its denominator is unverifiable.
> Design for the reader who photocopies in black and white: if the table only works in colour, it doesn’t work.


### Exercise 3.1: Rebuild three bad tables  (60 minutes)

**Purpose:** Diagnose real table-design flaws and rebuild each table to publication standard — the tables you fix here are prototypes for your team report’s Results section.

**Workbook:** DA-TOT_Exercise-Workbook_Day3.xlsx — read the README sheet first, then sheets Bad_Table_1, Bad_Table_2, Bad_Table_3; rebuild each on a new sheet named Table_1_Fixed, Table_2_Fixed, Table_3_Fixed; verify against Answer_Key.

**Steps**

1. **1. Open Bad_Table_1 without fixing anything yet.** List every flaw you can see against the “Best practices” rules above, then check your list against this one: the title is just “TB” — not self-contained (notifications or rates? which country? units?); there is no table number; whole-number counts are displayed with six decimal places; districts sit in arbitrary order; and there is no source note. (Ignore the red-on-yellow synthetic-data banner in row 1 — it is a file-level disclaimer, not part of the table.)
1. **2. Rebuild it as Table_1_Fixed:** add a table number and a self-contained title (what, where, when — e.g. “TB notifications by district, Demoland, 2021–2025”); show whole-number counts with no decimals, right-aligned; use a single horizontal header row; sort districts by 2025 notifications descending; add a source footnote naming the file and sheet.
1. **3. Diagnose Bad_Table_2.** Flaws to find: an unprofessional merged title (“fancy chart-style view”) in large red type; rainbow header fills that carry no meaning; values shown as proportions with up to 15 decimal places (0.870527…) instead of percentages; cryptic row labels “M”/“F”; no numerators or denominators anywhere; no definition of “treatment success”; no table number; a stray “Legend:” row; no source note.
1. **4. Rebuild it as Table_2_Fixed:** proper title and number; one-decimal percentages with the n/N beside each value; “Male”/“Female” row labels; a single-row header with no decorative fills; a footnote defining treatment success; a total row; a source note.
1. **5. Diagnose Bad_Table_3 (“Deaths by cause, 2025”).** Flaws to find: no table number and no place in the title (which country?); causes in arbitrary order instead of sorted by magnitude; deaths shown with four decimal places and no thousands separators; no share-of-total column; no source or coverage note.
1. **6. Rebuild it as Table_3_Fixed:** numbered, self-contained title including “Demoland”; causes sorted by descending deaths; whole numbers with thousands separators, right-aligned; an added “Share of all deaths (%)” column with one decimal; explicit headers; a source footnote.
1. **7. Apply the Table Critique Checklist (Worksheet 3A) to each rebuilt table.** Every box should be ticked before you move on.
1. **8. Compare with Answer_Key.** Note any flaw you missed and add it to your personal checklist for the team report.
**Expected output:** Three rebuilt tables (Table_1_Fixed, Table_2_Fixed, Table_3_Fixed), each with number, self-contained title, units, consistent formatting, sorted rows, and footnotes — all passing the Table Critique Checklist.

* **Reflection questions:** *

- Which single flaw, in your view, most misleads a busy decision-maker — and why?
- Bad_Table_2’s 15-decimal proportions are technically precise. Why does that precision make the table worse, not better?
## 14:00–15:00 · Best practices for creating figures

> **KEY POINTS** — Choose the chart for the message: trends over time → line chart; comparisons across districts → horizontal bar chart; composition of a whole → stacked bar (use pie only for 2–3 slices, never 3D); distribution → histogram.
> Bar and column charts must start the value axis at zero — truncating the axis exaggerates differences and is the commonest form of visual dishonesty.
> Write the takeaway in the title: “TB notifications fell nationally but rose in Westbrook, 2021–2025” beats “TB notifications by district”. A reader skimming titles should get the story.
> Label directly where possible (data labels on the line/bar ends) instead of forcing readers to bounce between legend and chart. Keep legends only when direct labelling clutters.
> Colour with restraint: one accent colour for the story’s focus (e.g. Westbrook’s line), grey for context; avoid red-green pairings (colour blindness); ensure the figure survives black-and-white printing.
> Declutter ruthlessly: remove gridlines or fade them, delete chartjunk (3D effects, shadows, background images), and put the data-ink ratio to work — every pixel should carry information.
> Every figure needs: a number (Figure 1, 2…), the takeaway title, axis labels with units, and a source note. Reference each figure in the results text (“Figure 2 shows…”).


### Exercise 3.2: Build correct charts and fix a misleading one (Tasks 1–4)  (60 minutes)

**Purpose:** Practise matching chart types to messages and repairing a dishonest visual — skills your team report’s figures depend on.

**Workbook:** DA-TOT_Exercise-Workbook_Day3.xlsx — read the README sheet first, then sheet Figure_Tasks (Data tables A, B, C and Tasks 1–4); build your charts on the same sheet or new sheets; verify against Answer_Key.

**Steps**

1. **1. Task 1 — trend.** Using Data table B (national TB notification rate per 100,000, 2021–2025), build the correct chart for a trend over time: a line chart with years on the horizontal axis, a labelled vertical axis (rate per 100,000), and a takeaway title stating what the trend actually shows.
1. **2. Task 2 — comparison.** Using Data table A (2025 TB notification rates for the 12 districts), build the correct comparison chart: a horizontal bar chart sorted by rate, value axis starting at zero, districts labelled directly, and a takeaway title naming the standout district.
1. **3. Task 3 — composition.** Using Data table C (deaths by cause, Demoland, 2025), build the correct composition chart: a single stacked bar (or a pie only if you can defend it for six causes) with each segment labelled by cause and share, plus a takeaway title. Never use 3D.
1. **4. Task 4 — fix the misleading chart.** Below the data tables sits a deliberately misleading line chart: it uses dual y-axes (TB rate per 100,000 on one side, treatment success on the other) and a truncated y-axis, and it plots treatment success as raw proportions (0.872) against a “%” label. First, list EVERYTHING that is wrong with it — axes, scales, units, titles, labels. Then rebuild it honestly: express treatment success as true percentages, give each measure its own properly scaled and labelled chart (or a single chart with one coherent measure), start bar axes at zero, add takeaway titles, axis labels with units, and a source note.
1. **5. Run the Figure Critique Checklist (Worksheet 3B) on every figure you built.** Fix any failures now.
1. **6. Compare with Answer_Key,** paying special attention to chart-type choices you got differently — discuss with your neighbour which choice communicates better and why.
**Expected output:** Three publication-standard figures (trend line, district comparison bars, cause-composition), a written list of every flaw in the misleading dual-axis chart, and an honestly rebuilt version — all passing the Figure Critique Checklist.

* **Reflection questions:** *

- Dual axes are sometimes defended as “space-saving”. What exactly makes them misleading here, and what is the honest alternative?
- Which misleads more: a bad chart, or a good chart of a bad (uncleaned, wrong-denominator) number?
## 16:00–17:00 · Creating maps in Excel

> **KEY POINTS** — Maps answer “where” at a glance: a district choropleth (areas shaded by value) makes geographic inequity instantly visible — Westbrook’s rise and Riverside’s gaps literally stand out.
> Excel’s Filled Map chart needs real geography data types, which do not exist for fictional Demoland — so the reliable method is a tile-grid map: 12 labelled cells arranged in a grid, coloured by value band with conditional formatting.
> Design rules carry over from figures: 3–5 colour bands (not 12 shades), a clear legend with the band ranges, district names on the tiles, a takeaway title, and a source note.
> Classify honestly: use equal-interval or quantile bands and state the method; never let default breaks hide the story or manufacture one. Always show the underlying rates table beside or beneath the map.
> Maps show pattern, not cause: a dark Westbrook invites investigation (transmission? better detection? migration?) — it does not diagnose.


### Exercise 3.3: Build a district choropleth-style map in Excel  (45 minutes)

**Purpose:** Produce a map-quality visual of district TB rates that a decision-maker can read in five seconds.

**Workbook:** DA-TOT_Exercise-Workbook_Day3.xlsx — read the README sheet first, then sheet Map_Task (it already contains the 2025 district rate table, build instructions for Option A/B, and a starter choropleth grid); verify against Answer_Key.

**Steps**

1. **1. Cross-check the provided rate table.** Map_Task lists each district’s 2025 TB notification rate per 100,000. Verify at least two values against your own Task 1 calculations from Day 2 — trust, but verify.
1. **2. Define 4 colour bands.** Choose equal-interval bands across the min–max range (or quartiles), write the band limits in a small legend table, and note the classification method beside it — the method is part of the figure’s honesty.
1. **3. Build the tile grid (Option B).** The sheet offers two routes: Option A, Excel’s Filled Map (note why it may fail — Demoland’s districts are fictional and have no geography data type), and Option B, the recommended conditional-formatting choropleth grid. Complete or rebuild the 12-tile starter grid so each tile shows its district name and is linked to that district’s rate (e.g. =VLOOKUP on the rate table), then apply 4 conditional-formatting rules mapping your bands to a single-hue light-to-dark progression. Place the legend beside the grid.
1. **4. Finish like a publication figure.** Add a takeaway title (e.g. a Figure number plus what the map shows: district TB notification rates per 100,000, Demoland, 2025 — or your sharper takeaway), a source note naming the files, and the band-classification method.
1. **5. Interpret in two sentences:** which district stands out, and what are two competing explanations for its shading? Record your answer on the sheet and check Answer_Key.
**Expected output:** A 12-tile conditional-formatting map with labelled districts, a 4-band legend with your computed breaks, a takeaway title, a source note, and a two-sentence interpretation.

* **Reflection questions:** *

- Why can a map persuade faster than a table — and what important information does the map hide that the table keeps?
- How would you adapt this tile-grid technique for your own country’s districts or provinces?

## Day 3 Worksheets

## Worksheet 3A: Table Critique Checklist

*Apply to every table before it enters your report. All boxes must be ticked.*

| **Check** | **Table 1** | **Table 2** | **Table 3** |
| --- | --- | --- | --- |
| Table number and self-contained title (what, where, when) | ☐ | ☐ | ☐ |
| Units stated in column headers | ☐ | ☐ | ☐ |
| Numbers right-aligned; consistent decimal places | ☐ | ☐ | ☐ |
| Counts as whole numbers; rates with one decimal | ☐ | ☐ | ☐ |
| No vertical text; no merged header cells | ☐ | ☐ | ☐ |
| Minimal gridlines; no decorative fills | ☐ | ☐ | ☐ |
| Rows sorted with intent (magnitude / time / lookup) | ☐ | ☐ | ☐ |
| Percentages shown with numerators and denominators | ☐ | ☐ | ☐ |
| Footnotes define terms, symbols, and abbreviations | ☐ | ☐ | ☐ |
| Source note names the file, sheet, and coverage | ☐ | ☐ | ☐ |
| Readable in black and white | ☐ | ☐ | ☐ |
| Referenced in the results text (“Table 1 shows…”) | ☐ | ☐ | ☐ |

## Worksheet 3B: Figure Critique Checklist

*Apply to every figure before it enters your report. All boxes must be ticked.*

| **Check** | **Figure 1** | **Figure 2** | **Figure 3** |
| --- | --- | --- | --- |
| Figure number and takeaway-message title | ☐ | ☐ | ☐ |
| Chart type matches the message (trend / comparison / composition) | ☐ | ☐ | ☐ |
| Bar/column value axis starts at zero | ☐ | ☐ | ☐ |
| Axes labelled with units | ☐ | ☐ | ☐ |
| Data labelled directly where possible; legend only if needed | ☐ | ☐ | ☐ |
| No chartjunk (3D, shadows, backgrounds) | ☐ | ☐ | ☐ |
| Colour restrained; focus colour on the story; colour-blind safe | ☐ | ☐ | ☐ |
| Source note present | ☐ | ☐ | ☐ |
| Figure works in black and white | ☐ | ☐ | ☐ |
| Referenced in the results text (“Figure 1 shows…”) | ☐ | ☐ | ☐ |

## Day 3 Daily Reflection

*Five minutes before you leave.*

**The table or figure I am proudest of today …**

**A design habit I need to unlearn (e.g. default Excel styling) …**

**How today’s visuals change my team’s Results section …**

**One question about IMRAD I want answered tomorrow …**

> **DAY KEY TAKEAWAYS** — IMRAD (Introduction, Methods, Results, Discussion) is the skeleton of your team report — plus an executive summary written last and annexes for detail.
> One table, one message: numbered, self-contained title (what/where/when), units in headers, right-aligned numbers, consistent decimals, sorted rows, footnotes, source note.
> Percentages without visible denominators are unverifiable — always show n/N.
> Match chart to message (line = trend, bar = comparison, stacked bar = composition); bar axes start at zero; titles state the takeaway, not the topic.
> Declutter every figure: no 3D, no chartjunk, restrained colour, direct labels, black-and-white safe.
> Tile-grid maps with conditional formatting give Excel a publication-quality district map without geography data types — always pair the map with its data table.
> Run both critique checklists on every table and figure before it enters the report.


## Notes

*Use this space for your own notes, questions for the facilitators, and ideas to take home.*
