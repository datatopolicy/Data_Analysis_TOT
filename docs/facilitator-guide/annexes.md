# Annex A — Glossary

Key terms used in this course, in alphabetical order. Facilitators: point participants here rather than defining terms from memory — consistent definitions across the four country teams matter.

|**Term**|**Definition**|
| --- | --- |
| Bloomberg Philanthropies | Funder of the Data for Health Initiative; supports government partnerships to strengthen public-health data systems. |
| Case notification rate | Number of notified cases (e.g., TB) divided by the population, multiplied by 100,000. Reflects what surveillance captures, not necessarily true incidence. |
| Categorical data | Data in named groups (sex, district, age group) rather than numbers; summarized with counts, proportions, and the mode. |
| Cause of death | The disease or injury that initiated the chain of events leading to death; recorded on the death certificate and coded (e.g., ICD) for statistics. |
| CDC Foundation | Implementing partner of the Data for Health Initiative alongside Bloomberg Philanthropies. |
| Census | Complete enumeration of a population, typically every 10 years; provides denominators for rates at fine geographic and demographic detail. |
| Cleaning log | Written record of every data-cleaning step (file, date, action, rows before/after); belongs in a report's Methods section for reproducibility. |
| Choropleth map | Thematic map shading areas by value (darker = higher); in this course built in Excel via Filled Map charts or conditional-formatting grids. |
| Civil registration | Continuous, compulsory government recording of vital events (births, deaths, marriages, divorces). |
| Completeness (of registration) | Proportion of actual vital events captured by the civil registration system; e.g., Riverside district's visibly incomplete mortality registration in Demoland. |
| Conditional formatting | Excel feature that formats cells by their values (e.g., color scales); used here for exploratory outlier detection and offline district maps. |
| Confidence interval | Range of values likely to contain the true population value; quantifies uncertainty around an estimate (beyond this course's descriptive scope, but analysts should know the term). |
| Continuous data | Numeric data that can take any value in a range (age, rate); summarized with means/medians and SD/IQR. |
| CRVS | Civil Registration and Vital Statistics — the system recording births/deaths and producing vital statistics; a core D4H focus area. |
| Data dictionary | Document defining every variable in a dataset: name, definition, format, allowed values, source. Essential companion to any shared file. |
| Data for Health (D4H) Initiative | Bloomberg Philanthropies–funded, CDC Foundation–implemented partnership strengthening government health-data systems, especially CRVS and routine health information. |
| Data validation (Excel) | Data-tab feature restricting cell entries to a defined list or rule; prevents typos at the point of entry. |
| Denominator | The population at risk (or total) divided into; must match the numerator in person, place, and time. Wrong denominators are the commonest rate error. |
| Descriptive statistics | Numbers summarizing data (mean, median, SD, counts, percentages); they describe but do not test hypotheses or prove cause. |
| DHIS2 | District Health Information Software 2 — open-source routine health information system used in 70+ countries for aggregate facility data. |
| Disaggregation | Splitting results into subgroups (sex, age, district); the core analytic habit of equity analysis. |
| Distribution | How values spread across their range; its shape (symmetric vs. skewed) determines whether to use mean or median. |
| Equity (health) | Everyone having a fair and just opportunity to be as healthy as possible; requires removing obstacles such as poverty and discrimination. Distinct from equality (same for all). |
| Filled Map (Excel) | Excel chart type shading geographic areas by value; requires internet (Bing geocoding) and recognized place names. |
| IMRAD | Introduction, Methods, Results, and Discussion — the standard structure of a technical report, each section with a strict border policy. |
| Incidence rate | (New cases ÷ population at risk) × multiplier (e.g., 100,000). Measures the risk of developing a condition over a period. |
| Indicator | Standardized measure (with defined numerator, denominator, and disaggregation) used to track a health phenomenon over time or across groups. |
| Interquartile range (IQR) | 75th percentile minus 25th percentile; spread of the middle half of the data; robust partner to the median. |
| Mean | Sum of values ÷ number of values; use for symmetric continuous data; pulled by outliers. |
| Median | Middle value when sorted; use for skewed data or data with outliers. |
| Metadata | Data about data: source, collection date, definitions, known limitations. A dataset without metadata is a rumor. |
| Mode | Most frequent value; the summary for categorical data. |
| Morbidity | Burden of disease/illness in a population (as distinct from mortality). |
| Mortality rate | (Deaths ÷ population) × multiplier; only interpretable where death registration is reasonably complete (cf. Riverside). |
| Multiplier | Scaling factor in a rate (100; 1,000; 100,000) chosen so the result is a readable number; always stated with the rate. |
| Numerator | The count of events (cases, deaths) placed over the denominator in an indicator. |
| Outlier | Value far from the rest; investigate (error? real extreme?) rather than silently deleting. |
| Pivot table | Excel engine for rapid stratified summaries: drag fields to rows/columns/values; with slicers it re-stratifies in one click. |
| Prevalence | Proportion of a population with a condition at a given time; distinct from incidence (new cases over a period). |
| PROGRESS-Plus | Equity checklist: Place, Race/ethnicity, Occupation, Gender/sex, Religion, Education, Socioeconomic status, Social capital, plus age, disability, and other context-specific dimensions. |
| Proportion | (Part ÷ whole) × 100; a share of a whole — not a rate (no population at risk, no time element). |
| Range | Maximum minus minimum; quickest but crudest measure of spread. |
| Rate | Events divided by population at risk over a period, scaled by a multiplier; enables fair comparison across differently sized populations. |
| Remove Duplicates (Excel) | Data-tab tool deleting repeated rows; select the full table first and tick only the columns defining a true duplicate. |
| Skewed data | Distribution with a long tail on one side (e.g., district rates pulled up by Westbrook); summarize with median + IQR, not mean + SD. |
| Slicer (Excel) | Clickable filter buttons for a pivot table; one click re-stratifies the analysis. |
| SOP (Standard Operating Procedure) | Written step-by-step instruction for a routine task — e.g., requesting, accessing, cleaning, and sharing health data. |
| Standard deviation (SD) | Typical distance of values from the mean; reported with the mean for symmetric data. |
| Stratification | See disaggregation: analysis within subgroups to reveal differences hidden by averages. |
| Synthetic data | Artificially generated data mimicking real patterns without real records; all Demoland datasets are 100% synthetic. |
| Text-to-Columns (Excel) | Data-tab wizard splitting combined text into columns by delimiters; also converts text-numbers to numbers. |
| Training of Trainers (TOT) | Course preparing participants to train others; this week's 24 participants become national trainers for Phase 2 cascade trainings. |
| Treatment success rate | (TB patients cured + treatment completed ÷ all registered for treatment) × 100; core TB program indicator. |
| TRIM (Excel) | Function removing leading/trailing spaces: =TRIM(A2); paste as values over the original. Spaces are the commonest cause of failed lookups. |
| Value Field Settings (Excel) | Pivot-table dialog controlling how a value field summarizes (sum, count, average) and displays (% of row/column total). |
| Vital statistics | Statistics on vital events (births, deaths, causes of death) derived from civil registration. |
| XLOOKUP (Excel) | Modern lookup: =XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found]); searches in any direction, exact match by default. |

