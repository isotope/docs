# Checkbox-Menü

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


## Optionen

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
        	<td>Optionen-Quelle</td>
        	<td>-</td>
        	<td>Hier kannst du auswählen, woher die Optionen für dieses Feld genommen werden sollen.<br>Zur Auswahl stehen:<br>
        	<ul>
        	<li>Attribut-Name (Einzelauswahl)</li>
        	<li>Optionen-Manager</li>
        	<li>Eigene Datanbank-Tabelle (foreignKey)</li>
        	<li>Optionen-Assistent (veraltet)</li>
        	</ul>
        	</td>
        </tr>
        <tr>
        	<td colspan="3">Optionen-Manager</td>
        </tr>
        <tr>
        	<td>Option bearbeiten</td>
        	<td>-</td>
        	<td>Füge dem Feld eine Option hinzu.</td>
        </tr>
        <tr>
        	<td>Neue Option</td>
        	<td>-</td>
        	<td>Lege eine neue Option an.</td>
        </tr>
        <tr>
            <td>Gruppe</td>
            <td>-</td>
            <td>Hier kannst du Option gruppieren (fügt der Option ein <code>optgroup</code> hinzu).</td>
        </tr>
        <tr>
            <td>Standard</td>
            <td>-</td>
            <td>Hier kannst du ein Option vorauswählen (fügt der Option ein <code>selected</code> hinzu).</td>
        </tr>
        <tr>
            <td>Bezeichnung</td>
            <td>-</td>
            <td>Hier kannst du bestimmen welche Bezeichnung die Option im Backend oder Frontend angezeigt werden soll.</td>
        </tr>
        <tr>
        	<td>Preisaufschläge oder -abschläge</td>
        	<td>-</td>
        	<td>Du kannst einen positiven oder negativen Wert eingeben, um den Produkt-Preis bei Auswahl dieser Option zu ändern.</td>
        </tr>
        <tr>
        	<td>Veröffentlicht</td>
        	<td>-</td>
        	<td>Diese Option im Produkt verfügbar machen.</td>
        </tr>
        <tr>
        	<td colspan="3">Eigene Datanbank-Tabelle (foreignKey)</td>
        </tr>
       <tr>
            <td>Fremdtabelle und Feld</td>
            <td>-</td>
            <td>Anstelle von Optionen können auch Daten aus der Datenbank ausgelesen werde. Eine mögliche Abfrage, nach dem Anlegen der Datenbanktabelle und Datenfeldern,  könnte wie folgt aussehen:<br><code># Datenbankfeld für die Fallback-Sprache<br>tl_meine_tabelle.mein_feld<br># Datenbankfeld für die Deutsche-Sprache<br>de=tl_meine_tabelle.mein_feld_de<br># Datenbankfeld für die Französische-Sprache<br>fr=tl_meine_tabelle.mein_feld_fr</code></td>
        </tr>
        <tr>
        	<td colspan="3">Optionen-Assistent (veraltet)</td>
        </tr>
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
            <td> 	Hier kannst du ein Option vorauswählen (fügt der Option ein <code>checked</code> hinzu).</td>
        </tr>
        <tr>
            <td>Gruppe</td>
            <td>-</td>
            <td>Checkboxen können nicht gruppiert werden.</td>
        </tr>
     </tbody>
</table>

<docrobot_message type="info"><p>Tipp: zum bequemen Anlegen und Pflegen von Fremdtabellen und Feldern eignet sich <a href="https://now.metamodel.me/" target="_blank">MetaModels</a> vorzüglich.</p></docrobot_message>


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
            <td>Macht, dass das Feld im Backend als Filter genutzt werden kann.</td>
        </tr>
    </tbody>
</table>

Die Ausgabe des angelegten Attributs im Backend erfolgt über die <docrobot_route name="product-types">Produkttypen</docrobot_route>. Wenn du das Checkbox-Menü `Durch den Kunden auswählbar` gemacht hast wird es automatisch im Frontend (mittels `$this->options` im Template) angezeigt. Andernfalls kannst du im gewünschten Isotope-Template das Attribut mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` ausgeben.

[1]: https://now.metamodel.me/
[2]: https://github.com/menatwork/MultiColumnWizard/issues/93