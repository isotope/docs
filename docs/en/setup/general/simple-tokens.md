# Simple tokens in messages

A simple token is a placeholder that is replaced with data when a supported message is generated. For example, `##order_total##` can become a formatted order total in an Isotope order notification.

Tokens are not Twig expressions or Contao insert tags. They have different syntax and are available in different contexts.

## A small order message

Use this as a starting point in the body of an Isotope order notification:

```text
Thank you for your order ##document_number##.

We have received the following items:

##cart_text##

Order total: ##order_total##
Payment method: ##payment_label##

##payment_note##
```

This acknowledges receipt of the order. It does not claim that payment has succeeded.

For an HTML message, use suitable HTML markup and the supported `##cart_html##` token for the order table. Test the plain-text and HTML versions independently.

## Common order-notification tokens

| Token | Meaning |
| --- | --- |
| `##recipient_email##` | Recipient email supplied for this context |
| `##order_id##` | Internal database order ID |
| `##document_number##` | Formatted order reference number |
| `##uniqid##` | Unique identifier used to access the order |
| `##order_total##` | Formatted total |
| `##order_subtotal##` | Formatted subtotal |
| `##order_items##` | Quantities summed |
| `##order_products##` | Number of order lines, which can include non-product lines |
| `##billing_address##` / `##shipping_address##` | Formatted HTML addresses |
| `##billing_address_text##` / `##shipping_address_text##` | Plain-text addresses |
| `##payment_label##` / `##payment_note##` | Selected payment wording |
| `##shipping_label##` / `##shipping_note##` | Selected shipping wording |
| `##order_status##` | Order status label |
| `##transaction_status##` | Payment status label |
| `##delivery_status##` | Shipping status label |

The token chooser and the actual notification type are your reference for where tokens are accepted. Verify the identifier printed by your message rather than assuming every reference token is the same number.

## Token families

Families such as `billing_address_*`, `shipping_address_*`, and `config_*` expose supported fields from those records. Replace the asterisk with an actual field name. It is not literal syntax to paste into a message.

`member_*` data depends on a member checkout. `form_*` data depends on configured order-condition fields. Previous-status tokens belong to the order-update notification type and may not exist in an initial order confirmation. That type also registers `tracking_numbers` and `customer_notes`.

Do not use `collection_*` in order notifications. Use the order tokens listed above. Document title/filename fields have their own documented collection-token support. Do not copy an arbitrary notification token into every text field and expect it to resolve.

## Test missing data

Send a guest test order and a member test order. Check optional address fields, missing shipping for exempt products, translated labels, and an empty payment note.

If a token remains visible, check its spelling, the notification type, and the field where it was inserted. If it becomes empty, check whether the source data exists in that context.
