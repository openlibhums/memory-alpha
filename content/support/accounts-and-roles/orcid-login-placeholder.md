<!-- Title: ORCID login

# ORCID login

Janeway supports ORCID login.
- how to register
- how to login

## Enable ORCID login
To enable ORIC login, you need to add the following to your settings file:

    ENABLE_ORCID = True
    ORCID_CLIENT_SECRET = ''
    ORCID_CLIENT_ID = ''

As the URLs for the ORCID API are fixed there is no need to set them.

## Callback URLs
You will need to set the callback URLs in the ORCID interface. If using domain mode you will need to add each domain, if using path you can set just the main domain.
-->
