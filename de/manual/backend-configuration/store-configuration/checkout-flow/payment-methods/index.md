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
			<td>Hier kannst du der Zahlungsart eine Notiz hinzufügen. Die Hinweise können in den Benachrichtigungen mitgesendet werden, indem <code>##payment_note##</code> oder <code>##payment_note_text##</code> verwwendet werden. Mehr über Simple Tokens findest du im <docrobot_route name="simple-tokens">entsprechenden Kapitel</docrobot_route>.</td>
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
			<td>Mindestbestellwert</td>
			<td>0.00</td>
			<td>Hier kannst du einen Mindestbestellwert für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von mindestens diesem Wert im Warenkorb hat.</td>
		</tr>
		<tr>
			<td>Höchstbestellwert</td>
			<td>0.00</td>
			<td>Hier kannst du einen Höchstbestellwert für diese Zahlungsart festlegen. Angewendet bedeutet das, der potenzielle Käufer diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von maximal diesem Wert im Warenkorb hat.</td>
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


