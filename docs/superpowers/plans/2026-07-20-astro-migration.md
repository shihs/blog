# Blog Migration to Astro — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Jekyll (Hyde/Poole) blog at `shihs.github.io/blog` with an Astro site that preserves all 100 post URLs exactly, carries the portfolio's design system (teal accent, mono headings, Inter body, light/dark toggle), and swaps Disqus/lunr.js for Giscus/Pagefind.

**Architecture:** Astro content collections hold the migrated posts. A dynamic route `[year]/[month]/[slug].astro` reproduces the old `/YYYY/MM/title.html` permalinks using an authoritative pre-computed manifest (`scripts/permalink-manifest.json`) rather than re-deriving Jekyll's slugify rules. A sidebar layout (matching the current structural pattern, restyled) wraps every page.

**Tech Stack:** Astro 7, Node 22 (Astro 7 requires Node >=22.12.0; discovered during Task 1 — local dev machine defaulted to Node 20 and needed nvm install 22), gray-matter (front-matter parsing), @astrojs/rss, @astrojs/sitemap, Pagefind (search), Giscus (comments), MathJax (kept via CDN script, unchanged).

## Global Constraints

- Requires Node >=22.12.0 (Astro 7's engine floor). Before running any `npm`/`node`/`astro` command in this worktree, run: `export PATH="$HOME/.nvm/versions/node/v22.23.1/bin:$PATH"` — the machine's default shell Node is 20.18.1, which is too old and will fail with a native-binding MODULE_NOT_FOUND error.
- Post permalinks MUST exactly match `docs/superpowers/specs/permalink-manifest.json` (100 entries, each `{path, url, title, date}`) — this file was generated from a real Jekyll build of the current site and is the source of truth for URLs.
- Site `base` is `/blog/` (deployed at `shihs.github.io/blog`).
- Design tokens (colors, fonts, dark mode) match the already-shipped system: `--accent: #1b7c71` (light) / `#7dd6cf` (dark), `--font-mono: 'MesloLGS NF', 'SFMono-Regular', Menlo, Consolas, monospace`, `--font-sans: 'Inter', 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif`. Full variable set is in Task 3.
- MathJax is kept as-is (CDN script `https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML`) — no math re-authoring.
- Drop entirely: `.travis.yml`, `build.R`, `_source/`, `js/lunr.min.js`, `js/search.js`, `search_data.json`, `public/css/*` (old Jekyll theme CSS).
- Pagination URLs deviate from the old site (`/page2/` etc.) to Astro's native `/2/`, `/3/` — this is a deliberate, documented deviation (pagination pages aren't the kind of URL people bookmark or that search engines index as entry points; post permalinks are the ones preserved exactly).

---

### Task 1: Scaffold the Astro project

**Files:**
- Create: `package.json`
- Create: `astro.config.mjs`
- Create: `tsconfig.json`
- Create: `src/pages/index.astro`
- Modify: none (new project lives at repo root, replacing Jekyll files — Jekyll files are removed in Task 13, not here, so the repo builds both ways until the cutover)

**Interfaces:**
- Produces: a working `npm run build` producing `dist/index.html`

- [ ] **Step 1: Create `package.json`**

```json
{
  "name": "mcshih-blog",
  "type": "module",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "build": "astro build && npx pagefind --site dist && node scripts/migrate-posts.mjs --check",
    "build:site": "astro build",
    "preview": "astro preview",
    "migrate": "node scripts/migrate-posts.mjs"
  },
  "dependencies": {
    "astro": "^7.1.1",
    "@astrojs/rss": "^4.0.19",
    "@astrojs/sitemap": "^3.7.3"
  },
  "devDependencies": {
    "gray-matter": "^4.0.3",
    "pagefind": "^1.5.2"
  }
}
```

- [ ] **Step 2: Install dependencies**

Run: `npm install`
Expected: `node_modules/` created, no errors, `package-lock.json` written.

- [ ] **Step 3: Create `astro.config.mjs`**

```js
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://shihs.github.io',
  base: '/blog',
  trailingSlash: 'never',
  build: {
    format: 'file',
  },
  integrations: [sitemap()],
});
```

- [ ] **Step 4: Create `tsconfig.json`**

```json
{
  "extends": "astro/tsconfigs/strict"
}
```

- [ ] **Step 5: Create a placeholder `src/pages/index.astro`**

```astro
---
---
<html>
  <head><title>M.C. Shih &middot; BLOG</title></head>
  <body><p>Scaffold OK</p></body>
</html>
```

- [ ] **Step 6: Build and verify**

