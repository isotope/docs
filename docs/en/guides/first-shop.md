# Your first shop: one product to one order

This walkthrough creates a small learning shop called Trail Supply. You will sell one mug, offer one delivery method, and arrange payment offline.

**Outcome:** a customer can find the mug, add it to a cart, provide an address, place an order, and see its details. You can then find and process that order in the backend.

## Before starting

Use a working [Isotope installation](../getting-started/installation.md) and a Contao website with a published root, page layout, and articles. Work on a test site. Use a mailbox you control and keep online payment integrations in their test environment.

Have one image and a short description ready. Choose one currency and one allowed delivery country for this exercise.

## 1. Create the store configuration

Under **Configuration → Store configurations**, create “Trail Supply test”. Choose your currency and **Gross** price display. Leave the price factor at `1`.

Set the default billing and shipping countries, then explicitly select allowed countries. Empty allowed lists mean all countries. Enable the address fields needed for the exercise, including a valid email address.

Assign this configuration to your website structure. Keep the store ID consistent across the pages belonging to this shop.

**Check:** the configuration exists and your shop pages use the intended website root.

## 2. Establish a simple price

For this isolated workflow exercise, use a price of `20.00` with no tax class. This makes the arithmetic simple. It does not prescribe the tax setup of a live shop.

Before accepting real orders, replace this exercise's tax treatment with your verified [tax classes and rates](tax-example.md).

## 3. Create a product type and gallery

Create a gallery suitable for product details, with an appropriate image size. Create a “Physical product” type using the core product class available in the installation.

Include name, SKU, teaser/description, price, images, and the relevant publishing/shipping fields. Leave variants and advanced pricing off. Select suitable list and reader templates/galleries.

**Check:** creating a product with this type exposes the fields you need.

## 4. Create the pages

Create and publish these pages with articles:

| Page | Purpose |
| --- | --- |
| Drinkware | Product category with list and reader |
| Cart | Review and edit the cart |
| Checkout | Supply addresses and choose methods |
| Order details | Display the order and handle payment |

Use current-page reader mode on Drinkware for this exercise. Place the product list and reader there, with **Hide in reader mode** enabled on the list.

Place a Cart, Checkout, and Order details content element on the matching pages.

## 5. Create the mug

Create “Trail mug” in **Products** using the new type. Enter SKU `MUG-001`, price `20.00`, and the description. Assign it to Drinkware, add the image, and publish it.

**Check:** the mug appears on Drinkware, opens in the reader, and can be added to a cart. If it does not appear, check category scope and publication before continuing.

## 6. Create delivery and payment

Create an enabled flat shipping method named “Test standard delivery”. Use flat calculation, charge `5.00`, and no tax class for the exercise.

Review the supplied payment statuses. Create an enabled Cash payment method with a customer label describing your offline test arrangement. Choose a processing status consistent with an unresolved payment. Add a note such as “This is a test order. No payment is required.”

Return to the store configuration and select both methods.

**Check:** both methods appear for the physical mug and chosen address.

## 7. Connect checkout

Set the cart's checkout destination to Checkout. In the checkout element, allow guest checkout and choose Order details as the completed-order destination.

Keep the steps visible for now. The order-details destination must contain its functional element, because payment handling continues there.

Optionally configure an order confirmation and select it in checkout. Use wording that acknowledges an order, not successful payment.

## 8. Place the test order

Open a private browser session. Add one mug, view the cart, and proceed to checkout. Enter fictional address details and your own test email. Choose the methods and inspect the summary.

Expected exercise totals are product `20.00`, shipping `5.00`, and total `25.00`, with no payment fee or tax. If your total differs, inspect the saved prices, factor, methods, and tax class before placing the order.

Submit once. Confirm that you reach the order-details page and can identify the order. If a notification is enabled, inspect the message.

## 9. Process it in the backend

Open **Orders** and locate the test order. Verify the product, quantity, address, total, and the three statuses. Remember that the Cash method has not collected money.

Rehearse your payment reconciliation and fulfillment procedure using the test record. Preview a document if configured. Walk through the allowed shipping and order transitions.

## 10. Expand deliberately

Add a second product, then variants, taxes, more shipping choices, and the intended payment integration. Test after each change.

Before launch, complete the [launch checklist](launch.md). A successful learning order proves the basic page connections, not every real-world checkout case.
