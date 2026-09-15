# Events and lifecycle

Events let a service observe or enrich an existing process. Choose the event by its dispatch location and timing, not only its class name.

## Useful event families

| Event | Purpose |
| --- | --- |
| `Store\Event\ContextCreatedEvent` | Work with newly created store context |
| `Product\Event\ProductCreatedEvent` | Observe a constructed product object and its data/context |
| `Product\Event\ProductConfigurationEvent` | Work with product configuration for rendering |
| `Product\Event\ProductPriceEvent` | Inspect or alter a calculated product price |
| `Checkout\Event\CheckoutStepEvent` | Enrich or validate a checkout step |
| `Store\Event\OrderValidationEvent` | Add constraints to order validation |
| `Store\Event\CollectOrderNotificationTokensEvent` | Add order-notification tokens |

These names are relative to `Isotope\CoreBundle`. `ProductCreatedEvent` describes product object construction. Do not assume it means a merchant has just inserted a new catalog record.

## Example: add a notification token

In an application with service autoconfiguration enabled, a focused listener can add a static support message:

```php
<?php

declare(strict_types=1);

namespace App\EventListener;

use Isotope\CoreBundle\Store\Event\CollectOrderNotificationTokensEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener]
final class OrderSupportTokenListener
{
    public function __invoke(CollectOrderNotificationTokensEvent $event): void
    {
        $event->addToken('support_message', 'Reply to this email if you need help.');
    }
}
```

The event is intentionally enriched through its mutating `addToken()` method. If Notification Center validates token names for the message field, also extend the notification type's allowed token definition before using `##support_message##` there. Verify registration, allowed-token validation, and a delivered message in a complete Contao application.

Do not put credentials or unnecessary customer data into a token. For multilingual messages, translate using the appropriate order context rather than hard-coding the English example.

## Checkout validation

`CheckoutStepEvent` exposes the step type, request, context, editing/submission state, and an error flag. It also supports markup before and after the step. Inspect whether your listener is running for address, shipping, payment, or `_summary`.

`OrderValidationEvent` accepts Symfony validation constraints. Use it for validation of order data rather than replacing an entire checkout controller for one check.

## Transaction lifecycle events

Isotope's transaction dispatcher uses named phases:

- `<name>.pre` before the operation.
- `<name>.error` when the wrapped operation throws.
- `<name>.post` after the dispatcher finishes the operation/handled-error path.

For example, `OrderTransactionEvent::NAME` is `isotope.order`, while `OrderStatusTransactionEvent::NAME` is `isotope.order_status`.

These phases are dispatched under explicit string names. Subscribe to the actual phase name when using them, not only to the event class. The dispatcher can let an error listener supply a result, so a post event alone should not be interpreted as proof of payment success or a generic database after-commit guarantee.

## External side effects

For accounting, fulfillment, and provider integrations, define retry and duplicate handling around a stable order/transaction reference. Validate payment evidence at the provider boundary. Avoid sending irreversible external actions from a phase that can run before persistence succeeds.

Sources: [transaction dispatcher](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/EventDispatcher/TransactionEventDispatcher.php), [notification-token event](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Event/CollectOrderNotificationTokensEvent.php).
