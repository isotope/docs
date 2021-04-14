---
title: "Produkt-Filter"
description: "Die Frontend-Konfiguration - Module - Produkt-Filter"
aliases:
    - /de/frontend-konfiguration-module-Produkt-Filter/
weight: 130
---


Das Modul `Produktfilter` ist für die Ausgabe von Filtereinstellungen zuständig. Diese werden anschliessend auf die Module `Produktliste` angewendet, sofern sie dort aktiviert wurden (siehe <docrobot_route name="product-list">entsprechende Dokumentation</docrobot_route> für weitere Informationen).

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
			<td>Jede einzelne Option ist im Contao-internen Helpwizard (![Helpwizard Icon](helpwizard.gif)) beschrieben.</td>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.</td>
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
			<td>"Pro Seite"-Limit aktivieren</td>
			<td>-</td>
			<td>Wenn du diese Checkbox aktivierst, kannst du dem Besucher ein Dropdown mit "Pro Seite"-Optionen ausgeben. Er kann so selber bestimmen, wie viele Produkte er auf ein Mal sehen will.</td>
		</tr>
		<tr>
			<td>"Pro Seite"-Optionen</td>
			<td>8,12,32,64</td>
			<td>Hast du die Checkbox bei "Pro Seite"-Limit gesetzt, kannst du hier eine komma-separierte Liste von möglichen Optionen eingeben. Aus diesen wird dann ein Dropdown generiert.</td>
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
		<tr>
			<td>Aktivierte Suchfelder</td>
			<td>-</td>
			<td>Hier bestimmst du, nach welchen Produkt-Attributen der Besucher suchen kann. Es stehen nur diejenigen zur Verfügung, welche für im Frontend als durchsuchbar markiert wurden. Beschäftige dich dazu <docrobot_route name="attributes">mit dem Kapitel zu den Produkt-Attributen</docrobot_route>.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Artikelnummer</li>
				<li>Name</li>
				<li>Teaser</li>
				<li>Beschreibung</li>
			</ul></td>
		</tr>
		<tr>
		    <td>Exakte Übereinstimmung umleiten</td>
		    <td>-</td>
		    <td>
		        {{< version-tag "2.6" >}}
		        Der Kunde wird zu den Produktdetails weitergeleitet, wenn die Keyword-Suche in einem dieser Felder genau übereinstimmt (z. B. Suche nach Artikelnummer).
		     </td>
		</tr>
		<tr>
			<td>Suchfeld mit Autovervollständigung</td>
			<td>-</td>
			<td>Aktivierst du diese Funktion, wird das Suchfeld mit dem hier ausgewählten Produkt-Attribut autovervollständigt. Wählst du hier bspw. "Name" und hast zwei Produkte deren Produktenamen mit "Gitarre" beginnen so wird beim Tippen ins Suchfeld von "Git" eine Auswahl der beiden Produkte angezeigt. {{% notice warning %}}<p>Verwende diese Funktion mit Vorsicht. Autovervollständigung ist kein performanter Vorgang und du solltest sie deshalb <strong>niemals</strong> für Filter aktivieren, die eine grosse Anzahl von Produkten durchsuchen.</p>{{% /notice %}}
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Artikelnummer</li>
				<li>Name</li>
				<li>Teaser</li>
				<li>Beschreibung</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Aktivierte Sortierfelder</td>
			<td>-</td>
			<td>Hier bestimmst du, nach welchen Produkt-Attributen der Besucher sortieren kann. Es stehen nur diejenigen zur Verfügung, welche für die "Frontend-Sortierung" aktiviert wurden. Beschäftige dich dazu <docrobot_route name="attributes">mit dem Kapitel zu den Produkt-Attributen</docrobot_route>.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Hinzugefügt am</li>
				<li>Artikelnummer</li>
				<li>Name</li>
				<li>Preis</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierfeld</td>
			<td>-</td>
			<td>Diese Einstellung bestimmt, welches der aktivierten Sortierfelder beim ersten Laden des Produktfilters vorausgewählt sein soll. Sinnigerweise deckt sich das mit den Einstellungen der <docrobot_route name="product-list">Produkt-Liste</docrobot_route>. Da sich ein Produkt-Filter allerdings auf mehrere Produkt-Listen beziehen kann, musst du die korrekte Einstellung für dich treffen.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Hinzugefügt am</li>
				<li>Artikelnummer</li>
				<li>Name</li>
				<li>Preis</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Anfängliche Sortierrichtung</td>
			<td>Abwärts</td>
			<td>Diese Einstellung bestimmt die anfängliche Sortierrichtung für das gewählte "Anfängliche Sortierfeld".
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Abwärts</li>
				<li>Aufwärts</li>
			</ul>
			</td>
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
			<td>Filter-Template</td>
			<td>iso_filter_default</td>
			<td>Hier kannst du ein Template für den Filter auswählen und die Ausgabe so verändern.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
		<tr>
			<td>Ausblenden bei Produktansicht</td>
			<td>-</td>
			<td>Diese Option blendet den Produktfilter aus, wenn ein Produkt-Alias in der URL gefunden wurde.</td>
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
			<td>Wenn du hier eine Seite auswählst, wird der Besucher beim Abschicken des Filters auf diese Seite weitergeleitet. {{% notice warning %}}<p>Da die Filtereinstellungen zwischengespeichert werden, ist die Platzierung des Filters unerheblich. Das ändert sich aber, sobald du Suchfelder aktivierst. Suchanfragen werden nicht zwischengespeichert und es ist deshalb notwendig, dass der Produktfilter <strong>vor der Produktliste auf der gleichen Seite</strong> eingebunden wird!</p>{{% /notice %}}</td>
		</tr>
		<tr>
            <td>Link zur primären URL</td>
            <td>-</td>
            <td>
                {{< version-tag "2.6" >}}
                Verknüpfe die Produktdetails mit der primären URL (canonical) anstelle der aktuellen Kategorie.
            </td>
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
