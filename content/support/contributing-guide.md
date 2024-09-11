Title: Contributing to Janeway documentation

# Contributing to Janeway documentation

Work-in-process note: This page could explain how people including us and
our clients should contribute documentation. It would need several
sections, including what style to write in, using GitHub effectively, and
how the docs are organized, but to get started, we just have a section on
how to name files and folders.

## Creating and editing pages

All the pages of the support site are generated from text files stored under
`/content/support/` in this repository. Old documentation can be found at
`/content/old-docs/` while the support site is being built.

Pages for the support site should be written in GitHub-flavored Markdown (GFM).
Image files should be added under `/content/support/images/`. All the content
can be edited on GitHub, so that you can make use of the Preview tab in GitHub.

When creating Git commits, either create a dedicated branch if you prefer, or
commit them to the perpetual branch `support-web-content`, and open pull
requests from there. If you need help with anything related to commits,
branches, or pull requests, please get in touch with our developers.

## Naming files and folders

All text and image files and folders should be named with standard naming
conventions so they are easily usable on the web.

Do:

- use dashes to separate words in the file names

```
  my-folder/my-file-name.txt
```

Don’t:

- use spaces (reason: shell scripting)
- use capital letters (reason: avoid broken links)
- use underscores (reason: search engine optimization)
- use special characters (reason: hyperlink parsing)

```
  my folder/my file name.txt
  My-Folder/My-File-Name.txt
  my_folder/my_file_name.txt
  my&your-folder/my&your-file-name.txt
```

## Page metadata

At the beginning of the file, please include the page title, preceded by
`Title: `. It will appear in the browser tab, on search results, and on social
media when the page is shared.

The page you are reading has this at the top:

```md
Title: Contributing to Janeway documentation
```

Please also include a top-level heading for each page, using the single hash in
Markdown syntax. Usually this will be the same as the page title.

For example:

```md
# Contributing to Janeway documentation
```

