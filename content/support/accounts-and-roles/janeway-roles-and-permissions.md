title: Roles and permissions on Janeway
# Roles and permissions on Janeway

This page explains the different roles available in Janeway and how permissions are managed.

Role VS permissions

<!--Needs some further work, checks and dev input on a few bits. Need to check out the granular permissions still.-->

## Janeway roles

Janeway has a variety of roles available that can be assigned to users, some of which will affect the permissions of the user. Roles do not exclude eachother, e.g. having one role will not prevent you another one.

- Author  
   Assigned automatically when a user registers with a journal or submits an article. This can be considered the 'base role'.
- Reviewer
- Editor  
   Editors handle processing of articles and assignment of tasks. An editor has access to the journal workflow, manager dashboard and journal settings, certain plugins and is able to do general journal management.
   An editor does not have access to the admin area, press level settings and certain plugins.
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

Editors can:
- Manage roles within their journal.
- View and edit account activation status for journal users.
- Edit basic account information on behalf of users.
- View a user’s assignment history (editorial, review, proofing, etc.).
  - The user history page also displays emails sent directly to the user - excluding 'automated' emails such as reminders, notifications and invitations. 

### Staff permission
Staff permission should only be assigned to press-level users (for example, publishers or system administrators). It can only be granted by another user with staff permission.

Staff users can:
- Perform all editor-level actions across all journals in the press.
- Merge duplicate user accounts at press level.
- Use all installed plugins.
- View additional manager pages (for example: inactive users, authenticated users).
- View the **All articles** page. <!-- check-->
- Access the **Admin area**. <!--missing hyperlink-->

### Superusers permission
‘Superuser’ will assign a user all roles across the system.

## Granular manager permissions
<!-- Note to self: this needs images -->

Janeway allows more granular permissions for journal managers and editors, using the **Permissions** setting group. This can be used on the configuration of licences and sections as following:
- Licenses  
    Permissions control whether users can access the licenses control pages based on their roles, defaulting to Editor and Journal Manager.

- Sections  
   Permissions control whether a user can access the sections control pages based on their roles, defaults to Editor and Journal Manager.

### Editing granular permissions (staff only - advanced)

>[!NOTE]
>The following sections contain information on configuring granular permissions. This requires more advanced technical knowledge, though you are unlikely to need this (often).

There is no interface for updating the roles that can access these pages and the setting is JSON stored in the database. If you are not comfortable or able editing this, please contact your system administrator.

> [!WARNING]
> Only modify granular permissions if you are confident in the change you are making.

By default, both settings read `["editor", "journal-manager"]`. If, for example, you wanted to stop editors from editing licenses, you could change it to read `["journal-manager"]`. Once saved, only users with the journal manager role will be able to access the licenses
pages.

### Granular settings permissions (staff only - advanced)

Users with staff permission can control which roles can view and edit individual settings via the **Admin area** (Core \> Settings), using the `editable_by` field. 

If a setting is displayed on a settings group page (for example, the **General** or **Submission settings** page) and a user does not have the appropriate permission to edit that setting, it will be hidden from the form.

As with the manager permissions changes, the default to settings permission maintains the status quo, and by default, all settings are editable by editors and journal managers.

By default, setting permissions are only editable by editors and journals. When upgrading to a Janeway version with the granular permissions, no changes will be made to the default.

If you wish to make these changes and are not confident using the Admin interface, contact your system administrator.