Run: `npm run build:site`
Expected: `dist/index.html` exists and contains `Scaffold OK`.

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json astro.config.mjs tsconfig.json src/pages/index.astro
git commit -m "chore: scaffold Astro project"
```

---

### Task 2: Content collection schema + post migration script

**Files:**
- Create: `src/content.config.ts` (NOT `src/content/config.ts` — Astro 7.1.1 hard-errors on that legacy path with `LegacyContentConfigError`; confirmed by an actual build during execution, not just reading docs)
- Create: `scripts/permalink-manifest.json` (copy of `docs/superpowers/specs/permalink-manifest.json`)
- Create: `scripts/migrate-posts.mjs`
- Create: `src/content/posts/` (populated by running the script)

**Interfaces:**
- Consumes: `_posts/*.md` (Jekyll source, still present in repo at this point), `scripts/permalink-manifest.json`
- Produces: `src/content/posts/<slug>.md` files with front matter `{ title: string, date: Date, categories: string[], slug: string }`; `public/img/` populated from `img/`

- [ ] **Step 1: Copy the permalink manifest into the new project**

```bash
mkdir -p scripts
cp docs/superpowers/specs/permalink-manifest.json scripts/permalink-manifest.json
```

- [ ] **Step 2: Define the content collection schema**

`src/content.config.ts`:

```ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    categories: z.array(z.string()).default([]),
    slug: z.string(),
  }),
});

export const collections = { posts };
```

- [ ] **Step 3: Write the migration script**

`scripts/migrate-posts.mjs`:

```js
import fs from 'node:fs';
import path from 'node:path';
import matter from 'gray-matter';

const ROOT = process.cwd();
const POSTS_DIR = path.join(ROOT, '_posts');
const OUT_DIR = path.join(ROOT, 'src/content/posts');
const MANIFEST_PATH = path.join(ROOT, 'scripts/permalink-manifest.json');
const IMG_SRC = path.join(ROOT, 'img');
const IMG_DEST = path.join(ROOT, 'public/img');

const checkOnly = process.argv.includes('--check');

function loadManifest() {
  const raw = fs.readFileSync(MANIFEST_PATH, 'utf8');
  const entries = JSON.parse(raw);
  const byPath = new Map();
  for (const e of entries) byPath.set(e.path, e);
  return byPath;
}

// "/2016/07/Python-使用python下載gmail附件.html" -> "Python-使用python下載gmail附件"
function slugFromUrl(url) {
  const parts = url.split('/').filter(Boolean); // [year, month, "Title.html"]
  const file = parts[2];
  return file.replace(/\.html$/, '');
}

function normalizeCategories(raw) {
  if (raw == null) return [];
  if (Array.isArray(raw)) return raw.map(String);
  return [String(raw)];
}

function transformBody(body) {
  let out = body;

  // Jekyll {% raw %}/{% endraw %} guards around Jinja/Liquid-lookalike code
  // samples — meaningless outside Jekyll, strip the tags but keep the content.
  out = out.replace(/\{%\s*raw\s*%\}/g, '').replace(/\{%\s*endraw\s*%\}/g, '');

  // Liquid image helper: {{ "/img/posts/x.png" | absolute_url }} -> /blog/img/posts/x.png
  out = out.replace(
    /\{\{\s*"([^"]+)"\s*\|\s*absolute_url\s*\}\}/g,
    (_m, p1) => `/blog${p1}`
  );

  // Image with kramdown width/height IAL:
  // ![alt](src){:height="400px" width="600px"} -> <img src="src" alt="alt" width="600" height="400">
  out = out.replace(
    /!\[([^\]]*)\]\(([^)]+)\)\{:\s*height="(\d+)px"\s*width="(\d+)px"\s*\}/g,
    (_m, alt, src, h, w) => `<img src="${src}" alt="${alt}" width="${w}" height="${h}">`
  );
  out = out.replace(
    /!\[([^\]]*)\]\(([^)]+)\)\{:\s*width="(\d+)%?"\s*heigh(?:t)?="(\d+)%?"\s*\}/g,
    (_m, alt, src, w, h) => `<img src="${src}" alt="${alt}" width="${w}%" height="${h}%">`
  );

  // Link with target=_blank IAL:
  // [text](url){:target="_blank"} -> <a href="url" target="_blank">text</a>
  out = out.replace(
    /\[([^\]]+)\]\(([^)]+)\)\{:\s*target="_blank"\s*\}/g,
    (_m, text, url) => `<a href="${url}" target="_blank">${text}</a>`
  );

  // Any leftover kramdown IAL we didn't specifically handle: drop it.
  out = out.replace(/\{:[^}]*\}/g, '');

  return out;
}

function copyImages() {
  if (checkOnly) return;
  fs.mkdirSync(IMG_DEST, { recursive: true });
  fs.cpSync(IMG_SRC, IMG_DEST, { recursive: true });
}

function migrate() {
  const manifest = loadManifest();
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const files = fs
    .readdirSync(POSTS_DIR)
    .filter((f) => /^\d{4}-\d{2}-\d{2}-.+\.md$/.test(f));

  let migrated = 0;
  const problems = [];

  for (const file of files) {
    const relPath = `_posts/${file}`;
    const entry = manifest.get(relPath);
    if (!entry) {
      problems.push(`No manifest entry for ${relPath}`);
      continue;
    }

    const raw = fs.readFileSync(path.join(POSTS_DIR, file), 'utf8');
    const { data, content } = matter(raw);

    const slug = slugFromUrl(entry.url);
    const frontMatter = {
      title: data.title || entry.title,
      date: entry.date,
      categories: normalizeCategories(data.category ?? data.categories),
      slug,
    };

    const body = transformBody(content);
    const out = matter.stringify(body, frontMatter);

    if (!checkOnly) {
      const outPath = path.join(OUT_DIR, `${slug}.md`);
      fs.writeFileSync(outPath, out, 'utf8');
    }
    migrated++;
  }

  console.log(`Migrated ${migrated}/${files.length} posts.`);
  if (problems.length) {
    console.error('Problems:');
    for (const p of problems) console.error(` - ${p}`);
    process.exitCode = 1;
  }
}

copyImages();
migrate();
```

- [ ] **Step 4: Run the migration**

Run: `node scripts/migrate-posts.mjs`
Expected output: `Migrated 100/100 posts.` with no "Problems:" section.

- [ ] **Step 5: Verify a sample output file**

Run: `cat "src/content/posts/Python-使用python下載gmail附件.md" | head -10`
Expected: front matter block with `title`, `date: 2016-07-08`, `categories: [Python]`, `slug: Python-使用python下載gmail附件`, followed by the post body with no literal `{% raw %}`, `{% endraw %}`, or `{:` sequences remaining.

- [ ] **Step 6: Grep the whole output for leftover Jekyll/kramdown syntax**

Run: `grep -rl '{%\|{{ "\|{:' src/content/posts/ | wc -l`
Expected: `0`

- [ ] **Step 7: Commit**

```bash
git add scripts/ src/content.config.ts src/content/posts/ public/img/
git commit -m "feat: migrate posts from Jekyll to Astro content collection"
```

---

### Task 3: Design-system CSS + BaseLayout

**Files:**
- Create: `src/styles/global.css`
- Create: `src/layouts/BaseLayout.astro`

**Interfaces:**
- Produces: `BaseLayout` Astro component accepting `{ title: string }` prop, rendering `<html><head>...</head><body><Sidebar /><main class="content"><slot /></main></body></html>` — Sidebar is added in Task 4, so BaseLayout references it starting then; for this task, render a placeholder `<div id="sidebar-placeholder" />` instead so the task is independently testable.

- [ ] **Step 1: Write the design-system CSS**

`src/styles/global.css`:

```css
:root {
  --bg: #ffffff;
  --bg-alt: #f5f5f5;
  --primary: #151515;
  --secondary: #6b6b6b;
  --accent: #1b7c71;
  --accent-dark: #145f56;
  --accent-bg: #e3f5f3;
  --on-accent: #ffffff;
  --border: #e2e2e2;
  --radius: 6px;
  --font-mono: 'MesloLGS NF', 'SFMono-Regular', Menlo, Consolas, monospace;
  --font-sans: 'Inter', 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme='light']) {
    --bg: #212121;
    --bg-alt: #2b2b2b;
    --primary: #d0d0d0;
    --secondary: #9a9a9a;
    --accent: #7dd6cf;
    --accent-dark: #9fe4de;
    --accent-bg: rgba(125, 214, 207, 0.15);
    --on-accent: #12302b;
    --border: #3a3a3a;
  }
}

:root[data-theme='dark'] {
  --bg: #212121;
  --bg-alt: #2b2b2b;
  --primary: #d0d0d0;
  --secondary: #9a9a9a;
  --accent: #7dd6cf;
  --accent-dark: #9fe4de;
  --accent-bg: rgba(125, 214, 207, 0.15);
  --on-accent: #12302b;
  --border: #3a3a3a;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--primary);
  font-family: var(--font-sans);
  line-height: 1.6;
}

a {
  color: var(--accent);
}

a:focus-visible,
button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-mono);
  color: var(--primary);
  line-height: 1.3;
}

.layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 18rem;
  flex-shrink: 0;
  background: var(--bg-alt);
  border-right: 1px solid var(--border);
  padding: 2rem 1.5rem;
}

.content {
  flex: 1;
  max-width: 42rem;
  padding: 3rem 2rem;
}

@media (max-width: 48rem) {
  .layout {
    flex-direction: column;
  }
  .sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
}

.theme-toggle {
  background: none;
  border: 1px solid var(--border);
  border-radius: 50%;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  cursor: pointer;
  font-size: 0.95rem;
  margin-top: 1rem;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}

.theme-toggle:hover {
  background: var(--bg);
  color: var(--accent);
  border-color: var(--accent);
}

.post-card {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-alt);
  padding: 1.6rem 1.8rem;
  margin-bottom: 1.5rem;
  transition: border-color 0.2s;
}

.post-card:hover {
  border-color: var(--accent);
}

.post-card h2 a {
  color: var(--primary);
  text-decoration: none;
}

.post-meta {
  color: var(--secondary);
  font-family: var(--font-mono);
  font-size: 0.85rem;
  margin: 0.4rem 0 0.8rem;
}

.tag-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  display: inline-block;
  border: 1px solid var(--accent);
  color: var(--accent);
  font-family: var(--font-mono);
  border-radius: 4px;
  padding: 0.15em 0.6em;
  font-size: 0.82rem;
  text-decoration: none;
}

.pagination {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
  font-family: var(--font-mono);
}

pre, code {
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
code {
  background: #f5f5f5;
  padding: 0.15em 0.4em;
  color: #bf616a;
}
pre {
  background: #f9f9f9;
  padding: 1rem;
  overflow-x: auto;
}
pre code {
  border: none;
  background: none;
  padding: 0;
  color: inherit;
}
```

- [ ] **Step 2: Write `BaseLayout.astro`**

```astro
---
interface Props {
  title: string;
}
const { title } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <script>
      (function () {
        const stored = localStorage.getItem('theme');
        if (stored) document.documentElement.setAttribute('data-theme', stored);
      })();
    </script>
    <!-- No SRI here: Google serves a different stylesheet body per requesting
         browser's User-Agent (different font formats/subsets), so a single
         static hash cannot match every visitor. Google's own docs advise
         against SRI for this endpoint. -->
    <link
      href="https://fonts.googleapis.com/css?family=Inter:400,500,600,700|Noto+Sans+TC:400,500,700&display=swap"
      rel="stylesheet"
    />
    <!-- Pinned version (5.0.8), content is static — SRI hash verified against
         the actual file served at this URL. -->
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.0.8/css/all.css"
      integrity="sha384-3AB7yXWz4OeoZcPbieVW64vVXEwADiYyAEhwilzWsLw+9FgqpyjjStpPnpBO8o8S"
      crossorigin="anonymous"
    />
    <link rel="alternate" type="application/rss+xml" title="RSS" href="/blog/rss.xml" />
    <!-- No SRI here: this URL is a server-generated config endpoint (the
         query string selects a config bundle), not a static file, so its
         content isn't fixed and can't have one hash. Kept unchanged from the
         current site per the migration spec. -->
    <script
      type="text/javascript"
      src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
      is:inline
    ></script>
    <style>
      @import '../styles/global.css';
    </style>
  </head>
  <body>
    <div class="layout">
      <div id="sidebar-placeholder"></div>
      <main class="content">
        <slot />
      </main>
    </div>
  </body>
</html>
```

- [ ] **Step 3: Use it from the placeholder index page**

Update `src/pages/index.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="M.C. Shih · BLOG">
  <p>Scaffold OK</p>
</BaseLayout>
```

- [ ] **Step 4: Build and verify styles are linked**

Run: `npm run build:site && grep -o 'Inter' dist/index.html`
Expected: at least one match (the font link is present in the output).

- [ ] **Step 5: Commit**

```bash
git add src/styles/global.css src/layouts/BaseLayout.astro src/pages/index.astro
git commit -m "feat: add design-system CSS and BaseLayout"
```

---

### Task 4: Sidebar component with theme toggle

**Files:**
- Create: `src/components/Sidebar.astro`
- Modify: `src/layouts/BaseLayout.astro` (replace `#sidebar-placeholder` with `<Sidebar />`)

**Interfaces:**
- Produces: `Sidebar.astro` (no props — site name/description/nav/social links are hardcoded, matching the current `_config.yml` values: title "M.C. Shih", description "Just for learning.")
- Consumes: none

- [ ] **Step 1: Write `Sidebar.astro`**

```astro
---
---
<div class="sidebar">
  <h1><a href="/blog/">M.C. Shih</a></h1>
  <p>Just for learning.</p>
  <nav>
    <a href="/blog/">Blog</a><br />
    <a href="/blog/about.html">About</a><br />
    <a href="/blog/archive.html">Archives</a><br />
    <a href="/blog/category.html">Category</a><br />
    <a href="/blog/search.html">Search</a>
  </nav>
  <p class="socials">
    <a href="https://shihs.github.io" target="_blank" aria-label="Home"><i class="fas fa-home"></i></a>
    <a href="https://github.com/shihs" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
    <a href="https://www.linkedin.com/in/min-chun-shih-6647779a/" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
    <a href="https://www.instagram.com/itakephotos_tw/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
  </p>
  <p>&copy; <span id="year"></span>. All rights reserved.</p>
  <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle dark mode">
    <i class="fas fa-moon"></i>
  </button>
</div>

<script>
  document.getElementById('year')!.textContent = String(new Date().getFullYear());

  const toggle = document.getElementById('theme-toggle')!;
  const icon = toggle.querySelector('i')!;

  function currentTheme(): 'light' | 'dark' {
    const attr = document.documentElement.getAttribute('data-theme');
    if (attr === 'dark' || attr === 'light') return attr;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function updateIcon(theme: 'light' | 'dark') {
    icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }

  updateIcon(currentTheme());

  toggle.addEventListener('click', () => {
    const next = currentTheme() === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateIcon(next);
  });
</script>
```

- [ ] **Step 2: Wire it into `BaseLayout.astro`**

Replace `<div id="sidebar-placeholder"></div>` with:

```astro
    <Sidebar />
```

And add the import at the top of the frontmatter block:

```astro
import Sidebar from '../components/Sidebar.astro';
```

- [ ] **Step 3: Build and verify**

Run: `npm run build:site && grep -o 'theme-toggle' dist/index.html`
Expected: at least one match.

- [ ] **Step 4: Commit**

```bash
git add src/components/Sidebar.astro src/layouts/BaseLayout.astro
git commit -m "feat: add sidebar with nav, socials, and dark-mode toggle"
```

---

### Task 5: Post list (index) with pagination

**Files:**
- Create: `src/components/PostCard.astro`
- Modify: `src/pages/index.astro`
- Create: `src/pages/[page].astro`

**Interfaces:**
- Consumes: `getCollection('posts')` from `astro:content` (Task 2)
- `PostCard` props: `{ post: CollectionEntry<'posts'> }`

- [ ] **Step 1: Write `PostCard.astro`**

```astro
---
import type { CollectionEntry } from 'astro:content';
interface Props {
  post: CollectionEntry<'posts'>;
}
const { post } = Astro.props;
const d = post.data.date;
const year = String(d.getUTCFullYear());
const month = String(d.getUTCMonth() + 1).padStart(2, '0');
const href = `/blog/${year}/${month}/${post.data.slug}.html`;
---
<article class="post-card">
  <h2><a href={href}>{post.data.title}</a></h2>
  <div class="post-meta">
    {d.toISOString().slice(0, 10)}
    {post.data.categories.map((c) => <span> · {c}</span>)}
  </div>
</article>
```

- [ ] **Step 2: Write the paginated index route**

`src/pages/index.astro`:

```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';
import PostCard from '../components/PostCard.astro';

const PAGE_SIZE = 8;
const all = (await getCollection('posts')).sort(
  (a, b) => b.data.date.valueOf() - a.data.date.valueOf()
);
const page1 = all.slice(0, PAGE_SIZE);
const hasNext = all.length > PAGE_SIZE;
---
<BaseLayout title="M.C. Shih · BLOG">
  {page1.map((post) => <PostCard post={post} />)}
  <div class="pagination">
    <span></span>
    {hasNext && <a href="/blog/2">Older →</a>}
  </div>
</BaseLayout>
```

- [ ] **Step 3: Write the remaining-pages route**

`src/pages/[page].astro`:

```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';
import PostCard from '../components/PostCard.astro';

export async function getStaticPaths() {
  // PAGE_SIZE must live inside getStaticPaths, not at module top-level:
  // Astro 7.1.1 tree-shakes top-level consts out of the bundle it builds
  // for this function, causing a "PAGE_SIZE is not defined" runtime error
  // (confirmed by inspecting the compiled chunk during Task 5's execution).
  const PAGE_SIZE = 8;
  const all = (await getCollection('posts')).sort(
    (a, b) => b.data.date.valueOf() - a.data.date.valueOf()
  );
  const pageCount = Math.ceil(all.length / PAGE_SIZE);
  const paths = [];
  for (let p = 2; p <= pageCount; p++) {
    paths.push({
      params: { page: String(p) },
      props: {
        posts: all.slice((p - 1) * PAGE_SIZE, p * PAGE_SIZE),
        hasPrev: true,
        hasNext: p < pageCount,
        page: p,
      },
    });
  }
  return paths;
}

interface Props {
  posts: Awaited<ReturnType<typeof getCollection<'posts'>>>;
  hasPrev: boolean;
  hasNext: boolean;
  page: number;
}
const { posts, hasPrev, hasNext, page } = Astro.props;
---
<BaseLayout title={`M.C. Shih · BLOG (page ${page})`}>
  {posts.map((post) => <PostCard post={post} />)}
  <div class="pagination">
    {hasPrev && <a href={page === 2 ? '/blog/' : `/blog/${page - 1}`}>← Newer</a>}
    {hasNext && <a href={`/blog/${page + 1}`}>Older →</a>}
  </div>
</BaseLayout>
```

- [ ] **Step 4: Run the migration script (if not already run) and build**

Run: `npm run migrate && npm run build:site`
Expected: no errors; `dist/index.html` and `dist/2/index.html` (or `dist/2.html` per `build.format: file` — check actual output filename) both exist.

Run: `find dist -maxdepth 1 -name "2*"`
Expected: a file or directory for page 2 is present, confirming pagination generated more than one page (100 posts / 8 per page = 13 pages).

- [ ] **Step 5: Commit**

```bash
git add src/components/PostCard.astro src/pages/index.astro "src/pages/[page].astro"
git commit -m "feat: add paginated post index"
```

---

### Task 6: Individual post pages preserving old permalinks

**Files:**
- Create: `src/layouts/PostLayout.astro`
- Create: `src/components/Comments.astro`
- Create: `src/pages/[year]/[month]/[slug].astro`

**Interfaces:**
- Consumes: `CollectionEntry<'posts'>`, `render(post)` from `astro:content` → `{ Content }` (NOT `post.render()` — that's the legacy content-collections API, incompatible with the glob-loader Content Layer API this project uses)
- Produces: pages at `/blog/{year}/{month}/{slug}.html`, matching every `url` in `scripts/permalink-manifest.json`

- [ ] **Step 1: Write `Comments.astro`**

This wires the Giscus embed. The real `data-repo-id` / `data-category-id` values do not exist yet — they are generated by registering the repo with https://giscus.app, which requires GitHub Discussions to be enabled on `shihs/blog` first. That is a manual, external step (documented in Task 14), not something this script can produce. The component reads them from `import.meta.env` so the build does not need to hardcode secrets:

```astro
---
const repoId = import.meta.env.PUBLIC_GISCUS_REPO_ID ?? '';
const categoryId = import.meta.env.PUBLIC_GISCUS_CATEGORY_ID ?? '';
---
{repoId && categoryId ? (
  <section class="comments">
    {/* No SRI: giscus ships client.js from a rolling, unversioned URL with
       no published per-release hash — pinning one here would silently break
       the widget the next time giscus updates it. crossorigin is kept so
       the browser still enforces CORS on the request. */}
    <script
      src="https://giscus.app/client.js"
      data-repo="shihs/blog"
      data-repo-id={repoId}
      data-category="Comments"
      data-category-id={categoryId}
      data-mapping="pathname"
      data-strict="0"
      data-reactions-enabled="1"
      data-emit-metadata="0"
      data-input-position="top"
      data-theme="preferred_color_scheme"
      data-lang="en"
      crossorigin="anonymous"
      async
      is:inline
    ></script>
  </section>
) : null}
```

- [ ] **Step 2: Write `PostLayout.astro`**

```astro
---
import BaseLayout from './BaseLayout.astro';
import Comments from '../components/Comments.astro';
import { getCollection, render, type CollectionEntry } from 'astro:content';

