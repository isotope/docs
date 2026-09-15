# Source map and documentation maintenance

The manual is grounded in core revision `96240eaa65c33a51e37951fe9833d9db1bd5980d`. Links below identify the implementation areas to revisit when behavior changes.

| Topic | Primary source |
| --- | --- |
| Requirements | [composer.json](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/composer.json) |
| Upgrade changes | [UPGRADE.md](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md) |
| Bundle settings and registered types | [IsotopeBundle](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php) |
| Backend fields | [DCA definitions](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca) |
| Labels and help | [English language files](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en) |
| Product construction and prices | [Product](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Product) |
| Price calculation | [Store/Price](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price) |
| Taxes | [TaxCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Tax/TaxCalculator.php) |
| Rule evaluation | [RuleBuilder](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder) |
| Storefront | [Content-element controllers](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement) |
| Payment and shipping | [Checkout](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout) |
| Status workflows | [WorkflowManager](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Order/WorkflowManager.php) |
| Order messages | [DefaultOrderNotificationTokensListener](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/EventListener/DefaultOrderNotificationTokensListener.php) |
| Documents | [DocumentManager](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/DocumentManager.php) |
| Templates | [Twig templates](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/templates) |
| Core checks | [CI workflow](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/.github/workflows/ci.yml) |

## Updating a chapter

1. Check the behavior in the target source version, including field definitions and dispatch paths.
2. Explain the concept before the configuration steps.
3. Include prerequisites, the intended result, and a way to verify it.
4. Update affected guides and troubleshooting entries together.
5. Run the documentation checks and strict build described in the repository README.
6. Update the baseline revision only after reviewing the affected manual scope.

Do not silently turn an extension-specific capability into a core promise. Record source/help inconsistencies in [Version notes](version-notes.md) until they are resolved.

## Additional chapter references

- [PurgeCartsCron](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Cron/PurgeCartsCron.php)
- [registered notification tokens](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/NotificationCenter/OrderNotificationType.php)
- [order token descriptions](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en/nc_tokens.xlf)
- [CashPayment](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CashPayment.php)
- [CorePaymentFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CorePaymentFactory.php)
- [FlatShipping](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Shipping/FlatShipping.php)
- [shipping fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_shipping.php)
- [tax-rate fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_tax_rate.php)
- [CheckoutController](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/CheckoutController.php)
- [OrderDetailsController](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/OrderDetailsController.php)
- [page help](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en/tl_page.xlf)
- [StandardDocument](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Document/StandardDocument.php)
- [OrderNotifier](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Order/OrderNotifier.php)
- [default status migration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Migration/OrderstatusMigration.php)
- [store configuration fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_config.php)
- [attribute configuration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_attribute.php)
- [base-price formatter](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceFormatter.php)
- [product type model](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Model/ProductTypeModel.php)
- [RuleMatcher](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder/RuleMatcher.php)
- [DefaultPriceFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Product/DefaultPriceFactory.php)
- [PriceCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceCalculator.php)
- [product fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_product.php)
