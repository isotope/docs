---
menuTitle: "Sparkasse"
title: "Zahlungsart Sparkasse"
description: "Die Shop-Konfiguration - Bestellablauf - Zahlungsarten - Sparkasse."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-zahlungsarten-Sparkasse/
weight: 180    
---


{{% notice info %}}<p>Hier fehlt ein genereller Beschrieb.</p>{{% /notice %}}

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
			<td>Zahlungsart</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Transaktions-Typ</td>
			<td>Autorisieren und Einnehmen</td>
			<td>Hier kannst du den Transaktions-Typ bestimmen.<br><br>
				<ul>
				<li><strong>Autorisieren und Einnehmen</strong><br>
				Transaktionen von diesem Typ werden für die Authorisierung gesendet. Die Transaktion wird automatisch zur Begleichung geleitet wenn die Transaktion erfolgreich war.</li>
				<li><strong>Nur Autorisieren</strong><br>
				Transaktionen dieses Typs werden übertragen, wenn der Händler die Kreditkarte auf die Menge der verkauften Waren prüfen lassen möchte. Wenn der Händler nicht genügend Waren im Lager hat oder die Bestellungen vor der Warenlieferung prüfen möchte, wird dieser Transaktiontyps übertragen.</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>Verkäufer ID</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Passwort</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Referenz</td>
			<td>-</td>
			<td></td>
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
			<td>-</td>
		</tr>
		<tr>
			<td>Aktiviere das Logging</td>
			<td>-</td>
			<td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
		</tr>
	</tbody>
</table>
