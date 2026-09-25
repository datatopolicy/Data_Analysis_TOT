> **DATA FOR HEALTH (D4H) INITIATIVE** — Funded by Bloomberg Philanthropies  ·  Implemented by the CDC Foundation


**Data Analysis and Report Writing**

**Training of Trainers (TOT)**

**PARTICIPANT WORKBOOK**

Kigali, Rwanda  ·  Monday 22 – Friday 26 March 2027

*Saturday 27 March 2027: travel day*

> **A NOTE ON THE DATA** — Every exercise in this workbook uses 100% synthetic demonstration data for the fictional country of “Demoland”. No real patient, facility, or country data is used at any point.
> Demoland has 12 districts: Northfield, Eastvale, Westbrook, Southgate, Lakeside, Hillcrest, Riverside, Meadowlands, Stonebridge, Fairview, Oakdale, and Pinehurst.
> Because the data are synthetic, describe patterns qualitatively (for example, “notifications are rising in Westbrook”) and always compute exact values yourself from the files — do not copy numbers from anyone else’s screen.


24 participants  ·  4 country teams: Bangladesh · Côte d’Ivoire · Rwanda · Tanzania

# How to Use This Workbook

This workbook is your day-by-day companion for the five-day Training of Trainers. Bring it — and your laptop — to every session.

- **Follow the day tabs.** Each day opens with the day’s agenda, then concise key-point summaries of every taught session, then the full hands-on exercises for that day.
- **Exercises are fully specified.** Every exercise names the exact file and worksheet to open, gives numbered steps you can follow on your own, describes the expected output, and ends with reflection questions. File and sheet names are shown in monospace, for example
- **Work in your country team.** Afternoon “teams analyze data” slots and Days 4–5 are for your team project: an analytical report and presentation on Demoland data, presented on Friday morning.
- **Worksheets are yours to keep.** Fill-in worksheets (objectives, equity lens, checklists, planning templates) are designed to be reused when you train others back home.
- **Check your work.** The Day 2 and Day 3 exercise workbooks contain an Answer_Key sheet. Attempt every task first, then compare and discuss differences with your team.
- **Use the back matter.** The glossary defines key terms; the one-page formula quick-reference is meant to live next to your keyboard all week.
Example file reference: DA-TOT_Demo_TB-Register_2021-2025.xlsx  → sheet Data

## Your data and exercise files

All files are provided on your USB drive / shared folder. Open the README sheet of each file first — it describes the file’s contents and conventions.

| **File name** | **What it contains** | **Used on** |
| --- | --- | --- |
| DA-TOT_Demo_TB-Register_2021-2025.xlsx | TB notifications by district × sex × age group × year (2021–2025), with treatment success counts. Sheets: README, Data, Data_Dictionary. | Days 1–2, team project |
| DA-TOT_Demo_Mortality-CRVS_2021-2025.xlsx | Deaths by district × sex × age group × cause (TB, HIV, malaria, maternal, road traffic injuries, other NCDs). Sheets: README, Data, Data_Dictionary. | Team project |
| DA-TOT_Demo_Census-Population.xlsx | Population by district × sex × year (2021–2025), plus age-group shares. Sheets: README, Population, Age_Structure. | Days 1–2, team project |
| DA-TOT_Exercise_Messy-DHIS2-Extract.xlsx | Messy monthly malaria extract: 6 facilities, 2024–2025, ~300 rows, 12+ planted data-quality issues. Sheets: README, Messy_Data, Cleaning_Log. | Day 1 |
| DA-TOT_Exercise-Workbook_Day2.xlsx | Structured exercises on rates, descriptive statistics, and pivot tables. Sheets: README, TB_Data, Census_Data, Tasks, Answer_Key. | Day 2 |
| DA-TOT_Exercise-Workbook_Day3.xlsx | Table, figure, and map exercises. Sheets: README, Bad_Table_1, Bad_Table_2, Bad_Table_3, Figure_Tasks, Map_Task, Answer_Key. | Day 3 |

## A note on numbers in this workbook

The Demoland datasets are built around a few deliberate patterns you will discover: a gradual national decline in TB notifications from 2021 to 2025, rising TB notifications in Westbrook district, a higher TB burden among males (roughly 60–65% of notifications), and visibly incomplete mortality registration in Riverside district. This workbook describes these patterns qualitatively. It never states exact counts or rates as fact — you must compute every number yourself from the demo files. If a number you calculate differs from a colleague’s, check your formulas and denominators before assuming the file is wrong.

