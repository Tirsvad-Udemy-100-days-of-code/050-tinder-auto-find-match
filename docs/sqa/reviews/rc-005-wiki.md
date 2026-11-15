# Review Record: Wiki against QC-WIKI-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-005 |
| CrossReference | [WIKI], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial review record; verdict Go-with-conditions (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms / education (a wiki is not an artifact with Language and Domain rows)
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | The sidebar starts with the wiki title in bold, then one list of the five English pages with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | The list links Home, Getting-Started, Lecture-Steps, Modernisation and Project-Documents; each of these files exists in docs/wiki/. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | The wiki has no related wiki, so the sidebar has no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | The Languages section is the last section and has one line each for English, Dansk and Bahasa Melayu, linking to Home, Home-da and Home-ms. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand; no generator produces it. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page has the language line at its top. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | The wiki exists in English (the PO language) and in Danish and Malay on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Each English page has a Danish (-da) and a Malay (-ms) page; the three sets are identical. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, the current language in bold and a link to the same page in each other language. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Danish pages end in -da.md and Malay pages in -ms.md; English pages have no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | The code blocks hold commands and file names in English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The host publishes `docs/wiki/` only after the merge; the published wiki is checked then. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No generator or template exists for this wiki, so no layout rule changes. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages and the sidebar are directly in docs/wiki/; no subfolder exists. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion passes except criterion 14, which cannot be checked until the host has published the wiki after the merge; it stays Pending.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar, every page and every link on the published wiki after the merge (QC-WIKI-001 criterion 14) | S02 | 2026-11-23 |

---

[WIKI]: ../../wiki/
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
