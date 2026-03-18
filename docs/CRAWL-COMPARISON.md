# Crawl comparison: WordPress vs Jekyll (GitHub Pages)

*Historical reference: migration is complete; this doc was used to align Jekyll with the live WordPress site.*

**Compared:** [https://www.jacobworsoe.dk/](https://www.jacobworsoe.dk/) (WordPress) vs [https://jacobworsoe.github.io/jacobworsoe-jekyll/](https://jacobworsoe.github.io/jacobworsoe-jekyll/) (Jekyll).

---

## 1. Page title

| | WordPress | Jekyll (GitHub Pages) |
|---|-----------|------------------------|
| **Homepage** | `jacobworsoe.dk \| – only differences that are significant are different, otherwise it's just random…` | `Home \| Jacob Worsøe Home \| Jacob Worsøe` (duplicate) |

**Issue:** Jekyll has a duplicate title because both a manual `<title>` in `_includes/head.html` and the `{% seo %}` tag (jekyll-seo-tag) output a title.  
**Fix:** Use only one source for the title (e.g. remove the manual `<title>` and let `{% seo %}` handle it, or keep manual and avoid duplicate from seo).

---

## 2. Date format

| | WordPress | Jekyll |
|---|-----------|--------|
| **Example** | `11. jan 2022`, `12. aug 2021` (lowercase month, Danish) | `11. Jan 2022`, `12. Aug 2021` (capitalized month, `%b` = English abbrev) |

**Issue:** Jekyll uses `{{ post.date \| date: '%d. %b %Y' }}`, which gives English abbreviated months with capital letter. WordPress uses Danish lowercase (e.g. jan, aug).  
**Fix:** Use a locale-aware format if possible (e.g. `date: '%d. %b %Y', 'da'` where supported), or a custom format / Danish month names so output matches WordPress style.

---

## 3. Post list (homepage)

- **WordPress:** 48 posts, from 2022 down to 2009. Includes e.g. “Case: Overvåg dit brand og scor nemme links”, “Case: Sådan øgede vi vores e-mail liste med 217%…”, “Tag Manager Quick Tip: Gem dit Analytics ID i en makro”.
- **Jekyll repo:** Also has 48 posts in `_posts/`, including the same three. If the live GitHub Pages list showed fewer posts or a “2026” block with empty titles, that is likely an older/cached build; a fresh deploy from current `main` should list all 48.

---

## 4. Footer / job title

| | WordPress | Jekyll |
|---|-----------|--------|
| **Role** | Senior Director, Measurement hos s360 | Head of Measurement & Attribution hos s360 |
| **Tagline** | Analytics ninja og datanørd (in bullet) | Missing in fetched content |

**Note:** The Jekyll footer in the repo includes “Analytics ninja og datanørd” in the description; if it’s missing on the live site, check `_includes/footer.html` and the deployed branch.

---

## 5. Small content differences

- **WordPress:** “10 fede **WordPress** plugins” (capital P).  
- **Jekyll:** “10 fede **Wordpress** plugins” (lowercase p).  
  Fix in the post’s front matter or body if you want consistency.

- **WordPress:** “HDMI kabel **–** Skal det virkelig koste…” (en dash).  
- **Jekyll:** “HDMI kabel **-** Skal det…” (hyphen).  
  Cosmetic; can normalize in the Markdown source.

---

## 6. URL structure

- Jekyll is now aligned with WordPress **Day and name** permalinks: `/:year/:month/:day/:title/` (e.g. `/2022/01/11/kan-browser-fingerprinting-erstatte-cookies/`).
- `_config.yml` has `permalink: /:year/:month/:day/:title/`. For project Pages, `baseurl` is set in CI.

---

## 7. Summary

| Item | Status |
|------|--------|
| Post count (48) | Same in repo; ensure latest build is deployed. |
| Page title | Duplicate on Jekyll → remove one title source. |
| Date format | Jekyll uses English-style capitalized months → align with Danish if desired. |
| Footer role/tagline | Align text and ensure footer include is deployed. |
| Spelling / punctuation | Optional: “Wordpress” → “WordPress”, dash consistency. |

Fixing the duplicate title in `_includes/head.html` (let `{% seo %}` set the title) is recommended so the Jekyll site matches intended behaviour and avoids duplicate “Home | Jacob Worsøe” in the tab.
