# Day 2 — Tuesday 23 March

**Rates, Descriptive Statistics & Pivot Tables**

## 9:00–9:30 · Day 1 debrief

> **KEY POINTS**— Teams share one analysis objective each for facilitator feedback — clarity and measurability are the tests.
> Common Day 1 pitfalls reviewed: objectives without a time period, objectives nobody would act on, and “CHECK” values left unresolved in the XLOOKUP exercise.
> Questions from yesterday’s reflection sheets answered before new material begins.


## 9:30–10:30 · Training Methodologies

> **KEY POINTS**— Adults learn differently: they need relevance (“why does this matter for my job?”), respect for their experience, and practice — not lectures. Every session you later deliver should be at least one-third hands-on.
> The TOT cascade: you learn it here → you teach it at home → your trainees teach others. Fidelity matters: use the same exercises, checklists, and answer keys so quality survives each cascade level.
> Facilitation beats presentation. Ask before you tell: “What would distort this chart?” produces deeper learning than listing chart rules. Use think-pair-share, live demos with mistakes left in, and frequent micro-exercises.
> Plan backwards from objectives: write the learning objectives first, then choose activities that produce them, then list materials. Worksheet 2A gives you the template — you will use it again on Day 5 for your country training plan.
> Manage energy deliberately: alternate input and activity every 20–30 minutes, use energizers after lunch, and never let one voice dominate — structured turn-taking (e.g. round-robins) protects quieter participants.


## 11:00–12:00 · Accessing and using census data to calculate rates in Excel

> **KEY POINTS**— Counts vs rates: a district with 500 TB notifications is not necessarily worse off than one with 200 — it may simply have more people. Rates divide by the population at risk so places become comparable.
> The rate formula: Rate = (Number of events ÷ Population at risk) × Multiplier. For TB notifications the standard multiplier is 100,000: “TB notification rate per 100,000 population”.
> Match numerator to denominator exactly: same place, same period, same sex and age breakdown. A 2025 district rate needs the district’s 2025 population — not the national total, not last year’s figure.
> Census files give you denominators: the Population sheet of DA-TOT_Demo_Census-Population.xlsx holds population by district × sex × year (2021–2025); Age_Structure gives age-group shares for age-specific rates.
> Small populations produce jumpy rates: a single extra case in a tiny district swings the rate wildly — flag uncertainty rather than ranking small districts precisely.
> Rates reveal what counts hide: compute Demoland’s district rates and the Westbrook story becomes sharper — is its rise just population growth, or a true increase in risk?


### Exercise 2.1: Calculate TB notification rates per 100,000 (Tasks 1–5)  (60 minutes)

**Purpose:**Turn raw TB notification counts into comparable district, sex, and yearly rates using census denominators — the core analytical move of the week.

**Workbook:**DA-TOT_Exercise-Workbook_Day2.xlsx — start with the README sheet; data are in TB_Data (district × year × sex, 120 rows) and Census_Data; complete Tasks 1–5 on the Tasks sheet; check yourself afterwards in Answer_Key.

**Steps**

1.**1. Read the README sheet end-to-end.**Note the learning objectives and the instruction to build formulas that reference TB_Data and Census_Data — never type values by hand. Do not peek at Answer_Key until you have attempted every task.
1.**2. Inspect TB_Data and Census_Data.**Confirm the shared keys: District, Year, Sex. TB_Data holds TB_Cases_Notified (and Treatment_Success counts for later); Census_Data holds the matching populations.
1.**3. Task 1 — district rates, 2025.**For each of the 12 districts compute =SUMIFS(TB_Data cases, district, 2025) ÷ SUMIFS(Census_Data population, district, 2025) × 100000. Format with one decimal place.
1.**4. Task 2 — rates by sex, 2025.**Same formula with a Sex criterion (Male, then Female). Compare the two: does the male rate exceed the female rate, consistent with the documented higher male burden?
1.**5. Task 3 — national trend, 2021–2025.**SUMIFS on the Year column only (all districts, both sexes) for each year, divided by the matching national population. Describe the trend in one sentence on the Tasks sheet.
1.**6. Task 4 — highest district, 2025.**Use MAX on your Task 1 rates and return the district name (INDEX/MATCH). Record it.
1.**7. Task 5 — the rising district.**For each district compute percent change = (2025 rate − 2021 rate) ÷ 2021 rate. One district rises while all others fall — name it, and write two sentences on whether its rising case counts reflect a rising rate or just population change.
1.**8. Check against Answer_Key.**For every mismatch, find the cause (wrong denominator year? counts instead of rates? sex not disaggregated?) and correct your method, not just the number.
**Expected output:**Tasks 1–5 completed: 2025 district rates, 2025 sex-specific rates, national yearly rates with a one-sentence trend description, the highest-rate district in 2025, and the identified rising district with a two-sentence verdict.

