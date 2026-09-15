# Extending Isotope

Isotope registers several behavior families through PHP attributes and factories. Follow the corresponding core implementation from registration through backend configuration to runtime behavior.

## Registered type families

| Attribute | Extension area |
| --- | --- |
| `AsPayment` | Payment methods |
| `AsShipping` | Shipping methods |
| `AsDocument` | Document renderers |
| `AsGallery` | Product galleries |
| `AsRuleCondition` | Rule conditions |
| `AsCheckoutStep` | Checkout steps |
| `AsProductFactory` | Product construction |
| `AsAttribute` | Product attributes |
| `AsProductFilter` | Product query/filter behavior |
| `AsProductAction` | Product actions |
| `AsProductCollectionAction` | Cart/order collection actions |
| `AsProductCollectionItemAction` | Collection item actions |

These live in `Isotope\CoreBundle\DependencyInjection\Attribute`. The bundle's autoconfiguration and compiler passes connect them to the relevant registries. Inspect each constructor and interface before implementing a type, as the contracts differ.

## A complete custom method needs several parts

For a payment or shipping type, plan the runtime implementation, factory, backend fields/palette, translations, configuration persistence, and availability/pricing behavior. Adding a label to a type selector is insufficient.

Use the current core factory as an example. Verify whether a base class is internal before depending on it, and pin/test against supported Isotope versions.

## Payment integration responsibilities

A provider integration must handle configuration, initiating a payment, success/failure/return processing, authoritative provider notifications, amount/currency matching, and duplicate delivery. It must associate results with the correct order transaction.

Do not trust a browser query parameter as payment confirmation. Use the provider's verified result and define retry, cancellation, and refund behavior explicitly.

## Document renderers

A document type produces an `OrderDocument` with a number, creation time, filename, content type, and contents. The Standard type is HTML. A PDF renderer must return actual PDF contents with the correct media type and handle fonts/layout in its own implementation.

Use the existing numbering and storage services through the intended workflow so generated records remain associated with the correct order.

## Hooks

The `AsIsotopeHook` PHP attribute replaces the old annotation syntax. Register only a hook that is actually dispatched by the installed version and implement its exact argument/return contract.

Prefer the purpose-specific event when it provides the behavior you need. Do not mechanically translate an old hook name into a new service attribute and assume its dispatch still exists.

## Integration acceptance

Exercise the normal flow, unavailable configuration, invalid input, provider outage, repeated callbacks, and retries. Test mixed product types, member/guest contexts, and currency changes where relevant.

Keep integration-specific setup instructions beside the extension and link them from the shop's operations notes. Clearly identify which behaviors belong to core and which the extension supplies.

Source: [IsotopeBundle registration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php).
