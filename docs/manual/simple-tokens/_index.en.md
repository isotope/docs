---
title: 'Simple Tokens'
description: 'Simple Tokens.'
aliases:
    - /en/simple-tokens/
weight: 40
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Simple Tokens is probably one of the most underrated features within Contao and is unfortunately only used for the newsletter module.

Simple Tokens are therefore only briefly mentioned in the [official documentation](https://docs.contao.org/manual/de/). In Isotope eCommerce, the tokens are often used because they give you a lot of flexibility. Among other things, they are used here:

- Throughout the [Notification Center](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum/).
- For displaying the addresses of the different countries (e.g. postcode before or after city etc.)
- In the [documents](/de/backend-konfiguration-shop-allgemein-dokumente/), to customize the document title as well as the document filename

{{% notice info %}}
In the notification center, by the way, you can get an autocompleter by simply typing `##`, which will assist you in selecting the tokens.
{{% /notice %}}

Unlike insert tags, simple tokens also support simple if-else queries, which would make it possible to use them in order confirmation emails, for example:

```
{if billing_address_gender=="male"}
Sehr geehrter Herr ##billing_address_lastname##,
{elseif billing_address_gender=="female"}
Sehr geehrte Frau ##billing_address_lastname##,
{else}
Sehr geehrte Damen und Herren,
{endif}
```

## Simple Tokens for the notification type "Isotope eCommerce order status change".

This notification type can be triggered when the status of an order changes, even if it is a brand new order since it is basically nothing more than a change from "no status" to "new" status.

### General tokens for the order

|        Simple Token         |                                             Description                                              |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| <code>##uniqid##</code>              | Unique ID of the order.                                                                              |
| <code>##order_status##</code>        | Description of the current status of the order.                                                      |
| <code>##order_status_old##</code>    | Description of the previous order status. Useful for example for "Order status changed from x to y". |
| <code>##order_status_id##</code>     | ID of the current status of the order.                                                               |
| <code>##order_status_id_old##</code> | ID of the previous status of the order.                                                              |
| <code>##recipient_email##</code>     | The e-mail address of the recipient.                                                                 |
| <code>##order_id##</code>            | The ID of the order.                                                                                 |
| <code>##order_items##</code>         | The number of items (number added up) in the order.                                                  |
| <code>##order_products##</code>      | The number of individual products in the order.                                                      |
| <code>##order_subtotal##</code>      | Subtotal of the order.                                                                               |
| <code>##order_total##</code>         | Total amount of the order.                                                                           |
| <code>##document_number##</code>     | The document number of the order (order number).                                                     |
| <code>##cart_text##</code>           | Order/shopping cart in text format.                                                                  |
| <code>##cart_html##</code>           | Order/shopping cart in HTML.                                                                         |
| <code>##document##</code>            | The document to be attached (e.g. an invoice).                                                       |
| <code>##form_*##</code>             | All fields created in the form generator.                                                            |
| <code>##payment_id##</code>          | ID of the payment type.                                                                              |
| <code>##payment_label##</code>       | Payment type label.                                                                                  |
| <code>##payment_note##</code>        | Note of the payment type.                                                                            |
| <code>##shipping_id##</code>         | ID of the shipping type.                                                                             |
| <code>##shipping_label##</code>      | Shipping type name.                                                                                  |
| <code>##shipping_note##</code>       | Shipping type note.                                                                                  |

### Billing Address Fields

|            Simple Token             |                  Description                   |
|-------------------------------------|------------------------------------------------|
| <code>##billing_address_gender##</code>      | The billing address field for "gender".        |
| <code>##billing_address_salutation##</code>  | The billing address field for "Salutation".    |
| <code>##billing_address_firstname##</code>   | The billing address field for "First Name".    |
| <code>##billing_address_lastname##</code>    | The billing address field for "Last Name".     |
| <code>##billing_address_dateOfBirth##</code> | The billing address field for "Date of birth". |
| <code>##billing_address_company##</code>     | The invoice address field for "Company".       |
| <code>##billing_address_vat_no##</code>      | The invoice address field for "VAT number".    |
| <code>##billing_address_street_1##</code>    | The invoice address field for "Street".        |
| <code>##billing_address_street_2##</code>    | The invoice address field for "Street 2".      |
| <code>##billing_address_street_3##</code>    | The invoice address field for "Street 3".      |
| <code>##billing_address_postal##</code>      | The billing address field for "Postcode".      |
| <code>##billing_address_city##</code>        | The billing address field for "City".          |
| <code>##billing_address_subdivision##</code> | The billing address field for "State".         |
| <code>##billing_address_country##</code>     | The billing address field for "Country".       |
| <code>##billing_address_phone##</code>       | The billing address field for "Phone Number".  |
| <code>##billing_address_email##</code>       | The billing address field for "Email Address". |

### Shipping Address Fields

|             Simple Token             |                   Description                   |
|--------------------------------------|-------------------------------------------------|
| <code>##shipping_address_gender##</code>      | The shipping address field for "Gender".        |
| <code>##shipping_address_salutation##</code>  | The shipping address field for "Salutation".    |
| <code>##shipping_address_firstname##</code>   | The shipping address field for "First Name".    |
| <code>##shipping_address_lastname##</code>    | The shipping address field for "Last Name".     |
| <code>##shipping_address_dateOfBirth##</code> | The shipping address field for "Date of birth". |
| <code>##shipping_address_company##</code>     | The shipping address field for "Company".       |
| <code>##shipping_address_vat_no##</code>      | The shipping address field for "VAT No.".       |
| <code>##shipping_address_street_1##</code>    | The shipping address field for "Street".        |
| <code>##shipping_address_street_2##</code>    | The shipping address field for "Street 2".      |
| <code>##shipping_address_street_3##</code>    | The shipping address field for "Street 3".      |
| <code>##shipping_address_postal##</code>      | The shipping address field for "Postcode".      |
| <code>##shipping_address_city##</code>        | The shipping address field for "City".          |
| <code>##shipping_address_subdivision##</code> | The shipping address field for "State".         |
| <code>##shipping_address_country##</code>     | The shipping address field for "Country".       |
| <code>##shipping_address_phone##</code>       | The shipping address field for "Phone Number".  |
| <code>##shipping_address_email##</code>       | The shipping address field for "Email address". |

### Shop configuration fields

|        Simple Token        |                    Description                    |
|----------------------------|---------------------------------------------------|
| <code>##config_firstname##</code>   | The store configuration field for "First Name".   |
| <code>##config_lastname##</code>    | The shop configuration field for "Last Name".     |
| <code>##config_company##</code>     | The shop configuration field for "Company".       |
| <code>##config_vat_no##</code>      | The shop configuration field for "VAT number".    |
| <code>##config_street_1##</code>    | The shop configuration field for "Street".        |
| <code>##config_street_2##</code>    | The shop configuration field for "Street 2".      |
| <code>##config_street_3##</code>    | The shop configuration field for "Street 3".      |
| <code>##config_postal##</code>      | The shop configuration field for "Postcode".      |
| <code>##config_city##</code>        | The shop configuration field for "City".          |
| <code>##config_subdivision##</code> | The shop configuration field for "State".         |
| <code>##config_country##</code>     | The shop configuration field for "Country".       |
| <code>##config_phone##</code>       | The shop configuration field for "Phone number".  |
| <code>##config_email##</code>       | The shop configuration field for "Email address". |

{{< version "2.6" >}}

|        Simple Token        |                             Description                             |
|----------------------------|---------------------------------------------------------------------|
| <code>##config_bankName##</code>    | The shop configuration field for "Bank Name".                       |
| <code>##config_bankAccount##</code> | The shop configuration field for "Bank account number (e.g. IBAN)". |
| <code>##config_bankCode##</code>    | The shop configuration field for "Bank code (BIC / SWIFT)".         |
| <code>##config_taxNumber##</code>   | The shop configuration field for "Tax number".                      |

### Contao member fields

|        Simple token        |                 Description                  |
|----------------------------|----------------------------------------------|
| <code>##member_firstname##</code>   | The Contao member field for "First name".    |
| <code>##member_lastname##</code>    | The Contao member field for "Last name".     |
| <code>##member_dateOfBirth##</code> | The Contao member field for "Date of birth". |
| <code>##member_gender##</code>      | The Contao member field for "Gender".        |
| <code>##member_company##</code>     | The Contao member field for "Company".       |
| <code>##member_street##</code>      | The Contao member field for "Street".        |
| <code>##member_postal##</code>      | The Contao member field for "Postal code".   |
| <code>##member_city##</code>        | The Contao member field for "City".          |
| <code>##member_state##</code>       | The Contao member field for "State".         |
| <code>##member_country##</code>     | The Contao member field for "Country".       |
| <code>##member_phone##</code>       | The Contao member field for "Phone number".  |
| <code>##member_mobile##</code>      | The Contao member field for "Mobile number". |
| <code>##member_fax##</code>         | The Contao member field for "Fax number".    |
| <code>##member_email##</code>       | The Contao member field for "Email address". |
| <code>##member_website##</code>     | The Contao member field for "Website".       |
| <code>##member_language##</code>    | The Contao member field for "Language".      |
| <code>##member_username##</code>    | The Contao member field for "Username".      |
| <code>##member_dateAdded##</code>   | The Contao member field for "Added on".      |

## Collection fields

|             Simple token             |                                                Description                                                 |
|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| <code>##collection_locked##</code>            | The date of the order. The output is a timestamp and must be formatted using an insert tag.                |
| <code>##collection_document_number##</code>   | The document number of the order.                                                                          |
| <code>##collection_uniqid##</code>            | Unique ID of the order.                                                                                    |
| <code>##collection_date_paid##</code>         | The date on which the order was paid. The output is a timestamp and must be formatted using an insert tag. |
| <code>##collection_date_shipped##</code>      | The date the order was shipped. The output is a timestamp and must be formatted using an insert tag.       |
| <code>##collection_subtotal##</code>          | The subtotal of the order.                                                                                 |
| <code>##collection_tax_free_subtotal##</code> | The subtotal of the order without taxes.                                                                   |
| <code>##collection_total##</code>             | The grand total of the order                                                                               |
| <code>##collection_tax_free_total##</code>    | The grand total of the order without taxes.                                                                |
| <code>##collection_currency##</code>          | The currency of the order.                                                                                 |

## Simple tokens for the notification type
"Isotope eCommerce address book change".

This notification type can be used to send notifications when a member changes their address.

### General Tokens

|    Simple Tokens    |                   Description                   |
|---------------------|-------------------------------------------------|
| <code>##admin_email##</code> | The email address of the website administrator. |
| <code>##domain##</code>      | The domain on which the change was made.        |
| <code>##link##</code>        | The full URL where the change was made.         |

### Address fields

|          Simple Token           |                 Description                 |
|---------------------------------|---------------------------------------------|
| <code>##address_gender##</code>          | The new address field for "Gender".         |
| <code>##address_old_gender##</code>      | The old address field for "Gender".         |
| <code>##address_salutation##</code>      | The new address field for "Salutation".     |
| <code>##address_old_salutation##</code>  | The old address field for "Salutation".     |
| <code>##address_firstname##</code>       | The new address field for "First name".     |
| <code>##address_old_firstname##</code>   | The old address field for "First name".     |
| <code>##address_lastname##</code>        | The new address field for "Last name".      |
| <code>##address_old_lastname##</code>    | The old address field for "Last name".      |
| <code>##address_dateOfBirth##</code>     | The new address field for "Date of birth".  |
| <code>##address_old_dateOfBirth##</code> | The old address field for "Date of birth".  |
| <code>##address_company##</code>         | The new address field for "Company".        |
| <code>##address_old_company##</code>     | The old address field for "Company".        |
| <code>##address_vat_no##</code>          | The new address field for "VAT number".     |
| <code>##address_old_vat_no##</code>      | The old address field for "VAT number".     |
| <code>##address_street_1##</code>        | The new address field for "Street".         |
| <code>##address_old_street_1##</code>    | The old address field for "Street".         |
| <code>##address_street_2##</code>        | The new address field for "Street 2".       |
| <code>##address_old_street_2##</code>    | The old address field for "Street 2".       |
| <code>##address_street_3##</code>        | The new address field for "Street 3".       |
| <code>##address_old_street_3##</code>    | The old address field for "Street 3".       |
| <code>##address_postal##</code>          | The new address field for "Postcode".       |
| <code>##address_old_postal##</code>      | The old address field for "Postal code".    |
| <code>##address_city##</code>            | The new address field for "City".           |
| <code>##address_old_city##</code>        | The old address field for "City".           |
| <code>##address_subdivision##</code>     | The new address field for "State".          |
| <code>##address_old_subdivision##</code> | The old address field for "State".          |
| <code>##address_country##</code>         | The new address field for "Country".        |
| <code>##address_old_country##</code>     | The old address field for "Country".        |
| <code>##address_phone##</code>           | The new address field for "Phone number".   |
| <code>##address_old_phone##</code>       | The old address field for "Phone number".   |
| <code>##address_email##</code>           | The new address field for "E-mail address". |
| <code>##address_old_email##</code>       | The old address field for "E-mail address". |
