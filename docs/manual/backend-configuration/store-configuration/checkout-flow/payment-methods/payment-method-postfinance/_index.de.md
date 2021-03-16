---
title: Zahlungsart "PostFinance"
---

Dieses Dokument beschreibt die Integration der Zahlungsart "PostFinance".
Weitere Informationen können auf [der entsprechenden Webseite][1] gefunden werden.


## Konfiguration des Zahlungsanbieters

Hier werden die Grunddaten zur Verknüpfung des e-Payment-Systems von PostFinance erfasst.

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
			<td>PSPID</td>
			<td>-</td>
			<td>Hier musst du deine PSPID erfassen. Die PSPID erhältst du von der PostFinance. Solltest du dich im Testmodus befinden, stelle bitte sicher, dass die PSPID auf "DEMO" endet.</td>
		</tr>
		<tr>
			<td>HTTP Methode</td>
			<td>-</td>
			<td>PostFinance unterstützt den Austausch der Daten sowohl über POST als auch über GET. Du kannst wählen was du möchtest, solange sowohl in Isotope eCommerce als auch im PSP Interface die selbe Methode ausgewählt ist. Generell ist POST die bessere Wahl.</td>
		</tr>
		<tr>
			<td>Hash-Methode</td>
			<td>-</td>
			<td>PostFinance unterstützt den verschiedene Hashing-Methoden. Du kannst wählen was du möchtest, solange sowohl in Isotope eCommerce als auch im PSP Interface die selbe Methode ausgewählt ist. Generell reicht SHA-1 aus.</td>
		</tr>
		<tr>
			<td>SHA-IN Signatur</td>
			<td>-</td>
			<td>Hier musst du einen beliebigen Hash eintragen, welcher zur Signatur der ausgetauschten Daten verwendet wird. Stelle sicher, dass du denselben Algorithmus verwendest, wie du bei "Hash-Methode" ausgewählt hast. Es gibt <a href="http://hash.online-convert.com">viele Hash-Generatoren</a>, welche dir einen Hash aus einem beliebigen Sicherheitsschlüssel generieren können. Stelle zudem sicher, dass du den Hash als kleingeschriebene, hexadezimale Zeichenkette eingibst. Den Hash den die hier erfasst, musst du dann ebenfalls im PSP Interface bei "SHA-IN Signatur" erfassen. So können sowohl das PSP als auch Isotope eCommerce die Richtigkeit der Daten verifizieren.</td>
		</tr>
		<tr>
			<td>SHA-OUT Signatur</td>
			<td>-</td>
			<td>Hier musst du einen beliebigen Hash eintragen, welcher zur Signatur der ausgetauschten Daten verwendet wird. Stelle sicher, dass du denselben Algorithmus verwendest, wie du bei "Hash-Methode" ausgewählt hast. Es gibt <a href="http://hash.online-convert.com">viele Hash-Generatoren</a>, welche dir einen Hash aus einem beliebigen Sicherheitsschlüssel generieren können. Stelle zudem sicher, dass du den Hash als kleingeschriebene, hexadezimale Zeichenkette eingibst. Den Hash den die hier erfasst, musst du dann ebenfalls im PSP Interface bei "SHA-OUT Signatur" erfassen. So können sowohl das PSP als auch Isotope eCommerce die Richtigkeit der Daten verifizieren.</td>
		</tr>

		<tr>
			<td>Vordefinierte Zahlungsmethode</td>
			<td>-</td>
			<td>{{< version-tag "2.3" >}} Standardmässig wählt der Kunde die gewünschte Zahlungsmethode (VISA, MasterCard etc.) auf der Seite von PostFinance. Du kannst aber die Auswahl auch bereits auf deiner Seite treffen und hier auswählen, zu welcher er automatisch weitergeleitet werden soll. Indem du mehrere Zahlungsmethoden vom Typ PostFinance definierst und in diesem Feld andere Zahlungsmethoden auswählst, kannst du deinen Kunden somit die gewünschte Zahlungsmethode bereits auf Seiten von deinem Shop wählen lassen.</td>
		</tr>
	</tbody>
