---
title: 'Base prices'
description: 'The shop configuration - basic prices.'
aliases:
    - /en/backend-configuration/store-configuration/products/base-price/
weight: 100
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

You can set a basic price (price per unit of measure) for a product. In the frontend, the basic price is then displayed in addition to the price (CHF 0.25 per 100 g).

In the first step, you define the basic price.

<table><thead><tr><th>Setting</th> <th>Standard setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Name</td> <td>-</td> <td>Assign a unique name to the base price, this will only be used in the backend.</td> </tr><tr><td>Base Amount</td> <td>-</td> <td>The base amount is the conversion factor for the base price, this should be identical to the number in the name. e.g. "100 g" results in a base amount of 100.</td> </tr><tr><td>Designation</td> <td>%s</td> <td>Here you can enter the label for the basic price. e.g. "%s per 100 g". `%s` is a placeholder and displays the calculated base price including the currency selected in the <docrobot_route name="configuration">shop configuration</docrobot_route>.</td></tr></tbody></table>

After that you have to create a [product type](/de/backend-konfiguration-shop-Produkttypen/) with the attribute `Grundpreis-Menge [baseprice]`.

![Product type with the attribute basic price quantity](attribut_grundpreis_menge.png)

When creating a [product](/de/backend-produkte/) you now have two fields available.

![Create a product with basic price](produkt_anlegen.png)

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Base price quantity</td> <td>-</td> <td>This is the total quantity of the product. This information must be entered in the same unit of measure as the base amount for the basic price. In our example in grams. e.g. basic price quantity 1000 and basic amount 100 result in CHF 0.50 per 100 g at a sales price of CHF 5.00.</td> </tr><tr><td>Selection</td> <td>-</td> <td>Here you can select the desired basic price.</td></tr></tbody></table>
