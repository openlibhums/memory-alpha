Issue DOI Pattern  
Janeway supports minting DOIs for journal issues automatically. With
this setting, you can define the pattern used to generate the
issue-level DOI that will be used for registration.

With the default pattern, an issue with ID `1` (and prefix `10.0001`,
and journal code `abcd`) will have a generated DOI of
`10.0001/abcd.issue.1`.

A collection with an ID of `2` would have a generated DOI of
`10.0001/abcd.collection.2`.

Auto-register issue-level DOIs  
When enabled, issues will have a DOI assigned and registered as soon as
the first article in the issue is scheduled for publication. If an issue
DOI has not been entered manually, Janeway will use the pattern defined
in the setting above to generate one automatically.


**Taken from issues, currently duplicate:**

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
