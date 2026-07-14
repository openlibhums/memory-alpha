# Article images import

The article images import tool allows you to supply an article
identifier and a URL for an image. Janeway will download the image and
set it as the articles large image file (also known as the hero image).

> [!WARNING]
> You MUST ensure you have a licence/permission to download and use the image. It is recommended to use Unsplash (or similar services), where images are licensed similar to CC0. The URL must be directly to the image, not the landing page. On Unsplash you can get this by right-clicking on the **Download free** button and selecting **Copy link address**.

1.  Download the [article image import template](../downloadables/article-images-import-template.csv).
2.  Fill in the details, you can add on article per line.
3.  On the Imports Plugin main page select **Article images** and click
    **Start import**.
4.  Select your CSV and **Upload it**.
5.  Click **Import** to complete the process.

> [!TIP]
> Download the [article image import sample](../downloadables/article-images-import-sample.csv) CSV to see example data.

## Metadata field reference

| Field           | Notes                                    |
| --------------- | ---------------------------------------- |
| Identifier Type | Must be either id, doi or pub-id       |
| Identifier      | The corresponding ID, DOI or Pub-ID      |
| URL             | A URL leading directly to an image file. |
