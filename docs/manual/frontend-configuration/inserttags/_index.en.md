---
title: InsertTags
description: 'The frontend configuration - InsertTags'
aliases:
    - /en/frontend-configuration/inserttags/
weight: 30
---

Isotope eCommerce offers a variety of InsertTags that you can use in the frontend.

{{< version "2.3" >}}

The InsertTags have been unified in Isotope eCommerce 2.3. It is possible that you are still using old InsertTags. These will still work 
until version 3.0, so choose the appropriate new InsertTag from the list below today!


## InsertTags for the current shopping cart

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{cart::items}}</code></td>
        <td>Returns the number of individual products in the shopping cart. The quantities are ignored here. So if <code>My product 1</code> was 
            added to the cart four times, this InsertTag will only count it once.</td>
    </tr>
    <tr>
        <td><code>{{cart::items_label}}</code></td>
        <td>Returns the number of individual products in the cart including the translation. Example: <code>1 product</code></td>
    </tr>
    <tr>
        <td><code>{{cart::quantity}}</code></td>
        <td>Returns the total number of products in the cart. The quantities are taken into account here. So if <code>My product 1</code> was 
            added to the cart four times, this InsertTag will count it four times.</td>
    </tr>
    <tr>
        <td><code>{{cart::quantity_label}}</code></td>
        <td>Returns the total number of products in the cart including the translation. Example: <code>4 products</code></td>
    </tr>
    <tr>
        <td><code>{{cart::subtotal}}</code></td>
        <td>Returns the subtotal of the shopping cart. This InsertTag also takes taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{cart::taxfree_subtotal}}</code></td>
        <td>Returns the subtotal of the shopping cart. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{cart::total}}</code></td>
        <td>Returns the total of the shopping cart. This InsertTag also takes the taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{cart::taxfree_total}}</code></td>
        <td>Returns the total of the shopping cart. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{cart::billing_address::~}}</code></td>
        <td>Returns a desired field from the billing address of the shopping cart. Example: <code>{{cart::billing_address::firstname}}</code>.</td>
    </tr>
    <tr>
        <td><code>{{cart::shipping_address::~}}</code></td>
        <td>Returns a desired field from the shipping address of the shopping cart. Example: <code>{{cart::shipping_address::firstname}}</code>.</td>
    </tr>
    <tr>
        <td><code>{{cart::~}}</code></td>
        <td>All parameters that do not match one of the previous ones will be searched directly on the database table <code>tl_iso_product_collection</code>, 
            where the placeholder refers to the corresponding column. Use this InsertTag e.g. to get the currency: <code>{{cart::currency}}</code></td>
    </tr>
    </tbody>
</table>


## InsertTags for the current order

{{% notice warning %}}<p>To get the current order, the GET parameter "uid" must be in the URL. This is the case on the order confirmation page, for example. 
It would look something like this: "complete.html?uid=550af3fe73763"</p>{{% /notice %}}

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{order::items}}</code></td>
        <td>Returns the number of individual products in the order. The quantity information is ignored here. So if <code>My product 1</code> was 
            ordered four times, this InsertTag will only count it once.</td>
    </tr>
    <tr>
        <td><code>{{order::items_label}}</code></td>
        <td>Returns the number of individual products in the order including the translation. Example: <code>1 product</code></td>
    </tr>
    <tr>
        <td><code>{{order::quantity}}</code></td>
        <td>Returns the total number of products in the order. The quantity information is included here. So if <code>My product 1</code> was ordered 
            four times, this InsertTag will count it four times.</td>
    </tr>
    <tr>
        <td><code>{{order::quantity_label}}</code></td>
        <td>Returns the total number of products in the order including translation. Example: <code>4 products</code></td>
    </tr>
    <tr>
        <td><code>{{order::subtotal}}</code></td>
        <td>Returns the subtotal of the order. This InsertTag also takes taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{order::taxfree_subtotal}}</code></td>
        <td>Returns the subtotal of the order. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{order::total}}</code></td>
        <td>Returns the total of the order. This InsertTag also takes taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{order::taxfree_total}}</code></td>
        <td>Returns the total of the order. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{order::billing_address::~}}</code></td>
        <td>Returns a desired field from the billing address of the order. Example: <code>{{order::billing_address::firstname}}</code>.</td>
    </tr>
    <tr>
        <td><code>{{order::shipping_address::~}}</code></td>
        <td>Returns a desired field from the shipping address of the order. Example: <code>{{order::shipping_address::firstname}}</code>.</td>
    </tr>
    <tr>
        <td><code>{{order::~}}</code></td>
        <td>All parameters that do not match one of the previous ones will be searched directly on the database table <code>tl_iso_product_collection</code>, 
            where the placeholder refers to the corresponding column. Use this InsertTag e.g. to get the order number: <code>{{order::document_number}}</code></td>
    </tr>
    </tbody>
