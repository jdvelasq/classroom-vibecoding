# S11 — Collect Cases from OTexts

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **OTexts** as the publisher source and each identifiable OTexts book as a
distinct subsource. Inspect `catalog/otexts/` first, then use first-party book
pages and documented book-specific repositories or packages to find absent
books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/otexts/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: OTexts`. Open publication does not by itself
establish the terms or original provenance of an included dataset; document both
separately.
