var ContentAsEcommerce = {
  // Track clicks on posts
  trackClicksOnPosts: function(e) {
    e = e || window.event;
    var target = e.target || e.srcElement;

    if (target.matches("a.home-post-link")) {      

      // Get data from attributes
      var id = target.dataset.id;
      var title = target.dataset.title;
      var position = target.dataset.position;
      var year = target.dataset.year;      
      var price = target.dataset.price;
      var category = target.dataset.category;
      var href = target.href;

      window.dataLayer = window.dataLayer || [];
      dataLayer.push({
        event: "productClick",
        ecommerce: {
          click: {
            actionField: { list: pageType },
            products: [
              {
                name: title,
                id: id,
                price: price,
                brand: year,
                category: category,
                variant: year,
                position: position
              }
            ]
          }
        }        
      }); // dataLayer.push
    }
  },

  // Track single post as product
  trackSinglePostAsProduct: function(product) {
    // Default time delay before checking location
    var scrollTimeout = 1000;

    // # px before tracking a reader
    var readerLocation = 150;

    // Set some flags for tracking & execution
    var timer = 0;
    var scroller = false;
    var oneThird = false;
    var twoThirds = false;
    var endContent = false;
    var didComplete = false;
    var purchase = false;
    var scrollToEndBeforeOneMinute = false;

    // Content area DIV class
    var contentArea = document.querySelector(".post-content");

    // Set some time variables to calculate reading time
    var startTime = new Date();
    var beginning = startTime.getTime();
    var totalTime = 0;

    // Track the article load as a Product Detail View
    dataLayer.push({
      event: "productDetailView",
      ecommerce: {
        detail: {
          products: product
        }
      }
    });

    // Check the location and track user
    function trackLocation() {
      clearTimeout(scrollTimeout);

      scrollTimeout = setTimeout(function() {
        // http://ryanve.com/lab/dimensions/
        bottom = window.innerHeight + window.pageYOffset;

        // If user starts to scroll send an event
        if (bottom > readerLocation && !scroller) {
          dataLayer.push({
            event: "addToCart",
            ecommerce: {
              add: {
                products: product
              }
            }
          });
          scroller = true;          
        }

        // If one third is reached
        if (
          bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 &&
          !oneThird
        ) {
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

        // If two thirds is reached
        if (
          bottom >= contentArea.offsetTop + contentArea.clientHeight / 3 * 2 &&
          !twoThirds
        ) {
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

        // If user has hit the bottom of the content send an event
        if (
          bottom >= contentArea.offsetTop + contentArea.clientHeight &&
          (!endContent || !purchase)
        ) {
          if (!endContent) {
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
        }

        // If user has reached end of funnel, check if 60 seconds is passed
        if (endContent && !purchase) {
          currentTime = new Date();
          contentScrollEnd = currentTime.getTime();
          timeToContentEnd = Math.round((contentScrollEnd - beginning) / 1000);
          if (timeToContentEnd > 60 && !purchase) {
            // Track purchase
            dataLayer.push({
              event: "purchase",
              ecommerce: {
                purchase: {
                  actionField: {
                    id:
                      new Date().getTime() +
                      "_" +
                      Math.random()
                        .toString(36)
                        .substring(5),
                    revenue: product[0].price
                  },
                  products: product
                }
              }
            });

            // Only do this once!
            purchase = true;

          } else {    
            
            if(!scrollToEndBeforeOneMinute) {                
              dataLayer.push({
                  event: 'removeFromCart',
                  ecommerce: {
                    remove: {
                      products: product
                    }
                  }
                });

                // Only do this once!
                scrollToEndBeforeOneMinute = true;
            }            

          }
        }
      }, 1000);
    }

    // Track the scrolling and track location
    window.addEventListener("scroll", trackLocation);    
  },

  // trackProductImpressions
  trackProductImpressions: function() {
    // Set objects to store posts
    window.ga_products = window.ga_products || [];
    window.ga_products_not_visible = window.ga_products_not_visible || [];

    function checkVisible(elm) {
      var rect = elm.getBoundingClientRect();
      var viewHeight = Math.max(
        document.documentElement.clientHeight,
        window.innerHeight
      );
      return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
    }

    function pushProducts(productElement, i) {
      ga_products.push({
        name: productElement[i].dataset.title,
        id: productElement[i].dataset.id,
        price: productElement[i].dataset.price,
        brand: productElement[i].dataset.year,
        category: productElement[i].dataset.category,
        variant: '',
        list: pageType,
        position: productElement[i].dataset.position
      });
    }

    function sendProducts() {
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({
        event: "productImpressions",
        ecommerce: {
          impressions: window.ga_products
        }
      });
      window.ga_products = [];
    }

    // Cache product element
    var articles = document.querySelectorAll(".home-post-headline a");

    // See if products are in view
    if (articles && articles.length > 0) {
      for (var i = 0; i < articles.length; i++) {
        if (checkVisible(articles[i])) {
          pushProducts(articles, i);
        } else {
          ga_products_not_visible.push(articles[i]);
        }
      }
    }

    // If any products was in view on pageload, send those products
    if (ga_products.length > 0) {
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({
        event: "productImpressions",
        ecommerce: {
          impressions: window.ga_products
        }
      });
      window.ga_products = [];
    }

    // If page contained products not in view, start the scroll tracker
    if (ga_products_not_visible.length > 0) {
      var scrollTimeout;

      function checkProductsInViewOnScroll() {
        clearTimeout(scrollTimeout);

        scrollTimeout = setTimeout(function() {
          for (var i = ga_products_not_visible.length - 1; i >= 0; i--) {
            if (checkVisible(ga_products_not_visible[i])) {
              pushProducts(ga_products_not_visible, i);

              // Remove the product in view from ga_products_not_visible
              ga_products_not_visible.splice(i, 1);
            }
          }

          if (ga_products.length > 0) {
            sendProducts();
          }
        }, 1000);
      }

      // Start scroll listener
      window.addEventListener("scroll", checkProductsInViewOnScroll);
    }
  }
};