# Zahlungsarten

Isotope eCommerce bietet dir eine Vielzahl an Zahlungsarten für die verschiedensten Anbieter.

## Zur Auswahl stehen:

1. <docrobot_route name="payment-method-cash">Bar</docrobot_route>
2. <docrobot_route name="payment-method-datatrans">Datatrans</docrobot_route>
3. <docrobot_route name="payment-method-epay">ePay</docrobot_route>
4. <docrobot_route name="payment-method-expercash">ExperCash</docrobot_route>
5. <docrobot_route name="payment-method-innopay">Innopay</docrobot_route>
6. <docrobot_route name="payment-method-payone">PayOne</docrobot_route>
7. <docrobot_route name="payment-method-paybyway">Paybyway</docrobot_route>
8. <docrobot_route name="payment-method-paypal">Paypal Standard Checkout</docrobot_route>
9. <docrobot_route name="payment-method-postfinance">PostFinance (Schweizer Post)</docrobot_route>
10. <docrobot_route name="payment-method-viveum">VIVEUM</docrobot_route>
11. <docrobot_route name="payment-method-saferpay">Saferpay</docrobot_route>
12. <docrobot_route name="payment-method-billpay">BillPay (mittels Saferpay)</docrobot_route>
13. <docrobot_route name="payment-method-sparkasse">Sparkasse</docrobot_route>
14. <docrobot_route name="payment-method-sofortueberweisung">sofortüberweisung.de</docrobot_route>
15. <docrobot_route name="payment-method-worldpay">WorldPay</docrobot_route>

<docrobot_message type="warning"><p>Beachte, dass jedes Zahlungsmodul selber dafür verantwortlich ist, wie die Bezahlung von statten geht und was anschliessend mit der Bestellung passiert. Es kann deshalb sein, dass obwohl ein Eingabefeld gleich benannt ist wie bei einer anderen Zahlungsart, das Verhalten nicht identisch ist. Deshalb ist es wichtig, dass die Dokumentation möglichst vollständig ist. Die Community ist somit auch auf deinen Beitrag angewiesen!</p></docrobot_message>

## Generelle Informationen für jede Zahlungsart

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


## Bestellhinweis

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
			<td>Hinweise</td>
			<td>-</td>
			<td>Hier kannst du der Zahlungsart eine Notiz hinzufügen. Die Hinweise können in den Benachrichtigungen mitgesendet werden, indem <code>##payment_note##</code> verwendet wird. Mehr über Simple Tokens findest du im <docrobot_route name="simple-tokens">entsprechenden Kapitel</docrobot_route>.</td>
		</tr>
	</tbody>
</table>

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
			<td>Status für neue Bestellungen</td>
			<td>-</td>
			<td>Im diesem Auswahlmenü kann der Status ausgewählt werden, welcher die Bestellung nach der Zahlung haben soll. Mehr zu den Bestellstatus findest du im <docrobot_route name="order-status">entsprechenden Kapitel</docrobot_route>.</td>
		</tr>
		<tr>
			<td>Anzahl-Berechnungsmodus</td>
			<td>-</td>
			<td>Diese Einstellung bezieht sich auf die nachfolgenden zwei Einstellungen "Minimale Anzahl" und "Maximale Anzahl" und regelt, ob die Werte für die Anzahl unterschiedlicher Produkte oder die gesamte Anzahl der Produkte im Warenkorb gelten sollen.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Minimale Anzahl</td>
			<td>0</td>
			<td>Hier kannst du eine minimale Anzahl für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von mindestens dieser Anzahl im Warenkorb hat.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Maximale Anzahl</td>
			<td>0</td>
			<td>Hier kannst du eine maximale Anzahl für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von maximal dieser Anzahl im Warenkorb hat.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Mindestbestellwert</td>
			<td>0.00</td>
			<td>Hier kannst du einen Mindestbestellwert für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von mindestens diesem Wert im Warenkorb hat.</td>
		</tr>
		<tr>
			<td>Höchstbestellwert</td>
			<td>0.00</td>
			<td>Hier kannst du einen Höchstbestellwert für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von maximal diesem Wert im Warenkorb hat.<docrobot_new_in_version version="2.3"><p>Dieses Feature ist neu in Isotope eCommerce 2.3</p></docrobot_new_in_version></td>
		</tr>
		<tr>
			<td>Aktive Länder</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Zahlungsart in der Zugänglichkeit für bestimmte Länder einschränken. Wenn du hier nichts auswählst, steht die Zahlungsart für alle Länder zur Verfügung.</td>
		</tr>
		<tr>
			<td>Versandarten</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Zahlungsart in der Zugänglichkeit für bestimmte Versandarten einschränken. Wenn du hier nichts auswählst, steht die Zahlungsart für alle Versandarten zur Verfügung. Du könntest somit z.B. die Bezahlmethode "Barzahlung bei Abholung" auf den Versandtyp "Abholung" einschränken.</td>
		</tr>
		<tr>
			<td>Produkttypen</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Zahlungsart in der Zugänglichkeit für bestimmte Produkttypen einschränken. Wenn du hier nichts auswählst, steht die Zahlungsart für alle Produkttypen zur Verfügung. Beispielsweise macht die Bezahlmethode "Barzahlung bei Abholung" für den Produkttyp "Online Downloads" wohl eher weniger Sinn.</td>
		</tr>
		<tr>
			<td>Shopkonfigurationen</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Zahlungsart in der Zugänglichkeit für bestimmte Shopkonfigurationen einschränken. Wenn du hier nichts auswählst, steht die Zahlungsart für alle Shopkonfigurationen zur Verfügung. Nützlich weil abhängig vom Zahlungsanbieter können möglicherweise nicht alle Währungen behandelt werden. <docrobot_new_in_version version="2.2"><p>Dieses Feature ist neu in Isotope eCommerce 2.2</p></docrobot_new_in_version></td>
		</tr>
	</tbody>
</table>

## Preis

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
			<td>Preis</td>
			<td>-</td>
			<td>Hier kannst du den Preis für diese Zahlungsart eingeben und so bspw. Kreditkartenkommissionen auf den Kunden umwälzen. Du kannst einen fixen Wert erfassen, sowie auch positive oder negative Prozentwerte, um vom Warenkorbwert abhängige Kosten darzustellen.</td>
		</tr>
		<tr>
			<td>Steuerklasse</td>
			<td>-</td>
			<td>Hier kannst du eine Steuerklasse auswählen, falls auf die Kosten der Zahlungsart Steuern erhoben werden sollen.</td>
		</tr>
	</tbody>
</table>

## Experten-Einstellungen

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
			<td>Nur für Gäste anzeigen</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, ob diese Zahlungsart nur für Gäste zur Verfügung stehen soll.</td>
		</tr>
		<tr>
			<td>Modul schützen</td>
			<td>-</td>
			<td>Im Gegensatz zu "Nur für Gäste anzeigen" kannst du hier die Zahlungsart für bestimmte Mitgliedergruppen einschränken.</td>
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
			<td>Aktiv</td>
			<td>-</td>
			<td>Hier kannst du die Zahlungsart aktivieren bzw. deaktivieren. 
<docrobot_message type="info"><p>Jede Zahlungsart kann aktiviert, sowie deaktiviert werden. Sie steht damit aber noch **nicht** automatisch im <docrobot_route name="checkout">Kassen-Modul</docrobot_route> zur Verfügung, sondern muss da zusätzlich aktiviert werden. Siehe auch entsprechendes Kapitel.</p></docrobot_message></td>
		</tr>
	</tbody>
</table>


