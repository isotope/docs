# Set up size and color variants

A variant is a separately selectable version of a product. Trail Supply begins with one fixed Blue, size M T-shirt. Once you sell several combinations, configure Size and Color once so editors can maintain the combinations in daily work.

## Configure Clothing

1. Create Size and Color selection attributes with stable option values.
2. Enable their use as variant options.
3. Add them to a product type with variants enabled.
4. Select the variant attributes that should be independently editable, such as SKU and price.
5. Keep shared fields on the parent.

Variant attributes are not simply a second copy of every parent field. Fields outside the variant selection are inherited. Some attributes cannot be enabled in both groups.

## Extend the first-shop example

Use Blue and Black for Color and S, M, and L for Size. This gives six possible combinations. Keep the name and description shared. Allow each combination its own SKU. Keep the 22.00 price shared unless you need different prices.

Test changes to Clothing with existing products before applying them to the live catalog. The original Blue, size M item should become the corresponding purchasable combination without leaving a duplicate offer. Have your maintainer check references from integrations when changing existing product structure.

## Hand over to the product editor

After saving the type, open a test Trail T-shirt and confirm the variant wizard offers the intended options. Continue with [Managing variants](../../usage/variants.md) to create, publish, and check the six combinations.
