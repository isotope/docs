# Product prices and quantity tiers

Start with a simple price unless the product genuinely needs conditional pricing. Decide how tax is included before entering amounts. See [Prices and taxes](../concepts/prices-and-taxes.md).

The amounts below use the [Trail T-shirt](../concepts/example-shop.md), with Standard goods and the fictional 10% tax included.

## Simple price

A simple price combines an amount and a tax class. The active store configuration supplies currency context and price display behavior.

Check the displayed result after saving. An entered 22.00 with included tax is different from 22.00 before tax, even though the number in the form looks identical.

## Advanced prices

Before using this section, have the person responsible for [product types](../setup/products/types.md#advanced-pricing) enable advanced pricing for Clothing. Each entry can contain a tax class, a rule, and a set of tier prices.

Isotope uses the **first advanced price entry whose rule matches**. An entry without a rule matches without restriction. Put specific entries first and an unrestricted fallback last.

For example:

| Entry order | Rule | Unit price from quantity 1 |
| --- | --- | ---: |
| 1 | Member belongs to Trade customers | 17.60 |
| 2 | No rule | 22.00 |

If the unrestricted entry comes first, it prevents the trade entry from being selected. A rule's numeric priority does not replace the price-entry order for product prices.

## Quantity tiers

Always provide a tier starting at quantity 1 for an ordinary purchasable product. Then add thresholds, such as:

| Minimum quantity | Unit price |
| --- | ---: |
| 1 | 22.00 |
| 5 | 19.80 |
| 10 | 17.60 |

These are unit prices for the qualifying quantity, not separate shipping fees or progressive blocks. Under this decreasing-price example, quantity 5 uses 19.80 per item for 99.00 including the fictional 10% tax, before shipping.

Isotope selects the **lowest amount among eligible tiers**, rather than blindly choosing the last threshold. Do not use increasing tier prices expecting a later threshold to force a higher unit price. Test nonstandard pricing with your developer.

The product type can allow the lowest tier to contribute to a “from” price. A “from” amount does not mean the customer receives it at quantity 1.

## Variants and prices

A type can use shared parent prices or separate variant prices. If independent prices are enabled, fill every required variant. Review a price range on the parent and the exact price after selecting a child.

## Store configurations and dates

Use rules to target a configuration, member group, date, or other supported context. Keep a fallback for customers who match none of the special entries. Test the start and end of timed offers and the site's timezone.

For currencies, check the store price factor as well as conditional prices. An unintended factor can multiply an already converted price.

## Acceptance tests

Test quantity 1, one below each threshold, the threshold itself, and one above it. Repeat for the matching and nonmatching customer group and for relevant variants. Inspect cart and order totals as well as product-list prices.
