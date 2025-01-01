### Copy-Paste and Rich Text Fields

When working on webpages, news items, and other fields such as
abstracts, many people copy and paste from a word processor into
Janeway. As of version 1.5.1, Janeway handles this better than before:
When a user attempts to paste text that carries over styling from
another application, Janeway will prompt the user to ask if they want to
retain the formatting or paste as plain text.

Additionally, Janeway will always remove any potentially harmful markup
being pasted in or typed using the code view across rich-text fields,
such as scripts that could lead to [Cross Site
Scripting](https://owasp.org/www-community/attacks/xss/) attacks.
