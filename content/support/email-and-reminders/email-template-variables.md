title: Email template variables

# Email template variables

Email template variables allow Janeway to automatically insert information into emails, such as article titles, reviewer names or due dates.

You do not need technical knowledge to use variables, but it is important to use them *exactly as shown*, unless you are confident about what they do. Changing or removing parts of a variable can cause emails to display incorrectly. If you are unsure, contact your system administrator or Janeway support.

This page explains:

- What variables are.
- Which variables are available in common templates.
- How to use them safely.

For general guidance on editing templates, see Email templates <!--missing hyperlink-->.

## What are email template variables?

Variables are placeholders that Janeway replace with real information when an email is sent.

For example:

- The reviewer’s name.
- The article title.
- A review deadline.
- A link to a review task.

Variables always appear inside double curly brackets, for example:

`{% raw %}{{ review_assignment.date_due }}{% endraw %}`

When the email is sent, Janeway replaces this with the actual due date.

>[!IMPORTANT]
> Variables must be copied exactly (if copying from reference). Do not add spaces, punctuation or text inside the brackets. You can safely change the surrounding text.

## Example template: Review assignment

Template code: review_assignment

This email is sent to potential reviewers when they are invited to review an article.

The following information can be inserted into the email using variables:

- Article information (title, abstract, journal name).
- Reviewer information.
- Editor information.
- Review details, such as the due date.
- A secure review link.

Commonly used variables include:

- `{% raw %}{{ article.safe_title }}{% endraw %}`  
  The article title.
- `{% raw %}{{ editor.first_name }}{% endraw %}`  
  The editor’s first name.
- `{% raw %}{{ review_assignment.reviewer.full_name }}{% endraw %}`  
  The reviewer's full name.
- `{% raw %}{{ review_assignment.date_due }}{% endraw %}`  
  The review due date.
- `{% raw %}{{ review_url }}{% endraw %}`  
  The link the reviewer uses to access the review.

### Review assignment objects (advanced users)
If you are a technical user and/or familiar with objects, here is a list of objects in this template's context:

- article, an Article object.
- editor, an Account object.
- review_assignment, a ReviewAssignment object.
- review_url, a reversed URL with FQDN.
- article_details, a string with article and review information in it, inc. Title, due date etc.

## Using variables in practice

Here are some common examples you can copy and reuse.

- Review due date  
  `{% raw %}{{ review_assignment.date_due }}{% endraw %}`

- Article title  
  `{% raw %}{{ article.safe_title }}{% endraw %}`

- Journal name  
  `{% raw %}{{ article.journal.name }}{% endraw %}`

- Review link  
  `{% raw %}{{ review_url }}{% endraw %}`

- Revisions link  
  `{% raw %}{{ do_revisions_url }}{% endraw %}`

- The title of the issue this article is projected to be part of  
 `{% raw %}{{ article.projected_issue.display_title }}{% endraw %}`

- The article's correspondence author  
  `{% raw %}{{ article.correspondence_author.full_name|se_can_see_pii:article }}{% endraw %}`

>[!NOTE]
> Certain variables, such as the title, have `safe_` appended to the second half of the object. This is to ensure they display correctly.

>[!NOTE]
> In certain templates, the author name variable will include "`|se_can_see_pii:article`". This determines the visibility of the variable's information to section editors when using triple anonymous review. You do not need to edit this or otherwise worry about this when not using triple anonymous review.

## Commonly used objects (advanced reference)
The sections below describe the main objects you may encounter.

### Objects

Listed here is a non-exhaustive list of the objects that you may have access to in an email template.

KEY

- Str is plain text.
- Int is a number.
- FK is Foreign Key, this means the attribute is a link to another
  object.
- M2M is Many to Many, this means the attribute links to multiple other
  objects of the given type.
- 121 is One to One, it means these two objects are linked.
- Bool is a Boolean value and will return True or False.
- DateTime is a field that stores a internationalised date and time.
- Email is a validated email address.

### Account object reference

The account object stores information about users.

- email (Email, unique)
- username (Str)
- first_name (Str)
- middle_name (Str)
- last_name (Str)
- salutation (Str)
- biography (Str)
- orcid (Str)
- institution (Str)
- department (Str)
- twitter (Str)
- facebook (Str)
- linkedin (Str)
- website (Str)
- interest (M2M Interest)
- country (FK Country)
- preferred_timezone (Str, valid timezone)
- is_active (Bool)
- is_staff (Bool)
- date_joined (DateTime)

### Article object reference

The article object contains the following attributes:

- journal (FK `Object Journal`)
- title (Str)
- abstract (Str)
- owner (FK `Object Account`)
- keywords (FK Keyword)
- language (Str)
- section (FK Section)
- license (FK License)
- publisher_notes (M2M PublisherNote)
- is_remote (Bool)
- remote_url (Str)
- authors (M2M Account)
- correspondence_author (FK `Object Account`)
- rights (Str)
- article_number (Int)

### Journal object reference

The journal object contains the following attributes:

- code (Str)
- name (Str)
- current_issue (FK Issue)
- carousel (121 Carousel)
- thumbnail_image (FK File)
- press_image_override (FK File)
- default_cover_image (ImageField)
- default_large_image (ImageField)
- header_image (ImageField)
- favicon (ImageField)
- description (Str)
- contact_info (Str)
- Keywords (Keyword)
- is_conference (Bool)
- is_archived (Bool)
- is_remote (Bool)
- remote_view_url (URLField)
- remote_submit_url (URLField)
- hide_from_press (Bool)
- sequence (Int)
- disable_front_end (Bool)

### ReviewAssignment object reference

- article (FK `Object Article`)
- reviewer (FK `Object Account`)
- editor (FK `Object Account`)
- form (FK ReviewForm)
- review_round (FK ReviewRound)
- date_due (DateTime)
- date_requested (DateTime)
- date_accepted (DateTime)
- date_complete (DateTime)
- decision (Str)
- visibility (Bool)
- access_code (Str, UUID format, though not enforced)
- is_complete (Bool)
- for_author_consumption (Bool)
- comments_for_editor (Str)
- review_file (FK File)
- display_review_file (Bool)

<!-- Q to devs: what happens if you'd include a variable for information that isn't available? E.g. ORCID / salutation / middle name. IF no one knows, I'll test it myself later + I assume dates get localisaed automatically?-->