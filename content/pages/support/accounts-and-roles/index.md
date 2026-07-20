# Accounts and roles

This section explains how user accounts and permissions work in Janeway, including how roles are assigned and managed. Read the following pages for more information:

- [Managing user accounts](../accounts-and-roles/managing-user-accounts.md)
- [Roles and permissions](../accounts-and-roles/roles-and-permissions-on-janeway.md)
- [Activating accounts](../accounts-and-roles/activating-accounts.md)
- [ORCID login](../accounts-and-roles/orcid-login.md)
- [Single sign-on (SSO)](#single-sign-on-sso-login)

## New accounts

There are two ways to create an account on Janeway:

1. A user registers for an account through the journal website.
2. An editor, press manager or member of staff can create an account through **Journal users**.

Generally, it is best to let a user register an account using the first option and then assign any roles as needed, see [Roles and permissions](./roles-and-permissions-on-janeway.md). If this is not possible, indivual user accounts can be created by following these steps:

1. Go to the **Journal users** page on the Manager dashboard.
2. Click **Add new user**
3. Fill in the user's details.  
   a. Make sure the **Is active** toggle is set to "Yes".
   b. Except if this user requires staff permissions, make sure the **Is staff** permission is set to "No".
   c. You will be required to set a password.
4. Click **Save**.

The user can now either login after requesting a password reset link, through the journal website, or you could a user their password. The latter is discouraged, as this introduces security risks.

## Single sign-on (SSO) login

Janeway supports single sign-on (SSO), allowing users to log in using their institutional credentials. SSO shows up on the login screen as a button reading “Log in with [name of institution]”

When users log in with SSO the first time, Janeway creates a regular account in the background, recording the name and email that it gets from the SSO system.

Users who originally signed in with SSO can switch to regular login after resetting their password from the login screen. Likewise, users who registered a normal Janeway account can start using SSO if their Janeway account email address matches the one they use with their institution.

> [!TIP]
> If you do not see the SSO login option on your installation of Janeway, then it has not been configured. Contact your system administrator for help configuring SSO.

For information on setting up SSO, see the [Janeway developer docs](https://github.com/openlibhums/janeway/tree/master/docs) - [OIDC specifically](https://github.com/openlibhums/janeway/blob/master/docs/source/dev/oidc.rst), for more information.
