# GA4 + GTM: content-as-ecommerce (`js/content-as-ecommerce.js`)

Blog posts are pushed to the dataLayer as GA4 **ecommerce** events. **Currency is always `DKK`.** The numeric **value / price** on items is **word count** (engagement metaphor), not money.

Reference: [Measure ecommerce (GTM)](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm)

## Events fired from the site

| Event | When |
|-------|------|
| `view_item_list` | Homepage/category: visible post links enter the viewport (may fire multiple times per page as user scrolls). |
| `select_item` | Click a post link on homepage/category. |
| `view_item` | Single post/page load (one “product” = that post). |
| `add_to_cart` | User scrolls past ~150px on the post. |
| `add_shipping_info` | Scroll past ~33% of `.post-content` (metaphor: content “checkout”). `ecommerce.shipping_tier` = `33pct`. |
| `add_payment_info` | Scroll past ~66% (`payment_type` = `66pct`). |
| `remove_from_cart` | User reaches end of content in &lt; 60 seconds. |
| `purchase` | User reaches end of content after &gt; 60 seconds (assumed read). |

## Data layer shape

Each ecommerce push is preceded by `dataLayer.push({ ecommerce: null })`.

On single posts and pages, `_includes/datalayer_product.html` sets global **`product`** to a one-element array of **GA4 `items` objects** (same keys as below). Homepage/category listing events build that shape in JS from link `data-*` attributes.

Standard GA4 keys on `ecommerce`:

- `currency`: `DKK`
- `value`: sum of `price * quantity` for `items` (word-count based)
- `items`: array of objects with at least `item_id`, `item_name`, `price`, `quantity`, `item_brand`, `item_category`, `item_variant` (empty), `index`
- `purchase` also requires `transaction_id` (unique string per conversion)
- `add_shipping_info`: include `shipping_tier` on `ecommerce` (GTM: Data Layer Variable `ecommerce.shipping_tier`).
- `add_payment_info`: include `payment_type` on `ecommerce` (`ecommerce.payment_type`).

## GTM setup (summary)

1. **GA4 Configuration** tag on all pages (if not already).

2. For each event name above, create a **Google Analytics: GA4 Event** tag:

   - **Event name**: match the dataLayer `event` (e.g. `view_item_list`, `purchase`).
   - Under **More settings → Ecommerce**, enable **Send Ecommerce data** and set **Data source** to **Data Layer**.

3. **Triggers**: **Custom Event**, event name equals the corresponding event (e.g. `view_item_list`, `add_shipping_info`, `add_payment_info`).

4. **Optional – custom dimensions in GA4** (Admin → Data display → Custom definitions):

   - Map `shipping_tier` / `payment_type` if you want them as dedicated dimensions (often available on the ecommerce event payload).

5. **Debug**: GTM Preview + GA4 **DebugView** to confirm `items`, `currency`, and `transaction_id` on `purchase`.

## Migration note

Older Universal Analytics Enhanced Ecommerce events (`productImpressions`, `productClick`, `checkout`, …) are **replaced** by the table above. Update or remove legacy UA EE tags in GTM to avoid duplicate or empty hits.
