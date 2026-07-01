title: DataCite plugin

# DataCite plugin

[GitHub Repo](https://github.com/openlibhums/datacite)

The DataCite plugin is an alternative to Janeway's built-in Crossref support. It registers Digital Object Identifiers (DOIs) with [DataCite](https://datacite.org/) rather than Crossref, and it manages the deposit itself through DataCite's REST API. DOIs are still stored on the core identifier record for each article, so the rest of Janeway treats a DataCite DOI the same way it treats any other DOI.

Use this plugin when your membership is with DataCite instead of, or in addition to, Crossref.

> [!NOTE]
> The DataCite and Crossref tools are independent. If you register a DOI with DataCite, do not also register the same article with Crossref.

## Before you start

A server administrator sets your DataCite credentials (username, password, and DOI prefix) when the plugin is installed. These values are not editable from the journal interface, so contact your administrator if they need to change.

While a site runs in debug mode, the plugin deposits to DataCite's test API rather than the live one. DOIs minted against the test system do not resolve and are periodically cleared by DataCite.

## Opening the plugin

To open the plugin, go to the manager and select **DataCite** from the list of plugins. The plugin's home page gives you three options:

- **Settings** controls automatic deposit for the whole journal.
- **Article List** lists articles and lets you mint DOIs by hand.
- **Section Controls** limits automatic deposit to chosen sections.

## Understanding DOI states

DataCite DOIs move through states, and this plugin uses two of them:

Draft (registered)  
The DOI and its metadata are stored at DataCite but the DOI does not resolve publicly. This is used before an article is published.

Findable (published)  
The DOI resolves to the article and its metadata is indexed. This is used once the article is published.

The plugin sends a draft deposit when an article is accepted and upgrades it to findable when the article is published.

## Registering DOIs automatically

Automatic deposit is the recommended approach for new content. When it is enabled, Janeway deposits DOIs for you at two points in the workflow:

1. When an article is accepted, Janeway mints a draft DOI and saves it to the article.
2. When the article is published, Janeway upgrades that DOI to findable so it resolves to the published page.

Minted DOIs follow the pattern `prefix/journalcode.articleid`, for example `10.0001/tester.42`.

To turn automatic deposit on:

1. On the plugin home page, select **Settings**.
2. Select **Enable Datacite Auto Deposit**.
3. Select **Save**.

### Limiting automatic deposit to certain sections

By default, automatic deposit applies to every section of the journal. You can restrict it to specific sections. For example, you can mint DOIs for research articles but not editorials.

Section controls only take effect while automatic deposit is enabled for the journal.

To choose which sections mint DOIs:

1. On the plugin home page, select **Section Controls**.
2. Select each section that should mint DOIs.
3. Select **Save**.

> [!NOTE]
> If you do not select any sections, Janeway mints DOIs for all sections.

## Registering DOIs manually

Automatic deposit does not cover every case. You may need to register DOIs by hand when you import back content, when deposit was turned on after some articles were already accepted, or when an earlier deposit did not complete.

The **Article List** shows every accepted article for the journal, alongside whether it already has a DOI.

To register a DOI for an article that does not have one:

1. On the plugin home page, select **Article List**.
2. Find the article and select the option to mint its DOI.
3. Check the identifier. Janeway suggests one that follows your prefix and journal code, but you can edit it.
4. To register the DOI as findable straight away, leave **Findable** selected. To register a draft DOI that does not yet resolve, clear the checkbox.
5. Select **Save**.

Janeway deposits the metadata with DataCite and, if the deposit succeeds, saves the DOI to the article. If the deposit fails, Janeway shows the error returned by DataCite so you can correct the metadata and try again.

For an article that already has a DOI, minting again from the **Article List** re-sends the current metadata to DataCite as a findable deposit. Use this after correcting metadata to bring DataCite's record up to date.

> [!TIP]
> To see the exact metadata Janeway will send, use the article's export option. It returns the DataCite JSON for that article without depositing anything.
