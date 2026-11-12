# Setting a journal's publishing status

A journal's state controls how Janeway presents it to readers. For example, it controls where the journal is listed on the press website, where its links go, and whether readers can see its public pages.

Some states are set with the journal's **Publishing status**. Others have their own settings. You can set most of them in the journal's General settings. **Disable front end** can only be set in the admin area.

## Journal states

- Active  
  The journal is publishing. It is listed on the press **Journals** page. This is the default for journals.

- Remote  
  The journal isn't hosted on Janeway. It is listed on the press **Journals** page, but its **View** and **Submit** buttons link to the journal's own website. Use this to list a journal that is part of your press but hosted elsewhere.  

  Janeway leaves remote journals out of its KBART feed, but it will be included in the sitemap (but not show the content hosted elsewhere).  

  Set it with **Is remote**, **Remote view URL** and **Remote submit URL**.

- Conference  
  The journal publishes conference proceedings. It is listed on the press **Conferences** page instead of the **Journals** page. Its Crossref deposits use Crossref's conference proceedings format.  

  In the OLH theme, the press menu links to the **Conferences** page automatically. In other themes, add a link to it in the press navigation. The page's address is `/conferences/` on your press website. See [Navigation](../journal-management/navigation.md).  
  Set it with **Is conference**.

- Submission-only  
  The journal has a Janeway submission page and back office, but no other public pages. Readers who go to the journal's home page, articles, issues, collections or search are sent to its submission information page instead. Authors can still sign in, submit and work through the workflow.  

  Use this when a journal:
  - Hosts its other content elsewhere, and only uses Janeway for submissions and the editorial workflow.
  - Is launching and wants to collect submissions while its content pages are still being prepared.

  Set it with **Disable front end**, in the admin area.

- Archived  
  The journal has stopped publishing, but its content stays online. It is listed separately on the press **Journals** page. Janeway's KBART feed reports the journal's last issue, so libraries and discovery services know the run has ended.

  Set it with **Is archived**

**Hide from press** works separately from these states. When it is ticked, the journal isn't listed on the press **Journals** or **Conferences** page, whatever its state.

## Check the state of several journals

1. Open the admin area.
2. Under **Journal**, select **Journals**.

The list shows each journal's **Publishing status**; **Hide from press**, **Is remote** and **Is conference** values. To show only the journals in one state, select a value in the **Filter** panel, such as **By publishing status**.

**Disable front end** isn't shown in the list. To check it, open the journal's record.
