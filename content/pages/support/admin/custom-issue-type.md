# Creating custom issue types

Janeway has two built-in issue types: "Issue" and "Collection". You can add your own custom types, such as "Special issue" or "Dossier", to group content in a way that suits your journal. A custom type works in the same way as a collection. It has its own list page, and you can add a link to it in the navigation bar. Issue types belong to one journal. To use a type on several journals, create it for each one.

## Chosing custom issue codes

Choose a code for the new type. Janeway uses the code in web addresses and, by default, in issue DOIs:

- Use lowercase letters, hyphens and underscores only, for example `special-issue`. Codes containing numbers don't work in the navigation link.
- Make the code different from the journal's other issue types.
- Don't change the code once the type is in use. Issue DOIs created from the default pattern include it, for example `10.xxxx/orbit.special-issue.12`.

## Creating a custom issue type

1. Under **Journal**, click **Issue types**.
2. Click **Add issue type**.
3. Complete the form:
   - **Journal**: the journal the type belongs to.
   - **Code**: the code you chose.
   - **Pretty name**: the name readers see, in the singular, for example "Special issue".
   - **Custom plural**: optional. Readers see this name in the navigation bar and on the list page. If you leave it blank, Janeway adds an "s" to the pretty name.
4. Click **Save**.
<!--images-->

You can now select this issue type when creating new issues.
