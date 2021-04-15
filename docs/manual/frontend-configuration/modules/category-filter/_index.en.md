---
title: 'Category filter'
description: 'The Frontend Configuration - Modules - Category Filter'
aliases:
    - /en/frontend-configuration/modules/category-filter/
weight: 140
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{< version "2.6" >}}

The module `Kategorie-Filter` allows to filter products by categories.

## Menu configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Start level</td> <td>0</td> <td>If you enter a value greater than 0 here, only the submenu items from this level are displayed.</td> </tr><tr><td>Stop level</td> <td>0</td> <td>If you enter a value greater than 0 here, you can limit the nesting depth of the menu to this level.</td> </tr><tr><td>Show protected pages</td> <td>-</td> <td>Here you can display menu items that are otherwise only visible to logged-in users.</td> </tr><tr><td>Show hidden pages</td> <td>-</td> <td>Here you can display menu items that are otherwise not visible in the navigation.</td> </tr></tbody></table>

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Set a reference page</td> <td>-</td> <td>Here you can assign an individual source or target page to the module.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can overwrite the default template.</td> </tr><tr><td>Navigation template</td> <td>nav\_default</td> <td>Here you can select a navigation template and change the view as you like. If you do not select anything here, the template of the respective product type will be selected (recommended). Selection options: - nav\_default
- nav\_dropdown
 
</td> </tr><tr><td>Hide for product view</td> <td>-</td> <td>This option hides the product list if a product alias is found in the URL.</td> </tr><tr><td>Include news</td> <td>-</td> <td>Enabling this option will allow the module to display errors, notices or confirmations that the visitor should see.</td> </tr><tr><td>Hide on product view</td> <td>-</td> <td>If enabled, the list will be hidden if a product alias is found in the URL.</td></tr></tbody></table>
