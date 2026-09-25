> **Download the original file:** [SOP-Template_Data-Access-and-Analysis.docx](../../assets/templates/SOP-Template_Data-Access-and-Analysis.docx)

**Standard Operating Procedure
Requesting, Analyzing, and Reporting Surveillance Data**

# Document Control

| **Item** | **Detail** |
| --- | --- |
| SOP number | SOP-DATA-001 (example — assign your institutional numbering) |
| Version | 1.0 (example) |
| Effective date | 1 April 2027 (example) |
| Review date | 1 April 2028 (example — review annually) |
| Owner | Head of M&E Unit, Ministry of Health (example) |
| Classification | Internal — contains no patient-identifiable data handling beyond aggregate records |

* **NOTE (template guidance):** **Replace all example names, dates, and titles in [brackets] with your institution's real ones before adoption.*

# 1. Purpose

This SOP defines the standard steps for requesting surveillance datasets, checking their quality, analyzing them, and producing approved program reports — so that every analysis in this institution is reproducible, timely, and decision-useful. Example in force: the Demoland (fictional) National TB Program uses this SOP for its annual TB notification and treatment-outcome analysis each January–March.

# 2. Scope

Applies to all staff who request, handle, analyze, or approve surveillance and program data for official reports, including M&E officers, district data managers, program managers, and contracted analysts. It covers aggregate case and program data; handling of patient-identifiable line lists follows SOP-DATA-002 (Data Privacy and Confidentiality) — example reference; create or cross-reference your equivalent.

# 3. Roles and Responsibilities

| **Role (example title)** | **Responsibilities** | **Example holder** |
| --- | --- | --- |
| Data Requester (Program Analyst) | Completes the Data Request Form; defines analysis objectives; conducts analysis per §6. | J. Habimana, TB Program Analyst (example) |
| Data Custodian (HMIS Manager) | Approves/releases datasets within 10 working days; logs all releases; maintains the master data dictionary. | A. Uwase, HMIS Manager (example) |
| District Data Manager | Submits complete monthly reports by the 15th; resolves quality flags within 5 working days. | District Data Managers, all 12 districts (example) |
| Senior Reviewer (Head of M&E) | Reviews methods and findings; chairs the validation meeting; signs off the report. | Dr. P. Nkurunziza, Head of M&E Unit (example) |
| Approving Authority | Gives final approval for external publication. | Director General of Health Services (example) |

# 4. Procedure for Requesting Surveillance Data

Step-by-step (example timeline in working days):

1. Step 1 — Define the need. The Data Requester drafts 2–4 analysis objectives and the decisions they will inform (use the Analysis-Objectives Worksheet).
1. Step 2 — Complete the Data Request Form (fields below) and submit to the Data Custodian by email with the Head of M&E in copy.
1. Step 3 — Custodian review (within 5 working days). The Custodian confirms availability, checks confidentiality requirements, and either approves or requests clarification.
1. Step 4 — Data release (within 10 working days of approval). Data are shared as a password-protected file with a data dictionary; the release is logged in the Data Release Register (date, requester, dataset version).
1. Step 5 — Confirm receipt. The Requester verifies record counts against the release note and signs the receipt log within 2 working days.
## Example Data Request Form — required fields:

| **Field** | **Example entry** |
| --- | --- |
| Requester name / title / unit | J. Habimana, TB Program Analyst, National TB Program (example) |
| Date of request | 12 January 2027 (example) |
| Dataset requested | National TB register extract, notified cases 2021–2025, district-year-sex-age aggregates |
| Purpose / analysis objectives | Annual TB report: (1) describe notification trends by district; (2) assess equity by sex/age; (3) estimate treatment success vs. 90% target |
| Decisions this will inform | 2027–2030 National TB Strategic Plan district prioritization |
| Variables needed | district, year, sex, age_group, tb_cases_notified, treatment cohort fields (see data dictionary) |
| Level of aggregation | Aggregate only — no line-list / no patient identifiers |
| Date needed by | 31 January 2027 (example) |
| Intended outputs | Annual TB surveillance report (internal + public summary) |
| Data storage & confidentiality | Password-protected drive; access limited to analysis team; per SOP-DATA-002 |

