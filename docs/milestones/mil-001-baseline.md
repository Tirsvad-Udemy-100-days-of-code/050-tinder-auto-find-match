# MIL-001: Baseline and framework alignment

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [261dc82] |

---

## Purpose

This gate decides whether Tinder auto find match has a complete, reviewed baseline: documents, wiki, README and metadata, merged to the default branch with a green build.

## Deliverable

A merged pull request that holds: the accepted Business Case, Stakeholder Analysis, Project Plan and this milestone with their review records; the traceability matrix; the wiki in English, Danish and Malay; the README in the framework template; `pyproject.toml` with complete licence metadata; the framework release adopted by the project; and the end-to-end `Dockerfile` with a user without root rights.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001 and MIL-001 each have an `Accepted` Version History row and a review record with the verdict `Go` | All four | Any missing or `Go-with-conditions` |
| 2 | `python -m pytest` runs (4 unit tests with a fake driver; they open no browser and contact no site) | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Getting-Started, Lecture-Steps, Modernisation and Project-Documents in en, da and ms | 15 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license` and `license-files` | Both set | Either missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |
| 7 | `tests/e2e/Dockerfile` sets a `USER` that is not `root` before its `ENTRYPOINT`, and the OpenGrep check of the pull request passes without a suppression | Both | Either fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | This is the first and only gateway of the baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | Criteria 2, 6 and 7 |
| O2 | Criteria 1 and 4 |
| O3 | Criterion 3 |
| O4 | Criterion 5 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills, hooks and `.editorconfig`, and track `.env.example` so the project follows the same rules as the other projects of the portfolio. | No | |
| 2 | Write and review the baseline documents | Create the Business Case, Stakeholder Analysis, Project Plan, this milestone and the traceability matrix, review each against its QC checklist and accept them on a `Go`, so the plan-first gate is met. | No | |
| 3 | Publish the wiki in English, Danish and Malay | Split the existing Home pages into Home, Lecture-Steps and Modernisation, add Getting-Started and Project-Documents and write the sidebar in `docs/wiki/`, so a visitor can learn what the exercise is and how to run it in their own language. | No | |
| 4 | Restore the README to the framework template | Bring back the original text of the README inside the template's sections and the document appendix, with the project links, so the README is complete and checkable. | No | |
| 5 | Add licence metadata to pyproject.toml | Set `license-files`, the authors and the project URLs next to the existing licence expression so package tools can read the licence. | No | |
| 6 | Run the end-to-end container as a user without root rights | Add a user with the id 1000 and a `USER` line before the `ENTRYPOINT` in `tests/e2e/Dockerfile`, so that the OpenGrep rule `missing-user` no longer matches. The scan is not suppressed. The program, the mock site and the paths of the screenshots are unchanged. The image is not built or run in this milestone (that needs Docker and a browser). | No | BC-001 objective O1 |

---

[BC-001]: ../business-case.md
[261dc82]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/050-tinder-auto-find-match/commit/261dc823b7e96a855fe22f2ada6fc9ee0ea6390a
