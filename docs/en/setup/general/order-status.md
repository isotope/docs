# Order, payment, and shipping statuses

Isotope 3 keeps three status tracks. Together, they tell staff what has happened and what remains to do.

| Track | Typical values | Purpose |
| --- | --- | --- |
| Order | Pending, Processing, Complete, On Hold, Cancelled | Overall processing |
| Payment | Open, Processing, Paid, Failed, Refunded | Money and payment attempts |
| Shipping | Open, Shipped, Shipped partially, Returned | Delivery progress |

For example, an order can be Processing, Paid, and Open for shipping. Staff can then prepare it for dispatch.

## Start with the supplied statuses

The migration supplies default records for missing status types. Review those records under **Configuration → Order status** before adding custom ones.

Keep the technical names stable. Code, saved orders, payment methods, and workflow transitions can refer to them. Change a customer-facing label when you only need different wording.

## Next possible states

Each record defines which states can follow it. These transitions form a workflow.

For example, an open payment can move to processing, paid, or failed as appropriate. A shipping record can move from open to shipped. If a desired next status is absent in order processing, inspect the current status's allowed transitions and the operator's permissions.

A color makes the backend easier to scan. It does not change what the status does.

## Payment state versus payment label

A payment status also maps to a technical state:

- **Pending** allows payment to be attempted or retried.
- **Processing** means the outcome is unresolved.
- **Complete** ends the active payment flow.

Do not equate the technical state Complete with proof of received money. The supplied Cancelled payment status also uses Complete. Staff must read the actual payment status and payment evidence.

Map payment-method outcomes deliberately. The offline Cash method simply sets its configured processing status. It does not detect receipt of money.

## Status changes do not perform every business action

Setting Shipped does not book a parcel. Setting Refunded does not necessarily issue a refund through the provider. Setting an order to Complete does not prove that both payment and delivery are finished.

Define the real action, perform or verify it, then update the corresponding record. If an integration automates that sequence, document its trigger and test it.

## Test your workflow

Use a test order to walk through normal fulfillment, failed payment, cancellation, and return. Confirm that staff can select necessary transitions and cannot accidentally skip critical business steps through your chosen permissions and procedures.

Next: [Processing orders](../../usage/orders.md).
