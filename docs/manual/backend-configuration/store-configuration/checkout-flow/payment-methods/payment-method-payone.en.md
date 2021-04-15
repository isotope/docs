---
menuTitle: PayOne
title: 'Payment method PayOne'
description: 'The shop configuration - order process - payment methods - PayOne.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-payone/
weight: 175
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

This payment method enables integration with PayOne[(https://www.payone.de/](https://www.payone.de/)).

## Information about the PAYONE Merchant Interface (PMI).

- Isotope uses the channel "Frontend", therefore this (called "FinanceGate Frontend") must be checked.
- Isotope encrypts with md5, therefore "md5" must be selected for "Procedure Hash Value Check".
- For "TransactionStatus URL", the postsale.php must be specified with additional parameters: `http(s)://(www.)domain.tld/system/modules/isotope/postsale.php?mod=pay&id=(ID des Isotope-Kassenmoduls)`

{{% notice warning %}}
Make sure that the path to "postsale.php" is correct and accessible from outside (popular error: .htaccess protection on development environments etc.).
{{% /notice %}}

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Transaction type</td> <td>Authorize and collect</td> <td>Here you can determine the transaction type. - **Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type is transmitted.
</td> </tr><tr><td>Transaction type</td> <td>-</td> <td>PAYONE requires you to specify a settlement type. For example, you can select "Credit Card" here, which makes this payment method responsible for processing credit cards. In this respect, it also makes sense to give the payment method an appropriate title for the customer. Simply duplicate the payment method as often as you like and select a different processing type here each time to offer your customers more options.</td> </tr><tr><td>PAYONE Sub-Account ID (aid)</td> <td>-</td> <td>The PAYONE Sub-Account ID is derived from the PMI (Sub-Account must be created there, the ID will be generated automatically).</td> </tr><tr><td>PAYONE Portal ID</td> <td>-</td> <td>The PAYONE Portal ID is also derived from the PMI.</td> </tr><tr><td>Security Key</td> <td>-</td> <td>The security key is also derived from the PMI (called "Key").</td></tr></tbody></table>

## Publishing

|     Setting      | Default Setting |                      Description                       |
|------------------|-----------------|--------------------------------------------------------|
| Use test system  | -               |                                                        |
| Activate logging | -               | Write transaction information to the system log files. |
