---
title: 'Tax brackets'
description: 'The shop configuration - order process - tax classes.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/tax-classes/
weight: 20
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Name

<table><thead><tr><th>Setting</th><th>Default setting</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>-</td><td>Create a name for the tax class that describes what it is used for.</td></tr><tr><td>Default</td><td>-</td><td>Click here if this is the default tax class.</td></tr></tbody></table>

## Tax Rates

<table><thead><tr><th>Setting</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td>Tax class included in product price</td><td>-</td><td>Select whether product prices with this tax class include a tax rate. This tax rate will be subtracted from the product price if it does not match.</td></tr><tr><td>Include label</td><td>-</td><td>A label for orders to display deducted taxes (if included taxes do not match). If this field is blank, the default tax rate caption will be displayed.</td></tr><tr><td>Add Tax Rates</td><td>-</td><td>Add these tax rates to products with these tax classes.</td></tr><tr><td>Use Rounding Surcharge</td><td>-</td><td>Use rounding surcharge of the shop configuration.</td></tr><tr><td>Non-negative</td><td>-</td><td>Prevents negative amounts for this tax (negative number is rounded up to 0.00).</td></tr></tbody></table>

## Example 1:

For sales to end consumers in Germany, the gross price is displayed and the included VAT is only shown.

![End user](steuerklasse_inklusive_mwst.png)

## Example 2:

For sales to business customers in Germany, the net price is displayed and the normal VAT is added.

![Commercial customers](steuerklasse_exklusive_mwst.png)
