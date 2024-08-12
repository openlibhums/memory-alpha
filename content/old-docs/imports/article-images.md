Title: Article Images Import

# Article Images Import

The article images import tool allows you to supply an article
identifier and a URL for an image. Janeway will download the image and
set it as the articles large image file (also known as the hero image).

<div class="warning">

<div class="title">

Warning

</div>

You MUST ensure you have a license/permission to download and use the
image. We recommend Unsplash, where Images are licensed similar to CC0.
The URL **MUST** be directly to the image, not the landing page. On
Unsplash you can get this by right-clicking on the "Download free"
button and selecting "Copy link address".

</div>

1.  Download the
    `article image import template <nstatic/article_images_import_template.csv>`.
2.  Fill in the details, you can add on article per line.
3.  On the Imports Plugin main page select **Article Images** and click
    **Start Import**.
4.  Select your CSV and **Upload it**.
5.  Click **Import** to complete the process.

<div class="tip">

<div class="title">

Tip

</div>

Download the
`article image import sample <nstatic/article_images_import_sample.csv>`
CSV to see example data.

</div>

## Metadata Field Reference

| Field           | Notes                                    |
|-----------------|------------------------------------------|
| Identifier Type | Should be either id, doi or pub-id       |
| Identifier      | The corresponding ID, DOI or Pub-ID      |
| URL             | A URL leading directly to an image file. |
