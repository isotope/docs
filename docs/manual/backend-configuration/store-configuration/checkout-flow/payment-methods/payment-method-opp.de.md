---
title: Zahlungsart "Open Payment Platform"
---

{{% notice info %}}<p>Hier fehlt ein genereller Beschrieb.</p>{{% /notice %}}

## Allgemeine Einstellungen

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
			<td>Hier kannst du den Transaktions-Typ bestimmen.<br><br>
				<ul>
				<li><strong>Autorisieren und Einnehmen</strong><br>
				Transaktionen von diesem Typ werden für die Authorisierung gesendet. Die Transaktion wird automatisch zur Begleichung geleitet wenn die Transaktion erfolgreich war.</li>
				<li><strong>Nur Autorisieren</strong><br>
				Transaktionen dieses Typs werden übertragen, wenn der Händler die Kreditkarte auf die Menge der verkauften Waren prüfen lassen möchte. Wenn der Händler nicht genügend Waren im Lager hat oder die Bestellungen vor der Warenlieferung prüfen möchte, wird dieser Transaktiontyps übertragen.</li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>

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
			<td>Benutzer-ID</td>
			<td>-</td>
			<td>Die Benutzer-ID.</td>
		</tr>
		<tr>
			<td>Passwort</td>
			<td>-</td>
			<td>Das Benutzer-Passwort.</td>
		</tr>
		<tr>
			<td>Entity/Channel ID</td>
			<td>-</td>
			<td>Die Entity oder Channel ID.</td>
		</tr>
		<tr>
			<td>Zahlungsmarken</td>
			<td>-</td>
			<td>Unterstützten Zahlungsmarken auswählen:<br><br>
			    <ul>
			        <li>American Express</li>
			        <li>Diners Club</li>
			        <li>SEPA Direct Debit</li>
			        <li>giropay</li>
			        <li>JCB</li>
			        <li>Klarna Ratenkauf</li>
			        <li>Klarna Rechnung</li>
			        <li>MasterCard</li>
			        <li>paydirect</li>
			        <li>PayPal</li>
			        <li>Ratenkauf by easyCredit</li>
			        <li>SOFORTüberweisung</li>
			        <li>VISA</li>
			    </ul>
			</td>
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
			<td>Definiert ob sämtliche Transaktionen über das Datatrans Testsystem abgewickelt werden sollen.</td>
		</tr>
		<tr>
			<td>Aktiviere das Logging</td>
			<td>-</td>
			<td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
		</tr>
	</tbody>
</table>
