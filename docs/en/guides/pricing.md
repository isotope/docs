# Pricing recipes

These recipes use [advanced prices](../usage/prices.md) and [rules](../setup/rules.md). They do not require an assumed coupon engine.

## A trade-customer price

**Goal:** signed-in members of a Trade customers group receive a different unit price.

1. Create the member group in Contao and assign a test member.
2. Create an enabled member-group rule matching that group.
3. Enable advanced pricing on the product type.
4. Add a first price entry with the trade rule, the intended tax class, and a quantity-1 price.
5. Add an unrestricted ordinary price entry below it, also with quantity 1.
6. Test while logged out, as a regular member, and as the trade member.

The first matching entry wins. If the ordinary entry is first, it will hide the special entry. Decide separately whether prices should be shown net or gross in the active configuration.

## A quantity discount

**Goal:** one mug costs 10.00, while five or more cost 9.00 each.

Use one matching advanced price entry with tiers at 1 → 10.00 and 5 → 9.00. Keep the amounts decreasing for this model, because the core selects the lowest eligible amount.

Test quantities 1, 4, 5, and 6. At quantity 5, expect a merchandise amount of 45.00 before any applicable tax or other charges. The discount applies to the qualifying line's units, not just the fifth item.

If a product type shows the lowest tier as a “from” price, make the quantity condition clear in your presentation.

## A timed price

**Goal:** a product uses a special price during a planned period.

Create a date-based rule with the intended interval. Put the promotional price entry before an unrestricted fallback. Test immediately before, within, and after the interval using an appropriate test setup and the site's timezone.

A date rule does not create campaign messaging. Update the page content and test the displayed price together so they do not disagree.

## A separate currency price

Create a rule for the relevant store configuration and a matching price entry. Verify the configuration's currency and price factor. If the entry is already expressed in the target amount, an additional conversion factor may multiply it again.

See [International shops](international.md) for switching behavior.

## When you need an extension

Coupon entry, single-use codes, redemption counts, automatic free gifts, and promotion stacking need an implementation that explicitly supports them. Specify how discounts interact with tax, shipping, refunds, and multiple currencies before choosing or building that integration.
