# Create and maintain products

A product record contains the information customers need to decide what to buy. The available fields come from its [product type](../setup/products/types.md).

## Before you start

Have a suitable product type, category page, price/tax setup, and product images ready. For the Trail T-shirt, use Clothing, the T-shirts category, a price of 22.00, and Standard goods. See [Our example shop](../concepts/example-shop.md) for the baseline.

## Create a product

1. Open **Isotope eCommerce → Products** and create a product.
2. Select its product type.
3. Enter a clear name and your SKU.
4. Add a short teaser and a useful full description.
5. Enter its price and tax class, or configure advanced prices if the type requires them.
6. Assign one or more category pages.
7. Add images and save after selecting files.
8. Fill the shipping information needed by your methods.
9. Publish the product and review any start/stop dates.
10. Visit the category and reader as a customer, then add it to the cart.

If you need variants, follow [Variants](variants.md) before treating the parent as the finished sellable item.

## Name, SKU, GTIN, and alias

The name is for people. The SKU is your internal identifier and should distinguish items that staff need to pick or reconcile separately. A GTIN is a standardized external trade identifier, not a replacement for your internal naming plan.

The alias is used for readable product URLs and can be generated from the name. Changing an established alias can affect bookmarked links and search results. Plan redirects through the site's routing setup when replacing public URLs.

## Write for the buyer

Explain what is included, dimensions or fit where relevant, materials, compatibility, and any choices the buyer must make. A teaser helps the list page. A description gives enough information to make the decision.

State limits clearly. If an accessory in a photograph is not included, say so. For personalized products, explain the input you need and the practical constraints.

## Categories and visibility

Categories are Contao pages. A product can appear in more than one. The list element must read those assignments through its category scope.

Publication can depend on the product's published setting and date range. Protected products also depend on member groups. Check while logged out and as the intended member when access differs.

## Inventory expectations

An SKU and a shipping weight do not provide stock control. Stock reservations, stock deductions, and overselling protection need a stock extension or warehouse integration. Verify any stock extension or warehouse integration separately, including concurrent purchases and cancellations.

## Maintaining products

After changing a price, type, image, or option, test the reader and a new cart. When retiring a product, unpublish it or follow your catalog retirement process before deleting historical references. Existing orders and generated documents need to remain understandable.

For imports or bulk changes, use a compatible integration and rehearse on a copy. Direct database edits can bypass validation, category relationships, variants, and indexing behavior.
