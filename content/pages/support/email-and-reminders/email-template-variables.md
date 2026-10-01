# Email template variables

Email template variables allow Janeway to automatically insert information into emails, such as article titles, reviewer names or due dates.

You do not need technical knowledge to use variables, but it is important to use them _exactly as shown_, unless you are confident about what they do. Changing or removing parts of a variable can cause emails to display incorrectly. If you are unsure, contact your system administrator or Janeway support.

This page explains:

- What variables are.
- Which variables are available in common templates.
- How to use them safely.

For general guidance on editing templates, see [Email templates](./email-templates.md).

## What are email template variables?

Variables are placeholders that Janeway replace with real information when an email is sent.

For example:

- The reviewer's name.
- The article title.
- A review deadline.
- A link to a review task.

Variables always appear inside double curly brackets, for example:

`{% raw %}{{ review_assignment.date_due }}{% endraw %}`

When the email is sent, Janeway replaces this with the actual due date.

> [!IMPORTANT]
> Variables must be copied exactly (if copying from reference). Do not add spaces, punctuation or text inside the brackets. You can safely change the surrounding text.

## Example: Review assignment

This email is sent to potential reviewers when they are invited to review an article.

The following information can be inserted into the email using variables:

- Article information (title, abstract, journal name).
- Reviewer information.
- Editor information.
- Review details, such as the due date.
- A secure review link.

Commonly used variables in review assignments include:

- `{% raw %}{{ article.safe_title }}{% endraw %}`  
  The article title.
- `{% raw %}{{ review_assignment.reviewer }}{% endraw %}`  
  The reviewer's full name.
- `{% raw %}{{ editor.first_name }}{% endraw %}`  
  The editor's first name.
- `{% raw %}{{ review_assignment.date_due }}{% endraw %}`  
  The review due date.
- `{% raw %}{{ review_url }}{% endraw %}`  
  The link the reviewer uses to access the review.
- `{% raw %}{{ article_details }}{% endraw %}`  
  A printout of the article and review information, including title and due date.

## Other common variables

Here are some common examples you can copy and reuse across templates.

> [!TIP]
> Not all variables are available on all templates, so always test out your template to make sure data is coming through.

- Article title  
  `{% raw %}{{ article.safe_title }}{% endraw %}`
- Journal name  
  `{% raw %}{{ article.journal.name }}{% endraw %}`
- Review due date  
  `{% raw %}{{ review_assignment.date_due }}{% endraw %}`
- Review link  
  `{% raw %}{{ review_url }}{% endraw %}`
- Revisions link  
  `{% raw %}{{ do_revisions_url }}{% endraw %}`
- The title of the issue this article is projected to be part of  
  `{% raw %}{{ article.projected_issue.display_title }}{% endraw %}`
- The article's correspondence author  
  `{% raw %}{{ article.correspondence_author|se_can_see_pii:article }}{% endraw %}`

If you use a variable with information that isn't available, e.g. a middle name for a user who has not provided one, it will be ignored nothing will be displayed.

> [!NOTE]
> Certain variables have `|safe` appended, or the word “safe” somewhere in the variable, to ensure they display correctly even if they have HTML markup. For example, an article named “Review of Prince’s _1999_” will be stored in the Janeway database as `Review of Prince’s <em>1999</em>`, and when `{% raw %}{{ article.safe_title }}{% endraw %}` is used in a template, “1999” will be italicized properly.

> [!NOTE]
> In certain templates, variables related to personally identifying information should have "`|se_can_see_pii:article`" on the end. This determines the visibility of the variable's information to section editors when using triple anonymous review. You do not need to edit this or otherwise worry about this when not using triple anonymous review.

## Variable reference (advanced)

Below are the main objects you may encounter. This section is for advanced users.

### Informational variables

These print out information when put into a template.

```
{% raw %}{{ article.id }}
{{ article.safe_title }}
{{ article.abstract|safe }}
{{ article.owner }}
{{ article.owner.email }}
{{ article.owner.salutation }}
{{ article.owner.orcid }}
{{ article.owner.primary_affiliation }}
{{ article.correspondence_author }}
{{ article.correspondence_author.email }}
{{ article.correspondence_author.salutation }}
{{ article.correspondence_author.orcid }}
{{ article.correspondence_author.primary_affiliation }}
{{ article.keyword_list_str }}
{{ article.language }}
{{ article.section }}
{{ article.license }}
{{ article.rights|safe }}
{{ article.article_number }}
{{ journal.code }}
{{ journal.name }}
{{ journal.current_issue }}
{{ journal.description|safe }}
{{ journal.contact_info|safe }}
{{ review_assignment.article }}
{{ review_assignment.reviewer }}
{{ review_assignment.reviewer.email }}
{{ review_assignment.reviewer.salutation }}
{{ review_assignment.reviewer.primary_affiliation }}
{{ review_assignment.editor }}
{{ review_assignment.editor.email }}
{{ review_assignment.editor.salutation }}
{{ review_assignment.editor.primary_affiliation }}
{{ review_assignment.review_round.round_number }}
{{ review_assignment.date_due }}
{{ review_assignment.date_requested }}
{{ review_assignment.date_accepted }}
{{ review_assignment.date_complete }}
{{ review_assignment.decision }}
{{ review_assignment.visibility }}
{{ review_assignment.comments_for_editor }}
{% endraw %}
```

> [!TIP]
> Some variables provide links to other ones, so you can chain them together. For example, `review_assignment.article` can be extended with any of the variables beginning `article`, like this: `review_assignment.article.id`.

### Logical variables

These provide yes/no (boolean) information and are used in if/else blocks. For example:

```
{% raw %}{% if review_assignment.is_complete %}
  The review assignment is complete.
{% else %}
  The review assignment is incomplete.
{% endif %}
{% endraw %}
```

Each of these variables can be used in the first line of the if/else block:

```
{% raw %}{% if journal.is_conference %}
{% if review_assignment.is_complete %}
{% if review_assignment.for_author_consumption %}
{% if review_assignment.display_review_file %}
{% if review_assignment.reviewer.is_active %}
{% endraw %}
```