interface Props {
  post: CollectionEntry<'posts'>;
}
const { post } = Astro.props;
// Use the standalone render() from astro:content, not post.render() —
// entry.render() was the legacy content-collections API; the Content Layer
// API (glob loader, used since Task 2's LegacyContentConfigError fix)
// requires the standalone function instead. Confirmed by a real build
// failure (`post.render is not a function`) during Task 6's execution.
const { Content } = await render(post);

const all = await getCollection('posts');
const related = all
  .filter((p) => p.id !== post.id)
  .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())
  .slice(0, 3);

function hrefFor(p: CollectionEntry<'posts'>) {
  const d = p.data.date;
  const year = String(d.getUTCFullYear());
  const month = String(d.getUTCMonth() + 1).padStart(2, '0');
  return `/blog/${year}/${month}/${p.data.slug}.html`;
}
---
<BaseLayout title={`${post.data.title} · M.C. Shih`}>
  <article>
    <h1>{post.data.title}</h1>
    <div class="post-meta">
      {post.data.date.toISOString().slice(0, 10)}
      {post.data.categories.map((c) => <span> · {c}</span>)}
    </div>
    <Content />
  </article>

  <Comments />

  <section class="related">
    <h2>Latest Posts</h2>
    <ul>
      {related.map((p) => (
        <li><a href={hrefFor(p)}>{p.data.title}</a></li>
      ))}
    </ul>
  </section>
