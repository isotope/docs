---
title: "updateItemInCollection"
hidden: true
---

The `updateItemInCollection` hook is called when an item is added or updated in the collection.

## Parameters

1. \Isotope\Model\ProductCollectionItem `$item` 
    
   The item that is added or updated.

2. array `$set`

    The set of data that is used to update the item.

3. \Isotope\Model\ProductCollection `$collection`

    The collection the item is added or updated in.


## Return Values

The return value is the set of data that is used to update the item.

## Example

```php
// src/EventListener/Isotope/UpdateItemInCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\ProductCollection;
use Isotope\Model\ProductCollectionItem;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("updateItemInCollection")
 */
class UpdateItemInCollectionListener
{
    
    public function __invoke(ProductCollectionItem $item, array $set, ProductCollection $collection): array
    {
        return $set;
    }
}
```

## References

* [\Isotope\Model\ProductCollection#L1198-L1208](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/ProductCollection.php#L1198-L1208)