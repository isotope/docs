---
title: "Hooks"
description: "Developer Reference for Isotope Hooks."
weight: 10
---

Hooks are entry points into the Isotope core (and some of its extension bundles). Have a look at the hook list of all available hooks. You can register your own callable logic that will be executed as soon as a certain point in the execution flow of the core will be reached. 


{{%expand "Registering hooks listeners" %}}

## Registering hooks listeners

There are two ways of registering hook listeners for isotope.

### Service annotations

{{< version "2.8" >}}

The recommended way of registering hooks is to use service annotations:

```php
// src/EventListener/Isotope/AddProductToCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Interfaces\IsotopeProduct
use Isotope\Interfaces\IsotopeProductCollection;
use Isotope\ServiceAnnotation\IsotopeHook;

class AddProductToCollectionListener
{
    /**
     * @IsotopeHook("addProductToCollection")
     */
    public function __invoke(IsotopeProduct $product, $quantity, IsotopeProductCollection $collection, array $config): int
    {
        // Your logic here

        return $quantity;
    }
}
```

The legacy way of registering hooks is to register them in the global array in your `config.php` files:

```php
// config/config.php
use App\EventListener\Isotope\AddProductToCollectionListener;

$GLOBALS['ISO_HOOKS']['addProductToCollection'][] = [AddProductToCollectionListener::class, '__invoke'];
```

```php
// src/EventListener/Isotope/AddProductToCollectionListener.php
namespace App\EventListener\Isotope;

use Isotope\Interfaces\IsotopeProduct
use Isotope\Interfaces\IsotopeProductCollection;

class AddProductToCollectionListener
{
    public function __invoke(IsotopeProduct $product, $quantity, IsotopeProductCollection $collection, array $config): int
    {
        // Your logic here

        return $quantity;
    }
}
```
{{% /expand%}}

## Reference

This is a list of all hooks available in isotope (as of version 2.8):

- addAssetImportRegexp
- addCollectionToTemplate
- [addProductToCollection](addProductToCollection)
- applyAdvancedFilters
- calculatePrice
- collectionLocked
- compileCart
- convertCurrency
- copiedCollectionItems
- copyCollectionItem
- createFromProductCollection
- deleteCollection
- deleteItemFromCollection
- downloadFromProductCollection
- emailRecipientForCollection
- findCategories
- findSurchargesForCollection
- generateDocumentNumber
- generateDocumentTemplate
- generateFilters
- generateOrderLog
- [generateProduct](generateProduct)
- generateProductList
- getAllowedProductIds
- getOrderConditionsValue
- getOrderNotificationTokens
- initializePostsale
- itemIsAvailable
- modifyAddressFields
- [postAddProductToCollection](postAddProductToCollection)
- [postCheckout](postCheckout)
- postDeleteCollection
- postDeleteItemFromCollection
- postOrderStatusUpdate
- postUpdateItemInCollection
- postUpdateProductInCollection
- [preCheckout](preCheckout)
- [preOrderStatusUpdate](preOrderStatusUpdate)
- priceDisplay
- productIsAvailable
- saveCollection
- updateAddressData
- updateDraftOrder
- [updateItemInCollection](updateItemInCollection)
- updateProductInCollection
- useTaxRate