</BaseLayout>
```

- [ ] **Step 3: Write the dynamic post route**

`src/pages/[year]/[month]/[slug].astro`:

```astro
---
import { getCollection, type CollectionEntry } from 'astro:content';
import PostLayout from '../../../layouts/PostLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('posts');
  return posts.map((post) => {
    const d = post.data.date;
    const year = String(d.getUTCFullYear());
    const month = String(d.getUTCMonth() + 1).padStart(2, '0');
    return {
      params: { year, month, slug: post.data.slug },
      props: { post },
    };
  });
}

interface Props {
  post: CollectionEntry<'posts'>;
}
const { post } = Astro.props;
---
<PostLayout post={post} />
```

- [ ] **Step 4: Build and spot-check against the manifest**

Run: `npm run build:site`

Run this check script inline:

```bash
node -e "
const fs = require('fs');
const manifest = JSON.parse(fs.readFileSync('scripts/permalink-manifest.json', 'utf8'));
let missing = 0;
for (const entry of manifest) {
  const p = 'dist' + entry.url;
  if (!fs.existsSync(p)) {
    console.error('MISSING:', p);
    missing++;
  }
}
console.log(missing === 0 ? 'All 100 permalinks present.' : missing + ' missing.');
"
```

Expected: `All 100 permalinks present.`

- [ ] **Step 5: Commit**

```bash
git add src/layouts/PostLayout.astro src/components/Comments.astro "src/pages/[year]"
git commit -m "feat: add individual post pages preserving old permalinks"
```

---

### Task 7: Archive page

**Files:**
- Create: `src/pages/archive.astro`

**Interfaces:**
- Consumes: `getCollection('posts')`

- [ ] **Step 1: Write the archive page, grouped by year**

```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';

