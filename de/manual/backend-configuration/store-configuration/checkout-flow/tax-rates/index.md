# Steuersätze

Für eine Shop-Konfiguration muss mindestens ein Steuersatz vorhanden sein.

  Klicke auf "Neuer Steuersatz" und fülle einfach die Pflichtfelder **Steuersatz-Name**, "Steuersatz" und "Adressbasis für die Berechnung" aus. **Adressbasis für die Berechnung** klingt erstmal seltsam. Steuersätze können von Land zu Land oder Staat zu Staat unterschiedlich sein. Daher wird hier ausgewählt ob die Rechnungs- oder Lieferadresse als Referenz bevorzugt werden soll, oder ob beide Adressen miteinbezogen werden sollen. 

<docrobot_new_in_version version="2.3">
	<p>Dieses Feature ist neu in Isotope eCommerce 2.3</p>
	<p>Neu kann die USt-IdNr. geprüft werden, falls diese gültig ist kann durch auswählen der entsprechenden Option im Steuersatz verhindert werden, dass die Steuer angewendet wird.</p>
</docrobot_new_in_version>


## Name

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
			<td>Name</td>
			<td>-</td>
			<td>Hier kannst du denn Steuersatz-Namen eingeben.</td>
		</tr>
		<tr>
			<td>Bezeichnung</td>
			<td>-</td>
			<td>Die Bezeichnung wird anstelle des Steuersatz-Namens im Frontend beim Bestellprozess angezeigt.</td>
		</tr>
		<tr>
			<td>Steuersatz</td>
			<td>-</td>
			<td>Hier kannst du denn Prozentwert für den Steuersatz festlegen.</td>
		</tr>
	</tbody>
</table>


## Ort

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
			<td>Adressbasis für die Berechnung</td>
			<td>Versanadresse</td>
			<td>Wähle auf Basis welcher Adresse dieser Steuersatz berechnet werden soll. Die Versandadresse für nicht versendbare Produkte.</td>
		</tr>
		<tr>
			<td>Länder</td>
			<td>-</td>
			<td>Wähle die Länder, auf welche diese Steuerklasse zutrifft.</td>
		</tr>
		<tr>
			<td>Bundesländer/Staaten/Regionen</td>
			<td>-</td>
			<td>Wähle die Länder, auf welche diese Steuerklasse zutrifft.</td>
		</tr>
		<tr>
			<td>Postleitzahlen</td>
			<td>-</td>
			<td>Begrenzt den Steuersatz auf Postleitzahlen. Du kannst einen Bereich mit kommaseparierte Liste auswählen (z.B. 1234,1235,1236-1239,1100-1200).</td>
		</tr>
	</tbody>
</table>

## Bedingungen

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
			<td>Zwischensummen-Wertbeschränkung</td>
			<td>-</td>
			<td>Beschränke diesen Steuersatz auf einen bestimmten Zwischensummen-Wert (z.B. für eine Luxussteuer).</td>
		</tr>
	</tbody>
</table>

## Konfiguration

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
			<td>Shop-Konfiguration</td>
			<td>-</td>
			<td>Wähle für welche Shop-Konfiguration dieser Steuersatz gilt.</td>
		</tr>
		<tr>
			<td>USt-IdNr. bei Gültigkeit befreien.</td>
			<td>-</td>
			<td>Die Steuer nicht anwenden, wenn die USt-IdNr. gültig ist.</td>
		</tr>
		<tr>
			<td>Berechnung bei Auslöser beenden</td>
			<td>-</td>
			<td>Andere Berechnungen beenden, wenn dieser Steuersatz ausgelöst wird.</td>
		</tr>
		<tr>
			<td>Nur bei Gästen verwenden</td>
			<td>-</td>
			<td>Diesen Steuersatz für eingeloggte Mitglieder nicht verwenden (ausser die entsprechenden Gruppen sind erlaubt).</td>
		</tr>
		<tr>
			<td>Steuersatz schützen</td>
			<td>-</td>
			<td>Diesen Steuersatz nur bestimmten Mitgliedergruppen zuweisen.</td>
		</tr>
	</tbody>
</table>

## Beispiel:

Für den Verkauf in Deutschland kommen zwei Steuersätze in Frage, der normale und der ermässigte (für z. B. Lebensmittel, Bücher, Zeitschriften).

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-rates/steuersaetze_normal.jpg" alt="Normaler Steuersatz">

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-rates/steuersaetze_ermaessigt.jpg" alt="Ermässigter Steuersatz">
