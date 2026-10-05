# Journal management at press level

Press managers use the press manager interface to add journals and set default settings for every journal. They also use it to control the press website and how journals are listed on it.

To open the press manager, sign in on the press website, select the account icon in the top-right corner, and then click **Manager**.

## Adding new journals

1. On the press manager, click **Add new journal** and a popup will open with fields to fill in.
2. Enter a code; a short abbreviation for the journal (not used for any other journal on the press), for example 'orbit' or 'jms'. In path mode, the code appears in the journal's web address. <!-- What is the code limit? Form says 15, DB says 40 -->
3. Optional: enter a domain if the journal will have its own web address. The domain must already be set up on your web server. \*If this is not yet set up, you can leave this blank and add it later.
4. At the bottom of the popup, click **Add new journal** to finish creating the new journal.

Janeway creates the journal and opens its **General settings** page, where you can add the journal name and other details. To continue setting up the journal, see [Creating a journal](../guides/journal-setup.md#creating-a-journal).

> [!TIP]
> Tick the **Hide from press** box on the journal's **General settings** page while you set it up. The journal then doesn't appear on the press website until it is ready.

## Path mode and domain mode

Janeway serves journals in one of two ways:

- Path mode  
   he journal shares the press domain and is identified by its code, for example 'www.pressdomain.com/orbit'.
- Domain mode  
   The journal has its own domain, for example 'www.orbitjournal.com'.

A journal in domain mode can still be reached through its press path. Janeway redirects visitors from the path to the journal's domain. This also gives you a fallback address if the journal's domain stops working, for example if it expires.

### Changing a journal's domain

1. On the press manager interface, find the journal in the journals table.
2. Click the **Edit** button in the **Domain** column.
3. Fill in the new domain, or clear the field to use path mode.
4. Click **Save**.

Using a custom domain requires DNS configuration. Contact your system administrator before you change a domain.

## Ordering journals

Journals appear on the press website in the order shown in the journals table on the press manager. On this table, you can drag and drop to reorder them. The new order saves immediately and automatically.

> [!NOTE] If **Order journals A-Z** is turned on in **Edit press details**, journals are listed alphabetically by name and the manual order is ignored. Alphabetical ordering does not work for translated journal names.

///

- Journal default settings
- Override journal settings
- Disabled journal display
- Custom journal description

The **Press manager** dashboard gives an overview of all journals on the press, the settings available at press level and settings to configure the press website.

## Configuring the press website

- Press settings
- Homepage manager
- Content manager
- News manager
- Contact manager

## Managing journals

- Add new journal
- Order journals
- Journal description as displayed in the list - will otherwise draw from journal made
- Direct link to journal settings

### Add new journal

\*Code is the only required one.
If using domain mode, it can always be configured later.

## Journal settings at press level

Settings worth considering setting at press level:

- User management <!-- missing hyperlink -->
- DOI settings
- Review settings
- One-click review
- User = author
- Review guidelines
- Copyright submission labels (may contain legal text) - can also be locked to be editable by press managers only.
- Google analytics code
- Journal default theme
- Login and registration page notices
- Publisher name and URL
- Support email and support message for staff
