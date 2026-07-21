import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('posts');
  return rss({
    title: 'M.C. Shih · BLOG',
    description: 'Just for learning.',
    site: new URL('/blog/', context.site),
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
