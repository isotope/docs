# Process orders

An order is a record of what the customer submitted. Processing it means checking what was ordered, confirming payment arrangements, and fulfilling it accurately.

## Practice with the first order

Open the Trail T-shirt order from [Your first shop](../getting-started/first-shop.md). It contains one `TSHIRT-BLUE-M`, 22.00 for the product, and 5.50 delivery, totaling 27.50 EUR. Test payment has collected no money. Use this order to learn where information appears, then apply the workflow below to real orders with actual payment and dispatch evidence.

## Open and review the order

In **Isotope eCommerce → Orders**, locate the order by its reference or other available filters. Check:

- Products, variants, customer-defined options, and quantities.
- Total, currency, tax information, shipping charge, and any payment fee.
- Billing and shipping addresses.
- Selected shipping and payment methods.
- Order, payment, and shipping statuses.
- Available payment transaction records and event history.

Do not use the order's overall status as the only evidence for payment or dispatch.

## Confirm payment

For online payment, reconcile the recorded result with the provider if it is unclear. A browser returning to the shop or an email reaching the customer does not prove the payment succeeded.

For offline payment, check the actual bank receipt, cash collection, or agreed credit arrangement. Update the payment status according to that evidence and your process.

An order with an unresolved payment should remain distinguishable from one ready for fulfillment. Use the configured statuses rather than free-form notes alone.

## Prepare fulfillment

Pick the exact SKU or variant and read personalization fields. Confirm the destination and method. For pickup, prepare the order and follow your collection communication process.

Create the required [document](../setup/general/documents.md) when it is appropriate in your workflow. Preview first if the template has recently changed.

## Record dispatch

After the real shipment or handover, update the shipping status. Record tracking and customer notes in the supported order update/log fields. Send the intended notification if your workflow offers that selection.

If only part of the order ships, use a suitable partial status and retain a clear record of what remains. A partial status label is not itself a per-item warehouse allocation system.

## Complete the order

Set the overall order status according to your business definition of completion. Check payment and shipping separately. An order can legitimately remain open for payment after delivery if you offer invoice terms.

Allowed status choices depend on the current workflow. If a needed transition is missing, have the administrator review the configuration rather than changing unrelated statuses to work around it.

## When something is wrong

If an address, amount, or item needs correction after ordering, preserve the original record and agree the appropriate amendment, cancellation, or replacement procedure. A historical order should not silently change because a catalog product was edited.

For suspected duplicate orders, compare references, payment transactions, and customer intent before fulfilling either one twice. For mail problems, troubleshoot delivery without creating additional live orders.

Continue with [Returns and refunds](returns.md) and [Troubleshooting](troubleshooting.md).
