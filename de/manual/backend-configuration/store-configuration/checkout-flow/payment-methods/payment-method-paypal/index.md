# Zahlungsart "PayPal"

<docrobot_message type="info">Hier fehlt ein genereller Beschrieb.</docrobot_message>

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
			<td>PayPal-Konto</td>
			<td>-</td>
			<td>Deine mit deinem PayPal-Konto verknüpfte E-Mail-Adresse. Auf dieses PayPal-Konto wird der Betrag gutgeschrieben.</td>
		</tr>
	</tbody>
</table>

<docrobot_message type="warning">Die Zahlungsmethode PayPal muss auch noch im Modul "Kasse" aktiviert werden, was oft vergessen wird.</docrobot_message>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-paypal/kassenmodul.png" alt="Aktivierung im Modul Kasse">

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
			<td>Falls aktiviert, wird die Bezahlung nur in einer Testumgebung (Sandbox) emuliert aber tatsächlich nicht ausgeführt. Man kann sich bei Paypal hierzu auch einen <a href="https://developer.paypal.com/docs/classic/lifecycle/sb_create-accounts">Test-Account erstellen</a>. <br>Falls man in Firefox statt der Paypal Sandbox-Seite eine Sicherheitswarnung bekommt (SSL_ERROR_NO_CYPHER_OVERLAP) muss man in about:config die Einstellung security.tls.version.max zurück setzen.</td>
		</tr>
	</tbody>
</table>
