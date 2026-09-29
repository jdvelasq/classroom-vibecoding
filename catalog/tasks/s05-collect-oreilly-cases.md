# S05 — Collect Cases from O'Reilly

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **O'Reilly Media** as the publisher source and each identifiable O'Reilly
book as a distinct subsource. Inspect `catalog/oreilly/` first, then use
first-party O'Reilly book pages and documented book-specific repositories or
author materials to find absent books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/oreilly/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: O'Reilly Media`. Do not assume an author repository
or a generic library establishes data provenance; document the original data
provider and terms independently.
