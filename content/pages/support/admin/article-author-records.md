# Article records

Generally, make changes to articles and their authors in the back office, using pages such as **Edit metadata** and the workflow stages. The back office checks your changes and keeps the article log up to date. There are two tasks that need the admin area:

- Anonymizing an author's comments to the editor if using triple anonymous review.
- Giving an imported article access to a workflow stage it never went through.

## Anonymize an author's comments to the editor

Authors can add comments for the editor when they submit. If these comments need anonymizing for triple anonymous review or other reasons, you can edit them in the admin area.

1. Open the admin area.
2. Under **Submission**, select **Articles**.
3. Search for the article by its title or ID, and open it.
4. In **Comments to the editor**, remove or replace the identifying details.
5. Select **Save**.

Change only **Comments to the editor**. Leave the article's other fields as they are.

## Add a workflow stage to an imported article

Articles brought in with the imports plugin or the backcontent plugin don't go through the workflow. Their workflow bar, the blue bar at the top of the article's pages, will no include any stages before the one they were importd into (none if using the backcontent plugin). If you need to do work at one of those stages, you can add it to the bar.

For example, to generate an HTML galley for an imported article with Pandoc, add the **Typesetting** stage. You can then open the article's typesetting page and use Pandoc, without moving the article out of its current stage.

1. Open the admin area.
2. Under **Submission**, select **Articles**.
3. Find the article in question, by searching for the title or article ID.

   > [!TIP]
   > You can use the _Is import_ filter on the right-hand side to narrow the list, if the article you are looking for has entered Janeway using the import or backcontent plugin.

4. Select the article and scroll down to **Workflow logs**
5. Select **Add another workflow log**
6. In the **Element** column, click the search button next to the field.
7. Search for the stage by name, such as **typesetting**, and filter by the article's journal. Select the stage.
8. Leave **Timestamp** as it is. **User** is optional.
9. Select **Save**.
10. Open the article in the back office and check the new stage appears in the workflow bar.

> [!IMPORTANT]
> Each journal on the press has its own copy of each stage. Always filter by the article's journal, so you add the stage that belongs to it.

Adding a stage doesn't move the article. It only adds the stage to the workflow bar so you can open it.
