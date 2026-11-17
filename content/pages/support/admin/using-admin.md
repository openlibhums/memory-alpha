# Using the admin area

## Getting started with the admin area

Generally, you should only use the admin area when there is no way of achieving your goal through the backoffice, when you have received specific instructions to do so, and are confident in what you are doing. It is recommended to only access this part of Janeway if you are generally confident with advanced functions of software and software as a service.

## Who can acces admin

Only users with staff permissions can access the admin area. Staff permission is usually only given to press managers, technical support, and on standalone journals it may be given to editors. See [Staff permission](../accounts-and-roles/roles-and-permissions-on-janeway.md#staff-permission) for more information.

If you can open the admin area but can't see a table or a record you need, contact your system administrator.

## Navigating admin

The admin homepage lists tables in sections (Janeway data is organised in tables). The order of sections and tables comes from Janeway's source code and can't be changed. Each section is the part of Janeway the records belong to, installed plugins usually appear in their own sections.

![The admin homepage.]()

For example:

- **Core**  
  Accounts, roles, settings and files.

- **Journal**  
  Journals, issues and issue types.

- **Submission**  
  Articles, sections, licences and frozen author records.

- **Utils**  
  Log entries and installed plugins.

The links at the top of each page show where you are, for example **Home › Core › Accounts**. Select any part of it to go back.

Within a table or section, there will be two types of pages: list pages and records. A list will show all the records in a table and will generally present you with the following functions:

- Search box  
  Finds records containing the words you type. Each table searches its own set of searchable fields.

- Filters  
  These can be used to narrow the list by a filter value; like journal, type or date. You can combine several filters. To clear them, click **Clear all filters**.

- Date links  
  Some tables show years, months and days above the list. Select one to show only records from that date.

- Column headings  
  Click a heading to sort the list by that column. Click it again to reverse the order.

- **Add** button  
  Creates a new record in this table. Don't use this button, records should never be added through the admin area.

- **Action** menu  
  Applies an action to every record you tick in the list. In most tables, the only action is to delete the selected records.

![A list page in the admin area.]()

> [!WARNING]
> Deleting records from a list page deletes every ticked record, and any records that depend on them. Janeway shows a summary before you confirm, but the deletion can't be undone.

## Finding a record

Janeway objects such as an article, account, review assignment or journal will have records you can view, edit or delete. To find a record:

1. On the admin home page, find the table you need. For example, under **Core** click on **Accounts**.
2. You will now see a list of records. You will need to narrow them down in one of the following ways:
   - Use the search box at the top of the page. What fields are searchable will depend on the information held in the record.
   - Use the filters on the righthand side of the page. The filters are preset and it is not possible to add additional filters.
3. Click on the record after finding it, you will now be able to access it.

> [!TIP]
> Most tables hold records for every journal on the press. If the list has a journal filter, use it first.

## Record pages

A record page shows every stored field for one record. Some pages also show linked records in tables lower down, such as an account's roles or linked review assignments.

- **Save**  
  Saves your changes and returns to the list.

- **Save and continue editing**  
  Saves your changes and keeps the record open.

- **Save and add another**  
  Saves your changes and opens a blank record.

- **Delete**  
  Deletes the record and any records that depend on it. Janeway lists these first and asks you to confirm.

- **History**  
  Shows changes made to this record through the admin area: who changed it, when, and which fields. Changes made in the back office don't appear here.

Some fields link to a record in another table. These show the linked record's number and a search button. Select the search button to choose a different record, rather than typing a number.
