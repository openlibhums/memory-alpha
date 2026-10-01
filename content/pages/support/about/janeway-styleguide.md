# Janeway style guide

## In this guide

- [Introduction](#introduction)
- [Editorial resources and hierarchy](#editorial-resources-and-hierarchy)
- [Quick reference](#quick-reference)

## Introduction

<details open>
 <summary>About this guide </summary>

- This style guide is adapted from the [Google style guide](https://developers.google.com/style) (which is available under a CC-BY 4.0 licence) and has been adjusted to meet Janeway’s requirements. It will also follow Google’s structure. This document is **NOT** intended to cover all issues. It currently contains summaries for ease of access while we adopt the guide, and additions, exceptions, and deviations from the Google guide. In the long term, it will serve solely to outline exceptions, deviations, additions, etc. from the Google guide. (Hopefully, there will not be many)
- This style guide **_does not_** follow OLH or OLHJ style - this is as it a) will have different requirements than OLH(J), b) will make this style guide easier to customise and maintain.
- This guide uses UK English.
- This guide uses the [Chicago style (17th edition)](https://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html) for citations and referencing (see also [Purdue's Online Writing Lab's guidance for Chicago 17th](https://owl.purdue.edu/owl/research_and_citation/chicago_manual_17th_edition/cmos_formatting_and_style_guide/chicago_manual_of_style_17th_edition.html)).

</details>

## Editorial resources and hierarchy

<details open>
<summary> Using this guide </summary>
Use the following resources, including this guide, in this order:

1. **Project-specific.** Specific projects may have their own style guides, outlining exceptions to this guide or terms that are relevant only to your project (such as marketing materials).

2. **This style guide.** Where project-specific style guides do not provide guidance, follow this style guide.

3. **Third-party resources.** If the previously listed resources do not provide guidance, you may wish to use the following:

- Technical style: [Google documentation style guide](https://developers.google.com/style)
- Spelling: [Oxford English Dictionary](https://www.oed.com/) <!-- Internal note: BBK has a subscription. -->
- If spelling not covered by OED: [Guardian and Observer style guide](https://www.theguardian.com/guardian-observer-style-guide-a)
- Non-technical style: [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html)
  <!--	Internal note: SH has a copy available.-->
  </details>

Other resources that may be helpful (especially when adding to / modifying this guide), but that are not part of the documentation itself:

<details>
 
 <summary> Other resources </summary>
 
* [Microsoft Writing Style Guide](https://learn.microsoft.com/en-gb/style-guide/welcome/)
* [Write the Docs](https://www.writethedocs.org/guide/writing/style-guides/)
* [Red Hat supplementary style guide for product documentation](https://redhat-documentation.github.io/supplementary-style-guide/)
* [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/)
* Strategic writing for UX - Torrey Podmajersky
* Don’t make me think, revisited - Steve Krug
 
</details>

## Quick reference

This section provides a brief overview of the content of the Google styleguide, not all sections and issues are covered here. If an issue is not described below, it is likely covered within [the full guide](https://developers.google.com/style/).

> [!NOTE]
> In terms of direct guidance, this document contains summaries and quick overviews. Additional detail and guidance on issues not covered or summarised in this guide are available in the full Google guide.

### Tone and content

- Be conversational and friendly without being frivolous. Remain professional.
- Avoid jargon or (complex) technical language where possible. If a term is required, explain it.
- Don’t pre-announce anything in the documentation.
- Write for a global audience.
- Avoid using phrases like _simply_, _It's that simple_, _It's easy_, or _quickly_ in a procedure.

See: [Voice and tone](https://developers.google.com/style/tone)
See: [Timeless documentation ](https://developers.google.com/style/timeless-documentation)

### Spelling and grammar

- Use UK English spelling and punctuation.
- Use the second person (“you” rather than “we”).
- Use active voice.
- Use present tense.
- Put conditions before instructions, not after.
- Use [prescriptive documentation](https://developers.google.com/style/prescriptive-documentation) standards. To indicate required or optional user actions or process outcomes, select an appropriate auxiliary verb — for example, _must_, _can_, or _might_. Generally, avoid the word _should_.

### Formatting, punctuation, and organisation

- Use sentence case for all headings: capitalise the first word, but do not use a period at the end.
- Use serial commas.
- [Numbers guidance](https://developers.google.com/style/numbers)
- Use numbered lists for sequences.
- Use bulleted lists for most other lists.
- [Lists guide](https://developers.google.com/style/lists)
- Use unambiguous date formatting.
- Put UI elements in bold.
- [UI elements and interaction guide](https://developers.google.com/style/ui-elements)

### Capitalisation

See: [Capitalisation](https://developers.google.com/style/capitalization)

Divert from Google:

- Use standard capitalisation rules for **UK English.**

Janeway-specific guidance:
Only capitalise Janeway roles when referring to a button / UI element or when explicitly referring to the role. Do not capitalise Janeway roles when referring to people.

For example:

:heavy_check_mark: **Recommended**: "The Editor role has permissions for…"

:x: **Not recommended**: "When you assign the typesetter role…"

:heavy_check_mark: **Recommended**: "When the typesetter sends the galleys…"

:x: **Not recommended**: "During review, Section editors require Editors to approve draft decisions."

### Accessibility

See: [Write accessible documentation](https://developers.google.com/style/accessibility)

#### General

- Avoid unnecessary font formatting. (Screen readers explicitly describe text modifications.)
- Avoid bias and harm when discussing disability and accessibility.
- Break up walls of text to aid in scannability. For example, separate paragraphs, create headings, and use lists.
- Place distinguishing and important information of a paragraph in the first sentence to aid in scannability.
- Use shorter sentences. Try to use fewer than 26 words per sentence.
- Define acronyms and abbreviations on first usage and if they're used infrequently.

#### Links

- Use meaningful, descriptive link text.
- If a link downloads a file, indicate this action and the file type in the link text.

#### Media

- Provide an alt attribute for every image used.
- Provide captions, transcripts, or descriptions of audio and video content.

#### Tables

- Avoid tables where possible.
- Introduce tables in the text preceding the table because not all screen readers preannounce tables.

#### Buttons

- Refer to buttons and other elements by their label. For visual elements that have no text, don't try to describe the element. Instead, use the element's `aria-label` attribute if possible.

> [!NOTE]
> This can be modified, updated and overwritten as required.

### Notes and other notices

See: [Notes, cautions, warnings, and other notices](https://developers.google.com/style/notices)

Janeway-specific:

The following notices are available in GitHub markdown:

> [!NOTE]
> Note.

- An ordinary aside or tip. Provides information that is useful but not critical to the reader. For example, "Generating excessive amounts of traffic to external systems can resemble a denial-of-service attack."

> [!CAUTION]
> Caution.

- Tells the reader to proceed carefully. For example, "We don't recommend using a broad `0.0.0.0/0` range that would allow all traffic."

> [!WARNING]
> Warning.

- Stronger than a **caution** notice; it means "Don't do this" or that this step might be irreversible, such as leading to permanent data loss. If readers don't heed the warning, they can lose work or open themselves to a security breach. For example, "Don't put a password on the command line; doing so is a security risk."

> [!IMPORTANT]
> Important.

- Can be used to highlight essential information. This information must also be in the main body of the text.

> [!TIP]
> TIP.

- Provides helpful information that has a practical meaning but may not be obvious to users.
