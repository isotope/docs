---
title: Configuration
description: 'The shop configuration - General settings - Configuration.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/configuration/
weight: 50
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Name

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Name of the shop configuration</td> <td>-</td> <td>Unique name which is only used in the backend.</td> </tr><tr><td>Name</td> <td>-</td> <td>Is used for the output in the frontend, e.g. for the <docrobot_route name="store-config-switcher">shop configuration changer</docrobot_route>.</td> </tr><tr><td>Default configuration</td> <td>-</td> <td>If multiple configurations exist, one of these configurations must be activated as the default configuration.</td></tr></tbody></table>

## Address

Here you enter the legally compliant address of the shop operator.

## Bank data

Here you enter the bank data of the shop operator.

## Checkout

Here you can select the available fields for the billing and shipping address when paying.

Available for selection are:

- Disabled
- Activated (Not mandatory)
- Enabled (Mandatory)

![Billing and shipping address fields](kasse.png)

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Default Invoicing Country</td> <td>-</td> <td>Define here which country should be preselected when creating a billing address, or leave the field empty if no preselection is desired.</td> </tr><tr><td>Default Shipping Country</td> <td>-</td> <td>Define here which country should be preselected when creating a shipping address, or leave the field empty if no preselection is desired.</td> </tr><tr><td>Billing countries</td> <td>-</td> <td>Here you can define which countries are available for the billing address in the order process.</td> </tr><tr><td>Shipping countries</td> <td>-</td> <td>Here you can determine which countries are available for the shipping address in the order process.</td> </tr><tr><td>Restrict member countries</td> <td>-</td> <td>Here you can restrict the registration or the administration mask of personal data (on the part of Contao) to the countries that have been entered as billing address or shipping address at `Rechnungs-Länder` and `Versand-Länder`.</td> </tr><tr><td>Validation of the VAT number.</td> <td>-</td> <td>{{< version-tag "2.3" >}} If you have activated one or more services here, the VAT address field will be validated.</td></tr></tbody></table>

## Prices

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Price display</td> <td>Gross (recommended)</td> <td> {{< version-tag "2.3" >}}Select here how the price display should be in your shop. Available are: - **Net**Displays the net price to all customers. Taxes that are included in the product price<docrobot_route name="tax-rates">(tax rate configuration</docrobot_route>) will be deducted.
- **Gross (recommended)**Displays the gross price to all customers. Applicable taxes are added to the displayed product price.
- **Fix**The product price is always displayed as set in the product settings. Taxes are always calculated as "included". This means that the shop owner's earnings will vary depending on the tax rates applied.
- **Legacy**The price is displayed smaller than 2.3 as in Isotope eCommerce. The gross price is displayed once a tax is included and applied. Additional taxes will only be displayed as a surcharge.

</td> </tr><tr><td>Price formatting</td> <td>-</td> <td>Define here how amounts are displayed, i.e. whether to use a comma or a period for decimals and how to group thousands.</td> </tr><tr><td>Rounding precision</td> <td>2</td> <td>Define the allowed decimal precision for amounts (e.g. price, VAT, total). {{% notice warning %}}
To ensure compatibility with all payment modules, we recommend that you use a value between 0 and 2.

{{% /notice %}}
</td> </tr><tr><td>Rounding surcharge</td> <td>0.01</td> <td>Define here which is the smallest declared unit in the respective currency. The Swiss franc, for example, only allows a rounding surcharge of 0.05.</td></tr></tbody></table>

## Currency formatting

{{% notice info %}}
When formatting the currency, pay attentionto the country-specific differences.
{{% /notice %}}

 <table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Currency</td> <td>-</td> <td>Here you can select the currency for your shop.</td> </tr><tr><td>Position of the currency label/symbol</td> <td>Left of the price</td> <td>Define here on which side of the price the currency is placed. Example for "Left of the price" CHF 1'000.00 or for "Right of the price" 1.000,00 EURO.</td> </tr><tr><td>Use currency symbol</td> <td>-</td> <td>Define here whether, if available, a currency symbol should be used. e. g. E.g. € for Euro or $ for Dollar.</td> </tr><tr><td>Insert space</td> <td>-</td> <td>Here you can insert a space between the price and the currency symbol.</td></tr></tbody></table>

## Currency conversion

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Calculation factor</td> <td>1</td> <td>Here you can specify a factor for the currency conversion.</td> </tr><tr><td>Calculation mode</td> <td>Multiply</td> <td>Here you can determine if the price should be divided or multiplied with the factor.</td> </tr><tr><td>Automatic currency converter</td> <td>-</td> <td>Here you can activate an automatic currency calculator.</td> </tr><tr><td>Origin currency</td> <td>-</td> <td>Here you can determine the currency for the calculation.</td> </tr><tr><td>Provider of the currency data</td> <td>ecb.int (European Central Bank)</td> <td>Here you can choose a provider of online currency data. Choice of options: - ecb.int
- admin.ch

</td></tr></tbody></table>

## Orders

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Purchase Order Number Prefix</td> <td>-</td> <td>Here you can add a prefix to the automatically incrementing order number.</td> </tr><tr><td>Order number length</td> <td>4</td> <td>Here you can define the minimum length of the order number. {{% notice info %}}
 `Bestellnummer-Präfix` is not counted.
{{% /notice %}}</td> </tr><tr><td>Status for new orders</td> <td>-</td> <td>Here you can set the <docrobot_route name="order-status">status</docrobot_route> for new orders. {{% notice warning %}}
This information can be overwritten by a <docrobot_route name="payment-methods">payment method</docrobot_route>.
{{% /notice %}}
</td> </tr><tr><td>Order status in case of an error</td> <td>-</td> <td>Here you can set the <docrobot_route name="order-status">status</docrobot_route> for failed orders.</td> </tr><tr><td>Module for backend view</td> <td>-</td> <td>Select an order details module to be used to display orders in the backend.</td></tr></tbody></table>

## Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Templates folder</td> <td>-</td> <td>If the checkbox is activated, a specific folder in the templates folder can be selected. The templates in this folder will then be automatically preferred by the system if their names are unchanged.</td> </tr><tr><td>Minimum Subtotal</td> <td>0.00</td> <td>If the value you enter in the shopping cart is not reached, the order cannot be completed. {{% notice info %}}
With the default value `0.00` this function is deactivated.
{{% /notice %}}
</td></tr></tbody></table>

## Products

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Duration for which a product is displayed as "New</td> <td>- days</td> <td>Here you can define how long you want to highlight a product as new in your shop. {{% notice info %}}
For the selected period of time, a CSS class `new` will be added to the product.
{{% /notice %}}
 Selection options: - Minutes
- Hours
- Days
- Weeks
- Months
- Years

</td></tr></tbody></table>

## Analytics

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Enable Google Analytics</td> <td>-</td> <td>Here you can enable tracking with Google Analytics.</td> </tr><tr><td>Account</td> <td>-</td> <td>Here you need to enter your Google Analytics account number with the format `UA-XXXXXXXX-X`.</td> </tr><tr><td>Track members</td> <td>-</td> <td>Here you can use <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> to track members (e.g. `##firstname##`). {{% notice warning %}}
Of course, you need to request the authority to track from the members in advance.
{{% /notice %}}
</td></tr></tbody></table>
