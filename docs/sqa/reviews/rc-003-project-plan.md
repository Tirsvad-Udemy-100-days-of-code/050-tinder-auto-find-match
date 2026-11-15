# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date, the end date (2026-11-23) and the one-week constraint of BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists MIL-001 once, with its document, decision date and owner; MIL-001 exists and lists the same gateway. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | The decision date 2026-11-23 lies in the window and equals the target date of MIL-001. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps all six in-scope items of BC-001 to MIL-001, and MIL-001 has no item outside the Business Case. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | There is one gateway with no predecessor, so the dependencies are acyclic and match the schedule. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go moves the end date and that S01 decides the new date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 and reviewer S02 are stakeholder IDs of SA-001; no governance document exists in this project, so there is no RACI to contradict. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source document; no baseline was changed, so there is no change to record. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for two risks; the first traces to the BC-001 risks on drift and on the wiki publication. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues lists two items, none contradicts the rest of the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable in the schedule names the same items as the Deliverable of MIL-001. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none (documentation and technical tasks)`. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bar and the decision marker use the same dates as the schedule table; the single-gateway chain agrees with the dependency view. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | The Milestone column links the milestone of the git host, or says it is not yet synced. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History has one row. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (DICT) exists in this project, and a dictionary is out of scope. The terms exercise, course, learner and visitor are used in one meaning each, with no synonym. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version of the document: no earlier accepted version exists, so there is no change of language or domain to review. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations such as SQA, QC, CI and FURPS+ are spelled out where they are first used. |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes; the document is accepted.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S02 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
