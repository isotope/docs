---
menuTitle: "ePay"
title: "Zahlungsart ePay"
description: "Die Shop-Konfiguration - Bestellablauf - Zahlungsarten - ePay."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-zahlungsarten-epay/
weight: 145    
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
			<td>Transaktions-Typ</td>
			<td>Autorisieren und Einnehmen</td>
			<td>
			    <ul>
			       <li><strong>Autorisieren und Einnehmen</strong><br>Transaktionen von diesem Typ werden für die Autorisierung gesendet. Die Transaktion wird automatisch zur Begleichung geleitet wenn die Transaktion erfolgreich war.</li>
			       <li><strong>Nur Autorisieren</strong><br>Transaktionen dieses Typs werden übertragen, wenn der Händler die Kreditkarte auf die Menge der verkauften Waren prüfen lassen möchte. Wenn der Händler nicht genügend Waren im Lager hat oder die Bestellungen vor der Warenlieferung prüfen möchte, wird dieser Transaktiontyps übertragen.</li>
			    </ul>
			</td>
		</tr>
		<tr>
			<td>Integrationstyp</td>
			<td>Vollbild</td>
			<td>
			    Integrations-Optionen:<br><br>
			    <ul>
			        <li><strong>Vollbild</strong></li>
			        <li><strong>Integriertes Zahlungsformular</strong></li>
			    </ul>
			</td>
		</tr>
		<tr>
			<td>Händler-Nummer</td>
			<td>-</td>
			<td>Die Händler-Nummer.</td>
		</tr>
		<tr>
			<td>Sicherheitsschlüssel</td>
			<td>-</td>
			<td>Der geheime Schlüssel in Ihrer ePay-Konfiguration.</td>
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
			<td>Aktiviere das Logging</td>
			<td>-</td>
			<td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
		</tr>
	</tbody>
</table>
