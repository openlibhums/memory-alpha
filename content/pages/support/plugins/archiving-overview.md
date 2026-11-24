# Archiving plugins

Archiving services keep copies of your journal's content, so it stays available if your website changes or closes. Most archives also need publishers to be members or to have an agreement with them. Contact an archiving service first if you are not sure.

The following functionalities are included in Janeway's core and do not require a plugin:

- The [OAI-PMH feed](../identifiers/index.md#oai-pmh) lets archives harvest metadata, and JATS XML where it exists.
- [JATS XML](../guides/metadata-on-janeway.md#jats-xml) galleys, or JATS XML stubs that Janeway generates, give archives a standard format.
- Sitemaps list the pages on the press and journal websites.

For specific services, a system administrator can install a plugin:

| Plugin                                        | How content is sent                                                                          | What is sent                                               | Record kept in Janeway |
| --------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------- |
| [Portico](portico.md)                         | The plugin can auto-desposit or an editor can send each issue manually from the plugin page. | PDF and XML                                                | In the admin area      |
| [CLOCKSS](clockss.md)                         | CLOCKSS collects content from the journal website.                                           | Full article metadata and content on the journal's domain. | No                     |
| [Library of Congress](library-of-congress.md) | The plugin can auto-desposit or an editor can send each issue manually from the plugin page. | PDF and XML                                                | No                     |

If an article has no XML galley, the Portico and Library of Congress plugins send a JATS XML stub instead.

The [Production transporter](production-transporter.md) plugin sends articles to an FTP server, for other services that collect content that way.

For how archiving fits with the rest of Janeway's metadata, see [Metadata on Janeway](../guides/metadata-on-janeway.md#archiving).
