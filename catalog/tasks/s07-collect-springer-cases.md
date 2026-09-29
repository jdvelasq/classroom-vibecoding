# S07 — Collect Cases from Springer

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **Springer** as the publisher source and each identifiable Springer book
as a distinct subsource. Inspect `catalog/springer/` first, then use first-party
Springer book pages and documented book-specific repositories or author
materials to find absent books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/springer/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: Springer`. A fictional or synthetic business case
may be documented only when its synthetic nature and pedagogical limitation are
explicit; do not present it as real-world data.
