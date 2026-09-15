# Store configurations

A store configuration collects the settings that determine how a shopping session behaves: currency, price display, address fields, permitted countries, and available checkout methods.

Use **Isotope eCommerce → Configuration → Store configurations**. For your first shop, create one configuration with a recognizable name such as “Trail Supply domestic”.

## Identity and address

Enter the business contact information you want to use in shop communications and documents. Bank information is useful for offline payment instructions. Filling these fields does not send a payment request to your bank.

The configuration name helps staff. The label can be shown to customers, for example in a configuration switcher.

## Address choices

A billing address identifies the buyer for billing. A shipping address tells you where to deliver. They may be the same, but customers sometimes send gifts or order from a business address.

Select the fields needed for each address and decide which are mandatory. Requiring unnecessary information adds work for every customer. Hiding information you need for fulfillment creates manual follow-up later.

Set default billing and shipping countries. Then explicitly select the countries you accept. **An empty allowed-country selection means all countries**, not no countries. Default countries are starting values, not geographic restrictions.

If you limit member countries, Contao member registration and personal-data choices can be restricted to the combined billing and shipping countries.

## Price display and currency

Choose the currency and Net, Gross, or Fixed price display. Fixed keeps the entered displayed price and treats applicable taxes as included, so net proceeds can vary with tax. Set the display format and rounding to match your accounting and payment integration. Formatting controls how an amount looks. The [tax class](../checkout/tax-classes.md) describes the tax already included in an entered price.

The price factor normally remains `1`. It can multiply prices for another configuration, but it is not an automatic exchange-rate service. Explicit prices per configuration can be easier to control when you need stable retail prices. See [Multiple languages and currencies](../../guides/international.md).

## Select checkout methods

Create [shipping](../checkout/shipping.md) and [payment](../checkout/payment.md) records, enable them, and then select them in this configuration. A method must also satisfy its availability conditions.

After adding a new method, return here. This extra selection is a common reason a newly created option does not appear at checkout.

## Connect the configuration to the website

In the Contao page structure, select the store configuration for the relevant website structure. Review the **Store ID** on the website root as well. The store ID groups related site roots for shared carts and addresses. It is different from the configuration record's database ID.

Start with one root and one configuration. When adding roots or a configuration switcher, test the same cart while moving between them. A configuration switch can recalculate the cart and affect applicable prices and checkout choices.

## Verify

Open a fresh guest session. Check currency, displayed price, default countries, allowed address countries, and shipping/payment choices. Do this again after entering a real test destination.

Source: [store configuration fields](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_config.php).
