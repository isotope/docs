---
menuTitle: ePay
title: 'Payment method ePay'
description: 'The shop configuration - order process - payment methods - ePay.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-epay/
weight: 145
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
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
        <td>Transaction Type</td>
        <td>Authorize and collect</td>
        <td>- **Authorize and collect**Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.
            - **Authorize Only**Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough goods in stock or wants to check the orders before the goods are delivered, this transaction type is transmitted.
        </td>
    </tr>
    <tr>
        <td>Integration type</td>
        <td>Full Screen</td>
        <td>Integration Options: - **Full Screen**
            - **Integrated payment form**
        </td>
    </tr>
    <tr>
        <td>Merchant number</td>
        <td>-</td>
        <td>The merchant number.</td>
    </tr>
    <tr>
        <td>Security Key</td>
        <td>-</td>
        <td>The secret key in your ePay configuration.</td>
    </tr>
    </tbody>
</table>

## Publishing

|    Setting     | Default setting |                      Description                       |
|----------------|-----------------|--------------------------------------------------------|
| Enable logging | -               | Write transaction information to the system log files. |
