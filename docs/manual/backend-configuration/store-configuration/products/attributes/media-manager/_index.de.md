---
title: "Medienverwaltung"
description: "Die Shop-Konfiguration - Medienverwaltung."
aliases:
    - /de/backend-konfiguration-shop-Attribute-Medienverwaltung/
weight: 125   
---


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
            <td>Hier kannst du ein kommagetrennte Liste erlaubter Dateitypen eingeben.</td>
        </tr> 
        <tr>
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Hier kannst du das Feld im Backend zum Pflichtfeld machen.</td>
        </tr>
  
     </tbody>
</table>


Die Ausgabe des angelegten Attributs im Backend erfolgt über die [Produkttypen](/de/backend-konfiguration-shop-Produkttypen/). Um die Dateien im Frontend anzuzeigen genügt folgender Code `<?php echo $this->getGallery('InternerName')->generateMainImage(); ?>` an der gewünschten Stelle im `iso_reader_default.html5` Template.
