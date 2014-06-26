# Bestellungsdetails

Das Modul ` Bestellungsdetails` ist dafür zuständig, die Detailansicht einer Bestellung auszugeben. Es gibt zwei Hauptverwendungszwecke für dieses Modul:

* Einbindung auf der Seite nach dem Absenden der Bestellung (z.B. für eine Druckansicht oder einfach noch einmal als Zusammenfassung)
* Einbindung auf der Weiterleitungsseite für das Modul <docrobot_route name="order-history">Vergangene Bestellungen</docrobot_route>

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
			<td>Login erforderlich machen</td>
			<td>-</td>
			<td>Standardmässig generiert Isotope eCommerce eine eindeutige ID, mit der die Bestellung aufgerufen werden kann. Das ist deshalb notwendig, weil Gäste über kein Login verfügen und trotzdem auf ihre eigene Bestellung zugreifen können sollen. Wenn du diese Checkbox aktivierst, wird für Mitglieder-Bestellungen ein Login zwingend erforderlich gemacht (empfohlen). <docrobot_message type="info">Es erscheint fragwürdig, warum diese Option überhaupt optional aktivierbar und es nicht einfach das Standardverhalten von Isotope ist. Dem ist so, weil diese Option erst in der 2.1 eingeführt wurde und das Verhalten von Isotope im Vergleich zur 2.0 verändert hätte, wäre es standardmässig neu so. Aus diesem Grund muss sie manuell aktiviert werden.</docrobot_message></td>
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
			<td>Hier kannst du ein Produktsammlung-Template auswählen und so die Darstellung der Produkte in der Bestellung beliebig verändern.</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Diese Auswahl ermöglicht dir, die Reihenfolge in der die Produkte der Bestellung aufgelistet werden, zu bestimmen.</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder der Bestellung verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
	</tbody>
</table>