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

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Transaction type</td> <td>Authorize and collect</td> <td>Here you can define the transaction type. - **Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type will be transferred.
</td></tr></tbody></table>

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Merchant ID</td> <td>-</td> <td>The merchant ID.</td> </tr><tr><td>HMAC Key</td> <td>-</td> <td>Key used to encrypt exchanged data.</td> </tr><tr><td>Hash Method</td> <td>MD5 (deprecated)</td> <td>Hash method to encrypt the exchanged data. Available for selection are: - **MD5**Insecure and therefore not recommended
- **SHA-256**Recommended setting
</td> </tr><tr><td>Convert HMAC key</td> <td>-</td> <td>Defines if the entered HMAC key should be converted to bytes before encrypting the exchanged data. This is necessary if you copy the HMAC key 1:1 from the Datatrans security settings.</td></tr></tbody></table>

## Share

|     Setting     | Default setting |                                    Description                                     |
|-----------------|-----------------|------------------------------------------------------------------------------------|
| Use test system | -               | Defines if all transactions should be processed through the Datatrans test system. |
| Enable logging  | -               | Write transaction information to the system log files.                             |
