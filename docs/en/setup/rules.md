# Rules and conditions

A rule is a named, reusable test of the current shopping situation. Prices, taxes, shipping methods, and payment methods can refer to it.

For example, “Domestic delivery” can test the shipping country. A shipping method can use that rule to decide whether it is available. The rule does not itself ship anything or set a price.

## Create a rule

1. Open **Isotope eCommerce → Rules**.
2. Give the rule a meaningful name.
3. Open its conditions and add the required checks.
4. Choose the operator for each check and fill its values.
5. Enable the rule.
6. Select it on the price, tax rate, or method that should use it.
7. Test a matching and nonmatching case.

Creating a rule without attaching it to a consumer has no effect on that consumer.

## How conditions combine

The documented matcher requires **every condition** in a rule to match. Think of multiple conditions as “and”. A rule with a shipping-country condition and a member-group condition requires both.

Where a condition supports a list and an operator such as “one of”, that operator controls the values within that condition. Do not assume an arbitrary nested “or” rule builder.

An enabled rule with no conditions matches. A disabled or missing rule does not match. Invalid conditions fail the match. This matters if you disable a rule attached to your only payment method.

## Core condition families

| Condition | Typical use |
| --- | --- |
| Store configuration | A price for one configuration |
| Currency | A choice restricted to a currency |
| Date or time | A scheduled offer |
| Customer logged in | A members-only choice |
| Member groups | A trade-customer price |
| Cart address | Country, region, or postal-code restrictions |
| Cart quantity | Sum of product item quantities |
| Cart products | Number of product lines |
| Cart total | A condition based on the calculated cart total |

The cart-total condition is not named “merchandise subtotal” and should not be treated as one. Shipping fees and recalculation can affect threshold behavior. Test either side of a boundary and after changing methods.

## Example: domestic shipping

Create an address condition using the shipping address and your intended country. Attach it to a flat shipping method. A customer using a different shipping country should not see that method. If you also restrict allowed shipping countries in the store configuration, check both layers.

## Rules are not automatically coupons

The core rule records in this version describe conditions. They do not provide the old promotion/coupon workflow simply because the backend section is called Rules. Use conditional [advanced prices](../usage/prices.md) for supported price changes. Coupon codes, redemption limits, and promotion stacking require a compatible implementation.

## Priority and price order

A numeric rule priority exists, but do not infer that it overrides every consumer's selection logic. The core product price factory takes the **first matching advanced price entry**. Put specific entries before an unrestricted fallback and test the actual result.

Implementation: [RuleMatcher](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder/RuleMatcher.php).
