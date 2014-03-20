# Medienverwaltung

<docrobot_image path="backend-configuration/store-configuration/products/attributes/media-manager/medienverwaltung_backend.png" alt="Medienverwaltung im Backend">

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


Die Ausgabe des angelegten Attributs im Backend erfolgt über die <docrobot_route name="product-types">Produkttypen</docrobot_route>. Um die Dateien im Frontend anzuzeigen genügt folgender Code `<?php echo $this->getGallery('InternerName')->generateMainImage(); ?>` an der gewünschten Stelle im `iso_reader_default.html5` Template.
