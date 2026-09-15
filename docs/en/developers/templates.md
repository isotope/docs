# Twig templates

Isotope 3 uses Twig. Its storefront features are Contao content elements, with product and collection rendering split into reusable templates and components.

## Find the right layer

A product-list content element controls the list container. The product list/reader template controls an individual product. Gallery and price components render smaller pieces.

Inspect the selected product type and any content-element override before changing a template. Editing a reader template will not necessarily change a list card using a different template.

The source defaults include `isotope/product/list` and `isotope/product/reader`. The shared `isotope/product.html.twig` contains blocks for images, options, price, quantity, and actions.

## Extend a small block

Use Contao's Twig template customization mechanism to create a selectable variant. A product reader variant can extend the core reader and preserve its existing price output:

```twig
{% extends '@Contao/isotope/product/reader.html.twig' %}

{% block product_price %}
    {{ parent() }}
    <p class="delivery-information">Delivery options are shown at checkout.</p>
{% endblock %}
```

Save the variant under the application's template structure, select it as the reader template for the intended product type/element, and rebuild the application cache if required by the environment. For a multilingual site, replace the literal sentence with an appropriate translation.

This example adds presentation only. It does not calculate delivery costs or change the product price.

## Preserve functional markup

The standard product template includes form identifiers, request tokens, action rendering, and Stimulus data attributes. Removing them can break option updates or add-to-cart behavior even when the page looks correct.

Prefer overriding narrow blocks and calling `parent()` when you need to retain behavior. Keep escaping enabled for customer input. Do not use `raw` simply to suppress unwanted escaping without understanding the value's origin.

## Use the calculated price

Core templates use helpers such as `isotope_price(product)`, `isotope_baseprice(product)`, and `isotope_gallery(product, 'images')`.

Do not render an unprocessed database price as the amount to pay. It can bypass tax, variants, quantity tiers, rules, currency factors, and formatting.

## Review custom output

Check product lists, readers, variants, validation errors, empty images, long labels, and mobile layouts. Add the product to a cart and place an order after presentation changes. Test both default and member-specific price contexts.

For documents and notifications, inspect their separate templates and available context. A product reader's variables are not automatically available in a document body.

Source: [shared product template](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/templates/isotope/product.html.twig).
