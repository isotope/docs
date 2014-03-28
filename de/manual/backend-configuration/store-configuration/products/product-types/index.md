# Produkttypen

Du musst mindestens ein Produkttyp anlegen.

## Produkttyp-Einstellungen

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
            <td>Wähle hier einen aussagekräftigen Namen für diesen Produkttyp, damit du auch bei mehreren die Übersicht behältst.</td>
        </tr>
        <tr>
            <td>Produktklasse</td>
            <td>Standard Produkt</td>
            <td>Über Dritterweiterungen können Entwickler Spezialfunktionen für Produkte realisieren. Die Standardfunktionen von Isotope eCommerce werden mit <code>Standard Produkt</code> abgedeckt.</td>
        </tr>
        <tr>
            <td>Standard</td>
            <td>-</td>
            <td>Ist dieses Feld aktiviert, wird beim Anlegen eines neuen Produktes automatisch dieser Produkttyp vorausgewählt.</td>
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
            <td>Hier kannst du Notizen zum Produkttyp hinterlegen, diese werden beim Anlegen eines neuen Produktes im Helpwizard (<docrobot_image path="images/helpwizard.gif" alt="Helpwizard Icon">) ausgegeben.</td>
        </tr>
    </tbody>
</table>


## Preise

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
            <td>Erweiterte Preisangaben</td>
            <td>-</td>
            <td>Durch aktivieren dieses Feldes, kannst du einem Produkt, mehrere Preise für verschiedene Shop-Konfigurationen oder Mitgliedergruppen zuweisen oder eine Preisstaffelung einrichten.</td>
        </tr>
        <tr>
            <td>Preisebenen anzeigen</td>
            <td>-</td>
            <td>Falls dieses Feld aktiviert ist, wird im Frontend der tiefste Preis der höchsten Ebene angezeigt. Hast du ein <docrobot_route name="product-management">Produkt</docrobot_route> mit folgender Preisstaffelung angelegt:
            <ul>
            <li>1 = 9.00</li>
            <li>3 = 8.00</li>
            <li>6 = 7.00</li>
            </ul>
            Sieht die Ausgabe im Frontend wie folgt aus:<br>
            Ab EUR 7.00</td>
        </tr>
    </tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/products/product-types/preise_verwalten.png
" alt="Anlegen einer Preisstaffelung beim Einpflegen eines neuen Produktes">

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
            <td>Auflistungs-Template</td>
            <td>iso_list_default</td>
            <td>Hier kannst du das Template für die <docrobot_route name="product-list">Produktliste</docrobot_route> auswählen.</td>
        </tr>
        <tr> 
            <td>Leser-Template</td>
            <td>iso_reader_default</td>
            <td>Hier kannst du das Template für den <docrobot_route name="product-reader">Produktleser</docrobot_route> auswählen.</td>
        </tr>
        <tr>
            <td>Galerie auflisten</td>
            <td>-</td>
            <td>Hier kannst du eine <docrobot_route name="galleries">Galerie</docrobot_route> für die Produktliste auswählen.</td>
        </tr>
        <tr>
            <td>Galerie für Detailseite</td>
            <td>-</td>
            <td>Hier kannst du eine <docrobot_route name="galleries">Galerie</docrobot_route> für den Produktleser auswählen.</td>
        </tr>
   </tbody>
</table>


## Produktattribute
 Mit dem Einstellen der Produktattribute wird bestimmt wie die Eingabemaske für diesen Produkttyp aussehen soll. Oft verwendete oder vom System benötigte Attribute sind schon vordefiniert. 

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
            <td>Die Bezeichnung in den eckigen Klammern rechts neben dem Attributnamen ist die Bezeichnung des dazugehörigen Datenbankfeldes.</td>
        </tr>
        <tr>
            <td>Gruppierung</td>
            <td>-</td>
            <td>In Contao können Gruppen von Formularfeldern definiert und aus- und eingeklappt werden. Isotope eCommerce bietet folgende Gruppen für Produkte an:
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
</ul></td>
        </tr>
        <tr>
            <td>Ausrichtung</td>
            <td>-</td>
            <td>Eine Übersicht der zur Verfügung stehenden Klassen erhältst du in der <docrobot_route name="product-types" path="#ausrichtung">Tabelle Ausrichtung</docrobot_route>.</td>
        </tr>
        <tr>
            <td>Verpflichtend</td>
            <td>-</td>
            <td>Hier kannst du das Feld zu einem Pflichtfeld machen.</td>
        </tr>
   </tbody>
