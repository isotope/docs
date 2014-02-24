# Benachrichtigungen

<docrobot_incomplete>

<docrobot_image path="backend-configuration/store-configuration/general-settings/notifications/navigation.png" alt="Navigation des Benachrichtigungszentrums">

<docrobot_new_in_version version="2.0"><p>Die Isotope eCommerce-eigenen E-Mail-Benachrichtigungen wurden in das `Benachrichtigungszentrum` ausgelagert. Du wirst feststellen, dass du bei Klick auf `Benachrichtigungen` zum entsprechenden Menüpunkt weitergeleitet wirst. Dies wurde eingebaut, um den Einstieg für Isotope 1.4-Kenner zu erleichtern.</p></docrobot_new_in_version>

Stellst du dir das `Benachrichtigungszentrum` losgelöst von Isotope eCommerce vor, so sollte einiges von Beginn weg klarer erscheinen. Es wurde unabhängig entwickelt und hat sich zum Ziel gesetzt, als zentrale Komponente für beliebige andere Erweiterungen und deren Benachrichtigungen zu fungieren. Die Anforderungen für Benachrichtigungen lassen sich nämlich gemeinsam festhalten:

* Eine Benachrichtigung hat immer einen Auslöser und da bei diesem Auslöser potenziell mehrere verschiedene Nachrichten ausgelöst werden sollen, besteht eine Benachrichtigung aus einer oder mehr Nachrichten.

<docrobot_message type="warning">Merke dir die unterschiedliche Verwendung von `Benachrichtigung` und einer einzelnen `Nachricht`. Eine `Benachrichtigung` ist ein Gefäss von einer oder mehreren `Nachrichten`.</docrobot_message>

* Eine Nachricht muss potenziell in verschiedene Sprachen übersetzbar sein
* Eine Nachricht definiert sich nicht durch das Wort "E-Mail". Es ist folglich für eine Nachricht irrelevant wohin oder mit welchem Hilfsmittel (Gateway) sie verschickt wird.
* Eine Nachricht besteht nicht zwingend aus menschenlesbarem Text. Ein Austausch von Maschine zu Maschine kann ebenso als "Nachricht" bezeichnet werden.

## Gateways

Ein Gateway bezeichnet den Weg mit dem eine `Nachricht` seinen Empfänger erreicht.
Beispiele für Gateways:

* Email
* SMS
* Brieftaube
* File Transfer Protocol (FTP)

> Warum benötige ich das?

* SMS-Benachrichtigung einer bestimmten Abteilung?
* Abspeichern von Daten als CSV-Datei?
* E-Mail an Shop-Admin via anderen SMTP-Server als Bestellbestätigung an Besucher?

> Was mache ich jetzt?

Es ist davon auszugehen, dass dir das mitgelieferte Email-Gateway völlig ausreicht. Du legst dir also im Prinzip einfach nur folgende Konfiguration an und speicherst diese:

<docrobot_image path="backend-configuration/store-configuration/general-settings/notifications/email_gateway.png" alt="E-Mail Gateway">

## Benachrichtigungen

Eine `Benachrichtigung` ist eine Sammlung von einzelnen `Nachrichten`. Ausserdem sind sie immer von einem bestimmten Typ. In Isotope eCommerce existiert aktuell nur ein Benachrichtigungstyp der sich `Änderung Bestellstatus` nennt.

<docrobot_image path="backend-configuration/store-configuration/general-settings/notifications/notification.png" alt="Benachrichtigungsübersicht">

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
			<td>Jede Benachrichtigung ist von einem bestimmten Typ. Beliebige Extensions können beliebige Typen zur Verfügung stellen. Sie definieren ausserdem später, welche Simple Tokens verwendet werden können.</td>
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
			<td>Diese Einstellung bezieht sich auf ein <docrobot_route name="documents">Dokument</docrobot_route>, welches der Nachricht später per Simple Token angehängt werden kann.</td>
		</tr>
	</tbody>
</table>
