# Worked example: domestic and destination taxes

This exercise shows why tax classes and tax rates are separate. It uses fictional rates and two destinations called A and B. Substitute your chosen test countries in the address rules. Do not copy these percentages into a live tax policy.

**Outcome:** a product entered at 110.00 including 10% tax has a net basis of 100.00. Its gross amount becomes 120.00 when a different 20% destination tax applies.

## 1. Use gross display

Choose **Gross** in the store configuration and keep the currency factor at `1`. Fixed price display has different behavior and is not used in this exercise.

Allow both test destinations and set A as the default shipping country. Use a physical product so you can enter a shipping address.

## 2. Create two rules

Create and enable a rule for shipping country A and another for shipping country B. Each uses a cart-address condition checking the shipping address.

These rules must be mutually exclusive for this exercise. Test only the country condition initially, without region or postal-code restrictions.

## 3. Create two tax rates

| Rate name | Percentage | Rule |
| --- | ---: | --- |
| Example A standard | 10 | Shipping country A |
| Example B standard | 20 | Shipping country B |

Give each a customer-readable label. Save both.

## 4. Create the class

Create “Example goods, A tax included”. Set the 10% A rate as the included rate. Select only the 20% B rate in **Apply tax rates**.

Do not select A a second time in the additional list. Its included-rate path already applies it when its rule matches.

## 5. Assign the product price

Create a product price of `110.00` and select the new class. Use one item and remove other fees for the simplest calculation. If your shipping method adds a charge, compare the product line separately.

## 6. Check the expected results

| Context | Entered price | Net basis | Applicable tax | Gross product price |
| --- | ---: | ---: | ---: | ---: |
| Address A | 110.00 | 100.00 | 10.00 | 110.00 |
| Address B | 110.00 | 100.00 | 20.00 | 120.00 |
| Neither rule matches | 110.00 | 100.00 | 0.00 | 100.00 |

The last row illustrates software behavior when no rate matches. It is not advice to exempt other destinations.

The calculation starts with `110 / 1.10 = 100`. It then applies the matching rate to 100. The price entered in the product remains 110.00.

## 7. Test before and after addresses

Check the product before entering an address, then complete checkout with A. Change to B and inspect the recalculated product line. Confirm that you changed the **shipping** address, because that is what these rules check.

Repeat with net display if you want to see the same setup present the 100.00 net amount. The included tax treatment remains defined by the class.

## 8. Add complexity one layer at a time

Test a second tax class, taxed shipping, multiple quantities, and rounding only after the simple example works. Keep a small expected-results table for the shop's real configurations and rerun it after tax or pricing changes.

Related: [Tax classes](../setup/checkout/tax-classes.md), [Tax rates](../setup/checkout/tax-rates.md), [Price display](../concepts/prices-and-taxes.md).
