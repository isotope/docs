---
title: 'Shipping methods'
description: 'The shop configuration - order process - shipping methods.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/shipping-methods/
weight: 30
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Isotope eCommerce offers you two shipping methods in the core, with which you can cover many use cases in combination.

## You can choose between:

{{% children showhidden="false" %}}

## General information for each shipping method

## Name &amp; Type

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Shipping Type Name</td> <td>-</td> <td>Here you can assign an internal name to the shipping type. It is not displayed in the frontend.</td> </tr><tr><td>Name</td> <td>-</td> <td>Here you can assign an external name to the shipping type. It is displayed to the visitor in the frontend and can be translated via <docrobot_route name="translations">translations</docrobot_route>.</td> </tr><tr><td>Shipping type</td> <td>Flat rate shipping</td> <td>Here you select your desired shipping type. Selection options: - Flat rate
 
shipping Shipping - grouping
 
</td></tr></tbody></table>

## Shipping note

<table><thead><tr><th>Setting</th><th>Default setting</th><th>Description</th></tr></thead><tbody><tr><td>Shipping method notes</td><td>-</td><td>Here you can add a note to the shipping method. The notes can be sent in the notifications by using `##shipping_note##`. You can find more about Simple Tokens in the corresponding chapter.</td></tr></tbody></table>

## Price and weight

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Price</td> <td>-</td> <td>Here you can enter the price for this shipping method and thus, for example, pass on shipping costs to the customer. You can enter a fixed value, as well as positive or negative percentages to represent costs dependent on the cart value.</td> </tr><tr><td>Tax class</td> <td>Tax free</td> <td>Here you can select a tax class, if taxes are to be levied on the costs of the shipping method. Selection options: - Tax-free
- Divided
 
</td> </tr><tr><td>Flat rate calculation</td> <td>Flat rate</td> <td> {{< version-tag "2.6" >}} In this selection menu you can determine if the entered price is a flat rate or if it should be charged per product or per piece. Selection options: - Flat rate
- Per product
 
Per - piece
 
Per - <docrobot_route name="shipping-method-flat">weight</docrobot_route>
 
</td></tr></tbody></table>

## Configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Countries</td> <td>-</td> <td>Here you can restrict the accessibility of the respective shipping method for certain countries. If you do not select anything here, the shipping method is available for all countries.</td> </tr><tr><td>Countries/States/Regions</td> <td>-</td> <td>Here you can restrict the accessibility of the respective shipping method for certain states/regions. If you do not select anything here, the shipping method is available for all states/regions.</td> </tr><tr><td>Postal codes</td> <td>-</td> <td>Here you can restrict the accessibility of the respective shipping method for certain zip codes. If you do not enter a comma-separated list here, the shipping method will be available for all zip codes.</td> </tr><tr><td>Quantity calculation mode</td> <td>Total quantity in shopping cart</td> <td> {{< version-tag "2.3" >}} This setting refers to the following two settings "Minimum quantity" and "Maximum quantity" and controls whether the values should apply to the number of different products or to the total number of products in the shopping cart. Selection options: - Total quantity in shopping
 
cart Quantity - of different products in
 
shopping cart </td> </tr><tr><td>Minimum quantity</td> <td>0</td> <td>{{< version-tag "2.3" >}} Here you can set a minimum quantity for this shipping method. Applied, this means that the potential buyer can only use this shipping method if he has products of at least this quantity in his shopping cart.</td> </tr><tr><td>Maximum quantity</td> <td>0</td> <td>{{< version-tag "2.3" >}} Here you can set a maximum quantity for this shipping method. Applied, this means that the potential buyer can only use this shipping method when he has products of at most this number in his shopping cart.</td> </tr><tr><td>Minimum subtotal</td> <td>0.00</td> <td>Here you can set a minimum subtotal for this shipping method. This means that the potential buyer can only use this shipping method when he has products of at least this value in his shopping cart.</td> </tr><tr><td>Maximum subtotal</td> <td>0.00</td> <td>Here you can set a maximum subtotal for this shipping method. Applied, this means that the potential buyer can only use this shipping method when he has products with a maximum value of this amount in his shopping cart.</td> </tr><tr><td>Minimum weight</td> <td>-</td> <td>This setting comes into play when the <docrobot_route name="product-types">product type</docrobot_route> allows the weight input attribute. Once Isotope knows how heavy a product is, the shipping method can be restricted to that weight.</td> </tr><tr><td>Maximum weight</td> <td>-</td> <td>This setting is used if the <docrobot_route name="product-types">product type</docrobot_route> allows the attribute for weight input. Once Isotope knows how heavy a product is, the shipping method can be restricted to weight.</td> </tr><tr><td>Product Types</td> <td>-</td> <td>Here you can limit the accessibility of the shipping method for certain product types. If you do not select anything here, the shipping method will be available for all product types.</td> </tr><tr><td>Product type conditions</td> <td>Only allow for the following product types in the shopping cart</td> <td>Select how the product type filter should be applied. Selection options: - Only
 
allow if the following product types are in the shopping cart - Only allow if all of the following product types
 
are in the shopping cart - Allow if any of the following product types are in the shopping cart
- Calculate price for these product types
 
</td> </tr><tr><td>Configurations</td> <td>-</td> <td>{{< version-tag "2.2" >}} Here you can restrict the accessibility of the respective shipping method for certain shop configurations. If you do not select anything here, the shipping method will be available for all shop configurations.</td></tr></tbody></table>

## Expert settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Show for guests only</td> <td>-</td> <td>Here you can determine whether this dispatch type should only be available for guests.</td> </tr><tr><td>Protect module</td> <td>-</td> <td>In contrast to "Show for guests only", here you can restrict the dispatch type for certain member groups.</td></tr></tbody></table>

## Release

<table><thead><tr><th>Setting</th><th>Default setting</th><th>Description</th></tr></thead><tbody><tr><td>Active</td><td>-</td><td>Here you can activate or deactivate the shipping method. {{% notice info %}} Each shipping method can be activated and deactivated. However, it is **not** yet automatically available in the checkout module, but must be activated there additionally. See also the corresponding chapter. 
{{% /notice %}}
</td></tr></tbody></table>
