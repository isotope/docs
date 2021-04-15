---
title: Checkout
description: 'The frontend configuration - Modules - Checkout'
aliases:
    - /en/frontend-configuration/modules/checkout/
weight: 125
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Kasse` is responsible for the ordering process. Many users wonder why certain settings take place in the checkout module and are not made in general. An often made beginner's mistake, for example, is a missing selection of payment methods or shipping methods, as many users assume that these - once configured - should be available in the checkout module. The fact that the modules have to be selected again here allows, for example, to configure the checkout module twice and include it on the same page and to show different member groups (by restricting access rights) the correspondingly correct module.

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Order transaction type</td> <td>Login/Registration required</td> <td>Here you can select whether this checkout module should only allow guest orders, only member orders or both. Selection options: Login/Register - required
- Only guest orders
- Both allowed

</td> </tr><tr><td>Payment methods</td> <td>-</td> <td>Here you can select which <docrobot_route name="payment-methods">payment methods</docrobot_route> should be available in this checkout module. You can also sort them here.</td> </tr><tr><td>Shipping methods</td> <td>-</td> <td>Here you can select which <docrobot_route name="shipping-methods">shipping methods</docrobot_route> should be available in this checkout module. You can also sort them here.</td> </tr><tr><td>Add to address book</td> <td>-</td> <td>If you have **not** selected only guest orders in the "Order process type", you can have isotopes for the addresses saved for members. Of course, this only makes sense if you also allow your members to manage the data. See also the chapter about the <docrobot_route name="address-book">address book</docrobot_route>.</td> </tr><tr><td>Notification</td> <td>-</td> <td>Here you can choose which <docrobot_route name="notifications_overview">notification</docrobot_route> should be sent when the order is sent.</td></tr></tbody></table>

## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Forward to confirmation page</td> <td>-</td> <td>Here you can redirect the visitor to the confirmation page if all required data is available.</td> </tr><tr><td>Skip order steps</td> <td>-</td> <td>Here you can skip order steps if only one option is available for each step. Options: - Use member address as billing address if member is logged in
- Use billing address as shipping address
- Skip payment step if only one payment method is

available Skip shipping step if only one - shipping
- method is

available </td> </tr><tr><td>Order confirmation forwarding page</td> <td>-</td> <td>Here you can select a confirmation page to which the visitor will be redirected when the order is successfully placed.</td> </tr><tr><td>Login page</td> <td>-</td> <td>Here you can select a login page to which the visitor will be redirected to log in.</td> </tr><tr><td>Shopping cart redirection page</td> <td>-</td> <td>If you select a page here, a button will be displayed in the checkout module to redirect the visitor to the shopping cart.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Product collection template</td> <td>iso\_collection\_default</td> <td>Here you can select a product collection template and change the display of the products in the checkout module as you wish. Selection options: - iso\_collection\_default
- iso\_collection\_favorites
- iso\_collection\_invoice
- iso\_collection\_mini

</td> </tr><tr><td>Sorting</td> <td>Added by date (ascending)</td> <td>Here you can define in which order the entries of a collection should be listed. Selection options: - by date added (ascending)

by - date added (descending

) by date - updated

(ascending) by date - updated (descending

) by - product name

(ascending) by product - name

- 

(descending) by - price

(ascending) - by

- 

price (descending) </td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery with which the product images of the checkout module will be processed. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td></tr></tbody></table>

## Order condition form

A `Bestellbedingungsformular` is a form created by Contao's form generator that you can include in the checkout module. It is displayed before the order is submitted and can for example consist of a checkbox "I accept the terms and conditions".

{{% notice info %}}By the way: All form fields are also available as [Simple Tokens](/de/simple-tokens/) in the corresponding notification. If you would name your AGB field e.g. `agb_checkbox`, the Simple Token `form_agb_checkbox` would be available.{{% /notice %}}

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Order Terms Form</td> <td>-</td> <td>Here you can select the desired form. Of course, you have to create it beforehand via the form generator. Logically, certain settings in the form, such as the forwarding, have no influence on this form. Only the form fields and their settings will be used.</td> </tr><tr><td>Tableless Layout</td> <td>-</td> <td>Determines whether the form should be output without HTML tables.</td> </tr><tr><td>Position of the form for the order conditions</td> <td>after the product list</td> <td>Here you can define where this form should be output. Options: - Top (Before address)
- Before product list
- After product list

</td></tr></tbody></table>
