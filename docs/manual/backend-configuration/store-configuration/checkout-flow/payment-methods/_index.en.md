---
title: 'Payment methods'
description: 'The shop configuration - order process - payment methods.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/
weight: 40
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Isotope eCommerce offers you a variety of payment methods for a wide range of vendors.

{{% notice info %}}
Additional payment methods can be found on the [Isotope eCommerce marketplace](https://www.isotopeecommerce.org/en/marketplace.html).
{{% /notice %}}


## You can choose from:

{{% children %}}

{{% notice warning %}}
Note that each payment module is responsible for how the payment is made and what happens to the order afterwards. Therefore, even though an input field is named the same as another payment type, the behavior may not be identical. Therefore it is important that the documentation is as complete as possible. The community is therefore also dependent on your contribution!
{{% /notice %}}

## General information for each payment type

## Name &amp; Type

|    Setting     | Default Setting |                                                                      Description                                                                      |
|----------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name           | -               | Here you can assign an internal name to the payment type. It is not displayed in the frontend.                                                        |
| Name           | -               | Here you can assign an external name to the payment type. It will be displayed to the visitor in the frontend and can be translated via translations. |
| Payment module | -               | Here you select your desired payment method.                                                                                                          |

## Order note

| Setting | Default setting |                                                                                        Description                                                                                         |
|---------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notes   | -               | Here you can add a note to the payment type. The notes can be sent in the notifications by using `##payment_note##`. You can find more about Simple Tokens in the corresponding chapter. |

## General settings

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
        <td>Status for new orders</td>
        <td>-</td>
        <td>In this dropdown menu you can select the status the order should have after payment. More about the order statuses can be found in the
            <docrobot_route name="order-status">corresponding chapter</docrobot_route>.
        </td>
    </tr>
    <tr>
        <td>Quantity calculation mode</td>
        <td>Total quantity in shopping cart</td>
        <td> {{< version-tag "2.3" >}} This setting refers to the following two settings "Minimum quantity" and "Maximum quantity" and regulates whether the values should apply to the number of different products or the total number of products in the shopping cart. Selection options:
        - Total quantity in shopping cart
        - Quantity of different products inshopping cart
        </td>
    </tr>
    <tr>
        <td>Minimum quantity</td>
        <td>0</td>
        <td>{{< version-tag "2.3" >}} Here you can set a minimum quantity for this payment method. Applied, this means that the potential buyer can only use this payment option if he has products of at least this quantity in his shopping cart.</td>
    </tr>
    <tr>
        <td>Maximum quantity</td>
        <td>0</td>
        <td>{{< version-tag "2.3" >}} Here you can set a maximum quantity for this payment method. Applied, this means that the potential buyer can only use this payment option when he has products of at most this quantity in his shopping cart.</td>
    </tr>
    <tr>
        <td>Minimum order value</td>
        <td>0.00</td>
        <td>Here you can set a minimum order value for this payment method. Applied, this means that the potential buyer can only use this payment option when he has products of at least this value in his shopping cart.</td>
    </tr>
    <tr>
        <td>Maximum order value</td>
        <td>0.00</td>
        <td>{{< version-tag "2.3" >}} Here you can set a maximum order value for this payment method. This means that the potential buyer can only use this payment option if he has products with a maximum value of this value in his shopping cart.</td>
    </tr>
    <tr>
        <td>Active countries</td>
        <td>-</td>
        <td>Here you can limit the accessibility of the payment method for certain countries. If you do not select anything here, the payment method is available for all countries.</td>
    </tr>
    <tr>
        <td>Shipping methods</td>
        <td>-</td>
        <td>Here you can limit the accessibility of the respective payment method for certain shipping methods. If you do not select anything here, the payment method is available for all shipping methods. For example, you could restrict the payment method "Cash on collection" to the shipping type "Collection".</td>
    </tr>
    <tr>
        <td>Product types</td>
        <td>-</td>
        <td>Here you can restrict the accessibility of the respective payment method for certain product types. If you do not select anything here, the payment method will be available for all product types. For example, the payment method "Cash on collection" makes less sense for the product type "Online downloads".</td>
    </tr>
    <tr>
        <td>Product type conditions</td>
        <td>Only allow for the following product types in the shopping cart</td>
        <td>Select how the product type filter should be applied. Options:
        <ul>
        <li>Only allow if the following product types are in the shopping cart</li>
        <li>Only allow if all of the following product types are in the shopping cart</li>
        <li>Allow if one of the following product types is in the shopping cart</li>
        </ul>
        </td>
    </tr>
    <tr>
        <td>Configurations</td>
        <td>-</td>
        <td>{{< version-tag "2.2" >}} Here you can restrict the accessibility of the respective payment method for certain shop configurations. If you do not select anything here, the payment method is available for all shop configurations. Useful because depending on the payment provider not all currencies can be handled.</td>
    </tr>
    </tbody>
</table>

## Price

|  Setting  | Default setting |                                                                                                                      Description                                                                                                                      |
|-----------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Price     | -               | Here you can enter the price for this payment method and thus, for example, pass on credit card commissions to the customer. You can enter a fixed value, as well as positive or negative percentages to represent costs dependent on the cart value. |
| Tax class | -               | Here you can select a tax class if taxes are to be levied on the costs of the payment type.                                                                                                                                                           |

## Expert settings

|       Setting        | Default setting |                                            Description                                             |
|----------------------|-----------------|----------------------------------------------------------------------------------------------------|
| Show for guests only | -               | Here you can determine if this payment method should only be available for guests.                 |
| Protect module       | -               | Unlike "Show for guests only", here you can restrict the payment method for certain member groups. |

## Release

| Setting | Default setting |                                                                                                                                                    Description                                                                                                                                                     |
|---------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active  | -               | Here you can activate or deactivate the payment method. {{% notice info %}} Each payment method can be activated or deactivated. However, it is **not** automatically available in the checkout module , but must be additionally activated there. See also the corresponding chapter. {{% /notice %}} |
