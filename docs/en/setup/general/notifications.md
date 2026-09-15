# Order notifications

Notifications keep customers and staff informed. An order confirmation answers “did the shop receive my order?” A payment confirmation answers a different question.

Isotope uses Notification Center, which is a package dependency. Installing it does not configure the mail transport, sender, recipient, or message content for your business.

## Configure an order confirmation

1. Set up and test the website's email transport.
2. In Notification Center, create a notification using the Isotope order notification type available in the installation.
3. Configure its message, gateway/transport, sender, recipient, language, and text/HTML content.
4. Use supported [simple tokens](../../guides/simple-tokens.md) for order data.
5. Enable the required message records.
6. Select the notification in the checkout element's **Order notifications** setting.
7. Place a test order and inspect both delivery and content.

The checkout controller sends selected notifications when the order has been created, before the subsequent payment flow finishes. Use wording such as “We have received your order” rather than “Your payment was successful”.

## Useful content

Include an order reference, products and quantities, total and currency, billing/shipping information, selected methods, and what happens next. For offline payment, include clear instructions and a reference the customer can use.

Common tokens include `##document_number##`, `##order_total##`, `##cart_text##`, `##cart_html##`, `##billing_address##`, `##shipping_address##`, and `##payment_note##`. Token availability depends on notification context. Member tokens may be empty for guest orders.

Use the HTML cart token in an HTML body and the text version in a plain-text body. Test both formats rather than sending raw HTML to a text recipient.

## Staff notifications

You can select more than one checkout notification. Use a separate message or notification for staff if their content or recipient differs. A staff alert should point to the work to be done without claiming that the money has already arrived.

## Status-change messages

Create an Isotope order-update notification for status-change messages. In the order update form, enable sending a notification, select that notification, and fill the tracking/customer-note fields when relevant. Creating a status label alone does not automatically send a message. For an automatic integration, have the developer implement and test the intended event-based trigger.

Test when the message sends and what happens if the same status update is repeated. Avoid promising shipment before the parcel has actually been handed over.

## Troubleshooting delivery

First confirm that the order exists. Then check the selected notification, enabled message, language, resolved recipient, and mail delivery logs. A successfully created order and a successfully delivered email are separate outcomes.

Do not repeatedly submit a customer's checkout merely to test mail. Use controlled test orders and inspect the existing notification result.

Source: [OrderNotifier](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Order/OrderNotifier.php).
