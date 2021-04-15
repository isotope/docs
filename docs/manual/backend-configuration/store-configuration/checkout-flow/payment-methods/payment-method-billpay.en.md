---
menuTitle: 'BillPay (via Saferpay)'
title: 'BillPay payment method (via Saferpay)'
description: 'The shop configuration - order process - payment methods - BillPay (using Saferpay).'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-billpay/
weight: 130
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
        <td>Saferpay Account ID</td>
        <td>-</td>
        <td></td>
    </tr>
    <tr>
        <td>Transaction type</td>
        <td>Authorize and collect</td>
        <td>Here you can specify the transaction type:
        <ul>
        <li>**Authorize and collect** Transactions of this type are sent for authorization. The transaction is automatically routed for settlement if the transaction is successful.</li>
        <li>**Authorize Only** Transactions of this type are sent when the merchant wants to have the credit card checked for the quantity of goods sold. If the merchant does not have enough merchandise in stock or wants to check the orders before the merchandise is delivered, this transaction type will be transmitted.</li>
        </ul>
        </td>
    </tr>
    <tr>
        <td>Checkout Description</td>
        <td>-</td>
        <td></td>
    </tr>
    <tr>
        <td>Payment Page Configuration (VTCONFIG)</td>
        <td>-</td>
        <td></td>
    </tr>
    </tbody>
</table>

## Publishing

|    Setting     | Default setting |                      Description                       |
|----------------|-----------------|--------------------------------------------------------|
| Enable logging | -               | Write transaction information to the system log files. |
