title: Crossref issue DOI
# Crossref issue DOI

Janeway supports registering (minting) DOIs for journal issues, in addition to article-level DOIs. Issue DOIs are not registered independently. Instead, they are registered with Crossref when an article in the issue has its article DOI minted. The issue DOI is included in the XML send to Crossref, which will then mint the issue DOI. Only the primary issue to which an article is assigned will have its DOI minted.

>[!NOTE]
> If an issue contains no articles for which it is the primary issue, its DOI will not be minted.

Issue-level DOIs can be generated automatically using a defined pattern or entered manually on a per-issue basis.

This page explains how issue DOIs are generated, when they are registered with Crossref, and important limitations to be aware of.

## Auto-register issue-level DOIs  
When **Auto-register issue-level DOIs** is enabled in the **Crossref settings**, Janeway will generate an issue DOI and register it with Crossref.
The issue DOI is registered when the first article in the issue has its article DOI minted or is scheduled for publication (this will depend on what the article has its issue set, for more information see: Crossref article DOIs <!-- missing hyperlink -->). The issue DOI is included in the article’s XML metadata sent to Crossref, and no separate action is required to register it.

> [!IMPORTANT]
> If auto-registration for issue DOIs is enabled, issue DOIs should not be entered manually. To manually set issue DOIs, you must first disable automatic issue DOI registration.

<!--  Dev check needed here. The old docs say:
 If an issue
DOI has not been entered manually, Janeway will use the pattern defined
in the setting above to generate one automatically.

The helptext on the page, however, implies the manual field needs to be left blank. But the above implies otherwise, so I may need to check this. Does manual work, even if autoregister is on, as long as you set it before autoregister has a chance to kcik in? Or do they not play nice and is that the end of it? -->

## Issue DOI pattern  

Janeway can automatically generate issue-level DOIs using a configurable pattern.

Using the default pattern:
- An issue with ID `1`, journal code `abcd`, and prefix `10.0001` will be assigned the DOI:  
  `10.0001/abcd.issue.1`.

- A collection with ID `2` will be assigned the DOI:  
  `10.0001/abcd.collection.2`

This pattern is used only if an issue DOI has not been entered manually.

### Issue DOIs

Issues can be assigned a DOI in Janeway. This can be done ad-hoc for
each issue by editing the issue details and inputting the DOI manually,
or by letting Janeway generate a DOI for you, based on a pattern (a DOI
pattern can be set from the Crossref Settings page)

When the Crossref integration is enabled, issue DOIs will be registered
with Crossref whenever an article in that issue is registered with
Crossref. This will be the case both for DOIs generated for Janeway as
well as for those manually set.

> [!TIP]
> If you are migrating a Janeway installation from a version that did not
support issue DOIs and would like to register issue DOIs for your back
content, this can be done by populating the DOI field on those issues
and then re-registering any of the articles in the issue with Crossref.

> [!WARNING]
> When an article is part of two or more issues, only the primary issue
DOI will be registered with Crossref. In a future version, it will be
possible to register issue DOIs on their own, even when they have no
articles or all its articles are part of multiple issues.
