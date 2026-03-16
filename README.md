# Jacob Worsøe – Jekyll site

Static site generated from the WordPress theme (jacobworsoe.dk). Host on GitHub Pages or any static host.

## Setup

1. **Ruby / Jekyll**
   ```bash
   bundle install
   bundle exec jekyll serve
   ```
   Site: http://localhost:4000

2. **Assets (CSS/JS from original theme)**
   ```bash
   npm install
   npm run build
   ```
   This builds `assets/css/` and `assets/js/` from the copied SCSS/JS.

3. **Content from WordPress**
   - Export posts: use `scripts/export-wp-posts.js` (Node, against WP REST API) or Jekyll’s wordpress importer (WXR). See `scripts/README.md`.
   - Export comments: use `scripts/export-wp-comments.js` to generate `_data/comments.yml`.

## Deploy to GitHub Pages

1. Create a **new** GitHub repository (e.g. `jacobworsoe.github.io` or `jacobworsoe-jekyll`). Do not use the existing WordPress theme repo.
2. Copy the **contents** of this folder (`jekyll-site`) into the new repo (so that `_config.yml`, `_layouts/`, etc. are at the repo root).
3. Push to the new repo.
4. In the repo: **Settings → Pages → Build and deployment**: Source = **GitHub Actions**.
5. The included workflow (`.github/workflows/jekyll.yml`) will build and deploy on push to `main` or `master`.
6. Optional: set a custom domain (e.g. jacobworsoe.dk) under Pages settings.
