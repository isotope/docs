---
title: 'Shopping cart'
description: 'The frontend configuration - Modules - Shopping cart'
aliases:
    - /en/frontend-configuration/modules/shopping-cart/
weight: 120
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Warenkorb` is responsible for the output of the current shopping cart for the visitor.

{{% notice info %}}
If your visitors have to log in, Isotope can make an assignment of the shopping cart to the visitor. Therefore, a shopping cart that was never converted into an order can be reloaded on the next visit. For guests this behaviour can logically not be done identically. Isotope sets a [HTTP-Cookie](http://de.wikipedia.org/wiki/HTTP-Cookie) during the visit and tries to recognize the shopping cart at the next visit. How long such a guest shopping cart should be saved can be defined in the system settings at `Zeitlimit für Gäste-Warenkorb`. Isotope automatically cleans up your database at regular intervals and deletes old entries.
{{% /notice %}}

 ## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Forwarding page for shopping cart</td> <td>-</td> <td>This setting specifies which page the user is redirected to when they want to see the full shopping cart. This can be useful if you place multiple shopping carts on one page and have, for example, a "mini shopping cart" to which you want to add a "click here for full view" button.</td> </tr><tr><td>Redirect page for checkout process</td> <td>-</td> <td>If you select a page here, the "continue to checkout" button will appear and then direct the user there as well.</td></tr></tbody></table>

## Template Settings

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Product collection template</td> <td>iso\_collection\_default</td> <td>Here you can select a product collection template and change the display of the products in the shopping cart as you wish. Selection options: - iso\_collection\_default
- iso\_collection\_favorites
- iso\_collection\_invoice
- iso\_collection\_mini

</td> </tr><tr><td>Sorting</td> <td>Added by date (ascending)</td> <td>Here you can define in which order the entries of a collection should be listed. Selection options: - Added by date (ascending)
- Added by date (descending)
- Updated by date (ascending)
- updated by date (descending)
- by product name (ascending)
- by product name (descending)
- by price (ascending)
- by price (descending)

</td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery that will be used to process the product images of the shopping cart. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Activate "Continue shopping" button</td> <td>-</td> <td>Adds a button that redirects the user back to the previously visited page. This button is **only** displayed the first time the user clicks on "add to cart".</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td> </tr><tr><td>Specify empty message</td> <td>-</td> <td>If no products have been added to the cart yet, you can easily override the default message here.</td></tr></tbody></table>
