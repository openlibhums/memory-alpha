# Reading log entries in admin

Janeway records many events in its log: emails sent, workflow actions, publication notifications, and more. You can see an article's log entries in the back office. The admin area lets you search the whole log, including entries that aren't linked to an article.

## When to use the admin area

Generally, the Janeway back office log should be the first place to check:

- For emails and actions on one article, use the article's **Logs, documents and more** page. See [Email logs](../email-and-reminders/email-logs.md).
- For emails sent to one user, use the user's **History** page.

Use the admin area for entries the back office doesn't show, such as:

- Publication notifications.
- When someone started and stopped controlling another user's account.
- To find messages sent to the journal through the contact form.

## Finding log entries

1. Open the admin area. See [Navigating admin](./using-admin.md#navigating-admin).
2. Under **Utils**, select **Log entries**.
3. Narrow the list using one or more of the following:
   - **By types** in the **Filter** panel: the kind of event, such as _Publication Notification_ or _Hijack Start_.
   - **By is email** in the **Filter** panel: emails only, or everything except emails.
   - The dates above the list, to show one year, month or day.
   - The search box: words in the entry's type, description or email subject, or the email address or name of the person who acted.
4. Select an entry to see its full details.

> [!IMPORTANT]
> The **By journal** filter only finds entries linked to an article in that journal. Entries linked to the journal itself, such as publication notifications, or to a user, such as control entries, don't appear when you filter by journal. Filter by type instead.

## Common log types

| Type                     | What it records                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Publication notification | A publication notification email sent to readers.                                                                                     |
| Hijack start             | A user started controlling another user's account.                                                                                    |
| Hijack release           | A user stopped controlling another user's account.                                                                                    |
| Contact message          | A message sent through a contact form.                                                                                                |
| Article published        | An article was published.                                                                                                             |
| Submission complete      | An author completed a submission.                                                                                                     |
| Authentication           | A failed log-in attempt.                                                                                                              |
| Error                    | A problem Janeway recorded, such as a missing file. These are **not** server error logs, contact your system administrator for these. |

Plugins can add their own types, the **By types** filter lists every type found in your log.

## Understanding an entry

Each log entry shows:

- **Types**: the kind of event.
- **Date**: when it happened.
- **Actor**: the user who caused it, if any. For an entry made while one user controlled another, the actor is the controlled user.
- **Content type**: the type of object the log relates to.
- **Target**: the record it relates to, such as an article, a journal or an account.
- **Description**: what happened.
- For emails: the subject, the addressees, and the delivery status if your installation tracks it.

Log entries are a record of what happened. **Do not** edit or delete them.
