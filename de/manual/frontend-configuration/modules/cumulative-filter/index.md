# Einschränkender Filter

Der `einschränkende Filter` generiert aus den gewählten Filter-Attributen eine Navigation, mit der eine Produktliste eingeschränkt werden kann.

Nach dem Anlegen und Konfigurieren des Filters diesen im gewünschten Produktlisting-Modul aktivieren und als Inhaltselement auf der Produktlisting-Seite einfügen.

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

Der Besucher kann nun, durch Klick auf "akustisch", eine Liste von allen akustischen Gitarren anzeigen lassen. Klickt er dann auf "Cort", so schränkt sich das Resultat weiter ein (deshalb `einschränkender Filter`) und zeigt nun nur noch alle akustischen Gitarren von Cort an.

Zum Deaktivieren eines Filters bzw. Filterbestandteils, muss auf das aktivierte Item in der Navigationsliste gelickt werden. Soll in den beschriebenen Beispiel wieder die Gitarren aller Hersteller erscheinen, so muss erneut auf "Cort" geklickt werden.

Die aktiven Items erhalten eine zusätzliche CSS-Klasse "active" im li-Tag. Damit können die aktiven Filter-Items optisch hervorgehoben werden.


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
	</tbody>
</table>