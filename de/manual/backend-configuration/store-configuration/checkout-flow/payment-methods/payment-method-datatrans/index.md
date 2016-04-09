# Zahlungsart "Datatrans"

Datatrans ist ein Schweizer Payment Service Provider. Das Modul implementiert die Zahlungsschnittstelle zur Abwicklung von Transaktionen über eine Vielzahl von Zahlungsmittel wie z.B. VISA, Mastercard, Postfinance und AMEX.

## Allgemeine Einstellungen

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
			<td>Transaktions-Typ</td>
			<td>Autorisieren und Einnehmen</td>
			<td>Hier kannst du den Transaktions-Typ bestimmen.<br><br>
				<ul>
				<li><strong>Autorisieren und Einnehmen</strong><br>
				Transaktionen von diesem Typ werden für die Authorisierung gesendet. Die Transaktion wird automatisch zur Begleichung geleitet wenn die Transaktion erfolgreich war.</li>
				<li><strong>Nur Autorisieren</strong><br>
				Transaktionen dieses Typs werden übertragen, wenn der Händler die Kreditkarte auf die Menge der verkauften Waren prüfen lassen möchte. Wenn der Händler nicht genügend Waren im Lager hat oder die Bestellungen vor der Warenlieferung prüfen möchte, wird dieser Transaktiontyps übertragen.</li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>

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
			<td>Händler-ID</td>
			<td>-</td>
			<td>Die Händler-ID (Merchant ID)</td>
		</tr>
		<tr>
			<td>HMAC Schlüssel</td>
			<td>-</td>
			<td>Schlüssel zur Verschlüsselung von ausgetauschten Daten</td>
		</tr>
		<tr>
			<td>Hash-Methode</td>
			<td>md5</td>
			<td>Hash-Methode zur Verschlüsselung der ausgetauschten Daten. Zur Auswahl stehen:<br><br>
				<ul>
					<li><strong>md5</strong><br>Unsichere und daher nicht empfohlene Einstellung</li>
					<li><strong>sha256</strong><br>Empfohlene Einstellung</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>HMAC Schlüssel konvertieren</td>
			<td>-</td>
			<td>Definiert ob der eingegebene HMAC Schlüssel vor Verschlüsselung der ausgetauschten Daten zu Bytes konvertiert werden soll. Dies ist notwendig wenn Du den HMAC Schlüssel 1:1 aus den Datatrans Sicherheitseinstellungen kopierst.</td>
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
			<td>Definiert ob sämtliche Transaktionen über das Datatrans Testsystem abgewickelt werden sollen.</td>
		</tr>
	</tbody>
</table>
