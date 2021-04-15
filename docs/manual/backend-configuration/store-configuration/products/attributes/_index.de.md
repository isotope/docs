---
title: "Attribute"
description: "Die Shop-Konfiguration - Attribute."
aliases:
    - /de/backend-konfiguration-shop-Attribute/
weight: 110    
---


In der Grundinstallation verfügt Isotope eCommerce bereits über die wichtigsten Attribute, welche für den Betrieb eines Shops normalerweise benötigt werden. Sollte dir dennoch Attribute für dein Projekt fehlen, kannst du sie unter `Attribute` anlegen und im 
[Produkttyp](/de/backend-konfiguration-shop-Produkttypen/) konfigurieren.

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
            <li>Video/Audio</li>
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
            ![Feldgruppen beim Anlegen eines neuen Produktes](feldgruppen.png)
            </td>
        </tr>
    </tbody>
</table>

Auf die Konfiguration der einzelnen Feldtypen wird in den Unterpunkten eingegangen.

{{% children showhidden="false" %}}
