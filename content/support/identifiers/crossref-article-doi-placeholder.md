title: Crossref article DOI
# Crossref article DOI

Janeway can automatically register (also called "mint" or "deposit") Digital Object Identifiers (DOIs) for articles with Crossref, provided the journal’s settings are correctly configured.

This page explains:
- When DOIs are created and updated
- How to check and manage DOIs using the DOI Manager
- How to interpret DOI registration statuses
- Which Crossref settings are required

## When are DOIs minted?

If Crossref settings are correctly configured, Janeway handles DOI registration automatically at key points in the publishing workflow.

By default, Janeway registers a DOI with Crossref when an article is accepted for publication.

After acceptance, the DOI will exist in Crossref’s system. However, the web page it points to may not yet be live if the article has not been published. This is expected and does not indicate a problem.

Provisional metadata is sent, but no author-identifiable details are shared.

Later, when the article is scheduled for publication, Janeway sends a deposit to Crossref to update the metadata. 

When the article is published, the DOI becomes a working permalink to the published article.

> [!TIP]
> You can allow editors to preview the data that will be sent to Crossref before accepting an article.  
> See **Accept article warning** under **Review settings**.  
<!--missing hyperlink-->

## When manual intervention may be needed

The automatic workflow may be interrupted in some situations, for example:
- Importing backlist content.
- Missing or incomplete metadata.
- Incorrect Crossref settings.

In these cases, you may need to take action using the **DOI Manager**.

//

## DOI manager

The **DOI Manager** allows you to view and manage DOI registration statuses. If you are an editor at journal level or if you are a staff member at press level.

The DOI manager can handle up to 25 articles at a time. If your journal has more than 25 articles in total, use the filter to narrow the list of articles. You can filter by date, registration status, or primary issue until you have an actionable set of articles.

Once you have filtered the list, you can:

- **Register DOIs**  
  Sends the article metadata to Crossref for registration.

- **Poll for status**    
  Checks the DOI status of Janeway articles.

Crossref processes deposits in a queue, so status updates may not appear immediately. If you want to check the status of a DOI, you can use **Poll for status**.

> [!WARNING]
> Using **Poll for status** on a large number of articles could take a long time. You may wish to test a small set first when investigating potential issues.

In some cases, you can also preview the XML that will be sent to Crossref before registering.

## Interpreting registration status

Each DOI in the DOI Manager shows a registration status:

- Unknown   
    Janeway doesn't know the status. Try **Poll for status**.

- Not yet registered  
    This DOI hasn't been registered yet. You can register it if what you see in the **DOI** column looks right (including pattern previews).

- Queued at Crossref  
    The deposit has been received by Crossref and is waiting to be processed.

- Registered  
    Crossref successfully processed the metadata and didn't find any problems with it.

> [!TIP]
> A status of **Registered** does not necessarily mean the DOI will resolve correctly if the article is not yet published (or if the URL is not operational for other reasons).

- Registered (but some citations not correctly parsed)  
    Article metadata was accepted, but citation parsing errors occurred. Check the XML shown in the **Response** column for details.

- Registered with warning  
    The DOI was registered, but Crossref returned a warning. Check the **Response** column for more information.

- Registration failed  
    Crossref could not register the DOI due to an error. Check the **Response** column to identify the issue.

## Crossref settings

Crossref settings are configured from the Manager interface under **Crossref settings**. On this page, you will find the following fields used to configure Crossref:

- Use Crossref DOIs 
     Enables or disables DOI registration for the journal. If disabled, no DOIs will be minted.

Use Crossref test deposit server   
    Sends DOIs to Crossref’s test system instead of the live system. Useful for testing only.

- Crossref username  
    Your Crossref account username.

- Crossref password  
  Your Crossref account password.

- Crossref depositor email  
    The email address of the depositor.

- Crossref depositor name  
    The name of the depositor

- Crossref prefix  
  Your Crossref prefix, usually in the form `10.xxxx`.

- Crossref registrant name  
    The registrant name recorded with Crossref for this journal (for example, "Open Library of Humanities").

## DOI formatting settings

- DOI display prefix  
  Text added before the DOI when generating display URLs. Usually `https://doi.org/`.

- DOI display suffix  
    Text added after the DOI when generating display URLs. Usually left blank.

- DOI pattern 
    The DOI pattern controls how article DOIs are generated automatically. By default, Janeway uses the journal code and article ID, for example: `orbit.123`. Using the following objects:
    > `{% raw %}{{ article.journal.code }}.{{ article.pk }}{% endraw %}`

- Title DOI  
    The DOI for the journal itself (not in URL format), for example: `10.001/my-journal`. It is included on all deposits for this journal and, is using, must be registered ahead of time.

A journal DOI is only mandatory if a journal does *not* have an ISSN, as Crossref requires at least one unique identifier per journal.

However, Crossref recommends registering a journal DOI even when an ISSN exists. We recommend using your journal code
as the DOI. For example, with the prefix of `10.0001` and the journal code `abcd`, you could set the journal DOI to `10.0001/abcd`.