/**
 * GA4 ecommerce-style dataLayer for "content as product" (blog posts).
 * Currency DKK; "price" is word count (engagement metaphor).
 * @see https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm
 */
var ContentAsEcommerce = (function() {
  var CURRENCY = "DKK";

  function parsePrice(v) {
    var n = parseFloat(v, 10);
    return isNaN(n) ? 0 : n;
  }

  /** 0-based index; listing markup uses 1-based data-position */
  function itemIndexFromDataPosition(pos) {
    var idx = parseInt(pos, 10);
    if (isNaN(idx)) return 0;
    return Math.max(0, idx - 1);
  }

  /** GA4 item from home/category link data-* attributes */
  function itemFromHomeDataset(ds) {
    return {
      item_id: String(ds.id != null ? ds.id : ""),
      item_name: String(ds.title != null ? ds.title : ""),
      price: parsePrice(ds.price),
      quantity: 1,
      item_brand: String(ds.year != null ? ds.year : ""),
      item_category: String(ds.category != null ? ds.category : ""),
      item_variant: "",
      index: itemIndexFromDataPosition(ds.position)
    };
  }

  function withListContext(item, listId, listName) {
    var o = Object.assign({}, item);
    if (listId) o.item_list_id = listId;
    if (listName) o.item_list_name = listName;
    return o;
  }

  function cloneItems(items) {
    var out = [];
    for (var i = 0; i < items.length; i++) out.push(Object.assign({}, items[i]));
    return out;
  }

  function lineValue(item) {
    return (item.price || 0) * (item.quantity || 1);
  }

  function sumItemsValue(items) {
    var t = 0;
    for (var i = 0; i < items.length; i++) t += lineValue(items[i]);
    return t;
  }

  /**
   * Clear previous ecommerce object, then push GA4-shaped event.
   * @param {string} eventName
   * @param {object} ecommerce - currency, value, items, transaction_id, etc.
   * @param {object} [extraRoot] - optional root-level keys merged into payload
   */
  function pushGa4Ecommerce(eventName, ecommerce, extraRoot) {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({ ecommerce: null });
    var payload = { event: eventName, ecommerce: ecommerce || {} };
    if (extraRoot) {
      for (var k in extraRoot) {
        if (Object.prototype.hasOwnProperty.call(extraRoot, k)) payload[k] = extraRoot[k];
      }
    }
    dataLayer.push(payload);
  }

  function listLabels() {
    var id = typeof pageType !== "undefined" ? String(pageType) : "list";
    var name =
      id === "homepage"
        ? "Homepage"
        : id === "category"
          ? "Category"
          : id.charAt(0).toUpperCase() + id.slice(1);
    return { id: id, name: name };
  }

  return {
    trackClicksOnPosts: function(e) {
      var target = (e && e.target) || (window.event && window.event.srcElement);
      if (!target || !target.matches || !target.matches("a.home-post-link")) return;

      var labels = listLabels();
      var item = withListContext(itemFromHomeDataset(target.dataset), labels.id, labels.name);
      pushGa4Ecommerce("select_item", {
        item_list_id: labels.id,
        item_list_name: labels.name,
        items: [item]
      });
    },

    trackSinglePostAsProduct: function(itemsInput) {
      var contentArea = document.querySelector(".post-content");
      if (!contentArea) return;

      var scrollTimeout = 1000;
      var readerLocation = 150;
      var scroller = false;
      var oneThird = false;
      var twoThirds = false;
      var endContent = false;
      var purchase = false;
      var scrollToEndBeforeOneMinute = false;
      var beginning = Date.now();

      var items = cloneItems(itemsInput);
      var v = sumItemsValue(items);

      pushGa4Ecommerce("view_item", {
        currency: CURRENCY,
        value: v,
        items: items
      });

      function trackLocation() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(function() {
          var bottom = window.innerHeight + window.pageYOffset;
          var itemsNow = cloneItems(itemsInput);
          var val = sumItemsValue(itemsNow);

          if (bottom > readerLocation && !scroller) {
            pushGa4Ecommerce("add_to_cart", {
              currency: CURRENCY,
              value: val,
              items: itemsNow
            });
            scroller = true;
          }

          var contentBottom = contentArea.offsetTop + contentArea.clientHeight;
          var oneThirdY = contentArea.offsetTop + contentArea.clientHeight / 3;
          var twoThirdsY = contentArea.offsetTop + (contentArea.clientHeight * 2) / 3;

          if (bottom >= oneThirdY && !oneThird) {
            pushGa4Ecommerce("add_shipping_info", {
              currency: CURRENCY,
              value: val,
              shipping_tier: "33pct",
              items: itemsNow
            });
            oneThird = true;
          }

          if (bottom >= twoThirdsY && !twoThirds) {
            pushGa4Ecommerce("add_payment_info", {
              currency: CURRENCY,
              value: val,
              payment_type: "66pct",
              items: itemsNow
            });
            twoThirds = true;
          }

          if (bottom >= contentBottom && !endContent) {
            endContent = true;
          }

          if (endContent && !purchase) {
            var timeToContentEnd = Math.round((Date.now() - beginning) / 1000);
            if (timeToContentEnd > 60) {
              var tid =
                Date.now() + "_" + Math.random().toString(36).substring(5);
              pushGa4Ecommerce("purchase", {
                transaction_id: tid,
                currency: CURRENCY,
                value: val,
                items: itemsNow
              });
              purchase = true;
            } else if (!scrollToEndBeforeOneMinute) {
              pushGa4Ecommerce("remove_from_cart", {
                currency: CURRENCY,
                value: val,
                items: itemsNow
              });
              scrollToEndBeforeOneMinute = true;
            }
          }
        }, 1000);
      }

      window.addEventListener("scroll", trackLocation);
    },

    trackProductImpressions: function() {
      window.contentItemListBuffer = window.contentItemListBuffer || [];
      window.contentItemListPending = window.contentItemListPending || [];
      var labels = listLabels();

      function checkVisible(elm) {
        var rect = elm.getBoundingClientRect();
        var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
        return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
      }

      function pushProducts(articles, i) {
        contentItemListBuffer.push(
          withListContext(itemFromHomeDataset(articles[i].dataset), labels.id, labels.name)
        );
      }

      function sendProducts() {
        var raw = window.contentItemListBuffer.slice();
        if (!raw.length) return;
        pushGa4Ecommerce("view_item_list", {
          item_list_id: labels.id,
          item_list_name: labels.name,
          items: raw
        });
        window.contentItemListBuffer = [];
      }

      var articles = document.querySelectorAll(".home-post-headline a");
      if (!articles || !articles.length) return;

      for (var i = 0; i < articles.length; i++) {
        if (checkVisible(articles[i])) {
          pushProducts(articles, i);
        } else {
          contentItemListPending.push(articles[i]);
        }
      }

      if (contentItemListBuffer.length > 0) {
        sendProducts();
      }

      if (contentItemListPending.length > 0) {
        var scrollTimeout;
        function checkProductsInViewOnScroll() {
          clearTimeout(scrollTimeout);
          scrollTimeout = setTimeout(function() {
            for (var j = contentItemListPending.length - 1; j >= 0; j--) {
              if (checkVisible(contentItemListPending[j])) {
                pushProducts(contentItemListPending, j);
                contentItemListPending.splice(j, 1);
              }
            }
            if (contentItemListBuffer.length > 0) sendProducts();
          }, 1000);
        }
        window.addEventListener("scroll", checkProductsInViewOnScroll);
      }
    }
  };
})();
