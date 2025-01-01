Issue DOI Pattern  
Janeway supports minting DOIs for journal issues automatically. With
this setting, you can define the pattern used to generate the
issue-level DOI that will be used for registration.

With the default pattern, an issue with ID `1` (and prefix `10.0001`,
and journal code `abcd`) will have a generated DOI of
`10.0001/abcd.issue.1`.

A collection with an ID of `2` would have a generated DOI of
`10.0001/abcd.collection.2`.

Auto-register issue-level DOIs  
When enabled, issues will have a DOI assigned and registered as soon as
the first article in the issue is scheduled for publication. If an issue
DOI has not been entered manually, Janeway will use the pattern defined
in the setting above to generate one automatically.