***Reflection questions:***

- For which policy question would raw counts be more useful than rates — and for which are rates essential?
- A district health officer asks why her district’s rate fell while its case count stayed flat. How do you explain it?
- Riverside’s mortality registration is visibly incomplete. What does that imply for any mortality rate you calculate there?
## 12:00–13:00 · Descriptive statistics review

> **KEY POINTS**— Central tendency: the mean (average) uses every value but is dragged by outliers; the median (middle value) resists outliers; the mode (most common) suits categories. Report the median alongside the mean whenever data are skewed.
> Spread matters as much as centre: range (max−min) is quick but fragile; the standard deviation (SD) measures typical distance from the mean; percentiles (e.g. the 25th and 75th) show where the bulk of values sit.
> Shape: in right-skewed data (a few very high districts) the mean exceeds the median — a signal to investigate the high outliers rather than report the mean alone.
> Choose deliberately: summarize symmetric data with mean ± SD; skewed data with median and interquartile range; categorical data with counts and percentages (always with denominators).
> Descriptive statistics describe — they do not explain. “Westbrook’s rate is the highest” is a description; “why” needs further analysis.


## 14:00–15:00 · Descriptive statistics using Excel

> **KEY POINTS**— Excel’s core functions: AVERAGE, MEDIAN, MODE.SNGL, STDEV.S (sample) vs STDEV.P (full population), MIN, MAX, QUARTILE.INC, PERCENTILE.INC, COUNT.
> Guard against text-that-looks-like-numbers and blanks: AVERAGE ignores blanks and text, which silently changes your n — check COUNT alongside every average.
> Use absolute references ($A$1) when a denominator or multiplier is reused across rows; use structured, labeled formula columns so a colleague can audit your logic.
> Document assumptions next to results (e.g. “SD computed with STDEV.S; n=12 districts”) — a number without its method is not reproducible.


### Exercise 2.2: Summarize district TB rates with descriptive statistics (Tasks 6–8)  (45 minutes)

**Purpose:**Practise choosing and computing the right summary statistics for a real-style indicator, and interpreting what skew tells you about equity.

**Workbook:**DA-TOT_Exercise-Workbook_Day2.xlsx — use your Task 1 district rates; complete Tasks 6–8 on the Tasks sheet; verify in Answer_Key.

**Steps**

1.**1. Take the 12 district TB notification rates for 2025 from Task 1.**These 12 values are your dataset (n=12).
1.**2. Task 6 — mean district rate.**Compute =AVERAGE over your 12 district rates in a labelled cell.
1.**3. Task 7 — median and standard deviation.**Compute =MEDIAN and =STDEV.S over the same 12 rates, each in a labelled cell with a note of the function used.
1.**4. Compare mean and median.**Which is larger? What does the gap tell you about the shape of district rates — and which single district is pulling the mean upward? Write one sentence of interpretation on the Tasks sheet.
1.**5. Task 8 — male-to-female rate ratio, 2025.**Divide your Task 2 male rate by the female rate. A ratio above 1 confirms the documented higher male burden — express it in words (e.g. “the male rate is about X times the female rate”).
1.**6. Spread check (stretch).**Compute the range (=MAX−MIN) and the 25th/75th percentiles (=QUARTILE.INC) of the 12 district rates. Has the spread across districts widened or narrowed since 2021? (Compute the 2021 equivalents to find out.)
1.**7. Check Answer_Key,**then write a three-line “statistical summary” paragraph as it might appear in a report’s Results section — centre, spread, and one equity-relevant observation.
**Expected output:**Tasks 6–8 completed: mean, median, and SD of the 12 district rates for 2025, the male-to-female rate ratio, plus a three-line results paragraph written in report language.

***Reflection questions:***

- Why is reporting only the national mean rate potentially misleading for equity?
- A journalist asks for “the average TB rate”. What do you give them, and what do you add?
## 15:00–16:00 · Data analysis using pivot tables

> **KEY POINTS**— A pivot table is a drag-and-drop summary engine: rows, columns, values, and filters replace dozens of SUMIFS formulas — and rebuild instantly when the question changes.
> Workflow: clean data first (Day 1), then Insert → PivotTable → drag fields. Put categorical fields (district, year, sex) in Rows/Columns and numeric fields in Values (as Sum, Average, or Count — check the aggregation, Excel often defaults to Count).
> Slicers add one-click filtering by year or sex — ideal for live exploration and for presentations.
> Pivot tables don’t calculate rates across rows automatically: compute rates from pivot outputs (or add a calculated field), keeping numerator and denominator visible.
> Refresh discipline: pivot tables snapshot the data — right-click → Refresh after any data change, and rebuild before finalizing a report.


### Exercise 2.3: Explore TB data with pivot tables (Tasks 9–10)  (45 minutes)

