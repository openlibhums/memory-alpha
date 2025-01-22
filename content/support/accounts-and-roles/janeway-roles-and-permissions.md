Title: Roles and Permissions on Janeway
# Roles and Permissions on Janeway

**WIP**
Needs some further work, checks and dev input on a few bits. Need to check out the granular permissions still.

## Janeway roles 
- Author
    - When someone registers with the journal or submits an article, they are given this role. 
- Reviewer
- Editor
  - Handles processing of articles and assignment of tasks
- Journal Manager
    - Has a similar level of permission to the editor role but can be given extra access (see below)
- Section Editor
- Copyeditor
- Typesetter
- Proofreader

> [!NOTE] 
> Whilst the Production Manager and Proofing Manager are still assignable in Janeway, they have been deprecated in 1.4 and are no longer in use.

- Reader  
  - This is not a role as such, but it is used to indicate whether a user is signed up for article publication notifications. For more information, see email notifications <!-- missing hyperlink -->

## Permissions

In addition to the roles and their respective permissions, separate permission levels can be assigned. Editors also have specific permissions associated with their roles.

###Editor permission 

Editors have control of:

- Enrolled Users (users who have a role in your journal)
- Enrolling Users (giving users a role in your journal)
- Journal Roles (viewing users with a given role)

###Staff permission
Staff have additional controls for:

- Inactive Users (users who have not activated their accounts)
- Authenticated Users (lists users with active sessions)
- Merge Users (available at the press level)

Admin permission
 Superusers permission

## Granular Manager Permissions

In version 1.5, we introduced more granular manager permissions. Initially, these roles were centred around journal manager and editor roles. We are introducing a new setting group, "Permission", and within this group, we will be adding new permission controllers starting with:

- Licenses  
  - Controls whether users can access the licenses control pages based on their roles, defaulting to Editor and Journal Manager.

- Sections  
  - Controls whether a user can access the sections control pages based on their roles, defaults to Editor and Journal Manager.

Currently, there is no interface for updating the roles that can access these pages and the setting is JSON stored in the database.

> [!WARNING]
> You should only edit the Permission settings if you are sure about the change you are making.

By default, both settings read `["editor", "journal-manager"]`. If, for example, you wanted to stop editors from editing licenses, you could change it to read `["journal-manager"]`. Once saved, only users with the journal manager role will be able to access the licenses
pages.

### Granular settings permissions

In version 1.5, we introduced permissions for granular settings. Staff can now determine which roles can edit any given setting object. This is done via the Django Admin panel (Core \> Settings), using the `editable_by` field. Staff can alter the roles that are allowed to see and edit a setting.

> [!NOTE]
> If a setting is also displayed on a settings group page (for example, the General or Submission settings page) and a user does not have the appropriate permission to edit that setting, it will be filtered out of the form and not be visible.

As with the manager permissions changes, the default to settings permission maintains the status quo, and by default, all settings are editable by editors and journal managers.

