---
title: "postCheckout"
---

The `postCheckout` hook is called after the checkout process is finished.

## Parameters

1. \Isotope\Model\ProductCollection\Order `$order`
   
    The order object.

2. `array $tokens`

    The notification center tokens.

## Example

```php
// src/EventListener/Isotope/PostCheckoutListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\ProductCollection\Order;
use Isotope\Module\Checkout;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("postCheckout")
 */
class PostCheckoutListener
{
    public function __invoke(Order $order, array $tokens): void
    {
        // Do something ...
    }
}
```

## References

* [\Isotope\Module\Checkout#L236-L245](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Module/Checkout.php#L236-L245)