const all = (await getCollection('posts')).sort(
  (a, b) => b.data.date.valueOf() - a.data.date.valueOf()
);

const byYear = new Map<string, typeof all>();
for (const post of all) {
  const year = String(post.data.date.getUTCFullYear());
  if (!byYear.has(year)) byYear.set(year, []);
  byYear.get(year)!.push(post);
}

function hrefFor(p: (typeof all)[number]) {
  const d = p.data.date;
  const year = String(d.getUTCFullYear());
  const month = String(d.getUTCMonth() + 1).padStart(2, '0');
  return `/blog/${year}/${month}/${p.data.slug}.html`;
}
---
<BaseLayout title="Archives · M.C. Shih">
  <h1>Archives</h1>
  {[...byYear.entries()].map(([year, posts]) => (
    <section>
      <h2>{year}</h2>
      <ul>
        {posts.map((p) => (
          <li>
            <span class="post-meta">{p.data.date.toISOString().slice(5, 10)}</span>
            <a href={hrefFor(p)}>{p.data.title}</a>
          </li>
        ))}
      </ul>
    </section>
  ))}
</BaseLayout>
```

- [ ] **Step 2: Build and verify**

Run: `npm run build:site && test -f dist/archive.html && echo OK`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add src/pages/archive.astro
git commit -m "feat: add archive page grouped by year"
```

