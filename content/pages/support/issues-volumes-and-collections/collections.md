# Collections

Collections are one of Janeway's built-in issue types, alongside issues. A collection groups related articles from across your journal, for example on a shared theme. Unlike an issue, a collection doesn't have to follow your journal's publication sequence. It can bring together articles published in different volumes, issues or years.

An article can belong to several collections as well as an issue. For example, an article published in Volume 1 - Issue 2 can also be part of a collection. Each article has one **primary issue**, which is the issue deposited with its metadata and shared with indexing services. See [Managing the primary issue](#managing-the-primary-issue). The primary issue will also determine how an article is cited.

Staff can create other issue types in the admin area. A custom issue type works the same way as a collection and can have its own navigation link. For more on the admin area, see admin docs. <!--missing hyperlink cos I didnt write it yet-->

## Creating collections

You create collections in the **Issue manager**, the same way as issues.

1. Open the **Issue manager** from **Issues** in the sidebar, or from the manager dashboard.
2. Click **Create issue**.
3. Set issue type to 'Collection' by selecting it in the dropdown.
4. Enter a title Readers see this title on the collection's page.
5. Enter a volume and issue number. See [Setting a volume and issue number](#setting-a-volume-and-issue-number) for more information.
6. Set the date. The collection will appear on the journal website from this date forwards.
7. Optional: complete the other fields:
   - **Description**. This is displayed on the collection's page.
   - **Short description**. This is displayed shown on the collections list page.
   - **Cover image** and **Large image**. These will be displayed at the top of the collection's page and in the collections list; make sure to add alt text for each image. For recommended dimensions, see [Image guidelines](../journal-management/image-guidelines.md).
   - **Code**. This is used to give the collection a short web address. See [collection codes](#collection-codes).
   - **DOI** or **ISBN**. See [Crossref issue DOIs](../identifiers/crossref-issue-doi.md) for information on issue DOIs. Only use the ISBN if this collection has an ISBN, such as a conference proceeding.
8. Click **Add issue** to save the collection.

<!-- Insert iumage: the create issue form with issue type set to collection.
![The Create issue form, with the issue type field set to Collection](../images/create-collection.png) -->

### Adding articles to a collection

The easiest way to add articles to a collection is through the issue manager.

<!--imagy image missing-->

1. In the **Issue manager**, click **View** next to the collection.
2. In the **Table of contents** section, click **Add article**.
3. Click **Add** next to each article you want to include.
   You can reorder sections and articles, remove articles, and add guest editors, in the same way as for an issue. See [Managing existing issues](./issues-and-volumes.md#managing-existing-issues).

> [!NOTE]
> Collections only appear on the journal website once they contains at least one published article.

### Setting a volume and issue number

Janeway requires a volume and issue number for every collection. Choose numbers based on how the collection relates to your publication schedule:

- Ongoing collections  
   For a collection you will continue to add to, or a collection not tied to a specific year, use Volume 0. Give each collection its own issue number, starting from 1. The collections won't interrupt the issue listing this way and will be grouped together, as they are ordered by volume number.

- Collections within a specific year  
   For a collection that belongs to a specific year (e.g. winter collection), use that year's volume number and any issue number you like. The collection then sits in its chronological place among that year's issues in the **Issue manager** and front-facing issue list.

> [!WARNING]
> Never use Volume 0, Issue 0. Janeway places imported articles with no volume or issue number there. There is an existing Volume 0, Issue 0 when this happens a server error will occur.

To hide the volume and issue numbers and show only the collection's title, change the issue display settings. See [Display settings](./issues-and-volumes.md#display-settings). These settings apply to all issues and collections.

### Collection codes

If you enter a **Code**, such as `pynchon`, readers can reach the collection at `yourjournal.com/collection/pynchon/`. This address redirects to the collection's page. Codes can contain lowercase letters, numbers and hyphens, but no spaces or special characters.

### Managing the primary issue

Make sure each article in a collection also has a regular issue as its primary issue. The primary issue is the one deposited with the article's metadata, shared with indexing services and used in its citation. An article whose only issue is a collection is cited and indexed under that collection.

To check or change an article's primary issue, open the article's **Edit metadata** page and select an issue from the**Primary issue** dropdonw. You can only choose an issue the article already belongs to. See [Article metadata](../article-management/article-metadata.md).

## Displaying collections

Collections have their own pages on the journal website, separate from the **Issues** page. They can be found at `yourjournal.com/collections`. A collection with a future date, or with no articles, does not appear.

The collections list page shows every collection that has a date in the past and contains at least one article. For each collection, it shows the large image, title, date and short description.

![The collections list page, showing each collection's image, title, date and short description](../images/collections-list.png) -->

Each collection has its own page, with the same layout as an issue page. It shows the collection's large image, title, description and table of contents. The sidebar lists the journal's other collections.

![A collection page, showing the large image, title, description, table of contents and a sidebar listing other collections](../images/collection-page.png)
