# Tipps und Tricks

## Bestellungen mit Uhrzeit im Backend ausgeben 

Folgenden Code in deine `system/config/dcaconfig.php` kopieren.

    $GLOBALS['TL_DCA']['tl_iso_product_collection']['fields']['locked']['eval']['rgxp'] = 'datim';



Vorher
<docrobot_image path="tips-and-tricks/order_list_date.png" alt="Bestellungen mit Datum im Backend">

Nachher
<docrobot_image path="tips-and-tricks/order_list_datim.png" alt="Bestellungen mit Datum und Uhrzeit im Backend">