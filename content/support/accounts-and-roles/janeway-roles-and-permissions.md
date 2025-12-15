title: Roles and permissions on Janeway
# Roles and permissions on Janeway

**WIP**
Needs some further work, checks and dev input on a few bits. Need to check out the granular permissions still.

## Janeway roles

Janeway has a variety of roles available that can be assigned to users, some of which will affect the permissions of the user. Roles do not exclude eachother, e.g. having one role will not prevent you another one.

- Author
   When someone registers with the journal or submits an article, they are given this role. This role may also be described as the 'base role'. 
- Reviewer
- Editor
   Editors handle processing of articles and assignment of tasks. An editor has access to the journal workflow, manager dashboard and journal settings, certain plugins and is able to do general journal management. An editor does not have access to the admin area, press level settings and certain plugins.
- Journal manager
   Journal managers have a similar level of permission to the editor role, but can be given additional access (see below).
- Section editor
   Section editors have access only to the workflow elements of articles assigned to them. They cannot access any articles not assigned to them, journal settings or plugins. This role is well-suited for (guest) editors who only need to handle specific articles within the journal.
- Copyeditor
- Typesetter
- Proofreader
- Reader  
  - This is not a role as such, but it is used to indicate whether a user is signed up for article publication notifications. For more information, see Email notifications <!-- missing hyperlink -->

> [!NOTE] 
> Whilst the Production manager and Proofing manager are still assignable in Janeway, they have been deprecated in 1.4 and are no longer in use.

## Permissions

In addition to the roles and their respective permissions, separate permission levels can be assigned for certain settings for journal managers and editors. Editors also have specific permissions associated with their roles.

### Editor permission 

Editors have permissions that allow:

- Managing roles within their journal.
- Viewing and editing the account activation status of journal users.
- Editing basic account information on behalf of journal users.
- Viewing a user's history (review/editorial/proofing etc. assignments).
  - The user history page also displays emails sent directly to the user - excluding 'automated' emails such as reminders, notifications and invitations. 

### Staff permission
The 'staff permission' should only be given to journal managers/publishers and can only be assigned by other users with the staff permission. Staff have additional controls for:

- The same controls as editors, but for all the journals belonging to the press.
- Merging duplicate user accounts (available at the press level).

### Superusers permission
- ‘Superuser’ will assign a user all roles across the system.

## Granular manager permissions


## Note to self: this needs images

Janeway allows more granular permissions for journal managers and editors, using the **Permissions** setting group. This can be used on the configuration of licences and sections as following:
- Licenses  
   - Permissions control whether users can access the licenses control pages based on their roles, defaulting to Editor and Journal Manager.

- Sections  
  - Permissions control whether a user can access the sections control pages based on their roles, defaults to Editor and Journal Manager.

Currently, there is no interface for updating the roles that can access these pages and the setting is JSON stored in the database. If you are not comfortable or able editing this, please contact your system administrator.

> [!WARNING]
> You should only edit the permission settings if you are sure about the change you are making.

By default, both settings read `["editor", "journal-manager"]`. If, for example, you wanted to stop editors from editing licenses, you could change it to read `["journal-manager"]`. Once saved, only users with the journal manager role will be able to access the licenses
pages.

### Granular settings permissions

Users with staff permission can edit settings to specify which roles can see and edit them. This is done via the Admin interface (Core \> Settings), using the `editable_by` field. If a setting is also displayed on a settings group page (for example, the **General** or **Submission settings** page) and a user does not have the appropriate permission to edit that setting, it will be filtered out of the form and not be visible.

As with the manager permissions changes, the default to settings permission maintains the status quo, and by default, all settings are editable by editors and journal managers.

If you wish to make these changes but are not confident using the Admin interface so, contact your system administrator.