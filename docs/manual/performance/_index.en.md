---
title: Performance
description: Performance.
aliases:
    - /en/performance/
weight: 50
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Isotope eCommerce was built with full flexibility in mind. Flexibility means unlimited possibilities, but flexibility also comes at the cost of performance.

This chapter shows you what you can do to speed up your webshop.

## Server

Most of the time this aspect gets lost. Performance is not only the task of Isotope eCommerce or Contao but also to a large extent of the server environment.

1. **Webhosting:** Who buys cheap, gets cheap. A good webhosting is the basis for a good working webshop. So a webhosting for € 1,- per month is most likely not the right basis for Isotope eCommerce.
2. **Safe Mode Hack:** If you need the Safe Mode Hack, this means that PHP has no rights to write files on the server and therefore has to take the (slow) detour via the FTP login. In simple words: Your server is misconfigured. You're better off not even trying, and you should revisit point 1.
3. **Database:** If the interface to your database is slow, that means every single query to the database is slow. You can imagine that Isotope has to make quite a lot of queries to the database due to its flexibility and if every single one of 100 queries costs two milliseconds more than a good connection, you are already wasting two tenths of a second on every call.
4. **PHP version:** The PHP developers constantly provide us with new versions. Of course, they also have an eye on performance and memory consumption. If possible, you should always use the latest available version, even if Isotope or Contao would also work on a lower version. The differences are sometimes serious.

## Isotope eCommerce

1. **The internal cache**: If the internal cache is not set up or checked in the settings `Internen Cache umgehen`, the load time of the entire website will immediately increase exponentially. So if you want to do performance testing, the internal cache must always be enabled!
2. **The deb**ug mode: The debug mode comes in handy during the development of Contao extensions. However, it also bypasses all isotope eCommerce internal caches and a lot of time goes into debugging output.
3. **The frontend preview with unpublished elements**: Optimizing queries to the database (keyword: SQL keys) can speed those up. If you use the frontend preview and have `unveröffentlichte Elemente anzeigen` enabled, the queries will change slightly and the optimizations will no longer work. So performance testing never with frontend preview enabled.
4. **Rules:** Rules are handy, but they can get very complex. Accordingly, they cost time. If you don't need the rules, you should deactivate `isotope_rules` in the system settings!
5. **Price calculation:** In Isotope eCommerce, product prices can be changed dynamically at runtime. Examples of this are time-limited discounts or discounts for certain members. It is therefore not possible to filter or sort the prices already on database level. If possible, you should provide a "Sort by price" function or "Filter by price" function in the product list so that only a manageable number of products need to be filtered or sorted.
6. **Variants with different prices:** In order for Isotope to display the correct starting price (e.g. "from EUR 15.00") in the product list, all variant prices must be calculated. I.e. if you have only 12 products, the list seems short, but if each of them has 40 variants, Isotope has to load 492 (12 x 40 + 12) "products" and their price. There are two optimization options here:
  1. Misconfiguration: You don't have different prices per variant and simply activated the attribute "Price" in the variant attributes and enter one and the same price for each variant? Deactivate the price in the variant attributes and select it in the normal product attributes instead. You then only need to maintain it once in the product itself, and Isotope doesn't have to go through all the variants only to find that the price would actually always have been identical. There is also potential for optimization here if you have only entered one product type for all your products out of sheer convenience, even though only some of them have different prices: There you could create a product type "Product with different prices per variant" and a "Product without different prices per variant" and thus optimize the performance.
  2. Benefit from lazy loading: If you don't need the price display in the list, you can remove the call to `<?php echo $this->generatePrice(); ?>` in the template. Isotope will then also not calculate prices for the list display.

{{% notice info %}}
With the appropriate budget and the developer(s) you trust, custom performance analysis and optimization can of course always be done.
{{% /notice %}}
