---
title: Einschränkender Filter
---

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

<docrobot_new_in_version version="2.3">
	<p>Neu lässt sich für jedes Attribut konfigurieren, ob eine Mehrfachauswahl des Feldes zu einer AND- oder OR-Suche führen soll.</p>
	<p>Es lässt sich nun konfigurieren, ob und wie eine Anzahl-Anzeige ausgegeben werden soll:</p>
	<ul>
		<li>"Show difference" zeigt die Differenz, wie viele Produkte zur Liste hinzukommen, wenn die Option angeklickt wird. Diese Anzeige macht primär bei einem OR-Filter Sinn, da ein AND-Filter zu einer negativen Anzahl führen würde.</li>
		<li>"Show total" zeigt an, wie viele Produkte nach Anklicken der Option in der Liste total erscheinen werden.</li>
		<li>"Do not show" entspricht dem bisherigen Verhalten und zeigt keine Anzahl an.</li>
</ul>
</docrobot_new_in_version>

![Die Einstellungen bei den Attributen](attribute-config.png)


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
			<td>Aktive Kategorie</td>
			<td>Jede einzelne Option ist im Contao-internen Helpwizard (![Helpwizard Icon">) beschrieben.<docrobot_new_in_version version="2.3](helpwizard.gif)<p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.{{< version "2.3" >}}</td>
		</tr>
		<tr>
			<td>Filterung für neue Produkte</td>
			<td>Zeige alle Produkte</td>
			<td>Wenn du die Möglichkeit in deinem Shop konfigurierst hast, Produkte als "neu" zu kennzeichnen, kannst du entweder nach alten, neuen oder nach allen Produkten filtern.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Zeige alle Produkte</li>
				<li>Zeige nur die neuen Produkte</li>
				<li>Zeige alte Produkte</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Filter-Konfiguration</td>
			<td>-</td>
			<td>Hier kannst du die Felder des Einschränkenden Filters konfigurieren.
				<table>
					<tbody>
						<tr>
							<td>Attribute</td>
							<td>-</td>
						</tr>
						<tr>
							<td>Abfrage-Typ</td>
							<td>"AND" oder "OR"</td>
						</tr>
						<tr>
							<td>Anzahl der Ergebnisse</td>
							<td>"Nicht anzeigen", "Zeige alle" oder "Unterschiede anzeigen"</td>
						</tr>
					</tbod>
				</table>
			</td>
		</tr>
		<tr>
			<td>Einzelne Auswahlen verstecken</td>
			<td>-</td>
			<td>Hier kannst du Felder für den Filter verstecken, wenn nur eine Auswahl vorhanden ist.</td>
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
			<td>Individuelles Template</td>
			<td>-</td>
			<td>Hier kannst du das Standard-Template überschreiben lassen.</td>
		</tr>
		<tr>
			<td>Navigationstemplate</td>
			<td>nav_default</td>
			<td>Hier kannst du ein Template für den Filter auswählen und die Ausgabe so verändern. Wie im Beispiel erklärt, generiert dieser Filter eine Navigation, weshalb hier alle Navigationstemplates zur Auswahl zur Verfügung stehen.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
		<tr>
			<td>Ausblenden bei Produktansicht</td>
			<td>-</td>
			<td>{{< version-tag "2.3" >}} Diese Option blendet den Produktfilter aus, wenn ein Produkt-Alias in der URL gefunden wurde.</td>
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
			<td>{{< version-tag "2.3" >}} Wenn du hier eine Seite auswählst, wird der Besucher beim Abschicken des Filters auf diese Seite weitergeleitet. {{% notice warning %}}<p>Da die Filtereinstellungen zwischengespeichert werden, ist die Platzierung des Filters unerheblich. Das ändert sich aber, sobald du Suchfelder aktivierst. Suchanfragen werden nicht zwischengespeichert und es ist deshalb notwendig, dass der Produktfilter <strong>vor der Produktliste auf der gleichen Seite</strong> eingebunden wird!</p>{{% /notice %}}</td>
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
			<td>Wenn du eine Referenzseite angibst, bezieht sich der "Kategorie-Anwendungsbereich" in der Modul-Konfiguration nicht auf die aktuelle Seite, sondern auf die ausgewählte Referenzseite. Ein Beispiel könnte eine Seite "Highlights" sein, zu der gewisse Produkte zugewiesen werden. Möchtest du diese jetzt auf der Startseite ausgeben, so wählst du bei "Kategorie-Anwendungsbereich" die "Aktive Kategorie" und wählst bei der Referenzseite die Seite "Highlights" aus.{{< version "2.3" >}}</td>
		</tr>
	</tbody>
</table>
