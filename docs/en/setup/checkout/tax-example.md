# Worked example: domestic and destination taxes

This exercise shows why tax classes and tax rates are separate. It uses fictional rates and two destinations called A and B. Substitute your chosen test countries in the address rules. Do not copy these percentages into a live tax policy.

Continue with Trail Supply’s T-shirt from [Your first shop](../../getting-started/first-shop.md). Use a test copy because changing a shared tax class affects every price using it.

**Outcome:** the T-shirt entered at 22.00 including 10% tax has a net basis of 20.00. Its gross amount becomes 24.00 when a different 20% destination tax applies.

## 1. Use gross display

Choose **Gross** in the store configuration and keep the currency factor at `1`. Fixed price display has different behavior and is not used in this exercise.

Allow both test destinations and set A as the default shipping country. Use a physical product so you can enter a shipping address.

## 2. Create two rules

Create and enable a rule for shipping country A and another for shipping country B. Each uses a cart-address condition checking the shipping address.

These rules must be mutually exclusive for this exercise. Test only the country condition initially, without region or postal-code restrictions.

## 3. Prepare the tax rates

| Rate name | Percentage | Rule |
| --- | ---: | --- |
| Example standard 10% | 10 | Shipping country A |
| Example destination 20% | 20 | Shipping country B |

Edit the existing Example standard 10% rate and attach the rule for A. Create Example destination 20% with the rule for B. Give each a customer-readable label and save.

## 4. Update the class

Edit the “Standard goods” class on your test copy. Set the 10% A rate as the included rate. Select only the 20% B rate in **Apply tax rates**.

Do not select A a second time in the additional list. Its included-rate path already applies it when its rule matches.

## 5. Assign the product price

Keep the Trail T-shirt price at `22.00` and select Standard goods. Use one item and remove other fees for the simplest calculation. If your shipping method adds a charge, compare the product line separately.

## 6. Check the expected results

| Context | Entered price | Net basis | Applicable tax | Gross product price |
| --- | ---: | ---: | ---: | ---: |
| Address A | 22.00 | 20.00 | 2.00 | 22.00 |
| Address B | 22.00 | 20.00 | 4.00 | 24.00 |
| Neither rule matches | 22.00 | 20.00 | 0.00 | 20.00 |

The last row illustrates software behavior when no rate matches. It is not advice to exempt other destinations.

The calculation starts with `22 / 1.10 = 20`. It then applies the matching rate to 20. The price entered in the product remains 22.00.

## 7. Test before and after addresses

Check the product before entering an address, then complete checkout with A. Change to B and inspect the recalculated product line. Confirm that you changed the **shipping** address, because that is what these rules check.

Repeat with net display if you want to see the same setup present the 20.00 net amount. The included tax treatment remains defined by the class.

## 8. Add complexity one layer at a time

Test a second tax class, taxed shipping, multiple quantities, and rounding only after the simple example works. Keep a small expected-results table for the shop's real configurations and rerun it after tax or pricing changes.

Related: [Tax classes](tax-classes.md), [Tax rates](tax-rates.md), [Price display](../../concepts/prices-and-taxes.md).
