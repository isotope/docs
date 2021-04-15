---
title: Favorites
description: 'The Frontend Configuration - Modules - Favorites'
aliases:
    - /en/frontend-configuration/modules/favorites/
weight: 115
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
 This feature is new in Isotope eCommerce 2.4 Imagine your customer wants to pre-select some products from your extensive assortment and then conveniently order them from a list. You set up this new feature as follows: In the[Product List](/de/frontend-konfiguration-module-produktliste/) and [Product Reader](/de/frontend-konfiguration-module-Produktleser/) modules, you can now activate a "Add to Favorites" button in addition to "Update", "Add to Cart."
{{% /notice %}}

{{% notice warning %}}
 Only works if the customer is logged in to the frontend. 
{{% /notice %}}

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Product collection template</td> <td>iso\_collection\_default</td> <td>Here you can select a collection template and change the view as you like. Selection options: - iso\_collection\_default
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

price (descending) </td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery with which the product images of the favorites list will be processed. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Include news</td> <td>-</td> <td>If this option is checked, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td> </tr><tr><td>Specify empty message</td> <td>-</td> <td>If no products were found (either because there are none or because the filter does not apply), the default message can be conveniently overwritten here.</td></tr></tbody></table>
