---
title: Vergangene Bestellungen
---

Das Modul `Vergangene Bestellungen` zeigt vergangene Bestellungen von Shop-Besuchern an.

{{% notice warning %}}Selbstverständlich funktioniert dieses Modul nur, wenn ein Mitglied eingeloggt ist, da nur einem eingeloggten Mitglied Bestellungen zugeordnet werden können.{{% /notice %}}

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
			<td>Konfigurationen</td>
			<td>-</td>
			<td>Da du beliebig viele Shop-Konfigurationen haben kannst und das Modul <code>Vergangene Bestellungen</code> sich nicht zwingend nur auf die gerade aktive Shop-Konfiguration beziehen muss (persönliche Bereiche sind ja meistens zentralisiert), kannst du hier die Shop-Konfigurationen anhaken, welche für die Suche der vergangenen Bestellungen berücksichtigt werden sollen.</td>
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
			<td>Weiterleitungsseite</td>
			<td>-</td>
			<td>Wähle hier die Seite aus, auf der sich das Modul <docrobot_route name="order-details">Bestellungsdetails</docrobot_route> befindet.</td>
		</tr>
		<tr>
			<td>Weiterleitungsseite für Warenkorb</td>
			<td>-</td>
			<td>Wähle hier die Seite aus, auf welche der Besucher weitergeleitet wird, wenn er den kompletten Warenkorb sehen möchte.</td>
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
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
	</tbody>
</table>
