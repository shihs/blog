# Blog migration: Jekyll (Hyde/Poole) → Astro

## Context

The blog at `shihs.github.io/blog` currently runs on Jekyll with the Hyde/Poole
theme. A CSS-only reskin (colors, fonts, dark mode, card styling) was applied
to bring it in line with the `shihs.github.io` portfolio's terminal-inspired
design system, but the underlying theme's structure and typography still read
as dated. The owner wants a full rebuild, not tied to Jekyll.

Scope: 102 existing posts (2016–2023), ~35MB of images, and the following
features currently in use: Disqus comments, a lunr.js client-side search,
a category "tag cloud" page, MathJax for math notation, RSS/sitemap via
jekyll-sitemap, and a GitHub Actions workflow that builds the site into a
`docs/` folder on the same branch for GitHub Pages.

Also present but unused/dead: `.travis.yml` and `build.R` (an old
R Markdown → Jekyll pipeline; only one leftover `.rmd` test file in
`_source/`, Travis CI itself is defunct). These are dropped in the rebuild.

## Decisions

| Area | Decision |
|---|---|
| Framework | Astro (content collections for posts, component-based layouts, static output) |
| Post URLs | Preserved exactly: `/YYYY/MM/title.html` (via a dynamic route reading the same fields Jekyll used: date + filename slug) |
| Design system | Same CSS variables/fonts/dark-mode toggle already built for the portfolio and the Jekyll reskin (teal accent, mono headings, Inter body, light/dark via `prefers-color-scheme` + manual toggle stored in `localStorage`) |
| Layout | Sidebar + content, matching the current Hyde structure (site title/description, nav, social icons, theme toggle) — visual language modernized, structural pattern kept, since a sidebar blog layout was explicitly approved earlier in this project |
| Comments | Disqus → **Giscus** (GitHub Discussions-backed, no tracking/ads). Existing Disqus comment history is not migrated (posts show 0 comments today regardless) |
| Search | lunr.js + jQuery + `search_data.json` → **Pagefind** (indexes the built static output directly, no hand-maintained search index file) |
| Category page | Simplified to a plain tag list per category (drop the dynamic font-size "tag cloud" styling) |
| Math | MathJax kept as-is (CDN script), since posts already use MathJax-compatible delimiters and re-authoring math syntax for KaTeX is out of scope |
| RSS / sitemap | Kept, via Astro's `@astrojs/rss` and `@astrojs/sitemap` |
| Deployment | GitHub Actions build step switches from "commit `docs/` back to the branch" to the standard `actions/deploy-pages` flow (build artifact → Pages deployment). Requires a one-time manual change in the repo's Settings → Pages → Source = "GitHub Actions", which the owner will do |
| Dropped | `.travis.yml`, `build.R`, `_source/` (dead R Markdown pipeline) |

## Content migration

A one-time Node script parses each file in `_posts/`:
- Extracts `date` and `slug` from the filename (`YYYY-MM-DD-title.md`)
- Reads Jekyll front matter (`title`, `categories`) into Astro-compatible
  front matter for the `posts` content collection
- Leaves the markdown body untouched (kramdown and Astro's markdown are
  close enough that most posts should render correctly as-is; a spot-check
  pass over the rendered output — especially posts with tables, footnotes,
  or embedded HTML — is part of the plan's verification step, not assumed
  up front)
- Copies referenced images from `img/` alongside their posts (or keeps a
  shared `public/img/` if paths are simple enough — decided during
  implementation based on how images are actually referenced in the posts)

## Structure (new repo layout, indicative)

```
src/
  content/
    config.ts          # posts collection schema
    posts/*.md          # migrated posts
  layouts/
    BaseLayout.astro    # sidebar + content shell, theme toggle
    PostLayout.astro    # post title/meta/content/Giscus/related posts
  components/
    Sidebar.astro
    PostCard.astro
    Pagination.astro
  pages/
    index.astro          # paginated post list
    [year]/[month]/[slug].astro
    archive.astro
    category/[tag].astro
    about.astro
    404.astro
  styles/
    global.css           # the design-system CSS (ported from custom.css)
public/
  img/ ...
  fonts/ (if self-hosted; otherwise Google Fonts links as today)
astro.config.mjs         # base: '/blog/'
.github/workflows/deploy.yml
```

## Out of scope for this pass

- Migrating Disqus comment history
- Rewriting math notation for KaTeX
- Redesigning the sidebar's fundamental structure (top-nav conversion) —
  not requested
- The `downloads/` folder contents (e.g. `get-pip.py`) are carried over
  as static files without review

## Open risk

Kramdown → Astro markdown differences (footnotes, definition lists, IAL
attributes like `{: .class}`) may not be 1:1. The plan should include a
verification pass that builds all 102 posts and flags any that render
visibly broken, rather than assuming a clean migration.
