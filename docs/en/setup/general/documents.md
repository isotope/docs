# Order documents

A document is a generated record associated with an order, such as an invoice or packing document. A document definition describes how to produce it. The generated file belongs to a particular order and has its own creation time and number.

An order number identifies the purchase. A document number identifies a generated document. Keep those roles distinct in your templates and internal procedures.

## Configure a definition

1. Open **Configuration → Documents**.
2. Create a definition and select the available document type.
3. Enter an internal name, document title, and filename pattern.
4. Set a number prefix and minimum number length if required.
5. Choose the template and optional gallery/logo settings supported by the type.
6. Save and preview it against a representative test order.

A filename pattern can use supported collection tokens, such as the documented `invoice_##collection_document_number##` pattern. Verify the actual preview and generated filename in your release. Do not assume notification tokens work identically in every document field.

## Preview versus create

Preview is for checking appearance and content. Creating a document assigns a document number and stores the generated file with the order.

Use preview while adjusting the template. Repeatedly creating documents to test a layout can create extra numbered records. Establish when staff should create the final version and how corrections are handled.

Generated files need to be included in backups together with their database records. A database row alone is not the stored document contents.

## Choose the output format

The Standard document type produces **HTML**. Confirm that this format fits how staff and customers will use the document.

If your workflow needs PDF files, ask your maintainer to configure a compatible PDF document type. Test fonts, page breaks, and attachments before using it for customer documents.

## Check representative orders

Preview a short order, a long order, long addresses, variants, customer options, discounts if implemented, mixed taxes, and shipping charges. Check that the document title and totals describe the intended document rather than inheriting misleading wording.

Arrange review of the required business information and numbering policy for your shop. The existence of an invoice template does not establish its suitability for every business.

## Attaching documents

Notification support depends on the chosen notification and document integration. Verify that a generated attachment opens correctly and belongs to the right order. Do not treat a token name alone as proof that a file will be generated and attached automatically.
