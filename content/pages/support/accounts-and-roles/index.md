# Accounts and roles

This section explains how user accounts and permissions work in Janeway, including how roles are assigned and managed. Read the following pages for more information:

- [Managing user accounts](../accounts-and-roles/managing-user-accounts.md)
- [Roles and permissions](../accounts-and-roles/roles-and-permissions-on-janeway.md)
- [Activating accounts](../accounts-and-roles/activating-accounts.md)
- [ORCID login](../accounts-and-roles/orcid-login.md)
- [Single sign-on (SSO)](#single-sign-on-sso-login)

## New accounts

<!-- Account creation VS self-registration -->

## Single sign-on (SSO) login

Janeway supports single sign-on (SSO), allowing users to log in using their institutional credentials. SSO shows up on the login screen as a button reading “Log in with [name of institution]”

When users log in with SSO the first time, Janeway creates a regular account in the background, recording the name and email that it gets from the SSO system.

Users who originally signed in with SSO can switch to regular login after resetting their password from the login screen. Likewise, users who registered a normal Janeway account can start using SSO if their Janeway account email address matches the one they use with their institution.

> [!TIP]
> If you do not see the SSO login option on your installation of Janeway, then it has not been configured. Contact your system administrator for help configuring SSO.

<!-- missing link for devs to OIDC docs -->
