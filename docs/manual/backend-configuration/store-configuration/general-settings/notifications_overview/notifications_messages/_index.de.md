---
title: "Nachrichten"
description: "Die Shop-Konfiguration - Allgemeine Einstellungen - Benachrichtigszentrum - Nachrichten."
aliases:
    - /de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-nachrichten/
weight: 30    
---


Eine `Nachricht` bestimmt einen gewissen Inhalt, der über ein bestimmtes [Gateway](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-gateways/) verschickt wird.

`Nachrichten` können, müssen aber nicht zwingend mehrsprachig sein. Machen wir wieder den Fehler und denken bei einer Nachricht nur an eine E-Mail, so scheint dies immer gewollt zu sein. Berücksichtigen wir allerdings eine Nachricht von Maschine zu Maschine, so wird diese kaum in mehreren Sprachen verfasst.

So legst du eine Nachricht an den Bestellenden an:

![Detail einer Nachricht an den Bestellenden](message.png)

### Titel & Gateway

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
			<td>Titel</td>
			<td>-</td>
			<td>Hier kannst du einen Titel für deine Nachricht eingeben. Er wird ausschliesslich für das Backend verwendet.</td>
		</tr>
		<tr>
			<td>Gateway</td>
			<td>-</td>
			<td>Jede Nachricht wird über ein bestimmtes <docrobot_route name="notifications_gateways">Gateway</docrobot_route> versendet, welches du hier auswählen kannst.</td>
		</tr>
	</tbody>
</table>

### Konfiguration für das Gateway "E-Mail"

{{% notice info %}}Die [Sprachen](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-sprachen/) werden im entsprechenden Kapitel behandelt{{% /notice %}}

### Experteneinstellungen

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
			<td>Priorität</td>
			<td>normal</td>
			<td>Hier kannst du die Priorität, mit der die E-Mail verschickt wird, festlegen.</td>
		</tr>
		<tr>
			<td>Template-Datei</td>
			<td>mail_default</td>
			<td>Hier kannst du das Template auswählen, mit welchem die E-Mail generiert wird.</td>
		</tr>
	</tbody>
</table>

### Einstellungen veröffentlichen

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
			<td>Nachricht veröffentlichen</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, ob diese Nachricht beim Versenden einer Benachrichtigung berücksichtigt werden soll oder nicht.</td>
		</tr>
	</tbody>
</table>
