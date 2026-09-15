# Multiple languages, currencies, and markets

Language, currency, delivery region, and store identity are related but different choices. An English-speaking customer does not necessarily want to pay in a particular currency or receive delivery in a particular country.

## Multiple languages

Use Contao's website roots and language structure. Configure the corresponding shop context and translate product information where the attributes support multilingual values.

Plan translations for product names/descriptions, attribute option labels, checkout labels and notes, notifications, and document text. Check image alternate text and photographs containing language-specific content.

A translated product should keep stable technical identifiers where your catalog model requires them. Do not create an unrelated second product merely to translate a label unless that is an intentional catalog design.

## Shared store ID

Related website roots can use the same store ID to share shop context such as member carts and addresses. Distinct stores should use an intentional separation.

Test switching languages with an existing cart. Confirm that the cart, product links, addresses, and order-detail access behave as intended. Sharing a store ID does not itself translate product content or synchronize separate product records.

## Multiple store configurations

Create a configuration for each intended currency/market behavior. Set its currency, display format, address choices, methods, and price factor. Assign defaults to the relevant site structure.

The configuration-switcher element can let the customer choose among selected configurations. It recalculates the cart when switching. With only one selected configuration, the element can apply that configuration without displaying a selector, so use such an element deliberately.

## Price conversion versus explicit prices

A price factor multiplies amounts. It is not a live exchange-rate feed. Explicit advanced prices selected by a configuration rule let you set stable commercial prices per configuration.

Choose one clear approach and test the result. If you enter a converted price and also apply a conversion factor, you may convert twice. Check fixed fees, shipping, price ranges, and quantity tiers as well as simple product prices.

## Taxes and addresses

Use explicit rules for your verified tax treatment. Default countries influence the browsing context before checkout supplies the actual address. Do not derive tax treatment solely from the interface language.

This manual does not determine cross-border tax obligations. Translate the approved business rules into Isotope conditions and test a matrix of destinations and customer types.

## Test matrix

For each supported language/configuration combination, check a product list, variant selection, cart, address entry, shipping/payment availability, order notification, and document. Include switching after a cart already contains products.

Related: [Store configurations](stores.md), [Tax example](../checkout/tax-example.md).
