#!/usr/bin/env node
/**
 * Export WordPress comments to Jekyll _data/comments.yml via REST API.
 * Comments are keyed by post slug (resolved from post ID).
 * Usage: node export-wp-comments.js --url=https://www.jacobworsoe.dk
 */
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const urlArg = args.find(a => a.startsWith('--url='));
const baseUrl = urlArg ? urlArg.replace('--url=', '').replace(/\/$/, '') : 'https://www.jacobworsoe.dk';

const apiBase = `${baseUrl}/wp-json/wp/v2`;
const dataDir = path.join(__dirname, '..', '_data');
const commentsPath = path.join(dataDir, 'comments.yml');

if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

async function fetchAll(endpoint, params = {}) {
  let all = [];
  let page = 1;
  let totalPages = 1;
  do {
    const q = new URLSearchParams({ per_page: 100, page, ...params });
    const res = await fetch(`${apiBase}/${endpoint}?${q}`);
    if (!res.ok) throw new Error(`${endpoint} ${res.status}: ${await res.text()}`);
    const data = await res.json();
    totalPages = parseInt(res.headers.get('x-wp-totalpages') || '1', 10);
    all = all.concat(data);
    page++;
  } while (page <= totalPages);
  return all;
}

function escapeYaml(str) {
  if (str == null) return '""';
  const s = String(str);
  if (s.includes('\n')) return `|\n${s.split('\n').map(l => '  ' + l).join('\n')}`;
  if (s.includes('"') || s.includes(':') || s.includes('#')) return `"${s.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
  return `"${s}"`;
}

function formatCommentDate(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  const day = String(d.getDate()).padStart(2, '0');
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const year = d.getFullYear();
  const h = String(d.getHours()).padStart(2, '0');
  const min = String(d.getMinutes()).padStart(2, '0');
  return `${day}/${month}-${year} - ${h}:${min}`;
}

async function main() {
  console.log('Fetching posts for slug map...');
  const posts = await fetchAll('posts');
  const idToSlug = {};
  posts.forEach(p => { idToSlug[p.id] = p.slug; });

  console.log('Fetching comments...');
  const comments = await fetchAll('comments');
  console.log('Fetched', comments.length, 'comments');

  const bySlug = {};
  for (const c of comments) {
    const postId = c.post;
    const slug = idToSlug[postId];
    if (!slug) continue;
    if (!bySlug[slug]) bySlug[slug] = [];
    bySlug[slug].push({
      author: c.author_name || '',
      date: formatCommentDate(c.date),
      content: (c.content?.rendered || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').replace(/\r\n/g, '\n').trim(),
      avatar_url: c.author_avatar_urls?.['96'] || c.author_avatar_urls?.['48'] || '',
      author_url: c.author_url || '',
    });
  }

  const lines = ['# WordPress comments (keyed by post slug)', ''];
  for (const [slug, list] of Object.entries(bySlug).sort()) {
    lines.push(`${slug}:`);
    for (const item of list) {
      lines.push(`  - author: ${escapeYaml(item.author)}`);
      lines.push(`    date: ${escapeYaml(item.date)}`);
      lines.push(`    content: ${escapeYaml(item.content)}`);
      lines.push(`    avatar_url: ${escapeYaml(item.avatar_url)}`);
      lines.push(`    author_url: ${escapeYaml(item.author_url)}`);
    }
    lines.push('');
  }

  fs.writeFileSync(commentsPath, lines.join('\n'), 'utf8');
  console.log('Wrote', commentsPath);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
