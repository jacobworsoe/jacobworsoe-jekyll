# WordPress export scripts

Run these scripts against your live WordPress site to export content and comments into the Jekyll site.

## Prerequisites

- Node.js (for the JavaScript scripts)
- WordPress site with REST API enabled (default at `https://yoursite.com/wp-json/wp/v2/`)

## Export posts (and pages)

**Option A: WordPress REST API (Node script)**

```bash
cd scripts
npm install
node export-wp-posts.js --url=https://www.jacobworsoe.dk
```

This fetches all posts (and optionally pages) and writes Markdown files to `../_posts/` with front matter (`title`, `date`, `categories`, `slug`, etc.). Adjust `--url` to your WordPress URL.

**Option B: Jekyll WordPress importer (WXR)**

1. In WordPress: Tools → Export → All content (or Posts). Download the WXR file.
2. Install the importer: `gem install jekyll-import`
3. Run (from repo root):
   ```bash
   ruby -rubygems -e 'require "jekyll-import"; JekyllImport::Importers::WordPress.run({"source" => "path/to/export.xml"})'
   ```
4. Move generated files from `_posts/` if needed and add `slug` to front matter from the post slug in the WXR.

## Export comments

```bash
node export-wp-comments.js --url=https://www.jacobworsoe.dk
```

Requires WordPress REST API with comments endpoint (public or with auth). Writes `../_data/comments.yml` keyed by post slug. If your API does not expose comments publicly, use Application Passwords or export comments from the database/WXR and convert with a small script.

## Post slug and comments key

Jekyll post layout expects a `slug` in front matter (used to look up comments in `site.data.comments[slug]`). The export-wp-posts.js script sets `slug` from the WordPress post slug. Ensure your WXR importer or manual exports also set `slug` so comments match.
