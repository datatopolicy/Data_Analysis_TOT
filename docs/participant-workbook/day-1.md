# Day 1 — Monday 22 March

**Foundations, Equity & Data Cleaning**

## 9:00–9:30 · Welcome and introductions

{% hint style="success" %}
**KEY POINTS**— Meet your facilitators, the 24 participants, and your country team (Bangladesh, Côte d’Ivoire, Rwanda, or Tanzania — six members each).
Course norms: punctuality, phones on silent, one conversation at a time, and “no question is too basic” — you will soon be answering these same questions as trainers.
Logistics: venue map, Wi-Fi, tea/lunch times, and where to find help with laptops and files.
Orient yourself to this workbook and the six Excel files listed in “Your data and exercise files” — you will open at least one every day.
{% endhint %}

## 9:30–10:00 · Introduction to the Data for Health Initiative Data Analysis Project

{% hint style="success" %}
**KEY POINTS**— The Data for Health (D4H) Initiative, funded by Bloomberg Philanthropies and implemented by the CDC Foundation, partners with governments to strengthen public-health data systems — especially civil registration and vital statistics (CRVS), cancer registries, and NCD risk-factor surveillance.
Good data only matters if it is used. This project’s goal is sustainable, in-country capacity to analyse routine health data and turn it into reports that decision-makers actually read.
That is why this is a Training of Trainers: you are not just learning analysis skills, you are learning to teach them. Everything this week — the exercises, the checklists, the templates — is designed to be reused in your home country.
Your team project (see next session) is the rehearsal: by Friday your team will have produced and presented a complete mini-analysis, exactly as you will later guide others to do.
{% endhint %}

## 10:00–10:30 · Review the TOT schedule and team project

{% hint style="success" %}
**KEY POINTS**— The week builds in order: clean and combine data (Day 1) → calculate rates and summarise (Day 2) → present with tables, figures, and maps (Day 3) → write the report and recommendations (Day 4) → present and plan your cascade training (Day 5).
Team project brief: in your country team of six, analyse the Demoland demo datasets and produce (a) a short analytical report of 4–6 pages using the IMRAD structure, and (b) a 12-minute slide presentation delivered on Friday morning.
Milestones: analysis objectives fixed by end of Day 1; core results and rates by end of Day 2; draft tables/figures/maps by end of Day 3; full draft report by end of Day 4.
Roles rotate, but every team needs at minimum: a coordinator, a data lead, a visuals lead, and a writing lead. Agree yours today.
{% endhint %}

## 11:00–12:00 · Principles of Equity

{% hint style="success" %}
**KEY POINTS**— Equality vs equity: equality gives everyone the same; equity gives people what they need to reach the same outcome. In health data work, equity means asking who is being left behind — and designing the analysis so the answer is visible.
PROGRESS-Plus is the standard lens: Place of residence, Race/ethnicity/culture, Occupation, Gender/sex, Religion, Education, Socioeconomic status, Social capital — Plus age, disability, and other context-specific factors.
Apply the lens at every stage: objectives (whose health are we measuring?), data (who is missing from the register?), analysis (disaggregate, don’t just average), reporting (show the gaps plainly), and recommendations (target the underserved).
Averages hide inequity. A national TB decline can coexist with a district where cases are rising — you will see exactly this in Demoland with Westbrook district.
Demoland worked example: males account for roughly 60–65% of TB notifications. An equity lens turns that statistic into questions: Are men less likely to seek care early? Are services reaching workplaces and transport hubs where men cluster? Your recommendations should answer those questions, not just report the share.
{% endhint %}

## 12:00–12:30 · Group Projects: Country teams report on SOPs and challenges accessing data

{% hint style="success" %}
**KEY POINTS**— Each country team gives a 5-minute report: What SOPs govern data access and sharing in your setting? What are the biggest practical challenges (permissions, timeliness, data quality, linkage)?
Listen for patterns across the four countries — common challenges become design constraints for the cascade trainings you will run.
Capture one challenge per team on a flipchart: you will revisit these on Day 5 when planning country-specific projects.
{% endhint %}

## 14:00–15:00 · Establish data analysis objectives

