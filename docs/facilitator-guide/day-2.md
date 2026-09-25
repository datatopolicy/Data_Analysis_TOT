# Day 2 — Tuesday 23 March 2027: Rates, Descriptive Statistics, and How to Teach

*Theme: from counts to meaning — rates with real denominators, honest summaries of distributions, and pivot tables as the analyst's engine. Plus the first training-methodologies session, because these participants are trainers from today onward.*

## Day 2 (Tue 23 Mar)  |  9:00–9:30

### Day 1 debrief

### Learning objectives

1. Resolve the previous day's unclear items surfaced by evaluations.
1. Report team project status and unblock shared problems.
1. Preview Day 2's outputs.
### Key content and talking points

Standard debrief structure used every morning (9:00–9:30):

1. Address the top 2–3 'still unclear' items from yesterday's daily evaluation forms — today's are likely VLOOKUP exact-match and the five-part objective anatomy. Re-teach each in under 5 minutes with a fresh example.
1. Report pace/confidence scores honestly ('yesterday's pace rating averaged 'about right'; confidence to teach cleaning averaged 3.4/5'). Transparency builds trust in the feedback loop.
1. Each team gives a 60-second status: topic, objectives final?, data merged? Unblock as a group where one team's solution helps another.
1. Preview the day: 'By 17:00 you will compute real TB notification rates and summarize any distribution five ways.'
### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 9:00–9:12 | 12 | Lead re-teaches top unclear items from daily forms. |
| 9:12–9:22 | 10 | Team stand-ups: 60 seconds each + group unblocking. |
| 9:22–9:30 | 8 | Day 2 preview; Q&A. |

### Materials needed

- Tallied daily evaluation forms
- Flipchart: parking lot
### Facilitator notes — pitfalls, pacing, contingencies

- **Never skip the re-teach —** it is the visible proof that feedback changes the course, which keeps the forms honest all week.
- **Timebox each unclear item to 5 minutes;** deeper confusion becomes a lunchtime clinic, not a debrief derailment.
> **TRAINER TIP** — Run the identical debrief structure in cascade trainings. Trainees who see their feedback acted on within 24 hours will give you the honest signals you need to steer.


## Day 2 (Tue 23 Mar)  |  9:30–10:30

### Training Methodologies

### Learning objectives

1. State four adult-learning principles and their implications for training design.
1. Describe the demonstrate → deconstruct → guided practice → feedback cycle.
1. Use the session-design template to plan a training segment.
### Key content and talking points

Frame: 'From this session on, you are learning everything twice — once as analysts, once as trainers.' Adult-learning foundations:

- **Adults learn by doing.** Lecture retention after 24 hours is poor; guided practice retention is high. Hence this week's ratio: short demos, long practice.
- **Respect experience.** Participants bring years of ministry work — start sessions by surfacing what they know (pair discussions, flipcharts) before adding new content.
- **Immediate relevance.** Every method session ties to their Phase 2 task: 'You will teach this exact skill to district analysts.'
- **Safety to fail.** Synthetic data, no shaming of errors, '#N/A is diagnostic information' — the climate you set is the climate they will replicate.
The core TOT teaching cycle — demonstrate, deconstruct, guided practice, feedback:

1. Demonstrate: perform the skill live at normal speed while narrating decisions (yesterday's cleaning demo was the model).
1. Deconstruct: replay the tricky step slowly; name the rule ('exact match = FALSE').
1. Guided practice: learners replicate immediately with the facilitator circulating — errors caught within minutes, not days.
1. Feedback: specific, prompt, and kind — 'your denominator is right; check the multiplier' beats 'good job'.
Introduce the session-design template they will use Friday and at home: objective → hook → demo → practice → debrief → take-home job aid. Distribute the blank template; they will fill one in on Day 5.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 9:30–9:45 | 15 | Mini-lecture: adult-learning principles; link each to something already experienced this week ('yesterday's cleaning demo...'). |
| 9:45–10:00 | 15 | Deconstruct the cycle using yesterday's VLOOKUP demo as the worked example — participants label each phase. |
| 10:00–10:20 | 20 | Pairs: take one Day 1 skill (e.g., Remove Duplicates) and sketch a 20-minute teach-back using the template. |
| 10:20–10:30 | 10 | Two pairs share; facilitator feedback models the 'specific, prompt, kind' standard. |

### Materials needed

- Slides: Training-Methodologies-1.pptx
- Blank session-design template (workbook)
### Facilitator notes — pitfalls, pacing, contingencies

- **Keep the theory tight —** participants are impatient for Excel; the principles land better when anchored to sessions they have just lived through.
- **Model the feedback standard visibly:** when a pair shares, praise one specific choice before suggesting one improvement. They will copy your tone at home.
> **TRAINER TIP** — This session is the seed of Phase 2. In cascade trainings, open day 1 with a 30-minute version of it — trainees who understand*why* you teach in demos-plus-practice will tolerate (and later copy) the format instead of demanding lectures.


## Day 2 (Tue 23 Mar)  |  10:30–11:00

### Tea

> **TRAINER TIP** — Check in with the team that struggled with merges yesterday — confirm they are unblocked before the rates session, which builds directly on merged files.


## Day 2 (Tue 23 Mar)  |  11:00–12:00

### Accessing and using census data to calculate rates in Excel

### Learning objectives

1. Explain why counts must be converted to rates for fair comparison.
1. Distinguish incidence rate, case notification rate, and proportion.
1. Compute a case notification rate in Excel from the merged Demoland files.
1. State the rules for matching numerators to denominators.
### Key content and talking points

The central epidemiologic idea of the morning: a count without a denominator is just a number; a rate is information. Comparing raw TB case counts across Demoland's districts misleads — a big district will always 'lead'. Rates divide by the population at risk so districts can be compared fairly.

Teach the three related measures precisely:

| **Measure** | **Formula** | **When to use it** |
| --- | --- | --- |
| Incidence rate | (new cases ÷ population at risk) × multiplier (e.g., 100,000) | New TB cases arising in a defined population over a period — the true risk measure. |
| Case notification rate | (notified cases ÷ population) × 100,000 | What surveillance actually captures; the workhorse indicator when, as in Demoland, we count notifications. |
| Proportion / percentage | (part ÷ whole) × 100 | Share of a whole — e.g., % of TB cases that are male (~60–65% in Demoland). Not a rate: no population at risk, no time. |

Worked mini-example (do this live on the flipchart, then in Excel): Suppose a district notifies 240 new TB cases in 2024 and its census population is 300,000. Case notification rate = (240 ÷ 300,000) × 100,000 = 80 per 100,000 population. Then ask: a second district notifies 200 cases in a population of 100,000 → (200 ÷ 100,000) × 100,000 = 200 per 100,000. Fewer cases, far higher burden — this is why rates exist. Have participants replicate with Demoland districts from the merged file, reading values live from the dataset.

- **Choose the multiplier** to avoid tiny decimals: per 100,000 for TB, per 1,000 for common vital events. Always state it ('per 100,000 population').
- **Match numerator to denominator in person, place, and time:** 2024 cases over the 2024 census population, same district, same sex/age strata when stratifying.
- **Never compute mortality rates from Riverside's data** without flagging incompleteness — a rate built on under-registered deaths understates mortality. Teach the integrity check first, the rate second.
- **Excel mechanics:** rate column = (cases_cell / pop_cell)* 100000; lock the multiplier in a named cell; format to 1 decimal; label the column 'TB notification rate per 100,000 (2024)'.
### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 11:00–11:15 | 15 | Hook + mini-lecture: the two-district paradox (200 vs 240 cases); definitions table. |
| 11:15–11:30 | 15 | Worked example live: flipchart math → Excel formula on the merged file; participants follow. |
| 11:30–11:55 | 25 | Exercise: compute 2024 TB notification rates for all 12 districts, then rank them. 'Which district has the most cases? Which has the highest rate? Are they the same?' |
| 11:55–12:00 | 5 | Plenary: the answers differ — land the moral: funding by counts alone misallocates resources. |

### Materials needed

- DA-TOT_Demo_TB-Register_2021-2025.xlsx + DA-TOT_Demo_Census-Population.xlsx (merged)
- Slides: Rates-and-Denominators.pptx
- Flipchart for worked example
### Facilitator notes — pitfalls, pacing, contingencies

- **Watch for the classic error:** rates computed on the wrong year's population or on district totals mismatched to sex-stratified cases. Circulate and check one formula per table early.
- **Do not let anyone invent census numbers —** all denominators come from DA-TOT_Demo_Census-Population.xlsx; describe Demoland patterns qualitatively, values read live from the file.
- **If the exercise finishes early,** stretch: sex-specific rates for 2024 — it previews the equity stratification habit.
> **TRAINER TIP** — Back home, replace Demoland with your country's census and DHIS2 data — the two-district paradox works with any real numbers and instantly convinces managers why denominators matter. Teach the multiplier as 'choose it so the rate is a readable number, then always state it.'


## Day 2 (Tue 23 Mar)  |  12:00–13:00

### Descriptive statistics review

### Learning objectives

1. Define mean, median, mode, range, IQR, and standard deviation.
1. Select the appropriate summary for symmetric vs. skewed vs. categorical data.
1. Explain why the mean alone can mislead when outliers are present.
1. State the limits of descriptive statistics.
### Key content and talking points

Conceptual session — no laptops open. Descriptive statistics summarize data; they do not explain causes. Teach the two families:

### Measures of central tendency — 'what is typical?'

| **Measure** | **Definition** | **When to use it** | **Caution** |
| --- | --- | --- | --- |
| Mean | Sum of values ÷ number of values | Symmetric, continuous data (e.g., average age of TB cases when roughly normal) | Pulled by outliers — one very old case shifts it |
| Median | Middle value when sorted | Skewed data or data with outliers (e.g., district rates when one district spikes) | Hides the shape of the distribution |
| Mode | Most frequent value | Categorical data (most common age group, most affected district) | A dataset can have two modes or none |

### Measures of spread — 'how much does it vary?'

| **Measure** | **Definition** | **When to use it** |
| --- | --- | --- |
| Range | Maximum − minimum | Quick sense of span; very sensitive to extremes |
| Interquartile range (IQR) | 75th percentile − 25th percentile | Spread of the middle half; robust partner to the median |
| Standard deviation (SD) | Typical distance of values from the mean | With the mean for symmetric data; ~68% of values fall within ±1 SD when roughly normal |

The decision rule to drill: plot or at least sort the data first; if symmetric → mean + SD; if skewed or with outliers → median + IQR; if categorical → mode and proportions. Choosing mean + SD for everything is the commonest beginner error — demonstrate with Demoland district rates: Westbrook's rise skews the picture, so the median district rate tells a truer 'typical district' story than the mean.

Close with intellectual honesty: descriptive statistics describe; they do not test hypotheses or prove cause. That boundary is what keeps reports credible.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 12:00–12:20 | 20 | Mini-lecture: central tendency table; the Westbrook-skew demonstration. |
| 12:20–12:40 | 20 | Mini-lecture: spread table; the decision rule; descriptive vs. inferential boundary. |
| 12:40–13:00 | 20 | Paper exercise: 6 small datasets on the worksheet — for each, choose mean/median/mode and justify in one sentence. Peer-check in pairs, then plenary. |

### Materials needed

- Slides: Descriptive-Statistics.pptx
- Worksheet: choosing-summaries (in workbook)
- Flipchart
### Facilitator notes — pitfalls, pacing, contingencies

- **No laptops this hour —** the concepts must live in words before they live in formulas, or participants will compute without choosing.
- **The SD intuition ('typical distance from the mean')** matters more than the formula; save the formula for the Excel session.
- **If energy dips before lunch,** run the paper exercise as a table-vs-table competition — small stakes, big revival.
> **TRAINER TIP** — Re-teach this session with zero technology first, exactly as done here: paper, discussion, decision rules. Trainees who can justify 'median, because Westbrook skews the mean' in words will use the right Excel function without prompting.


## Day 2 (Tue 23 Mar)  |  13:00–14:00

### Lunch

> **TRAINER TIP** — Lunchtime clinic option: invite anyone still shaky on merges or rates to a 20-minute table session. Keep it voluntary and small — no stigma.


## Day 2 (Tue 23 Mar)  |  14:00–15:00

### Descriptive statistics using Excel

### Learning objectives

1. Compute mean, median, mode, SD, quartiles, and n for Demoland district rates.
1. Choose the appropriate summary and justify the choice in one sentence.
1. Apply conditional formatting color scales for exploratory outlier detection.
1. Sort multi-column tables without scrambling row integrity.
### Key content and talking points

Now the morning's concepts become formulas. Participants work with district-level TB notification rates they computed at 11:00. Teach each function with the decision rule attached — never a naked formula:

| **Excel function** | **Syntax** | **Use when** |
| --- | --- | --- |
| AVERAGE | =AVERAGE(range) | Symmetric continuous data |
| MEDIAN | =MEDIAN(range) | Skewed data / outliers present |
| MODE.SNGL | =MODE.SNGL(range) | Most common value |
| STDEV.S | =STDEV.S(range) | Sample SD (our districts are a sample of possible years/places) |
| STDEV.P | =STDEV.P(range) | Only when the range is the entire population of interest |
| MIN / MAX | =MIN(range) / =MAX(range) | Range endpoints |
| QUARTILE.INC | =QUARTILE.INC(range,1) and (...,3) | Q1 and Q3 for the IQR |
| COUNT / COUNTA | =COUNT(range) | How many numeric values — always report n alongside any summary |

- **Build a summary-statistics block:** one row per district-rate indicator, columns for n, mean, median, SD, min, max. Label every cell — a future reader (or their ministry successor) must understand it without them present.
- **Compare mean vs. median aloud:** 'Our mean district rate is X, our median is Y — the gap tells us the distribution is skewed by high-burden districts.' That one sentence is the interpretation habit.
- **Conditional formatting (Home → Conditional Formatting → Color Scales):** apply a 2-color scale to the district-rate column so outliers glow. Steps: select the rate cells → Color Scales → choose a color-blind-safe scale → the highest-burden districts are instantly visible. Use it for exploration, never as the final presentation graphic.
- **Sorting caution:** sort the full table (select all columns) or use Data → Sort with 'expand the selection' — sorting one column alone scrambles district labels from their values, the classic Excel catastrophe. Undo (Ctrl+Z) is the emergency exit.
### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 14:00–14:15 | 15 | Demo: build the summary-statistics block on the district-rate table; narrate each function choice. |
| 14:15–14:40 | 25 | Guided practice: participants replicate, then add sex-stratified summaries. Circulate; check STDEV.S vs STDEV.P choices. |
| 14:40–14:55 | 15 | Conditional formatting + safe-sorting demo and practice; deliberately demo the one-column-sort catastrophe on a copy, then Ctrl+Z. |
| 14:55–15:00 | 5 | Plenary: one table reads its mean-vs-median interpretation sentence aloud. |

### Materials needed

- District-rate tables from the morning
- Slides: Stats-in-Excel.pptx
### Facilitator notes — pitfalls, pacing, contingencies

- **STDEV.S vs STDEV.P confuses everyone —** give the one-line rule (sample → .S) and move on; it rarely changes decisions at this level.
- **The deliberate sort catastrophe** is the most-remembered 60 seconds of the week. Do it on a copy, gasp with them, Ctrl+Z, then teach 'expand the selection'.
- **If participants race ahead,** stretch: IQR via QUARTILE.INC and a one-sentence comparison of IQR vs SD for these data.
> **TRAINER TIP** — In cascade trainings, teach this session on trainees' own district data — the mean-vs-median sentence about their own districts is the moment descriptive statistics becomes theirs. Keep the deliberate sorting catastrophe; it is unforgettable pedagogy.


## Day 2 (Tue 23 Mar)  |  15:00–16:00

### Data analysis using pivot tables

### Learning objectives

1. Build a pivot table from clean tabular data with correct field placement.
1. Use Value Field Settings and 'Show Values As' for counts and percentages.
1. Add slicers to re-stratify analyses by year and sex.
1. Refresh pivot tables after source-data changes.
### Key content and talking points

Position pivot tables as the analyst's engine: 'Everything you did with COUNTIF/SUMIF this morning, a pivot table does in 30 seconds — and redoes instantly when the question changes.' Requirements: clean tabular data with one header row, no merged cells, no blank header cells (recall Monday's cleaning — this is the payoff).

Live build, step by step (participants mirror each step):

1. Click any cell in the TB table → Insert → PivotTable → New Worksheet → OK.
1. Drag Year to Rows, District to Rows (below Year), Sex to Columns, Cases to Values.
1. Click the Cases field in Values → Value Field Settings → change 'Sum of Cases' as needed; for rates work keep sums, then compute rates beside the pivot with GetPivotData-free cell references or by copy-pasting values.
1. Show Values As: right-click a value → Show Values As → '% of Row Total' to get the sex distribution (~60–65% male) instantly; '% of Column Total' for district share of national burden.
1. Group dates/ages: right-click an age-group or year field → Group, to collapse into broader bands.
1. Add slicers (PivotTable Analyze → Insert Slicer) for Year and Sex — one click re-stratifies the whole table. This is the equity disaggregation machine.
1. Refresh discipline: right-click → Refresh after source data changes; a stale pivot is a wrong report.
Exercise: 'Answer in under 3 minutes each: (1) Which district had the highest male TB notifications in 2024? (2) What % of each district's cases are female? (3) Show the national trend 2021–2025 by sex.' The point is speed and flexibility, not just correctness.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 15:00–15:20 | 20 | Live build: lead constructs the TB pivot step by step; participants mirror. Narrate every click. |
| 15:20–15:45 | 25 | Speed exercise: three questions, 3 minutes each; first table to answer correctly explains their field layout. |
| 15:45–16:00 | 15 | Slicers + refresh discipline; plenary: 'What did the pivot reveal that the flat table hid?' |

### Materials needed

- Cleaned DA-TOT_Demo_TB-Register_2021-2025.xlsx
- Slides: Pivot-Tables.pptx
- Workbook: pivot exercise questions
### Facilitator notes — pitfalls, pacing, contingencies

- **Blank header cells and merged cells** break pivot tables — when a pivot misbehaves, the source table is guilty 90% of the time. Teach the diagnosis, not just the clicks.
- **Participants will drag fields to wrong areas;** the fix is instant (drag back), so keep energy high and errors light.
- **If the room is fast,** stretch: computed rates beside the pivot. If slow, drop slicers to team time and protect the core build.
> **TRAINER TIP** — Pivot tables are the single highest-ROI skill in a cascade training — district analysts who pivot stop fearing their own DHIS2 exports. Teach it exactly as a speed tool ('answer in under 3 minutes'), and always on clean data, so the cleaning lesson gets its payoff.


## Day 2 (Tue 23 Mar)  |  16:00–17:00

### Teams analyze data

### Learning objectives

1. Compute district TB notification rates (total and sex-stratified).
1. Produce stratified pivot-table outputs for the team project.
1. Draft the summary-statistics block for the project dataset.
### Key content and talking points

Milestone by 17:00: every team has computed TB notification rates for all districts (2024, total and by sex), built at least one stratified pivot table, and drafted the summary-statistics block. Facilitators verify one rate calculation per team by hand — this is the competency check for the rates session.

Close: 5-minute plenary. Each team states its highest-rate district and its male share of TB — values read from their files. Preview Wednesday: 'Tomorrow we learn to show these findings honestly — IMRAD, tables, figures, maps.' Distribute the Day 2 evaluation form at 16:50; collect at the door.

### Activity plan (minute-by-minute)

| **Clock** | **Min** | **What happens** |
| --- | --- | --- |
| 16:00–16:50 | 50 | Team work; facilitators circulate and hand-verify one rate per team. |
| 16:50–17:00 | 10 | Plenary close: highest-rate district + male share per team; evaluation forms; preview Wednesday. |

### Materials needed

- Merged Demoland files
- Evaluation forms (Day 2)
### Facilitator notes — pitfalls, pacing, contingencies

- **Hand-verify the rates —** a team building Wednesday's figures on a wrong denominator wastes a full day. Ten seconds per team now saves hours later.
- **Collect evaluation forms at the door,** not 'tomorrow morning' — overnight completion rates collapse.
> **TRAINER TIP** — End every cascade-training day the same way: teams state one finding aloud from their own data. Public findings create momentum that carries into the next morning, and the hand-verification habit keeps standards high without shaming.

