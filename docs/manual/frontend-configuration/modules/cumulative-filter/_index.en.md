---
title: 'Restrictive filter'
description: 'The frontend configuration - Modules - Restrictive filter'
aliases:
    - /en/frontend-configuration/modules/cumulative-filter/
weight: 135
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The `einschränkende Filter` generates a navigation from the selected filter attributes, with which a product list can be restricted.

## Example

As an example we use a music store that sells guitars online. The guitars in this case differ by the following attributes with their respective options:

- Type
  - acoustic
  - electronic
- Manufacturer
  - Alhambra
  - Cort
  - Fender
  - Gibson
  - Taylor

With `einschränkenden Filter` you can now generate a navigation menu with the tree structure just shown. Here all options (i.e. level 2) are clickable.

{{% notice info %}}
 Starting with Isotope eCommerce 2.3 only those options are displayed which have a product assigned to them. In addition, the number of hits will be displayed in parentheses. Example: "Taylor (42)"
{{% /notice %}}

The visitor can now, by clicking on "acoustic", display a list of all acoustic guitars. If he then clicks on "Cort", the result is further restricted (therefore `einschränkender Filter`) and now only shows all acoustic guitars from Cort.

{{% notice info %}}
 You can now configure for each attribute whether a multiple selection of the field should lead to an AND or OR search. You can now configure whether and how a number display should be shown: " Show difference**"** shows the difference of how many products are added to the list when the option is clicked. This display primarily makes sense with an OR filter, since an AND filter would lead to a negative number. "Show**total"** shows how many products will appear in total in the list after clicking the option. Do not show"**corresponds to** the previous behavior and does not show a number.
{{% /notice %}}

![The settings for the attributes](attribute-config.png)

## Module configuration

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
        <td>Category Application Area</td>
        <td>Active category</td>
        <td>{{< version-tag "2.3" >}} Each individual option is described in Contao's internal helpwizard (!\[Helpwizard Icon">).</td>
    </tr>
    <tr>
        <td>Condition</td>
        <td>-</td>
        <td>{{< version-tag "2.3" >}} Here you can enter your own SQL conditions, which will be appended to the corresponding query and executed.</td>
    </tr>
    <tr>
        <td>Filtering for new products</td>
        <td>Show all products</td>
        <td>If you have configured the ability in your store to mark products as "new", you can either filter for old, new or all products.
            <br>Choice options:
            <ul>
                <li>Show all products</li>
                <li>Show only the new products</li>
                <li>Show old products</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Filter configuration</td>
        <td>-</td>
        <td>Here you can configure the fields of the restricting filter.
            <table>
                <tbody>
                <tr>
                    <td>Attributes</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td>Query Type</td>
                    <td>"AND" or "OR"</td>
                </tr>
                <tr>
                    <td>Number of Results</td>
                    <td>"Don't Show", "Show all" or "Show differences"</td>
                </tr>
                </tbod>
            </table>
        </td>
    </tr>
    <tr>
        <td>Hide individual selections</td>
        <td>-</td>
        <td>Hide fields for the filter when there is only one selection.</td>
    </tr>
    </tbody>
</table> <h2>Template settings</h2>
<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Standard setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Individual template</td>
        <td>-.</td>
        <td>Here you can have the default template overridden.</td>
    </tr>
    <tr>
        <td>Navigationstemplate</td>
        <td>nav\_default</td>
        <td>Here you can select a template for the filter and change the output that way. As explained in the example, this filter generates a navigation, so all navigation templates are available for selection here.</td>
    </tr>
    <tr>
        <td>Include messages</td>
        <td>-</td>
        <td>If this option is enabled, the errors and notices will be output directly in the module and not as a JavaScript overlay.</td>
    </tr>
    <tr>
        <td>Hide on product view</td>
        <td>-</td>
        <td>{{< version-tag "2.3" >}} This option hides the product filter if a product alias is found in the URL.</td>
    </tr>
    </tbody>
</table> <h2>Redirect</h2>
<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Standard setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Redirect-Page</td>
        <td>-</td>
        <td>{{< version-tag "2.3" >}} If you select a page here, the visitor will be redirected to that page when the filter is submitted.
        {{% notice warning %}}<p>Since the filter settings are cached, the placement of the filter is irrelevant. But that changes as soon as you enable search fields. Search queries are not cached and it is therefore necessary that the product filter is included <strong>before the product list on the same page</strong>!</p>{{% /notice %}}
        </td>
    </tr>
    </tbody>
</table> <h2>Reference Page</h2>
<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Standard Setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Setting a Reference Page</td>
        <td>-.</td>
        <td>{{< version-tag "2.3" >}} When you specify a reference page, the "category application area" in the module configuration will refer to the selected reference page rather than the current page. An example could be a "Highlights" page to which certain products are assigned. If you now want to display these on the home page, you select "Active Category" for "Category Application Area" and select the "Highlights" page for the reference page.</td>
    </tr>
    </tbody>
</table></td></tr></tbody></table>
