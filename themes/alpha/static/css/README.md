# CSS for Memory Alpha Theme

We take a hybrid approach to CSS in this theme, balancing utility classes
with component-based semi-scoped styles. The structure is loosely inspired
by the ITCSS upside-down pyramid,[1] where the wide end has layers with low
precedence and specificity and the narrow point has greater precedence
and specificity.

```
   ######### settings
    ####### resets
     ##### elements
      ### components
       # utilites
```

## Settings

Our settings file includes colours, fonts, and custom properties for
things like spacing and font sizes. To understand the spacing and
font-sizing properties, read James Gilyead’s blog post[2] and look at the
scale generators on Utopia’s website.[3, 4]

## Resets

We have a single file for resets that was made by drawing from a several
modern resets by Andy Bell, Josh W. Comeau, and Kevin Powell.[5, 6, 7]

## Elements

Next in the layers is a set of base styles for HTML elements like headings
and paragraphs. The idea here is to introduce theme defaults that can be
easily overwritten if needed, but which work well for the
general use case. We use element selectors so they have low specificity
and can be overwritten with classes in components or utilities. By using
element selectors, we also encourage good use of semantic HTML for
straightforward content.

Heydon Pickering on this strategy:

> Each time you come to creating a new
> component, if it introduces new elements, style those new elements with
> element selectors. Now is not the time to introduce restrictive,
> high-specificity selectors. Nor is there any need to compose a class.
> Semantic elements are what they are.[8]

## Components

When things go beyond elements, our approach to components recognises that
often you need a very precise combination of HTML and CSS to achieve
a high-spec visual design that is also usable and accessible. We also know
that it is all very well and good creating CSS components that look and
work great, but if we return to them in two years’ time and cannot
remember which HTML markup works with them and which doesn’t, we may
misuse them, introduce inconsistencies, or stretch them beyond their
boundaries of usability and accessibility.

For these reasons, we want to keep the HTML and CSS for components
together. We place the HTML and CSS for each component in the same place,
in `static/components/`. This is outside the normal `static/css` folder
for CSS and outside the normal `templates` folder for HTML, but that is
OK, because we have settings in `pelicanconf.py` to pick up these files
and make them available in their relative contexts so that they can be
imported in both Jinja templates and in the `index.css` file.

Components can and should make use of the CSS from settings, elements, and
utilities, in addition to defining their own classes and declaration
blocks if needed. The only requirement we want to hold to is about nesting
for namespacing: introduce a new class with the same name as the component
and nest all other declarations for that component under it.

## Utilities

The utilities layer is loaded last so that it has the greatest precedence.
Utilities are provided for spacing, margins, colours, fonts, layouts, and
accessibility. Several of these were inspirerd by Kevin Powell.[7]

Of note is the flow spacing utility. For usage please see Andy Bell’s
explainer.[9] In short, it lets you put margin between prose elements that
is appropriate to those elements, but not every time, just when it makes
sense. Use it for prose and other text contexts for help with spacing.

See also the utilities for flex and grid,[10] which should be used for
layouts depending on the situation. We have a few basic helpers here but
can expand these as needed.

## Other

A mastodon thread from Julia Evans about switching away from Tailwind
helped in finding all these resources.[11]

## Sources

1. Lubos Kmetko, “ITCSS: Scalable and Maintainable CSS Architecture,” Nov 2021,
   https://www.xfive.co/blog/itcss-scalable-maintainable-css-architecture/

2. James Gilyead, “Designing with fluid type scales,” 1 Feb 2020,
   https://utopia.fyi/blog/designing-with-fluid-type-scales

3. “Fluid Type Calculator,” https://utopia.fyi/type/calculator

4. “Fluid Space Calculator,” https://utopia.fyi/space/calculator/

5. Andy Bell, "A more modern CSS reset," 18 Sept 2023,
   https://piccalil.li/blog/a-more-modern-css-reset/

6. Josh W. Comeau, “A modern CSS reset,” 3 Apr 2024,
   https://www.joshwcomeau.com/css/custom-css-reset/

7. Kevin Powell, “Space Tourism,”
   https://github.com/kevin-powell/space-tourism

8. Heydon Pickering, “CSS inheritance, the cascade and global scope: Your
   new old worst best friends,”
   https://www.smashingmagazine.com/2016/11/css-inheritance-cascade-global-scope-new-old-worst-best-friends/

9. Andy Bell, “My favourite 3 lines of CSS,”
   https://piccalil.li/blog/my-favourite-3-lines-of-css/

10. Andy Bell, “Create a responsive grid layout,”
    https://piccalil.li/blog/create-a-responsive-grid-layout-with-no-media-queries-using-css-grid/

11. Julia Evans, “Have any of you switched from Tailwind to regular CSS?”,
    28 June 2024, https://social.jvns.ca/@b0rk/112696139088286557
