title: Carousel configuration

# Carousel configuration

The homepage carousel is a rotating banner that can display selected content from your journal, such as articles, news items, issues, or collections. These content types can be mixed within the same carousel.

You can configure the carousel from the **Manager dashboard**:

1. On the Manager dashabord, select **Homepage**.
2. If the carousel is not yet enabled, click **Add** next to **Carousel**.
3. If the carousel is already active, click **Configure**.

To remove the carousel from your homepage, click the **Delete** icon next to it.

## Customising carousel content

The carousel can display three types of content articles, news items, and issues and collections. All of these can appear together in the same carousel. The carousel does not enforce a fixed display order. It cycles through the selected items continuously. For usability reasons, we keeping the total number of items between 5-6 items, and avoiding more than 10.

### Images used in the carousel

The image shown in the carousel comes from the `large image` associated with the item, these are set as part of creating a news item, creating an issue or collection, or publishing an article. <!-- missing hyperlink 3x-->

If an item does not have a large image:
1. Janeway will use the default large image configured in **Images**.
2. If no default image is configured, the system will fall back to the server default image.

For best results, ensure items included in the carousel have suitable large images set. See **Image guidelines** for recommendations. <!--missing hyperlink-->

## Exclude option
The **Exclude** tickbox changes how the selection lists behave.

- **Disabled (default):**  
  The selected items are **included** in the carousel.

- **Enabled:**  
  The selected items are **excluded** from the carousel.

<!-- This is at the moment one of the few places places where I am using the bold for emphasis - which I have not really done elsewhere. BUT I want this to be clear as it's such a pain. Thoughts?-->

## Selecting items for the carousel

When selecting specific content for the carousel, Janeway uses a two-column interface:

- **Available** (left column)
- **Chosen** (right column)

To include an item in the carousel, select it in **Available** and click the **right-facing arrow** to move it to **Chosen**.

To remove an item, select it in **Chosen** and click the **left-facing arrow**.

Buttons below each column allow you to **Select all** or **Remove all** items.

![" "](image.png)

### Articles
Articles can be added automatically or selected manually.

To show recent articles automatically, enable **Latest articles** and set the **Maximum number of articles** to display. For example, if **Latest articles** is enabled and the maximum is 4, the carousel will display the four most recently published articles.

If you prefer to curate the carousel manually, move articles from **Available** to **Chosen** using the selection interface.

### News
Enable **Latest news** to automatically display recent announcements, and set the **Maximum number** of items to include Alternatively, you can manually select specific news items using the selector interface described above.

### Issues and collections
Issues and collections behave the same as articles and news in the carousel. However, instead of the option to show multiple recent issues, is has the option to enable **Current issue** to display the issue currently marked as current.

>[!TIP]
> If changes are not appearing on the homepage, trying clearing the cache. <!-- missing hyperlink-->

## Image contrast and carousel overlays

In the carousel, Janeway will display a low-opacity grey overlay on top of the image. This is used to improve the contrast between the image and the text displayed over it (such as the article or news title).

As a result, the image may appear darker than the original file and/or less vivid than expected. This does _not_ necessarily mean there is a problem with the uploaded image, but may cause issues if you have a strict housestyle.

### Removing the overlay

The overlay can be changed or removed through CSS styling (see Custom styling <!-- missing hyperlink -->). However, this should only be done with care.

> [!WARNING]
> Before removing or reducing the overlay, make sure the text remains clearly readable against the image.

By default, carousel text is white, so removing the overlay may make text difficult to read if the image is pale, bright, or low-contrast.

If you are using custom text colours or disable the overlay, make sure there is still sufficient contrast between the text and the background image.

### Good practice

- Keep the overlay if your carousel images vary in brightness.
- Test carousel slides with both light and dark images.
- Avoid using very pale or very busy images behind text unless you have checked accessibility impact.
- If editing the CSS, review the carousel on mobile as well as desktop.