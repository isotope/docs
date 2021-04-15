---
title: 'File Upload'
description: 'The shop configuration - file upload.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/file-upload/
weight: 140
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

If you want to enable your customer to transfer a file to you, `Datei-Upload` will help you.

## Description

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Description</td> <td>-</td> <td>This description serves as a hint to the backend user and is displayed below the input field.</td></tr></tbody></table>

## Attribute Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Allowed file types</td> <td>jpg,jpeg,gif,png</td> <td>Restrict the allowed file types using a comma-separated list.</td> </tr><tr><td>Maximum length</td> <td>0</td> <td>Here you can limit the field length to a certain number of characters (text) or bytes (file upload).</td> </tr><tr><td>Mandatory field</td> <td>-</td> <td>Here you can make the field in the frontend a mandatory field, so the product cannot be added to the shopping cart without a value.</td></tr></tbody></table>

## Save file

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Save uploaded files</td> <td>-</td> <td>Here you can set that the uploaded file will be moved to a folder on the server.</td> </tr><tr><td>Destination directory</td> <td>files/orders/##document\_number##/##product\_position##\_\_{{flag::##product_name##|standardize}}/##attribute\_field##</td> <td>Here you can specify a target directory in the Contao folder `files` for the file.</td> </tr><tr><td>Target filename</td> <td>\##file\_target##</td> <td>Enter the target filename. Use simple tokens and insert tags to generate a dynamic name.</td></tr></tbody></table>

Creating the attribute in the backend is done via the [product types](/de/backend-konfiguration-shop-Produkttypen/). In the fontend you can output the attribute in the desired isotope template with the following code `<?php echo $this->generateAttribute('InternerName'); ?>`.
