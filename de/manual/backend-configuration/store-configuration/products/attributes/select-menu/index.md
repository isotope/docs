# Select-Menü

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
            <td>Für Varianten verwenden</td>
            <td>-</td>
            <td>Hier kannst du das Attribut für die Konfiguration von Produktvarianten zur Verfügung stellen.</td>
        </tr>
        <tr>
            <td>Durch den Kunden auswählbar</td>
            <td>-</td>
            <td>Dieses Feld musst du auswählen, falls der Kunde im Frontend die Möglichkeit haben sollte, eine Eingabe zu tätigen.</td>
        </tr>       
    </tbody>
</table>


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


# Optionen

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
            <td>Wert</td>
            <td>-</td>
            <td>Hier kannst du den Wert der Option eingeben, welcher beim Absenden des Formulars übertragen werden soll.</td>
        </tr>
        <tr>
            <td>Bezeichnung</td>
            <td>-</td>
            <td>Hier kannst du bestimmen welche Bezeichnung die Option im Backend oder Frontend angezeigt werden soll.</td>
        </tr>      
        <tr>
            <td>Standard</td>
            <td>-</td>
            <td>Hier kannst du ein Option vorauswählen (fügt der Option ein <code>selected</code> hinzu).</td>
        </tr>
        <tr>
            <td>Gruppe</td>
            <td>-</td>
            <td>Hier kannst du Option gruppieren (fügt der Option ein <code>optgroup</code> hinzu).</td>
        </tr>
        <tr>
            <td>Fremdtabelle und Feld</td>
            <td>-</td>
            <td>Anstelle von Optionen können auch Daten aus der Datenbank ausgelesen werde. Eine mögliche Abfrage, nach dem Anlegen der Datenbanktabelle und Datenfeldern,  könnte wie folgt aussehen:<br><code># Datenbankfeld für die Fallback-Sprache<br>tl_meine_tabelle.mein_feld<br># Datenbankfeld für die Deutsche-Sprache<br>de=tl_meine_tabelle.mein_feld_de<br># Datenbankfeld für die Französische-Sprache<br>fr=tl_meine_tabelle.mein_feld_fr</code></td>
        </tr>
     </tbody>
</table>

<docrobot_message type="info"><p>Kleiner Tipp: zum bequemen Anlegen und Pflegen von Fremdtabellen und Feldern eignet sich [MetaModels][1] vorzüglich.</p></docrobot_message>

<docrobot_message type="warning"><p>Die Standard- und Gruppenfunktion ist im Moment nicht funktionstüchtig.</p></docrobot_message>

<docrobot_message type="warning"><p>Die "falsche" Platzierung des Titels `Bezeichnung` ist der Erweiterung "MultiColumnWizard" geschuldet und wurde auf [GitHub gemeldet][2].</p></docrobot_message>


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
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Falls <code>Durch den Kunden auswählbar</code> ausgewählt ist kann das Produkt ohne die Angabe nicht in den Warenkorb gelegt werden. Ansonsten wird das Feld beim Anlegen eines Produktes als Pflichtfeld im Backend ausgegeben.</td>
        </tr>
        <tr>
            <td>Mehrfach-Auswahl</td>
            <td>-</td>
            <td>Ermöglicht dem Nutzer mehr als eine Option auszuwählen.</td>
        </tr>      
        <tr>
            <td>Listengröße</td>
            <td>5</td>
            <td>Sobald `Mehrfach-Auswahl` ausgewählt ist, kannst du hier die Grösse der Auswahlbox bestimmen.</td>
        </tr> 
     </tbody>
</table>



## Suche- & Filter-Einstellungen

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
            <td>Filterbar im Frontend</td>
            <td>-</td>
            <td>Sobald dieses Feld ausgewählt wurde, kann dieses Attribut im Frontend als Filter genutzt werden.</td>
        </tr>
        <tr>
            <td>Zur "Sortieren nach"-Optionsliste hinzufügen</td>
            <td>-</td>
            <td>Macht das Feld, falls es im Backend gepflegt wurde und für den Kunden sichtbar ist, im Listenmodul sortierbar.</td>
        </tr>
        <tr>
            <td>Filterbar im Backend</td>
            <td>-</td>
            <td>Sobald dieses Feld ausgewählt wurde, kann dieses Attribut im Backend als Filter genutzt werden.</td>
        </tr>
        <tr>
            <td>Durchsuchbar im Frontend</td>
            <td>-</td>
            <td>Macht das Feld, falls es im Backend gepflegt wurde, für die Suchmaschine durchsuchbar.</td>
        </tr>
    </tbody>
</table>

Die Ausgabe des angelegten Attributs im Backend erfolgt über die <docrobot_route name="product-types">Produkttypen</docrobot_route>. Wenn du das Textfeld `Durch den Kunden auswählbar` gemacht hast, kannst du das Attribut im Template `iso_reader_default.html5` mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` an der gewünschten Stelle ausgeben. Wurde `für Varianten verwenden`ausgewählt und mindestens eine Variante dem Produkt hinzugefügt, werden diese automatisch im Frontend ausgegeben. Es ist in diesem Fall also keine Template Anpassung notwendig. 


[1]: https://now.metamodel.me/
[2]: https://github.com/menatwork/MultiColumnWizard/issues/93