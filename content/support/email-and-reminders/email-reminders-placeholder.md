## Scheduled Reminders

> [!NOTE]
> The Scheduled Reminders manager has been updated as part of version 1.4.

Janeway lets you define your own email reminders for overdue Reviews and
Revision assignments. They are defined using the following:

- Type  
  - Review (new), Review (accepted) or Revision reminder.

- Run Type  
  - Whether to run before or after the request is due.

- Days  
  - The number of days before or after the request is due this reminder
    should be sent.

- Template Name  
  - The name of the template that should be used when sending the
    reminder. If this template does no exist you will be asked to create
    it.

- Subject  
  - The email subject to send with the reminder.

There are three types of reminder email supported by Janeway:

- Review (Invited) - sent when a reviewer has been invited but not
  accepted a review request.
- Review (Accepted) - sent when a reviewer has accepted a review request
  but not yet completed it.
- Revision - Sent to authors with active revision requests.

Review reminders, both invited and accepted, are sent based on the
review assignment due date set by the editor. Revision reminders are
sent based on the revision request due date set by the editor. You can
set reminders to be sent either before or after the set due date.

A reminder email has access to three objects in the template:

- review_assignment or revision (depending on which type of reminder)
- journal - the journal sending the reminder
- article - the appropriate article

On the edit template page there is a small guide showing some of the
variables you can use when generating these templates.

![A GIF showing the creating, editing and deleting of a reminder, showing the various screens and fields.](../../nstatic/create-reminders.gif)

Once a reminder is created a Cron job on the server will start
processing requests but it will not process these for Review and
Revision requests that have passed the reminder dates.

> [!TIP]
> If automated reminders are not being sent for your journal the most
likely explanation is that the cron job has not been setup properly. You
should contact your administrator who can setup the call to the
send_reminders management command.

