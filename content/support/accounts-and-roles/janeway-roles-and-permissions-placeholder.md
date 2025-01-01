<!--## Janeway roles 
- Author
    - When someone registers with the journal or submits an article, they are given this role. 
- Reviewer
- Editor
  - Handles processing of articles and assignment of tasks
- Journal Manager
    - Has a similar level of permission to the Editor role, but can be
    given extra access (see below)
- Section Editor
- Copyeditor
- Typesetter
- Proofreader
> [!NOTE] 
> Whilst the Production Manager and Proofing Manager are still assignable in Janeway, they have been deprecated in 1.4 and are no longer in use.
-->

<!-- - Reader  
  - This role indicated whether a user is signed up for now article
    notifications 
    Note: this is not a typical role as such? Maybe this should be put with email notifications?
  
    -->
<!--## Permissions

In addition to the roles and their respective permissions, there are also seperate permission levels that can be assigned. Editors also have specific permissions associated with their role.-->
<!-- Editor permission 

Editors have control of:

- Enrolled Users (users who have a role on your journal)
- Enrolling Users (giving users a role on your journal)
- Journal Roles (viewing users with a given role)-->

<!-- Staff permission

Staff have additional controls for:

- Inactive Users (users who have not activated their accounts)
- Authenticated Users (lists users with active sessions)
- Merge Users (available at the press level)-->
<!-- Admin permission-->
<!-- Superusers permission-->

<!-- ## Granular Manager Permissions

In version 1.5 we introduced more granular manager permissions.
Initially these are centered around the journal manager and editor
roles. We are introducing a new setting group "Permission", and within
this group we will be adding new permission controllers starting with:

- Licenses  
  - Controls whether a user can access the licenses control pages base
    on their roles, defaults to Editor and Journal Manager

- Sections  
  - Controls whether a user can access the sections control pages base
    on their roles, defaults to Editor and Journal Manager

Currently there is no interface for updating the roles that can access
these pages and the setting is JSON stored in the database.

> [!WARNING]
> You should only edit the Permission settings if you are sure about the change you are making.

By default both settings read `["editor", "journal-manager"]`. If, for example, you wanted to stop editors
from editing licenses you could change it to read
`["journal-manager"]`. Once saved, only
users with the journal manager role will be able to access the licenses
pages.

## Granular Settings Permissions

In version 1.5 we introduced granular settings permissions. Staff can
now determine, for any given setting object, which roles are allowed to
edit it. This is done via the Django Admin panel (Core \> Settings),
using the `editable_by` field. Staff can
alter the roles that are allowed to see and edit a setting.

> [!NOTE]
> If a setting is also displayed on a settings group page (for example the
General or Submission settings page) and a user does not have the
appropriate permission to edit that setting it will be filtered out of
the form and not be visible.

As with the manager permissions changes the default to settings
permission maintains the status quo and by default all settings are
editable by editors and journal managers.-->
