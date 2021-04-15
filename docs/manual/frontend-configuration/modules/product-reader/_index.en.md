---
title: 'Product reader'
description: 'The Frontend Configuration - Modules - Product Reader'
aliases:
    - /en/frontend-configuration/modules/product-reader/
weight: 110
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Produktleser` is responsible for the output of a single product. It is normally placed together with the [product list](/de/frontend-konfiguration-module-produktliste/) on the same page.

Optionally, the module `Produktleser` can also be placed on a separate page, e.g. product details. For this, the redirection to the details page must be set in the page properties - see " Creating the[page structure"](/de/backend-seitenstruktur/).

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Activate quantity</td> <td>-</td> <td>By default, no quantity can be specified when adding to cart. If this option is enabled, the visitor can specify a quantity.</td> </tr><tr><td>Show a 404 error page</td> <td>-</td> <td>If this option is enabled, the 404 (page not found) page will be displayed if no product alias is found in the URL. Of course, this page must also be created in the page tree. Use this setting if the product reader is used on a separate page that may not be called without product alias or makes no sense that way.</td></tr></tbody></table>

## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>"Add to cart redirect page</td> <td>-</td> <td>If the "Add to Cart" button is enabled and a page is selected here, the visitor will be redirected to the appropriate page after clicking the button.</td></tr></tbody></table>

## Template Settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Product reader template</td> <td>-</td> <td>Here you can select a reader template and change the view as you wish. If you do not select anything here, the template of the respective product type will be selected (recommended). Selection options: - iso\_reader\_default
 
</td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery that will be used to process the product images of the displayed product. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Include news</td> <td>-</td> <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td> </tr><tr><td>Buttons</td> <td>Add to cart</td> <td>Here you can determine which buttons should be displayed in the product reader. You can also determine the order in which the buttons are displayed. Options: - Add to cart
- Update
Add to - favorites
 
</td></tr></tbody></table>
