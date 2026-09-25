# Glossary of Key Terms

*The working vocabulary of the week. Starred terms (*) appear in the Formula Quick-Reference.*

|**Term**|**Definition**|
| --- | --- |
| Age group | Population band used for disaggregation (here: 0–14, 15–24, 25–44, 45–64, 65+). Never collapse into “adult” without justification. |
| Cascade training | TOT model in which trainees become trainers, passing skills to successive cohorts. Fidelity to the original materials protects quality. |
| Cell reference (absolute vs relative) | A1 adjusts when filled down; $A$1 stays fixed. Use absolute references for multipliers and denominator cells reused across rows. |
| Choropleth map | Map in which areas are shaded by value bands. In this course, built as a tile-grid map with conditional formatting. |
| Cleaning log | Row-by-row record of data-quality issues found and fixes applied — the audit trail of Exercise 1.1 and of any real analysis. |
| Completeness | Data-quality dimension: are all expected records present? (Riverside’s mortality file is the course’s deliberately incomplete example.) |
| Consistency | Data-quality dimension: do values follow the same codes, spellings, and formats throughout? |
| CRVS | Civil registration and vital statistics — the system recording births, deaths, marriages, and divorces; the backbone of mortality statistics. |
| Data dictionary | Document defining every variable: name, definition, codes, units, missing-value conventions. Read it before touching the data. |
| Denominator | The population at risk that a count is divided by to form a rate. Must match the numerator on place, period, sex, and age. |
| Descriptive statistics | Numbers that summarize data: centre (mean, median, mode), spread (range, SD, percentiles), and shape (skew). |
| DHIS2 | District Health Information Software 2 — the open-source platform many countries use for routine health facility reporting. |
| Disaggregation | Splitting results into subgroups (district, sex, age). Averages hide inequity; disaggregation reveals it. |
| Equity (health) | Everyone having a fair opportunity to attain full health — which may require unequal effort and resources. Contrast equality (the same for all). |
| Executive summary | One-page standalone synopsis: objectives, headline findings with numbers, recommendations. Written last, read first. |
| IMRAD | Introduction, Methods, Results, and Discussion — the standard structure for analytical reports. |
| Incidence | New cases occurring in a population over a period. (TB notification rates approximate incidence as captured by the system.) |
| Interquartile range | The range from the 25th to the 75th percentile — the spread of the middle half of the data; robust to outliers. |
| Mean | Arithmetic average: sum ÷ n. Sensitive to outliers and skew. |
| Median | The middle value when data are ordered. Resists outliers; preferred for skewed distributions. |
| Metadata | Data about data: source, coverage, collection method, definitions, known limitations. |
| Mortality rate | Deaths ÷ population at risk × multiplier, for a defined cause, place, and period. Meaningless where registration is incomplete. |
| Numerator | The count of events (cases, deaths) that forms the top half of a rate. |
| Percent change | ((New − Old) ÷ Old) × 100. Use for trends; always state the baseline. |
| Pivot table | Excel’s drag-and-drop summarization tool: rows, columns, values, and filters that rebuild instantly as questions change. |
| PROGRESS-Plus | Equity lens: Place, Race/ethnicity, Occupation, Gender/sex, Religion, Education, Socioeconomic status, Social capital — Plus age, disability, and context-specific factors. |
| Rate | (Events ÷ population at risk) × multiplier (e.g. per 100,000). Makes places and periods comparable. |
| Recommendation | Evidence-linked, actionable statement of who should do what, where, by when — derived from a specific finding. |
| SOP | Standard operating procedure — the documented rules governing data access, sharing, and handling in each country. |
| Standard deviation (SD) | Typical distance of values from the mean. Report as mean ± SD for symmetric data. |
| Synthetic data | Artificially generated data mimicking real structure without real records. All Demoland data are 100% synthetic. |
| TB notification rate | Notified TB cases ÷ population × 100,000, per year. The course’s core indicator. |
| Timeliness | Data-quality dimension: are data available soon enough to act on? |
| Treatment success rate | (Cured + treatment completed) ÷ all notified TB cases × 100, per cohort. |
| Validity | Data-quality dimension: do values fall within plausible ranges and formats (no negatives where impossible, no text in numeric fields)? |
| XLOOKUP* | Modern Excel lookup: =XLOOKUP(lookup_value, lookup_array, return_array). Exact match by default; searches in any direction. |