---

### Task 8: Category page (simplified tag list)

**Files:**
- Create: `src/pages/category.astro`

**Interfaces:**
- Consumes: `getCollection('posts')`

- [ ] **Step 1: Write the category page**

```astro
---
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';

const all = await getCollection('posts');

const byCategory = new Map<string, typeof all>();
for (const post of all) {
  for (const cat of post.data.categories) {
    if (!byCategory.has(cat)) byCategory.set(cat, []);
    byCategory.get(cat)!.push(post);
  }
}
const sortedCategories = [...byCategory.entries()].sort((a, b) =>
  a[0].localeCompare(b[0])
);

function hrefFor(p: (typeof all)[number]) {
  const d = p.data.date;
  const year = String(d.getUTCFullYear());
  const month = String(d.getUTCMonth() + 1).padStart(2, '0');
  return `/blog/${year}/${month}/${p.data.slug}.html`;
}
---
<BaseLayout title="Category · M.C. Shih">
  <h1>Category</h1>
  <ul class="tag-list">
    {sortedCategories.map(([cat]) => (
      <li><a class="tag" href={`#${cat}`}>{cat} ({byCategory.get(cat)!.length})</a></li>
    ))}
  </ul>
  {sortedCategories.map(([cat, posts]) => (
    <section id={cat}>
      <h2>{cat}</h2>
      <ul>
        {posts
          .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())
          .map((p) => (
            <li><a href={hrefFor(p)}>{p.data.title}</a></li>
          ))}
      </ul>
    </section>
  ))}
