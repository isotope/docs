---
title: "Adressbuch"
description: "Die Frontend-Konfiguration - Module - Adressbuch"
aliases:
    - /de/frontend-konfiguration-module-Adressbuch/
weight: 180
---


Das Modul `Adressbuch` dient zur Verwaltung der Adressen von Mitgliedern. Damit ermöglichst du deinen wiederkehrenden Besuchern einen einfacheren Bestellprozess, da sie jeweils eine Liefer- bzw. Rechnungadresse von ihrem Adressbuch auswählen können.

Wenn du möchtest, dass bei jeder Bestellung eines Mitglieds die angegebenen Adressen im Adressbuch abgelegt werden, 
so muss das im [Kassenmodul](/de/frontend-konfiguration-module-Kasse/) eingestellt werden.

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
			<td>Benachrichtigung</td>
			<td>-</td>
			<td>Hier kannst du auswählen, welche <docrobot_route name="notifications_overview">Benachrichtigung</docrobot_route>  beim Absenden der Bestellung verschickt werden soll.</td>
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
			<td>Formular-Template</td>
			<td>member_default</td>
			<td>Hier kannst du ein Formular-Template auswählen. Beachte: Diese Einstellung bezieht sich einzig und alleine auf den Bearbeiten-Modus.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>member_default</li>
				<li>member_grouped</li
			</ul>
			</td>
		</tr>
		<tr>
			<td>Tabellenloses Layout</td>
			<td>-</td>
			<td>Bestimmt ob das Formular im Bearbeiten-Modus ohne HTML-Tabellen ausgegeben werden soll.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
	</tbody>
</table>
