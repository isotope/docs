# Tipps und Tricks


## Bestellungen mit zusätzlichem Attribut im Backend ausgeben

Lege ein Attribut mit folgenden Eigenschaften an:

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Wert</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Name</td>
            <td>Lieferbar</td>
        </tr>
        <tr>
            <td>Interner Name</td>
            <td>lieferbar</td>
        </tr>
        <tr>
            <td>Typ</td>
            <td>Radio-Button-Menü</td>
        </tr>
        <tr>
            <td>Options Wizard</td>
            <td>
            	<table>
    				<thead>
        				<tr>
            				<th>Wert</th>
            				<th>Bezeichnung</th>
        				</tr>
    				</thead>
    				<tbody>
        				<tr>
        					<td>Ja</td>
        					<td>Ja</td>
        				</tr>
        				<tr>
        					<td>Nein</td>
        					<td>Nein</td>
        				</tr>
        			</tbody>
        		</table>
            </td>
        </tr>
     </tbody>
</table>

Danach das Attribut im Produkttyp aktivieren.

Folgenden Code in deine `system/config/dcaconfig.php` kopieren.

```php
if(is_array($GLOBALS['TL_DCA']['tl_iso_product']['list']['label']['fields']))
{
    if(!in_array('lieferbar',$GLOBALS['TL_DCA']['tl_iso_product']['list']['label']['fields']))
        $GLOBALS['TL_DCA']['tl_iso_product']['list']['label']['fields'][] = 'lieferbar'; 
} 
```

Das Resultat
<docrobot_image path="tips-and-tricks/attribut_im_backend.png" alt="Bestellungen mit zusätzlichem Attribute im Backend ausgeben">

Herzlichen Dank an <a href="https://community.contao.org/de/member.php?9203-Spooky" target="_blank">Spooky</a>.



## Bestellungen mit Uhrzeit im Backend ausgeben 

Folgenden Code in deine `system/config/dcaconfig.php` kopieren.

```php
$GLOBALS['TL_DCA']['tl_iso_product_collection']['fields']['locked']['eval']['rgxp'] = 'datim';
```

Vorher
<docrobot_image path="tips-and-tricks/order_list_date.png" alt="Bestellungen mit Datum im Backend">

Nachher
<docrobot_image path="tips-and-tricks/order_list_datim.png" alt="Bestellungen mit Datum und Uhrzeit im Backend">



## Staffelpreis-Tabelle in der Produktansicht ausgeben

Folgenden Code an der gewünschten Stelle in die `iso_reader_default.html5` kopieren.

```php
<?php echo $this->generateAttribute('price_tiers'); ?>
```

<docrobot_image path="tips-and-tricks/staffelpreis_tabelle.png" alt="Staffelpreis-Tabelle in der Produktansicht ausgeben">