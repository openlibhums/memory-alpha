# Science Open Transporter

This plugin allows users with staff or superuser access to click a button to deposit the full text of each journal issue in [Science Open](https://www.scienceopen.com/).

## Configuration

Setting up this plugin requires paid access to Science Open’s discovery services. You need an FTP server name, a username, and a password.

A system administrator then needs to install and configure the plugin using the [GitHub repository](https://github.com/openlibhums/so_transporter) and your Science Open account details.

## Depositing content

The plugin can be accessed through the journal-level plugin menu.

When you open it, there is a list of journal issues, with two actions available for each one:

- **Send to Science Open**
  Bundles the issue content and sends it via FTP.
- **Download Zip**
  Bundles the issue content and downloads it as a ZIP file, so you can check the content and troubleshoot.

## What is sent

The plugin sends the primary public PDF and XML galley files (see [Typesetting files](../guides/editor-guide-to-typesetting.md#typesetting-files)) associated with an article, along with any images that belong in the XML galley.

If there is no XML galley, Janeway generates and sends a JATS XML stub file containing essential metadata about the article.

## Checking content that was sent

The plugin does not create a record of what was sent, so it’s best to check the content in Science Open.

## Sending all the issues in a journal

System administrators can send all issues of a journal for you, using the command line.
