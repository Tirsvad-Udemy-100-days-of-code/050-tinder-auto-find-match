# Stakeholder Analysis: Tinder auto find match

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This analysis names the people and parties who have a stake in Tinder auto find match, rates their power and interest, records their concerns in business language with a FURPS+ attribute, and links the concerns to the objectives of the Business Case ([BC-001]). It follows the power/interest grid and gives each stakeholder a stable ID that other documents cite for owners and reviewers. FURPS+ stands for functionality, usability, reliability, performance and supportability, plus design, implementation, interface and legal constraints.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Product Owner, learner and developer | Tirsvad | HIGH | HIGH | Manage Closely | A working exercise that shows what was learned |
| S02 | Jens Tirsvad Nielsen | Reviewer and approver (merges the pull request) | Tirsvad | HIGH | HIGH | Manage Closely | Every document is checked before it is accepted |
| S03 | Learners and portfolio visitors | Readers of the repository and wiki | Public | LOW | MEDIUM | Keep Informed | Clear instructions in their own language |
| S04 | Udemy course instructor | Author of the exercise | Udemy | LOW | LOW | Monitor | The solution follows the course exercise |

## Power/Interest Classification Rationale

- **Manage Closely (S01, S02):** the same person decides scope, writes the code and approves the documents, so power and interest are both high. The roles are kept apart as S01 and S02 so that author and reviewer are never the same ID.
- **Keep Informed (S03):** visitors cannot change the project but depend on its documentation; they are informed through the README and the wiki.
- **Monitor (S04):** the course author does not follow this repository; the project only watches the course for changes to the exercise.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The program keeps working and its tests keep passing | Functionality |
| CN-002 | S02 | Each document has a review record and a verdict before it is accepted | Supportability |
| CN-003 | S03 | The instructions to install and run the program are clear and available in English, Danish and Malay | Usability |
| CN-004 | S03 | The licence of the code is clear | Legal (the `+` of FURPS+) |
| CN-005 | S04 | The program stays faithful to the course exercise | Functionality |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| C-01 | Pull request on the git host | Once, at the end of the milestone | Documents, wiki and review records to read | [MIL-001] |
| C-02 | End-of-run summary in chat | Once per project run | Pull requests, review verdicts and stand-in decisions | [MIL-001] |
| C-03 | README and wiki | Continuous | Purpose, setup and run instructions | [MIL-001] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The author and the reviewer are the same person, so the review is not independent | S01, S02 | The AI assistant acts as stand-in reviewer, every record says `Mode: autonomous, not independent`, and the summary lists each stand-in decision so that S02 can challenge it |
| Speed (a short baseline) against completeness (full design documents) | S01, S02 | The scope excludes use cases and design artifacts; they are added in a later milestone only if the exercise changes |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1 in [BC-001] |
| S02 | CN-002 | O2 in [BC-001] |
| S03 | CN-003 | O3 in [BC-001] |
| S03 | CN-004 | O4 in [BC-001] |
| S04 | CN-005 | O1 in [BC-001] |

## Sign-Off

Accepted on the `Go` verdict of the review record of this document, by the AI as stand-in for S02 (autonomous mode, not independent). The Product Owner (S01) accepted the plan and the stand-in rule in chat when starting the run.

---

[BC-001]: ./business-case.md
[MIL-001]: ./milestones/mil-001-baseline.md
