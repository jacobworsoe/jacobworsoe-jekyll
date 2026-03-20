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
- **`<figure>` + `<figcaption>` in Kramdown:** Avoid **`<a><figure><img … /><figcaption>…</figcaption></figure></a>`**. After a void `<img />`, Kramdown can **end the raw-HTML block** and treat `<figcaption>…</figcaption>` as text, so it appears on the site as escaped `&lt;figcaption&gt;`. Prefer the same structure as WordPress captions: **`<figure><a href="…"><img … /></a><figcaption>…</figcaption></figure>`** (often easiest as **one line** in the Markdown file).
- **Prefer Markdown paragraphs** (blank-line separated text) over a single opening `<p>` that runs to the end of the article—Kramdown will emit valid `<p>` boundaries.
- **`<blockquote>`** (non–Twitter embed): use `<blockquote><p>…</p></blockquote>` like WordPress; `<cite>` may sit inside that `<p>`.
- **Ordered lists:** each `<li>` that uses a paragraph should be `<li><p>…</p></li>`—never `</p></li>` without a matching `<p>`.
- **Twitter oEmbed** (`class="twitter-tweet"`): leave as provided; do not wrap the whole embed in an extra `<p>`.

## WordPress Text editor, `wpautop`, and why imports differ

In the **Classic “Tekst” editor**, authors often mix **explicit HTML** (`<h2>`, `<img>`, `<p class="…">`) with **bare paragraphs** (lines of text with no `<p>` tags). On the live site, WordPress runs **`wpautop`** (usually at priority 10 on `the_content`): it infers block boundaries from blank lines, wraps runs of text in `<p>…</p>`, turns single line breaks into `<br />` in some cases, and tries not to break block tags.

**Jekyll does not run `wpautop`.** The same source is parsed by **Kramdown** plus your mix of raw HTML. That changes the DOM in subtle ways:

| Pattern in DB / Text editor | Typical WordPress output | Risk in Jekyll without adjustment |
|----------------------------|--------------------------|-----------------------------------|
| `<img … />` and the **next line** is body copy (no blank line) | `wpautop` tends to keep the image outside or split blocks so the paragraph is separate | Kramdown may emit **one `<p>`** wrapping `<img>` and the following sentence → bad HTML5 / wrong semantics (see rule above: **add a blank line** after the image). Same idea for **`<div>…<img>…</div>`** before prose. |
| `<h2>…</h2>` then **text on the next line** (no `<p>`) | Opening `<p>` is usually inserted before that text | Kramdown often still produces a **separate** following `<p>` for that line, so this pattern is **less** prone to the “img-in-`p`” bug—but spacing and `<br />` behavior still won’t match WP exactly. |
| Whole stanzas separated by **single** newlines only | Often collapsed / merged by `wpautop` depending on context | In Markdown, **paragraphs need a blank line**; a single newline can merge lines or behave differently than on WP. Prefer explicit blank lines between paragraphs in the migrated file. |
| `<strong>NB:</strong> Long run of text…` as one line (no wrapping `<p>`) | Wrapped in `<p>` on output | Usually becomes a normal Markdown/HTML paragraph in Jekyll; watch for **missing blank line** before the next block element. |
| Shortcodes (`[caption]…[/caption]`, etc.) | Expanded by WordPress | Must be **converted in export** to HTML/Liquid; leftover shortcodes are broken in Jekyll. This repo’s MySQL export **rewrites** `[caption]` → `<figure>` (see export script docs). |
| `<!--more-->` | Defines teaser | In Jekyll, use **`excerpt_separator`** in front matter or excerpts; the comment alone does nothing unless your layout uses it. |
| Shortcodes / embeds as URLs only | oEmbed expands to HTML | Ensure the **exported HTML** (or equivalent) is in the Markdown file. |
| Legacy `wp-content` URLs in `src`/`href` | Worked on WP host | Violates this project’s **no runtime WordPress** rule—must be `assets/images/…` + `relative_url` (export handles many cases). |

**Practical takeaway:** Treat “valid on WordPress after filters” as **not** guaranteed valid or equivalent in Jekyll. After migration, prefer **explicit structure** (blank lines, real `<p>` where needed, `<figure>` for captioned images) and run **`python scripts/check_post_html5.py`** on changes.

## WordPress import vs. Jekyll-first editing

Full MySQL export is useful for **initial migration**, but WordPress `post_content` often mixes invalid nesting (unclosed `<p>`, stray `</p>` in lists). **Re-importing overwrites fixes** in this repo.

**Recommendation:** treat Jekyll `_posts/` as the source of truth; run `python scripts/export_all.py` only when you intentionally refresh from the DB and are prepared to re-apply structural fixes (or diff and merge). Prefer editing Markdown/HTML here and using `scripts/check_post_html5.py` before commit.

## Check script

```bash
python scripts/check_post_html5.py
```

Exits with code `1` if any post body appears to have a `<p>` that contains a block-level tag before its closing `</p>` (heuristic; code blocks and `<pre>` are ignored).
