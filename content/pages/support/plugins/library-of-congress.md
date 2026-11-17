# Library of Congress

This plugin allows users with editor access to click a button to deposit the full text of a journal issue in the [Library of Congress](https://www.loc.gov/) (LOC).

## When to use this plugin

Historically, the US Copyright Office required all publishers distributing works in the United States to send copies of those works to the Library of Congress. This is called [mandatory deposit](https://www.copyright.gov/help/faq/mandatory_deposit.html).

However, not all online-only journals are subject to this requirement. According to the [Copyright Office’s FAQ page](https://www.copyright.gov/cad/), “The regulation establishes that online-only works are exempt from mandatory deposit until the Copyright Office issues a demand for deposit of such works.” So, deposit is required for most Janeway journals only if the Copyright Office issues a Notice for Mandatory Deposit.

## Configuration

Setting up this plugin requires some information that you can get on the Notice for Mandatory Deposit your journal received, or by contacting the specialist at the Library of Congress who issued the notice:

- a Service Request Number (SRN), which is a unique number assigned to your journal
- an FTP server address
- an FTP server key
- a username and password

Your Janeway system administrator then needs to install and configure the plugin using the [GitHub repository](https://github.com/openlibhums/loc_transporter) and your LOC details.

## Accessing the plugin

The plugin can be accessed through the plugin menu at either the press or journal level.

## Creating a new SRN record

You need to create an SRN for each journal that has a deposit mandate.

The **SRN** comes from the Notice for Mandatory Deposit.

You can create the **Journal name filename** from the journal name by lowercasing all letters, removing a leading “the” and any punctuation, and replacing spaces with underscores. For example, “The Journal of Electronic Publishing” becomes `journal_of_electronic_publishing`.

## Depositing content

When you open each SRN, there is a list of journal issues, with two actions available for each one.

- **Send**
  Bundles the issue content and sends it via FTP.
- **Download Zip**
  Bundles the issue content and downloads it as a ZIP file, so you can check the content and troubleshoot.

## What is sent

The plugin sends the primary public PDF and XML galley files (see [**Typesetting files**](../guides/editor-guide-to-typesetting.md#typesetting-files)) associated with an article, along with any images that belong in the XML galley.

If there is no XML galley, Janeway generates and sends a JATS XML stub file containing essential metadata about the article.

## Checking content that was sent

The plugin does not create a record of what was sent, so it’s best to check the content in the LOC catalog.