{% hint style="success" %}
**KEY POINTS**— Every analysis starts before the data: with a written objective. Analyses that start with “let’s see what the data says” produce unfocused reports nobody uses.
A strong objective names the health issue, the population, the place, the time period, and the measure: “Estimate annual TB notification rates per 100,000 by district and sex, Demoland, 2021–2025.”
Work backwards from the decision: What policy question must this answer? Who will act on the answer? Write those down first (Worksheet 1A), then the objective almost writes itself.
Limit yourself: three to five objectives per report. Each objective should map to one results section and at least one recommendation.
Revisit objectives after first exploring the data — Riverside’s incomplete mortality registration, for example, may force you to narrow a mortality objective or add a data-quality objective.
{% endhint %}

### Exercise 1.1: Clean the messy DHIS2 malaria extract  (60 minutes)

**Purpose:**Practise a systematic, documented data-cleaning workflow on a realistic messy extract, so that every downstream rate, table, and map rests on data you can defend.

**Open:**DA-TOT_Exercise_Messy-DHIS2-Extract.xlsx — start with the README sheet, then work in Messy_Data.

**Log sheet:**DA-TOT_Exercise_Messy-DHIS2-Extract.xlsx — sheet Cleaning_Log (template provided).

**Steps**

1.**1. Read the README sheet.**Note the file’s grain: monthly malaria reports from 6 facilities, 2024–2025, about 300 rows. The columns are Facility, District, Month, Year, Sex, Age_Group, Malaria_Cases, and Malaria_Tests (row 1 is a banner — the headers are in row 2). Note which columns are required and which must be numeric.
1.**2. Protect the original.**Right-click the Messy_Data tab → Move or Copy → tick “Create a copy” → rename the copy Messy_Data_ORIGINAL. Do all cleaning on Messy_Data, never on the original.
1.**3. Set up your Cleaning_Log.**The template has columns Step_No | Issue_Found | Rows_Affected | Fix_Applied | Excel_Feature_Used, and Step 1 (duplicate rows) is already completed as an example. You will add at least 11 more rows — 12 documented fixes minimum, one per issue type below.
1.**4. Hunt down and fix each of the 12 planted issue types:**(a) Duplicate rows — select the data → Data → Remove Duplicates; record how many rows were removed. (b) Inconsistent district spelling and capitalization (e.g. “westbrook”, “WestBrook ”, “WESTBROOK”) — standardize every value to the 12 official district names (Northfield, Eastvale, Westbrook, Southgate, Lakeside, Hillcrest, Riverside, Meadowlands, Stonebridge, Fairview, Oakdale, Pinehurst) using Find & Replace or PROPER() plus manual checks. (c) Leading/trailing spaces in text fields — apply =TRIM() in a helper column, paste back as values. (d) Mixed date formats (text dates, dd/mm/yyyy vs mm/dd/yyyy confusion) — convert the whole column to true Excel dates (yyyy-mm-dd); use DATEVALUE() or Text to Columns for text dates, and verify century/month-day order row by row. (e) Missing (blank) values in required fields — filter for blanks, decide a rule (e.g. exclude from numerators, never silently fill), and document the rule. (c–e are the classic trio: fix them before anything else.) (f) Text strings in numeric fields (“N/A”, “unknown”, “-”) — replace with blank (missing) or a documented code, never with zero unless zero is truly meant. (g) Negative counts in fields that cannot be negative — filter for <0, investigate, and recode as missing with a log note. (h) Inconsistent sex labels (M, F, Male, Female, m, f) — standardize the whole column to “Male”/“Female”. (i) Inconsistent facility names (spelling variants of the same 6 facilities) — standardize; check with a pivot table count per facility afterwards. (j) Implausible out-of-range values (e.g. a monthly case count far beyond any plausible value for one facility) — flag as “verify with source” rather than deleting. (k) Merged header cells and stray blank rows/columns — unmerge all, give every column a single-row header, delete fully blank rows/columns. (l) Numbers stored as text (green triangle in the cell corner) — convert to values (Text to Columns → Finish, or Paste Special × 1).
1.**5. Verify with a pivot table.**Insert → PivotTable on the cleaned data: count rows by facility and by month. Totals should look plausible and complete for 2024–2025 — no facility should vanish.
1.**6. Complete the Cleaning_Log.**Every fix gets a row: where, what the issue was, and exactly what you did. A log someone else could audit is the pass mark.
1.**7. Save a cleaned copy.**File → Save As → DA-TOT_Exercise_Messy-DHIS2-Extract_CLEANED.xlsx in the same folder. Keep the original file untouched.
**Expected output:**A cleaned Messy_Data sheet (single-row headers, no merged cells, consistent districts/facilities/sex labels, true dates, numeric fields numeric, no duplicates, no negatives) plus a Cleaning_Log with at least 12 documented fixes, and a verification pivot table.

