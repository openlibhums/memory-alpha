title: Triple Anonymous Peer Review
# Triple Anonymous Peer Review

<!-- images still needed -->

Triple anonymous peer review in Janeway involves anonymising author information to ensure that section editors are unaware of the authors' identities during the review process. This review method ensures that the reviewer, section editor, and author remain anonymous to one another until the completion of the review stage. Here is an overview of how this feature operates:

## Key settings for triple anonymous peer review
- Section editor personally identifiable information filter (se_pii_filter)
   - This setting must be toggled on to enable anonymisation of author data in the relevant interfaces.

- Reply-to address (replyto_address)
   - This setting must be set to a valid email address. This is required to avoid leaking author email addresses during the review process.


These settings are accessible through the ‘All Settings’ page (found on the Manager dashboard, under ‘Journal settings’).

## Workflow of triple anonymous peer review
- Assigning the section editor: The journal editor assigns a section editor to the manuscript. Before doing so, the manuscript file must be anonymous to prevent the section editor from seeing any personal data.
- Assigning reviewers: The section editor can now manage the peer review process as usual.
- Anonymised data: Instead of viewing the author's personal details (name, email, institution), the section editor will see '[Anonymised data]' in these fields throughout the review process.
- Access to information post-review: Section editors regain access to the author's personal information once the review is completed.


## Areas with anonymisation
Here are the specific areas within Janeway where anonymisation is applied:
- Dashboards
  - Anonymises author data on the main dashboard, kanban view, and active submissions section.


- Unassigned
   - Anonymises author data for unassigned submissions.


- Review
   - Section editors cannot access the document manager, where author details might be stored.


- View metadata
   - Author details are anonymised in the metadata view.


- Edit metadata
   - Section editors are blocked from editing article metadata, ensuring no access to author information.

- Article log
   - Author information is anonymised in the article log, ensuring section editors do not gain access to personal data through log entries.

- Email templates
   - Limits the display of author information in email templates, notably for decision letters (e.g., revision request, acceptance, and decline).

This system ensures a rigorous triple-anonymous process, safeguarding the identities of all parties involved.

