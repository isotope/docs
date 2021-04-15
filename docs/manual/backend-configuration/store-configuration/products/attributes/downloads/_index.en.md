---
title: Downloads
description: 'The shop configuration - downloads.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/downloads/
weight: 135
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Here you can add an element of the type `Download/Downloads` to your product, e.g. product details as PDF.

## Description

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Description</td> <td>-</td> <td>This description serves as a hint to the backend user and is displayed below the input field.</td></tr></tbody></table>

## Attribute Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Field Type</td> <td>Checkbox</td> <td>Here you can set whether one file (radio button) or multiple files (checkbox) can be selected.</td> </tr><tr><td>Sort by</td> <td>Own order</td> <td>Here you can select a sort order for the output in the fontend, the following are available. When selecting `Eigene Reihenfolge` you can change the order by drag &amp; drop when <docrobot_route name="product-management">creating the product</docrobot_route> in the backend. - Own order
- File name (ascending)
- File name (descending)
- Date (ascending)
- Date (descending)
- Random order
 
</td> </tr><tr><td>Base Directory</td> <td>-</td> <td>Specify here from which directory the folder structure should be displayed.</td> </tr><tr><td>Mandatory field</td> <td>-</td> <td>Here you can make the field mandatory in the backend.</td> </tr><tr><td>Multilingual</td> <td>-</td> <td>Select if this attribute needs to be translated into other languages (e.g. text fields).</td> </tr><tr><td>Show files</td> <td>-</td> <td>If you select this, files and not only folders will be displayed.</td> </tr><tr><td>Mark as gallery</td> <td>-</td> <td>Allows for a better view in the backend.</td></tr></tbody></table>

The output of the created attribute in the backend is done via the [product types](/de/backend-konfiguration-shop-Produkttypen/). In the fontend you can output the attribute in the desired isotope template with the following code `<?php echo $this->generateAttribute('InternerName'); ?>`.
