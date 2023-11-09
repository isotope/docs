---
title: "preCheckout"
hidden: true
---

The `preCheckout` hook is called before the checkout process is started.
It allows to abort the checkout process.

## Parameters

1. \Isotope\Model\ProductCollection\Order|null `$order`
   
    The order object.

1. \Isotope\Module\Checkout `$module`
   
    The checkout module.

## Return Values

The hook must return a boolean value. If `false` is returned, the checkout process is aborted.

## Example

```php
// src/EventListener/Isotope/PreCheckoutListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\ProductCollection\Order;
use Isotope\Module\Checkout;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("preCheckout")
 */
class PreCheckoutListener
{
    public function __invoke(?Order $order, Checkout $module): bool
    {
        if (!$order) {
            return true;
        }
        
        if (count($order->getItems()) > 5) {
            // only allow max 5 articles per order
            return false;
        }

        return true;
    }
}
```

## References

* [\Isotope\Model\ProductCollection\Order#L235-L244](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection/Order.php#L235-L244)