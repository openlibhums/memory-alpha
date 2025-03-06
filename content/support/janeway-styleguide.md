# Janeway styleguide
## In this guide
* [Introduction](#introduction)
* [Editorial resources and hierarchy](#editorial-resources-and-hierarchy)
* [Quick reference](#quick-reference)
* [Content](#content)
* [Language and grammar](#language-and-grammar)
* [Punctuation](#punctuation)
* [Formatting and organisation](#formatting-and-organisation)

## Introduction

This style guide is adapted from the [Google style guide](https://developers.google.com/style) (which is available under a CC-BY 4.0 license) and has been adjusted to meet Janeway’s requirements. It will follow Google’s structure as well. This style guide ___does not___ follow OLH or OLHJ style - this is as it a) will have different requirements than OLH(J), b) will make this style guide easier to customise and maintain. This guide uses UK English. This guide uses the Chicago style (17th edition) for citations and referencing.


## Editorial resources and hierarchy

Use the following resources, including this guide, in this order:
1. **Project-specific.** Specific projects may have their own style guides, outlining exceptions to this guide or terms that are relevant only to your project (such as marketing materials).

2. **This style guide.** Where project-specific style guides do not provide guidance, follow this style guide.

3. **Third-party resources.** If the previously listed resources do not provide guidance, you may wish to use the following:

* Spelling: [Oxford English Dictionary](https://www.oed.com/) <!-- Internal note: BBK has a subscription. -->
* If spelling not covered by OED: [Guardian and Observer style guide](https://www.theguardian.com/guardian-observer-style-guide-a)
* Technical style: [Google documentation style guide](https://developers.google.com/style)
* Non-technical style: [The Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html)
<!--	Internal note: SH has a copy available.-->

Other resources that may be helpful (especially when adding to / modifying this guide), but that are not part of the documentation itself:

* [Microsoft Writing Style Guide](https://learn.microsoft.com/en-gb/style-guide/welcome/)
* [Write the Docs](https://www.writethedocs.org/guide/writing/style-guides/)
* [Red Hat supplementary style guide for product documentation](https://redhat-documentation.github.io/supplementary-style-guide/)
* [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/)
* Strategic writing for UX - Torrey Podmajersky
* Don’t make me think, revisited - Steve Krug

## Quick reference

### Tone and content
* Be conversational and friendly without being frivolous. Remain professional.
* Avoid jargon or (complex) technical language where possible. If a term is required, explain it.
* Don’t pre-announce anything in the documentation.
* Use descriptive link text.
* Write accessibly.
* Write for a global audience.

### Language and grammar
* Use UK English spelling and punctuation.
* Use the second person (“you” rather than “we”).
* Use active voice.
* Put conditions before instructions, not after.

### Formatting, punctuation, and organisation
* Use sentence case for all headings: capitalise the first word, but do not use a period at the end.
* Use serial commas.
* Use numbered lists for sequences.
* Use bulleted lists for most other lists.
* [Lists guide](https://developers.google.com/style/lists)
* Use unambiguous date formatting.
* Put UI elements in bold.
* [UI elements and interaction guide](https://developers.google.com/style/ui-elements)

>[!NOTE]
> As labels are inconsistent, use title case for page titles and sentence case for other elements. This will need to be revisited because Janeway itself is inconsistent.

### Images
* Provide alt text.
* Provide high-resolution or vector images when practical.
* [Diagrams, figures, and other images guide](https://developers.google.com/style/images)

## Content

### Voice and tone
See: [Voice and tone](https://developers.google.com/style/tone)

At a glance:
* Be friendly, conversational, and respectful.
* Be polite, but avoid _please_.
* Be clear and consistent. 

Avoid:
* Buzzwords and jargon.
* Placeholder phrases like _please note_ and _at this time_.
* Choppy or long-winded sentences.
* Starting all sentences with the same phrase (such as _You can_ or _To do_).
* Using phrases like _simply_, _It's that simple_, _It's easy_, or _quickly_ in a procedure.

### Global audience
See:[ Write for a global audience ](https://developers.google.com/style/translation)

At a glance:

* Use present tense.
* Write dates and times in unambiguous and clear ways.
* Provide context. Don't assume that the reader already knows what you're talking about.
* Avoid negative constructions when possible. Consider whether it's necessary to tell the reader what they can't do instead of what they can.
* Be consistent with your writing (font, wording, capitalisation, lists, etc.).
* Avoid colloquialisms, idioms, or slang.
* Don't be too culturally specific. In particular, don't refer to specific holidays, cultural practices, or sports unless you're certain they're known worldwide.

### Prescriptive documentation
See: [Prescriptive documentation ](https://developers.google.com/style/prescriptive-documentation)

At a glance:

Prescriptive documentation recommends a way to achieve tasks. It tells the reader what to do instead of giving them a list of options to choose from. When a goal or task is complex and involves multiple approaches or products, prescriptive documentation recommends a path. 
 
To indicate required or optional user actions or process outcomes, select an appropriate auxiliary verb — for example, _must_, _can_, or _might_. Generally, avoid the word _should_.

### Accessibility
See: [Write accessible documentation](https://developers.google.com/style/accessibility) 

At a glance: 

**General**
* Avoid unnecessary font formatting. (Screen readers explicitly describe text modifications.)
* Avoid bias and harm when discussing disability and accessibility.
* Break up walls of text to aid in scannability. For example, separate paragraphs, create headings, and use lists.
* Place distinguishing and important information of a paragraph in the first sentence to aid in scannability.
* Use shorter sentences. Try to use fewer than 26 words per sentence.
* Define acronyms and abbreviations on first usage and if they're used infrequently.

**Links**
* Use meaningful link text.
* If a link downloads a file, indicate this action and the file type in the link text.

**Media**
* Provide an alt attribute for every image used.
* Provide captions, transcripts, or descriptions of audio and video content.

**Tables**
* Avoid tables where possible.
* Introduce tables in the text preceding the table because not all screen readers preannounce tables.

**Buttons**
* Refer to buttons and other elements by their label. For visual elements that have no text, don't try to describe the element. Instead, use the element's `aria-label` attribute if possible.

>[!NOTE]
>This can be modified, updated and overwritten as required.

### Timeless documentation 
See: [Timeless documentation ](https://developers.google.com/style/timeless-documentation)

At a glance:

Avoid:
* Words and phrases that make promises or project plans and strategies.
* Words and phrases that assume prior knowledge of a product or feature.
* Words and phrases that become outdated soon after publication.

Examples of words to avoid:
* currently
* does not yet
* eventually
* existing
* future, in the future
* latest
* new, newer
* now
* old, older
* presently, at present
* soon

## Language and grammar
### Active voice
See: [Active voice](https://developers.google.com/style/voice)

At a glance:

* Use active voice instead of passive voice; make clear who is performing the action.

### Capitalisation
See: [Capitalisation](https://developers.google.com/style/capitalization)

Divert from Google:
* Use standard capitalisation rules for __UK English.__

Janeway-specific guidance:
Only capitalise Janeway roles when referring to a button / UI element or when explicitly referring to the role. Do not capitalise Janeway roles when referring to people.

For example:

  :heavy_check_mark: **Recommended**: "The Editor role has permissions for…"

  :x: **Not recommended**: "When you assign the typesetter role…"

  
  
  :heavy_check_mark: **Recommended**: "When the typesetter sends the galleys…"

  :x: **Not recommended**: "During review, Section editors require Editors to approve draft decisions."

At a glance:

Don't use unnecessary capitalisation; before capitalising a word, think about why (and whether) it should be capitalised.

Use a lowercase letter to begin the first word of the text immediately following a colon, unless the text is one of the following:
* A proper noun
* A heading
* A quotation
* Text that follows a label such as _Caution_ or _Note_

### Present tense
See: [Present tense](https://developers.google.com/style/tense)

At a glance:

Use present tense for statements describing general behaviour not associated with a particular time. However, it's fine to use future tense (will) to distinguish an action that will occur in the future. Don't use the future tense to describe how a product or feature will work after the next release or update. Also, avoid the hypothetical future _would._

### Sentence structure
See: [Sentence structure](https://developers.google.com/style/sentence-structure)

At a glance:

If you want to tell the reader to do something, try to mention the circumstance, conditions, or goal before you provide the instruction. Mentioning the circumstance first lets the reader skip the instruction if it doesn't apply.

## Punctuation 
### Colons and Semicolons
See: [Colons](https://developers.google.com/style/colons) and [semicolons](https://developers.google.com/style/semicolons)

At a glance:

* When a colon introduces a list, the text that precedes the colon must be able to stand alone as a complete sentence.
* Generally, the first word in the text following a colon should be in lowercase.
* If possible, avoid using semicolons. For exceptions, see [Google style guide on semicolons](https://developers.google.com/style/semicolons).

### Commas
See: [Commas](https://developers.google.com/style/commas)

At a glance:

* Use serial commas.
* In general, place a comma after an introductory word or phrase.
* When a coordinating conjunction (and, but, or, nor, for, so, or yet) separates two independent clauses, insert a comma after the first clause (before the conjunction) unless both clauses are very short.
* When an independent clause and a dependent clause are separated by a coordinating conjunction, insert a comma only if the sentence could be misunderstood without one.

### Periods and end punctuation
See: [Periods and other end punctuation ](https://developers.google.com/style/periods)

At a glance:

* End a complete sentence with a period, unless it's a question. There are exceptions for working in lists.
* Try to avoid a URL directly preceding a period. Either use a link or rewrite the sentence. 
* When a sentence ends with material inside quotation marks, place the period inside the quotation marks even if the period isn't part of the material inside the quotation marks. 
* If the material inside the quotation marks ends with a question mark or an exclamation point, don't use a period.
* If the last part of a sentence is contained inside parentheses, put the period after the closing parenthesis.
* If the parentheses contain a complete sentence, put the period inside the parentheses. 
* Don't use exclamation points in text, except when they're part of a code example.


### Quotation marks and apostrophes
See: [Quotation marks ](https://developers.google.com/style/quotation-marks)

At a glance:

* Generally, avoid quotation marks except when necessary.
    * Code
    * Referring to titles
    * Referring to sections, when you cannot link to the section.
    * Directly citing or quoting.
    * Using a term metaphorically, but only if it's not an established usage in the domain.
* Always use straight quotation marks and straight apostrophes.
* The only times to use single quotation marks in our documentation are the following:
    * In code examples, in languages that use single quotation marks.
    * When nesting a quotation inside another quotation.


## Formatting and organisation
### Notes and other notices
See: [Notes, cautions, warnings, and other notices](https://developers.google.com/style/notices)

Janeway-specific:

The following notices are available in GitHub markdown:

**Note**

* An ordinary aside or tip. Provides information that is useful but not critical to the reader. For example, "Generating excessive amounts of traffic to external systems can resemble a denial-of-service attack." 

**Caution**

* Tells the reader to proceed carefully. For example, "We don't recommend using a broad `0.0.0.0/0` range that would allow all traffic."

**Warning**

* Stronger than a __caution__ notice; it means "Don't do this" or that this step might be irreversible, such as leading to permanent data loss. If readers don't heed the warning, they can lose work or open themselves to a security breach. For example, "Don't put a password on the command line; doing so is a security risk."

**Important**

* Can be used to highlight essential information. This information should also be in the main body of the text.

**Tip**

* Provides helpful information that has a practical meaning but may not be obvious to users.

## Computer interfaces

### Menus, buttons and interaction
See: [UI elements and interaction](https://developers.google.com/style/ui-elements)

At a glance:

When practical, state instructions in terms of what the user should accomplish, rather than focusing on the widgets and gestures. By avoiding reference to UI elements, you help the user understand the purpose of an instruction, and it can help future-proof procedures.

:heavy_check_mark: **Recommended**: **Refresh** the page.

:heavy_check_mark: **Recommended**: Expand the **Advanced options** section.

However, know the audience and understand the context. In some cases, the point of a procedure is to guide the user through elements on the page. Or the UI might not be obvious, and it's helpful to explain the gestures for completing a step. Provide the level of detail that seems useful for the intended audience.

Format names of buttons, menus, windows, etc. in bold. Don't make an official feature name or product name bold, except when it directly refers to an element on the page that uses the name (such as a window title or button name).

:heavy_check_mark: **Recommended**: Click on **Edit metadata** to access the article's metadata.

:x: **Not recommended**: **Janeway** can send automatic reminders.


>[!NOTE]
>As label capitalisation is inconsistent, use sentence case for page titles and labels in all uppercase. When referring to multiple labels that are inconsistently cased, use sentence case for all of the labels. Follow capitalisation as it is on the page for other UI elements. This will need to be revisited.

:x: **Not recommended**: On the **Journal Settings** page, go to the **OTHER** section and select the **Hide from press** checkbox.

:heavy_check_mark: **Recommended**: On the **Journal settings** page, go to the **Other** section and select the **Hide from press** checkbox.

<!--Code in text

Code samples -->
