# Janeway analytics

Janeway tracks views and downloads for articles, and can report on this activity across your journal or press. This section explains what analytics data is available and how to access it.

- [Reporting](./reporting.md)  
  A breakdown of the reports available through the Reporting plugin, including press reports, journal usage by month, article metrics, citations and more.
- Google Analytics  
  _Coming soon_ — connecting Google Analytics to your journal for additional web traffic insights.

## Institutional statistics

Janeway cannot provide usage statistics broken down by institution, since this would require tracking readers behind a paywall in a way Janeway does not support. Author, reviewer and editor affiliation data is available where it has been saved as part of a frozen author record.

## How Janeway measures access

<!--

Janeway VS COUNTER.

- How do we measure stats and how does meet COUNTER requirements.

This section needs dev input.

-->

### Article access logs

Most of the time, when an article is viewed or downloaded, Janeway records an **Article access** log. These logs are the basis of data in the Reporting plugin.

Logs include a few non-personal details of the action:

- Whether the user is viewing or downloading
- What type of galley is provided
- What country the user is accessing from

#### Article views by type

Here are the most common ways an article is viewed.

- No galley (a.k.a “abstract”)  
  A view of a webpage for an article that has been published without any galleys. Because no galley has been made public, the user can only see metadata like title, abstract, and authors, not the full text content.
- XML  
  A view of a webpage for an article that has been marked up as JATS-XML and uploaded with an XML galley. The XML galley has been converted to HTML and the full text of the article has been rendered in the webpage for the user to read in their browser.
- HTML  
  A view of a webpage for an article that has been marked up as HTML, sometimes via pandoc conversion from Word. The HTML galley has been rendered in the webpage for the user to read in their browser.
- PDF  
  A view of a PDF loaded in the user’s browser or other window (depending on user preferences outside of Janeway), after they’ve clicked **View PDF** on the article webpage. This link only appears if the journal has ticked **View pdf button** on the **Article settings** page.

#### Article downloads by type

Here are the most common ways an article is downloaded.

- XML  
  A download of a raw JATS-XML file, after the user has clicked **Download XML** on the article webpage.
- HTML  
  A download of a raw HTML file, after the user has clicked **Download HTML** on the article webpage. This option only appears if the journal has left unticked **Disable html downloads** on the **Article settings** page.
- PDF  
  A download of a PDF file after the user has clicked **Download PDF** on the article webpage.

Other less common galley types are possible. If any of these are uploaded, new links to download them appear on the article page, and new article downloads for these types can be logged in the article’s metrics.

- EPUB
- Word (DOC)
- Word (DOCX)
- OpenDocument Text Document (ODT)
- LaTeX
- RTF
- Other
- Image

#### Events that are not logged

There are some interactions with article content that are _not_ recorded as **Article access** logs.

- If a web crawler identifies itself as such (like a search engine crawler or archive indexer), it can access article pages and galley files without triggering an article access log.
- Downloads of full journal issues are available, including galley files. When a user downloads a full issue of files, no article access is logged.
- If there is an XML or PDF galley available, there is a hidden link in the HTML metadata of every article webpage that indexers can use to get the raw file . (It is worth having this link in addition to the user-facing download links because it is provided with a recognizable name that indexers know to look for, `citation_xml_url` or `citation_pdf_url`.) Visits to this link are not logged.
- In the citation section of article metadata, users can download metadata in RIS or BIB formats without triggering any article access log.
- The APIs Janeway provides (JSON and OAI-XML), do not trigger article access logs unless one of the full-text article links is followed.

#### Avoiding duplicate logs

If a user refreshes a page or clicks on a download link again soon after their first visit, Janeway does not record another access. For most users, the time frame for not counting duplicates is two weeks, because Janeway can recognize their browser session by using a safe cookie. If an article is visited in such a way that only the IP address can be checked, the time frame is one hour.

However, there may be multiple access events if the user takes multiple actions, such as both viewing and downloading, or downloading multiple galley types.

Similarly, if a user accesses an article on multiple devices, such as their laptop and their phone, multiple events will be recorded.

> [!NOTE]
> Janeway needs to use IP addresses to make sure double-clicks or page refreshes are not recorded as new events, but we do not store original IP addresses, only fingerprints (hashes) that cannot be used to recover the original.

#### Filtering out bad traffic

It is up to server administrators who install and run Janeway to make sure that the installation is not bogged down with exploitative traffic from bots and scrapers. This is because the most effective solutions sit outside Janeway and filter out bad actors before they reach the application layer.

With OLH-managed installations, we currently use two methods:

- Since 2025, after a sharp rise in extractive LLM-related traffic, we are trialling using a web firewall utility like Anubis, which poses an algorithmic challenge that makes it computationally expensive for most extractive crawlers to continue. Recognized traditional search and archive indexers like Google Scholar, Crossref, Web of Science, EBSCO, and Proquest are able to pass through this firewall. Other indexers like DOAJ receive content by direct deposit and so are not affected.
- We limit the rate of lots of traffic that comes in rapid succession from the same actor.

### COUNTER and Janeway

Janeway does not yet fully support [COUNTER](https://www.countermetrics.org/), a global standard for usage metrics.

The only current COUNTER metric Janeway could potentially provide is the total global usage per item, journal, or press. This information is available through the [Reporting plugin](reporting.md).

#### COUNTER’s focus on institutional metrics

COUNTER has historically been focused on showing usage attributable to a particular institution, so that the institution’s subscription cost for paywalled content can be justified. This is why some of the most widely used COUNTER reports omit “Open” and “Free to read” content.

There are some reports that include “Open” and “Free to read” content, but these reports are less meaningful if the usage cannot be attributed to an institution, according to libraries we have worked with in the past.

As a diamond open-access platform, Janeway does not track readers’ institutions. Readers are not required to log into anything, and we avoid making inferences about IP addresses. As a result, we would not be able to provide institution data in any COUNTER reports, were we to implement the standard. This is one of the main reasons we have not yet implemented COUNTER.

#### Comparison to COUNTER usage data processing rules

Janeway and COUNTER have some of the same methods for processing usage data. These include rules around HTTP status codes, filtering double-clicks, and counting unique items (articles) and titles (journals).

There are also several differences that are worth noting.

- COUNTER recommends blocking bots and crawlers with a block-list, whereas we use the methods described in [Filtering out bad traffic](#filtering-out-bad-traffic)
- COUNTER makes a distinction in how fully the user accesses or captures the content of an item, which they call the metric type. They categorize more surface encounters like viewing of metadata records and sharing a link to an item with someone else “investigations”, and they categorize more substantive views or downloads of full text or actual content “requests”. Janeway does not distinguish between these types, and instead either records the access or not, depending on which link is used, and whether the actor can get through the firewall, as described above.
- COUNTER requires a separate access method for text and data mining (TDM), whereas Janeway does not make a distinction between TDM and other requests.
- COUNTER requires usage data to be available programmatically via an API with a standardized JSON/TSV structure, whereas Janeway usage data is provided with a custom data model and is not available via an API.
- COUNTER has rules for counting searches in databases, whereas Janeway does not track any search activity, except if a user visits an article page as described above.

> [!NOTE]
> This section was written with COUNTER 5.1.1 as a reference.
