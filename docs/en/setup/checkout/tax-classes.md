# Configure tax classes

A tax class describes the tax treatment of a price. Assign the class to product prices and, where appropriate, shipping or payment charges. Read [Prices and taxes explained](../../concepts/prices-and-taxes.md) first if these terms are new.

## Create rates first

A class refers to existing [tax rates](tax-rates.md). Create the rates and their rules before creating the class.

For the examples below, imagine a fictional 10% domestic rate and a fictional 20% destination rate. These are teaching values.

## Class for tax-exclusive catalog prices

If you enter a product price of 20.00 before tax:

1. Create a class named “Standard goods, entered net”.
2. Leave **Tax rate included with product price** empty.
3. Select the applicable rate under **Apply tax rates**.
4. Assign this class to the product price.

With only the 10% rate matching, the result is 20.00 net and 22.00 gross.

## Class for tax-inclusive catalog prices

If you enter 22.00 including the domestic 10% rate:

1. Use the “Standard goods” class from the first-shop example.
2. Select the 10% rate as **Tax rate included with product price**.
3. Add a different destination rate under **Apply tax rates** only when your intended rules require it.
4. Make the domestic and destination rules mutually exclusive if only one rate should apply.
5. Assign the class to the product price.

The included rate is extracted from the entered amount. When its rule matches, it is also applied. **Do not select that same rate again in the additional rates list.** Selecting it twice can add tax twice.

When the domestic rule no longer matches, the domestic tax is removed. If the 20% rate matches instead, the gross price becomes 24.00 on the same 20.00 net basis.

## Included-tax label

The class provides an include label for the removed included-tax situation. Use customer-readable wording. If the class label is blank, the rate's label is used where applicable.

## Defaults and exceptions

Mark a class as default only when it is the intended common selection. Review the tax class actually saved with each price, including advanced prices and variants. A default does not explain or correct existing data automatically.

Use a separate class when products have different tax treatment. Do not overload a product type or category name to stand in for a tax class.

## Verify before bulk entry

Test one product in each class, each destination rule, and both the initial browsing context and completed address context. Check net, tax, and gross separately. Once the result is correct, use the same setup consistently across the catalog.

Continue with the [worked tax guide](tax-example.md).
