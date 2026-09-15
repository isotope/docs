# Payment methods

A payment method describes how a customer pays. An offline method, such as payment on collection, needs staff to reconcile the money. An online method delegates a payment attempt to a provider and receives a result.

An order can exist before payment completes. Configure [payment statuses](../general/order-status.md) and test failure as carefully as success.

## Start with offline payment

The core registers a Cash payment type. You can use it for an offline workflow with a suitable label and instructions.

1. Open **Configuration → Payment methods**.
2. Select the Cash type.
3. Enter the name and customer label, such as “Pay on collection”.
4. Add a payment note explaining what the customer should do.
5. Select the payment status used when processing starts. Use a status that reflects your actual offline workflow.
6. Restrict shipping methods or product types if necessary.
7. Add a fee and tax class only if intended.
8. Enable the method and select it in the store configuration.
9. Place a test order and verify the recorded payment status and instructions.

The Cash implementation updates the configured status and returns to the shop. It does not check a bank account or collect money. Staff must confirm receipt through the real payment process before marking the payment accordingly.

For a bank-transfer arrangement, use an appropriate customer label and include the required bank details in a tested notification. Filling the store's bank fields alone does not display instructions everywhere.

## Online integrations and the documented version

The checked source also registers a PayPal implementation and a PayPal settings form, including an account field, processing/paid/failed status mappings, and debug mode. However, its upgrade notes say third-party payment methods were removed. See [version notes](../../reference/version-notes.md) for this inconsistency.

Treat availability in the installed, tested release as decisive. Have your integrator verify the intended provider integration, configuration persistence, and callback handling before enabling live payments. Do not infer support for every gateway listed in an Isotope 2 manual.

## Map the outcomes

A provider may report processing, success, or failure. Map these to the matching **payment** statuses. The order's overall status is a separate workflow.

A return to the shop does not always settle the payment. Some providers report the authoritative result separately. Confirm the stored transaction result as well as the page the customer sees.

## Availability restrictions

A payment method can be limited by a rule, allowed shipping methods, and product-type conditions. “Cash on collection” should not appear for an ordinary parcel order unless that is intentional.

Check carts that do not require shipping as well. An over-restrictive shipping-method selection can remove a payment option for services.

## Test before going live

Exercise success, customer cancellation, failure, and an interrupted return to the shop using the provider's supported test process. Verify the amount, currency, order association, and resulting status. Confirm that repeated notifications do not create duplicate business actions in your integration.

Keep test and live credentials separate. After switching to live mode, run the acceptance procedure agreed with the provider and shop owner.

Implementation: [CashPayment](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CashPayment.php), [CorePaymentFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CorePaymentFactory.php).
