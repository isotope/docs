---
title: "convertCurrency"
---

The `convertCurrency` hook will be triggered if your [store configuration](/en/backend-configuration/store-configuration/general-settings/configuration/#currency-conversion)
uses custom currency conversion provider (i.e. other than `ecb.int` or `admin.ch` that Isotope ships by default).
This hook will be triggered by Isotope Automator according to cronjob schedule (`daily` by default),
and this is where you should pull the up-to-date exchange rate and save it to the database.

## Parameter

1. \Isotope\Model\Config `$config`
   
    The instance of the `Config` model. The hook is called once for each store config that
    has custom provider set up.

## Example

```php
// contao/config/config.php
$GLOBALS['TL_DCA']['tl_iso_config']['fields']['currencyProvider']['options'][] = 'cbr_ru';
```

```php
// src/EventListener/Isotope/ConvertCurrencyListener.php
namespace App\EventListener\Isotope;

use Isotope\Model\Config;
use Isotope\ServiceAnnotation\IsotopeHook;
use Psr\Log\LoggerInterface;
use Symfony\Contract\HttpClient\HttpClientInterface;

/**
 * @IsotopeHook("convertCurrency")
 */
class ConvertCurrencyListener 
{
    private HttpClientInterface $client;
    private LoggerInterface $logger;

    public function __construct(HttpClientInterface $client, LoggerInterface $contaoErrorLogger) {
        $this->client = $client;
        $this->logger = $contaoErrorLogger;
    }

    public function __invoke(Config $config): void
    {
        // Query custom exchange rate provider
        if ('cbr_ru' != $config->currencyProvider) {
            return;
        }

        try {
            $response = $this->client->request('GET', 'https://www.cbr.ru/scripts/XML_daily.asp');
        } catch (\Exception $e) {
            $this->logger->error('Error retrieving data from cbr.ru: ' . $e->getMessage());

            return;
        }

        // Process API response...
        $fltCourse = ...;
        $fltCourseOrigin = ...;

        // Save updated exchange rate
        $config->priceCalculateFactor = round($fltCourse / $fltCourseOrigin, 10);
        $config->save();
    }
}
```

## References

* [\Isotope\Automator#L170-L177](https://github.com/isotope/core/blob/2.8/system/modules/isotope/library/Isotope/Automator.php#L170-L177)
