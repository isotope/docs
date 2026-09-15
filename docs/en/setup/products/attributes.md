# Attributes and product options

An attribute is a field describing a product or collecting a customer's choice. Name, material, and color are examples. Attribute configuration decides how a field is edited, validated, translated, and offered for filtering.

## Decide what kind of information it holds

| Information | Model it as |
| --- | --- |
| “Made from cotton” | An editor-defined descriptive attribute |
| “Blue, size M”, with its own SKU | Variant option attributes and a variant |
| “Please print Sam” | A customer-defined text option |

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

Treat the internal name as a technical identifier. Integrations and templates can depend on it. Ask your maintainer to plan any change to an established internal name.

## Selection values and labels

An option has a stored value and a readable label. Use stable stored values such as `blue` and translate the label if needed. Changing the label is different from replacing a stored value already used by products and orders.

The options manager is useful when several products share a fixed choice list. Product-specific options are useful when valid choices differ for each product. Custom database sources require a developer. Use the options manager for new shared lists.

## Customer-defined fields

Enable **Defined by customer** when the buyer supplies the value. Use a meaningful label, a useful hint, and realistic validation. For a printed name, set a maximum length that production can actually fulfill.

Test an empty value, the longest accepted value, and a rejected value. Add two versions of the product with different inputs and confirm that cart and order details preserve the choices separately.

Do not assume a field automatically changes the price. Pricing for options must be supported by the configured attribute and the installation's price handling. Test the total rather than inferring it from the field's presence.

## Search and filters

An attribute must be enabled for frontend searching or filtering before you offer it in the relevant filter element. Also configure that element and connect it to the product list. Backend searching and filtering are separate settings for editors.

A descriptive value needs template support to appear where you want it. Enabling a field on the product type primarily makes it available to the product model and editing form.

## Changing established fields

Changing or deleting an established attribute can affect existing products and their display. Ask your maintainer to handle any required database update and confirm what happens to saved values. Check existing products after the change.
