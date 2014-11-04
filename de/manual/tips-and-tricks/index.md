# Tipps und Tricks

## Bestellungen mit Uhrzeit im Backend ausgeben 

Folgenden Code in deine `system/config/dcaconfig.php` kopieren.

    $GLOBALS['TL_DCA']['tl_iso_product_collection']['fields']['locked']['eval']['rgxp'] = 'datim';

Vorher
<docrobot_image path="tips-and-tricks/order_list_date.png" alt="Bestellungen mit Datum im Backend">

Nachher
<docrobot_image path="tips-and-tricks/order_list_datim.png" alt="Bestellungen mit Datum und Uhrzeit im Backend">



## Staffelpreis-Tabelle in der Produktansicht ausgeben

Folgenden Code an der gewünschten Stelle in die `iso_reader_default.html5` kopieren.

    <?php echo $this->generateAttribute('price_tiers'); ?>


<docrobot_image path="tips-and-tricks/staffelpreis_tabelle.png" alt="Staffelpreis-Tabelle in der Produktansicht ausgeben">