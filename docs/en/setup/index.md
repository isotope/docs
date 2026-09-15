# Setup roadmap

Configuration defines the choices available to product editors and customers. Work through it in dependency order so you can select the records you have already created.

## Follow the navigation from top to bottom

The numbered stages in the sidebar follow the order below. Complete stages 1–6 for the basic shop. Stage 7 contains optional features to add when you need them.

For a guided first purchase with exact values, use [Your first shop](../getting-started/first-shop.md). This roadmap explains the same dependencies in more detail.

### 1. Establish the store

Create the [store configuration](general/stores.md) and assign it to the website root. Choose the currency, price display, and address countries. Leave shipping and payment selections until you have created those methods in stage 5.

### 2. Configure prices and taxes

Read [Prices and taxes explained](../concepts/prices-and-taxes.md), then learn how [rules](rules.md) decide when a setting applies. Create any required rules before the [tax rates](checkout/tax-rates.md) that use them. Create [tax classes](checkout/tax-classes.md) after the rates.

For the first Trail T-shirt order, use the fictional 10% rate and Standard goods class from the walkthrough. That single-country example does not need a rule.

### 3. Prepare the catalog

Set up any custom [attributes](products/attributes.md), then [galleries](general/galleries.md), then [product types](products/types.md). A product type selects existing attributes and galleries, which is why it comes last in this stage.

For Trail Supply, prepare Clothing images and the Clothing type. Keep variants and advanced pricing disabled for the first purchase.

### 4. Build the storefront

Follow [Displaying products](frontend/products.md) to create category pages and connect product lists and readers. Then [create the Trail T-shirt](../usage/products.md), assign it to T-shirts, and verify its description, image, and 22.00 price as a visitor. The product-editing instructions live in Daily use because you will repeat that task after launch.

### 5. Connect checkout

Review [order statuses](general/order-status.md) before configuring [shipping](checkout/shipping.md) and [payment](checkout/payment.md). Payment methods need the statuses that describe their outcomes and can depend on shipping choices.

Return to the [store configuration](general/stores.md) and select the methods you created. A saved method is not automatically offered by the store.

Decide how [members and guests](frontend/customers.md) will shop, then connect the [cart and checkout pages](frontend/checkout.md), including the order-details destination. Place the first test order and confirm it appears in Orders.

### 6. Prepare for daily operations

Configure [notifications](general/notifications.md), using [simple tokens](general/simple-tokens.md) for order-specific information. Return to the checkout element to select the order confirmation, then place another test order to verify delivery and wording.

Prepare any required [documents](general/documents.md) and give staff appropriate [access](general/access.md). Check that they can [process the test order](../usage/orders.md).

### 7. Extend the shop when needed

These features are optional. Choose the ones your shop needs after the basic purchase works:

- [Variants](products/variants.md) for selectable T-shirt sizes and colors.
- [Related products](products/relations.md) to recommend the Trail hoodie.
- [Base prices](products/base-prices.md) to compare garment-wash bottle sizes.
- [Shipping recipes](checkout/shipping-recipes.md) for more delivery choices.
- [The worked tax example](checkout/tax-example.md) to practice destination rules.
- [International shops](general/international.md) for additional languages, currencies, or markets.

If one of these is essential to your shop, complete it before launch and repeat the affected checkout tests.

## Before accepting customers

Finish the [launch checklist](../getting-started/launch.md). After launch, use [Daily use](../usage/index.md) for product editing and order processing. Return to Shop setup when the business needs a configuration change.

## Configuration versus daily work

Creating a product type is setup work. Adding another T-shirt of that type is daily work. Defining which shipping statuses may follow each other is setup. Marking a particular order as shipped is daily work.

Restrict configuration access to people who understand these wider effects. A change to a shared tax class, attribute, or store configuration can affect many products and future carts.

## Names and labels

Many records have both a name and a label. Use names that staff can recognize, such as “Domestic parcel, standard tariff”. Use customer-facing labels that make a clear promise, such as “Standard delivery”. Avoid putting internal identifiers in the customer's choices.

## Validate one change at a time

After creating a record, select it wherever it is used and test the relevant frontend behavior. A method can exist but remain unavailable because it is disabled, unselected in the active configuration, or excluded by a rule.
