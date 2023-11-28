---
title: "preOrderStatusUpdate"
---

The `preOrderStatusUpdate` hook is called before the order status is updated.

## Parameters

1. \Isotope\Model\ProductCollection\Order `$order` 

   The order model.

2. \Isotope\Model\OrderStatus `$newStatus`

    The new order status.

3. `array $updates`

    The order status updates.

## Return Values

Return `true` to cancel the order status change.

## Example

```php
// src/EventListener/Isotope/PreOrderStatusUpdateListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\OrderStatus;
use Isotope\Model\ProductCollection\Order;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("preOrderStatusUpdate")
 */
class PreOrderStatusUpdateListener
{
    public function __invoke(Order $order, OrderStatus $newsStatus, array $updates): bool
    {
        // Cancel the order status change if the order is not paid.
        if (!$order->isPaid()) {
            return true;
        }

        return false;
    }
}
```

## References

* [\Isotope\Model\ProductCollection\Order#L308-L318](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection/Order.php##L308-L318)