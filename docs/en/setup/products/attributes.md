# Attributes and product options

An attribute is a field describing a product or collecting a customer's choice. Name, material, and color are examples. Attribute configuration decides how a field is edited, validated, translated, and offered for filtering.

## Decide what kind of information it holds

| Information | Model it as |
| --- | --- |
| “Made from stainless steel” | An editor-defined descriptive attribute |
| “Blue, size M”, with its own SKU | Variant option attributes and a variant |
| “Please engrave Sam” | A customer-defined text option |

A color label alone does not make a product variant. A text input alone does not track a distinct stocked item.

## Create an attribute

1. Open **Configuration → Attributes**.
2. Choose a clear display name and a stable, unique internal name.
3. Select the field type, such as text or a selection field.
4. Set validation and whether the value is required.
5. Choose whether it is multilingual.
6. For selections, configure the option source and options.
7. Add the attribute to the relevant [product type](types.md).
8. Edit a test product and verify the resulting form and frontend.

Treat the internal name as a technical identifier. Integrations and templates can depend on it. Renaming or deleting an established field needs a data migration plan.

## Selection values and labels

An option has a stored value and a readable label. Use stable stored values such as `blue` and translate the label if needed. Changing the label is different from replacing a stored value already used by products and orders.

The options manager is useful when several products share a fixed choice list. Product-specific options are useful when valid choices differ for each product. Custom database sources require a developer. The older options wizard is marked deprecated in the source help.

## Customer-defined fields

Enable **Defined by customer** when the buyer supplies the value. Use a meaningful label, a useful hint, and realistic validation. For engraving, set a maximum length that production can actually fulfill.

Test an empty value, the longest accepted value, and a rejected value. Add two versions of the product with different inputs and confirm that cart and order details preserve the choices separately.

Do not assume a field automatically changes the price. Pricing for options must be supported by the configured attribute and the installation's price handling. Test the total rather than inferring it from the field's presence.

## Search and filters

An attribute must be enabled for frontend searching or filtering before you offer it in the relevant filter element. Also configure that element and connect it to the product list. Backend searching and filtering are separate settings for editors.

A descriptive value needs template support to appear where you want it. Enabling a field on the product type primarily makes it available to the product model and editing form.

## Schema changes

Attributes can correspond to database columns. Follow the database-update workflow when changes require it. Deleting an attribute does not automatically remove its stored database column. Review proposed schema deletions and retain a backup before removing data.

Source: [attribute configuration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_attribute.php).
