---
menuTitle: 'PayPal PLUS'
title: 'Payment method PayPal PLUS'
description: 'The shop configuration - order process - payment methods - PayPal PLUS.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-paypal-plus/
weight: 107
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}

 {{< version "2.5" >}}


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
        <td>Client ID</td>
        <td>-</td>
        <td>These are live API credentials from your PayPal PLUS account. You can find them in your PayPal Developer account: Dashboard &gt; My Apps &amp; Credentials. [How do I create the Client ID and Secret?](https://www.paypalobjects.com/webstatic/de_DE/downloads/Dokumentation_REST_API_Zugangsdaten.pdf)</td>
    </tr>
    <tr>
        <td>Secret</td>
        <td>-</td>
        <td>These are live API credentials from your PayPal PLUS account. You can find them in your PayPal Developer account: Dashboard &gt; My Apps &amp; Credentials. [How do I create the Client ID and Secret?](https://www.paypalobjects.com/webstatic/de_DE/downloads/Dokumentation_REST_API_Zugangsdaten.pdf)</td>
    </tr>
    </tbody>
</table>


## Publishing

|     Setting     | Default setting |                                                              Description                                                               |
|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Use test system | -               | Check this box if you want to work in test mode. Requests will then automatically go to the test system and not the production system. |
| Enable logging  | -               | Write transaction information to the system log files.                                                                                 |