</table>

Schlussendlich sollte es in etwa so aussehen:

![PostFinance im Backend](overview.png)

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
			<td>Testsystem verwenden</td>
			<td>-</td>
			<td>Aktiviere diese Checkbox, wenn du im Testmodus arbeiten möchtest. Die Anfragen gehen dann automatisch an das Testsystem und nicht das Produktivsystem.</td>
		</tr>
        <tr>
            <td>Aktiviere das Logging</td>
            <td>-</td>
            <td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
        </tr>
	</tbody>
</table>

## Konfiguration des PSP Interfaces

Als nächster Schritt wird das PSP Interface konfiguriert.
Alle nachfolgenden Konfigurationen werden in "Configuration > Technical information" vorgenommen.

### Tab "Global security parameters"

![PSP Tab Security](tab_security.png)

Stelle sicher, dass die Einstellungen mit dem oberen Bild übereinstimmen. Du musst den "Hash algorithm" entsprechend deiner Konfiguration in Isotope eCommerce anpassen.

### Tab "Data and origin verification"

![PSP Tab Data and Origin](tab_data_n_origin.png)

Stelle sicher, dass du die korrekte URL/Domain zu deinem Webshop hier eingibst. Das PostFinance PSP System validiert alle eingehenden Anfragen und prüft, ob die Herkunft einer validen URL entspricht. Wenn du hier eine falsche Seite erfasst, bekommst du einen Fehler "unknown order/1/r" (siehe Error-Logs im Postfinance Backend).

Danach erfasse die genau gleiche SHA-IN Signatur wie du sie vorher in Isotope eCommerce angegeben hast.

{{% notice warning %}}<p>Bitte beachte den Unterschied zwischen SHA-IN und SHA-OUT!</p>{{% /notice %}}

### Tab "Transaction feedback"

![Server zu Server Request](tab_transaction_n_feedback_1.png)

Scroll runter zu "Direct HTTP server-to-server request" und setze "Timing of the request" gemäss dem Bild oben.
Die URL's sind für beide identisch und sind wie folgt aufzubauen:

>	«Die URL zu deinem Webshop»/system/modules/isotope/postsale.php

{{% notice info %}}<p>Stelle sicher, dass diese URL über das Internet erreichbar ist. Das heisst, du musst sicherstellen, dass du die Seite nicht bspw. mit einem `.htaccess`-Schutz versehen hast. Andernfalls wird das Zahlungs-Feedback fehlschlagen und Isotope eCommerce ist nicht fähig, die Bestellung abzuschliessen.</p>{{% /notice %}}

Zum Schluss, setze die "Request method" gemäss derjenigen, die du in Isotope eCommerce während des Setups der Zahlungsart ausgewählt hast.

![SHA-OUT Signatur](tab_transaction_n_feedback_2.png)

Vergiss nicht, die SHA-OUT Signatur zu ergänzen. Auch hier muss sie mit der Konfiguration in Isotope eCommerce übereinstimmen.

{{% notice warning %}}<p>Bitte beachte den Unterschied zwischen SHA-IN und SHA-OUT!</p>{{% /notice %}}

Das wär's! Du kannst jetzt Isotope eCommerce zusammen mit Zahlungen via PostFinance e-Payment geniessen.

## PostFinance mit FIS Integration

{{% notice warning %}}<p>Diese Funktion ist aktuell noch deaktiviert und wird im Moment in Zusammenarbeit mit der PostFinance getestet. Sobald die entsprechenden Funktionen im Isotope eCommerce Core gelandet sind, wird die Dokumentation an dieser Stelle ergänzt</p>{{% /notice %}}

[1]: https://www.postfinance.ch/de/biz/prod/eserv/epay.html
