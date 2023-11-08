---
title: 'Related products'
description: 'The Frontend Configuration - Modules - Related Products'
aliases:
    - /en/frontend-configuration/modules/related-products/
weight: 185
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Ähnliche Produkte` displays the similar products of the currently displayed product. The [linked categories](/de/backend-konfiguration-shop-Verkn%C3%BCpfte-Kategorien/) are used as a basis for this module.

Let's assume you have defined a `verknüpfte Kategorie` named `Zubehör`. In the product settings you have selected the products `Kapodaster` as well as `Stimmgabel` for your product `Gitarre` for the `verknüpfte Kategorie` `Zubehör` , so this module can output the two products `Kapodaster` as well as `Stimmgabel`, provided you have selected the category `Zubehör` in the module configuration.

{{% notice info %}}
Since the module `Ähnliche Produkte` is in the end only a <docrobot_route name="product-list">product list</docrobot_route>, we will refrain from documenting all identical settings here.
{{% /notice %}}

## Module Configuration

<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Default setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Linked categories</td>
        <td>-</td>
        <td>Select categories from which to display products.</td>
    </tr>
    <tr>
        <td>Total number of items</td>
        <td>3</td>
        <td>If you enter a number greater than 0, a maximum of this number of products will be listed. This can be useful, for example, to display the latest 4 products on the home page.</td>
    </tr>
    <tr>
        <td>Items per page</td>
        <td>0</td>
        <td>If you don't change anything here, all found products will be displayed on the page without pagination. Otherwise a page break takes place after the entered number of products.</td>
    </tr>
    <tr>
        <td>Condition</td>
        <td>-</td>
        <td>Here you can enter your own SQL conditions, which will be attached to the corresponding query and executed.</td>
    </tr>
    <tr>
        <td>Filtering for new products</td>
        <td>Show all products</td>
        <td>This setting refers to the optional setting for new products in the
            <docrobot_route name="configuration">shop configuration</docrobot_route>
            . For example, if you have set 30 days, you can select "Show only new products" here. If you do this, only products created within the last 30 days will be listed. The option "Show old products" logically refers to the opposite.
        </td>
    </tr>
    <tr>
        <td>Initial sort field</td>
        <td>-</td>
        <td>Here you can set by which product attribute should be sorted on the first page view. Your shop visitor can change the sorting later on his own by using the filter module.
        {{% notice warning %}}<p>If you have sorted the products for a page (category) manually, you may <strong>not</strong> make a selection here!</p>{{% /notice %}} Selection options:
        <ul>
        <li>Added on</li>
        <li>Item number</li>
        <li>Name</li>
        <li>Price</li>
        </ul>
        </td>
    </tr>
    <tr>
        <td>Initial sort direction</td>
        <td>Downwards</td>
        <td>
        If you have selected a sort field, you can determine here whether it should be sorted upwards or downwards.
        Selection options:
        <ul>
        <li>Downwards</li>
        <li>Upwards</li>
        </ul>
        </td>
    </tr>
    </tbody>
</table>

## Forwarding

<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Default setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>"Add to cart forwarding page</td>
        <td>-</td>
        <td>This setting specifies which page - other than the currently active one - the visitor will be redirected to when adding a product to the cart.</td>
    </tr>
    </tbody>
</table>

## Template settings

<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Default setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Individual template</td>
        <td>-</td>
        <td>Here you can overwrite the default template.</td>
    </tr>
    <tr>
        <td>Product List Template</td>
        <td>-</td>
        <td>Here you can select a list template and change the view as you like. If you don't select anything here, the template of the respective product type will be chosen (recommended). Selection options:
            <ul>
            <li>iso_list_default</li>
            <li>iso_list_variants</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Gallery</td>
        <td>-</td>
        <td>Here you can select the gallery with which the product images of the product list will be processed. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td>
    </tr>
    <tr>
        <td>Columns</td>
        <td>1</td>
        <td>This option allows you to customize the generation of CSS classes. Depending on the setting, the classes <code>row_</code>, <code>col_</code> or <code>odd</code> and <code>even</code> will be adjusted and allow you individual styling.</td>
    </tr>
    <tr>
        <td>Enable set</td>
        <td>-</td>
        <td>By default, no quantity can be specified when adding to cart. If this option is enabled, the visitor can specify a quantity.</td>
    </tr>
    <tr>
        <td>Include messages</td>
        <td>-</td>
        <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td>
    </tr>
    <tr>
        <td>Specify empty message</td>
        <td>-</td>
        <td>If no products were found (either because there are none or because the filter does not apply) the default message can be conveniently overwritten here.</td>
    </tr>
    <tr>
        <td>Buttons</td>
        <td>Add to cart</td>
        <td>Here you can determine which buttons should be displayed in the list. For example, if you only want to allow adding to the shopping cart in the product reader, you do not activate the "Add to cart" button here. You can also determine the order in which the buttons are displayed. Options: - Add to cart
            - Update
            Add to - favorites
        </td>
    </tr>
    </tbody>
</table>
