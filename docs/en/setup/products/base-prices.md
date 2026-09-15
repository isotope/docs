# Base prices and comparison quantities

A base price is a comparison price for a standard amount. It helps a customer compare differently sized packages.

For example, Trail Supply’s 250 ml garment wash costing 6.60 has a comparison price of 2.64 per 100 ml. A 500 ml bottle costing 11.00 has a comparison price of 2.20 per 100 ml. The larger bottle has the lower price per milliliter even though its package price is higher.

This is different from a net price, a wholesale price, or a quantity discount. The customer still buys the package at its package price.

## The calculation

```text
base price = product unit price / product amount × reference amount
6.60 / 250 × 100 = 2.64
```

Use the same measurement unit for both amounts. If the reference amount is 100 milliliters, a 1.5 liter bottle must be represented as 1500 milliliters for this calculation.

## Set it up

1. Create a definition under **Configuration → Base prices**.
2. Give it a recognizable name, such as “Per 100 milliliters”.
3. Enter reference amount `100`.
4. Use a label such as `%s per 100 ml`. The `%s` position receives the formatted comparison price.
5. Enable the base-price field on the product type. On the product, select the reference definition and enter the package amount, such as `250`.
6. Verify that the selected product template renders the comparison price.

If the base-price field is missing, check the selected product type’s enabled attributes.

## Check a sample

Use a package with an easy calculation and compare the displayed result manually. Test a second package size, variants with different amounts, and any member or quantity prices. A comparison price should follow the actual unit price used for that context.

Decide which products need comparison pricing with the person responsible for your shop's product information. This chapter explains the mechanism, not jurisdiction-specific display requirements.
