---
title: Cards
url: https://docs.docker.com/contribute/components/cards/
source: llms
fetched_at: 2026-01-24T14:06:36.248010746-03:00
rendered_js: false
word_count: 170
summary: Explains how to implement and configure card and grid components using shortcodes, including layout behavior and front matter data definition.
tags:
    - shortcodes
    - ui-components
    - grid-layout
    - markdown-limitations
    - front-matter-configuration
category: guide
---

Cards can be added to a page using the `card` shortcode. The parameters for this shortcode are:

There's a known limitation with the Markdown description of cards, in that they can't contain relative links, pointing to other .md documents. Such links won't render correctly. Instead, use an absolute link to the URL path of the page that you want to link to.

For example, instead of linking to `../install/linux.md`, write: `/engine/install/linux/`.

There's also a built-in `grid` shortcode that generates a... well, grid... of cards. The grid size is 3x3 on large screens, 2x2 on medium, and single column on small.

Grid is a separate shortcode from `card`, but it implements the same component under the hood. The markup you use to insert a grid is slightly unconventional. The grid shortcode takes no arguments. All it does is let you specify where on a page you want your grid to appear.

The data for the grid is defined in the front matter of the page, under the `grid` key, as follows: