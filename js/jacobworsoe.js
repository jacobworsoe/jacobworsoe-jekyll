var JacobWorsoeMain = {
  init: function() {
    this.bindUIActions();
  },

  bindUIActions: function() {
    // single.php
    if (
      (typeof pageType !== "undefined" && pageType === "single") ||
      (typeof pageType !== "undefined" && pageType === "page")
    ) {
      ContentAsEcommerce.trackSinglePostAsProduct(product);      

      // Track clicks on links in post content
      document
        .querySelector(".post-content")
        .addEventListener("click", function(e) {
          Tracking.trackLinkClicks(e, "Link click in content");
        });
    }

    // index.php
    if (
      (typeof pageType !== "undefined" && pageType === "homepage") ||
      (typeof pageType !== "undefined" && pageType === "category")
    ) {
      ContentAsEcommerce.trackProductImpressions();

      // Track clicks on posts
      document.querySelector(".content").addEventListener("click", function(e) {
        ContentAsEcommerce.trackClicksOnPosts(e);
      });
    }
  }
};

// Launch main app
JacobWorsoeMain.init();