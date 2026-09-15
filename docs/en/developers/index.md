# Developer guide

The shop-owner chapters explain the behavior your implementation needs to preserve. Read the relevant setup chapter before changing pricing, checkout, or order processing.

This section targets the documented Isotope 3 source revision. Several classes carry `@internal` or `@experimental` annotations. Inspect those markers and the installed version before treating a class as a stable extension contract.

## Installation and operations

Use [technical installation](installation.md) for Composer and migrations, then [bundle configuration](bundle-configuration.md) for application settings. Routine product and order work belongs in [Daily use](../usage/index.md).

Maintainers also own [upgrades](upgrading.md), [performance](performance.md), complete backups, and restoration tests. Before a change, preserve the database, uploaded files, generated documents, configuration, custom code, and dependency lock file. Test on a separate installation and plan recovery without losing new orders or payments.

## Architecture map

| Area | Main responsibility |
| --- | --- |
| `Controller/ContentElement` | Contao storefront elements |
| `Product` | Product data, factories, configuration, rendering, and events |
| `ProductCollection` | Carts, orders, line items, and payment transaction handling |
| `Store/Context` | Currency, configuration, member, address, and cart context |
| `Store/Price` and `Store/Tax` | Price definitions, calculations, and formatting |
| `Checkout` | Steps and shipping/payment methods |
| `RuleBuilder` | Reusable contextual conditions |
| `Document` and `Store/Document` | Rendering, numbering, and document storage |
| `contao/dca` | Backend fields and editing forms |
| `contao/templates` | Twig templates and components |

A DCA, or data container array, is Contao's definition of an editing interface and its fields. It is useful evidence for what administrators can actually configure. Translation help text can lag behind implementation, so check both.

## Choose the extension point

- For presentation, start with [Twig templates](templates.md).
- For observing or enriching an existing process, inspect [events](events.md).
- For a new method or behavior family, use the relevant registered type/factory pattern described in [Extensions](extensions.md).
- For global configuration, use the documented [bundle settings](bundle-configuration.md).

Keep custom code in the application or a dedicated compatible bundle. Editing files inside an installed dependency makes updates difficult to reproduce.

## Testing scope

Use a full Contao application for integration and browser tests. The bare core repository is a bundle, not a configured shop. Test guest/member contexts, multiple quantities, address changes, retries, and external-provider failures where relevant.

The core repository contains PHPStan, Rector, ECS, dependency analysis, PHPUnit, ESLint/stylelint configuration, and asset build tooling. Its CI calls shared Contao build tools and runs PHPUnit across PHP 8.3–8.5 with Contao 5.7. Follow the checked-out project's actual tools and versions rather than assuming one generic command covers them all.

See the [source map](source-map.md) for the files used to ground this manual and the [implementation notes](version-notes.md) for unresolved behavior in this revision.
