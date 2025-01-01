<!-- ## Submission Page Items

A new addition to v1.4 the Submission Page Items system lets you totally
customise the Submission page to your liking. The existing submission
items have automatically been setup for you and can now be edited.

![List of default submission items generated in the v1.4 upgrade process.](../../nstatic/submission-items.png)

You can manage submission items in three ways:

- Link to a setting
- Custom HTML
- Special Display

From the main screen you can add new, edit existing and delete items as
well as re-order them by dragging and dropping rows of the table.

![List of default submission items generated in the v1.4 upgrade process.](../../nstatic/submission-items-reorder.gif)



### Link to a Setting

You can opt to link a submission item to an existing setting so it will
display the same content as that setting. This is currently used for the
majority of the automatically generated submission page items. Some
examples of this are:

- About
- Focus and Scope
- Submission Checklist

You can tell when a submission item is linked to a setting under the
'Setting or Text' column in the main table or the 'Existing setting'
field being completed when editing a submission item.
-->



## Additional Submission Fields

The additional submission fields page allows us to add custom fields to
the Article Info submission page. It works in a similar fashion to the
Review Forms generator.

Field types are:

- Text Field
- Text Area
- Checkbox
- Select (dropdown)
- Email
- Upload
- Date

To add a new Element:

- In the form add Name and select a Kind  
  - If you choose "select" as kind you will need to add the options to
    the Choices field. These should be seperated by the bar "\|"
    character e.g. `choice 1|choice 2|choice 2` or `1|2|3|4|5` if you
    wanted a numeric choice. If you select any other Kind, ignore the
    Choices field.

- Required  
  - If this field MUST be completed, ensure this box is checked, if it
    is optional make sure it is not checked

- Order  
  - The order in which this element will appear on the form

- Width  
  - 1/3, 1/2 or Full width. If you put two half width elements next to
    each other in order they will both display on the same line

- Help text  
  - This text will display under the Name field on the form and explain
    what the reviewer needs to do with this field.


