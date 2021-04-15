---
title: 'Order details'
description: 'The frontend configuration - Modules - Order details'
aliases:
    - /en/frontend-configuration/modules/order-details/
weight: 155
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Bestellungsdetails` is responsible for outputting the detailed view of an order. There are two main uses for this module:

- Inclusion on the page after the order has been submitted (e.g. for a print view or simply again as a summary).
- Inclusion on the forwarding page for the module [Past Orders](/de/frontend-konfiguration-module-Vergangene-Bestellungen/)

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Make login required</td> <td>-</td> <td>By default, Isotope eCommerce generates a unique ID that can be used to access the order. This is necessary because guests do not have a login and should still be able to access their own order. If you check this box, a login will be made mandatory for member orders (recommended). {{% notice info %}}It seems questionable why this option is optional to enable in the first place and it is not simply the default behavior of Isotope. This is because this option was only introduced in 2.1 and would have changed the behavior of Isotope compared to 2.0 if it were new by default. For this reason, it must be enabled manually.{{% /notice %}}
</td></tr></tbody></table>

## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Forwarding page for shopping cart</td> <td>-</td> <td>Select here the page to which the visitor will be redirected if he wants to see the complete shopping cart.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Product collection template</td> <td>iso\_collection\_default</td> <td>Here you can select a product collection template and change the display of the products in the order as you wish. Selection options: - iso\_collection\_default
- iso\_collection\_favorites
- iso\_collection\_invoice
- iso\_collection\_mini

</td> </tr><tr><td>Sorting</td> <td>Added by date (ascending)</td> <td>Here you can define in which order the entries of a collection should be listed. Selection options: - by date added (ascending)

by - date added (descending

) by date - updated

(ascending) by date - updated (descending

) by - product name

(ascending) by product - name

- 

(descending) by - price

(ascending) - by

- 

price (descending) </td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery with which the product images of the order will be processed. If you do not select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Include news</td> <td>-</td> <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td></tr></tbody></table>
