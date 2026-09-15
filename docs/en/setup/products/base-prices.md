# Base prices and comparison quantities

A base price is a comparison price for a standard amount. It helps a customer compare differently sized packages.

For example, a 250 g bag costing 6.00 has a comparison price of 2.40 per 100 g. A 500 g bag costing 10.00 has a comparison price of 2.00 per 100 g. The larger bag has the lower price per gram even though its package price is higher.

This is different from a net price, a wholesale price, or a quantity discount. The customer still buys the package at its package price.

## The calculation

```text
base price = product unit price / product amount × reference amount
6.00 / 250 × 100 = 2.40
```

Use the same measurement unit for both amounts. If the reference amount is 100 grams, a 1.5 kg package must be represented as 1500 grams for this calculation.

## Set it up

1. Create a definition under **Configuration → Base prices**.
2. Give it a recognizable name, such as “Per 100 grams”.
3. Enter reference amount `100`.
4. Use a label such as `%s per 100 g`. The `%s` position receives the formatted comparison price.
5. Enable the base-price field on the product type. On the product, select the reference definition and enter the package amount, such as `250`.
6. Verify that the selected product template renders the comparison price.

Isotope 3 provides the product base-price field directly. The upgrade notes remove the former dedicated BasePrice attribute class, not the comparison-price feature. If the field is missing, check the selected product type's enabled attributes.

## Check a sample

Use a package with an easy calculation and compare the displayed result manually. Test a second package size, variants with different amounts, and any member or quantity prices. A comparison price should follow the actual unit price used for that context.

Decide which products need comparison pricing with the person responsible for your shop's product information. This chapter explains the mechanism, not jurisdiction-specific display requirements.

Implementation: [base-price formatter](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceFormatter.php).