</BaseLayout>
```

- [ ] **Step 2: Build and verify**

Run: `npm run build:site && test -f dist/category.html && echo OK`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add src/pages/category.astro
git commit -m "feat: add simplified category/tag listing page"
```

---

### Task 9: About page and 404

**Files:**
- Create: `src/pages/about.astro`
- Create: `src/pages/404.astro`

**Interfaces:** none beyond `BaseLayout`

- [ ] **Step 1: Write `about.astro`** (content ported from the current `about.md`)

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="About · M.C. Shih">
  <h1>About</h1>
  <p>Hello, I'm Min-Chun, from Taiwan.</p>
  <p>
    Data Engineer / Machine Learning Engineer with a Master's in Statistics
    and Machine Learning from Linköping University, Sweden.
  </p>
  <p>I share what I've learnt along the way.</p>
  <p>Contact me: <a href="mailto:mcshihs@gmail.com">mcshihs@gmail.com</a></p>
</BaseLayout>
```

- [ ] **Step 2: Write `404.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="404 · M.C. Shih">
  <h1>404</h1>
  <p>Page not found.</p>
  <p><a href="/blog/">Back to the blog</a></p>
</BaseLayout>
```

- [ ] **Step 3: Build and verify**

Run: `npm run build:site && test -f dist/about.html && test -f dist/404.html && echo OK`
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add src/pages/about.astro src/pages/404.astro
git commit -m "feat: add about and 404 pages"
```

---

### Task 10: RSS feed

**Files:**
- Create: `src/pages/rss.xml.js`

**Interfaces:**
- Consumes: `@astrojs/rss`, `getCollection('posts')`

- [ ] **Step 1: Write the RSS route**

```js
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('posts');
  return rss({
    title: 'M.C. Shih · BLOG',
    description: 'Just for learning.',
    site: context.site,
    items: posts.map((post) => {
      const d = post.data.date;
      const year = String(d.getUTCFullYear());
      const month = String(d.getUTCMonth() + 1).padStart(2, '0');
      return {
        title: post.data.title,
        pubDate: post.data.date,
        link: `/blog/${year}/${month}/${post.data.slug}.html`,
        categories: post.data.categories,
      };
    }),
  });
}
```

- [ ] **Step 2: Build and verify**

Run: `npm run build:site && test -f dist/rss.xml && echo OK`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add src/pages/rss.xml.js
git commit -m "feat: add RSS feed"
```

---

### Task 11: Pagefind search

**Files:**
- Create: `src/pages/search.astro`
- Modify: `package.json` (already wired the `build` script to run `npx pagefind --site dist` in Task 1 — verify here)

**Interfaces:**
- Consumes: the Pagefind UI script/CSS, generated into `dist/pagefind/` by the `pagefind` CLI after `astro build` runs (this is why `build.format: 'file'` output needs to exist before Pagefind indexes it — the `npm run build` script order already handles this: `astro build && npx pagefind --site dist`)

- [ ] **Step 1: Write the search page**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Search · M.C. Shih">
  <h1>Search</h1>
  <div id="search"></div>
  <link href="/blog/pagefind/pagefind-ui.css" rel="stylesheet" />
  <script src="/blog/pagefind/pagefind-ui.js" is:inline></script>
  <script is:inline>
    window.addEventListener('DOMContentLoaded', () => {
      new PagefindUI({ element: '#search', showSubResults: true });
    });
  </script>
</BaseLayout>
```

- [ ] **Step 2: Run the full build (including Pagefind indexing) and verify**

Run: `npm run build`
Expected: ends with Pagefind's own summary output (e.g. "Indexed X pages"); `dist/pagefind/pagefind-ui.js` exists.

Run: `test -f dist/pagefind/pagefind-ui.js && echo OK`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add src/pages/search.astro
git commit -m "feat: add Pagefind-powered search page"
```

---

### Task 12: GitHub Actions deploy workflow

**Files:**
- Create: `.github/workflows/deploy.yml`
- Delete: `.github/gh-pages.yml`

**Interfaces:** none (CI configuration only)

- [ ] **Step 1: Write the new workflow**

`.github/workflows/deploy.yml`:

```yaml
name: Build and deploy blog to GitHub Pages

