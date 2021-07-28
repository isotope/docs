---
menuTitle: Datatrans
title: 'Payment method Datatrans'
description: 'The shop configuration - Order process - Payment methods - Datatrans.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-datatrans/
weight: 140
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Datatrans is a Swiss payment service provider. The module implements the payment interface for processing transactions via a variety of payment methods such as VISA, Mastercard, Postfinance and AMEX.

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
        <td>Transaction type</td>
        <td>Authorize and collect</td>
        <td>Here you can define the transaction type.<br><br>
            <ul>
            <li><strong>Authorize and collect</strong><br>
            Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.</li>
            <li><strong>Authorize Only</strong><br>
            Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type will be transferred.</li>
            </ul>
        </td>
    </tr>
</tbody>
</table>

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
        <td>Merchant ID</td>
        <td>-</td>
        <td>The merchant ID.</td>
    </tr>
    <tr>
        <td>HMAC Key</td>
        <td>-</td>
        <td>Key used to encrypt exchanged data.</td>
    </tr>
    <tr>
        <td>Hash Method</td>
        <td>MD5 (deprecated)</td>
        <td>Hash method to encrypt the exchanged data. Available for selection are:<br><br>
            <ul>
                <li><strong>MD5</strong><br>Insecure and therefore not recommended</li>
                <li><strong>SHA-256</strong><br>Recommended setting</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Convert HMAC key</td>
        <td>-</td>
        <td>Defines if the entered HMAC key should be converted to bytes before encrypting the exchanged data. This is necessary if you copy the HMAC key 1:1 from the Datatrans security settings.</td>
    </tr>
</tbody>
</table>

## Share

|     Setting     | Default setting |                                    Description                                     |
|-----------------|-----------------|------------------------------------------------------------------------------------|
| Use test system | -               | Defines if all transactions should be processed through the Datatrans test system. |
| Enable logging  | -               | Write transaction information to the system log files.                             |


## Configuration at Datatrans

In order for the module to work correctly, some settings must be made on the payment provider's site.  
To do this, log in to the system and make the following settings:

 - UPP Verwaltung => UPP Daten
    - The post URL must point to the postsale.php script in your installation (example <http://example.org/system/modules/isotope/postsale.php>)


## Configuration in Contao

Unfortunately, Datatrans uses a POST request to send the shop visitor back from the merchant portal to Contao,  
 which interferes with the [request token check](https://docs.contao.org/dev/framework/request-tokens/).  
 To circumvent this limitation, you must disable the referer check in the Contao settings (`disableRefererCheck`).
