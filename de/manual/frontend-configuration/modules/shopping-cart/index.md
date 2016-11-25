# Warenkorb

Das Modul `Warenkorb` ist für die Ausgabe des aktuellen Warenkorbs für den Besucher zuständig.

<docrobot_message type="info"><p>Wenn sich deine Besucher einloggen müssen, kann Isotope eine Zuordnung des Warenkorbs zum Besucher vornehmen. Deshalb kann ein Warenkorb der nie in eine Bestellung umgewandelt wurde jeweils beim nächsten Besuch wieder geladen werden. Für Gäste kann dieses Verhalten logischerweise nicht identisch erfolgen. Isotope setzt dann beim Besuch ein [HTTP-Cookie][1] und versucht so den Warenkorb beim nächsten Besuch wieder zu erkennen. Wie lange ein solcher Gast-Warenkorb gespeichert werden soll, kannst du in den Systemeinstellungen unter `Zeitlimit für Gäste-Warenkorb` festlegen. Isotope räumt automatisch in regelmässigen Abständen deine Datenbank auf und löscht alte Einträge.</p></docrobot_message>

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
			<td>Weiterleitungs-Seite für Warenkorb</td>
			<td>-</td>
			<td>Diese Einstellung gibt an, zu welcher Seite der Nutzer weitergeleitet wird, wenn er den kompletten Warenkorb sehen möchte. Das kann dann nützlich sein, wenn man mehrere Warenkörbe auf einer Seite platziert und z.B. einen "Mini-Warenkorb" hat, dem man eine "klicke hier für die Gesamtansicht"-Schaltfläche hinzufügen will.</td>
		</tr>
		<tr>
			<td>Weiterleitungs-Seite für Bestellvorgang</td>
			<td>-</td>
			<td>Wählst du hier eine Seite aus, so erscheint die Schaltfläche "weiter zur Kasse" und leitet den Benutzer dann auch da hin.</td>
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
			<td>Individuelles Template</td>
			<td>-</td>
			<td>Hier kannst du das Standard-Template überschreiben lassen.</td>
		</tr>
		<tr>
			<td>Produktsammlung-Template</td>
			<td>iso_collection_default</td>
			<td>Hier kannst du ein Produktsammlung-Template auswählen und so die Darstellung der Produkte im Warenkorb beliebig verändern.
			<br>Auswahl Möglichkeiten:
			<ul>
				<li>iso_collection_default</li>
				<li>iso_collection_favorites</li>
				<li>iso_collection_invoice</li>
				<li>iso_collection_mini</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Hier kannst du definieren, in welcher Reihenfolge die Einträge einer Sammlung aufgelistet werden sollen.
			Auswahl Möglichkeiten:
			<br><ul>
				<li>nach Datum hinzugefügt (aufsteigend)</li>
				<li>nach Datum hinzugefügt (absteigend)</li>
				<li>nach Datum aktualisiert (aufsteigend)</li>
				<li>nach Datum aktualisiert (absteigend)</li>
				<li>nach Produktnamen (aufsteigend)</li>
				<li>nach Produktnamen (absteigend)</li>
				<li>nach Preis (aufsteigend)</li>
				<li>nach Preis (absteigend)</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder des Warenkorbs verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>"Einkauf fortsetzen"-Schaltfläche aktivieren</td>
			<td>-</td>
			<td>Fügt eine Schaltfläche hinzu, welche den Benutzer zur zuvor besuchten Seite zurückleitet. Diese Schaltfläche wird <strong>ausschliesslich</strong> beim ersten Aufruf nach Klick auf "zum Warenkorb hinzufügen" angezeigt.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
		<tr>
			<td>Leer-Nachricht angeben</td>
			<td>-</td>
			<td>Falls dem Warenkorb noch keine Produkte hinzugefügt wurden, so kann die Standard-Meldung hier bequem überschrieben werden.</td>
		</tr>
			</tbody>
</table>


[1]: http://de.wikipedia.org/wiki/HTTP-Cookie
