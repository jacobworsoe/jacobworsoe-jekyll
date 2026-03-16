var Tracking = {
  trackLinkClicks: function(e, eventCategory) {
    if (!window.google_tag_manager || e.target.tagName !== "A") return;

    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      event: "customLinkClick",
      eventCategory: eventCategory,
      clickText: e.target.innerText,
      href: e.target.href
    });
  }
};
