# Similarity checker

You can check submitted files for similarity with published work, using iThenticate from Turnitin. Crossref also offers iThenticate to its members as [Similarity Check](https://www.crossref.org/services/similarity-check/).

Janeway connects to iThenticate through the [Turnitin plugin](https://github.com/openlibhums/turnitin_tca). You send a file from the editorial workflow, and Janeway shows the similarity score and a link to the full report. The plugin works with Janeway 1.7 and later.

Janeway versions before 1.9 also include a built-in iThenticate integration. For more information, see [Built-in Crosscheck settings](#built-in-crosscheck-settings).

## Before you start

You need an iThenticate account with access to the Turnitin Core API. You can buy iThenticate directly from Turnitin or through [Crossref Similarity Check](https://www.crossref.org/services/similarity-check/).

Your Janeway system administrator installs the plugin and enters your Turnitin account details. One Turnitin account covers every journal on your Janeway installation.

If your iThenticate licence comes directly from Turnitin, editors accept the Turnitin End User Licence Agreement (EULA) the first time they send a file. If your licence comes through Crossref, editors don't see the EULA.

## Turn on the plugin for your journal

1. Go to the manager and select **Turnitin Core API** from the list of plugins.
2. Select **Turnitin Core API enabled**.
3. Optional: Change the report options. For more information, see [Choose what the score includes](#choose-what-the-score-includes).
4. Select **Save**.

The **Turnitin account** box on the same page shows whether your administrator has set up the account and whether your licence requires the EULA.

## Send a file for a similarity report

Editors and journal managers can send files. Section editors can send files for the articles they are assigned to.

1. Open the article's similarity page in one of the following ways:
   - On the **Unassigned** or **In Review** page for the article, select **Turnitin Similarity** in the **Actions** box.
   - Select **Turnitin Similarity** in the editor menu, find the article, and select **Similarity**. This list shows articles from submission to the end of review.

   > [!NOTE]
   > Janeway 1.7 doesn't show the option in the **Actions** box, and Janeway 1.8 shows it on the **In Review** page only. In these versions, use the editor menu.

2. Find the file you want to check, and select **Send for report**.
3. If Janeway shows the EULA, read it and select **Accept and continue**.

The similarity page lists every file attached to the article. Each file has a type: **Manuscript**, **Data/Figure**, **Source**, **Current revision**, or **Review round** followed by the round number.

Reports usually take a few minutes. When a report is ready, Janeway emails the editor who sent the file.

## Report statuses

The **Status** column shows where each file is in the process:

- **Not sent**  
  Nobody has sent the file to Turnitin yet.

- **Processing**  
  Turnitin has the file and is generating the report.

- **Retrying**  
  The send failed because of a temporary problem. Janeway tries again automatically, and shows the time of the next attempt.

- **Report ready**  
  The report is complete, and the **Similarity** column shows the score.

- **Error**  
  The send or the report failed. Janeway shows the reason under the status.

## Read the report

To open the full report in the Turnitin viewer, select **View Report**.

The similarity score is the percentage of the file that matches other sources. A high score doesn't prove plagiarism. For example, it can come from properly cited quotations or the author's own preprint. Check the matches in the report before you make a decision.

Your system administrator chooses whether Turnitin keeps the changes you make in the viewer, such as excluding a source. If Turnitin keeps them and the score changes, Janeway updates the score on the similarity page.

To check the same file again, select **Request new report**. The new report replaces the current score.

## Choose what the score includes

Report options control which parts of a file count towards the similarity score. Your system administrator sets defaults for the whole installation, and you can change them for your journal on the plugin settings page.

- **Exclude quotes**  
  Leaves text in quotation marks out of the score.

- **Exclude bibliography**  
  Leaves the reference list out of the score.

- **Exclude citations**  
  Leaves in-text citations out of the score.

- **Exclude abstract**  
  Leaves the abstract out of the score.

- **Exclude methods**  
  Leaves the methods section out of the score.

- **Exclude custom sections**  
  Leaves out the custom sections defined in your iThenticate account.

- **Exclude preprints**  
  Leaves matches against preprints out of the score.

- **Exclude small matches**  
  Leaves matches shorter than the **Small match word count** out of the score. The word count must be at least 8.

Report options apply to new reports. Editors can also change them in the Turnitin viewer for a single report.

## Fix failed sends

If a file shows **Error**, select **Resend**. Janeway sends the file again as a new submission to Turnitin.

If several files have failed, select **Resend all failed** at the top of the similarity page.

If the file reached Turnitin but the report failed, select **Request report again**.

If a file keeps failing, contact your system administrator. They can see the full error message from Turnitin and raise it with Turnitin support.

## Built-in Crosscheck settings

Janeway versions before 1.9 include a built-in iThenticate integration. You set it up from **Crosscheck Settings** in the manager. The Turnitin plugin doesn't use these settings. If you use the plugin, leave them blank.

The settings are:

- **Enable Crosscheck**  
  Adds a **Similarity Check** column to the files on the **Unassigned** page, so that editors can send files and view reports.

- **Username for crosscheck/ithenticate**  
  Your iThenticate username.

- **Password for crosscheck/ithenticate**  
  Your iThenticate password.

Janeway only sends files to iThenticate when you enter both the username and the password.
