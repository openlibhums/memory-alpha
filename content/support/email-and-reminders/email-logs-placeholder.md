title: Email logs 
# Email logs
All outgoing emails sent through Janeway are tracked in the article log. This allows editors, journal managers and staff to confirm which emails have been sent, when they were sent, and (where supported) their delivery status. 

Email logs are commonly used when:
- A reviewer or author reports not receiving an email.
- You need to confirm that a decision or notification was sent.
- An email needs to be resent.

## Accessing email logs

You can view an article's logs through **Logs, docs and more**, which appears in the blue workflow progress at the top of the article screen.

You can access this through:

 - The article's workflow stage, or 
 - The archive (Dashboard -\> Left hand menu
-\> Back Content -\> Articles).

![Screenshot showing where to access Logs, docs and more](email-logs-access.png)

## Understanding the log entries

Each entry in the log records an action that has taken place on the article. The following information is shown:

- Entry type  
     The type of action that was logged ("Review request accepted" or "Typesetting complete" for example).
- Date
- Actor  
    The user or system process that iniated the action.
- Level
<!-- what does this mean??-->

If the logged action relates to an email, additional details are available:
- Addressees  
    The recipient(s) of the email, including any CC or BCC addresses.
- Subject
- Email status
    Information about the delivery status of the email. See &&Interpreting email statuses** below for more information. <!--missing hyperlink-->
- There is an option to click through to see the email content.

![Screenshot of an email log entry showing status and actions.](article-log.png)

## Interpreting statuses

Emails sent through Janeway may display a delivery status, indicated with both text and coloured dots. 

>[!NOTE]
>If your installation does not use Mailgun, but another email service (for example, Googlemail), the coloured dots will not display meaningful status information.

Janeway can only track events that occur within the system and the configured email service. It cannot track what happens after an email leaves that service (for example, if an email is blocked by the recipient’s local mail server).

If you suspect persistent email delivery issues, contact your system administrator.

### Email status meanings

The following statuses can appear:

- No information  
    No delivery information is available from the email service.
- Accepted  
    The email has been accepted by the email service for delivery.
- Delivered  
    The email has been delivered to the recipient’s mail server.
- Failed <!-- check with dev-->  
    The email could not be delivered.

>[!NOTE]
> Seeing "No information" under email status does not necessarily mean an email was not sent.

## Actions

From this page there are also two things you can do:
- Refresh the email status  
     This checks the latest delivery status for the email. This can be used to check the delivery status. This cannot detect issues on the recipient’s side (such as local spam filtering).

- View email content
    This displays the email message that was sent From this screen, you can also resend the email.