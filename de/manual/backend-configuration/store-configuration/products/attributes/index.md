# Attribute

In der Grundinstallation verfügt Isotope eCommerce bereits über die wichtigsten Attribute, welche für den Betrieb eines Shops normalerweise benötigt werden. Sollte dir dennoch Attribute für dein Projekt fehlen, kannst du sie unter `Attribute` anlegen und im <docrobot_route name="product-types">Produkttyp</docrobot_route> konfigurieren.

Attribute sind zusätzliche Datenfelder, welche im Backend bei der Einpflege der Produkte zur Verfügung gestellt und danach im Frontend an gewünschter Stelle ausgegeben werden können. So kann zum Beispiel ein Farbauswahl-Select-Menü erstellt werden, in dem der Kunde im Frontend eine Farbe auswählen muss, bevor er das Produkt in den Warenkorb legen kann.

Nach klick auf `Neues Attribut` hast du folgende Einstellungsmöglichkeiten:

## Attribut-Name & -Typ

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Standardeinstellung</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Name</td>
            <td>-</td>
            <td>Hier gibst du dem Attribut einen aussagekräftigen Namen, dieser wird nur im Backend verwendet.</td>
        </tr>
        <tr>
            <td>Interner Name</td>
            <td>-</td>
            <td>Hier bestimmst du den Namen für das Datenbankfeld in der Datenbanktabelle <code>tl_iso_attribute</code>, dieser Wert muss einzigartig sein.
</td>
        </tr>
        <tr>
            <td>Typ</td>
            <td>-</td>
            <td>Hier kannst du den gewünschten Feldtyp für ein Attribut auswählen, Isotope eCommerce stellt dir folgende Typen zur Verfügung:
            <ul>
            <li>Textfeld</li>
            <li>Textarea</li>
            <li>Select-Menü</li>
            <li>Radio-Button-Menü</li>
            <li>Checkbox-Menü</li>
            <li>Medienverwaltung</li>
            <li>Dateibaum</li>
            <li>Downloads</li>
            <li>Datei-Upload</li>
            </ul>
</td>
        </tr>
        <tr>
            <td>Feldgruppe</td>
            <td>-</td>
            <td>Hier wird die Gruppierung für die Ausgabe im Backend beim Anlegen eines Produktes festgelegt. Du kannst dem Attribut folgenden Feldgruppen zuweisen:
            <ul>
            <li>Allgemeine Einstellungen</li>
            <li>Meta-Angaben</li>
            <li>Preis-Einstellungen</li>
            <li>Inventar-Einstellungen</li>
            <li>Versand-Einstellungen</li>
            <li>Produktoptionen-Einstellungen</li>
            <li>Dateiverwaltung</li>
            <li>Experten-Einstellungen</li>
            <li>Veröffentlichung</li>
            </ul>
            <docrobot_image path="images/feldgruppen.png" alt="Feldgruppen beim Anlegen eines neuen Produktes">
            </td>
        </tr>
    </tbody>
</table>



Auf die Konfiguration der einzelnen Feldtypen wird in den Unterpunkten eingegangen.

- <docrobot_route name="text-field">Textfeld</docrobot_route>
- <docrobot_route name="textarea">Textarea</docrobot_route>
- <docrobot_route name="select-menu">Select-Menü</docrobot_route>
- <docrobot_route name="radio-button-menu">Radio-Button-Menü</docrobot_route>
- <docrobot_route name="checkbox-menu">Checkbox-Menü</docrobot_route>
- <docrobot_route name="media-manager">Medienverwaltung</docrobot_route>
- <docrobot_route name="file-tree">Dateibaum</docrobot_route>
- <docrobot_route name="downloads">Downloads</docrobot_route>
- <docrobot_route name="file-upload">Datei-Upload</docrobot_route>


