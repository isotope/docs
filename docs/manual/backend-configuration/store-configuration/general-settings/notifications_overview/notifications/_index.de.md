## Benachrichtigungen

Eine `Benachrichtigung` ist eine Sammlung von einzelnen <docrobot_route name="notifications_messages">Nachrichten</docrobot_route>. Ausserdem ist sie immer von einem bestimmten Typ. In Isotope eCommerce existiert aktuell nur ein Benachrichtigungstyp, der sich `Änderung Bestellstatus` nennt.

{{% notice info %}}Du fragst dich womöglich, warum es keinen Typ <code>Bestellbestätigung</code> gibt. Der Grund ist einfach: Es entspricht einer Statusänderung von <code>gar nichts</code> zu <code>neu</code> und ist somit auch nur eine <code>Änderung (des) Bestellstatus</code>.{{% /notice %}}

![Benachrichtigungsübersicht](notification.png)

### Titel & Typ

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
			<td>Titel</td>
			<td>-</td>
			<td>Hier kannst du einen Titel für deine Benachrichtigung eingeben. Er wird ausschliesslich für das Backend verwendet.</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>-</td>
			<td>Jede Benachrichtigung ist von einem bestimmten Typ. Beliebige Extensions können beliebige Typen zur Verfügung stellen. Sie definieren ausserdem später, welche <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> verwendet werden können.</td>
		</tr>
	</tbody>
</table>

### Konfiguration für den Typ "Änderung Bestellstatus"

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
			<td>Hier kannst du ein Produktsammlung-Template auswählen und so die Darstellung der Produkte in deine Nachrichten beliebig verändern.</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Diese Auswahl ermöglicht dir, die Reihenfolge in der die Produkte in der Nachricht aufgelistet werden, zu bestimmen.</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder in der Nachricht verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Dokument</td>
			<td>-</td>
			<td>Diese Einstellung bezieht sich auf ein <docrobot_route name="documents">Dokument</docrobot_route>, welches der Nachricht später per <docrobot_route name="simple-tokens">Simple Token</docrobot_route> angehängt werden kann.</td>
		</tr>
	</tbody>
</table>
