# Post content and HTML5 structure

## Rules of thumb

- **Code samples with angle brackets (`<…>`) in posts:** Do not use raw `<pre><code class="language-…">` followed immediately by `<` in Markdown. Kramdown parses those as real HTML. Use a **fenced block** (` ```html `, ` ```php `, ` ```javascript `, etc.) so the source is escaped and Prism still highlights it. This applies to **`language-html`**, mixed **PHP + `<style>` / `<a>`**, and **`<script>`…`</script>`** samples labeled as JavaScript.

  ````markdown
  ```html
  <div>...</div>
  ```
  ````

- **Liquid in samples:** If a fence must show `{%` / `{{`, either keep **HTML entities** (`&#123;` …) as in the original export, or wrap with `{% raw %}…{% endraw %}`—otherwise Jekyll may execute Liquid inside the Markdown file.

- **`<p>` is only for phrasing content.** Close `</p>` before block-level siblings: headings (`<h1>`–`<h6>`), `<figure>`, `<blockquote>`, `<pre>`, lists (`<ul>`/`<ol>` when outer), `<div>`, etc.
- **Raw `<img>` (or `<div>…<img>…</div>`) in Markdown:** Put a **blank line** after the image block before normal paragraph text. If the image line is glued to the next prose line, Kramdown often emits one `<p>` that wraps both the image and the text, which is invalid / unreliable in HTML5.
- **Prefer Markdown paragraphs** (blank-line separated text) over a single opening `<p>` that runs to the end of the article—Kramdown will emit valid `<p>` boundaries.
- **`<blockquote>`** (non–Twitter embed): use `<blockquote><p>…</p></blockquote>` like WordPress; `<cite>` may sit inside that `<p>`.
- **Ordered lists:** each `<li>` that uses a paragraph should be `<li><p>…</p></li>`—never `</p></li>` without a matching `<p>`.
- **Twitter oEmbed** (`class="twitter-tweet"`): leave as provided; do not wrap the whole embed in an extra `<p>`.

## WordPress import vs. Jekyll-first editing

Full MySQL export is useful for **initial migration**, but WordPress `post_content` often mixes invalid nesting (unclosed `<p>`, stray `</p>` in lists). **Re-importing overwrites fixes** in this repo.

**Recommendation:** treat Jekyll `_posts/` as the source of truth; run `python scripts/export_all.py` only when you intentionally refresh from the DB and are prepared to re-apply structural fixes (or diff and merge). Prefer editing Markdown/HTML here and using `scripts/check_post_html5.py` before commit.

## Check script

```bash
python scripts/check_post_html5.py
```

Exits with code `1` if any post body appears to have a `<p>` that contains a block-level tag before its closing `</p>` (heuristic; code blocks and `<pre>` are ignored).
