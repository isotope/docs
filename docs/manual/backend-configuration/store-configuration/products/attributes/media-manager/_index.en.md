---
title: 'Media management'
description: 'The shop configuration - media management.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/media-manager/
weight: 125
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Description

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Description</td> <td>-</td> <td>This description serves as a hint to the backend user and is displayed below the input field.</td></tr></tbody></table>

## Attribute Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Allowed file types</td> <td>jpg,jpeg,gif,png</td> <td>Here you can enter a comma separated list of allowed file types.</td> </tr><tr><td>Mandatory field</td> <td>-</td> <td>Here you can make the field mandatory in the backend.</td></tr></tbody></table>

The output of the created attribute in the backend is done via the [product types](/de/backend-konfiguration-shop-Produkttypen/). To display the files in the frontend the following code `<?php echo $this->getGallery('InternerName')->generateMainImage(); ?>` at the desired position in the `iso_reader_default.html5` template is sufficient.
