Title: Review settings

# Review settings

Under review settings we can control how peer review operates for the
given journal. The settings editable here are:

- Review guidelines  
  - A set of generic review guidelines that a reviewer should follow.

- Default Review Visibility  
  - Either Open, Anonymous or Double Anonymous, this is the default
    information visibility for a review assignment. If open, authors can
    see reviewers and vice versa, if single anonymous reviewers can see
    authors, if double anonymous neither can see information on the
    other. When using double anonymous review, the editor must ensure
    the manuscript files are anonymous.

- Default Review Days  
  - The default number of days a reviewer is given, this is used to then
    control reminders. This field is set to 56 days (8 weeks) initially.
    The due date can be changed on a per review basis.

- One Click Access  
  - If enabled a special access token is appended to the reviewer link
    in the assignment email, this link allows the reviewer to view the
    review without logging into the system. Once the review is complete
    the token is deleted so it cannot be reused. Tokens are UUID4s which
    are unique.

- Draft Decisions  
  - If enabled, section editors will not be able to accept papers,
    instead they can make recommendations to senior editors who can then
    accept papers.

- Enable open peer review  
  - Turns on the open peer review feature (see below).

- Default Review Form  
  - The default review form that will be automatically selected when
    assigning a reviewer.

- Reviewer Form Download  
  - If enabled this allows the Reviewer to download a copy of the review
    form in DOCX format to complete offline and then upload.

- Enable save review progress  
  - If enabled, reviewers will be able to save the progress in a
    peer-review assignment and come back later to complete it later
    (Only recommended for journals using custom review forms that are
    particularly long)

- Accept Article Warning  
  - This is a block of text displayed to the editor before they accept
    an article, prompting initial DOI and metadata registration with
    Crossref if the journal or press is set to use Crossref. You can use
    the setting to provide a readout of current metadata so the editor
    can do a quick check of what will be sent to Crossref.

- Enable expanded review details  
  - When this setting is enabled, the editor's review dashboard will
    show all active reviews. Otherwise it will show just a count of
    completed reviews.



<!-- ## Reviewer cannot access a review

Its possible because of how emails are edited that an outgoing review
request will not contain a valid review request URL. We recommend you
reset your review_assignment email in this instance and here is a
workaround to assist reviewers who have received the email without the
link:

1.  Go to the article review page.
2.  For the Reviewer having the issue select the View button.
3.  You'll see an Access Code like below image.
4.  Copy this link and send it to the reviewer.

![""](../old-docs/nstatic/view-review.png)-->