# Course Objectives

By the end of this Training of Trainers, you will be able to:

1. Write clear, policy-relevant data analysis objectives linked to a defined audience and decision.
1. Apply an equity lens (PROGRESS-Plus) at every stage of an analysis, from objective-setting to recommendations.
1. Systematically clean and document messy health data in Excel, and combine datasets using lookup functions.
1. Calculate and interpret rates using census denominators, and summarize data with appropriate descriptive statistics.
1. Use Excel pivot tables to explore large health datasets efficiently and reproducibly.
1. Structure an analytical report using the IMRAD framework and design publication-quality tables, figures, and maps.
1. Draft specific, actionable, evidence-linked recommendations for decision-makers.
1. Produce, as a country team, a short analytical report and slide presentation on real-style demo data.
1. Plan and deliver cascade training in your home country using adult-learning methodologies.
1. Develop a 90-day country action plan for applying and teaching these skills after the workshop.

# Agenda at a Glance

*Kigali, Rwanda · Monday 22 – Friday 26 March 2027 · Saturday 27 March: travel day*

### Day 1 — Mon 22 Mar

| **Time** | **Session** |
| --- | --- |
| 9:00–9:30 | Welcome and introductions |
| 9:30–10:00 | Introduction to the Data for Health Initiative Data Analysis Project |
| 10:00–10:30 | Review the TOT schedule and team project |
| 10:30–11:00 | Tea |
| 11:00–12:00 | Principles of Equity |
| 12:00–12:30 | Group Projects: Country teams report on SOPs and challenges accessing data |
| 13:00–14:00 | Lunch |
| 14:00–15:00 | Establish data analysis objectives |
| 15:00–16:00 | Cleaning data in Excel |
| 16:00–16:30 | Combining data sets in Excel |
| 16:30–17:00 | Teams analyze data |

### Day 2 — Tue 23 Mar

| **Time** | **Session** |
| --- | --- |
| 9:00–9:30 | Day 1 debrief |
| 9:30–10:30 | Training Methodologies |
| 10:30–11:00 | Tea |
| 11:00–12:00 | Accessing and using census data to calculate rates in Excel |
| 12:00–13:00 | Descriptive statistics review |
| 13:00–14:00 | Lunch |
| 14:00–15:00 | Descriptive statistics using Excel |
| 15:00–16:00 | Data analysis using pivot tables |
| 16:00–17:00 | Teams analyze data |

### Day 3 — Wed 24 Mar

| **Time** | **Session** |
| --- | --- |
| 9:00–9:30 | Day 2 debrief |
| 9:30–10:30 | IMRAD Structure |
| 10:30–11:00 | Tea |
| 11:00–12:00 | Best practices for creating tables |
| 12:00–13:00 | Tables exercise |
| 13:00–14:00 | Lunch |
| 14:00–15:00 | Best practices for creating figures |
| 15:00–16:00 | Figures exercise |
| 16:00–17:00 | Creating maps in Excel |

### Day 4 — Thu 25 Mar

| **Time** | **Session** |
| --- | --- |
| 9:00–9:30 | Day 3 debrief |
| 9:30–10:30 | Guidelines for creating report templates |
| 10:30–11:00 | Tea |
| 11:00–11:30 | Drafting appropriate recommendations |
| 11:30–12:30 | Teams work on group projects |
| 13:00–14:00 | Lunch |
| 14:00–14:30 | Check in on the progress of group projects |
| 14:30–15:30 | Teams continue working on group projects |

### Day 5 — Fri 26 Mar

| **Time** | **Session** |
| --- | --- |
| 9:00–9:30 | Day 4 debrief |
| 9:30–10:30 | Group report presentations |
| 10:30–11:00 | Tea |
| 11:00–11:30 | Group report presentations (continued) |
| 11:30–13:00 | Team working time: finalize presentations |
| 13:00–14:00 | Lunch |
| 14:00–15:00 | Training Methodologies |
| 15:00–16:00 | Preparing for country-specific data analysis projects |
| 16:00–17:00 | Workshop evaluation and wrap-up |
