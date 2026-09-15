# Troubleshooting

Start with the smallest failing step. Record the URL, installed versions, customer state, active store configuration, cart contents, and what changed recently. Use test data when reproducing a problem.

## A product is missing

| Check | Why it matters |
| --- | --- |
| Product publication and dates | A saved product can still be unavailable |
| Category page assignment | Lists read page-based categories |
| List category scope | The current page may not include child assignments |
| Page/article/element publication | The surrounding Contao content must be visible |
| Product/member protection | The visitor may not belong to the allowed group |
| Active filters | A previous filter can exclude the product |
| Variants | Required children may be unpublished or incomplete |

Test with a fresh visitor session and an uncomplicated list before changing the database.

## Product details do not open

Check the category's reader mode. For separate-page readers, configure the reader page on **each** category. The setting is not inherited. Confirm the destination contains a product-reader element and that the product alias is valid.

If list and reader share a page, enable hiding the list in reader mode. If reader mode is disabled, detail links are intentionally unavailable for that category.

## The price is wrong or absent

Check the product type's price fields and whether pricing belongs to the parent or variants. For advanced prices, verify the first matching entry, a quantity-1 tier, and the fallback.

Check the tax class's included rate, additional rates, and rules. Then inspect the active configuration's Net/Gross/Fixed mode and currency factor. Change one variable at a time and compare net, tax, and gross separately.

A higher quantity tier does not force a higher unit price in Isotope’s lowest-eligible-price calculation.

## A shipping or payment method is missing

1. Confirm the method is enabled.
2. Confirm it is selected in the active store configuration.
3. Check whether its rule is enabled and matches.
4. Inspect product-type restrictions against the whole cart.
5. For shipping, check weights and whether shipping is required.
6. For payment, check allowed shipping-method combinations, including carts without shipping.
7. Verify that the method type is actually registered by the installed release/extension.

An empty list of available methods is usually a configuration/availability issue, not a missing checkout template.

## Checkout redirects or does not complete

Confirm the completed-order destination contains Order details, rather than only a thank-you message. Verify required forms and available methods.

For member-required checkout, test a signed-in user and ask your maintainer to review the [member-checkout version note](../developers/version-notes.md) if login keeps repeating.

If an order already exists after an error, inspect it before asking the customer to order again. The failure could be in notification or payment handling after creation.

## Payment remains unresolved

Read the order's payment status and transaction history, then check the provider. Verify account configuration, amount/currency, callback accessibility, and status mappings with the integrator.

Do not manually mark an order Paid solely because the customer reached a success-looking page. Reconcile the authoritative payment evidence.

## No email arrives

Check the checkout's selected notification, notification type, enabled message, language, recipient token, and mail transport. Look at mail logs or delivery results.

A guest notification cannot assume member fields exist. Raw `##token##` text indicates unsupported syntax/context or a misspelling. An empty replacement can indicate missing data.

## A document is not a PDF

The Standard document type creates HTML. Ask your maintainer to configure a compatible PDF document type if PDF is required.

## Escalate with useful evidence

Provide exact reproduction steps, expected/actual results, a test order reference, versions, and the relevant error excerpt. Remove private customer details and credentials. Say whether the problem reproduces with the standard templates and without the optional integration involved.
