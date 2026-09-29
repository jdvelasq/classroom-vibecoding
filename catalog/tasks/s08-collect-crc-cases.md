# S08 — Collect Cases from CRC Press

Read `AGENTS.md` and
[`_collect-publisher-cases.md`](_collect-publisher-cases.md) before execution.

## Source scope

Treat **CRC Press** as the publisher source and each identifiable CRC book as a
distinct subsource. Treat the **Chapman & Hall/CRC** imprint as CRC Press for
catalog-path purposes; do not create a parallel publisher tree merely because a
book uses that imprint. Inspect `catalog/crc-press/` first, then use first-party
book pages and documented companion materials to find absent books and recent
editions.

## Output

Create only verified, nonduplicate records at:

`catalog/crc-press/<book-slug>/<case-slug>.yaml`

Set `book_source.publisher: CRC Press` and preserve the displayed imprint in a
separate `book_source.imprint` field when applicable.
