# Article review import

The article review import tool allows you to create peer reviews by uploading a CSV file.

> [!WARNING]
> This tool only allows the import of reviews as files. Further, they must already be on the server where Janeway is running when you use the importer. So you may need an administrator to load the files onto the server for you.

To import peer reviews:

1. Download the [article review import template](../downloadables/reviewer-import-template.csv).
2. Enter your peer review details, one per row.
3. On the **Imports** plugin main page select **Reviewer import** and click **Start Import**.
4. Select your CSV and, if you want you reviewers to receive a password
   reset notification, check that option.
5. Click **Import** to complete the process.

## Metadata field reference

| Field                    | Notes                                                              |
| ------------------------ | ------------------------------------------------------------------ |
| Identifier Type          | Must be either id, doi or pub-id                                   |
| Identifier               | The corresponding ID, DOI or Pub-ID                                |
| Reviewer email           |                                                                    |
| Editor email             |                                                                    |
| Review round number      | Must be a number                                                   |
| Review recommendation    | Either: "accept", "minor_revisions", "major_revisions" or "reject" |
| Review body              | Has no effect--leave blank                                         |
| Review filename          | Path to a file on disk, like `/home/username/files/review.pdf`     |
| Date assigned            | Must be in ISO format YYYY-MM-DD                                   |
| Date accepted or started | Must be in ISO format YYYY-MM-DD                                   |
| Date completed           | Must be in ISO format YYYY-MM-DD                                   |
| Visibility               | Either: "open", "blind" or "double-blind"                          |

> [!TIP]
> Download the [article review import sample](../downloadables/reviewer-import-sample.csv) CSV to see example data.