# Annex B — Excel Formula Quick-Reference

One-page-per-topic reference for participants' desks. All syntax verified for Excel 2016 and later; XLOOKUP notes where it requires Excel 2021 / Microsoft 365 (use INDEX/MATCH on older versions). Absolute references ($A$2) lock ranges when filling down — press F4 to toggle.

|**Formula / feature**|**Syntax**|**Example**|**Use case**|
| --- | --- | --- | --- |
| SUM | =SUM(B2:B13) | =SUM(Jan:Dec!B2) across sheets | Total cases, deaths, or any additive measure. |
| AVERAGE | =AVERAGE(B2:B13) | =AVERAGE(rate_range) | Mean of symmetric continuous data. |
| MEDIAN | =MEDIAN(B2:B13) | =MEDIAN(district_rates) | Typical value for skewed data (e.g., district rates with Westbrook high). |
| MODE.SNGL | =MODE.SNGL(B2:B13) | =MODE.SNGL(age_group_codes) | Most frequent value; categorical data. |
| STDEV.S | =STDEV.S(B2:B13) | =STDEV.S(rate_range) | Sample standard deviation; partner to the mean. |
| STDEV.P | =STDEV.P(B2:B13) | =STDEV.P(full_pop_range) | Population SD; only when the range is the entire population. |
| MIN / MAX | =MIN(B2:B13) | =MAX(B2:B13)-MIN(B2:B13) for range | Endpoints and range of a distribution. |
| QUARTILE.INC | =QUARTILE.INC(B2:B13,1) | =QUARTILE.INC(r,3)-QUARTILE.INC(r,1) for IQR | Q1/Q3; IQR = robust spread with the median. |
| COUNT / COUNTA | =COUNT(B2:B13) | =COUNTA(A2:A100) | COUNT: numeric cells (report n); COUNTA: non-empty cells. |
| COUNTIF | =COUNTIF(C2:C100,"Male") | =COUNTIF(district_range,"Westbrook") | Count rows meeting one criterion. |
| COUNTIFS | =COUNTIFS(C2:C100,"Male",D2:D100,2024) | — | Count rows meeting multiple criteria. |
| SUMIF | =SUMIF(C2:C100,"Male",B2:B100) | — | Sum values where a criterion holds. |
| SUMIFS | =SUMIFS(B2:B100,C2:C100,"Male",D2:D100,2024) | — | Sum with multiple criteria. |
| AVERAGEIF(S) | =AVERAGEIF(C2:C100,"Female",B2:B100) | — | Mean within a subgroup. |
| IF | =IF(B2>100,"High","Low") | =IF(B2="","Missing","OK") | Conditional logic; flagging thresholds and missing data. |
| IFERROR | =IFERROR(VLOOKUP(...),"Check key") | =IFERROR(A2/B2,"No data") | Trap errors gracefully during merges and rate math. |
| VLOOKUP | =VLOOKUP(A2,Pop!$A$2:$B$13,2,FALSE) | — | Pull denominator by key; FALSE = exact match (always for merges); key must be leftmost column. |
| XLOOKUP | =XLOOKUP(A2,Pop!$A$2:$A$13,Pop!$B$2:$B$13,"Missing") | — | Modern lookup; any direction; exact by default; built-in not-found value. Excel 2021+/365. |
| INDEX/MATCH | =INDEX(Pop!$B$2:$B$13,MATCH(A2,Pop!$A$2:$A$13,0)) | — | Flexible lookup for Excel 2016/2019 without XLOOKUP; immune to inserted columns. |
| CONCAT / TEXTJOIN | =CONCAT(A2,"_",B2) | =TEXTJOIN("_",TRUE,A2:C2) | Build composite keys (district_year) for merging. |
| TEXT | =TEXT(A2,"000") | =TEXT(B2,"mmm-yyyy") | Format numbers/dates as text with fixed patterns. |
| DATE / YEAR / MONTH | =DATE(2024,3,22) | =YEAR(A2) | Build or extract date parts; validate date columns. |
| DATEVALUE | =DATEVALUE(A2) | — | Convert text-dates to real dates (then format as Date). |
| TRIM | =TRIM(A2) | Paste Special → Values over original | Strip leading/trailing spaces before merges. |
| UPPER / LOWER / PROPER | =PROPER(A2) | — | Standardize text case ('westbrook' → 'Westbrook'). |
| LEFT / RIGHT / MID | =LEFT(A2,4) | =MID(A2,6,4) | Extract parts of coded fields before Text-to-Columns. |
| LEN | =LEN(A2) | =IF(LEN(A2)<>12,"Check ID","") | Length checks for ID/code validation. |
| ROUND | =ROUND(B2/C2*100000,1) | — | Rates to 1 decimal; percentages sensibly rounded. |
| Pivot: Value Field Settings | Right-click value → Value Field Settings | Summarize by Sum/Count/Average | Control how the pivot aggregates each field. |
| Pivot: Show Values As | Right-click → Show Values As → % of Row Total | — | Instant sex distributions and district shares. |
| Pivot: Slicer | PivotTable Analyze → Insert Slicer → Year, Sex | — | One-click re-stratification for equity analysis. |
| Pivot: Refresh | Right-click pivot → Refresh | Alt+F5 | Update after source data changes; a stale pivot is a wrong report. |
| Conditional Formatting | Home → Conditional Formatting → Color Scales | — | Exploratory outlier detection; offline district grid-maps. |
| Sort safely | Data → Sort (expand selection) | — | Sort whole tables; never one column alone. |
| Remove Duplicates | Data → Remove Duplicates | Tick key columns only | Deduplicate on district+year+sex+age-group, not all columns. |
| Data Validation | Data → Data Validation → List | — | Lock categorical columns to allowed values at entry. |

{% hint style="info" %}
**TRAINER TIP**— Print Annex B on card stock and hand it out on Monday morning — participants reach for it all week, and it becomes the most-used page of their cascade-training workbook back home.
{% endhint %}
