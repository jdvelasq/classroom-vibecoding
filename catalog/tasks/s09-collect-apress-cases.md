# S09 — Collect Cases from Apress

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **Apress** as the publisher source and each identifiable Apress book as a
distinct subsource. Inspect `catalog/apress/` first, then use first-party Apress
book pages and documented book-specific repositories or author materials to
find absent books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/apress/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: Apress`. Separate a repository's code license from
the provenance and terms of every dataset it contains or references.
