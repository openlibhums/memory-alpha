# Identifiers & discovery

Janeway supports minting Digital Object Identifiers (DOIs) for articles and issues through Crossref and DataCite. This section explains how DOIs are generated and registered, and covers other identifier and discovery services relevant to your journal.

- [Crossref article DOI](./crossref-article-doi.md)  
  When article DOIs are minted, how to check and manage them using the DOI Manager, and the Crossref settings required.
- [Crossref issue DOI](./crossref-issue-doi.md)  
  How issue-level DOIs are generated and registered alongside article DOIs, and important limitations to be aware of.
- [DataCite DOIs](../plugins/datacite.md)  
  Registering DOIs with DataCite as an alternative to Crossref.

## Google Scholar

Google Scholar indexing is automatic; they use a webcrawler that looks for relevant materials (articles, monographs, preprints, reports, etc). It takes some time for new journals to appear on Google Scholar and for changes to existing content to show. [Google Scholar advises](https://scholar.google.com/intl/en/scholar/inclusion.html#troubleshooting) it may take 6-9 months for changes to appear.

If your journal is not properly indexed contact your system administrator or Janeway support.

If you experience issues with the metadata, the first step is to compare the galleys against the meta-tags in the HTML for any mismatches.

## OAI-PMH

OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) is a standard way for other systems to collect metadata from Janeway. Archives and aggregators use it, for example. Janeway provides an OAI-PMH feed without any plugins.

The feed's address is `/api/oai/`, added to the web address of the site you want to harvest:

- A journal: `https://yourjournal.org/api/oai/`. If your journal uses a path, add the feed address after the journal code, for example `https://yourpress.org/yourjournal/api/oai/`.
- The press: `https://yourpress.org/api/oai/`. This covers every journal that isn't hidden from the press.
- A repository: the same address on the repository's website lists its preprints.

The feed supports the standard OAI-PMH requests, including `Identify`, `ListRecords`, `ListIdentifiers`, `GetRecord`, `ListMetadataFormats` and `ListSets`. If a request doesn't say which one, the feed lists records. For example:

- `https://yourjournal.org/api/oai/?verb=Identify` describes the feed.
- `https://yourjournal.org/api/oai/?verb=ListRecords&metadataPrefix=jats` lists records in JATS.

The feed offers two metadata formats:

- Dublin Core (`oai_dc`), this is the default.
- JATS (`jats`). If an article has a JATS XML galley, the feed uses it. Otherwise, Janeway generates a JATS XML stub with the article's essential metadata.

Records are grouped into sets by journal, issue and section.

## KBART

KBART (Knowledge Bases and Related Tools) is a format for title lists. Libraries and knowledge bases use it to record which journals, volumes and issues a publisher makes available. Janeway produces a KBART list without the need for any plugins.

The list is at the following addresses, added to the journal or press web address (see OAI-PMH for a more in-depth explanation of these links):

- `/api/kbart/` gives a tab-separated (TSV) file.
- `/api/kbart/csv` gives a comma-separated (CSV) file.

A journal's address gives a list for that journal. The press address lists every journal that isn't hidden from the press. Journals marked as remote are never included.

<!--I assume we did complete the 'IF hide from press = TRUE' update? -->

Each row describes one journal, including its title, ISSNs, web address, publisher, and the dates and numbers of its first and last issues online.

If your journal is subject to an embargo, set it in **Embargo period (KBART)** on the **All settings** page. Use the KBART format, for example `P1Y` or `R2Y`. See [Journal settings](../journal-management/journal-settings.md).

## CRediT

CRediT (Contributor Role Taxonomy) describes what each author contributed to an article. Janeway can collect CRediT roles for each author and shares them in its metadata. See [Contributor Role Taxonomy (CRediT)](../guides/metadata-on-janeway.md#contributor-role-taxonomy-credit).

## ORCID

ORCIDs identify researchers. Users can sign in to Janeway with ORCID, and authors' ORCIDs are included in Crossref deposits and JATS XML stubs. See [ORCID login](../accounts-and-roles/orcid-login.md).

## Funder information

Authors can add funding information during submission. They search the Crossref Funder Registry (previously FundRef) for each funder, or enter the details by hand, and can add a grant ID. See [Funding](../guides/author-guide.md#funding) in the author guide.

When Janeway registers an article's DOI with Crossref, it includes each funder's name, its Funder Registry identifier and the grant ID, if these were provided in the submission.

## More metadata

For how Janeway uses metadata standards, and how metadata reaches discovery services and archives, see [Metadata on Janeway](../guides/metadata-on-janeway.md).
