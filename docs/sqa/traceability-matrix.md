# Traceability Matrix: Tinder auto find match

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; created with the review records of the baseline (autonomous, not independent) | [261dc82] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Tinder auto find match so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001] | [RC-003] |
| [MIL-001] | Milestone | en | education | [BC-001], [PP-001] | - | [RC-004] |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-005] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-001] (Go/No-Go criterion 2) | - | - | Covered |
| CN-002 | [MIL-001] (Go/No-Go criterion 1) | - | - | Covered |
| CN-003 | [MIL-001] (Go/No-Go criterion 3) | - | - | Covered |
| CN-004 | [MIL-001] (Go/No-Go criterion 5) | - | - | Covered |
| CN-005 | [MIL-001] (Go/No-Go criterion 2) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

No view, design or test-plan artifact exists yet (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of [MIL-001]. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-milestone-001.md
[RC-005]: ./reviews/rc-005-wiki.md
[261dc82]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/050-tinder-auto-find-match/commit/261dc823b7e96a855fe22f2ada6fc9ee0ea6390a
