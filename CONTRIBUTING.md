# Contributing

Thanks for helping keep this Awesome list accurate.

## Rules (hard)

1. **Every paper entry MUST have a valid arXiv id** (`YYMM.NNNNN` or older `archive/NNNNNNN`).
2. **Never invent** title, authors, year, venue, or links. Verify via the arXiv API before adding:
   ```bash
   curl -sL "https://export.arxiv.org/api/query?id_list=XXXX.XXXXX"
   # or
   make fetch
   ```
3. If the API returns no entry, a wrong title, or a different domain, **omit** the id.
4. `code_url` is optional and must point to an official / author-linked repository (prefer URLs cited in the paper abstract/comment). Use `null` when unsure.
5. Do **not** add TimesNet / Autoformer / iTransformer as standalone entries (keep them in the TSlib toolkit blurb only).
6. Prefer THUML / 金明 / Chronos-family / major TSFMs when curating new additions.

## How to add a paper

1. Append an object to `data/papers.json` with at least:
   - `arxiv_id`, `title`, `authors` (list), `year`, `categories` (list), `code_url` (string or null), `notes` (string or null)
2. Suggested `categories` tags: `survey`, `tsfm`, `chronos`, `thuml`, `jin`, `llm4ts`, `multimodal`, `benchmark`, `related`.
3. Run:
   ```bash
   make fetch     # refresh metadata from arXiv over HTTPS
   make validate
   make readme    # regenerate README from data/papers.json
   ```
4. Open a PR with a short note: why this paper belongs, and confirmation that metadata was verified.

## PR checklist

- [ ] arXiv id verified (HTTPS API)
- [ ] Title/authors/year match arXiv
- [ ] Categories chosen appropriately
- [ ] `code_url` verified or left `null`
- [ ] `make validate` passes
- [ ] README regenerated if you edited JSON by hand without `make readme`

## Non-goals

- Padding the list for volume
- Blog-only models without papers (document in README Resources / notes instead — e.g. Chronos-Bolt)
- Pushing to GitHub from CI without maintainer approval