**Purpose:**Answer policy questions in minutes by pivoting the TB dataset — and confirm the headline patterns in the demo data yourself.

**Workbook:**DA-TOT_Exercise-Workbook_Day2.xlsx — sheets TB_Data and Census_Data; complete Tasks 9–10 on the Tasks sheet; verify in Answer_Key.

**Steps**

1.**1. Task 9 — pivot district trends.**Insert → PivotTable from TB_Data: Rows = District, Columns = Year, Values = Sum of TB_Cases_Notified. (Check the aggregation is Sum, not Count.) Sort 2025 descending, add a Year slicer, and confirm the rising district you identified in Task 5.
1.**2. Pivot the sex burden (stretch).**Rows = Sex, Columns = Year, Values = Sum of TB_Cases_Notified. Compute the 2025 male share (male ÷ total) and compare with the documented roughly 60–65% pattern.
1.**3. Task 10 — treatment success rate by district, 2025.**Values = Sum of Treatment_Success and Sum of TB_Cases_Notified; beside the pivot add =successes/notified formatted as % with one decimal. Also compute the national rate. Which districts lag, and what equity question does that raise?
1.**4. Turn the Task 9 pivot into rates.**Copy its values beside it, attach each district-year population from Census_Data (SUMIFS or XLOOKUP), and compute rates per 100,000. Confirm your Tasks 1–5 results match — two methods, one answer.
1.**5. Record all findings on the Tasks sheet,**then verify against Answer_Key and note any pivot-aggregation mistakes (e.g. Count instead of Sum) you caught.
**Expected output:**Tasks 9–10 completed: a district × year pivot of TB cases (with slicer), treatment success rates by district and nationally for 2025, and a rates cross-check matching Tasks 1–5.

***Reflection questions:***

- What can a pivot table answer in two minutes that would take twenty with formulas — and what can it not do?
- Why must you still check whether Excel summed or counted your Values field?
## 16:00–17:00 · Teams analyze data

Team time. Deliverable: core results for your team’s objectives — district/year/sex rates, key descriptive statistics, and answers to your policy questions, all computed from the demo files and ready to become tables tomorrow.

## Day 2 Worksheets

## Worksheet 2A: Training Session Planning Template

*Use this template for every session you will deliver back home. The first row shows a completed example — a 60-minute “Cleaning data in Excel” session — then plan your own session in the blank rows.*

|**Element**|**Completed example**|**Your session plan**|
| --- | --- | --- |
| Session title & duration | Cleaning data in Excel — 60 minutes |  |
| Learning objectives (by the end, participants will be able to…) | 1) Name 6 common data-quality issues; 2) clean a messy extract using filters, TRIM, and Remove Duplicates; 3) document fixes in a cleaning log. |  |
| Content outline (timed) | 0–10 min: why cleaning matters (war story); 10–20: demo of 3 fixes; 20–50: guided exercise in pairs; 50–60: debrief + log review. |  |
| Methods / activities (adult learning) | Think-pair-share on “worst dataset you’ve met”; live demo with deliberate mistakes; paired hands-on exercise; gallery walk of cleaning logs. |  |
| Materials needed | Laptop per pair; DA-TOT_Exercise_Messy-DHIS2-Extract.xlsx; printed Cleaning_Log template; projector. |  |
| How you will assess learning | Exit ticket: each pair submits its Cleaning_Log with ≥12 documented fixes; facilitator spot-checks two logs per table. |  |
| Equity & inclusion notes | Pair stronger/weaker Excel users; invite quieter participants to demo one fix; use local district names in examples. |  |

## Day 2 Daily Reflection

*Five minutes before you leave.*

**One rate I calculated today that changed how I see the data …**

**A statistic I now understand better than yesterday …**

**Something about pivot tables I want to practise more …**

**Status of my team’s core results (what’s done, what’s stuck) …**

> **DAY KEY TAKEAWAYS**— Always compare with rates, not raw counts — Rate = (Events ÷ Population at risk) × 100,000, with numerator and denominator matched on place, period, sex, and age.
> Attach denominators with XLOOKUP on a composite key; a wrong year’s population silently corrupts every rate.
> Summarize with the right statistic: mean ± SD for symmetric data, median + interquartile range for skewed data, counts + denominators for categories.
> When mean and median disagree, investigate the outliers — the gap itself is often the equity story.
> Pivot tables answer new questions in minutes: check the Values aggregation (Sum vs Count), refresh after data changes, and compute rates from pivot outputs.
> Small populations make jumpy rates — flag uncertainty instead of over-ranking small districts.
> Incomplete registration (as in Riverside) corrupts mortality rates: name the limitation in the report, don’t bury it.


## Notes

*Use this space for your own notes, questions for the facilitators, and ideas to take home.*