***Reflection questions:***

- Which of the 12 issue types would most distort a trend chart of malaria cases over time — and why?
- When is it acceptable to delete a suspicious value, and when must you flag it instead? Who decides?
- How does poor cleaning in this small file scale into risk when the file has 300,000 rows instead of 300?
## 16:00–16:30 · Combining data sets in Excel

{% hint style="success" %}
**KEY POINTS**— Counts alone mislead: a district with more cases may simply have more people. Combining case data with population denominators is what turns counts into comparable rates.
XLOOKUP is the modern Excel lookup: =XLOOKUP(lookup_value, lookup_array, return_array). It searches left-to-right or right-to-left, defaults to exact match, and lets you specify what to return when there is no match.
Build a single lookup key on both sides (e.g. District & “|” & Year & “|” & Sex) so one formula matches district, year, and sex together — this avoids the classic error of attaching the wrong year’s population.
Wrap lookups in IFERROR to handle missing combinations explicitly, e.g. =IFERROR(XLOOKUP(...), “CHECK”), then investigate every “CHECK” instead of letting a silent zero through.
District names must match character-for-character between files — which is exactly why you standardized spellings in Exercise 1.1.
{% endhint %}

### Exercise 1.2: Combine TB notifications with census denominators (XLOOKUP)  (30 minutes)

**Purpose:**Attach the correct population denominator to every TB notification record, producing an analysis-ready file for Day 2’s rate calculations.

**Cases:**DA-TOT_Demo_TB-Register_2021-2025.xlsx — sheet Data (read README and Data_Dictionary first).

**Denominators:**DA-TOT_Demo_Census-Population.xlsx — sheet Population.

**Steps**

1.**1. Open both files and inspect.**In the TB register’s Data sheet, identify the District, Year, Sex, and Age_Group columns — and note the built-in Population column (age-group populations, useful later for validation). In the census file’s Population sheet, confirm it holds official population by district × sex × year for 2021–2025 (columns District, Year, Sex, Population).
1.**2. Add a lookup key in the TB file.**Insert a column “Key_TB” with =District&“|”&Year&“|”&Sex (adjust to your actual column letters). Fill down.
1.**3. Add the same key in the census file.**Insert a column “Key_Pop” built identically: district, year, sex in the same order with the same separator.
1.**4. Pull the census population across.**In the TB file add a column “Census_Pop” with =IFERROR(XLOOKUP(Key_TB, Key_Pop_range, Population_range), “CHECK”). Fill down.
1.**5. Investigate every “CHECK”.**A missing match means a spelling mismatch or a genuinely absent combination — fix the cause, don’t overwrite the formula.
1.**6. Spot-check five rows by hand.**Pick five diverse rows (different districts, years, sexes) and confirm the Census_Pop value matches the census sheet manually.
1.**7. Validate against the built-in figures.**In a quick pivot, sum the TB file’s built-in age-group Population by district × year × sex and compare with Census_Pop: the two should agree closely. Investigate any district-year-sex where they don’t — that disagreement is exactly the kind of denominator problem this exercise trains you to catch.
1.**8. Save your work.**Save the TB file under a new name, e.g. DA-TOT_Demo_TB-Register_2021-2025_WITH-POP.xlsx, so the distributed original stays pristine.
**Expected output:**A TB dataset in which every notification record carries its matching official census population (Census_Pop), with zero unresolved “CHECK” values, a validation note comparing Census_Pop against the summed age-group populations, and a short note of your five spot-checks.

***Reflection questions:***

- Why is a combined district+year+sex key safer than looking up district alone?
- What would happen to your Day 2 rates if one district’s name were misspelled in only one of the two files?
## 16:30–17:00 · Teams analyze data

