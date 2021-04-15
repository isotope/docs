---
menuTitle: ExperCash
title: 'Payment method ExperCash'
description: 'The shop configuration - order process - payment methods - ExperCash.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-expercash/
weight: 150
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}

 ## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>ExperCash Popup ID</td> <td>-</td> <td>The pop-up ID of the ExperCash portal.</td> </tr><tr><td>ExperCash Profile</td> <td>0</td> <td>The three digit profile number of the ExperCash profile.</td> </tr><tr><td>ExperCash pop-up key</td> <td>-</td> <td>The pop-up key of the ExperCash portal.</td> </tr><tr><td>Transaction type</td> <td>Selection of the payment type by the end customer:</td> <td>Predefine the transaction type or let the customer select it: - **Selection of payment type by the end customer.**
- **Payment by direct debit (ELV)**
- **Verification and storage of account data for later collection**
- **Credit card payment**
- **Binding reservation on a credit card for later collection**
- **Transaction via giropay**
- **Transaction via Sofortüberweisung**
</td></tr></tbody></table>

## Template

|   Setting    | Default setting |               Description               |
|--------------|-----------------|-----------------------------------------|
| CSS template | -               | Select a CSS file to pass to ExperCash. |

## Share

|    Setting     | Default Setting |                      Description                       |
|----------------|-----------------|--------------------------------------------------------|
| Enable logging | -               | Write transaction information to the system log files. |
