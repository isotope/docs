---
title: Documents
description: 'The shop configuration - General settings - Documents.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/documents/
weight: 20
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

In Isotope eCommerce, `Dokumente` is always used to display a collection of products. At the core of Isotope, we are talking about PDF files here. However, it would also be conceivable to support any output format (from `.docx` to `.odt`), provided that the appropriate tools are available on the server.

In the core of Isotope eCommerce, only the document type `Standard` is currently provided. It is similar to the print function for articles of the Contao core: It tries to generate a PDF from HTML code.

You can create as many documents as you like and then select them in other parts of Isotope eCommerce. Conceivable are for example:

- Invoice
- Order confirmation
- Shipping confirmation
- etc.

Since an invoice is desired in most cases, the configuration of such an invoice is illustrated below.

![Example setting for an invoice document](invoice.png)

## Name &amp; Type

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Document Name</td> <td>-</td> <td>Here you can enter an internal name for the document.</td> </tr><tr><td>Document type</td> <td>-</td> <td>Select the desired document type here.</td></tr></tbody></table>

{{% notice info %}}
Your trusted programmer can program document types and make them available for you to choose from here. So if the existing document types are not enough for you, Isotope eCommerce gives you the flexibility to fix that.

{{% /notice %}}
 ## General settings

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Document title</td> <td>-</td> <td>Here you can define the title of the document. It is available in the template as a variable and represents the heading. Use <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> ( `collection_*`), where `*` stands for the row of the database table `tl_iso_product_collection`. A classic example would be the generated document number or in this case the invoice number: `Ihre Rechnung ##collection_document_number##`.</td> </tr><tr><td>Filename</td> <td>-</td> <td>Here you can define the generated filename of the document. Use <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> ( `collection_*`), where `*` stands for the row of the database table `tl_iso_product_collection`. A classic example would be the generated document number or in this case the invoice number: `rechnung_##collection_document_number##`.</td></tr></tbody></table>

## Template

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Document Template</td> <td>-</td> <td>This setting refers to the HTML template around the `Sammlung-Template`. Here you can select a template, in which you place e.g. the invoice address somewhere else or add a logo of your company.</td> </tr><tr><td>Gallery</td> <td>-</td> <td>Here you can select the gallery that will be used to process the product images in the document. If you do not select anything here, the template of the respective product type will be chosen (recommended).</td> </tr><tr><td>Collection template</td> <td>iso\_collection\_invoice</td> <td>Here you can select a product collection template to change the display of the products in your document as you wish. Selection options: - iso\_collection\_default - iso\_collection\_favorites - iso\_collection\_invoice - iso\_collection\_mini 
</td> </tr><tr><td>Sorting</td> <td>added by date (ascending)</td> <td>This selection allows you to determine the order in which the products in this document are listed. Selection options: - added by date (ascending) - added by date (descending) - updated by date (ascending) - updated by date (descending) - by product name (ascending) - by product name (descending) - by price (ascending) - by price 
(descending) </td></tr></tbody></table>
