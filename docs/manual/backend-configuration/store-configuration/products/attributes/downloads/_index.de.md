---
title: "Downloads"
description: "Die Shop-Konfiguration - Downloads."
aliases:
    - /de/backend-konfiguration-shop-Attribute-Downloads/
weight: 135   
---


Hier kannst du deinem Produkt ein Element vom Typ `Download/Downloads` hinzufügen, z. B. Produktdetails als PDF.

## Beschreibung

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
            <td>Beschreibung</td>
            <td>-</td>
            <td>Dieses Beschreibung dient dem Backend-Nutzer als Hinweis und wird unter dem Eingabefeld ausgegeben.</td>
        </tr>
    </tbody>
</table>


## Attribut-Konfiguration

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
            <td>Feld-Typ</td>
            <td>Checkbox</td>
            <td>Hier kannst du einstellen ob eine Datei (Radio-Button) oder mehrere Dateien (Checkbox) gewählt werden können.</td>
        </tr>
    	<tr>
            <td>Sortieren nach</td>
            <td>Eigene Reihenfolge</td>
            <td>Hier kannst du eine Sortierreihenfolge für die Ausgabe im Fontend auswählen, folgende stehen dir zur Verfügung. Bei der Auswahl von <code>Eigene Reihenfolge</code> kannst du die Reihenfolge beim <docrobot_route name="product-management">Anlegen des Produktes</docrobot_route> im Backend per Drag & Drop verändern.
            <ul>
            <li>Eigene Reihenfolge</li>
            <li>Dateiname (aufsteigend)</li>
            <li>Dateiname (absteigend)</li>
            <li>Datum (aufsteigend)</li>
            <li>Datum (absteigend)</li>
            <li>Zufällige Reihenfolge</li>
            </ul>
            </td>
        </tr>
    	<tr>
            <td>Basisverzeichnis</td>
            <td>-</td>
            <td>Lege hier fest, ab welchem Verzeichnis die Ordnerstruktur angezeigt werden soll.</td>
        </tr>
        <tr>
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Hier kannst du das Feld im Backend zum Pflichtfeld machen.</td>
        </tr>
        <tr>
        	<td>Mehrsprachig</td>
        	<td>-</td>
        	<td>Wähle ob dieses Attribut in andere Sprachen übersetzt werden muss (z.B. Textfelder).</td>
        </tr>
    	<tr>
            <td>Dateien anzeigen</td>
            <td>-</td>
            <td>Falls du diese Auswahl getroffen hast, werden Dateien und nicht nur Ordner angezeigt.</td>
        </tr>
        <tr>
            <td>Als Galerie markieren</td>
            <td>-</td>
            <td>Ermöglicht eine bessere Ansicht im Backend.</td>
        </tr>
	</tbody>
</table>

Die Ausgabe des angelegten Attributs im Backend erfolgt über die [Produkttypen](/de/backend-konfiguration-shop-Produkttypen/). Im Fontend kannst du das Attribut im gewünschten Isotope-Template mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` ausgeben.
