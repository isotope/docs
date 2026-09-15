# Configure tax rates

A tax rate stores a percentage, a label, and an optional condition rule. Tax classes refer to rates. The rate record itself is not assigned independently to every product.

## Create a rate

1. Open **Configuration → Tax rates**.
2. Give it a clear internal name.
3. Enter a customer-facing label.
4. Enter the percentage as a number, such as `10` for a fictional 10% example.
5. Select a rule if the rate should apply only in a particular context.
6. Save and select it in the appropriate [tax class](tax-classes.md).

A rate without a rule matches without a condition restriction. A selected rule must be enabled and its conditions must match.

## Use rules for applicability

The current source connects tax rates to the [rule builder](../rules.md). For a destination-based example, use an address condition and select whether it checks billing or shipping.

For region restrictions, review the [implementation note](../../reference/version-notes.md) about subdivision matching in this revision before relying on the condition.

Do not copy old instructions that expect country and postal-code fields directly on the tax-rate record. Create that condition in a rule and reference the rule from the rate.

The shop uses address context even before checkout, including defaults from the store configuration. Confirm what customers see before entering an address and after changing it.

## Overlapping rates

Isotope can collect multiple matching rates from a class. It does not decide that two rates are alternatives just because their names sound similar. If exactly one must apply, make their conditions mutually exclusive.

In the documented calculator, rates are calculated against the net amount. Do not assume sequential, compounded tax-on-tax calculations. Have a developer assess requirements that go beyond that model.

## Horizontal and vertical calculation

The store configuration offers two modes:

- **Horizontal** rounds calculated tax at the individual calculation stage before amounts are combined.
- **Vertical** retains precision at that stage and rounds later in the combined calculation/display process.

A small example shows why this can matter. Two separate net amounts of 0.05 at a fictional 10% each produce 0.005 tax. Rounding each to 0.01 gives 0.02 together. Combining first gives 0.01.

This illustrates rounding, not a promise about how every cart groups its lines. Test your real line quantities and tax classes. Choose a mode that agrees with your accounting and payment processing and keep it consistent.

## When changing a rate

Do not change a live percentage casually. Establish the effective date and test the intended conditions, prices, and new orders on a copy first. Retain historical order and document records. A current catalog setting is not a substitute for the tax information recorded on an earlier order.

Implementation: [tax-rate fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_tax_rate.php) and [calculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Tax/TaxCalculator.php).
