# Einschränkender Filter

Der `einschränkende Filter` generiert aus den gewählten Filter-Attributen eine Navigation, mit der eine Produktliste eingeschränkt werden kann.

## Beispiel

Als Beispiel dient uns ein Musikgeschäft, das online Gitarren verkauft.
Die Gitarren unterscheiden sich in diesem Falle durch folgende Attribute mit den jeweiligen Optionen:

* Typ
	* akustisch
	* elektronisch
* Hersteller
	* Alhambra
	* Cort
	* Fender
	* Gibson
	* Taylor

Mit dem `einschränkenden Filter` lässt sich nun ein Navigationsmenü mit der eben abgebildeten Baumstruktur generieren.
Hierbei werden alle Optionen (also Level 2) klickbar.

<docrobot_new_in_version version="2.3"><p>Ab Isotope eCommerce 2.3 werden nur noch die Optionen ausgegeben, welche auch ein Produkt zugewiesen haben. Ausserdem werden auch die Anzahl der Treffer in Klammer ausgegeben. Beispiel: "Taylor (42)"</p></docrobot_new_in_version>

Der Besucher kann nun, durch Klick auf "akustisch", eine Liste von allen akustischen Gitarren anzeigen lassen. Klickt er dann auf "Cort", so schränkt sich das Resultat weiter ein (deshalb `einschränkender Filter`) und zeigt nun nur noch alle akustischen Gitarren von Cort an.

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
			<td>Kategorie-Anwendungsbereich</td>
			<td>-</td>
			<td>Jede einzelne Option ist im Contao-internen Helpwizard (<docrobot_image path="images/helpwizard.gif" alt="Helpwizard Icon">) beschrieben.</td><docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Aktivierte Filter</td>
			<td>-</td>
			<td>Hier bestimmst du, nach welchen Produkt-Attributen der Besucher filtern kann. Es stehen nur diejenigen zur Verfügung, welche für die "Frontend-Filterung" aktiviert wurden. Beschäftige dich dazu <docrobot_route name="attributes">mit dem Kapitel zu den Produkt-Attributen</docrobot_route>.</td>
		</tr>
		<tr>
			<td>Einzelne Auswahlen verstecken</td>
			<td>-</td>
			<td>Wenn du diese Checkbox aktivierst, werden Filter ausgeblendet, wenn es nur eine mögliche Option gibt.</td>
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
			<td>Wenn du eine Referenzseite angibst, bezieht sich der "Kategorie-Anwendungsbereich" in der Modul-Konfiguration nicht auf die aktuelle Seite, sondern auf die ausgewählte Referenzseite. Ein Beispiel könnte eine Seite "Highlights" sein, zu der gewisse Produkte zugewiesen werden. Möchtest du diese jetzt auf der Startseite ausgeben, so wählst du bei "Kategorie-Anwendungsbereich" die "Aktive Kategorie" und wählst bei der Referenzseite die Seite "Highlights" aus.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
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
			<td>Navigationstemplate</td>
			<td>nav_default</td>
			<td>Hier kannst du ein Template für den Filter auswählen und die Ausgabe so verändern. Wie im Beispiel erklärt, generiert dieser Filter eine Navigation, weshalb hier alle Navigationstemplates zur Auswahl zur Verfügung stehen.</td>
		</tr>
		<tr>
			<td>Ausblenden bei Produktansicht</td>
			<td>-</td>
			<td>Diese Option blendet den Produktfilter aus, wenn ein Produkt-Alias in der URL gefunden wurde.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
	</tbody>
</table>

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
			<td>Weiterleitungs-Seite</td>
			<td>-</td>
			<td>Wenn du hier eine Seite auswählst, wird der Besucher beim Abschicken des Filters auf diese Seite weitergeleitet. <docrobot_message type="warning"><p>Da die Filtereinstellungen zwischengespeichert werden, ist die Platzierung des Filters unerheblich. Das ändert sich aber, sobald du Suchfelder aktivierst. Suchanfragen werden nicht zwischengespeichert und es ist deshalb notwendig, dass der Produktfilter <strong>vor der Produktliste auf der gleichen Seite</strong> eingebunden wird!</p></docrobot_message><docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version>
</td>
		</tr>
	</tbody>
</table>