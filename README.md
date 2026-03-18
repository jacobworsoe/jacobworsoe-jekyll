# Jacob Worsøe – Jekyll site

Static site (former WordPress content). Deploy on GitHub Pages or any static host.

**Do not** link images, favicon, or other assets to the old WordPress host — mirror files under `assets/images/`. See **`docs/MIGRATION.md`** and **`.cursor/rules/jekyll-no-wordpress-hosting.mdc`**.

## Setup

1. **Ruby / Jekyll**
   ```bash
   bundle install
   bundle exec jekyll serve
   ```
   Site: http://localhost:4000

2. **Assets (CSS/JS)**
   ```bash
   npm install
   npm run build
   ```

3. **Content from WordPress (MySQL, until cutover)**  
   - `python scripts/export_all.py` or `scripts/build.ps1` / `build.bat`  
   - Credentials: `scripts/.mysql-credentials` (see `scripts/README.md`)

## Deploy (GitHub Pages)

Workflow **`.github/workflows/jekyll.yml`**: `npm run build` + `bundle exec jekyll build` on push to `main` / `master`.
