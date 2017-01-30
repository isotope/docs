# Zahlungsart "QuickPay"

QuickPay ist ein dänischer Zahlungsanbieter, der seit 2004 seine Leistungen anbietet. Weitere Informationen bietet [die Firmenwebsite][1].

Der Prozess erfordert ein QuickPay Konto, dass dir die Informationen liefert, um ein entsprechendes Zahlungsfenster deinen Kunden zur Verfügung zu stellen.

<docrobot_message type="warning"><p>Du brauchst auch noch ein Konto mit einem Zahlungsunternehmen, dass dir den eigentlichen Geldverkehr (tatsächliche Kontobelastung / -gutschrift) erledigt. Im Falle von QuickPay kannst du das Zahlungsunternehmen innerhalb deines QuickPay Kontos auswählen und entsprechend benutzen. Selbstverständlich brauchst du auch ein gesonderten Vertrag mit dem Zahlungsunternehmen.</p></docrobot_message>

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
		<td>Händler-ID</td>
		<td>-</td>
		<td>Entspricht im QuickPay der Merchant-ID</td>
	</tr>
	<tr>
		<td>Einverständnis-ID</td>
		<td>-</td>
		<td>Entspricht im QuickPay der Payment Window - Agreement ID.</td>
	</tr>
	<tr>
		<td>API-Schlüssel</td>
		<td>-</td>
		<td>Entspricht im QuickPay dem Payment Window - API KEY Schlüssel</td>
	</tr>
	<tr>
		<td>Privater Schlüssel</td>
		<td>-</td>
		<td>Entspricht im QuickPay der Merchant information - Private Key.</td>
	</tr>
	<tr>
		<td>Zahlungsarten</td>
		<td>creditcard</td>
		<td>Hier kannst du die mit dem Zahlungsunternehmen vereinbarten Zahlungsarten hinterlegen. [Weitere Informationen...][2]</td>
	</tr>
		</tr>
	</tbody>
</table>

Hier eine bildliche Hilfe des Feldmappings:

QuickPay:

<docrobot_image path="QuickPayIntegration.png" alt="Konfigurationsparameter in der QuickPay Settings / Integration">

und das entsprechende Mapping in Isotope:

<docrobot_image path="isotopeKonfiguration.png" alt="Konfigurationsparameter in Isotope">


[1]: https://www.quickpay.net/
[2]: https://learn.quickpay.net/tech-talk/appendixes/payment-methods/
