# Before you open the shop

A shop is ready when customers can complete the supported purchase journeys and staff can handle the resulting orders. A working homepage is only the beginning.

Record the tester, date, result, and order reference for each acceptance test. Use a copy or the payment provider's supported test environment before live testing.

## Catalog and navigation

- [ ] Categories show the intended published products.
- [ ] Reader links work from every category, including child pages.
- [ ] Names, descriptions, images, quantities, and included items are accurate.
- [ ] Every offered variant has the right SKU, price, and image.
- [ ] Customer-defined options are validated and preserved in the order.
- [ ] Missing products and invalid URLs produce a useful result.
- [ ] Protected products are visible only to intended member groups.

## Prices and taxes

- [ ] The currency, price factor, and Net/Gross/Fixed mode are intentional.
- [ ] Included and additional taxes produce manually verified amounts.
- [ ] Default-address prices and final-address prices behave as expected.
- [ ] Every relevant destination and tax class is tested.
- [ ] Shipping and payment fees use the intended tax treatment.
- [ ] Tier boundaries and conditional-price fallbacks work.
- [ ] Rounding agrees across cart, order, payment, and documents.

## Checkout journeys

| Test case | What to verify |
| --- | --- |
| New guest | Address entry and order completion |
| Signed-in member | Login, address reuse, and complete checkout |
| Different billing/shipping addresses | Correct delivery and tax context |
| Physical-only cart | Shipping choices and charges |
| Exempt-only cart, if offered | No unnecessary parcel requirements |
| Mixed cart | Valid shipping and payment combinations |
| Quantity change | Recalculated prices and availability |
| Empty cart | Clear route back to browsing |

- [ ] Every supported combination has an available shipping/payment path.
- [ ] Disallowed countries and product combinations are rejected appropriately.
- [ ] Required checkout forms block incomplete submission.
- [ ] The completed-order destination displays the order and handles payment.

## Payment outcomes

- [ ] Success records the correct order, amount, currency, and payment status.
- [ ] Failure and cancellation leave understandable recovery options.
- [ ] An interrupted return from the provider is reconciled correctly.
- [ ] Delayed or repeated provider notifications are handled safely.
- [ ] Offline payment instructions and staff reconciliation are clear.
- [ ] Live credentials and endpoint settings are verified for the intended release.

## Communication and operations

- [ ] Order confirmation wording does not incorrectly claim payment success.
- [ ] Customer and staff notifications arrive with resolved tokens.
- [ ] Every supported notification language is checked.
- [ ] Documents have the intended content, format, numbering, and storage.
- [ ] Staff can process payment, dispatch, cancellation, and return cases.
- [ ] Tracking links lead to the correct carrier information.
- [ ] Product information, checkout wording, and business policies have been reviewed by their responsible owners.

## Access, recovery, and maintenance

- [ ] A different customer cannot access a member's order or address book.
- [ ] Private order pages and customer-specific responses are not shared through caches.
- [ ] Staff accounts have appropriate access.
- [ ] HTTPS, email delivery, and scheduled tasks are operating.
- [ ] Database, files, and generated documents have a tested restore process.
- [ ] Someone owns ongoing updates and error monitoring.

Resolve failures before accepting the affected kind of order. The [version notes](../reference/version-notes.md) identify source-specific concerns to include in your testing.
