title: ORCID login
# ORCID login

**WIP**

Janeway supports ORCID login.
- How to register
- How to login

<!-- General info - needs some input from dev -->

## Using ORCID to login to Janeway
*If you don't have ORCID, you will need one. <!-- missing hyperlink -->

Start with:

### Linking ORCID to an existing account

## Technical information

### Enable ORCID login
To enable ORIC login, you need to add the following to your settings file:

    ENABLE_ORCID = True
    ORCID_CLIENT_SECRET = ''
    ORCID_CLIENT_ID = ''

As the URLs for the ORCID API are fixed, setting them is unnecessary.

### Callback URLs
You will need to set the callback URLs in the ORCID interface. If using domain-mode you will need to add each domain, if using path-mode you can set just the main domain.


