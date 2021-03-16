---
title: Zahlungsart "VIVEUM"
---

{{% notice info %}}<p>Hier fehlt ein genereller Beschrieb.</p>{{% /notice %}}

## Konfiguration des Zahlungsanbieters

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
			<td></td>
		</tr>
		<tr>
			<td>HTTP Methode</td>
			<td>POST</td>
			<td>VIVEUM unterstützt den Austausch der Daten sowohl über POST als auch über GET.</td>
		</tr>
		<tr>
			<td>Hash-Methode</td>
            <td>SHA-256</td>
            <td>Hash-Methode zur Verschlüsselung der ausgetauschten Daten. Zur Auswahl stehen:<br><br>
                <ul>
                    <li><strong>SHA-1</strong></li>
                    <li><strong>SHA-256</strong></li>
                    <li><strong>SHA-512</strong></li>
                </ul>
            </td>
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
			<td>Dynamische Template URL</td>
			<td>-</td>
			<td></td>
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
			<td>Testsystem verwenden</td>
			<td>-</td>
			<td></td>
		</tr>
		<tr>
			<td>Aktiviere das Logging</td>
			<td>-</td>
			<td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
		</tr>
	</tbody>
</table>
