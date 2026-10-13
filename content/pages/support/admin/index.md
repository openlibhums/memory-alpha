# Janeway admin area

The admin area is Janeway's direct view of its database. This section is for users with staff permission, on hosted and self-hosted installations of Janeway. Server configuration is not covered; for that, contact your system administrator. The admin area allows users with staff permission to find, inspect and edit records that the back office doesn't show (and in ways not allowed in the back office). Ordinarily, you only need it only for a small number of tasks, such as deleting accounts, creating a custom issue type, changing journal codes, and adding elements to the workflow bar for imported articles. The admin area is a builtin part of the underlying Janeway infrastructure and _cannot_ be edited or changed like the Janeway backoffice. It is not possible to change its appearance, add features or reorganise its information.

> [!NOTE]
> Advanced users: As Janeway uses Django, thus the admin area is a [Django admin area](https://www.w3schools.com/django/django_admin.php).

> [!CAUTION]
> Changes in the admin area take effect immediately and can't be undone. They bypass the checks, permissions and emails built into the back office. If you are unsure about a change, contact your system administrator before you make it. Under no circumstance delete content unless you 100% sure.

## Getting started with the admin area

Generally, you should only use the admin area when there is no way of achieving your goal through the backoffice, when you have received specific instructions to do so, and are confident in what you are doing. It is recommended to only access this part of Janeway if you are generally confident with advanced functions of software and software as a service.

### Who can acces admin

Only users with staff permissions can access the admin area. Staff permission is usually only given to press managers, technical support, and on standalone journals it may be given to editors. See [Staff permission](../accounts-and-roles/roles-and-permissions-on-janeway.md#staff-permission) for more information.

If you can open the admin area but can't see a table or a record you need, contact your system administrator.

### Navigating admin

The admin homepage lists tables in sections (Janeway data is organised in tables). The order of sections and tables comes from Janeway's source code and can't be changed. Each section is the part of Janeway the records belong to, installed plugins usually appear in their own sections. For example:

- **Core**  
  Accounts, roles, settings and files.

- **Journal**  
  Journals, issues and issue types.

- **Submission**  
  Articles, sections, licences and frozen author records.

- **Utils**  
  Log entries and installed plugins.

The links at the top of each page show where you are, for example **Home › Core › Accounts**. Select any part of it to go back.

### Finding a record

Janeway objects such as an article, account, review assignment or journal will have records you can view, edit or delete. To find a record:

1. On the admin home page, find the table you need. For example, under **Core** click on **Accounts**.
2. You will now see a list of records. You will need to narrow them down in one of the following ways:
   - Use the search box at the top of the page. What fields are searchable will depend on the information held in the record.
   - Use the filters on the righthand side of the page. The filters are preset and it is not possible to add additional filters.
3. Click on the record after finding it, you will now be able to access it.

> [!TIP]
> Most tables hold records for every journal on the press. If the list has a journal filter, use it first.

## Accounts and roles

## Journal configuration

## Issues and content

## Logs and troubleshooting

## Reference
