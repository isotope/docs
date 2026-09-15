# Upgrading to Isotope 3

Treat a major-version upgrade as a migration project. The page architecture, templates, integrations, and data structures can change even when the shop looks similar to a customer.

## Inventory the existing shop

Record the Isotope, Contao, PHP, and extension versions. List custom templates, hooks, payment/shipping integrations, product attribute types, documents, promotions, analytics, and any external stock/accounting connections.

Keep a database/files backup and test restoration. Perform the upgrade on a separate copy before scheduling production work.

## Changes called out by the source

The documented [core upgrade notes](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md) include:

| Earlier setup | Isotope 3 consideration |
| --- | --- |
| Isotope frontend modules | Reimplemented as content elements |
| Legacy templates | Rewritten in Twig |
| `@IsotopeHook` annotations | Replaced with `#[AsIsotopeHook]` |
| Legacy PostSale entry point | Removed, use an appropriate controller/integration |
| Automatic currency converter | Removed |
| Legacy price display | Removed, check current Net/Gross/Fixed behavior |
| ElevateZoom and image watermarks | Removed |
| Built-in Google Analytics integration | Removed |
| Favorites | Extracted to an extension |
| Wishlist | Removed |
| Downloads/FileTree/Media attributes | Extracted to an extension |
| Range/cumulative filters and variant-list feature | Removed |
| Custom SQL product-list queries | Removed |

The notes also remove old dedicated attribute classes for values now represented differently, including price, base price, and shipping weight/price. Inspect the current product fields instead of recreating obsolete classes.

Payment integration notes disagree with the registered PayPal code in this checkout. Review [version notes](../reference/version-notes.md) and validate the exact intended release.

## Rehearse migrations

1. Install compatible dependency versions on the copy.
2. Run the database migration workflow and review output.
3. Inspect products, category assignments, variants, and prices.
4. Inspect historical orders and all three status tracks.
5. Rebuild or adapt Twig templates and page elements.
6. Reconfigure or replace unsupported integrations.
7. Complete the [launch tests](launch.md), including failure and return paths.

Do not assume automatic data migrations make old custom code compatible. Check the resulting records and presentation.

## Historical orders and statuses

Isotope 3 separates order, payment, and delivery statuses. Verify mapped historical values against known orders, including paid, unpaid, cancelled, and shipped examples.

The checked migration contains a delivery-status assignment concern documented in the version notes. Have the maintainer validate and resolve it before applying this revision to historical production data.

## Production cutover

Agree when orders can be accepted during deployment and how to reconcile provider activity around that window. Deploy the tested versions, templates, and configuration, then run the defined smoke tests.

Keep access to the previous backup and the exact migration/deployment record. A rollback involving a database must account for new orders and payments rather than simply replacing current data with an older copy.
