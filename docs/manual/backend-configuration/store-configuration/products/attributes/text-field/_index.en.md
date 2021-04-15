---
title: 'Text field'
description: 'The shop configuration - text field.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/text-field/
weight: 100
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Attribute Name &amp; Type

<table><thead><tr><th>Setting</th> <th>Default</th> <th>Description</th> </tr></thead><tbody><tr><td>Selectable by the customer</td> <td>-</td> <td>You must select this field if the customer should be able to make an entry in the frontend.</td></tr></tbody></table>

## Description

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Description</td> <td>-</td> <td>This description serves as a hint to the backend user and is displayed below the input field.</td></tr></tbody></table>

## Attribute Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Minimum length</td> <td>0</td> <td>{{< version-tag "2.2" >}} Here you can require a minimum number of characters.</td> </tr><tr><td>Maximum length</td> <td>0</td> <td>Here you can limit the field length to a certain number of characters.</td> </tr><tr><td>Input check</td> <td>-</td> <td>The individual options can be found in the following table `Eingabeprüfung`.</td> </tr><tr><td>Placeholder</td> <td>-</td> <td>{{< version-tag "2.2" >}} Here you can define a HTML5 placeholder for the field.</td> </tr><tr><td>Mandatory field</td> <td>-</td> <td>If `Durch den Kunden auswählbar` is selected, the product cannot be added to the shopping cart without this information. Otherwise the field will be displayed as mandatory field in the backend when creating a product.</td> </tr><tr><td>Multilingual</td> <td>-</td> <td>Makes the text field translatable in the backend for a multilingual website.</td> </tr><tr><td>Date selection</td> <td>-</td> <td>Adds a date picker (!\[Datepicker Icon\](datepicker.gif)) to the text field in the backend or frontend.</td></tr></tbody></table>

###  Input validation

<table><thead><tr><th>Input check</th> <th>Description</th> </tr></thead><tbody><tr><td>Numeric characters</td> <td>Allows numeric characters, minus (-), period (.), and space ( ).</td> </tr><tr><td>Alphabetic characters</td> <td>Allows alphabetic characters, minus (-), period (.), and space ( ).</td> </tr><tr><td>Alphanumeric characters</td> <td>Allows alphanumeric characters, minus (-), period (.), and space ( ).</td> </tr><tr><td>Extended alphanumeric characters</td> <td>Allows everything except special characters which are normally encoded for security reasons (#/()&lt;=&gt;).</td> </tr><tr><td>Date</td> <td>Checks if the input conforms to the global date format.</td> </tr><tr><td>Time</td> <td>Checks if the input conforms to the global time format.</td> </tr><tr><td>Date and time</td> <td>Checks whether the input conforms to the global date and time format.</td> </tr><tr><td>Phone number</td> <td>Allows numeric characters, plus (+), minus (-), slash (/), parentheses (), and space ( ).</td> </tr><tr><td>E-mail address</td> <td>Checks if the input is a valid email address.</td> </tr><tr><td>URL format</td> <td>Checks if the input is a valid URL.</td> </tr><tr><td>Price</td> <td>Checks if the input is a valid price.</td> </tr><tr><td>Discount</td> <td>Checks if the input is a valid discount. Example: -10%, -10, +10, +10%.</td> </tr><tr><td>Price surcharge</td> <td>Checks if the input is a valid markup. Example: 10.00, 10%</td></tr></tbody></table>

## Search &amp; Filter Settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Searchable in frontend</td> <td>-</td> <td>Makes the field, if maintained in the backend, searchable by the search engine.</td> </tr><tr><td>Add to "Sort by" option list.</td> <td>-</td> <td>Makes the field, if maintained in the backend and visible to the customer, sortable in the list module.</td> </tr><tr><td>Searchable in the backend</td> <td>-</td> <td>The backend search function will search this field for search terms.</td> </tr><tr><td>Filterable in the backend</td> <td>-</td> <td>Makes the field can be used as a filter in the backend.</td></tr></tbody></table>

The output of the created attribute in the backend is done via the [product types](/de/backend-konfiguration-shop-Produkttypen/). If you made the text field `Durch den Kunden auswählbar` it will be automatically displayed in the frontend (using `$this->options` in the template). Otherwise you can output the attribute in the desired isotope template with the following code `<?php echo $this->generateAttribute('InternerName'); ?>`.
