# Prices and taxes explained

A price is more than a number. You need to know its currency, whether it contains tax, and whether additional charges apply.

All percentages and amounts below are fictional teaching examples. They explain Isotope's calculation model and do not specify the tax treatment for your business.

## Net and gross

**Net** means before tax. **Gross** means including tax.

With a fictional 10% rate:

| Calculation | Amount |
| --- | ---: |
| Net price | 100.00 |
| Tax, 10% of 100.00 | 10.00 |
| Gross price | 110.00 |

To extract tax from 110.00, divide by 1.10. Do not subtract 10% of 110.00. That would remove 11.00 and give the wrong net price.

## What a tax rate is

A **tax rate** stores a percentage and can refer to a rule that decides when it applies. Its backend name helps staff identify it. Its label explains it to customers.

For example, a fictional “Domestic standard 10%” rate might apply when the shipping address is in your domestic delivery area. Another rate could apply for a different destination. The appropriate address and conditions come from your business's tax setup.

Rates exist separately from products so you can reuse the same treatment without entering percentages on every product.

## What a tax class is

A **tax class** connects a product price to its tax treatment. You might have “Standard goods”, “Reduced goods”, and a separate class for delivery charges.

In Isotope a class can specify:

- The rate already **included** in the number you enter.
- Other rates to **apply** when their rules match.

The class answers “how should this price be interpreted and taxed?” The rate answers “what percentage applies under these conditions?” A product type answers an entirely different question about product fields and behavior.

## Entering net prices

Suppose you enter 100.00 and intend that number to exclude tax. Leave the class's included rate empty and add the fictional 10% rate under **Apply tax rates**. When it matches, the resulting gross price is 110.00.

## Entering gross prices

Suppose you enter 110.00 and intend it to contain the domestic 10% rate. Select that rate as the class's **Tax rate included with product price**.

Isotope extracts the included tax to establish the net amount. When the included rate's rule matches, that rate also applies. You should not select the same rate again as an additional applied rate.

If the included rate stops matching, its tax is removed. If a different 20% rate then applies, the same 100.00 net becomes 120.00 gross. Changing the address can therefore change the displayed price.

## Display choice is a separate setting

The store configuration offers Net, Gross, and Fixed price display. The examples above use Gross. That choice does not change what you meant when entering a tax-inclusive catalog price. The tax class still needs to describe the entered number correctly.

Before the customer provides an address, the shop has default address context. Checkout can supply more specific information. Test both browsing and checkout totals, especially when you use destination rules.

## Fixed display

Fixed display keeps the entered customer-facing price and calculates applicable taxes as included in that amount. For an entered 110.00, a fictional 10% rate gives 100.00 net. At 20%, the same 110.00 gives approximately 91.67 net. Your net proceeds change while the displayed product amount stays fixed.

Use Fixed only when that is your intended pricing policy. It differs from Gross mode, which preserves the net basis in the destination example above. Currency factors and other price rules can still affect the starting amount.

## Shipping, fees, and rounding

Shipping and payment charges can have their own tax classes. Product tax configuration does not automatically settle the treatment of every charge.

Rounding also matters. Rounding tax for each line can differ slightly from rounding combined tax at the end. Isotope offers horizontal and vertical calculation modes. See [Tax rates](../setup/checkout/tax-rates.md) for the practical implications.

Next: [Configure tax classes](../setup/checkout/tax-classes.md), then [test a tax setup](../guides/tax-example.md).

Implementation: [TaxCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Tax/TaxCalculator.php).
