---
title: "Favoriten"
description: "Die Frontend-Konfiguration - Module - Favoriten"
aliases:
    - /de/frontend-konfiguration-module-Favoriten/
weight: 115
---


{{% notice info %}}
Dieses Feature ist neu in Isotope eCommerce 2.4. Stell dir vor, dein Kunde möchte einige Produkte aus deinem umfangreichen Sortiment vorauswählen und sie danach bequem aus einer Liste bestellen. Diese neue Funktion richtest du wie folgt ein: In den Modulen 
[Produktliste](/de/frontend-konfiguration-module-produktliste/) und [Produktleser](/de/frontend-konfiguration-module-Produktleser/) kannst du neu neben "Aktualisierung", "In den Warenkorb" auch noch ein Button «Zu Favoriten hinzufügen» aktivieren.
{{% /notice %}}

{{% notice warning %}}
Funktioniert nur wenn der Kunde im Frontend angemeldet ist.
{{% /notice %}}

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
			<td>Produktsammlung-Template</td>
			<td>iso_collection_default</td>
			<td>Hier kannst du ein Sammlung-Template auswählen und so die Ansicht beliebig verändern.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>iso_collection_default</li>
				<li>iso_collection_favorites</li>
				<li>iso_collection_invoice</li>
				<li>iso_collection_mini</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Hier kannst du definieren, in welcher Reihenfolge die Einträge einer Sammlung aufgelistet werden sollen.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>nach Datum hinzugefügt (aufsteigend)</li>
				<li>nach Datum hinzugefügt (absteigend)</li>
				<li>nach Datum aktualisiert (aufsteigend)</li>
				<li>nach Datum aktualisiert (absteigend)</li>
				<li>nach Produktnamen (aufsteigend)</li>
				<li>nach Produktnamen (absteigend)</li>
				<li>nach Preis (aufsteigend)</li>
				<li>nach Preis (absteigend)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder der Favoritenliste verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
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
	</tbody>
</table>
