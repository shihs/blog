# mcshih-blog

Personal blog built with [Astro](https://astro.build), deployed to GitHub Pages at [shihs.github.io/blog](https://shihs.github.io/blog).

## Development

```bash
npm install
npm run dev
```

## Scripts

- `npm run dev` — start the local dev server
- `npm run build` — build the site and generate the [Pagefind](https://pagefind.app) search index
- `npm run build:site` — build the site without the search index
- `npm run preview` — preview the production build locally

## Structure

- `src/content/posts/` — blog posts (Markdown, with `title`/`date`/`categories`/`slug` frontmatter)
- `src/pages/` — routes (post archive, category, search, about, RSS)
- `src/layouts/`, `src/components/` — page layouts and shared UI (sidebar, post card, comments)
- `public/` — static assets served as-is
- `downloads/` — files linked directly from post content

Comments use [giscus](https://giscus.app) and are configured via the `PUBLIC_GISCUS_REPO_ID` / `PUBLIC_GISCUS_CATEGORY_ID` environment variables.

## Deployment

Pushes to `master` trigger `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

## License

Open sourced under the [MIT license](LICENSE.md).
