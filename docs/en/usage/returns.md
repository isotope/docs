# Cancellations, returns, and refunds

These actions describe different parts of the business process.

A **cancellation** stops further processing. A **return** concerns goods coming back. A **refund** concerns money going back. One can happen without all the others.

## Cancel an unpaid order

1. Identify the correct order and verify its payment situation.
2. Stop picking or delivery work through your operational process.
3. Use an allowed order/payment transition appropriate to the cancellation.
4. Record the reason and communicate the outcome to the customer.
5. Check whether an external payment attempt is still processing.

A delayed provider result may arrive after a customer abandons checkout. Reconcile unresolved transactions before assuming nothing was paid.

## Handle a return

Record which items are being returned and why. Check what actually arrives and whether any part of the order remains fulfilled. Use the available Returned or Returned partially shipping statuses as appropriate.

Decide separately whether a refund, replacement, or other resolution is due under the shop's agreed process. This manual describes record handling and does not set your return policy.

## Issue and record a refund

Perform the refund through the payment provider or offline payment process that actually moves the money. Use the integration's refund action if it explicitly supports one. Confirm the result and amount.

Then update the payment record/status through the supported workflow, retain the external reference, and send the intended communication. **Changing the status label to Refunded does not by itself prove that money was returned.**

For a partial refund, make clear which amount and items it covers. Do not infer automatic item-level accounting merely from a Paid partially or Refunded partially status.

## Stock, shipping, and documents

If you use stock or accounting integrations, verify whether they react to the chosen transition and whether repeated updates are safe. Returning goods does not necessarily mean they are immediately sellable again.

Preserve existing documents and follow the business's correction-document process. Deleting an order to make an error disappear also removes context needed to reconcile the transaction.

## Test exception paths

Before launch, rehearse an unpaid cancellation, a failed payment retry, a full return, and a partial refund with test data. Record which actions are performed in Isotope, which in the payment provider, and which in another system.

Related: [Order statuses](../setup/general/order-status.md), [Processing orders](orders.md).
