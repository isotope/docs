# Version and implementation notes

This manual was checked against Isotope core revision `96240eaa65c33a51e37951fe9833d9db1bd5980d`. It documents the supplied source, not an independently certified production release.

The points below distinguish confirmed implementation details from assumptions in older text. They are especially useful when an integrator prepares the documented revision for a real shop.

## Current architecture

Storefront features are content elements and templates use Twig. Prices and applicability use the current price/rule model. Orders have separate order, transaction, and delivery status fields.

Old labels may still use “module” or reference removed integrations. Follow the actual field definitions and registered implementations.

## Payment integration mismatch

`UPGRADE.md` says third-party payment methods were removed, but `CashPayment` and `PaypalPayment` both carry registration attributes and `CorePaymentFactory` creates both. The payment DCA also contains a PayPal palette.

Additionally, the PayPal account field in this revision has input configuration but no SQL definition in that DCA. This needs verification in a complete application's resulting schema before assuming configuration persistence works.

The manual therefore describes the registered implementation and requires release-specific validation rather than declaring all historical gateways supported or all provider methods absent.

Sources: [upgrade notes](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md), [payment factory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CorePaymentFactory.php), [payment DCA](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_payment.php).

## Member-required checkout redirect

In `CheckoutController::enforceMemberLogin()`, member-required mode unconditionally redirects to the configured login page. The method does not check whether the current customer is already authenticated.

That is a source-level concern for member-required checkout, not a tested report for every released Isotope 3 version. Verify and resolve it on the installed revision before enabling that flow. Guest checkout is used for the introductory walkthrough.

Source: [checkout controller](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/CheckoutController.php).

## Address-rule regions

The checked `CartAddressCondition` rejects an address when its subdivision is contained in the configured subdivision array. This differs from the apparent inclusion meaning of the region selection.

Country-only examples in this manual avoid that ambiguity. Validate and resolve region-dependent rules on your target release before relying on them for taxes or checkout availability.

Source: [address condition](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder/Condition/CartAddressCondition.php).

## Historical delivery-status migration

In `OrderstatusMigration::migrateOrders()`, the branch that creates `delivery_status` then updates `transaction_status` to `shipped`. Review that assignment before applying this revision to historical orders.

This manual does not modify the core migration. A production upgrade requires a tested correction or a verified release where the issue is resolved.

Source: [status migration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Migration/OrderstatusMigration.php).

## Documents and price behavior

- Standard documents contain HTML, regardless of the `.pdf` suffix on a preview route.
- The first matching advanced price entry wins.
- Among eligible quantity tiers, the price calculator selects the lowest amount.
- Fixed display keeps the starting displayed amount and extracts applicable tax from it.
- The base-price field remains available even though the old dedicated attribute class was removed.

These are reflected in the relevant setup chapters. They are not reasons to recreate removed Isotope 2 components.

## Scope of validation

The manual's links, navigation, examples, and static site build can be checked in the documentation repository. End-to-end shop behavior requires a configured Contao application, database, mail setup, and provider integrations. The [launch checklist](../getting-started/launch.md) defines those acceptance tests.
