# Shipping methods

A shipping method tells the customer how goods will reach them and what that choice costs. It can represent standard delivery, express delivery, or a pickup arrangement.

The method calculates an offered charge and availability. Booking a carrier, printing a label, and physically dispatching the parcel are separate tasks unless an installed integration handles them.

## Create your first method

1. Open **Configuration → Shipping methods**.
2. Choose a flat shipping type for a simple fixed charge.
3. Enter an internal name and a clear customer label.
4. Add a note explaining delivery expectations.
5. Choose flat calculation and enter the charge.
6. Assign its tax class if needed.
7. Add a destination rule or product restrictions if needed.
8. Enable the method.
9. Select it in the active [store configuration](../general/stores.md).
10. Add a physical product to the cart and check checkout.

Start with a single uncomplicated method. Add alternatives after you have verified the first end to end.

## Core calculation types

**Flat shipping** starts with the configured price. Its modes can charge once, per product line, per item quantity, or according to weight.

For a cart containing three identical Blue, size M T-shirts and one Trail hoodie, the example charge of 5.50 gives 5.50 in flat mode, 11.00 for two product lines, or 22.00 for four items. These amounts include the fictional 10% tax when using Standard goods. This compares alternative calculation modes. The first-shop walkthrough uses flat mode. Product-type restrictions and shipping-exempt items can change which lines participate.

Weight mode uses the configured weight basis. The charge is proportional to weight and can truncate fractional weight amounts. Do not assume it rounds up to the next parcel or kilogram. Test fractional weights and boundaries before using it for a carrier tariff.

**Product-price shipping** uses shipping prices stored with products. Its modes select the highest or lowest price, or sum prices, either per product line or multiplied by quantity.

**Grouped shipping** combines available child methods using the first, lowest, highest, or summed charge. It can present several internal calculations as a single customer choice. Test the group when one child becomes unavailable.

## Availability and price are separate

A method can have a valid price and still be unavailable. Check:

- Enabled status and selection in the active store configuration.
- The attached rule, especially the shipping address.
- Product-type conditions for the complete cart.
- Minimum and maximum weights where configured.
- Whether the cart requires shipping at all.

Testing just one product is insufficient when a cart can mix product types.

## Pickup and shipping exemption

A pickup-only product can suppress the shipping address. An exempt product, such as a service, does not require parcel shipping. These are product/type behaviors, not just labels on a method. Test the actual fields shown for pickup and mixed carts.

If payment is only accepted at collection, restrict the payment method to the intended shipping arrangement. See [Payment methods](payment.md).

## Tracking

A tracking URL can contain `%s` where the tracking number belongs. Test it with a real-format sample number and verify the resulting link. Entering tracking information in an order record does not itself book or dispatch a shipment.
