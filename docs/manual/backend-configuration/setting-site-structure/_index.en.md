---
title: 'Creating the page structure'
description: 'The creation of the page structure.'
aliases:
    - /en/backend-configuration/setting-site-structure/
weight: 10
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

In every shop, regardless of size and product type, at least these pages are required for the system:

- Product overview (product list)
- Product details (product reader)
- Shopping cart
- Legal information (e.g. payment, shipping, AGB)
- Checkout
- Order completed

{{% notice note %}}
Since **Isotope 2.0** the modules `Produktliste` and `Produktleser` can be placed on one page.
{{% /notice %}}

{{% notice warning %}}
When

creating the module `Produktliste` in the template settings, mark **Hide in product view**

, so that the list is not shown in the detail view.
{{% /notice %}}
 If the modules `Produktliste` and `Produktleser` should not be placed together on one page and the `Produktleser` should be moved to a separate page, another page must be created.

- Product details

By default, the module `Produktliste` expects the module `Produktleser` on the same page for the detail link. To override this and redirect to a separate detail page with the module `Produktleser`, the checkbox "Use detail page" must be set in the page properties of the page "Product overview" in the section "Isotope eCommerce" and the detail page must be selected.

If there is to be access protection for the orders, these pages are also required for the members.

- Registration
- Registration successful
- My account
- Order history
- Order details
- Forgotten Password
- Logout

Furthermore, shops often have a search function. For this the search results page is needed.

**Overview of the modules to be integrated into these pages**

<table><thead><tr><th>Page name</th> <th>Module</th> <th>Remarks</th></tr></thead><tbody><tr><td>Product overviewProduct details</td> <td><docrobot_route name="product-list">Product list</docrobot_route> (isotopes <docrobot_route name="product-reader">)Product reader</docrobot_route>(isotopes)</td> <td>Default setting: both modules on one page</td></tr><tr><td>Product reader</td> <td><docrobot_route name="product-reader">Product</docrobot_route> reader (isotopes)</td> <td>Optional: a separate page for the details; set redirection in the page properties of the product page</td></tr><tr><td>Shopping cart</td> <td><docrobot_route name="shopping-cart">Shopping cart</docrobot_route> (Isotopes)</td> <td></td></tr><tr><td>Legal information</td> <td>Content elements `Text` (Contao)</td> <td>e.g. payment, shipping, terms and conditions</td></tr><tr><td>Checkout</td> <td><docrobot_route name="checkout">Checkout</docrobot_route> (Isotope)</td> <td></td></tr><tr><td>Order completed</td> <td><docrobot_route name="order-details">Order details</docrobot_route> (Isotopes )Content elements `Text` (Contao)</td> <td></td></tr><tr><td>Registration</td> <td>Registration (Contao)</td> <td></td></tr><tr><td>Registration successful</td> <td>Content elements `Text` (Contao)</td> <td></td></tr><tr><td>My account</td> <td>Personal data (Contao <docrobot_route name="order-history">)Past orders</docrobot_route> (Isotope) Close account (Contao)</td> <td>The modules can be included in Accordion sections.</td></tr><tr><td>Order history</td> <td><docrobot_route name="order-history">Past orders</docrobot_route> (Isotope)</td> <td>If the module is already on the "My Account" page, the separate "Order History" page can be omitted.</td></tr><tr><td>Order details</td> <td><docrobot_route name="order-details">Order details</docrobot_route> (Isotopes)</td> <td></td></tr><tr><td>Forgotten password</td> <td>Forgotten password (Contao)</td> <td></td></tr><tr><td>Logout</td> <td>Automatic logout (Contao)</td> <td></td></tr><tr><td>Search results</td> <td>Search engine (Contao)</td> <td></td></tr></tbody></table>
