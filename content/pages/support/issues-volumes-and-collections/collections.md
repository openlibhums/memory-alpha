# Collections

Collections are one of Janeway's built-in issue types, alongside issues. A collection groups related articles from across your journal, for example on a shared theme. Unlike an issue, a collection doesn't have to follow your journal's publication sequence. It can bring together articles published in different volumes, issues or years.

An article can belong to several collections as well as an issue. For example, an article published in Volume 1 - Issue 2 can also be part of a collection. Each article has one **primary issue**, which is the issue deposited with its metadata and shared with indexing services. See [Managing the primary issue](#managing-the-primary-issue). The primary issue will also determine how an article is cited.

Staff can create other issue types in the admin area. A custom issue type works the same way as a collection and can have its own navigation link. For more on the admin area, see admin docs. <!--missing hyperlink cos I didnt write it yet-->

## Creating collections

You create collections in the **Issue manager**, the same way as issues.

1. Open the **Issue manager** from **Issues** in the sidebar, or from the manager dashboard.
2. Click **Create issue**.
3. Set **Issue type** to **Collection** by selecting it in the dropdown.
4. Enter a **Title**. Readers see this title on the collection's page.
5. Enter a **Volume** and **Issue** number. See [Choose a volume and issue number](#choose-a-volume-and-issue-number) for more information.
6. Set the **Date**. The collection will appear on the journal website from this date forwards.
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

///

Collections differ in so much as they are not a primary issue for a paper but tend to be collections of papers with similar topics across multiple issues. So an article may be in the Thomas Pynchon Collection but its primary issue may be Volume 1 Issue 2 2019. You can also define your own issue types in the Django admin area. <!-- missing hyperlink -->

Volume 0 can be helpful for collections, if you do not wish for the collections to follow or interrupt the regular Volume-Issue order. (E.g. for collections you may continuously add to and aren't part of specific years.)

## Creating collections

## Displaying collections