</table>


### Ausrichtung

Das Contao-Backend verwendet ein 2-spaltiges Grid-System, um Formularfelder innerhalb ihrer Gruppen auszurichten.

<table id="ausrichtung">
	<thead>
		<tr>
			<th>tl_class</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>w50</td>
			<td>Setzt die Feldbreite auf 50% und floatet das Element (<code>float:left</code>).</td>
		</tr>
		<tr>
			<td>clr</td>
			<td>Hebt alle Floats auf (<code>clear:both</code>).</td>
		</tr>
		<tr>
			<td>wizard</td>
			<td>Verkürzt das Eingabefeld, damit genug Platz für den Wizard (z.B. Date Picker) ist.</td>
		</tr>
		<tr>
			<td>long</td>
			<td>Lässt das Eingabefeld zwei Spalten umspannen.</td>
		</tr>
		<tr>
			<td>m12</td>
			<td>Fügt dem Element einen oberen Abstand von 12 Pixeln hinzu (z.B. für einzelne Checkboxen).</td>
		</tr>
	</tbody>
</table>


## Variantenattribute

Mit Variante kann einem Produkt, zusätzlich Auswahlmöglichkeiten mitgegeben werden. z. B. Farben, Grössen etc.

<docrobot_image path="backend-configuration/store-configuration/products/product-types/varianten_backend.png" alt="Varianten im Backend">

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
            <td>Varianten aktivieren</td>
            <td>-</td>
            <td>Aktiviere Varianten für diesen Produkttyp.</td>
        </tr>
        <tr>
            <td>Name</td>
            <td>-</td>
            <td>Die Bezeichnung in den eckigen Klammern rechts neben dem Attributnamen ist die Bezeichnung des dazugehörigen Datenbankfeldes.</td>
        </tr>
        <tr>
            <td>Gruppierung</td>
            <td>-</td>
            <td>In Contao können Gruppen von Formularfeldern definiert und aus- und eingeklappt werden. Isotope eCommerce bietet folgende Gruppen für Produkte an:
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
</ul></td>
        </tr>
        <tr>
            <td>Ausrichtung</td>
            <td>-</td>
            <td>Eine Übersicht der zur Verfügung stehenden Klassen erhältst du in der <docrobot_route name="product-types" path="#ausrichtung">Tabelle Ausrichtung</docrobot_route>.</td>
        </tr>
        <tr>
            <td>Verpflichtend</td>
            <td>-</td>
            <td>Hier kannst du das Feld zu einem Pflichtfeld machen.</td>
        </tr>
        <tr>
            <td>Varianten eines Attributes immer anzeigen</td>
            <td>-</td>
            <td>Falls du Varianten eines Attributes (Select-Menü, Radio-Menü) auch anzeigen möchtest, wenn nur eine vorhanden ist, musst du dieses Feld aktivieren.</td>
        </tr>
   </tbody>
</table>


## Experten-Einstellungen

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
            <td>Vom Versand ausschliessen</td>
            <td>-</td>
            <td>Falls du ein Produkt vom Versand ausschliessen möchtest, musst du dieses Feld aktivieren (z. B. Download-Produkte)</td>
        </tr>
        <tr>
            <td>Downloads aktivieren</td>
            <td>-</td>
            <td>Handelt es sich beim Produkttyp um ein Produkt das Heruntergeladen werden soll, musst du dieses Feld aktivieren.</td>
        </tr>
   </tbody>
</table>