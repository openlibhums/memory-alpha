# Memory Alpha

<p>
  <a href="https://github.com/BirkbeckCTP/memory-alpha/actions/workflows/pelican.yml"><img src="https://github.com/BirkbeckCTP/memory-alpha/actions/workflows/pelican.yml/badge.svg?branch=main" alt="build status"></a>
  <a href="https://github.com/BirkbeckCTP/memory-alpha/actions/workflows/playwright.yml"><img src="https://github.com/BirkbeckCTP/memory-alpha/actions/workflows/playwright.yml/badge.svg?branch=main" alt="test status"></a>
</p>

This repository is for the build of the janeway.systems site.

The website is built on top of the static-site generator
[Pelican](https://getpelican.com/).

## Contributing to documentation

We welcome contributions to our documentation. See “[Contributing to Janeway
documentation](/content/support/contributing-guide.md).”

## Setting up the development environment

### Native install

Pelican is built for Python (3.8.4+). In order to setup the project, you can
install your dependecies (including Pelican) with pip: `pip install -r
requirements.txt`.

Pelican's build system uses [GNU Make](https://www.gnu.org/software/make/) which comes pre-installed on most GNU Linux distributions.

You can refer to the guide on how to [install Pelican](https://docs.getpelican.com/en/latest/quickstart.html#installation) for more details.

To run the site in development and listen for changes to templates, use `pelican --autoreload --listen`. To build the site locally, use `pelican content`.

You can also run `make help` to see a full list of available build targets.

Finally, for testing, you will need to install testing requirements including Playwright:

```
pip install -r test-requirements.txt
playwright install
```

### Docker install

Our Makefile has two targets for working within a docker container:

- `make image` will create build a docker image on top of the official Python
  Alpine linux docker image, which you can use for all Pelican build processes

- `make shell` will create an ephemeral container and connect to it via tty. From
  here you can run `make help` to see a list of available build targerts

## Development

### Testing

Run automatic tests with `pytest`.

For manual testing, note you can serve Pelican to other devices like a mobile phone
on your secure LAN with `pelican --autoreload --listen --bind 0.0.0.0`.

### Janeway site pages

Steps to create a Janeway site page:

1. Create a new HTML file in `content/pages`. It does not have to be a full HTML
   document, it just needs a `head` with a `title` and a `body` containing the
   page content. Pelican will implicitly extend it from `page.html`.
   You can use jinja thanks to the `pelican-jinja2content` plugin.

2. Add the page name and URL to `MENUITEMS` in `pelicanconf.py`.

### Support pages

Documentation authors are asked to place all content in `/content/support/`,
using GitHub-flavored Markdown and including images in
`/content/support/images/`.

Pelican interprets these pages as “articles,” so minimal requirements about
having a `Title` in the YAML metadata apply.

If they are editing on GitHub.com, they can make commits on the perpetual
`copyediting` branch, or if they are working locally, they should open
a dedicated feature branch. They may often need help with pull requests and
merges from there into main.

### Components

The first time you build a given section or element,
if there is no appropriate component already, and if you are not sure
whether you will need to re-use it, just make your new thing with utility
classes and HTML markup in the content file, if possible. In other words, don’t bother
with a component if you’re not sure it will be worth it.

But as soon as you need that thing a second time, or if you need to write CSS
that cannot be easily abstracted into elements or utilities, go ahead and
abstract the repeated parts of it away from your content by creating
a component. Make sure to go back and revise the original instance of it to use
the component.

Components should be stored in `themes/[theme]/static/components/` in a flat
list (no subfolders). Give the component a descriptive name, generally using
two words or more.

### Types of components

What do we mean by components?

In many cases a component might just be a jinja template that you can use with
`{% include %}`.

But often you will want to make components for styling and layout purposes that allow
nesting like HTML elements (in other words they have “slots”).
By making both HTML and CSS files for a given component, you are aiding
consistency across the codebase because any page that wants to use the
component will be able to use the same combination of HTML and CSS as
everywhere else. This is especially important for accessibility since
it is the particular combination of HTML and CSS that is key for accessibility.

For components that need to nest other content, you can use jinja’s macro syntax:

<!-- prettier-ignore-start -->
```html
<!-- themes/[theme]/static/components/example_component.html -->
{% macro example_component() -%}
  <div class="bg-alpha-white text-alpha-blue">
    {{ caller() }}
  </div>
{%- endmacro %}
```
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
```html
<!-- content/pages/example_page.html -->
{% from 'components/example_component.html' import example_component %}
{% call example_component() %}
  <p>This is how I call my component and pass text into the slot
  provided, with the styling and framing markup abstracted to the
  component.</p>
{% endcall %}
```
<!-- prettier-ignore-end -->

See also “Components” in `static/css/README.md`.

### Images

Images should be stored in `themes/[theme]/static/images`
if they belong to the theme, or `docs/images` if they belong to documentation.
In the future we may want a more generic content images folder for
blog content or other content. But it would need to be easy to tell apart from
the docs images folder to make things clear for people editing the docs via GitHub.

### Colour

Designer guidelines: “As a hard rule, let's stick strictly to blue, black, and
tan for text/background combos. The other colors will be part of a secondary
palette reserved for illustrations.”

For accessibility we are aiming for all color contrast pairs to have
a [contrast ratio of at least 4.5](https://app.contrast-finder.org/). Based on
the colors defined in `css/settings.css` and `css/utilities.css`, we have
identified these accessible colour pairs for text and semantic elements:

```
text-alpha-white bg-alpha-black
text-alpha-yellow bg-alpha-black
text-alpha-black bg-alpha-white
text-alpha-red bg-alpha-white
text-alpha-blue bg-alpha-white
text-alpha-white bg-alpha-red
text-alpha-white bg-alpha-blue
text-alpha-black bg-alpha-yellow
```

Other combinations may be used (e.g. bg-alpha-yellow + bg-alpha-red) if the boundary
between them is not used to designate a semantic or navigational element
(e.g. a button). Textured backgrounds may be used behind text in certain cases,
but only when the text is large enough for sufficient contrast.

Note that you can use `best_foreground` from `utils.html` to make
to produce accessible colour pairs. It chooses either white or blue text
based on the background colour you pass in.

### Responsiveness and breakpoints

We currently use one breakpoint of 50 rems. Use media queries with
`width <= 50rem` or `width > 50rem`.

At the smaller width, think primarily of touch-screen users, especially those
using phones, but also make sure things are usable with a mouse.

In the wider range, think about layouts that can be easily linearized
for narrow screens using something simple like `flex-direction`, and note that there
are utility classes for flex direction. Avoid separate HTML structures for wide
and narrow screens, as duplicate content is harder to maintain.

We sparingly use one other wide breakpoint, 70 rems, in multi-column layouts where there would be empty space otherwise.

### CSS in general

See the [CSS README](themes/alpha/static/css/README.md).

### JS assets

Avoid copy-pasting JS source code into this repository. Instead find a suitable
module on NPM and install it with `npm install [module]`. Always prefer ES6
modules if available.

### Formatting

We use Prettier to consistently auto-format HTML, CSS, JS, MD, YAML, JSON, etc.
Install an IDE plugin or check your changes on the command line before
submitting pull requests.

```
npx prettier . --check
npx prettier . --write
```
