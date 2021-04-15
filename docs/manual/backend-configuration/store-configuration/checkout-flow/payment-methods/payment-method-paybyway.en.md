---
menuTitle: Paybyway
title: 'Payment method Paybyway'
description: 'The shop configuration - order process - payment methods - Paybyway.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-paybyway/
weight: 170
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{< version "2.2" >}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Transaction Type</td> <td>Authorize and collect</td> <td>Here you can determine the transaction type. - **Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type is transmitted.
</td> </tr><tr><td>Transaction type</td> <td>-</td> <td></td> </tr><tr><td>PAYONE subaccount ID (aid)</td> <td>-</td> <td></td> </tr><tr><td>PAYONE Portal ID</td> <td>-</td> <td></td> </tr><tr><td>Security Key</td> <td>-</td> <td></td></tr></tbody></table>

## Publishing

|     Setting      | Default setting |                      Description                       |
|------------------|-----------------|--------------------------------------------------------|
| Use test system  | -               |                                                        |
| Activate logging | -               | Write transaction information to the system log files. |
