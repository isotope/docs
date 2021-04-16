---
title: 'Product list'
description: 'The frontend configuration - Modules - Product list'
aliases:
    - /en/frontend-configuration/modules/product-list/
weight: 100
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Produktliste` is responsible for the output of products. It offers a variety of settings which are described below.

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Total number of posts</td> <td>3</td> <td>If you enter a number greater than 0, a maximum of this number of products will be listed. This can be useful, for example, to show the latest 4 products on the home page.</td> </tr><tr><td>Items per page</td> <td>0</td> <td>If you don't change anything here, all found products will be displayed on the page without pagination. Otherwise a page break will take place after the entered number of products.</td> </tr><tr><td>Category application area</td> <td>Active category</td> <td>Every single option is described in the Contao internal Helpwizard (<img src="/de/images/helpwizard.gif?classes=icon">).</td> </tr><tr><td>Condition</td> <td>-</td> <td>Here you can enter your own SQL conditions, which will be attached to the corresponding query and executed.</td> </tr><tr><td>Filtering for new products</td> <td>Show all products</td> <td>This setting refers to the optional setting for new products in the shop configuration. For example, if you have set 30 days, you can select "Show only new products" here. If you do this, only products created within the last 30 days will be listed. The option "Show old products" logically refers to the opposite.</td> </tr><tr><td>Filter modules</td> <td>-</td> <td>Since you are potentially using multiple filter modules and product lists on a page, you can select here which filter modules the product list should respond to.</td> </tr><tr><td>Initial sort field</td> <td>-</td> <td>Here you can set by which product attribute the product list should be sorted on the first page load. Your shop visitor can change the sorting later on his own by the filter module. {{% notice warning %}}If you have manually sorted the products for a page (category), you may **not** make a selection here!
{{% /notice %}}
 Selection options: - Added on
- Item number
- Name
- Price
 
</td> </tr><tr><td>Initial sort direction</td> <td>Downwards</td> <td>If you have selected a sort field, you can determine here whether it should be sorted upwards or downwards. Selection options: - Downwards
- Upwards
 
</td></tr></tbody></table>

{{% notice warning %}}
Sorting by `Preis` is an extremely time-consuming process. Isotope eCommerce knows the possibility to adjust the price based on rules and it is therefore not possible to pre-filter the products already on the database. Therefore, in such a case, Isotope eCommerce must first load **all the** products from the database and then sort them at PHP level! See also chapter [Performance](/de/performance/).
{{% /notice %}}

## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>"Add to cart forwarding page.</td> <td>-</td> <td>If the "Add to Cart" button is enabled in the product list and a page is selected here, the visitor will be redirected to the corresponding page after clicking the button.</td> </tr><tr><td>Forward to first product</td> <td>-</td> <td>If this option has been activated, the first product is automatically loaded when the page is called up. This makes it possible to place the product list and the product reader on the same page and to display the first product of the list directly in the product reader when the page is called up.</td></tr></tbody></table>

## Reference page

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Set a reference page</td> <td>-</td> <td>When you specify a reference page, the "Category Application Area" in the module configuration refers to the selected reference page rather than the current page. An example could be a "Highlights" page to which certain products are assigned. If you now want to display these on the start page, you select the "Active category" for the "Category application area" and select the "Highlights" page for the reference page.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can overwrite the default template.</td> </tr><tr><td>Product list template</td> <td>iso\_list\_default</td> <td>Here you can select a list template and change the view as you like. If you do not select anything here, the template of the respective product type will be selected (recommended). Selection options: - iso\_list\_default
- iso\_list\_variants
 
</td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery with which the product images of the product list will be processed. If you don't select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Columns</td> <td>1</td> <td>This option allows you to customize the generation of the CSS classes. Depending on the setting, the classes 'row\_', 'col\_' or 'odd' and 'even' will be adjusted and allow you individual styling.</td> </tr><tr><td>Enable set</td> <td>-</td> <td>By default, no quantity can be specified when adding to cart. If this option is activated, the visitor can specify a quantity.</td> </tr><tr><td>Hide on product view</td> <td>-</td> <td>This option hides the product list if a product alias is found in the URL.</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is enabled, the errors and notices will be displayed directly in the module and not as a JavaScript overlay.</td> </tr><tr><td>Specify empty message</td> <td>-</td> <td>If no products were found (either because there are none or because the filter does not apply) the default message can be conveniently overridden here.</td> </tr><tr><td>Define a message if no filter is set</td> <td>-</td> <td>If no filter is set yet, a message can be entered here by default. This makes it possible not to display all products at once when the page is loaded for the first time, but to first display the message entered here before the visitor then activates a filter. This can be particularly useful if a large number of products are assigned to a page/category and it does not make sense to display all products without a filter restriction.</td> </tr><tr><td>Buttons</td> <td>Add to shopping cart</td> <td>Here you can determine which buttons should be displayed in the list. For example, if you only want to allow adding to the shopping cart in the product reader, you do not activate the "Add to cart" button here. You can also determine the order in which the buttons are displayed. Selection options: - Add to cart
- Update
 
Add to - favorites
 
</td></tr></tbody></table>
