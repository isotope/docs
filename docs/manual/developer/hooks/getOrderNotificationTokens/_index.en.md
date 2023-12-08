---
title: "getOrderNotificationTokens"
---

The `getOrderNotificationTokens` hook is invoked each time when order notifications
are triggered, for instance on checkout or order status update. It can be used to
update the values of [simple tokens](/en/simple-tokens) or add custom ones.


## Parameters

1. Isotope\Model\ProductCollection\Order `$order`
   
    The order object.

2. array `$tokens`
   
    The notification center tokens.

## Return values

Return array of notification tokens with their values

## Example

```php
// src/EventListener/Isotope/PostAddProductToCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\ProductCollection\Order;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("postAddProductToCollection")
 */
class PostAddProductToCollectionListener 
{
    public function __invoke(Order $order, array $tokens): array
    {
        // Add ##first_product## token that displays the name of the first product in cart
        $products = $order->getItems();
        $firstProduct = reset($products);
        
        $tokens['first_product'] = $firstProduct->getName();
        
        return $tokens;
    }
}
```

## References

* [\Isotope\Model\ProductCollection\Order#L545-L552](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection/Order.php#L545-L552)
