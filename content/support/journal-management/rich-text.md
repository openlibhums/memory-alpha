title: Managing rich text fields
# Managing rich text fields

* Something about us using TinyMCE
* Explaining what it currently does and doesn't preserve
* Do we want to outline common issues?

Many people copy and paste from a word processor into Janeway when working on webpages, news items, and other fields such as abstracts. When a user attempts to paste text that carries over styling from another application, Janeway will prompt the user to ask if they want to retain the formatting or paste it as plain text.

Additionally, Janeway removes any potentially harmful markup being pasted in or typed using the code view across rich-text fields, such as scripts that could lead to [Cross Site Scripting](https://owasp.org/www-community/attacks/xss/) attacks.
