# Setting up your journal

This guide takes you through setting up a journal on Janeway, from creating it to opening submissions. The stages appear in the order you would normally work through them, and each one links to a reference page if you need more detail.
 
You do not have to do everything in one sitting. Most settings can be changed later, and the guide flags the few that are awkward to undo.

## In this guide

## Before you start

### Information to keep to hand

Keeping this information on hand will make the set up process easier:

- The journal title and code (an abbreviation for the journal - this may show up in the DOI and URL).
- Journal ISSN, if you have one.
- Publisher name, website and contact email address.
- Journal logo, default issue cover, default banner image.
- If using, your Crossref prefix and credentials.
- The names and email addresses of editors.

Optional information that may be helpful:
- A postal address, if your indexers require one.
- The names and addresses of your editorial board.
- A list of the licenses used for the journal.

### Who can set up a journal

Creating a journal happens at press level and needs staff permission. If you are an editor, you cannot do this step yourself.
 
> [!NOTE]
> If a journal does not exist yet, ask your press manager or system administrator to create it. Once it exists and you have the editor or journal manager role, you can work through the rest of this guide.
 
Everything after [Creating a journal](#creating-a-journ) is available to editors and journal managers, with two exceptions noted in the text: press-level settings and the admin area.
 
For a full breakdown of who can do what, see [Roles and permissions on Janeway](../accounts-and-roles/roles-and-permissions-on-janeway.md). If you have not worked in Janeway before, read [Navigating Janeway](./navigating-janeway.md) first so the interfaces mentioned below make sense.

## Stage 1

###  Creating a journ

A press manager creates the journal from the **Press manager**, clicking **Add new journal**.
 
![The Add new journal form in the Press manager](../images/add-new-journal.png)
 
Three pieces of information matter at this point:
 
- Journal code  
  A short abbreviation or word that identifies the journal, for example `orbit`. In path mode, this appears in the journal's web address.

- Journal name  
  The full title of the journal, as you want it to appear to readers, this will be filled in on the next page

- Domain  
  Only needed if the journal runs on its own domain.

The code is the only required field. If you are using domain mode, you can configure the domain later.
 
Janeway serves journals in one of two ways:
 
- Path mode  
  All journals share the press domain, and the journal code identifies each one, for example `www.pressdomain.com/orbit`.

- Domain mode  
  Each journal has its own domain, for example `www.myjournal.com`.

After clicking **Add new journal** you are taken to the new journal's general settings page. 

It is recommended to enable **Hide from press** whilst you are setting up the journal, so it cannot be accessed by visitors from the press webpage.

### Set the general settings

After creating a journal and clicking  **Add new journal**, you are automatically taken to the new journal's general settings page. You can also find this page on the manager dashboard and then go to **General** under **Journal settings**.
 
![Where the find the general settings.](../images/manager-general.png)

On the general settings page, you may wish to work through the following settings:

- Journal information  
  Title, ISSN, description and keywords.


- Publisher information  
  Publisher name, website, and contact details. The latter (potentially including an address) may be required by certain indexers.

- Email settings.
  The addresses Janeway uses when it sends automated emails.

- Language settings  
  The languages your journal's frontpage can be displayed in.

- Remote website settings  
  Relevant if your journal content is hosted elsewhere.

- Enable CRediT  
   If you wish to enable CRediT on your journal and its submissions, you will need to enable this setting by ticking the box.

Click **Submit** at the bottom of the page to save any changes.

Some of these are better set once at press level than repeated for every journal, including publisher name and URL, support email, and login and registration page notices. If you run several journals, see [Journal management at press level](../press-management/journal-management-press-level.md) before filling them in one by one.

For the full reference, see [Journal settings](../journal-management/journal-settings.md).

> [!TIP]
> If you are looking for a specific setting and cannot find it, open **All settings** from the **Journal settings** panel and search for it there.

### Designing your journal

Janeway from 1.9 onwards has four themes: Clean, Material, OLH and Clarity. Clarity is only available from 1.9 onwards. They share the same features and content, but differ in layout and how prominently they use images.
Clarity is the most accessible theme as of 1.9, Clean is the most accessible before 1.9. The theme setting is found on the **General** page under **Journal settings**.

In addition to setting a theme, you may wish to upload default images. These images act as fallbacks: if an article or issue has no image of its own, Janeway uses the journal default.

- Header image  
  Your journal logo, shown in the site header.

- Cover image  
  The default or backup issue cover, which can be seen on the issues list on the journal website.

- Large image  
  The wide banner used at the top of the article page and on an issue's page, and in the homepage carousel.

- Thumbnail image  
  The square image shown in places where articles are listed on the journal website.

- Favicon  
  The icon in the browser tab.

> [!TIP]
> Check the colour contrast in your logo and cover images. Try to aim for a contrast ratio of at least 4.5:1 between text and the background.

For more information or information on image sizing, see [Image guidelines](../journal-management/image-guidelines.md)

## Stage 2

### Configuring the workflow

By default, Janeway has the following stages:

1. Unassigned (submission)
2. Review
3. Copyediting
4. Typesetting
5. Prepublication

These can be edited, reordered and removed by someone with the staff permission through the **Workflow** page, which is accessible through the left-hand side menu.

>[!WARNING]
>Removing stages may have unintended consequences, only do this if you are comfortable doing this. Otherwise, contact your system administrator.

### Setting up article types (sections)

Article types (sections) are used to categorise articles by content type, e.g., research articles, book reviews and editorials. You can configure these by clicking **Sections (Article types)** on the manager dashboard.

If your journal only publishes one article type, you can hide the section field during submission using the submission fields configurator (see submissions for more info <!--missing hyperlink-->). If you do, set a default section so the information still reaches the article metadata.

>[!NOTE]
>A section cannot be deleted once articles are assigned to it. To remove a section that contains articles, first move every article to a different section. It is worth getting your section list roughly right before you open submissions.

For more information on configuring sections, see the documentation on [Article sections](../article-management/article-sections.md)

### Setting up licenses

Authors can chose a licence when they submit, so the licence list needs to be right before submissions open. Janeway comes lists the CC 4.0 licences and All Rights Reserved licence by default. Edit this list from the **Licence manager** which can be found on the manager dashboard.

Similarly to sections, if journal only publishes with a single licence, you can hide the submission selection field during submission <!-- mising hyperlink-->. If you do, set a default licence so the information still reaches the article metadata.

For more information on configuring licences, see the [Licence manager](../submission/licence-manager.md)

### Setting up submissions

The submission process setup has four parts, all reached from the manager dashboard:
1. Submission settings
    This controls the process itself; whether submissions are open, who is notified upon submission, whether to limit filetypes, etc.

2. Submission page items
    This controls various blocks on the public submission page (the page with information before starting a submission) which are also visible during the submission itself. E.g., the submission checklist, focus and scope and licences will all appear before as well as during submission.

3. Submission fields configuration
    This controls which fields are shown to authors during submissions, as Janeway comes with a set of default fields, but you may not wish to use all of them.

4. Additional submission fields
  This lets you set up additional submission fields and questions.

>[!TIP]
>You may wish to leave submissions disabled until your sections, licences, review settings, and editor accounts are setup. It is easier handling submissions when all is ready, though his is not necessary.

For more information, see: [Submissions](../submission/index.md)

### Setting up review


//

Additionally, Janeway sets up two things for you when the journal is created:

- A review form called **Default Form**, containing a single text area. You can edit or replace it.

- A set of licences covering the CC 4.0 licences and All Rights Reserved.
///
Journal name

Journal domain
If the journal is on its own domain, not the press domain + `/JOURNAL_CODE`

Journal code
An abbreviation / word that signifies the journal. If on path mode <!-- what is path mode -->, it will show on the journal URL.

These and the journal ISSN will be filled in on the **Journal settings** page, more on this below.

## Journal settings

- Privacy policy
- Login page and/or registration page notice
- Identiers (assuming they are in use) CrossRef or DataCite <!-- missing hyperlink-->

Journal design - see guide <!-- missing hyperlink -->.

## Users

- Typesetters (if applicable)
- Editors
- Editorial board
  Can be imported, see [import plugin](../plugins/imports-plugin.md).

## Submission

- Enable or disable submission.
- [Setup licences for submission](../submission/licence-manager.md).

## Review

- Review type: double or single anonymous, [open peer review](../review/open-peer-review.md) or [triple anonymous](../review/triple-anonymous-peer-review.md)
- Review form
- One-click peer review

## Website content

- Navbar
- Contacts
- Webpages
