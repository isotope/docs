---
title: "modifyAddressFields"
---

The `modifyAddressFields` hook is triggered by "Billing Address" and "Shipping Address"
checkout steps. Each checkout step triggers the hook twice – first when address form is
being rendered, then upon submit when fields are validated.

It can be used to modify fields configuration, add or remove fields, or do something with
the submitted values.

## Parameters

1. array `$fields`
   
    Array of form fields configurations (similar to DCA).

2. \Isotope\Model\Address `$address`
   
    Instance of the Address model.

3. string `$class`
   
    Standardized version of the current CheckoutStep class, that can be used in CSS context,
    e.g. `'billingaddress'`

## Return value

Return the `$fields` array.

## Example

```php
// src/EventListener/Isotope/ModifyAddressFieldsListener.php
namespace App\EventListener\Isotope;

use Contao\Input;
use Isotope\Model\Address;
use Isotope\ServiceAnnotation\IsotopeHook;

/**
 * @IsotopeHook("modifyAddressFields")
 */
class ModifyAddressFieldsListener 
{
    public function __invoke(array $fields, Address $address, string $class): array
    {
        // Normalize email addresses to lower-case form
        if (Input::post('FORM_SUBMIT') === 'iso_mod_checkout_billingaddress') {
            Input::setPost('billingaddress_email', strtolower(Input::post('billingaddress_email')));
        }
        
        return $fields;
    }
}
```

## References

* [\Isotope\CheckoutStep\Address#L238-L245](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/CheckoutStep/Address.php#L238-L245)
