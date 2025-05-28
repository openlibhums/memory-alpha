title: Editor guide - typesetting 
# Editor guide - typesetting

This stage covers typesetting and proofreading of typeset files.

The typesetting overview screen shows all articles currently in typesetting with their status
You can **Claim** an article to indicate who is managing its typesetting (this doesn't restrict other editors' access). Use the filter in the top-right corner to show only **My assignments**.

This guide will outline three types of typesetting workflows:
Uploading galleys yourself.
Converting files within Janeway.
Working with an external typesetter.
<!-- missing hyperlinks -->

## Typesetting files

Galleys are typeset files used for proofing and displaying content, such as HTML and JATS-XML files. Typeset files typically include, but are not limited to:
- PDF files
- HTML files
- JATS-XML files

All typeset files will become available for download from the article page once the article is published. Janeway can display JATS XML or HTML galleys and list other formats as downloads.

## File labels
When uploading typeset files, Janeway will ask you to set a label. The label will be displayed publicly in the option to download a file as 'Download [label]'. So if you set the label as 'PDF', it will be 'Download PDF'. 

Labels can also be used to denote the language of a file to readers. For instance, labelling a PDF file as 'PDF (EN)' and another as 'PDF (ES)' will allow readers to download the correct PDF for their language.

For PDF, XML and HTML files, Janeway can automatically set the label to the file type if left blank. For other filetypes, it will default to ‘OTHER’ if left blank.

## Manual upload
If you do not use a typesetter or file conversion through Janeway, you can upload typeset files yourself by clicking **Upload new typeset file** in the **Current galleys** section. Once you have selected a file, you can also mark whether the file should be public upon publication and set its label.

When uploading an HTML or XML file with images, they must be uploaded separately. Images can be uploaded by clicking **Edit galley** and using the upload functions provided, for more information see: Images and figure files <!-- missing hyperlink -->. On this page, you can also replace the galley file, edit its label and upload an accompanying CSS file if the article requires specific styling.

Until the images are uploaded and matched to the galley, Janeway will display a missing image warning.

> [!CAUTION]
> Do not use this for supplementary files. See Supplementary files for more information.<!-- missing hyperlink -->

