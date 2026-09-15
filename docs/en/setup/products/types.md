# Product types

A product type is a reusable editing and display setup for a family of products. It determines which attributes editors fill in, whether variants exist, how pricing is configured, and which templates and galleries are used.

It is **not a category**. A category controls where a product is found. A type controls how it is modeled. A mug can appear in both Drinkware and Gifts while using one “Physical product” type.

## Plan a small set

Start with a simple type for ordinary physical goods. Add another type when the editing needs or behavior differ substantially.

| Example | Useful type setup |
| --- | --- |
| Mug | Name, SKU, description, price, images |
| T-shirt | Shared description plus size/color variants |
| Coffee | Price, package amount, comparison base price |
| Service | Appropriate product fields and shipping exemption |

Do not create a new type for every product. Shared types make consistent editing easier.

## Create a type

1. Open **Configuration → Product types** and create a record.
2. Give it a name and a description that helps other editors choose it.
3. Choose the appropriate product class available in the installation.
4. Select the attributes editors need. Group related fields so the form remains understandable.
5. Include a price field for a normally purchasable product.
6. Choose list and reader templates and galleries where offered.
7. Save, then create a sample product using this type.

If a field is missing from a product form, inspect its type before creating a duplicate attribute.

## Advanced pricing

Enable advanced pricing when you need multiple conditional price sets or quantity tiers. A simple one-price product does not need that extra editing complexity. See [Prices](../../usage/prices.md) for the first-matching-price behavior.

## Variants and inheritance

Enable variants for products sold in combinations such as size and color. Select the variant option attributes that identify each combination. Other variant attributes let the child hold data such as a different SKU or price.

Fields not configured as variant attributes are inherited from the parent. Decide deliberately which information belongs to the parent and which changes between variants. Follow [Variants](../../usage/variants.md) for a complete example.

## Shipping handling

The type can describe ordinary shipping, exemption, or pickup behavior. An exempt service should not require parcel delivery. Pickup can suppress the shipping address.

Shipping exemption alone does not implement digital file delivery. That requires the relevant extension and its access rules. Always test a mixed cart, because a service and a shipped item still require delivery for the physical item.

## Change types carefully

Changing a shared type affects the editing and presentation of its products. Adding a required field can leave existing products without a useful value. Moving pricing to variants can leave variants without prices. Recheck existing catalog items after a type change.

Source: [product type model](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Model/ProductTypeModel.php).
