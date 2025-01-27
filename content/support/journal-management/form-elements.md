title: Form Elements
# Form Elements
Custom forms in Janeway have the following aspects to them yada yada.

<!-- edit to work for review, submission and hunt for any other custom forms. -->

- Name
	- This field provides the name of the submission element
 In case of a short question, you could put a question in this field. If using a longer question, you may wish to use a more generic description and provide further guidance in the help text.

- Kind
  - blabla kinds yada yada I am so tired besties.

- Required  
  - Check this setting’s box to make this part of the form obligatory to complete.

- Order  
  - This determines the order of elements on the submission form.
 
- Help text  
  - This text will display under the submission element and can provide further guidance or information for authors.

- Default visibility  
  - If enabled, this element will be visible to the author by default once the editor has shared the review with them. If disabled, the author will not see this element unless the editor overrides it.

## Element types (kind)
A submission form element can be one of the following kinds:
- Text field
	- This is a single-line input area for short text answers such as names, keywords or subjects. It does not allow for formatting.
![Example text field](../../support/images/element-text-field.png)

- Text area
	- This is a larger, multi-line input area for longer texts such as comments and descriptions. It allows for formatting and line breaks.
![Example text area](../../support/images/element-text-area.png)

- Checkbox
	- This element asks users to check a box, which can be used to declare no competing interests / agree to terms, for example.
![Example checkbox](../../support/images/element-check-box.png)

- Select (dropdown)
	- Shows a predefined list of options, allowing users to select one. You will need to create the options. This is done through the ‘Choices’ field. The options should be separated by the bar " | " character, e.g. " choice 1|choice 2|choice 2 ".
![Example dropdown](../../support/images/element-select.png)

- Email
	- Specific text field for emails. It checks if the input looks like an email address. / follows the format of an email address.
 ![Example email field](../../support/images/element-email.png)

- Upload
	- Asks the users to upload a file from their device.
    ![Example upload field](../../support/images/element-file-upload.png)

- Date
	-Asks the user to provide a date.
 ![Example date field](../../support/images/element-date.png)

> [!NOTE]
> When using an element kind other than 'Select', you can ignore the ‘Choices’ field.