</table>


{{< version "2.9" >}}

## InsertTags for the current favorites

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{favorites::items}}</code></td>
        <td>Returns the number of individual products in the favorites. The quantity information is ignored here. So if <code>My product 1</code> was 
            ordered four times, this InsertTag will only count it once.</td>
    </tr>
    <tr>
        <td><code>{{favorites::items_label}}</code></td>
        <td>Returns the number of individual products in the favorites including the translation. Example: <code>1 product</code></td>
    </tr>
    <tr>
        <td><code>{{favorites::quantity}}</code></td>
        <td>Returns the total number of products in the favorites The quantity information is included here. So if <code>My product 1</code> was ordered 
            four times, this InsertTag will count it four times.</td>
    </tr>
    <tr>
        <td><code>{{favorites::quantity_label}}</code></td>
        <td>Returns the total number of products in the favorites including translation. Example: <code>4 products</code></td>
    </tr>
    <tr>
        <td><code>{{favorites::subtotal}}</code></td>
        <td>Returns the subtotal of the favorites. This InsertTag also takes taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{favorites::taxfree_subtotal}}</code></td>
        <td>Returns the subtotal of the favorites. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{favorites::total}}</code></td>
        <td>Returns the total of the favorites. This InsertTag also takes taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{favorites::taxfree_total}}</code></td>
        <td>Returns the total of the favorites. This InsertTag does not take taxes into account.</td>
    </tr>
    <tr>
        <td><code>{{favorites::~}}</code></td>
        <td>All parameters that do not match one of the previous ones will be searched directly on the database table <code>tl_iso_product_collection</code>, 
            where the placeholder refers to the corresponding column. Use this InsertTag e.g. to get the order number: <code>{{order::document_number}}</code></td>
    </tr>
    </tbody>
</table>


## Product specific InsertTags

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{product::~}}</code></td>
        <td>Returns a specific attribute of the current product (product alias in the URL). Example: <code>{{product::name}}</code></td>
    </tr>
    <tr>
        <td><code>{{product::~::~}}</code></td>
        <td>Returns a specific attribute of a specific product (product ID). Example: <code>{{product::name::42}}</code></td>
    </tr>
    </tbody>
</table>


## InsertTags for translations.

For more information about translations, we refer you to the corresponding [documentation](/en/backend-configuration/store-configuration/miscellaneous/translations/).

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{isolabel::~}}</code></td>
        <td>Returns the translation of a given string in the language of the current page. Example: <code>{{isolabel::My string}}</code></td>
    </tr>
    <tr>
        <td><code>{{isolabel::~::~}}</code></td>
        <td>Returns the translation of a given string in a given language. Example: <code>{{isolabel::My string::en_US}}</code></td>
    </tr>
    </tbody>
</table>


## Format Simple Token Timestamp with InsertTag.

The following customization of the InsertTag can be used to affect the output of the date and time using the Date function (related link: 
[PHP Date function](http://php.net/manual/de/function.date.php#refsect1-function.date-parameters)):

<table>
    <thead>
    <tr>
        <th>InsertTag</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>{{formatted_datetime::##collection_locked##::<strong>d.m.Y</strong>}}</code></td>
        <td>Enter the desired format using the date function. With <code>d.m.Y</code> the output looks like this <code>01.09.2014</code>.</td>
    </tr>
    <tr>
        <td><code>{{formatted_datetime::##collection_locked##::<strong>date</strong>}}</code></td>
        <td>With <code>date</code> the date format which you have set under settings or in the start point of the page will be used.</td>
    </tr>
    <tr>
        <td><code>{{formatted_datetime::##collection_locked##::<strong>time</strong>}}</code></td>
        <td>With <code>time</code> the time format which you have defined under settings or in the starting point of the page is used.</td>
    </tr>
    <tr>
        <td><code>{{formatted_datetime::##collection_locked##::<strong>datim</strong>}}</code></td>
        <td>With <code>datim</code> the date and time format which you have defined under settings or in the starting point of the page is used.</td>
    </tr>
    </tbody>
</table>
