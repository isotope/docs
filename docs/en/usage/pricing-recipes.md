# Pricing recipes

These recipes extend the [Trail T-shirt example](../concepts/example-shop.md). All prices include the fictional 10% tax. Before daily editing, ask your shop administrator to enable advanced pricing on Clothing and prepare the required [rules](../setup/rules.md). See [Prices](prices.md) for editing basics.

## A trade-customer price

**Goal:** signed-in members of a Trade customers group receive a different unit price.

1. Confirm the Trade customers member group and its matching rule are available.
2. Open the Trail T-shirt’s advanced prices.
3. Add a first entry with the trade rule, Standard goods tax class, and quantity-1 price 17.60.
4. Add an unrestricted ordinary entry below it with quantity-1 price 22.00 and the same tax class.
5. Test while logged out, as a regular member, and as the trade member.

The first matching entry wins. If the ordinary entry is first, it will hide the special entry. Decide separately whether prices should be shown net or gross in the active configuration.

## A quantity discount

**Goal:** one Trail T-shirt costs 22.00, while five or more cost 19.80 each.

Use one matching advanced price entry with tiers at 1 → 22.00 and 5 → 19.80. Keep the amounts decreasing for this model, because Isotope selects the lowest eligible amount.

Test quantities 1, 4, 5, and 6. At quantity 5, expect a merchandise amount of 99.00 including 9.00 tax, before shipping or other charges. The discount applies to the qualifying line's units, not just the fifth item.

If a product type shows the lowest tier as a “from” price, make the quantity condition clear in your presentation.

## A timed price

**Goal:** a product uses a special price during a planned period.

Create a date-based rule with the intended interval. Put the promotional price entry before an unrestricted fallback. Test immediately before, within, and after the interval using an appropriate test setup and the site's timezone.

A date rule does not create campaign messaging. Update the page content and test the displayed price together so they do not disagree.

## A separate currency price

Create a rule for the relevant store configuration and a matching price entry. Verify the configuration's currency and price factor. If the entry is already expressed in the target amount, an additional conversion factor may multiply it again.

See [International shops](../setup/general/international.md) for switching behavior.

## When you need an extension

Coupon entry, single-use codes, redemption counts, automatic free gifts, and promotion stacking need an implementation that explicitly supports them. Specify how discounts interact with tax, shipping, refunds, and multiple currencies before choosing or building that integration.
