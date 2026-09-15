# How a shop works

A shop turns a customer's choices into an order you can fulfill. Understanding the objects involved makes the backend much easier to use.

## From catalog to delivery

1. You create a **product**, such as a mug, with a description and price.
2. You assign it to a **category**, such as Drinkware, so customers can find it.
3. A customer opens the product details and chooses any options.
4. Adding it to the **cart** records what they currently want to buy.
5. During **checkout**, the customer supplies addresses and chooses available shipping and payment methods.
6. The customer reviews the totals and places an **order**.
7. Payment is attempted or arranged, depending on the method.
8. You confirm the payment situation, prepare the goods, and record delivery progress.

A cart is provisional. Addresses, quantities, and selected methods can change its totals. An order is a recorded purchase request. Its existence alone does not prove payment has arrived.

## Product, variant, and option

A **product** is an item you describe and offer. A **variant** is a particular version of that item, such as a blue T-shirt in size M. Variants are useful when combinations have their own SKU, price, or other data.

A **customer-defined option** records a customer's input, such as an engraving message. It does not automatically create a separately managed catalog item.

An **attribute** is a field holding information. Color can be a descriptive attribute, a variant choice, or an option depending on how you model the product. A **product type** is the reusable setup that decides which fields and behaviors a family of products has.

## Products and order lines

A cart line normally combines a selected product or variant, its configuration, and a quantity. Three identical mugs can appear as one line with quantity 3. A different engraving can require a separate line even when the underlying product is the same.

This explains why “number of products” and “number of items” can differ. Rules and shipping calculations may count lines or sum quantities. Choose the measurement that matches your business intention.

## Price, tax, and extra charges

The **unit price** is the price of one item. Its quantity produces the line total. Shipping and payment can add separate charges. Taxes describe the tax component of applicable amounts.

A **net price** excludes tax. A **gross price** includes tax. A **tax rate** is a percentage and its conditions. A **tax class** groups the tax treatment you assign to a price. Read [Prices and taxes](prices-and-taxes.md) before entering your catalog.

A **subtotal** and the final total need not be equal. Always show the customer the final amount, currency, and method choices before placing the order.

## Three kinds of progress

| Status | Question it answers | Example |
| --- | --- | --- |
| Order | What is happening to the purchase overall? | Processing |
| Payment | What is happening to the money? | Open or Paid |
| Shipping | What is happening to fulfillment? | Open or Shipped |

An order may be paid but not shipped. A delivered invoice order may still be awaiting payment. Keeping these separate helps staff avoid shipping twice or mistaking an order confirmation for a payment receipt.

Next: [Contao essentials](contao.md) and [Your first shop](../guides/first-shop.md).
