Title: Issues

# Issues

Articles do not have to be part of an issue. There are some services
that do require an article have an issue or volume (such as Crossref) so
we recommend that if you do continues publication that you create a
yearly volume/issue to add papers to. Articles are added to Issues
during the Pre Publication stage, however, Issues can be managed on
their own through the Issue Manager, a link to which is available on the
Manager page and the main sidebar.

<!-- ![The Issue Management page.](../nstatic/issue-management.png) -->

> [!TIP]
> To set the current issue, click the Make Current button. The Issue without this button *is* the current issue.

> [!TIP]
> To re-order the issues you can drag and drop the rows of the tables or use the sort buttons at the top of the page.

## Issue Types

Janeway comes with two issue types built in: Issue and Collection. Collections differ in so much as they are not a primary Issue for a paper but tend to be collections of papers with similar topics across multiple different issues. So an article may be in the Thomas Pynchon Collection but it's primary Issue may be Volume 1 Issue 2 2019. You can also define your own issue types in the Django admin area.

## Display Settings

In the top right of the Issue Management page there is the Edit Display Settings button. This allows you to configure how issue titles and the issue page are displayed.

You can turn these elements on or off:

- Volume number
- Issue number
- Issue year
- Issue title
- Article number
- Article page numbers
- Issue DOI
- Group issues by decade

Here are a few example issue displays:

- Volume 6 • Issue 3 • Fall 2015 • 5–17
- Winter 2009 • 19 pages
- Volume 35 • 2021 • Number 49

> [!TIP]
> If you want to display a totally custom issue title, disable everything except issue title, and use that field to form the issue display for each issue.

> [!TIP]
> You can use the article number field to set an arbitrary number for each article, whether to distinguish articles within each volume or issue or to number articles across volumes and issues. Article number is an optional field separate from article ID and can be set in Edit Metadata.

> [!TIP]
> If your journal has a lot of issues you can enable the "Group issues by decade" feature to allow readers to jump to a specific decade on the issues interface.

## Creating and Editing Issue Details

You can create new issues from this page using the Create Issue button and you view and edit the detail of individual issues by selecting them.

<!-- ![An empty create issue form](../nstatic/create-issue.png) -->

Information on the sizes of the cover image and large image can be found in the Styling section

## Manage an Issue

Clicking on View takes you through to the manage issue page where you can alter an individual issue. The page is split into 4 sections.

- Issue Management
- Table of Contents
- Guest Editors
- Galleys

### Issue Management

Here you can see the metadata for your issue, edit it, delete it and if the issue is published there is a link to view it on the front end.

### Table of Contents

In the Table of Contents section, you can add articles to the issue, sort the sections and sort the articles within their sections.

For each section, there are arrow icons that allow you to move the section up and down; each of the articles can be dragged and dropped into order from inside their section.

<!-- ![Issue table of contents](../nstatic/issue-table-of-contents.png) -->

You can drop an article from an issue using the Remove link and add new ones clicking the Add Article link.

<!-- ![Articles that can be added to issues](../nstatic/issue-articles.png) -->

A list of all articles published in the journal that are not already in the issue is displayed and you can use the Add button to place it in the issue.

### Guest Editors

An issue can list Guest Editors if the articles aren't being handled by the normal editorial team. Use the Manage button to control who appears as a Guest Editor for an issue/collection.

<!-- ![An issue with no guest editors](../nstatic/empty-guest-editors.png) -->

<!-- ![An issue with no guest editors](../nstatic/manage-guest-editors.png) -->

When adding a new guest editor you can also enter a role, the default text for this role is *Guest Editor* though you can change it. Use the **Add** button to add a new guest editor.

### Galleys

You can upload a Galley file for the whole issue, usually a PDF so that users can download the whole issue in one go.

<!-- ![An issue with no guest editors](../nstatic/issue-galley.png) -->

> [!TIP]
> If you don't upload a Galley for the issue then Janeway will allow users to download a zip file of all the individual article galley files.

### Issue DOIs

Issues can be assigned a DOI in Janeway. This can be done ad-hoc for each issue by editing the issue details and inputting the DOI manually, or by letting Janeway generate a DOI for you, based on a pattern (a DOI pattern can be set from the Crossref Settings page)

When the Crossref integration is enabled, issue DOIs will be registered with Crossref whenever an article in that issue is registered with Crossref. This will be the case both for DOIs generated for Janeway as well as for those manually set.

> [!TIP]
> If you are migrating a Janeway installation from a version that did not support issue DOIs and would like to register issue DOIs for your back content, this can be done by populating the DOI field on those issues and then re-registering any of the articles in the issue with Crossref.

> [!WARNING]
> When an article is part of two or more issues, only the primary issue DOI will be registered with Crossref. In a future version, it will be possible to register issue DOIs on their own, even when they have no articles or all its articles are part of multiple issues.


<!-- needs to be edited and sorted, currently merged from different sections-->

## Issue Manager

The issue manager lets you create, edit, delete and manage article records for issues. The main interface presents a list of your existing issue records with buttons to:

- Create a new issue
- Edit a given issue
- Delete a given issue
- Mark an issue as Current

It also displays some basic data about the issues like date published and the number of articles in an issue.

<!-- ![Issue list](../../nstatic/issue-manager.png) -->

### Creating a New Issue or Collection

To create an issue select ***Create Issue*** in the top right and in the modal that appears you can complete the issue metadata.

- Title  
  - Optional, a title for the issue.

- Volume  
  - The volume number.

- Issue  
  - The issue number.

- Date  
  - The date published, if in the future the issue won't appear until the date published.

- Cover Image  
  - The cover image, see the example below.

- Large Image  
  - A large image file used at the head of the issue page, will be resized automatically but should be landscape.

- Description

- Issue type  
  - Issues can be standard issues or can also be collections which are used to collect articles from across the journal into narratives.

<!-- ![New issue form](../../nstatic/new-issue.png) -->

- Issue DOI  
  - Issues can have a DOI, which will be registered with all of its articles in Crossref. If you are using Janeway's autoregistration (recommended) or if you are not interested on registering DOIs for issues, you can leave this field blank.

### Issue Articles

You can manage the article associated with a given issue by selecting the ***View*** option, the data of the issue will be displayed along with a list of articles grouped by section.

<!-- ![An issue page](../../nstatic/issue-page.png) -->

You can reorder the Section headers using the arrows Up and Down arrows on the right and you can re-order the articles within their sections by dragging and dropping them into the order you want. To add a new article into the issue select *Add Article* and select the article you want to add.

In addition, if the issue has guest editors you can add them using the Guest Editor manager at the bottom of the Issue page.

### Projected Issues

Janeway allows editors to mark articles as projected to be published within a given issue. This can be done in the Editor Assignment stage by using the "**Assign Projected Issue"** button.

> [!WARNING]
> Assigning an article to a projected issue is not the same as assigning an article directly to an issue. Projected issues are used mainly for internal tracking.

<!-- ![On the Editor Assignment screen you can see which issue an article is projected to be in.](../../nstatic/assign-projected-issue-link.png) -->

On the projected issue screen, you can select, from a drop-down, the issue you expect the article to be published in.

<!-- ![Select an issue and click "Save Projected Issue" to update the projected issue for your article.](../../nstatic/assign-a-projected-issue.png) -->

