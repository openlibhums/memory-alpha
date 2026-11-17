# Portico

Status: Active

[GitHub repository](https://github.com/openlibhums/portico)

This plugin allows users with editor access to click a button to deposit the full text of a journal issue in the [Portico](https://www.portico.org/).

## Before using this plugin

Before this plugin can work on your installation, you will need to be a member of Portico as a publisher and pay a yearly fee.

Your Janeway system administrator then needs to install and configure the plugin using the GitHub repository and your Portico account details.

## Depositing content

Once it is installed, you can access the plugin through the journal-level plugin menu.

When you open the plugin, you see a list of journal issues, with two actions available for each one.

- **View**
  Opens the issue management page.
- **Export**
  Bundles the issue content and downloads it as a ZIP file, so you can check the content and troubleshoot.
- **Send to Portico**
  Bundles the issue content and sends it via FTP.

## What is sent

The plugin sends the primary public PDF, XML, and HTML galley files (see [**Typesetting files**](../guides/editor-guide-to-typesetting.md#typesetting-files)) associated with an article, along with any images that belong in the XML galley or HTML galley.

If there is no XML galley, Janeway generates and sends a JATS XML stub file containing essential metadata about the article.

> [!NOTE]
> Note: The JATS metadata sent by this plugin is more limited than in other JATS exports from Janeway. For example, it does not include ORCIDs, keywords, competing interest statements, or funding statements.

## Checking content that was sent

The plugin creates a brief record of each deposit, including the time sent, which you can view if you have access to the admin area. Look under **Portico** and search the **Delivereds** records.

It is also a good idea to check records on Portico to make sure they are being received.

## Sending all the articles in a journal

System administrators can send bulk deposits for you, using the command line.
