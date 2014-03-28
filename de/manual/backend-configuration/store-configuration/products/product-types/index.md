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
            <td></td>
        </tr>
        <tr>
            <td>Preisebenen anzeigen</td>
            <td>-</td>
            <td></td>
        </tr>
    </tbody>
</table>


## Templates

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
            <td></td>
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
            <td></td>
        </tr>
        <tr>
            <td>Name</td>
            <td>-</td>
            <td></td>
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
            <td></td>
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
            <td></td>
        </tr>
        <tr>
            <td>Downloads aktivieren</td>
            <td>-</td>
            <td></td>
        </tr>
   </tbody>
</table>



Mindestens ein Produkttyp muss angelegt werden. Bei der Verwendung mehrerer Produkttypen muss ein Produkttyp als Standard deklariert werden. Dafür aktiviere einfach die Checkbox beim gewählten **Standard-Produkttyp**. Unter Beschreibung kann ein Hinweistext für den Produkt-Verwalter hinterlassen werden. **Wichtige Hinweise** können sein, für welche Produktkategorie der Produkttyp benutzt werden kann oder wie bestimmte Felder auszufüllen sind. Unter den Templates-Einstellungen kann dem Produkttyp ein **Produktlisten-Template** und ein **Produktleser-Template** aus den zwei Dropdownauswahlen zugeordnet werden. Diese werden vom System verwendet, wenn in den Produktlist- oder Produktleser-Modulen kein Template ausgewählt wird.

 Mit den Einstellen der Produktattribute wird bestimmt wie die Eingabemaske für diesen Produkttyp aussehen soll. Oft verwendete oder vom System **benötigte Attribute** sind schon vordefiniert. Aktiviere die Checkbox vor dem jeweiligen Attribut, damit dieses Attribut in der Produkt-Eingabemaske angezeigt wird. Die Bezeichnung in den eckigen Klammern rechts neben dem **Attributnamen** ist die  **Bezeichnung des dazugehörigen Datenbankfeldes**. In den Spalten rechts der Bezeichnung des Attributes können weitere Eigenschaften festgelegt werde. Fahre einfach über die blauen **Info-Kreise/Zeichen** um mehr über die Bedeutung zu erfahren.

 Die Option **"Varianten aktivieren"** sollte aktiviert werden wenn Produktvarianten generiert werden sollen. Das ist dann sinnvoll, wenn es Produkte gibt die sich bis auf wenige Eigenschaften gleichen. Zusätzliche Attribute wie Farben, Grössen oder Ähnliches können im Vorfeld angelegt werden um dann hier für eine Variantenaktivierung zur Verfügung zu stehen. Wenn sich durch die Abweichung dieser Eigenschaften später der Preis ändern soll, werden diese Attribute aktiviert. In der **Auswahl der Vaianten-Attribute** wird dann der Preis aktiviert. Ein Attribut sollte nur in einer der zwei Listen ausgewählt werden, entweder “Attribute” oder “Varianten-Attribute”.

 **"Always show variant attributes"** - Diese Checkbox bezieht sich auf die Frontend-Ausgabe des Varianten-Attributes, falls keine Auswahl besteht, obwohl es eine Checkbox oder ein Radiobutton ist.


Um Produkte als **Downloads** im Shop einrichten zu können musst das Feld "Downloads aktivieren" aktiviert werden. Damit es funktioniert ist wichtig das unter "Attribute", **"Versand-Einstellungen"** "Vom Versand ausschließen `[shipping_exempt]`" aktiviert ist. In der Produkt-Eingabemaske muss die Eigenschaft dann immer aktiviert sein. Beim Bestellprozess erscheint sonst die Versanddaten-Abfrage. Die Versanddaten werden beim Download nicht benötigt.