# 5. Data-Quality Checks (on receipt, before any analysis)

Run every check below and log results in the Data-Quality Log. Resolve all flags before analysis:

- Completeness: % of expected district-month reports received; list missing district-months (example finding: Riverside district mortality reports incomplete 2021–2025 — exclude Riverside from mortality analysis and document it).
- Timeliness: % of reports received by the 15th of the following month; national standard ≥ 80%.
- Validity: values within allowed ranges (e.g., treatment_success_count ≤ treatment_cohort_size; notification_rate_per_100k ≥ 0); dates valid.
- Consistency: totals match across tables (district sums = national total); no duplicate record_ids; trends checked for implausible jumps (e.g., Westbrook's rise was verified against source registers before acceptance as a real finding).
- Missing data: quantify missing sex/age fields (<1% in example); decide and document exclusion rules.
- Document every limitation that survives these checks in the report's Methods section — never silently drop problem data.
# 6. Analysis Steps

- Work from a read-only copy of the released file; never edit the original extract.
- Build the analysis in a single workbook with separate sheets: 00_README (objectives, version), 01_Raw, 02_Clean, 03_Analysis, 04_Tables_Figures.
- Calculate indicators exactly per the data dictionary definitions (e.g., notification rate = cases ÷ mid-year population × 100,000).
- Disaggregate every key indicator by sex, age group, and district as a minimum equity check.
- A second analyst independently re-runs the key tables; discrepancies are resolved and logged before drafting.
- Save versions as v0.1, v0.2 …; v1.0 is the version that goes to review (see §8).
# 7. Report Production Timeline (example: annual TB report)

| **Week (example)** | **Activity** | **Owner (example)** |
| --- | --- | --- |
| Week 1–2 (Jan) | Data request approved; extract received; quality checks completed | Analyst + HMIS Manager |
| Week 3–5 (Jan–Feb) | Analysis; second-analyst verification | Analyst; peer reviewer |
| Week 6–7 (Feb) | Draft report (IMRAD) with tables/figures | Analyst |
| Week 8 (Feb) | Internal validation meeting; findings checked with program staff | Head of M&E (chair) |
| Week 9 (Mar) | Revisions; senior review and sign-off (§9) | Analyst; Senior Reviewer |
| Week 10 (Mar) | Final approval; publication/dissemination | Approving Authority |

* **NOTE (template guidance):** **Adapt the weeks to your reporting cycle; keep the sequence: quality check → analysis → verification → draft → validation → sign-off.*

# 8. Version Control

- File naming: <ReportShortName>_v<major>.<minor>_<YYYYMMDD>_<initials>. Example: TB_AnnualReport_v1.0_20270315_JH.docx (example).
- v1.0 = first version sent for formal review; only the Approving Authority's signed version becomes v2.0 FINAL.
- Maintain a version history table on the report's cover page: version, date, author, changes.
- Archive superseded versions in a dedicated folder; never delete them — they are the audit trail.
# 9. Review and Approval Sign-Off

No report leaves the institution without the signatures below (example holders — replace with real names/titles):

| **Role** | **Name (example)** | **Title (example)** | **Signature** | **Date** |
| --- | --- | --- | --- | --- |
| Prepared by | J. Habimana | TB Program Analyst |  |  |
| Verified by (2nd analyst) | S. Mukamana | M&E Officer |  |  |
| Reviewed by | Dr. P. Nkurunziza | Head of M&E Unit |  |  |
| Approved by | [Name] | Director General of Health Services |  |  |

* **NOTE (template guidance):** **Electronic signatures are acceptable where institutional policy allows; record the approval email in the file.*

# 10. Related Documents

- Report-Template_IMRAD.docx (this Templates Pack)
- Data-Dictionary-Template.xlsx (this Templates Pack)
- SOP-DATA-002 Data Privacy and Confidentiality (example reference — link your equivalent)
- Analysis-Objectives-Worksheet.docx (this Templates Pack)

*Data for Health (D4H) Initiative  •  Bloomberg Philanthropies  •  CDC Foundation*
