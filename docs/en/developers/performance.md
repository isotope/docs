# Performance

A fast catalog makes browsing easier. Checkout also needs correctness under changing customer context, so measure performance without removing the behavior shoppers rely on.

## Start with evidence

Identify the slow page and record its product count, filters, variant complexity, image sizes, and whether a customer is logged in. Compare a simple category, a large category, a product reader, and checkout.

Have the maintainer measure server time and queries on a test environment. A slow image download and a slow database query need different fixes.

## Keep product lists focused

Use pagination rather than rendering a large catalog on one page. Select a category scope that fits the page. Avoid loading all descendants when a landing page only needs a small selection.

If a list does not show product options, enable **Disable product options**. The element's setting explicitly avoids generating option widgets and loading variants for that purpose. Keep options enabled when customers need to make choices directly in the list.

Limit frontend filter/search fields to useful choices. A dozen rarely used filters can add complexity without helping customers.

## Use appropriate images

Configure separate list and reader gallery sizes. Small list cards should not download unnecessarily large originals. Check cropping and sharpness on actual devices after changing sizes.

Review products with many images and variants. A gallery should provide useful detail without making the initial page heavy.

## Preserve customer-specific behavior

Prices and method availability can depend on member groups, addresses, currency, cart contents, and rules. Do not place cart, checkout, order details, or member information in a shared static cache.

When a reverse proxy or other cache is introduced, have the maintainer verify Contao's cache/session behavior and run two independent customer sessions. One session must never receive the other's cart or personal information.

## Keep scheduled maintenance working

The core registers a daily job for old guest carts and carts belonging to deleted members. The guest timeout defaults to 30 days. Verify that Contao's scheduled tasks actually run, rather than assuming the timeout alone removes records.

See [Bundle configuration](bundle-configuration.md) for the setting.

## Recheck functionality

After optimization, test variants, customer options, search/filter combinations, conditional prices, and checkout. A faster page that loses a required option or shows the wrong price is not a completed improvement.
