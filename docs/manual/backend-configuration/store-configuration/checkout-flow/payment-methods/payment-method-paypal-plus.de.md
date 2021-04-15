---
menuTitle: "PayPal PLUS"
title: "Zahlungsart PayPal PLUS"
description: "Die Shop-Konfiguration - Bestellablauf - Zahlungsarten - PayPal PLUS."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-zahlungsarten-PayPalPLUS/
weight: 107    
---


{{% notice info %}}<p>Hier fehlt ein genereller Beschrieb.</p>{{% /notice %}}

{{< version "2.5" >}}

## Konfiguration des Zahlungsanbieters

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
			<td>Client ID</td>
			<td>-</td>
			<td>Dies sind live API Zugangsdaten von Ihrem PayPal PLUS Account. Sie können diese in Ihrem PayPal Developer Account finden: Dashboard > My Apps & Credentials. <a href="https://www.paypalobjects.com/webstatic/de_DE/downloads/Dokumentation_REST_API_Zugangsdaten.pdf" target="_blank">Wie erstelle ich die Client ID und Secret?</a></td>
		</tr>
		<tr>
			<td>Secret</td>
			<td>-</td>
			<td>Dies sind live API Zugangsdaten von Ihrem PayPal PLUS Account. Sie können diese in Ihrem PayPal Developer Account finden: Dashboard > My Apps & Credentials. <a href="https://www.paypalobjects.com/webstatic/de_DE/downloads/Dokumentation_REST_API_Zugangsdaten.pdf" target="_blank">Wie erstelle ich die Client ID und Secret?</a></td>
		</tr>
	</tbody>
</table>

## Freigabe

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
			<td>Testsystem verwenden</td>
			<td>-</td>
			<td>Aktiviere diese Checkbox, wenn du im Testmodus arbeiten möchtest. Die Anfragen gehen dann automatisch an das Testsystem und nicht das Produktivsystem.</td>
		</tr>
		<tr>
			<td>Aktiviere das Logging</td>
			<td>-</td>
			<td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
		</tr>
	</tbody>
</table>
