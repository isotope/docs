# Kasse

Das Modul `Kasse` ist für den Bestellprozess zuständig. Viele Anwender fragen sich, warum gewisse Einstellungen im Kassen-Modul stattfinden und nicht generell vorgenommen werden. Ein oft gemachter Anfängerfehler beispielsweise sind eine fehlende Auswahl der Zahlungsarten oder Versandarten, da viele Anwender davon ausgehen, dass diese - sobald konfiguriert - im Kassen-Modul zur Verfügung stehen sollten.
Dass die Module hier noch einmal angewählt werden müssen, ermöglicht beispielsweise das Kassenmodul zwei Mal zu konfigurieren und auf derselben Seite einzubinden und unterschiedlichen Mitgliedergruppen (durch Einschränkung der Zugriffsrechte) das entsprechend korrekte Modul anzuzeigen.

## Modul-Konfiguration

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
			<td>Bestellvorgang-Art</td>
			<td>-</td>
			<td>Hier kannst du auswählen, ob für dieses Kassen-Modul nur Gastbestellung, nur Mitgliederbestellungen oder beides erlauben soll.</td>
		</tr>
		<tr>
			<td>Zahlungsarten</td>
			<td>-</td>
			<td>Hier kannst du auswählen, welche <docrobot_route name="payment-methods">Zahlungsarten</docrobot_route> in diesem Kassen-Modul zur Verfügung stehen sollen. Ausserdem kannst du sie hier sortieren.</td>
		</tr>
		<tr>
			<td>Versandarten</td>
			<td>-</td>
			<td>Hier kannst du auswählen, welche <docrobot_route name="shipping-methods">Versandarten</docrobot_route> in diesem Kassen-Modul zur Verfügung stehen sollen. Ausserdem kannst du sie hier sortieren.</td>
		</tr>
		<tr>
			<td>Benachrichtigung</td>
			<td>-</td>
			<td>Hier kannst du auswählen, welche <docrobot_route name="notifications_overview">Benachrichtigung</docrobot_route>  beim Absenden der Bestellung verschickt werden soll.</td>
		</tr>
	</tbody>
</table>

## Weiterleitung

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
			<td>Weiterleiten zur Bestätigungsseite</td>
			<td>-</td>
			<td>Hier kannst du eine Bestätigungsseite auswählen, zu welcher der Besucher weitergeleitet wird, wenn die Bestellung erfolgreich platziert wurde.</td>
		</tr>
		<tr>
			<td>Weiterleitungs-Seite für Warenkorb</td>
			<td>-</td>
			<td>Wenn du hier eine Seite auswählst, wird im Kassenmodul eine Schaltfläche ausgegeben, die den Besucher zum Warenkorb leitet.</td>
		</tr>
	</tbody>
</table>

## Template-Einstellungen

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
			<td>Produktsammlung-Template</td>
			<td>iso_collection_default</td>
			<td>Hier kannst du ein Produktsammlung-Template auswählen und so die Darstellung der Produkte im Kassen-Modul beliebig verändern.</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Diese Auswahl ermöglicht dir, die Reihenfolge in der die Produkte des Kassen-Moduls aufgelistet werden, zu bestimmen.</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder des Kassen-Moduls verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
	</tbody>
</table>

## Bestellbedingungsformular

Ein `Bestellbedingungsformular` ist ein per Formulargenerator von Contao erstelltes Formular, das du im Kassenmodul einbinden kannst. Es wird vor dem Absenden der Bestellung ausgegeben und kann beispielsweise aus einer Checkbox "Ich akzeptiere die AGB" bestehen.

<docrobot_message type="info">Übrigens: Alle Formularfelder sind auch als <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> verfügbar in der entsprechenden Benachrichtigung. Würdest du dein AGB-Feld bspw. `agb_checkbox` nennen, so wäre der Simple Token `form_agb_checkbox` verfügbar.</docrobot_message>

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
			<td>Bestellbedingungsformular</td>
			<td>-</td>
			<td>Hier kannst du das gewünschte Formular auswählen. Du musst es natürlich vorher via Formular-Generator anlegen. Logischerweise haben gewisse Einstellungen im Formular wie bspw. die Weiterleitung, keinen Einfluss auf dieses Formular. Es werden ausschliesslich die Formularfelder und ihre Einstellungen übernommen.</td>
		</tr>
		<tr>
			<td>Tabellenloses Layout</td>
			<td>-</td>
			<td>Bestimmt ob das Formular ohne HTML-Tabellen ausgegeben werden soll.</td>
		</tr>
		<tr>
			<td>Position des Formulars für die Bestellbedingungen</td>
			<td>nach der Produktliste</td>
			<td>Hier kannst du definieren, wo dieses Formular ausgegeben werden soll.</td>
		</tr>
	</tbody>
</table>
