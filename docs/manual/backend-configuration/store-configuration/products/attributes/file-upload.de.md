---
title: "Datei-Upload"
description: "Die Shop-Konfiguration - Datei-Upload."
aliases:
    - /de/backend-konfiguration-shop-Attribute-Datei-Upload/
weight: 140   
---


Möchtest du deiner Kundin oder deinem Kunden ermöglichen eine Datei an dich zu übermitteln, hilft dir `Datei-Upload` weiter.

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
            <td>Erlaubte Dateitypen</td>
            <td>jpg,jpeg,gif,png</td>
            <td>Schränke die erlaubten Dateitypen anhand einer kommagetrennten Liste ein.</td>
        </tr>
    	<tr>
            <td>Maximallänge</td>
            <td>0</td>
            <td>Hier kannst du die Feldlänge auf eine bestimmte Zeichenanzahl (Text) oder Bytes (Datei-Upload) einschränken.</td>
        </tr>
        <tr>
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Hier kannst du das Feld im Frontend zum Pflichtfeld machen, somit kann das Produkt nicht ohne einen Wert in den Warenkorb gelegt werden.</td>
        </tr>
	</tbody>
</table>


## Datei speichern

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
            <td>Hochgeladene Dateien speichern</td>
            <td>-</td>
            <td>Hier kannst du einstellen, dass die hochgeladenen Datei in einen Ordner auf dem Server verschoben wird.</td>
        </tr>
        <tr>
            <td>Zielverzeichnis</td>
            <td>files/orders/##document_number##/##product_position##__{{flag::##product_name##|standardize}}/##attribute_field##</td>
            <td>Hier kannst du ein Zielverzeichnis im Contao Ordner <code>files</code> für die Datei bestimmen.</td>
        </tr>
    	<tr>
            <td>Ziel-Dateiname</td>
            <td>##file_target##</td>
            <td>Gebe den Ziel-Dateinamen ein. Benutze Simple Tokens und Inserttags um einen dynamischen Namen zu generieren.</td>
        </tr>
	</tbody>
</table>

Das Anlegen des Attributs im Backend erfolgt über die [Produkttypen](/de/backend-konfiguration-shop-Produkttypen/). Im Fontend kannst du das Attribut im gewünschten Isotope-Template mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` ausgeben.


[1]: https://github.com/isotope/core/issues/1039
