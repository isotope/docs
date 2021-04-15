---
title: Templates
description: 'The frontend configuration - templates'
aliases:
    - /en/frontend-configuration/templates/
weight: 20
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice warning %}}
Isotope eCommerce delivers since version 2.0 only `.html5`-templates. On the one hand this reduces the maintenance effort and on the other hand there are hardly any reasons why you have to use XHTML. Of course you can overwrite the templates as usual and also create them as `.xhtml`-variant.
{{% /notice %}}

<table>
    <thead>
    <tr>
        <th>Module</th>
        <th>Templates</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>
            <docrobot_route name="product-list">Productlist</docrobot_route>
        </td>
        <td>mod_iso_productlist.html5 mod_iso_productlist_caching.html5 iso_list_default.html5</td>
        <td>Module Template Output when loading a list (Ajax) Defaultoutput of the list</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="product-variant-list">Product variant list</docrobot_route>
        </td>
        <td>mod_iso_productlist.html5 iso_list_variants.html5</td>
        <td>Module Template Output of the list with variants</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="product-reader">Product reader</docrobot_route>
        </td>
        <td>mod_iso_productreader.html5 iso_reader_default.html5</td>
        <td>Module TemplateOutput of the reader page</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="shopping-cart">Shopping cart</docrobot_route>
        </td>
        <td>mod_iso_cart.html5 iso_collection_default.html5 iso_collection_mini.html5</td>
        <td>Module Template Default output of the list Minimized output of the list</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="checkout">Checkout</docrobot_route>
        </td>
        <td>mod_iso_checkout.html5 iso_collection_default.html5 iso_checkout_address.html5 iso_checkout_shipping_method.html5 iso_checkout_payment_method.html5 iso_checkout_order_info.html5 iso_checkout_order_conditions.html5</td>
        <td>Module Template Standard Output of the list Step 1 in the checkout Step 2 inthe checkout Step 3in the checkout Step 4in the checkout Customizing the form</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="product-filter">Product filter</docrobot_route>
        </td>
        <td>iso_filter_default.html5</td>
        <td>Filter output</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="cumulative-filter">Restrictive filter</docrobot_route>
        </td>
        <td>mod_iso_cumulativefilter.html5 nav_default.html5 *Contao*</td>
        <td>Module Template Default Navigation Template</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="order-history">Past orders</docrobot_route>
        </td>
        <td>mod_iso_orderhistory.html5</td>
        <td>Module Template</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="order-details">Order details</docrobot_route>
        </td>
        <td>mod_iso_orderdetails.html5 iso_collection_default.html5</td>
        <td>Module Template Default List Output</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="store-config-switcher">Shop configuration switcher</docrobot_route>
        </td>
        <td>mod_iso_configswitcher.html5</td>
        <td>Module Template</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="address-book">Addressbook</docrobot_route>
        </td>
        <td>mod_iso_addressbook.html5 member_default.html5 *Contao*member_grouped.html5 *Contao*</td>
        <td>Module Template Standard Member List Grouped member list (e.g. personal data, address data etc.)</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="related-products">Related products</docrobot_route>
        </td>
        <td>mod_iso_productlist.html5 iso_list_default.html5</td>
        <td>Module Template Standard Output of the list</td>
    </tr>
    <tr>
        <td>
            <docrobot_route name="messages">Messages</docrobot_route>
        </td>
        <td>mod_iso_messages.html5</td>
        <td>Module Template</td>
    </tr>
    </tbody>
</table>

<table>
    <thead>
    <tr>
        <th>Other</th>
        <th>Templates</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Galleries</td>
        <td>iso_gallery_standard.html5 iso_gallery_inline.html5</td>
        <td>Output of a standard gallery Output ofan inline gallery</td>
    </tr>
    <tr>
        <td>Documents</td>
        <td>iso_document_default.html5</td>
        <td>Output of a document</td>
    </tr>
    </tbody>
</table>
