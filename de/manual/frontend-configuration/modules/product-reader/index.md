# Produktleser


Das Modul `Produktleser` ist für die Ausgabe eines einzelnen Produkts zuständig. Es wird im Normalfall zusammen mit der <docrobot_route name="product-list">Produktliste</docrobot_route> auf der selben Seite platziert.

Optional kann das Modul `Produktleser` auch auf eine separate Seite z.B. Produktdetails gesetzt werden. Dafür muss die Umleitung in den Seiteneigenschaften auf die Detailseite eingestellt werden - siehe "<docrobot_route name="setting-site-structure">Anlegen der Seitenstruktur</docrobot_route>".

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
			<td>Menge aktivieren</td>
			<td>-</td>
			<td>Standardmässig kann beim Hinzufügen zum Warenkorb keine Menge angegeben werden. Wird diese Option aktiviert, so kann der Besucher eine Anzahl angeben.</td>
		</tr>
		<tr>
			<td>Eine 404 Fehlerseite anzeigen</td>
			<td>-</td>
			<td>Wenn diese Option aktiviert ist, wird die 404 (Seite nicht gefunden)-Seite angezeigt, wenn kein Produktalias in der URL gefunden wurde. Selbstverständlich muss diese Seite im Seitenbaum auch angelegt werden. Verwende diese Einstellung falls der Produktleser auf einer separaten Seite verwendet wird, die nicht ohne Produktalias aufgerufen werden darf bzw. so keinen Sinn ergibt.</td>
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
			<td>"In den Warenkorb"-Weiterleitungsseite hinzufügen</td>
			<td>-</td>
			<td>Falls die Schaltfläche "In den Warenkorb" aktiviert ist und hier eine Seite ausgewählt wurde, wird der Besucher nach Klick auf die Schaltfläche zur entsprechenden Seite weitergeleitet.</td>
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
			<td>Produktleser-Template</td>
			<td>iso_reader_default</td>
			<td>Hier kannst du ein Lesertemplate auswählen und so die Ansicht beliebig verändern. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder des angezeigten Produkts verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
		<tr>
			<td>Schaltflächen</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, welche Schaltflächen im Produktleser angezeigt werden sollen. Ausserdem kannst du die Reihenfolge der Ausgabe der Schaltflächen bestimmen.</td>
		</tr>
	</tbody>
</table>
