# Discovery plugins

Discovery services help readers find your journal's content. The following functionalities are included in Janeway's core and do not require a plugin:

- [OAI-PMH](../identifiers/index.md#oai-pmh): a feed that harvesters use to collect metadata.
- [KBART](../identifiers/index.md#kbart): a title list that library knowledge bases use to record what content is available.
- [Google Scholar](../identifiers/index.md#google-scholar): article pages carry metadata tags that search engines read.
- [Crossref DOIs](../identifiers/crossref-article-doi.md): registering a DOI sends the article's metadata to Crossref, which shares it with many other services.
  For specific services, a system administrator can install a plugin. Most services need an account or agreement before they will ingest any data.

| Plugin                         | What it does                                                                                             | Status |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ------ |
| [DataCite](datacite.md)        | Registers DOIs with DataCite instead of Crossref                                                         | Active |
| [DOAJ](doaj.md)                | Sends article metadata to the Directory of Open Access Journals, automatically on publication or by hand | Active |
| [ScienceOpen](science-open.md) | Sends each issue's full text to ScienceOpen                                                              | Beta   |
| [EBSCO](ebsco.md)              | Sends each issue's full text to EBSCO                                                                    | Beta   |

<!-- Check: the status of the beta plugins -->

For services that collect files by FTP, see the [Production transporter](production-transporter.md) plugin.

For how discovery fits with the rest of Janeway's metadata, see [Metadata on Janeway](../guides/metadata-on-janeway.md#discovery).
