---
menuTitle: Sofortüberweisung
title: 'Payment method instant bank transfer'
description: 'The shop configuration - order process - payment methods - instant bank transfer.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-sofortueberweisung/
weight: 125
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

With Sofortüberweisungen, the customer authorizes SOFORT AG to make a transfer from the customer's account to the merchant using an online banking TAN provided by the customer. Further information is available [on the company website.](https://www.sofort.com/ger-DE/verkaeufer/su/e-payment-sofort-ueberweisung/)

A fee-based contract with SOFORT AG is required for use.

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Transaction type</td> <td>Authorize and collect</td> <td>Here you can determine the transaction type. - **Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type will be transmitted.
 
</td> </tr><tr><td>Customer ID</td> <td>-</td> <td>The SOFORT customer number is located in the SOFORT backend on the left.</td> </tr><tr><td>Project ID</td> <td>-</td> <td>The project ID can also be found in the SOFORT backend, for example in the upper right corner.</td> </tr><tr><td>Project Password</td> <td>-</td> <td> The project password must be generated in the SOFORT backend and can then be viewed in a modal window. {{% notice warning %}}
 (ATTENTION: The notification password must not be set in the SOFORT backend. SOFORT support can delete this if it has already been set by mistake.

{{% /notice %}}
 </td></tr></tbody></table>

## Release

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Enable logging</td> <td>-</td> <td>Write transaction information to the system log files.</td></tr></tbody></table>

The following screenshot highlights where the data needed for the configuration can be read from the SOFORT backend:

![Configuration parameters in the SOFORT website](sofort-values.png)

A complete backend configuration should look something like this:

![SOFORT in the backend](backend-mask.png)

## Configuration in the SOFORT backend

In the SOFORT provider menu, various settings must be made in the project so that Isotope and SOFORT work together correctly. Aborts and error messages during orders are probably due to incorrect settings in these fields.

There are various sub-items in the **Advanced Settings** tab. *Shop system interface* and *notifications* are particularly important, but each setting should be carefully checked before going live.

### Settings for the shop system interface

This configuration determines, among other things, the URL to which a buyer is redirected after a transaction. Usually this should be the confirmation page (step *complete*) of Isotope eCommerce. In addition, an error page ( *failed* step) can be specified.

![SOFORT forwarding targets](sofort-redirect.png)

{{% notice warning %}}
Note

that on the screenshot the URL's are given without the "step" parameter! It depends on whether you have enabled "Enable Auto\_item" in your Contao system settings or not. If you have not activated it, the URLs must contain "step" (e.g. "/checkout/step/complete.html" etc.).

{{% /notice %}}
 It is important to pass a URL parameter so that the posting of isotopes can be assigned. For this purpose, the component `?uid=-USER_VARIABLE_2-` must be appended to the address. This parameter will be replaced by SOFORT with the booking reference passed by Isotope.

### Notification settings

Isotope eCommerce does not rely on a URL call that a user could make themselves without actually making the payment. Instead, SOFORT must make an asynchronous call to an Isotope interface with a so-called post-sale request to confirm to Isotope that the payment has been made. Only then is the user redirected back to the shop.

For this purpose, an **HTTP notification** must be created in the SOFORT backend. If this HTTP POST request cannot be executed, the order process terminates. It must therefore be ensured that SOFORT can reach the path specified here from outside and is not prevented from doing so by firewalls or .htaccess statements.

![IMMEDIATE Notification](sofort-notification.png)

The URL for the notification is the domain as well as the path to the postsale file of Isotope, supplemented by some parameters. For example, if Contao is installed in the base directory, the path is like this:

`https://domain/system/modules/isotope/postsale.php?mod=pay&id=1&uv1=-USER_VARIABLE_0-&uv1hash=-USER_VARIABLE_0_HASH_PASS-`

The ID of the payment module can be read in the backend of Contao via the blue information icon of the payment type. The number has to be passed as URL parameter *id*.

### Passwords and hash algorithm

To secure the transferred data, hash sums of some transfer parameters are sent with each call. Isotope eCommerce requires that these hashes are generated with the SHA1 method. Since SOFORT uses a newer algorithm by default, the setting has to be adjusted.

![SOFORT hash method](sofort-hash.png)
