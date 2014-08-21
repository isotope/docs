# Video/Audio

<docrobot_new_in_version version="2.2"><p>Dieses Feature ist neu in Isotope eCommerce 2.2</p></docrobot_new_in_version>

Dieses Attribut verhält sich identisch wie das vom Contao Core bekannte Inhaltselement.
Damit kannst du also problemlos Videos oder Audiodateien für die Produktpräsentation verwenden.

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
    </tbody>
</table>

Das Anlegen des Attributs im Backend erfolgt über die <docrobot_route name="product-types">Produkttypen</docrobot_route>. Im Fontend kannst du das Attribut im gewünschten Isotope-Template mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` ausgeben.