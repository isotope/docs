# Product variants

Variants represent specific versions of a shared product. A T-shirt's description may be shared, while each size/color combination has its own SKU and possibly a different price or image.

Use a customer-defined option instead when you simply need free-form input such as an engraving message. See [Attributes](../setup/products/attributes.md).

## Example: a T-shirt

Trail Supply sells a shirt in Blue and Black, each in S, M, and L. This creates six combinations. The parent product holds the shared name and description. Each child represents one combination.

## Prepare the product type

1. Create Size and Color selection attributes with stable option values.
2. Enable their use as variant options.
3. Add them to a product type with variants enabled.
4. Select the variant attributes that should be independently editable, such as SKU and price.
5. Keep shared fields on the parent.

Variant attributes are not simply a second copy of every parent field. Fields outside the variant selection are inherited. Some attributes cannot be enabled in both groups.

## Create the combinations

1. Create the parent T-shirt product.
2. Complete its shared description, categories, and images.
3. Use the product's variant action/wizard to add the combinations you actually sell.
4. Check each child's size and color values.
5. Assign a distinct SKU where operationally needed.
6. Enter independent prices or images where configured, or use inheritance.
7. Publish the intended variants and choose a default variant if appropriate.
8. Test the product reader.

Do not generate combinations that do not exist. If Blue is only available in S and M, avoid an accidental Blue/L offer.

## Inheritance

Inheritance means “use the parent's value”. It is useful for shared descriptions or photographs. An overridden child value stays independent when the parent changes.

If a variant has the wrong description or price, inspect the product type's variant attributes and the child's inherited fields. Do not repeatedly edit the parent when the child has an independent value.

## Default and visible choices

A default variant can be preselected. The type can also force variant attributes to remain visible when only one choice exists. Decide whether the customer needs an explicit choice to understand what they are buying.

A “from” price can reflect variant or tier differences. Verify that the final selected combination's price is clear before adding it to the cart.

## Test the entire selection

Choose every meaningful combination and verify SKU, price, image, availability, and recorded order options. Add two different variants of the same parent to a cart. Change quantities and confirm the lines remain distinct.

## Adding a choice later

Adding “XL” to the Size options does not complete all your product data. Create the intended variants, provide any required independent information, publish them, and test the updated selector.

Source: [ProductTypeModel](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Model/ProductTypeModel.php).
