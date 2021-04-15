---
title: 'Product filter'
description: 'The Frontend Configuration - Modules - Product Filters'
aliases:
    - /en/frontend-configuration/modules/product-filter/
weight: 130
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Produktfilter` is responsible for the output of filter settings. These are subsequently applied to the modules `Produktliste`, provided they have been activated there (see corresponding [documentation](/de/frontend-konfiguration-module-produktliste/)for more information).

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Category Application Area</td> <td>Active category</td> <td>Each individual option is described in the Contao internal helpwizard (!\[Helpwizard Icon\](helpwizard.gif)).</td> </tr><tr><td>Condition</td> <td>-</td> <td>Here you can enter your own SQL conditions, which will be attached to the corresponding query and executed.</td> </tr><tr><td>Filtering for new products</td> <td>Show all products</td> <td>If you have configured the possibility to mark products as "new" in your shop, you can filter either for old, new or for all products. Options: - Show all products Show
- only new
products Show - old

products </td> </tr><tr><td>Activate "per page" limit</td> <td>-</td> <td>If you check this box, you can give the visitor a dropdown with "per page" options. He can decide how many products he wants to see at once.</td> </tr><tr><td>"Per page" options</td> <td>8,12,32,64</td> <td>If you have set the checkbox for "Per page" limit, you can enter a comma-separated list of possible options here. A dropdown will then be generated from these.</td> </tr><tr><td>Activated filters</td> <td>-</td> <td>Here you determine which product attributes the visitor can filter by. Only those that have been activated for "Frontend filtering" are available. Please refer <docrobot_route name="attributes">to the chapter on product attributes</docrobot_route>.</td> </tr><tr><td>Hide single selections</td> <td>-</td> <td>If you check this box, filters will be hidden if there is only one possible option.</td> </tr><tr><td>Enabled search fields</td> <td>-</td> <td>Here you determine which product attributes the visitor can search for. Only those that have been marked as searchable in the frontend are available. Please refer <docrobot_route name="attributes">to the chapter on product attributes</docrobot_route> for more information. Selection options: - Item number
- Name
- Teaser
- Description

</td> </tr><tr><td>Redirect exact match</td> <td>-</td> <td> {{< version-tag "2.6" >}} The customer will be redirected to the product details if the keyword search in one of these fields is an exact match (e.g. search by item number). </td> </tr><tr><td>Search field with autocomplete</td> <td>-</td> <td>If you activate this function, the search field will be autocompleted with the product attribute selected here. For example, if you select "Name" and have two products whose names begin with "Guitar", typing "Git" into the search field will display a selection of the two products. {{% notice warning %}}
Use this function with caution. Autocomplete is not a high-performance operation, so you should **never**
 enable it for filters that search a large number of products.
{{% /notice %}}
 Selection options: - Item
- name
- Teaser
- Description

</td> </tr><tr><td>Enabled sort fields</td> <td>-</td> <td>Here you determine by which product attributes the visitor can sort. Only those are available which have been activated for the "Frontend sorting". Please refer <docrobot_route name="attributes">to the chapter on product attributes</docrobot_route>. Selection options: - Added on
- Item number
- Name
- Price

</td> </tr><tr><td>Initial sort field</td> <td>-</td> <td>This setting determines which of the activated sort fields should be preselected when the product filter is first loaded. Sensibly, this coincides with the <docrobot_route name="product-list">product list</docrobot_route> settings. However, since a product filter can apply to multiple product lists, you will need to choose the correct setting for you. Selection options: - Added on
- Item number
- Name
- Price

</td> </tr><tr><td>Initial sort direction</td> <td>Downwards</td> <td>This setting determines the initial sort direction for the selected "Initial Sort Field". Choices: - Downwards

- 

- Upwards

</td></tr></tbody></table>

## Template Settings

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Custom Template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Filter template</td> <td>iso\_filter\_default</td> <td>Here you can select a template for the filter and change the output.</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is enabled, the errors and notices will be output directly in the module and not as a JavaScript overlay.</td> </tr><tr><td>Hide on product view</td> <td>-</td> <td>This option hides the product filter if a product alias is found in the URL.</td></tr></tbody></table>

## Redirect

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Forwarding Page</td> <td>-</td> <td>If you select a page here, the visitor will be redirected to this page when submitting the filter.
{{% notice warning %}}
Since the filter settings are cached, the placement of the filter is irrelevant. However, this changes as soon as you activate search fields. Search queries are not cached and it is therefore necessary to include the product filter **before the product list on the same page**!
{{% /notice %}}

</td> </tr><tr><td>Link to primary URL</td> <td>-</td> <td> {{< version-tag "2.6" >}} Link the product details to the primary URL (canonical) instead of the current category. </td></tr></tbody></table>

## Reference page

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Set a reference page</td> <td>-</td> <td>When you specify a reference page, the "Category Application Area" in the module configuration refers to the selected reference page rather than the current page. An example could be a "Highlights" page to which certain products are assigned. If you now want to display these on the start page, you select the "Active category" for the "Category application area" and select the "Highlights" page for the reference page.</td></tr></tbody></table>
