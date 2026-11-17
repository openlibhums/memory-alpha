# DOAJ

Status: Active

[GitHub repository](https://github.com/openlibhums/doaj_transporter)

This plugin allows users with editor access to send regular deposits of published article metadata to the [Directory of Open Access Journals](https://doaj.org/) (DOAJ).

Articles can be sent automatically when they are published, or individual articles or issues can be sent manually.

Content files (galleys) do not go into DOAJ, but are accessible via direct links if they remain available on Janeway.

## Installation

Using this plugin requires that you have applied to have your journal indexed in DOAJ, and have received an API token from them.

Your Janeway system administrator then needs to install the plugin using the GitHub repository.

## Accessing the plugin

Once installed, the plugin can be accessed through the plugin menu at the journal level.

## Setting up deposits

Select **Configure** to see the API token and push settings.

The **DOAJ API key** should be put in here only if no press-wide default has already been set, using **Edit journal default settings** from the press-level manager.

The tickbox **Automatically push article metadata when an article is published** controls auto-deposit.

## Depositing metadata

If articles are set to be automatically deposited, no further action is required.

Otherwise, you can deposit things individually:

- On the list of issues, you can open the issue, or send the whole issue using **Push to DOAJ**.
- If you open the issue, you have more detailed options:
  - **Admin logs**  
    Click through to any record of the article being sent (requires superuser or admin area access)
  - **View JSON**  
    Allows you to preview the data that will be sent.
  - **Push**  
    Deposits the one article’s metadata.

## What is sent

The plugin sends the article metadata, following the [DOAJ data model](https://doaj.github.io/doaj-docs/master/data_models/IncomingAPIArticle).

## Checking records that were sent

The plugin creates a brief record of each article that is sent, including the time sent. These are linked from the issue page via the **Admin logs** button, and you can also search for them by article title or ID in the admin page for the plugin. Look under **DOAJ_TRANSPORTER** and search the **DOAJ deposits** records.

It is also a good idea to check records on DOAJ.

## Sending all the articles in a journal

System administrators can send bulk deposits and do other backlist synching for you, using the command line.
