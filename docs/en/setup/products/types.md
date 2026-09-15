# Product types

A product type is a reusable editing and display setup for a family of products. It determines which attributes editors fill in, whether variants exist, how pricing is configured, and which templates and galleries are used.

It is **not a category**. A category controls where a product is found. A type controls how it is modeled. The Trail T-shirt can appear in both T-shirts and Gifts while using one “Clothing” type.

## Plan a small set

Start with a simple type for ordinary physical goods. Add another type when the editing needs or behavior differ substantially.

| Example | Useful type setup |
| --- | --- |
| Trail T-shirt, first shop | Clothing type with name, SKU, description, price, and images |
| Trail T-shirt and Trail hoodie, expanded catalog | Clothing type extended with shared descriptions and size/color variants |
| Garment wash | A separate care-product type with package volume and comparison base price |

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

Fields not configured as variant attributes are inherited from the parent. Decide deliberately which information belongs to the parent and which changes between variants. Follow [Variant setup](variants.md) for a complete example.

## Shipping handling

The type can describe ordinary shipping, exemption, or pickup behavior. An exempt service should not require parcel delivery. Pickup can suppress the shipping address.

Shipping exemption alone does not implement digital file delivery. That requires the relevant extension and its access rules. Always test a mixed cart, because a service and a shipped item still require delivery for the physical item.

## Change types carefully

Changing a shared type affects the editing and presentation of its products. Adding a required field can leave existing products without a useful value. Moving pricing to variants can leave variants without prices. Recheck existing catalog items after a type change.
