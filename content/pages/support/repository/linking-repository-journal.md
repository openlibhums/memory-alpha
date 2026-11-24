# Linking a repository and journal

A repository and the journals on the same press can be linked in two directions:

- From the repository to a journal: a moderator sends a preprint to a journal, which creates a submission in that journal.
- From a journal to the repository: the Isolinear plugin creates preprints from journal submissions.

## Sending a preprint to a journal

Repository moderators can send a preprint to any journal on the press. Janeway creates an article in the journal, at the workflow stage you choose.

1. In the **Repository manager**, click on the preprint's title to open it.
2. In the control panel, click **Send to journal**.
3. Find the journal in the list and click **Select**.
4. Complete the form:
   - **License**: the journal licence the article uses. The list shows the licences available on that journal.
   - **Section**: the article type in the journal.
   - **Stage**: the workflow stage the article starts in. The list shows the stages in that journal's workflow.
   - **Force**: tick this box to create a new article, even if this preprint has already been sent to a journal. The earlier article isn’t deleted, but it will no longer be linked to this preprint.
5. Click **Send to journal**.

Janeway shows the new article's ID and the journal's name. You can now find the article in the journal's workflow.

<!--add image-->

### New article metadata

The new article has:

- The preprint's title and abstract.
- The licence and section you chose.
- A copy of each of the preprint's authors. Authors who have an account are given the author role on the journal.
- The latest version of the preprint's file, as the manuscript file.
- The note "Submitted from" followed by the repository's name, in the comments to the editor.

The article's owner is the preprint's owner, and its submission date is the date you sent it.

### Sending a preprint again

A preprint can be linked to one article. If it has already been sent, the **Send to journal** page says which journal and article ID it went to. Sending it again doesn't create a new article.

<!--add image-->

To create a new article anyway, tick **Force**. Janeway creates a new article and links the preprint to it. The previous article stays in its journal, but is no longer linked to the preprint.

> [!CAUTION]
> **Force** doesn't delete the previous article. It stays in its journal's workflow until someone deals with it there.

### Published version notice

Once a preprint is linked to an article, its public page tells readers that a published version is available on the journal. The notice links to the article.

If a version of the preprint has a published DOI, the page shows that DOI instead.

<!-- Can someone check if this plays nice on 1.9 and the new branch? I am getting a server error -->

## Create preprints from journal submissions

The [Isolinear plugin](../plugins/isolinear.md) works in the other direction. It adds options to a journal's workflow:

- In **Unassigned**, editors can approve an article for preprint publication. This creates a preprint record of the article.
- In **Review**, editors can create a new preprint version from a revised manuscript.

Isolinear is a plugin, so it is only available where it has been installed. For how it works, see [Isolinear (preprints)](../plugins/isolinear.md).
