# Zahlungsarten

Isotope eCommerce bietet dir eine Vielzahl an Zahlungsarten für die verschiedensten Anbieter.

## Zur Auswahl stehen:

1. Cash
2. Datatrans
3. ExperCash
4. PayOne
5. Paypal Standard Checkout
6. PostFinance (Schweizer Post)
7. VIVEUM
8. Saferpay
9. Sparkasse
10. sofortüberweisung.de
11. WorldPay

<docrobot_message type="warning"><p>Beachte, dass jedes Zahlungsmodul selber dafür verantwortlich ist, wie die Bezahlung von statten geht und was anschliessend mit der Bestellung passiert. Es kann deshalb sein, dass obwohl ein Eingabefeld gleich benannt ist wie bei einer anderen Zahlungsart, das Verhalten nicht identisch ist. Deshalb ist es wichtig, dass die Dokumentation möglichst vollständig ist. Die Community ist somit auch auf deinen Beitrag angewiesen!</p></docrobot_message>

## Generelle Informationen für jede Zahlungsart

<docrobot_message type="info"><p>Jede Zahlungsart kann aktiviert, sowie deaktiviert werden. Sie steht damit aber noch **nicht** automatisch im <docrobot_route name="checkout">Kassen-Modul</docrobot_route> zur Verfügung, sondern muss da zusätzlich aktiviert werden. Siehe auch entsprechendes Kapitel.</p></docrobot_message>

## Name & Typ

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
			<td>Name</td>
			<td>-</td>
			<td>Hier kannst du der Zahlungsart einen internen Namen vergeben. Er wird im Frontend nicht angezeigt.</td>
		</tr>
		<tr>
			<td>Bezeichnung</td>
			<td>-</td>
			<td>Hier kannst du der Zahlungsart einen externen Namen vergeben. Er wird dem Besucher im Frontend angezeigt und kann via <docrobot_route name="translations">Übersetzungen</docrobot_route> übersetzt werden.</td>
		</tr>

		<tr>
			<td>Zahlungsmodul</td>
			<td>-</td>
			<td>Hier wählst du deine gewünschte Zahlungsart aus.</td>
		</tr>
	</tbody>
</table>