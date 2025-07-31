title: Managing submission fields
# Managing submission fields

There are two parts to managing submission fields on Janeway: standard fields and custom fields. The standard fields are the preexisting submission fields on Janeway, whereas the custom ones are any you create.

## Standard submission items

![" "](../../support/images/manager-submission-fields-configurator.png)

There are a set of default submission fields within Janeway, the **Submission fields configurator** allows you to configure which one of these will appear during the submission process. The fields you have checked will display, while any of those which are unchecked will not. The default submission fields include:

- Publication fees
- Submission check <!--check this-->
- Copyright notice
- Competing interests
- Comments to editor
- Abstract
- Language
- License
- Keywords
- Section
- Funding
- Figures and data files

If you choose not to use the license, language and section fields as a part of the submission process, we recommend setting a default value for those. E.g. if you only accept submissions in English, you could remove the language selection from the submission process. If you do so, it is recommended you set English as the default language. If nothing is set, the language will be absent from the article metadata (or license or article type, respectively).

If you are using Janeway in languages other than English, you can also set the label for the submission file. This is what the ‘main text’ the author uploads will be labelled within the system.

![" "](../../support/images/manuscript-label.png)

## Custom submission fields
Under the same header, you will also find **Additional submission fields**. This lets you add custom fields to the submission process. It works similarly to the Review form editor. <!-- missing hyperlink -->

Submission fields are made up of multiple elements. Each element asks for some kind of input from a user by either typing, clicking, or selecting something.

To add a new field, must provide the following:

### Name
For each element, you will need to set a name. That name will display as text above the part which the user fills in or interacts with.
Short questions or prompts such as “Is this your first submission?” or “Upload” should be put  in this field. If you have a longer question or need to provide more details, you may wish to use a more generic header and include additional information in the help text.

### Kind
A submission form can have the following types of form elements:

- Text field
	- This creates a single-line input area for short text answers such as names, keywords or subjects. It does not allow for formatting.

![" "](../../support/images/element-text-field.png)

- Text area
	- This provides a larger, multi-line input area for longer texts such as comments and descriptions. It allows for formatting and line breaks.

![" "](../../support/images/element-text-area.png)

- Checkbox
	- This allows you to ask users to tick a box. These can be used to declare no competing interests or agree to terms and conditions. 

![" "](../../support/images/element-check-box.png)

- Select (dropdown)
	- This lets you provide a set of options to be displayed in a dropdown list, allowing users to select one. 

To add these options, use the **Choices** field. The options should be separated by the bar (" | ") character. This should look like this: "choice 1|choice 2|choice 2". 

![" "](../../support/images/element-select.png)

- Email
	- This is a specific text field for emails. It checks if an email address is correctly formatted before a user submits the form and prompts them to edit it if it is not. 

- Upload
	- This lets a user upload a file from their device.

![" "](../../support/images/element-file-upload.png)

- Date
	-This asks the user to provide a date.

### Choices
The **Choices** field used in the dropdown element will appear for all of these fields. However, it can be ignored in all other cases as it only applies to **Select (dropdown)**. 

### Required
Checking this box will make it obligatory for users to complete that specific field. This means that they cannot submit the form without doing so. Unchecking it means that it will become optional.

### Order
This determines the order of the elements on the submission form. This is expressed numerically, so “1” means that the element will be displayed first, “2” means that it will be displayed second, etc. 

You also have the option to click and drag elements from the full form view to reorder them.

<!-- ### Width
This setting configures the width of the submission element. Being deprecated, still needed?-->

### Help text
Here you have the option to add text that will display under the submission element. This can be used to provide additional information or guidance.