on:
  push:
    branches: ["master", "main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@v4

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Build (Astro + Pagefind)
        run: npm run build
        env:
          PUBLIC_GISCUS_REPO_ID: ${{ secrets.PUBLIC_GISCUS_REPO_ID }}
          PUBLIC_GISCUS_CATEGORY_ID: ${{ secrets.PUBLIC_GISCUS_CATEGORY_ID }}

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Remove the old workflow**

```bash
rm .github/gh-pages.yml
```

- [ ] **Step 3: Validate the YAML parses**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml'))" && echo OK`
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/deploy.yml
git rm .github/gh-pages.yml
git commit -m "ci: switch deploy to actions/deploy-pages"
```

---

### Task 13: Remove Jekyll files and do a full verification pass

**Files:**
- Delete: `_layouts/`, `_includes/`, `_posts/` (after confirming migration succeeded), `_config.yml`, `Gemfile*` (if present), `public/css/`, `js/lunr.min.js`, `js/search.js`, `search_data.json`, `search.md`, `category.md`, `archive.md`, `about.md`, `index.html` (Jekyll root), `.travis.yml`, `build.R`, `_source/`
- Keep: `img/` (already copied to `public/img/` in Task 2 — remove only after this task's build passes), `downloads/`

**Interfaces:** none

- [ ] **Step 1: Confirm a from-scratch build still succeeds before deleting anything**

Run: `rm -rf dist node_modules/.astro && npm run build`
Expected: succeeds with all 100 posts, `dist/pagefind/` present, no errors.

- [ ] **Step 2: Remove dead/legacy files**

```bash
git rm -r _layouts _includes public/css js/lunr.min.js js/search.js search_data.json \
  search.md category.md archive.md about.md index.html \
  .travis.yml build.R _source
```

(Do not remove `_posts/` or `_config.yml` yet — Step 4 double-checks first.)

- [ ] **Step 3: Rebuild after removal to make sure nothing in `src/` depended on the removed files**

Run: `rm -rf dist && npm run build`
Expected: succeeds identically to Step 1.

- [ ] **Step 4: Remove the now-fully-migrated Jekyll source, and retire the one-time migration tooling**

DECISION (made after Task 13 first flagged this as a conflict, not assumed
upfront): going forward, new posts are authored directly in
`src/content/posts/` using the Astro front-matter shape (`title`, `date`,
`categories`, `slug`) — not in Jekyll's `_posts/` format. The migration
script and its CI step were a one-time bridge, not a permanent part of the
build. `.github/workflows/deploy.yml` (Task 12) has already been corrected
to drop its "Migrate posts" step. This step follows through on that
decision:

```bash
git rm -r _posts _config.yml
git rm img -r  # already duplicated into public/img/ by the migration script
git rm scripts/migrate-posts.mjs scripts/permalink-manifest.json
```

Also edit `package.json`'s `build` script to drop the now-meaningless
migrate/check step (there's nothing left for it to check against), and
remove the `migrate` script entry entirely:

```json
"scripts": {
  "dev": "astro dev",
  "build": "astro build && npx pagefind --site dist",
  "build:site": "astro build",
  "preview": "astro preview"
}
```

- [ ] **Step 5: Final full verification build**

Run: `rm -rf dist && npm ci && npm run build`
Expected: succeeds; re-run the manifest check (same logic as Task 6 Step 4,
but reference the copy that still exists at
`docs/superpowers/specs/permalink-manifest.json` since
`scripts/permalink-manifest.json` was just deleted) — all 100 permalinks
present.

Run:
```bash
grep -rl '{%\|{:' dist/*.html 2>/dev/null | wc -l
```
Expected: matches only come from the site's own CSS (`:not(...)` selectors
containing `{:` as a byproduct of the grep pattern, not `{: ...}` kramdown
syntax) — inspect any hits by hand to confirm they're CSS, not leftover
Jekyll/kramdown markup that leaked into rendered post content specifically
(check `dist/{year}/{month}/*.html` post pages, not just any `dist/*.html`).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "chore: remove Jekyll source files, Astro is now the sole build"
```

---

### Task 14: Manual follow-up steps (not code — do these by hand)

These cannot be done by running a script; they require the repo owner to
click through external UIs.

1. **Enable GitHub Discussions** on `shihs/blog`: repo Settings → General →
   Features → check "Discussions". Create a "Comments" category (or use the
   default one) — this must match `data-category="Comments"` in
   `src/components/Comments.astro`.
2. **Register with giscus.app**: visit https://giscus.app, enter
   `shihs/blog` as the repository, follow its steps, and copy the generated
   `data-repo-id` and `data-category-id` values.
3. **Add repo secrets**: in `shihs/blog` → Settings → Secrets and variables →
   Actions, add `PUBLIC_GISCUS_REPO_ID` and `PUBLIC_GISCUS_CATEGORY_ID` with
   the values from step 2 (the GitHub Actions workflow from Task 12 already
   reads these).
4. **Switch the Pages source**: repo Settings → Pages → Build and
   deployment → Source = "GitHub Actions" (it's currently implicitly
   Jekyll-building from the branch; this build no longer produces a `docs/`
   folder Jekyll can auto-process, it needs the Actions-based deploy from
   Task 12).
5. Push to `master`/`main` and confirm the Actions run deploys successfully,
   then spot-check a handful of old post URLs live (from
   `docs/superpowers/specs/permalink-manifest.json`) to confirm they still
   resolve.

---

## Notes for the implementer

- `scripts/permalink-manifest.json` is authoritative — it was generated by
  actually building the current Jekyll site and reading `post.url` /
  `post.path` for every post, not by re-deriving Jekyll's slugify rules by
  hand. Trust it over any manual slug computation.
- 37 of the 100 posts use the `{{ "/img/..." | absolute_url }}` Liquid image
  tag; 4 use external `user-image.logdown.io` hotlinks (left untouched, they
  still resolve); 42 use kramdown `{: ...}` attribute lists (mostly
  `{:target="_blank"}` and image width/height) — all three are handled by
  `scripts/migrate-posts.mjs`, but Task 2 Step 6's grep is the safety net
  that catches anything that pattern didn't anticipate.
- 15 posts contain `$$` (math). MathJax is kept unchanged, but Astro's
  markdown processor (remark, not kramdown) may interact with underscores
  or asterisks inside math differently. There is no upfront fix for this in
  the plan — it's the "Open risk" from the design spec. After Task 13's
  build, do a visual spot-check of those 15 posts specifically:
  `grep -l '\$\$' src/content/posts/*.md`
