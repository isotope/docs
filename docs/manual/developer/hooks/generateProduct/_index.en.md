---
title: "generateProduct"
---

The `generateProduct` hook is called when the product page (reader) is rendered. It allows to add custom information to the product page.

## Parameters

1. \Isotope\Template `$template`
   
    The template object.

2. \Isotope\Interfaces\IsotopeProduct `$product`
   
    The product model.

## Example

```php
// src/EventListener/Isotope/GenerateProductListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\Product\AbstractProduct;
use Isotope\ServiceAnnotation\IsotopeHook;
use Isotope\Template;

/**
 * @IsotopeHook("generateProduct")
 */
class GenerateProductListener
{
    public function __invoke(Template $template, IsotopeProduct $product): void
    {
        $template->customMessage = 'We currently have more orders than usual. Please expect longer waiting times.';
    }
}
```

## References

* [\Isotope\Model\Product\Standard#L643-L647](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Model/Product/Standard.php#L643-L647)
