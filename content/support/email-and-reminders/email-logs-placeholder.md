title: Email logs 
# Email logs
All outgoing emails sent through Janeway are tracked in the article log.

You can view an article's logs through **Logs, docs and more**, which is found in the blue article workflow progress at the top of the screen. You can find this either through its workflow stage or through the archive (Dashboard -\> Left hand menu
-\> Back Content -\> Articles). Under **Logs, docs and more**, select **Logs**.

![image of what to click]()

On this page, you can see:
- Entry type  
     What type of action has been logged.
- Date
- Actor  
    Who iniated the action.
- Level
<!-- what does this mean??-->

If the action logged was an email:
- Addressees  
    Who this was sent to; including CC and/or BCC.
- Subject
- Email status
    Information about the delivery status of the email. See the section below on interpreting email statuses for more information. <!--missing hyperlink-->
- There is an option to click through to see the email content.

<!-- [insert images] -->

## Interpreting statuses

Emails sent through Janeway can have multiple statuses, accompanied with colour-coded dots. The coloured dots will only communicate a status if your Janeway installation uses Mailgun for its email services. If you are using Googlemail, the coloured dots will not convey any information. Janeway cannot track what occurs outside of the installation and the mailservice attached. E.g., if emails are blocked by the local, receiving servers we cannot track this. If you think you may be having email delivery issues, contact your system administrator.

Janeway email statuses:

- No information
- Accepted
- Delivered
- Failed <!-- check with dev-->

## Actions

- Refresh email status (??)
- View content
    - Resend email
