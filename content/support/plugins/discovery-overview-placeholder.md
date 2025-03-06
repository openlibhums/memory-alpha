title: Discovery placeholder file.
# Discovery placeholder file.

- OAI-PMH
- KBART
- FTP

- DataCite (active) - Need to be its own page.
  - [GitHub Repo](https://github.com/openlibhums/datacite)
  - Allows staff to mint Datacite DOIs.
  - Works the same as CrossRef DOI. Username and poassword through API.
  - Different from CrossRef: creates a draft DOI at acceptance. Exists on the server but istn available publicly, allows you to check before publication.
    Settings need to be done by sysadmin (contact support). Need to go per journal, cannot be set at press level.


- DOAJ
  - [GitHub Repo](https://github.com/openlibhums/doaj_transporter)
  - This is a plugin for Janeway that allows exporting of journal and article metadata to DOAJ.

- ScienceOpen (beta release)
  - [GitHub Repo](https://github.com/openlibhums/so_transporter)
 
- EBSCO (beta release)
  - An FTP plugin for depositing works with EBSCO.
  - [GitHub Repo](https://github.com/openlibhums/ebsco_transporter)

See also: FTP plugin. <!-- Missing hyperlink -->


## EBSCO 
Deposits a zip file of articles on EBSCO's FTP server. The ZIP packages are in the following format:

- ** Issue Zip **
  - Article 1 JATS (either XML galley or stub)
  - Article 2 JATS
  - ...
