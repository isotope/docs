# Produktliste

Das Modul `Produktliste` ist für die Ausgabe von Produkten zuständig. Es bietet eine Vielzahl an Einstellungen welche nachfolgend beschrieben sind.

## Modul-Konfiguration

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
			<td>Gesamtzahl der Beiträge</td>
			<td>0</td>
			<td>Wenn du eine Zahl grösser als 0 eingibst, werden maximal diese Anzahl an Produkten aufgelistet. Das kann beispielsweise nützlich sein, um die neusten 4 Produkte auf der Startseite anzuzeigen.</td>
		</tr>
		<tr>
			<td>Elemente pro Seite</td>
			<td>0</td>
			<td>Änderst du hier nichts, werden alle gefundenen Produkte ohne Pagination auf der Seite ausgegeben. Ansonsten findet ein Seitenumbruch nach der eingegebenen Anzahl an Produkten statt.</td>
		</tr>
		<tr>
			<td>Kategorie-Anwendungsbereich</td>
			<td>-</td>
			<td>Jede einzelne Option ist im Contao-internen Helpwizard (<docrobot_image path="images/helpwizard.gif" alt="Helpwizard Icon">) beschrieben.</td>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.</td>
		</tr>
		<tr>
			<td>Filter-Module</td>
			<td>-</td>
			<td>Da du potenziell mehrere Filtermodule und Produktlisten auf einer Seite einsetzt, kannst du hier auswählen, auf welche Filtermodule die Produktliste reagieren soll.</td>
		</tr>
		<tr>
			<td>Filterung für neue Produkte</td>
			<td>Zeige alle Produkte</td>
			<td>Diese Einstellung bezieht sich auf die in der <docrobot_route name="configuration">Shop-Konfiguration</docrobot_route> optional zu konfigurierende Einstellung für neue Produkte. Solltest du dort z.B. 30 Tage eingestellt haben, kannst du hier "Zeige nur die neuen Produkte" auswählen. Tust du das, werden nur die Produkte aufgelistet, die innerhalb der letzten 30 Tage angelegt wurden. Die Option "Zeige alte Produkte" bezieht sich logischerweise auf das Gegenteil.</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierfeld</td>
			<td>-</td>
			<td>Hier kannst du einstellen, nach welchem Produktattribut beim ersten Seitenaufruf sortiert werden soll. Dein Shopbesucher kann durch das Filtermodul die Sortierung später selbstständig ändern.</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierrichtung</td>
			<td>Abwärts</td>
			<td>Falls du ein Sortierfeld ausgewählt hast, kannst du hier bestimmen, ob aufwärts oder abwärts danach sortiert werden soll.</td>
		</tr>
	</tbody>
</table>

<docrobot_message type="warning">Sortieren nach `Preis` ist ein äusserst aufwändiger Vorgang. Isotope eCommerce kennt die Möglichkeit, den Preis aufgrund von Regeln anzupassen und es ist deshalb nicht möglich, die Produkte bereits auf der Datenbank vorzufiltern. Insofern muss sich Isotope eCommerce in einem solchen Fall zuerst **alle** Produkte aus der Datenbank laden und sie anschliessend auf PHP-Ebene sortieren! Sie auch Kapitel <docrobot_route="performance">Performance</docrobot_route>.</docrobot_message>

## Weiterleitung

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
			<td>"In den Warenkorb"-Weiterleitungsseite hinzufügen</td>
			<td>-</td>
			<td>Falls in der Produktliste die Schaltfläche "In den Warenkorb" aktiviert ist und hier eine Seite ausgewählt wurde, wird der Besucher nach Klick auf die Schaltfläche zur entsprechenden Seite weitergeleitet.</td>
		</tr>
		<tr>
			<td>Zum ersten Produkt weiterleiten</td>
			<td>-</td>
			<td>Wenn diese Option aktiviert wurde, wird beim Aufruf der Seite automatisch das erste Produkt geladen. So ist es möglich, die Produktliste und den Produktleser auf der gleichen Seite zu platzieren und beim Seitenaufruf direkt das erste Produkt der Liste im Produktleser anzuzeigen.</td>
		</tr>
	</tbody>
</table>

## Referenzseite

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
			<td>Eine Referenzseite festlegen</td>
			<td>-</td>
			<td>Wenn du eine Referenzseite angibst, bezieht sich der "Kategorie-Anwendungsbereich" in der Modul-Konfiguration nicht auf die aktuelle Seite, sondern auf die ausgewählte Referenzseite. Ein Beispiel könnte eine Seite "Highlights" sein, zu der gewisse Produkte zugewiesen werden. Möchtest du diese jetzt auf der Startseite ausgeben, so wählst du bei "Kategorie-Anwendungsbereich" die "Aktive Kategorie" und wählst bei der Referenzseite die Seite "Highlights" aus.</td>
		</tr>
	</tbody>
</table>

## Template-Einstellungen

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
			<td>Produktlisten-Template</td>
			<td>iso_list_default</td>
			<td>Hier kannst du ein Listentemplate auswählen und so die Ansicht beliebig verändern. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder der Produktliste verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Spalten</td>
			<td>1</td>
			<td>Diese Option ermöglicht dir, die Generierung der CSS-Klassen anzupassen. Je nach Einstellung werden die Klassen `row_`, `col_` bzw. `odd` und `even` angepasst und ermöglichen dir individuelles Styling.</td>
		</tr>
		<tr>
			<td>Menge aktivieren</td>
			<td>-</td>
			<td>Standardmässig kann beim Hinzufügen zum Warenkorb keine Menge angegeben werden. Wird diese Option aktiviert, so kann der Besucher eine Anzahl angeben.</td>
		</tr>
		<tr>
			<td>Ausblenden bei Produktansicht</td>
			<td>-</td>
			<td>Diese Option blendet die Produktliste aus, wenn ein Produkt-Alias in der URL gefunden wurde.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
		<tr>
			<td>Leer-Nachricht angeben</td>
			<td>-</td>
			<td>Falls keine Produkte gefunden wurden (sei es, weil es gar keine gibt oder weil der Filter nicht zutrifft) so kann die Standard-Meldung hier bequem überschrieben werden.</td>
		</tr>
		<tr>
			<td>Definieren Sie eine Nachricht wenn kein Filter gesetzt ist</td>
			<td>-</td>
			<td>Wenn noch kein Filter gesetzt ist, kann hier standardmässig eine Nachricht eingegeben werden. Dies ermöglicht beim erstmaligen Laden der Seite nicht alle Produkte auf einmal auszugeben, sondern erst einmal die hier erfasste Nachricht anzuzeigen, bevor der Besucher dann einen Filter betätigt. Das kann insbesondere dann sinnvoll sein, wenn sehr viele Produkte einer Seite/Kategorie zugeordnet sind und die Anzeige aller Produkte ohne Filtereinschränkung nicht sinnvoll ist.</td>
		</tr>
		<tr>
			<td>Schaltflächen</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, welche Schaltflächen in der Liste angezeigt werden sollen. Möchtest du beispielsweise das Hinzufügen zum Warenkorb nur im Produktleser erlauben, so aktivierst du die Schaltfläche "In den Warenkorb" hier nicht. Ausserdem kannst du die Reihenfolge der Ausgabe der Schaltflächen bestimmen.</td>
		</tr>
	</tbody>
</table>
