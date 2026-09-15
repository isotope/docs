# Shipping recipes

Shipping setup combines a calculation, availability rules, and selection in the store configuration. Read [Shipping methods](shipping.md) for the available types.

## One domestic flat rate

**Goal:** offer a fixed parcel charge for one shipping country.

1. Create an enabled shipping-address rule for the country.
2. Create a flat shipping method named Standard delivery with flat calculation and a charge of 5.50.
3. Assign Standard goods and the country rule. This keeps the fictional 10% tax included in the charge.
4. Enable the method and select it in the active store configuration.
5. Test one physical product with matching and nonmatching destinations.

Also select allowed shipping countries in the store configuration. The address-country list and method rule have different purposes.

## Standard and express

Create two methods with distinct labels, notes, and charges. Select both in the store configuration. Explain the delivery service rather than exposing internal tariff names.

Test switching between them and verify the final total. If a payment method depends on shipping, confirm that changing shipping also updates the valid payment choices.

A label such as Express does not create a carrier integration or guarantee a delivery deadline. Your operational process must provide the advertised service.

## Free delivery above a threshold

A zero-charge method can represent free shipping. If you use a cart-total rule for eligibility, be aware that the condition reads the calculated cart total, not an explicitly isolated merchandise subtotal.

A threshold can interact with the shipping fee itself. Test below the threshold, exactly at it, and above it, then change quantities and methods. Check whether both paid and free methods are visible and whether that matches your intention.

If your business requires “free delivery above a merchandise subtotal excluding shipping and payment fees”, have the developer implement and test that exact condition. Do not silently substitute cart total.

## Pickup arrangements

Configure the intended pickup behavior for the relevant products/types and a clearly labeled checkout arrangement. Explain where and how collection happens. Check whether the shipping address is suppressed as intended.

Restrict an offline “Pay on collection” payment method to the appropriate shipping choices if it must not appear for parcels. Test a cart mixing pickup-only and ordinary products before offering that combination.

## Weight-dependent charges

Enter accurate product weights with their units. Test the method's weight basis and minimum/maximum availability boundaries. The flat-per-weight calculation is proportional and does not automatically implement every carrier's rounding bands.

For discrete tariff bands, use an implementation that matches the carrier's published calculation and verify sample parcels. A packaging weight setting and a product weight do not necessarily participate in every calculation in the same way.

Record the expected results for representative baskets so you can retest after changing tariffs.
