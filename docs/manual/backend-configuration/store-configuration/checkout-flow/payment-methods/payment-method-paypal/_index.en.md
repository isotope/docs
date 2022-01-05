---
menuTitle: PayPal
title: 'Method of payment PayPal'
description: 'The shop configuration - order process - payment methods - PayPal.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-paypal/
weight: 105
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
 A general description is missing here.
{{% /notice %}}

## Configuration of the payment provider

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
            <td>PayPal account</td>
            <td>-</td>
            <td>Your email address associated with your PayPal account. The amount will be credited to this PayPal account.</td>
        </tr>
    </tbody>
  </table>

{{% notice warning %}}
The PayPal payment method must also be activated in the "Checkout" module, which is often forgotten.
{{% /notice %}}

![Activation in the Cash module](kassenmodul.png)

## Enable

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Use test system</td> <td>-</td> <td>If enabled, the payment will only be emulated in a test environment (sandbox) but not actually executed. You can also [create](https://developer.paypal.com/docs/classic/lifecycle/sb_create-accounts) a [test account](https://developer.paypal.com/docs/classic/lifecycle/sb_create-accounts) at Paypal. If you get a security warning in Firefox instead of the Paypal sandbox page (SSL\_ERROR\_NO\_CYPHER\_OVERLAP) you have to reset the setting security.tls.version.max in about:config.</td> </tr><tr><td>Enable logging</td> <td>-</td> <td>Write transaction information to the system log files.</td></tr></tbody></table>

## Configuration at PayPal

### General description

The "PayPal" payment method uses the service of PayPal (Europe) S.à r.l. et Cie, S.C.A.. The customer is redirected externally to PayPal, completes the payment there and authorizes PayPal to direct debit.

In order to use PayPal, the shop operator requires a PayPal account. If the customer does not have a PayPal account, he is free to pay with his bank account or credit card, depending on the settings made in the PayPal backend.

[More information about PayPal](https://www.paypal.com/de/)

### Note for description of PayPal account setting

If there are multiple email addresses associated with the PayPal account, the default email address must be set in Isotope eCommerce.

### Configuration in PayPal backend

For PayPal, various settings need to be made in order for Isotope and PayPal to work together properly.

### Type of PayPal account

The PayPal account must be a business account, only then the required settings will be enabled.

### Settings for the IPN

The Instant Payment Notification (IPN) informs the shop owner via email about incoming payments on the PayPal account. In the screenshot you can see under which menu item you can find it:

![Settings for the IPN](paypal-ipn.jpg)

In addition to the pure activation, the correct notification URL must also be entered. The URL is the absolute path to postsale.php, to which the ID of the payment module "PayPal" is appended.

{{% notice info %}}

If the module has the **ID 1**, the notification URL is e.g. `https://www.domain.de/system/modules/isotope/postsale.php?mod=pay&id=<strong>1</strong>`

{{% /notice %}}

![Settings for the notification URL](paypalurl.jpg)

{{% notice warning %}}

For online stores, it is generally recommended to use an SSL certificate. PayPal requires encrypted connections as of June 2016, so the notification URL must also contain https. Please make sure that the online shop is running under SSL.

{{% /notice %}}

#### Voice encoding settings for IPN.

In PayPal the language encoding should be set to UTF-8, by default it is set to `windows-1252`, which can lead to errors, especially with umlauts. You can find the settings under "Language encoding of PayPal buttons", there select `UTF-8` under "More options".

![Voice coding settings for IPN](ebay-kodierung-buttons.png)

#### Hints for using Isotope, eBay and IPN at the same time

If you also run an eBay shop (or other systems) with your PayPal account, PayPal will try to communicate with Isotope via IPN for eBay orders as well. Isotope then reports back with a 500 or 424 status code, but more and more errors appear in the system log and PayPal sends several mails that the IPN URL should be checked for errors.

### Settings for the return URL

If you want the customer to be automatically redirected back to the Isotope shop after successful payment, you have to set a setting in the "Website Settings" of the PayPal backend.

![Settings for the return URL](website-einstellungen-overview.jpg)

According to PayPal guidelines, the return URL must contain various information. Here you enter the absolute path to this page.

![Settings for the redirect URL](rueckleitung-einstellungen.jpg)

### Email address

In the PayPal account under "Profile and settings" -> "Login and security" -> "Email address", the email address defined for the isotope payment method "PayPal Standard" in Contao under "PayPal account" must be defined as the "default address". A second email address that may have been entered in the PayPal account can lead to disruptions in the payment process.

### Settings in the backend configurations in the payment type
#### With activated test system

For the payment processing in the PayPal sandbox to work in the test system you have to
the checkmark at **Use test system** must be set and
under **PayPal account** the business email address of the created sandbox account must be entered.
![Shop-Konfiguration](https://user-images.githubusercontent.com/33038265/116972092-cf7e7d80-acba-11eb-8536-136cf83b1072.png)

{{% notice warning %}}

Before the store goes live, the checkmark must be removed again and the store's own email address must be inserted.

{{% /notice %}}
