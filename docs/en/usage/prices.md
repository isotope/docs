# Product prices and quantity tiers

Start with a simple price unless the product genuinely needs conditional pricing. Decide how tax is included before entering amounts. See [Prices and taxes](../concepts/prices-and-taxes.md).

## Simple price

A simple price combines an amount and a tax class. The active store configuration supplies currency context and price display behavior.

Check the displayed result after saving. An entered 110.00 with included tax is different from 110.00 before tax, even though the number in the form looks identical.

## Advanced prices

Enable advanced pricing on the product type when you need multiple price entries or quantity tiers. Each entry can contain a tax class, a rule, and a set of tier prices.

The core uses the **first advanced price entry whose rule matches**. An entry without a rule matches without restriction. Put specific entries first and an unrestricted fallback last.

For example:

| Entry order | Rule | Unit price from quantity 1 |
| --- | --- | ---: |
| 1 | Member belongs to Trade customers | 8.00 |
| 2 | No rule | 10.00 |

If the unrestricted entry comes first, it prevents the trade entry from being selected. A rule's numeric priority does not replace the price-entry order in this factory.

## Quantity tiers

Always provide a tier starting at quantity 1 for an ordinary purchasable product. Then add thresholds, such as:

| Minimum quantity | Unit price |
| --- | ---: |
| 1 | 10.00 |
| 5 | 9.00 |
| 10 | 8.00 |

These are unit prices for the qualifying quantity, not separate shipping fees or progressive blocks. Under this decreasing-price example, quantity 5 uses 9.00 per item for 45.00 before applicable tax.

The documented calculator selects the **lowest amount among eligible tiers**, rather than blindly choosing the last threshold. Do not use increasing tier prices expecting a later threshold to force a higher unit price. Test nonstandard pricing with your developer.

The product type can allow the lowest tier to contribute to a “from” price. A “from” amount does not mean the customer receives it at quantity 1.

## Variants and prices

A type can use shared parent prices or separate variant prices. If independent prices are enabled, fill every required variant. Review a price range on the parent and the exact price after selecting a child.

## Store configurations and dates

Use rules to target a configuration, member group, date, or other supported context. Keep a fallback for customers who match none of the special entries. Test the start and end of timed offers and the site's timezone.

For currencies, check the store price factor as well as conditional prices. An unintended factor can multiply an already converted price.

## Acceptance tests

Test quantity 1, one below each threshold, the threshold itself, and one above it. Repeat for the matching and nonmatching customer group and for relevant variants. Inspect cart and order totals as well as product-list prices.

Sources: [DefaultPriceFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Product/DefaultPriceFactory.php), [PriceCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceCalculator.php).
