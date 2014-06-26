# Adressbuch

Das Modul `Adressbuch` dient zur Verwaltung der Adressen von Mitgliedern. Damit ermöglichst du deinen wiederkehrenden Besuchern einen einfacheren Bestellprozess, da sie jeweils eine Liefer- bzw. Rechnungadresse von ihrem Adressbuch auswählen können.

Wenn du möchtest, dass bei jeder Bestellung eines Mitglieds die angegebenen Adressen im Adressbuch abgelegt werden, so muss das im <docrobot_route name="checkout">Kassenmodul</docrobot_route> eingestellt werden.

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
			<td>Formular-Template</td>
			<td>member_default</td>
			<td>Hier kannst du ein Formular-Template auswählen. Beachte: Diese Einstellung bezieht sich einzig und alleine auf den Bearbeiten-Modus.</td>
		</tr>
		<tr>
			<td>Tabellenloses Layout</td>
			<td>-</td>
			<td>Bestimmt ob das Formular im Bearbeiten-Modus ohne HTML-Tabellen ausgegeben werden soll.</td>
		</tr>
		<tr>
			<td>Nachrichten einbinden</td>
			<td>-</td>
			<td>Wird diese Option aktiviert, so werden die Fehler und Hinweise direkt im Modul und nicht als JavaScript-Overlay ausgegeben.</td>
		</tr>
	</tbody>
</table>