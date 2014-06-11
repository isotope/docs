# Zahlungsart „Sofortüberweisung“

Bei Sofortüberweisungen autorisiert der Kunde die SOFORT AG, mittels einer vom Kunden bereitgestellten Onlinebanking-TAN eine Überweisung vom Konto des Kunden an den Händler vorzunehmen. Weitere Informationen bietet [die Firmenwebsite][1].

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
			<td>Kunden ID</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Projekt ID</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Projekt-Passwort</td>
			<td>-</td>
			<td></td>
		</tr>
	</tbody>
</table>

Eine vollständige Backend-Konfiguration sollte in etwa so aussehen:

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-sofortueberweisung/backend-maske.png" alt="SOFORT im Backend">

[1]: https://www.sofort.com/ger-DE/verkaeufer/su/e-payment-sofort-ueberweisung/