Team time. Today’s deliverable: agree your team’s 3–5 analysis objectives (Worksheet 1A below), assign team roles (coordinator, data lead, visuals lead, writing lead), and confirm every member can open all six files. Facilitators circulate to review draft objectives before you leave.

## Day 1 Worksheets

## Worksheet 1A: Analysis Objectives Worksheet

*For each analysis objective, state the policy question it answers, who will act on the answer, and what data it needs. The first row is a completed worked example for the Demoland TB analysis — use it as your model.*

|**#**|**Analysis objective (issue + population + place + period + measure)**|**Policy question it answers**|**Intended audience**|**Data needed**|
| --- | --- | --- | --- | --- |
| Ex. | Estimate annual TB notification rates per 100,000 population by district, sex, and year, Demoland 2021–2025. | Is TB declining nationally, and which districts and sex groups are being left behind? | National TB Programme managers; D4H country team. | TB register notifications (DA-TOT_Demo_TB-Register_2021-2025.xlsx, Data) + census denominators (DA-TOT_Demo_Census-Population.xlsx, Population). |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

## Worksheet 1B: Health Equity Lens Checklist (PROGRESS-Plus)

*Work through each domain for your team’s analysis topic. The TB column shows completed example answers — your team completes the right-hand column for its own topic.*

|**PROGRESS-Plus domain**|**Equity question to ask**|**Example answer: Demoland TB analysis**|**Your team’s answer**|
| --- | --- | --- | --- |
| Place of residence | Do rates differ by district or urban/rural? | Westbrook’s notifications are rising while the national trend declines — plan a district-disaggregated analysis, not a national average. |  |
| Race / ethnicity / culture | Are any ethnic or cultural groups over- or under-represented? | Demoland demo files do not record ethnicity — note this as a data gap and avoid conclusions about groups you cannot see. |  |
| Occupation | Do occupational exposures or access barriers differ? | Mining and transport corridors cluster in specific districts — cross-check district patterns against known occupational hubs. |  |
| Gender / sex | Do males and females differ in burden or care-seeking? | Males carry roughly 60–65% of notifications — disaggregate every rate by sex and ask whether services reach men. |  |
| Religion | Do beliefs affect care-seeking or registration? | No religion variable in the demo data — consider qualitative follow-up rather than assuming no effect. |  |
| Education | Does health literacy shape early care-seeking? | Not in the demo files — flag for the recommendations section as a likely driver of late presentation. |  |
| Socioeconomic status | Are poorer districts or groups worse affected? | Compare district rates against district poverty proxies where available; never rank districts without context. |  |
| Social capital | Do marginalized groups face stigma or exclusion? | TB stigma may suppress care-seeking — interpret low notifications as possible under-detection, not low burden. |  |
| Plus: age | Which age groups carry the burden? | Use the 0–14 / 15–24 / 25–44 / 45–64 / 65+ groups in the TB file — do not collapse into “adult”. |  |
| Plus: disability | Are people with disabilities counted and reached? | Not recorded — list as a limitation and a future data-collection recommendation. |  |

## Day 1 Daily Reflection

*Take five minutes before you leave. Honest answers here become your personal study guide for the week.*

**The most important thing I learned today was …**

**One thing I am still unsure about (I will ask tomorrow) …**

**One idea from today I can already use in my home country …**

**My team’s analysis objectives after today’s discussion …**

{% hint style="success" %}
**DAY KEY TAKEAWAYS**— Start every analysis with written objectives tied to a policy question and a named audience — never with “let’s see what the data says”.
Equity is a method, not a topic: apply the PROGRESS-Plus lens at objective-setting, data review, analysis, reporting, and recommendations.
National averages hide inequity — always disaggregate by place, sex, and age before drawing conclusions.
Clean data systematically and log every fix: the Cleaning_Log is your audit trail and your credibility.
Standardize text fields (districts, facilities, sex labels) before combining files — lookups only match character-for-character.
Combine case counts with census denominators via XLOOKUP on a composite key (district + year + sex); investigate every non-match.
Your team project runs all week: objectives today, results by Tuesday, visuals by Wednesday, draft report by Thursday, presentation Friday.
{% endhint %}

## Notes

*Use this space for your own notes, questions for the facilitators, and ideas to take home.*
