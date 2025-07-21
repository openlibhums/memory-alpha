title: Journal contacts
# Journal contacts

You can control the contacts listing for your journal by adding and removing contacts through this interface. Only three fields are used for this:

- Name  
  - The contact's name.

- Email  
  - The email address that should be contacted.

- Role  
  - The contact's role, e.g. editor or reviewer.

Each outgoing message is recorded in the database and can be viewed in the admin area by staff.

<!-- ![Contact Manager interface. The sort handles indicate you can drag and drop to re-order your contacts.](../../nstatic/contact-manager.png) -->

<!-- there is also the field in the journal settings - include info on it -->

## Forming a link for a specific contact

Once you have configured someone as a contact person, you can form a link to them by adding `?recipient=email@example.org` to the end of the contact page link.

They will then be pre-selected as the recipient in the contact form drop-down.

For example:

```html
<a href="https:://myjournal.org/contact/?recipient=managingeditor@example.org">Contact our managing editor</a>
```
