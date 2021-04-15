---
menuTitle: 'Savings Bank'
title: 'Savings bank payment method'
description: 'The shop configuration - order process - payment methods - savings bank.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-sparkasse/
weight: 180
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}


## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Payment type</td> <td>-</td> <td></td> </tr><tr><td>Transaction Type</td> <td>Authorize and Collect</td> <td>Here you can determine the transaction type. - **Authorize and Collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type will be transmitted.
</td> </tr><tr><td>Seller ID</td> <td>-</td> <td></td> </tr><tr><td>Password</td> <td>-</td> <td></td> </tr><tr><td>Reference</td> <td>-</td> <td></td></tr></tbody></table>


## Publishing

|     Setting     | Default setting |                      Description                       |
|-----------------|-----------------|--------------------------------------------------------|
| Use test system | -               | -                                                      |
| Enable logging  | -               | Write transaction information to the system log files. |
