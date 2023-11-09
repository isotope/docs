---
title: "addProductToCollection"
hidden: true
---

The `addProductToCollection` hook is triggered every time a product is added to the cart.
It allows manipulating the number of items added to the cart.

## Parameters

1. \Isotope\Interfaces\IsotopeProduct `$product`
   
    The product that is added to the collection.

2. int `$quantity`
   
    The quantity of the product that is added to the collection.

3. \Isotope\Interfaces\IsotopeProductCollection `$collection`
   
    The collection the product is added to.

4. array `$config`
   
    The model configuration.

## Example

```php
// src/EventListener/Isotope/AddProductToCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Interfaces\IsotopeProduct;
use Isotope\Interfaces\IsotopeProductCollection;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("addProductToCollection")
 */
class AddProductToCollectionListener 
{
    public function __invoke(IsotopeProduct $product, $quantity, IsotopeProductCollection $collection, array $config): int
    {
        // example for allowing max 5 items per product
        if ($quantity > 5) {
            return 5;
        }
        return $quantity
    }
}
```

## References

* [\Isotope\Model\ProductCollection#L1053-L1059](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection.php#L1053-L1059)
