title: Scheduling reminders
# Scheduling reminders

Janeway lets you define your own email reminders for overdue Reviews and Revision assignments. They are defined using the following:

- Type  
  - Review (new), Review (accepted) or Revision reminder.

- Run Type  
  - Whether to run before or after the request is due.

- Days  
  - The number of days before or after the request is due this reminder should be sent.

- Template Name  
  - The template name should be used when sending the reminder. If this template does not exist, you will be asked to create it.

- Subject  
  - The email subject to send with the reminder.

Janeway supports three types of reminder emails:

- Review (Invited)
  - Sent when a reviewer has been invited but not accepted a review request.
- Review (Accepted)
  - Sent when a reviewer has accepted a review request but not yet completed it.
- Revision
  - Sent to authors with active revision requests.

Review reminders, both invited and accepted, are sent based on the review assignment due date set by the editor. Revision reminders are sent based on the revision request due date set by the editor. You can set reminders to be sent either before or after the set due date.

A reminder email has access to three objects in the template:
- Review_assignment or revision (depending on which type of reminder)
- Journal
  - The journal sending the reminder.
- Article
  - The appropriate article

On the edit template page, there is a guide that shows some of the variables you can use when generating these templates.

<!-- ![A GIF showing the creating, editing and deleting of a reminder, showing the various screens and fields.](../../nstatic/create-reminders.gif) -->

Once a reminder is created, a Cron job <!-- missing hyperlink explaining what that is--> on the server will start processing requests, but it will not process these for Review and Revision requests that have passed the reminder dates.

> [!TIP]
> If automated reminders are not being sent for your journal the most likely explanation is that the cron job has not been setup properly. You should contact your administrator, who can set up the call to the send_reminders management command.

