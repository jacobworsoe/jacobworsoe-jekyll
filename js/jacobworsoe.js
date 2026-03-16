var JacobWorsoeMain = {
  init: function() {
    this.bindUIActions();
  },

  bindUIActions: function() {
    if (typeof pageType === "undefined") return;

    if (pageType === "single" || pageType === "page") {
      if (typeof product !== "undefined" && Array.isArray(product) && product.length) {
        ContentAsEcommerce.trackSinglePostAsProduct(product);
      }
      var postContent = document.querySelector(".post-content");
      if (postContent) {
        postContent.addEventListener("click", function(e) {
          Tracking.trackLinkClicks(e, "Link click in content");
        });
      }
    }

    if (pageType === "homepage" || pageType === "category") {
      ContentAsEcommerce.trackProductImpressions();
      var contentEl = document.querySelector(".content");
      if (contentEl) {
        contentEl.addEventListener("click", function(e) {
          ContentAsEcommerce.trackClicksOnPosts(e);
        });
      }
    }
  }
};

JacobWorsoeMain.init();
