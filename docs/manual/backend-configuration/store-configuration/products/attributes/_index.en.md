---
title: Attributes
description: 'The shop configuration - attributes.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/
weight: 110
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

In the basic installation Isotope eCommerce already has the most important attributes, which are normally needed for the operation of a shop. If you are still missing attributes for your project, you can create them at `Attribute` and configure them in the[product type](/de/backend-konfiguration-shop-Produkttypen/).

Attributes are additional data fields, which are made available in the backend when the products are entered and can then be displayed in the frontend at the desired location. For example, you can create a color select menu where the customer has to choose a color in the frontend before he can put the product into the shopping cart.

After clicking on `Neues Attribut` you have the following setting options:

## Attribute Name &amp; Type

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Name</td> <td>-</td> <td>Here you give the attribute a meaningful name, this will only be used in the backend.</td> </tr><tr><td>Internal name</td> <td>-</td> <td>Here you determine the name for the database field in the database table `tl_iso_attribute`, this value must be unique.</td> </tr><tr><td>Type</td> <td>-</td> <td>Here you can select the desired field type for an attribute, Isotope eCommerce provides the following types: - Text field
- Textarea
- Select-Menu
- Radio button menu
- Checkbox menu
- Media management
- File tree
- Downloads
- File Upload
- Video/Audio
 
</td> </tr><tr><td>Field group</td> <td>-</td> <td>This sets the grouping for the output in the backend when creating a product. You can assign the following field groups to the attribute: - General Settings
- Meta information
- Price settings
- Inventory settings
- Shipping settings
- Product Option Settings
- File Management
- Expert Settings
- Publishing
 
 !\[fieldgroups when creating a new product\](fieldgroups.png). </td></tr></tbody></table>

The configuration of each field type is discussed in the subsections.

{{% children showhidden="false" %}}