# Excel Formula Quick-Reference

*Keep this page beside your keyboard. All formulas use Excel’s standard English function names.*

### Summarizing data

|**What you want**|**Formula**|**Example**|
| --- | --- | --- |
| Sum | =SUM(range) | =SUM(C2:C301) |
| Average (mean) | =AVERAGE(range) | =AVERAGE(C2:C301) |
| Median | =MEDIAN(range) | =MEDIAN(C2:C13) |
| Mode | =MODE.SNGL(range) | =MODE.SNGL(C2:C301) |
| Standard deviation (sample) | =STDEV.S(range) | =STDEV.S(C2:C13) |
| Minimum / maximum | =MIN / =MAX | =MAX(C2:C13)-MIN(C2:C13)  → range |
| 25th / 75th percentile | =QUARTILE.INC(range,1 or 3) | =QUARTILE.INC(C2:C13,1) |
| Count of numbers | =COUNT(range) | =COUNT(C2:C301) |

### Conditional sums and counts

|**What you want**|**Formula**|**Example**|
| --- | --- | --- |
| Count matching a criterion | =COUNTIF(range,criterion) | =COUNTIF(B2:B301,“Westbrook”) |
| Count matching several criteria | =COUNTIFS(r1,c1,r2,c2…) | =COUNTIFS(B2:B301,“Westbrook”,D2:D301,“Female”) |
| Sum matching criteria | =SUMIFS(sum_range,r1,c1…) | =SUMIFS(C2:C301,B2:B301,“Westbrook”) |
| Average matching criteria | =AVERAGEIFS(avg_range,r1,c1…) | =AVERAGEIFS(C2:C301,B2:B301,“Westbrook”) |

### Combining datasets & cleaning text

|**What you want**|**Formula / tool**|**Example**|
| --- | --- | --- |
| Look up a value | =XLOOKUP(key, lookup_array, return_array) | =XLOOKUP(A2,Pop!$A:$A,Pop!$D:$D) |
| Safe lookup (flag misses) | =IFERROR(XLOOKUP(…),“CHECK”) | =IFERROR(XLOOKUP(A2,Pop!$A:$A,Pop!$D:$D),“CHECK”) |
| Remove extra spaces | =TRIM(text) | =TRIM(B2) → paste as values |
| Standardize case | =UPPER / =LOWER / =PROPER | =PROPER(B2) → “Westbrook” |
| Build a composite key | =A2&“\|”&B2&“\|”&C2 | =B2&“\|”&C2&“\|”&D2 |
| Branch on a condition | =IF(test, if_true, if_false) | =IF(C2<0,“CHECK”,C2) |
| Remove duplicates | Data → Remove Duplicates | Select data first; record rows removed |
| Text to true dates/numbers | Data → Text to Columns → Finish | Fixes dates & numbers stored as text |

### Rates and change

|**What you want**|**Formula**|**Example**|
| --- | --- | --- |
| Rate per 100,000 | =events/population*100000 | =B2/C2*100000 → 1 decimal |
| Percentage share | =part/total*100 | =B2/B$14*100 → 1 decimal |
| Percent change over time | =(new-old)/old*100 | =(C6-C2)/C2*100 |
| Treatment success rate (%) | =successes/notified*100 | =D2/B2*100 |

### Presenting

|**Task**|**How**|**Tip**|
| --- | --- | --- |
| Pivot table | Insert → PivotTable | Check Values = Sum (not Count); Refresh after edits |
| Slicer | PivotTable Analyze → Insert Slicer | One-click filtering for exploration & demos |
| Conditional formatting | Home → Conditional Formatting | 3–4 bands, single-hue progression for maps |
| Freeze panes | View → Freeze Panes | Keep headers visible while scrolling |
| Thousands separator | Number format “#,##0” | Counts readable at a glance |
