Title: Journal Settings

# Journal Settings

In journal settings, you can set basic information about the journal, configure home page elements, upload logos and banner images, and adjust some display elements.

If you have the Janeway role Editor or Staff, you can access Journal Settings by selecting **Manager** under **Staff**.

## All Settings

The All Settings page lists every underlying journal-level setting within Janeway and allows you to edit them. The setting groups are:

- Crossref
- Email
- Email Subject
- General
- Identifiers
- Preprints
- Review

This is a fallback area for editing a setting when you can't find it in the interface or for editing settings introduced into your instance.

<!-- ![the All Settings area.](../../nstatic/all-settings.png) -->

<!-- add explanations and what setting groups do -->

## General

The general journal settings page is home to various configuration settings for the journal. Each field is explained in Janeway.

- Journal information (title, ISSN, description, keywords, design theme)
- Publisher information (name, website, contact)
- Email settings for system-generated emails
- Remote website settings
- Language settings
- Integration with Slack or Discord

<!-- SHould this be in dev? Otherwise a note should be here that this is not for regular users

## Accessing Settings in Templates and Code

Setting values can be accessed inside templates using
**journal_settings.group_name.setting_name**:

{% raw %}
```
{{ journal_settings.crosscheck.enable_crosscheck }}
```
{% endraw %}

In Django they can be accessed with **get_setting**:

```py
request.journal.get_setting('group_name', 'setting_name')
```
-->
