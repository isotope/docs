---
menuTitle: 'Open Payment Platform'
title: 'Payment method Open Payment Platform'
description: 'The shop configuration - order process - payment methods - Open Payment Platform.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-opp/
weight: 165
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}
 ## General settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Transaction Type</td> <td>Authorize and collect</td> <td>Here you can specify the transaction type. - **Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
- **Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type will be transferred.

</td></tr></tbody></table>

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>User ID</td> <td>-</td> <td>The user ID.</td> </tr><tr><td>Password</td> <td>-</td> <td>The user password.</td> </tr><tr><td>Entity/Channel ID</td> <td>-</td> <td>The entity or channel ID.</td> </tr><tr><td>Payment Tokens</td> <td>-</td> <td>Select supported payment tokens: - American Express
- Diners Club
- SEPA Direct Debit
- giropay
- JCB
- Klarna hire purchase
- Klarna invoice
- MasterCard
- paydirect
- PayPal
- Installment purchase by easyCredit
- SOFORTüberweisung
- VISA

</td></tr></tbody></table>

## Publishing

<table><thead><tr><th>Setting</th> <th>Standard setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Use test system</td> <td>-</td> <td>Defines if all transactions should be processed through the Datatrans test system.</td> </tr><tr><td>Enable logging</td> <td>-</td> <td>Write transaction information to the system log files.</td></tr></tbody></table>
