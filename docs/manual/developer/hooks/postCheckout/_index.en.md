---
title: "postCheckout"
---

The `postCheckout` hook is called after the checkout process is finished.
It can be used e.g. to store additional information about the order, process
analytics etc.

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
use MailchimpMarketing\ApiClient;

/**
 * @IsotopeHook("postCheckout")
 */
class PostCheckoutListener
{
    private ApiClient $mailchimp;
    
    public function __construct(ApiClient $mailchimp){
        $this->mailchimp = $mailchimp;
    }
    
    public function __invoke(Order $order, array $tokens): void
    {
        // Update customer's information on Mailchimp subscribers list
        $billingAddress = $order->getBillingAddress();
        
        $listMemberInfo = [
            'email_address' => $billingAddress->email,
            'merge_fields' => [
                'FNAME' => $billingAddress->firstname,
                'LNAME' => $billingAddress->lastname
            ]
        ];
        
        $this->mailchimp->lists->updateListMember(
            'listId',
            md5(strtolower($billingAddress->email)),
            $listMemberInfo
        );
    }
}
```

## References

* [\Isotope\Module\Checkout#L236-L245](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Module/Checkout.php#L236-L245)
