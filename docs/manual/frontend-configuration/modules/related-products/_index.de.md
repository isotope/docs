---
title: "Ähnliche Produkte"
description: "Die Frontend-Konfiguration - Module - Ähnliche Produkte"
aliases:
    - /de/frontend-konfiguration-module-Ähnliche-Produkte/
weight: 185
---


Das Modul `Ähnliche Produkte` gibt die ähnlichen Produkte des aktuell angezeigten Produkts aus.
Als Basis für dieses Modul werden die [verknüpften Kategorien](/de/backend-konfiguration-shop-Verknüpfte-Kategorien/) verwendet.

Nehmen wir an, du hast eine `verknüpfte Kategorie` namens `Zubehör` definiert.
In den Produkteinstellungen hast du für dein Produkt `Gitarre` für die `verknüpfte Kategorie` `Zubehör` die Produkte `Kapodaster` sowie `Stimmgabel` ausgewählt, so kann dieses Modul die beiden Produkte `Kapodaster` sowie `Stimmgabel` ausgeben, sofern du bei der Modul-Konfiguration die Kategorie `Zubehör` ausgewählt hast.

{{% notice info %}}<p>Da das Modul <code>Ähnliche Produkte</code> im Endeffekt auch nur eine <docrobot_route name="product-list">Produktliste</docrobot_route> darstellt, wird darauf verzichtet, hier noch einmal alle identischen Einstellungen zu dokumentieren.{{% /notice %}}

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
			<td>Verknüpfte Kategorien</td>
			<td>-</td>
			<td>Wähle Kategorien aus, aus denen Produkte angezeigt werden sollen.</td>
		</tr>
		<tr>
			<td>Gesamtzahl der Beiträge</td>
			<td>3</td>
			<td>Wenn du eine Zahl grösser als 0 eingibst, werden maximal diese Anzahl an Produkten aufgelistet. Das kann beispielsweise nützlich sein, um die neusten 4 Produkte auf der Startseite anzuzeigen.</td>
		</tr>
		<tr>
			<td>Elemente pro Seite</td>
			<td>0</td>
			<td>Änderst du hier nichts, werden alle gefundenen Produkte ohne Pagination auf der Seite ausgegeben. Ansonsten findet ein Seitenumbruch nach der eingegebenen Anzahl an Produkten statt.</td>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.</td>
		</tr>
		<tr>
			<td>Filterung für neue Produkte</td>
			<td>Zeige alle Produkte</td>
			<td>Diese Einstellung bezieht sich auf die in der <docrobot_route name="configuration">Shop-Konfiguration</docrobot_route> optional zu konfigurierende Einstellung für neue Produkte. Solltest du dort z.B. 30 Tage eingestellt haben, kannst du hier "Zeige nur die neuen Produkte" auswählen. Tust du das, werden nur die Produkte aufgelistet, die innerhalb der letzten 30 Tage angelegt wurden. Die Option "Zeige alte Produkte" bezieht sich logischerweise auf das Gegenteil.</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierfeld</td>
			<td>-</td>
			<td>Hier kannst du einstellen, nach welchem Produktattribut beim ersten Seitenaufruf sortiert werden soll. Dein Shopbesucher kann durch das Filtermodul die Sortierung später selbstständig ändern. {{% notice warning %}}Wenn du die Produkte für eine Seite (Kategorie) manuell sortiert hast, darfst du hier <strong>keine</strong> Auswahl treffen!{{% /notice %}}
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
			<td>Anfängliches Sortierrichtung</td>
			<td>Abwärts</td>
			<td>Falls du ein Sortierfeld ausgewählt hast, kannst du hier bestimmen, ob aufwärts oder abwärts danach sortiert werden soll.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>Abwärts</li>
				<li>Aufwärts</li>
			</ul>
			</td>
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
			<td>"In den Warenkorb"-Weiterleitungsseite hinzufügen</td>
			<td>-</td>
			<td>Diese Einstellung gibt an, zu welcher Seite - ausser der gerade aktiven - der Besucher weitergeleitet wird, wenn er ein Produkt in den Warenkorb legt.</td>
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
			<td>Produktlisten-Template</td>
			<td>-</td>
			<td>Hier kannst du ein Listen-Template auswählen und so die Ansicht beliebig verändern. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>iso_list_default</li>
				<li>iso_list_variants</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder der Produktliste verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Spalten</td>
			<td>1</td>
			<td>Diese Option ermöglicht dir, die Generierung der CSS-Klassen anzupassen. Je nach Einstellung werden die Klassen <code>row_</code>, <code>col_</code> bzw. <code>odd</code> und <code>even</code> angepasst und ermöglichen dir individuelles Styling.</td>
		</tr>
		<tr>
			<td>Menge aktivieren</td>
			<td>-</td>
			<td>Standardmässig kann beim Hinzufügen zum Warenkorb keine Menge angegeben werden. Wird diese Option aktiviert, so kann der Besucher eine Anzahl angeben.</td>
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
			<td>Schaltflächen</td>
			<td>In den Warenkorb</td>
			<td>Hier kannst du bestimmen, welche Schaltflächen in der Liste angezeigt werden sollen. Möchtest du beispielsweise das Hinzufügen zum Warenkorb nur im Produktleser erlauben, so aktivierst du die Schaltfläche "In den Warenkorb" hier nicht. Ausserdem kannst du die Reihenfolge der Ausgabe der Schaltflächen bestimmen.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>In den Warenkorb</li>
				<li>Aktualisieren</li>
				<li>Zu Favoriten hinzufügen</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>
