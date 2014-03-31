# Versandarten

Isotope eCommerce bietet dir im Core zwei Versandarten, mit denen du in Kombination viele Anwendungsfälle abdecken kannst.

## Zur Auswahl stehen:

1. <docrobot_route name="shipping-method-flat">Pauschalversand</docrobot_route>
2. <docrobot_route name="shipping-method-group">Versandgruppierung</docrobot_route>

## Generelle Informationen für jede Versandart

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
			<td>Versandart-Name</td>
			<td>-</td>
			<td>Hier kannst du der Versandart einen internen Namen vergeben. Er wird im Frontend nicht angezeigt.</td>
		</tr>
		<tr>
			<td>Bezeichnung</td>
			<td>-</td>
			<td>Hier kannst du der Versandart einen externen Namen vergeben. Er wird dem Besucher im Frontend angezeigt und kann via <docrobot_route name="translations">Übersetzungen</docrobot_route> übersetzt werden.</td>
		</tr>

		<tr>
			<td>Versandart-Typ</td>
			<td>-</td>
			<td>Hier wählst du deine gewünschte Versandart aus.</td>
		</tr>
	</tbody>
</table>


## Versandhinweis

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
			<td>Versandart-Hinweise</td>
			<td>-</td>
			<td>Hier kannst du der Versandart eine Notiz hinzufügen. Die Hinweise können in den Benachrichtigungen mitgesendet werden, indem <code>##shipping_note##</code> verwendet wird. Mehr über Simple Tokens findest du im <docrobot_route name="simple-tokens">entsprechenden Kapitel</docrobot_route>.</td>
		</tr>
	</tbody>
</table>

## Preis-Grenzwert und Steuerklassen-Anwendbarkeit

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
			<td>Hier kannst du den Preis für diese Versandart eingeben und so bspw. Versandkosten auf den Kunden umwälzen. Du kannst einen fixen Wert erfassen, sowie auch positive oder negative Prozentwerte, um vom Warenkorbwert abhängige Kosten darzustellen.</td>
		</tr>
		<tr>
			<td>Steuerklasse</td>
			<td>-</td>
			<td>Hier kannst du eine Steuerklasse auswählen, falls auf die Kosten der Versandart Steuern erhoben werden sollen.</td>
		</tr>
		<tr>
			<td>Pauschalpreis-Berechnung</td>
			<td>Pauschal</td>
			<td>Im diesem Auswahlmenü kannst du bestimmen, ob der erfasste Preis ein Pauschalpreis darstellt oder pro Produkt bzw. pro Stück erhoben werden soll.</td>
		</tr>
	</tbody>
</table>

## Konfiguration

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
			<td>Länder</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Versandart in der Zugänglichkeit für bestimmte Länder einschränken. Wenn du hier nichts auswählst, steht die Versandart für alle Länder zur Verfügung.</td>
		</tr>
		<tr>
			<td>Staat/Regionen</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Versandart in der Zugänglichkeit für bestimmte Staaten/Regionen einschränken. Wenn du hier nichts auswählst, steht die Versandart für alle Staaten/Regionen zur Verfügung.</td>
		</tr>
		<tr>
			<td>Postleitzahlen</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Versandart in der Zugänglichkeit für bestimmte Postleitzahlen einschränken. Wenn du hier keine komma-separierte Liste eingibst, steht die Versandart für alle Postleitzahlen zur Verfügung.</td>
		</tr>
		<tr>
			<td>Mindestbetrag Zwischensumme</td>
			<td>0.00</td>
			<td>Hier kannst du einen Mindestbetrag der Zwischensumme für diese Versandart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Versandart erst dann nutzen, wenn er Produkte von mindestens diesem Wert im Warenkorb hat.</td>
		</tr>
		<tr>
			<td>Höchstbetrag Zwischensumme</td>
			<td>0.00</td>
			<td>Hier kannst du einen Höchstbetrag der Zwischensumme für diese Versandart festlegen. Angewendet bedeutet das, der potenzielle Käufer kann diese Versandart erst dann nutzen, wenn er Produkte von maximal diesem Wert im Warenkorb hat.</td>
		</tr>

		<tr>
			<td>Versandarten</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Zahlungsart in der Zugänglichkeit für bestimmte Versandarten einschränken. Wenn du hier nichts auswählst, steht die Zahlungsart für alle Versandarten zur Verfügung. Du könntest somit z.B. die Bezahlmethode "Barzahlung bei Abholung" auf den Versandtyp "Abholung" einschränken.</td>
		</tr>
		<tr>
			<td>Mindestgewicht</td>
			<td>-</td>
			<td>Diese Einstellung kommt dann zum Tragen, wenn der <docrobot_route name="product-types">Produkttyp</docrobot_route> das Attribut für die Gewichtseingabe erlaubt. Sobald Isotope weiss, wie schwer ein Produkt ist, kann die Versandart auf das Gewicht eingeschränkt werden.</td>
		</tr>
		<tr>
			<td>Höchstgewicht</td>
			<td>-</td>
			<td>Diese Einstellung kommt dann zum Tragen, wenn der <docrobot_route name="product-types">Produkttyp</docrobot_route> das Attribut für die Gewichtseingabe erlaubt. Sobald Isotope weiss, wie schwer ein Produkt ist, kann die Versandart auf das Gewicht eingeschränkt werden.</td>
		</tr>
		<tr>
			<td>Produkttypen</td>
			<td>-</td>
			<td>Hier kannst du die jeweilige Versandart in der Zugänglichkeit für bestimmte Produkttypen einschränken. Wenn du hier nichts auswählst, steht die Versandart für alle Produkttypen zur Verfügung.</td>
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
			<td>Hier kannst du bestimmen, ob diese Versandart nur für Gäste zur Verfügung stehen soll.</td>
		</tr>
		<tr>
			<td>Modul schützen</td>
			<td>-</td>
			<td>Im Gegensatz zu "Nur für Gäste anzeigen" kannst du hier die Versandart für bestimmte Mitgliedergruppen einschränken.</td>
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
			<td>Hier kannst du die Versandart aktivieren bzw. deaktivieren. 
<docrobot_message type="info"><p>Jede Versandart kann aktiviert, sowie deaktiviert werden. Sie steht damit aber noch **nicht** automatisch im <docrobot_route name="checkout">Kassen-Modul</docrobot_route> zur Verfügung, sondern muss da zusätzlich aktiviert werden. Siehe auch entsprechendes Kapitel.</p></docrobot_message></td>
		</tr>
	</tbody>
</table>


