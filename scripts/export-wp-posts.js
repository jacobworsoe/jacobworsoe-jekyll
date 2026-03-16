#!/usr/bin/env node
/**
 * Export WordPress posts (and optionally pages) to Jekyll _posts via REST API.
 * Usage: node export-wp-posts.js --url=https://www.jacobworsoe.dk [--pages] [--per-page=100]
 */
const fetch = require('node-fetch');
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const urlArg = args.find(a => a.startsWith('--url='));
const baseUrl = urlArg ? urlArg.replace('--url=', '').replace(/\/$/, '') : 'https://www.jacobworsoe.dk';
const includePages = args.includes('--pages');
const perPage = parseInt(args.find(a => a.startsWith('--per-page='))?.replace('--per-page=', '') || '100', 10);

const apiBase = `${baseUrl}/wp-json/wp/v2`;
const postsDir = path.join(__dirname, '..', '_posts');

if (!fs.existsSync(postsDir)) fs.mkdirSync(postsDir, { recursive: true });

function escapeYaml(str) {
  if (str == null) return '';
  const s = String(str);
  if (s.includes('\n') || s.includes('"') || s.includes(':') || s.includes('#')) return `"${s.replace(/"/g, '\\"')}"`;
  return s;
}

function slugify(s) {
  return (s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

async function fetchAll(endpoint) {
  let all = [];
  let page = 1;
  let totalPages = 1;
  do {
    const res = await fetch(`${apiBase}/${endpoint}?per_page=${perPage}&page=${page}&_embed`);
    if (!res.ok) throw new Error(`${endpoint} ${res.status}: ${await res.text()}`);
    const data = await res.json();
    totalPages = parseInt(res.headers.get('x-wp-totalpages') || '1', 10);
    all = all.concat(data);
    page++;
  } while (page <= totalPages);
  return all;
}

function wpDateToJekyll(d) {
  if (!d) return '';
  const date = new Date(d);
  return date.toISOString().replace('T', ' ').replace(/\.\d{3}Z$/, ' +0000');
}

function mdFromPost(post, isPage = false, categoryNames = {}) {
  const date = new Date(post.date);
  const ymd = date.toISOString().slice(0, 10);
  const slug = (post.slug || slugify(post.title?.rendered || '')).replace(/^\d+-/, '');
  const title = (post.title?.rendered || '').replace(/"/g, '\\"');
  let content = (post.content?.rendered || '')
    .replace(/\r\n/g, '\n')
    .replace(/<!-- \/?wp:.*?-->/g, '');
  const categories = (post.categories || []).map(cid => categoryNames[cid] || cid).filter(Boolean);
  const frontMatter = [
    '---',
    `layout: ${isPage ? 'page' : 'post'}`,
    `title: ${escapeYaml(title)}`,
    `date: ${wpDateToJekyll(post.date)}`,
    `slug: ${slug}`,
    categories.length ? `categories:\n${categories.map(c => `  - ${escapeYaml(c)}`).join('\n')}` : '',
    '---',
  ].filter(Boolean).join('\n');
  return `${frontMatter}\n\n${content}\n`;
}

async function main() {
  console.log('Fetching categories...');
  const cats = await fetchAll('categories');
  const categoryNames = {};
  cats.forEach(c => { categoryNames[c.id] = c.name || c.slug; });

  console.log('Fetching posts from', apiBase);
  const posts = await fetchAll('posts');
  console.log('Fetched', posts.length, 'posts');

  for (const post of posts) {
    const date = new Date(post.date);
    const ymd = date.toISOString().slice(0, 10);
    const slug = (post.slug || slugify(post.title?.rendered || '')).replace(/^\d+-/, '');
    const filename = `${ymd}-${slug}.md`;
    const filepath = path.join(postsDir, filename);
    const body = mdFromPost(post, false, categoryNames);
    fs.writeFileSync(filepath, body, 'utf8');
    console.log('Wrote', filename);
  }

  if (includePages) {
    console.log('Fetching pages...');
    const pages = await fetchAll('pages');
    console.log('Fetched', pages.length, 'pages');
    const pagesDir = path.join(__dirname, '..');
    for (const page of pages) {
      const slug = page.slug || slugify(page.title?.rendered || 'page');
      const filename = `${slug}.md`;
      const filepath = path.join(pagesDir, filename);
      const body = mdFromPost(page, true, categoryNames);
      fs.writeFileSync(filepath, body, 'utf8');
      console.log('Wrote page', filename);
    }
  }

  console.log('Done.');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
