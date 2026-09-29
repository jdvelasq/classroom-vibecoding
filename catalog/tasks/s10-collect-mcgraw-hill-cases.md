# S10 — Collect Cases from McGraw-Hill

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **McGraw-Hill** as the publisher source and each identifiable book as a
distinct subsource. Inspect `catalog/mcgraw-hill/` first, then use first-party
book pages and documented book-specific repositories or author materials to
find absent books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/mcgraw-hill/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: McGraw-Hill`. Verify that a case's dataset is
book-specific or independently traceable rather than simply bundled in a
third-party technical package.
