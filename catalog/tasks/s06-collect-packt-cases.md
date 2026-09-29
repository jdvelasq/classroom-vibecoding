# S06 — Collect Cases from Packt

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **Packt** as the publisher source and each identifiable Packt book as a
distinct subsource. Inspect `catalog/packt/` first, then use first-party Packt
book pages and documented book-specific repositories or author materials to
find absent books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/packt/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: Packt`. Do not assume an author repository or a
generic library establishes data provenance; document the original data provider
and terms independently.
