# CLOCKSS

This plugin creates a manifest page on your Janeway installation with all the information that [CLOCKSS](https://clockss.org/) needs to archive your content.

> [!NOTE]
> See an example manifest page: [Political Philosophy](https://politicalphilosophyjournal.org/plugins/clockss/)

## Before using this plugin

Your Janeway system administrator should first install and configure the plugin using the [GitHub repository](https://github.com/openlibhums/lockss).

For CLOCKSS to ingest your content, you will need to be a member of CLOCKSS as a publisher and pay a yearly fee. You will need to share the Janeway CLOCKSS manifest page with CLOCKSS so they know where to look for new content.

## Depositing content

Once it is set up and CLOCKSS has your manifest link, no further action is required. CLOCKSS will periodically check for and ingest new content.

## What is archived

CLOCKSS ingests the full article metadata and content, including HTML, JATS XML, PDF galleys, media, and supplementary files, as long as they live at the same domain. If they are hosted on a separate domain, CLOCKSS harvests them only if there is a permission statement that allows them to do so.

## Checking content that was archived

There is no record in Janeway of what CLOCKSS retrieved.

To verify journal content is reaching CLOCKSS, you can check the title list provided on the CLOCKSS website, which includes preserved volumes and preserved years.
