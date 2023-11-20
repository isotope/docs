---
title: "postAddProductToCollection"
---

The `postAddProductToCollection` hook is triggered after a product is added to the cart and can be used to perform additional actions.


## Parameters

1. \Isotope\Interfaces\IsotopeProduct `$product`
   
    The product that was added to the collection.

2. int `$quantity`
   
    The quantity of the product that was added to the collection.

3. \Isotope\Interfaces\IsotopeProductCollection `$collection`
   
    The collection the product was added to.

4. array `$config`
   
    The model configuration.

## Example

```php
// src/EventListener/Isotope/PostAddProductToCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Interfaces\IsotopeProduct;
use Isotope\Interfaces\IsotopeProductCollection;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("postAddProductToCollection")
 */
class PostAddProductToCollectionListener 
{
    public function __invoke(IsotopeProduct $product, $quantity, IsotopeProductCollection $collection, array $config): void
    {
        // Do something …
    }
}
```

## References

* [\Isotope\Model\ProductCollection#L1112-L1118](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection.php#L1112-L1118)