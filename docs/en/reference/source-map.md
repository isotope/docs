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
