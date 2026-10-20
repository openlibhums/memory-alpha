export default function renderedHeading() {
  const dataDocumentLink = document.querySelector("[data-document-link]");
  const url = window.location;
  if (dataDocumentLink) {
    // Get the current URL, omitting query parameters and fragment
    dataDocumentLink.href = `${url.protocol}//${url.host}${url.pathname}`;
  }
}
