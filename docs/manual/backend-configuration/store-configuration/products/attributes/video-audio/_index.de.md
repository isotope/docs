---
title: "Video/Audio"
description: "Die Shop-Konfiguration - Video/Audio."
aliases:
    - /de/backend-konfiguration-shop-Attribute-Video-Audio/
weight: 145   
---


{{< version "2.2" >}}

Dieses Attribut verhält sich identisch wie das vom Contao Core bekannte Inhaltselement.
Damit kannst du also problemlos Videos oder Audiodateien für die Produktpräsentation verwenden.

{{% notice warning %}}<p>Das <em>j_mediaelement</em>-Template muss im Seitenlayout eingebunden sein.</p>{{% /notice %}}

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
            <td>Basisverzeichnis</td>
            <td>-</td>
            <td>Lege hier fest, ab welchem Verzeichnis die Ordnerstruktur angezeigt werden soll.</td>
        </tr>
        <tr>
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Das Produkt kann ohne die Angabe nicht gespeichert werden (Backend) bzw. in den Warenkorb gelegt werden (Frontend).</td>
        </tr>
        <tr>
        	<td>Mehrsprachig</td>
        	<td>-</td>
        	<td>Wähle ob dieses Attribut in andere Sprachen übersetzt werden muss.</td>
        </tr>
    </tbody>
</table>

Das Anlegen des Attributs im Backend erfolgt über die [Produkttypen](/de/backend-konfiguration-shop-Produkttypen/). Im Fontend kannst du das Attribut im gewünschten Isotope-Template mit folgendem Code `<?php echo $this->generateAttribute('interner_name'); ?>` ausgeben.

Dem Attribut lassen sich ausserdem weitere Optionen übergeben:

    <?php
    $arrOptions = array();
    $arrOptions['autoplay'] = true; // Video automatisch abspielen
    $arrOptions['width'] = 640; // Breite des Video-Players
    $arrOptions['height'] = 480; // Höhe des Video-Players

    echo $this->generateAttribute('interner_name', $arrOptions);
    ?>

{{% notice info %}}
  Folgende Video und Audio-Dateien werden unterstützt: **mp4**, **m4v**, **mov**, **wmv**, **webm**, **ogv**, **m4a**, **mp3**, **wma**, **mpeg**, **wav** und **ogg**.<br>
  Zusätzlich kannst du ein Standbild für das Video oder die Audio-Datei in den folgenden Formaten hinterlegen: **jpg**, **jpeg**, **gif**, **png**, **tif**, **tiff** und **bmp**.
{{% /notice %}}
