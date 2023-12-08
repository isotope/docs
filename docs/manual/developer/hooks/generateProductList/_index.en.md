---
title: "generateProductList"
---

The `generateProductList` hook is called when the product list page is rendered.
It can be used to add custom context variables to the products list page, filter
rendered products or even to modify parsed HTML directly.

## Parameters

1. array `$buffer`
   
    Array that holds information used to render each product in the list.
    Array items have the following shape:

    ```php
    [
        'cssID' => '', // HTML "id" attribute
        'class' => '', // HTML "class" attribute
        'html' => '', // parsed product template (iso_reader_default.html5)
        'product' => \Isotope\Model\Product // product model
    ]
    ```

2. array `$products`
   
    Array of product models.

3. \Contao\Template `$template`

    Frontend template instance that is used to render `mod_iso_productlist` template.

4. \Isotope\Module\ProductList `$module`

    Instance of `ProductList` frontend module.

## Return values

Return the `$buffer` array.

## Example

```php
// src/EventListener/Isotope/GenerateProductListListener.php
namespace App\EventListener\Isotope;

use Contao\Template;
use Isotope\Module\ProductList;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("generateProductList")
 */
class GenerateProductListListener
{
    public function __invoke(array $buffer, array $products, Template $template, ProductList $module): array
    {
        // Do something ...

        return $buffer;
    }
}
```

## References

* [\Isotope\Module\ProductList#L286-L293](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Module/ProductList.php#L286-L293)
