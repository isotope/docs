# Our example shop: Trail Supply

Trail Supply sells clothing. Throughout the manual, you work with the same small catalog so you can concentrate on learning Isotope.

You do not need to sell these products yourself. Use the examples on a test website, then apply the same ideas to your own catalog.

## Start with the Trail T-shirt

| Setting | Example value |
| --- | --- |
| Shop name | Trail Supply |
| Store configuration | Trail Supply domestic |
| Product | Trail T-shirt |
| Category page | T-shirts |
| Product type for the first exercise | Clothing |
| First sellable item | Blue, size M |
| SKU | `TSHIRT-BLUE-M` |
| Currency | EUR |
| Entered price | 22.00, including the fictional 10% example tax |
| Price display | Gross |
| Tax class | Standard goods |
| Shipping method | Standard delivery |
| Shipping charge | 5.50, including the same example tax |
| Learning payment method | Test payment, using the Cash type |

An **SKU** is your internal item identifier. A **gross price** includes tax. The [tax chapter](prices-and-taxes.md) explains the calculation before you configure it.

**All tax percentages here are fictional teaching values.** The currency does not imply a country's tax policy. For your real shop, use the treatment and rates appropriate to your business.

Choose one country you can recognize as the domestic test destination. Use that country consistently for the store's defaults and allowed addresses. The international tax exercise calls it A and introduces a second destination B.

## Grow the same product step by step

In [Your first shop](../getting-started/first-shop.md), the Trail T-shirt has one fixed size and color. You state those in its description and sell it as a simple product. There are no size or color selectors yet.

When you reach [Variants](../usage/variants.md), you offer Blue and Black in S, M, and L. Each sellable combination gets its own SKU, such as `TSHIRT-BLACK-L`. The ordinary price stays 22.00 for every combination.

A customer-defined **Printed name** field later lets a buyer request “Sam” on the T-shirt. It illustrates collecting text, without adding a fee in our example.

The quantity-pricing exercise uses these prices for the same T-shirt:

| Quantity from | Gross unit price |
| --- | ---: |
| 1 | 22.00 |
| 5 | 19.80 |
| 10 | 17.60 |

A separate trade-customer exercise uses 17.60 from quantity 1. Each exercise says when to enable these prices. They are not already active in the first-shop walkthrough.

## Two supporting products

| Product | Used to explain |
| --- | --- |
| Trail hoodie | Related products and a basket containing different product lines |
| Garment wash, 250 ml at 6.60 or 500 ml at 11.00 | Comparison prices per 100 ml |

The hoodie belongs on a Hoodies category page. Garment wash belongs on Clothing care. These are optional additions after the T-shirt checkout works.

## The first order's expected total

| Part | Net | Example tax | Gross |
| --- | ---: | ---: | ---: |
| One Trail T-shirt | 20.00 | 2.00 | 22.00 |
| Standard delivery | 5.00 | 0.50 | 5.50 |
| Total | 25.00 | 2.50 | 27.50 |

Later tax examples change one condition at a time and explain the new result. For example, a different applicable rate can change the gross price while leaving the T-shirt's net amount at 20.00.

Next: [Install Isotope](../getting-started/installation.md), or continue with [Your first shop](../getting-started/first-shop.md) if it is already installed.
