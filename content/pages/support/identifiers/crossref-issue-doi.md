# Crossref issue DOI

Janeway supports registering (minting) DOIs for journal issues, in addition to article-level DOIs. Issue DOIs are not registered independently. Instead, they are registered with Crossref when an article in the issue has its article DOI minted. The issue DOI is included in the XML send to Crossref, which will then mint the issue DOI. Only the primary issue to which an article is assigned will have its DOI minted.

> [!NOTE]
> If an issue contains no articles for which it is the primary issue, its DOI will not be minted.

Issue-level DOIs can be generated automatically using a defined pattern or entered manually on a per-issue basis.

This page explains how issue DOIs are generated, when they are registered with Crossref, and important limitations to be aware of.

## When and how issue DOIs are formed

When a new issue is created, and at any time after, editors can put in a manual DOI for an issue.

If no DOI is manually put in by the time the first article is added to the issue, then one will be automatically created based on the issue DOI pattern.

Here are a few examples of how the default pattern works:

- An issue with ID `1`, journal code `abcd`, and prefix `10.0001` will be assigned the DOI:  
  `10.0001/abcd.issue.1`.

- A collection with ID `2` will be assigned the DOI:  
  `10.0001/abcd.collection.2`

An auto-generated issue DOI can be edited afterward if needed, though this can cause problems if the DOI is already registered and the registration is not subsequently updated.

> [!TIP]
> Janeway never overwrites manually input DOIs, and what it sends for registration always matches the value you see in the DOI field.

## Auto-register issue-level DOIs

When **Auto-register issue-level DOIs** is enabled in the **Crossref settings**, Janeway will register the DOI that appears in the issue DOI field with Crossref. This could be a manually entered DOI or an auto-generated one.

The issue DOI is registered when the first article in the issue has its article DOI minted (for more information see: [Crossref article DOIs](./crossref-article-doi.md)). The issue DOI is included in the article's XML metadata sent to Crossref, and no separate action is required to register it.

> [!TIP]
> If you are migrating a Janeway installation from a version that did not
> support issue DOIs and would like to register issue DOIs for your back
> content, this can be done by populating the DOI field on those issues
> and then re-registering any of the articles in the issue with Crossref.

> [!WARNING]
> When an article is part of two or more issues, only the primary issue
> DOI will be registered with Crossref.
