# Metadata on Janeway

Janeway collects metadata about articles, authors and issues, and shares it with indexes, discovery services and archives. This guide explains how metadata gets into Janeway, which standards it uses, and where it goes.

## Managing metadata

Most article metadata is collected during submission. Authors enter the article's title, abstract, keywords, author details and other information in the submission form. Editors can then check and change it at any stage of the workflow, and after publication.

The fields authors see depend on how the journal is set up, see the following pages for more information on this:

 - [Managing submission fields](../submission/managing-submission-fields.md) explains how to choose which standard fields appear, and how to create custom fields.
- [Article sections](../article-management/article-sections.md) explains how to set up the article types authors choose from.
- [Licence manager](../submission/licence-manager.md) explains how to set up the licences available to authors.

For informaiton on managing metadata after the article has been submitted:

 [Article metadata](../article-management/article-metadata.md) explains how to view and edit an article's metadata, for both unpublished and published articles.
- [Issues and volumes](../issues-volumes-and-collections/issues-and-volumes.md) explains how to create and edit issues; their titles, numbers and dates.

You can also add metadata in bulk, instead of through the submission form. See [Importing metadata](#importing-metadata).

### Author metadata

Author records include name, email, biography, affiliations, and optional contributor roles, including structured persistent identifiers for people, organizations, and roles. These records are created by authors during the article submission phase, and they remain with the article permanently. Editors can change them throughout the workflow stages as needed.

> [!NOTE]
> Technically, editors can also change author records after publication, to handle important name changes when requested. But it is best to avoid edits after publication if possible, and it may not always be possible to change the name everywhere it appears, in search results, discovery services, and typeset versions of the article.

Records for authors are distinct from user accounts. So if you choose to delete your user account after you publish an article, or if your affiliations change, your author record remains intact, to maintain a public record of your authorship at the time of publication.

If you are a correspondence author, you must have a user account linked to your author record. But if another author is handling the correspondence, you do not need to have an account.

Janeway remembers the order of author records, as set by the submitting author. Editors can change it later too if needed. This order is used to set the sequence of author names wherever they are output in metadata or displayed to readers.

> [!TIP]
> For ease of use and better metadata, authors with ORCID accounts are encouraged to use the ORCID login option, and anyone creating affiliations should choose from the list of provided institutions rather than manually entering custom institutions.

## Metadata standards

Janeway integrates with a number of common open metadata standards to support interoperability, discovery, and data management.

### Research Organization Registry (ROR)

To assess the reach of publishing activities, it can be valuable to group publications by the research organizations that stand behind them. However, problems arise when people describe their affiliations in slightly different ways, when organizations have names in more than one language, or when two organizations have the same name.

These problems are solved by the [Research Organization Registry](https://ror.org/). They assign persistent identifiers to organizations, like DOIs for articles, ORCIDs for people, and ISBNs for books. This allows multiple names to be associated with a single organization, for easier discovery and display, and it adds to the possibilities for linked open data. The ROR team regularly updates and maintains the registry, which in 2025 included more than 114,000 entries from around the world.

Janeway integrates with ROR from the point of submission through to publication and metadata distribution. When authors first submit a manuscript to a Janeway journal, they are asked to search in registry data for their affiliated institutions. And if they signed in via ORCID, Janeway pulls over their primary affiliation from their public ORCID profile, usually with ROR IDs in tow. Other users such as editors can also create affiliations that are connected to ROR data.

When Janeway metadata is distributed, the persistent identifier is provided alongside the organization names. This way, other platforms and discovery services can understand Janeway affiliation metadata unambiguously and programmatically, without the need for intensive data curation, cleaning, or matching.

ROR data is available from Janeway in these places:

- Journal article web pages (HTML)
- Auto-generated JATS XML stubs
- [Crossref deposits (XML)](../identifiers/crossref-article-doi.md)
- The OAI-PMH feed (XML)
- The Open Access Switchboard (via the [**OA Switchboard** plugin](../plugins/oaswitchboard.md))

<!--
  Future development
  - the repository system
  - reports (via the **Reporting** plugin)
  - metadata imports and exports (via the **Imports** plugin)
  - Datacite deposits (via the **Datacite** plugin)
  - the **Supporters** plugin
-->

Typesetters have access to ROR data and are encouraged to encode it in any JATS XML they produce for Janeway.

### Contributor Role Taxonomy (CRediT)

What does an author do? What do coauthors do? Many things, and not always the same ones. How do you represent this in metadata?

The [CRediT system](https://credit.niso.org/) standardizes fourteen roles that are common in collaborative research and authorship, with names like "Conceptualization" and "Writing - original draft." If a journal chooses to turn this system on, each contributor's effort can be described with one or more of these terms.

Each CRediT term is connected to a persistent identifier with a URI form, so CRediT data can be used in linked data environments alongside ORCIDs and ROR IDs.

CRediT data is distributed by Janeway in these places:

- on journal article web pages (HTML)
- in auto-generated JATS XML stubs
- the OAI-PMH feed (XML)
- the Open Access Switchboard (via the [**OA Switchboard** plugin](../plugins/oaswitchboard.md))

<!--
  Future development
  - in Crossref deposits (XML)
  - metadata imports and exports (via the **Imports** plugin)
  - the repository system
  - Datacite deposits (via the **Datacite** plugin)
-->

<!-- missing hyperlinks -->

Typesetters have access to CRediT data and are encouraged to encode it in any JATS XML they produce for Janeway.

## Exporting metadata

Janeway makes metadata available in several formats, some with and some without any plugins. Most of these are read automatically by indexes, discovery services and archives.

### OAI-PMH feed

OAI-PMH is a standard way for other systems to harvest metadata. Janeway's feed is at `/api/oai/`, added to the journal's web address, for example `https://yourjournal.org/api/oai/`. The same address on the press website covers every journal that isn't hidden from the press. A repository's feed lists its preprints.

The feed offers two metadata formats:

- Dublin Core (`oai_dc`), the default.
- JATS (`jats`). If an article has a JATS XML galley, the feed uses it. Otherwise, Janeway generates a JATS XML stub with the article's essential metadata.

Records are grouped into sets by journal, issue and section. For more, see [OAI-PMH](../identifiers/index.md#oai-pmh).

### KBART

KBART is a title list format that libraries and knowledge bases use to record which journals and issues are available. Janeway's KBART list is at `/api/kbart/` (tab-separated) or `/api/kbart/csv` (comma-separated), added to the journal or press web address. For more, see [KBART](../identifiers/index.md#kbart).

### Article page metadata

Each published article page carries its metadata in the page's code, in two formats:

- Google Scholar tags, such as `citation_title`, `citation_author` and `citation_pdf_url`.
- Dublin Core tags, such as `DC.Title` and `DC.Identifier.DOI`.

Search engines and reference citation software use these tags.

## JATS XML

JATS is the standard XML format for journal articles. If a typesetter provides a JATS XML galley, Janeway uses it for the article page. It also shares it through the OAI-PMH feed and some archiving plugins. Otherwise, Janeway generates a JATS XML stub with the article's essential metadata.

### Spreadsheet export

Users with staff permission can export article metadata as a CSV file from the **All articles** page. See [Import, export, update](../plugins/import-export-update.md#exporting). This functionality requires the Imports plugin to be installed.

### DOI registration

When Janeway registers DOIs, it sends article and issue metadata to Crossref or to DataCite through a plugin. See [Identifiers and discovery](../identifiers/index.md).

## Discovery

Discovery services help readers find a journal's content. Janeway supports discovery in two broad ways:

- Built-in features that services read automatically:
  - DOI registration with Crossref sends metadata to Crossref, which shares it with other services.
  - Article page metadata lets Google Scholar and other search engines index articles.
  - The OAI-PMH feed lets harvesters collect metadata.
  - The KBART list tells library knowledge bases which content is available.
  - Sitemaps (`/sitemap.xml`) list the pages on the press and journal websites for search engines.
- Plugins that send metadata or content to a particular service:
  - [DOAJ](../plugins/doaj.md) sends article metadata to the Directory of Open Access Journals.
  - [DataCite](../plugins/datacite.md) registers DOIs with DataCite instead of Crossref.
  - [ScienceOpen](../plugins/science-open.md) sends each issue's full text to ScienceOpen.
  - [EBSCO](../plugins/ebsco.md) sends each issue's full text to EBSCO.
  - There are various other generic plugins available as well, such as the FTP plugin, that can be used for indexing, archiving and discovery.

Most services need an account or agreement with them before you can sent content. For more, see [Discovery plugins](../plugins/discovery-overview.md).


<!-- ## Metadata streams

- DOI manager
- Downstream dataflows

## Importing metadata

- Import spreadsheet. See import plugin.

## Exporting metadata

- OAI PMH
  Journal/api/oai
- KBART
- Frozen author metadata
- Export plugin. -->
