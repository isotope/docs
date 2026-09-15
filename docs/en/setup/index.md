# Setup roadmap

Configuration defines the choices available to product editors and customers. Work through it in dependency order so you can select the records you have already created.

## Recommended order

| Step | Configure | Why it comes here |
| --- | --- | --- |
| 1 | [Store configuration](general/stores.md) | Establish currency, addresses, and the shop's identity |
| 2 | [Tax rates](checkout/tax-rates.md) and [tax classes](checkout/tax-classes.md) | Decide what your entered prices mean |
| 3 | [Attributes](products/attributes.md), [galleries](general/galleries.md), and [product types](products/types.md) | Define how products are edited and shown |
| 4 | [Products](../usage/products.md) and category pages | Supply something to sell |
| 5 | [Order statuses](general/order-status.md) | Prepare the payment and fulfillment workflow |
| 6 | [Shipping](checkout/shipping.md) and [payment](checkout/payment.md) | Define available delivery and payment choices |
| 7 | Store configuration again | Select the shipping and payment methods you just created |
| 8 | [Product pages](frontend/products.md) and [checkout pages](frontend/checkout.md) | Connect the customer journey |
| 9 | [Notifications](general/notifications.md) and [documents](general/documents.md) | Complete communication and administrative output |
| 10 | [Launch checks](../getting-started/launch.md) | Verify the complete shop |

For a hands-on walkthrough with one product, use [Your first shop](../getting-started/first-shop.md).

## Configuration versus daily work

Creating a product type is setup work. Adding another T-shirt of that type is daily work. Defining which shipping statuses may follow each other is setup. Marking a particular order as shipped is daily work.

Restrict configuration access to people who understand these wider effects. A change to a shared tax class, attribute, or store configuration can affect many products and future carts.

## Names and labels

Many records have both a name and a label. Use names that staff can recognize, such as “Domestic parcel, standard tariff”. Use customer-facing labels that make a clear promise, such as “Standard delivery”. Avoid putting internal identifiers in the customer's choices.

## Validate one change at a time

After creating a record, select it wherever it is used and test the relevant frontend behavior. A method can exist but remain unavailable because it is disabled, unselected in the active configuration, or excluded by a rule.
