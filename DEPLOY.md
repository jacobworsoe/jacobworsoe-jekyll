# Deploy and test

## Local build (optional)

With Ruby and Bundler installed:

```bash
bundle install
bundle exec jekyll serve
```

With Node installed (for full CSS/JS from the original theme):

```bash
npm install
npm run build
```

Then open http://localhost:4000 and check:

- Homepage lists posts; year headings and links work.
- Single post: title, date, content, word-count script, and comments block (if `_data/comments.yml` has entries for that post slug).
- Sitemap at `/sitemap/`.
- GTM and dataLayer: open DevTools → Network and Console; confirm `dataLayer` and GTM script load. Tracking (content-as-ecommerce, link clicks) will fire when the full JS bundle is built (`npm run build`).

## GitHub Pages

1. Create a new repository. Copy the **contents** of `jekyll-site` into it (so the repo root has `_config.yml`, `_layouts/`, etc.).
2. Push to `main` or `master`.
3. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
4. The workflow `.github/workflows/jekyll.yml` builds assets (npm), builds Jekyll (bundle), and deploys `_site` to Pages.
5. Optional: Custom domain under Pages settings.

## After first WordPress export

1. Run `scripts/export-wp-posts.js` (and optionally export pages) to populate `_posts/`.
2. Run `scripts/export-wp-comments.js` to populate `_data/comments.yml`.
3. Rebuild and deploy.
