---
menuTitle: 'Shipping grouping'
title: 'Shipping type Shipping grouping'
description: 'The shop configuration - order process - shipping methods - shipping grouping.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/shipping-methods/shipping-method-group/
weight: 110
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The shipping type "Shipping Grouping" groups or combines multiple flat rate shipping methods[and can](/de/backend-konfiguration-shop-bestellablauf-versandarten-pauschalversand/) become a very powerful tool. Examples that can be achieved with this shipping method:

- Up to shopping cart amount € 100.- the shipping costs € xx.xx and from € 100.- it costs € xx.xx.
- To Germany the shipping costs € xx.xx, to Switzerland € xx.xx
- etc.

## Configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Shipping types</td> <td>-</td> <td>All other shipping methods are listed here. Here you can determine from which shipping types you want to make a grouping. Furthermore you can sort them, which can have an influence on "group calculation". {{% notice info %}}
You can therefore also group shipping types and thus configure arbitrarily complex and powerful shipping types.
{{% /notice %}}
</td></tr></tbody></table>

## Price limit and tax class applicability

<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Default setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Group calculation</td>
        <td>Price of first available method</td>
        <td>Here you can determine the price calculation method.
        <ul>
        <li><strong>Price of the first available method</strong> In this method, Isotope eCommerce will go through the selected shipping methods according to the sort order and take the price of the first available shipping method.</li>
        <li><strong>Lowest price of the available shipping methods</strong> In this method, Isotope eCommerce determines the lowest priced of all applicable selected shipping methods.</li>
        <li><strong>Highest price of available shipping methods</strong> In this method, Isotope eCommerce determines the most expensive of all applicable shipping methods selected.</li>
        <li><strong>Total price of available shipping methods</strong> In this method, Isotope eCommerce determines the sum of all applicable shipping methods selected.</li>
        </ul>
        </td>
    </tr>
    </tbody>
</table>

## Examples

### Parcel shipping based on weight

The prerequisite for this is that you record the weight of each of your products. In the shipping types, you first create a separate entry of the type flat-rate shipping for each parcel size:
- DHL Paket 2 kg (price = 4.99 € | weight from 0 kg to 1.999 kg) 
- DHL Paket 5 kg (price = 5.99 € | weight from 2 kg to 4.999 kg) 
- DHL Paket 10 kg (price = 8.49 € | weight from 5 kg to 9.999 kg)

To group the corresponding shipping types for the calculation, use a shipping group method.
Here you add all previously created shipping methods and select "Price of the first available method" in "Group calculation".

Now add this shipping group in the checkout module. This will calculate the shipping costs based on the weight. Currently, the problem would be that a shopping cart weighing more than 10 kg would not have a shipping method and thus could not be shipped.
