Title: Contributing to Janeway documentation

Work-in-process note: This page could explain how people including us and
our clients should contribute documentation. It would need several
sections, including what style to write in, using GitHub effectively, and
how the docs are organized, but to get started, we just have a section on
how to name files and folders.

## Naming files and folders

All text and image files and folders should be named with standard naming
conventions so they are easily usable on the web.

Do:

- use dashes to separate words in the file names

<pre class="ff-space-mono-regular">
  my-folder/my-file-name.txt
</pre>

Don’t:

- use spaces (reason: shell scripting)
- use capital letters (reason: avoid broken links)
- use underscores (reason: search engine optimization)
- use special characters (reason: hyperlink parsing)

<pre class="ff-space-mono-regular">
  my folder/my file name.txt
  My-Folder/My-File-Name.txt
  my_folder/my_file_name.txt
  my&your-folder/my&your-file-name.txt
</pre>
