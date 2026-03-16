var ContentAsEcommerce = {
  trackClicksOnPosts: function(e) {
    var target = (e && e.target) || (window.event && window.event.srcElement);
    if (!target || !target.matches || !target.matches("a.home-post-link")) return;

    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      event: "productClick",
      ecommerce: {
        click: {
          actionField: { list: pageType },
          products: [{
            name: target.dataset.title,
            id: target.dataset.id,
            price: target.dataset.price,
            brand: target.dataset.year,
            category: target.dataset.category,
            variant: target.dataset.year,
            position: target.dataset.position
          }]
        }
      }
    });
  },

  trackSinglePostAsProduct: function(product) {
    var contentArea = document.querySelector(".post-content");
    if (!contentArea) return;

    var scrollTimeout = 1000;
    var readerLocation = 150;
    var scroller = false;
    var oneThird = false;
    var twoThirds = false;
    var endContent = false;
    var didComplete = false;
    var purchase = false;
    var scrollToEndBeforeOneMinute = false;
    var beginning = Date.now();

    dataLayer.push({
      event: "productDetailView",
      ecommerce: { detail: { products: product } }
    });

    function trackLocation() {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(function() {
        var bottom = window.innerHeight + window.pageYOffset;

        if (bottom > readerLocation && !scroller) {
          dataLayer.push({
            event: "addToCart",
            ecommerce: { add: { products: product } }
          });
          scroller = true;
        }

        var contentBottom = contentArea.offsetTop + contentArea.clientHeight;
        var oneThirdY = contentArea.offsetTop + contentArea.clientHeight / 3;
        var twoThirdsY = contentArea.offsetTop + (contentArea.clientHeight * 2) / 3;

        if (bottom >= oneThirdY && !oneThird) {
          dataLayer.push({
            event: "checkout",
            ecommerce: {
              checkout: {
                actionField: { step: 1, option: product[0].dimension1 },
                products: product
              }
            }
          });
          oneThird = true;
        }

        if (bottom >= twoThirdsY && !twoThirds) {
          dataLayer.push({
            event: "checkout",
            ecommerce: {
              checkout: {
                actionField: { step: 2, option: product[0].dimension1 },
                products: product
              }
            }
          });
          twoThirds = true;
        }

        if (bottom >= contentBottom && !endContent) {
          dataLayer.push({
            event: "checkout",
            ecommerce: {
              checkout: {
                actionField: { step: 3, option: product[0].dimension1 },
                products: product
              }
            }
          });
          endContent = true;
        }

        if (endContent && !purchase) {
          var timeToContentEnd = Math.round((Date.now() - beginning) / 1000);
          if (timeToContentEnd > 60) {
            dataLayer.push({
              event: "purchase",
              ecommerce: {
                purchase: {
                  actionField: {
                    id: Date.now() + "_" + Math.random().toString(36).substring(5),
                    revenue: product[0].price
                  },
                  products: product
                }
              }
            });
            purchase = true;
          } else if (!scrollToEndBeforeOneMinute) {
            dataLayer.push({
              event: "removeFromCart",
              ecommerce: { remove: { products: product } }
            });
            scrollToEndBeforeOneMinute = true;
          }
        }
      }, 1000);
    }

    window.addEventListener("scroll", trackLocation);
  },

  trackProductImpressions: function() {
    window.ga_products = window.ga_products || [];
    window.ga_products_not_visible = window.ga_products_not_visible || [];

    function checkVisible(elm) {
      var rect = elm.getBoundingClientRect();
      var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
      return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
    }

    function pushProducts(articles, i) {
      ga_products.push({
        name: articles[i].dataset.title,
        id: articles[i].dataset.id,
        price: articles[i].dataset.price,
        brand: articles[i].dataset.year,
        category: articles[i].dataset.category,
        variant: "",
        list: pageType,
        position: articles[i].dataset.position
      });
    }

    function sendProducts() {
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({
        event: "productImpressions",
        ecommerce: { impressions: window.ga_products }
      });
      window.ga_products = [];
    }

    var articles = document.querySelectorAll(".home-post-headline a");
    if (!articles || !articles.length) return;

    for (var i = 0; i < articles.length; i++) {
      if (checkVisible(articles[i])) {
        pushProducts(articles, i);
      } else {
        ga_products_not_visible.push(articles[i]);
      }
    }

    if (ga_products.length > 0) {
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({
        event: "productImpressions",
        ecommerce: { impressions: window.ga_products }
      });
      window.ga_products = [];
    }

    if (ga_products_not_visible.length > 0) {
      var scrollTimeout;
      function checkProductsInViewOnScroll() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function() {
          for (var i = ga_products_not_visible.length - 1; i >= 0; i--) {
            if (checkVisible(ga_products_not_visible[i])) {
              pushProducts(ga_products_not_visible, i);
              ga_products_not_visible.splice(i, 1);
            }
          }
          if (ga_products.length > 0) sendProducts();
        }, 1000);
      }
      window.addEventListener("scroll", checkProductsInViewOnScroll);
    }
  }
};
