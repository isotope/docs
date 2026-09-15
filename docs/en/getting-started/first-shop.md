# Your first shop: sell a Trail T-shirt

**You will need:** [Isotope installed](installation.md), a working Contao website with a page layout, and administrator access. Use a test site and an email address you control.

**When you finish:** a visitor can buy one Trail T-shirt, and you can find that order in the backend. You will use one currency, one delivery country, and one offline test payment method.

The values below come from [Our example shop](../concepts/example-shop.md). At this stage, the T-shirt is only available in Blue, size M. You will add selectable variants later.

## 1. Create the store configuration

Open **Isotope eCommerce → Configuration → Store configurations** and create **Trail Supply domestic**.

Choose **EUR**, **Gross** price display, and a price factor of `1`. Gross means the displayed amount includes tax.

Choose your domestic test country as both the default billing and shipping country. Explicitly select that same country in the allowed billing and shipping lists. An empty allowed-country list permits every country.

Enable the address fields you need, including name, street, postal code, city, country, and email. Make the billing email mandatory so the test order has a contact address. Save the configuration.

In Contao's page structure, select this store configuration for your website root. Use one store ID for this test shop.

**Check:** your configuration is saved and assigned to the website. The shipping and payment selections can remain empty until you create those methods in step 6.

## 2. Set up the example tax

The T-shirt costs **22.00 including a fictional 10% tax**. Its net amount is 20.00 and the tax is 2.00. Read [Prices and taxes](../concepts/prices-and-taxes.md) if the distinction is new to you.

1. In **Configuration → Tax rates**, create **Example standard 10%**.
2. Enter rate `10` and a label such as “Example tax 10%”. Leave its rule empty for this single-country exercise.
3. In **Configuration → Tax classes**, create **Standard goods**.
4. Select Example standard 10% as **Tax rate included with product price**.
5. Leave **Apply tax rates** empty and save. The included rate already applies, so it should not be selected again.

You will assign Standard goods to both the T-shirt and delivery charge in this exercise. This fictional rate and treatment are for learning. Use the appropriate tax configuration for your business before launch.

**Check:** both records exist. The tax class identifies the percentage already included in the prices you will enter.

## 3. Prepare the product type and gallery

Create a gallery under **Configuration → Galleries** and call it **Clothing images**. Select a gallery type, choose an image size suited to the site layout, and save.

Under **Configuration → Product types**, create **Clothing**. Use the standard product class offered by the installation. Enable the fields needed for name, SKU, description, price, images, and publishing. Include shipping weight if your later delivery methods will use it.

Leave variants and advanced pricing disabled. Choose the supplied list and reader templates and the Clothing images gallery. A product type is the reusable editing setup for products like this T-shirt.

**Check:** save a draft product with type Clothing and confirm the required fields appear. You can use that draft in step 5.

## 4. Create the shop pages

In Contao's page structure, create these regular pages under the website root. Give each an article and publish it using your existing page layout.

| Page | Content elements to add |
| --- | --- |
| T-shirts | Product list and Product reader |
| Cart | Cart |
| Checkout | Checkout |
| Order details | Order details |

A content element is a block inside an article. In the element's type selection, use the matching Isotope element.

On T-shirts, choose the page's current-page reader mode. In the product list, use the current category scope and enable **Hide in reader mode**. The list shows available products, while the reader shows the selected product. Keep the **Add to cart** button selected on the reader.

Keep Order details out of ordinary navigation. Customers reach it through their individual order link.

**Check:** you can open T-shirts and Cart as a visitor. An empty product list and empty cart are expected until you add the product.

## 5. Add the Trail T-shirt

Open **Products** and edit your draft or create a product with type Clothing.

| Field | Enter |
| --- | --- |
| Name | Trail T-shirt |
| SKU | `TSHIRT-BLUE-M` |
| Description | Cotton T-shirt, Blue, size M. One T-shirt is included. |
| Price | `22.00` |
| Tax class | Standard goods |
| Categories | T-shirts |

Add a photograph, save it, and publish the product. Leave start and stop dates empty for this exercise.

**Check:** the T-shirt appears on the category page, opens in the reader, and shows 22.00 EUR. Its size and color are stated in the description. It does not need selection fields yet.

## 6. Add delivery and test payment

In **Configuration → Shipping methods**, create **Standard delivery**. Choose the flat shipping type, flat calculation, a price of `5.50`, and tax class Standard goods. Enable and save it.

In **Configuration → Payment methods**, choose **Cash** and label the method **Test payment**. Select **Processing** for payment in progress from the supplied payment statuses. Leave any payment fee empty. Add the note “This is a test order. No money will be collected.” Enable and save the method.

The Cash type lets you practice an offline payment workflow. It does not take money or check a bank account.

Return to **Store configurations → Trail Supply domestic** and select Standard delivery and Test payment. Save.

**Check:** both methods are enabled and selected in the configuration. You will see them at checkout once the pages are connected.

## 7. Connect the pages

In the product reader, set **Add product jump to page** to Cart so the customer has a route to the basket. Set its checkout destination to Checkout.

In the Cart element, select Checkout as the checkout destination. In the Checkout element, select guest checkout and set the completed-order destination to Order details. Keep the address, shipping, and payment steps visible for this first test.

The Order details page needs its Isotope element. It displays the purchase and continues payment handling after the order is placed.

**Check:** add the T-shirt and open Cart. From there, the checkout link should open Checkout.

## 8. Place the test order

Use a separate visitor session. Buy one T-shirt, enter fictional address details in your selected test country, and use your own email address. Choose Standard delivery and Test payment.

The summary should show:

| Part | Gross amount |
| --- | ---: |
| One Trail T-shirt | 22.00 EUR |
| Standard delivery | 5.50 EUR |
| Total | 27.50 EUR |

The total contains 2.50 EUR of example tax. There is no payment fee. If the figures differ, check the tax class, prices, configuration, and selected methods before placing the order.

Submit the order once. You should reach its details page and see an order reference.

**Check:** the details match your selection. The payment status can be Processing because this test method has not collected money.

## 9. Find the order as a shop owner

In the backend, open **Orders** and find the test order. Check the T-shirt SKU, quantity, addresses, total, and the separate order, payment, and shipping statuses.

This confirms that the purchase reached the shop. The separate [Processing orders](../usage/orders.md) chapter explains the daily routine of checking payment and preparing delivery.

## 10. Finish preparing the shop

Set up an [order confirmation](../setup/general/notifications.md), select it in the checkout element, and place another test order to check delivery and wording.

Then use [Shop setup](../setup/index.md) for the features you need, such as selectable sizes and colors, real payment methods, or documents. Work through [Before you open the shop](launch.md) before accepting real purchases.

After launch, use **[Daily use](../usage/index.md)** for adding products, changing prices, and processing orders. You do not need to repeat this installation walkthrough for those tasks.
