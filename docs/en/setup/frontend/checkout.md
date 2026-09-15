# Cart and checkout pages

Checkout connects product selection to a recorded order and payment handling. It needs functioning destination pages, not just a checkout element dropped onto an otherwise empty website.

## Create the page chain

| Page | Content element | Main connection |
| --- | --- | --- |
| Category/product page | Product list and reader | Add-to-cart behavior |
| Cart | Cart | Checkout destination |
| Checkout | Checkout | Completed-order destination |
| Order details | Order details | Displays the selected order and handles payment |

Create and publish the pages and their articles before selecting them as destinations. Keep the order-details page out of ordinary navigation if it only makes sense with an order identifier.

## Configure the cart

Place the cart element on the cart page. Select the checkout destination and verify the cart template's update/removal controls. Decide whether adding a product keeps the customer on the product page or sends them to the cart using the relevant add-product jump setting.

Test quantity changes and removal. The customer should be able to correct their selection before ordering. Show a useful empty-cart message and a route back to browsing.

## Configure checkout

1. Add a checkout element to the Checkout page.
2. Choose guest, member, or both as the checkout method.
3. For member checkout, configure the login destination and the account experience.
4. Select the completed-order destination containing the **Order details** element.
5. Select order notifications if configured.
6. Start with visible address, shipping, and payment steps.
7. Add required order-condition forms if needed.

The completed-order destination is functional. The controller redirects there with an order identifier and a request to initialize payment. A plain “thank you” text page does not replace the order-details element.

## What customers complete

The core supplies address, shipping, and payment steps, plus the order summary. Some steps are unnecessary for particular carts, such as shipping for an exempt service.

The customer must complete the relevant steps before placing the order. The summary is their last opportunity to review products, quantities, addresses, charges, and the total.

Checkout notifications are sent after the order is created. They should confirm the order, not assert that payment has succeeded unless a separate verified payment event supplies that message.

## Skip steps only after testing

Options can use a signed-in member's address, always reuse billing as shipping, or skip a method selection when only one method is available. These reduce effort but also remove opportunities for correction.

Test all relevant customer types before enabling them. A business customer ordering a gift may need a different delivery address.

## Order-condition forms

Create the appropriate form in Contao and select it in checkout's order-condition settings. Choose its step and position. Product-type conditions can restrict when it appears.

Use required validation when the answer is genuinely necessary. Verify that the form blocks submission when incomplete and that its values reach the order/notification context you need. Form fields can become `form_*` notification tokens.

## Verify all destinations

Place a guest order, open its details, and verify the payment behavior. Repeat as a member where supported. Test a missing identifier, a different member's order, and an empty cart. The [launch checklist](../../guides/launch.md) expands these tests.

Source: [CheckoutController](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/CheckoutController.php).