## Generating typeset files with Janeway
Janeway also offers the option to convert manuscript files using the [Pandoc plugin](https://github.com/BirkbeckCTP/pandoc), which can generate HTML galleys from a MS Word document. 

If you are interested in using the Pandoc plugin, contact your System administrator (What is a system administrator? <!-- missing hyperlink -->).

## Working with a typesetter

### Assigning a typesetter

Click **Add typesetter** to open the typesetter assignment page and start a new typesetting assignment. You can now do the following: 
1. Select a typesetter.
2. Select the files you would like this typesetter to work on.
3. Set a due date.
4. Add any notes, e.g. what outputs you would like.
5. Send a notification email to the typesetter (or skip this step).

If no issue has been set yet for this article, you may wish to do this now as typesetters may need this information (especially if working with JATS-XML).

There is no limit on the number of typesetters you can assign at one time.

>[!TIP]
>Typesetters automatically access all images / figure files uploaded by the author and the article metadata. Verify metadata is production-ready via **Actions > View metadata** before assignment.

### Reviewing the typesetting task
Once the typesetter has completed their task, you will receive an email notification. You can now review the typesetting task and select one of the following three options:
- Request corrections
   - If you notice a problem with the typeset files straight away, you can request corrections to the typesetter. See Requesting corrections <!-- missing hyperlink -->
- Proofing required
   - Accept the typeset files and record the decision to send the files for proofing.
- Accept 
   - If no (further) proofing or corrections are required, you can accept the files and end the typesetting stage.

## Proofing
This part of typesetting is used to check galley files for any issues before they are published. Files provided by the typesetter are usually sent to the authors, and potentially other editors, for proofreading. Janeway allows you to create a proofing task, where authors and/or editors can be invited to proof the typeset files.

### Requesting proofreading
Click **Assign proofreaders** to open a new proofing task. All files listed under **Current galleys** will be made available to proofreaders. You can now do the following:

1. Select the proofreader. 

The list of potential proofreaders is made up of editors, the authors of the paper and any other users with the proofreader role. You can only select one proofreader, but you can add multiple assignments. If you wish to select a user who is not displayed in the list, click **Enrol a proofreader**.

2. Set a due date.

3. Provide instructions for the proofreader.

4. After completing this, you can optionally email the proofreader with information about their task.

Proofing assignments can still be edited before they are accepted. You will have the option to edit it using the **Actions** drop-down. You can change the galleys, the due date and the note to the proofreader. There is also a **Delete** button that will completely remove the assignment, though information is retained in Janeway's logs.


////

## Requesting Corrections

As soon as all proofing tasks are completed we will hit the request
corrections button, which will start a new round of typesetting.

![""](../nstatic/typesetting/request-corrections-button.png)

Now we can asssign a typesetter to work on the corrections (usually, the
same typesetter that produced the Typeset Files in the first place).
When creating the task, we will be presented with the option to include
the feedback from the proofreaders.

![""](../nstatic/typesetting/corrections-notes-display.png)

Even when the comments are made available, it is still recommended that
the editor/production manager summarises the corrections requested using
the "task" field (especially in cases where the proofreaders might
request contradictory corrections). We can also select which files the
typesetter needs to apply the corrections to:

![""](../nstatic/typesetting/corrections-files.png)

After the task is sent out, we just have to wait for the typesetter to
complete it, at which point we can review their work and dispatch new
proofing tasks to the author if necessary, or accept their changes and
complete the process.

## Supplementary Files

Authors are able to upload supplementary files to Janeway as part of
their submission. If the intention is to host the file on Janeway
Editors can create a Supplementary File object and assign it a DOI
within Janeway. This section is located at the bottom of the Typesetting
Article page. If the file isn't already uploaded to Janeway you can opt
to upload a new file.

> [!TIP]
> You should create the supplementary file object in advance of sending
the article for typesetting where possible and notify the typesetter (if
you use external typesetters). They will be able to see the file record
and the DOI that has been assigned to it.

![""](../nstatic/typesetting/supp-files.gif)

## Managing Typeset Files/Galleys

Once a typesetter or production manager has uploaded typeset files into
Janeway they become manageable within the system. To manage a typeset
file/galley press the Edit icon on the relevant table row.

![""](../nstatic/typesetting/editor/typeset-files.png)

An XML typeset file with missing figure files.

### File Detail

![""](../nstatic/typesetting/editor/file-details.png)

The file label is displayed on the main article page and is displayed in
the format "Download Label". If you set the label to XML it will read
"Download XML".

> [!TIP]
> When uploading a PDF, XML or HTML file Janeway will set the label for
you automatically if you leave it blank.

You can also mark a typeset file as not for public consumption by
unchecking the "Public" field in this section.

### Replacing the Typeset File

![""](../nstatic/typesetting/editor/edit-typeset-file.png)

If you need to upload a new version of the typeset file you can do so
from within the Edit Typeset File screen. Browse for the new file and
click Upload. The old version of the file is retained. Alternatively you
could mark this file as not public and upload a new typeset file if you
wanted to keep two separate file records.

### Image/Figure Files

HTML and XML files that are uploaded will be scanned by Janeway to
detect graphic, figure or img tags. If tags are found that have no
corresponding Image file will report on the main typesetting page as
having missing images. (see figure at the top of this section for an
example). You can load up images against a typeset file by editing it
and scrolling to the Image File section.

![""](../nstatic/typesetting/editor/image-files.png)

For each missing image file Janeway will present you with a block where
you can either upload a new image file or select an existing one from
the images already linked to the article.

> [!TIP]
> For typeset files with a large number of images you can also create a
zip archive and place an image (with a name matching those in the file)
and upload it using the Zip Uploader. Janeway will unzip the archive and
assign the images based on their name.

### CSS and XSL files

CSS File
If a given article requires special styling you can upload a CSS file alongside it and Janeway will output it on the article page.

> [!WARNING]
> The CSS uploaded here should only target elements inside the <article> block otherwise it could break general styling of the site.

XSL File
Janeway's XSL Transformation process uses a version controlled XSL (Extensible Stylesheet Language) file. When you upload a JATS XML file to Janeway it marks the file as using the current XSL file. This means that as we make changes to the XSL file it will only affect future files uploaded and not any back content.

> [!WARNING]
> Changing a XML file's XSL may cause it to render differently. It is only recommended that you do this before sending it for proofreading.
