# Zahlungsart "Saferpay"

[Saferpay][1] ist ein Dienst, mit dem unter anderen Kreditkartenzahlungen durchgeführt werden können. Um den Dienst nutzen zu können, musst du zuvor einen Test-Account beantragen oder einen Vertrag mit dem Dienstleister abschliessen.

## Konfiguration des Zahlungsanbieters

Beim Anlegen der Zahlungsart sind folgende Daten für die Verknüpfung mit Saferpay anzugeben:

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
			<td>Saferpay Account-ID</td>
			<td>-</td>
			<td>
			    Die Account-ID, welche per E-Mail mitgeteilt wird.
			    <docrobot_message type="warning">Es handelt sich bei dieser ID nicht um den Benutzernamen, sondern um das Konto.</docrobot_message>
            </td>
		</tr>
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
		<tr>
            <td>Saferpay API-Benutzer</td>
            <td>-</td>
            <td>
                Hier kannst du den Saferpay JSON API-Benutzer eingeben.
                <docrobot_new_in_version version="2.6"><p>Dieses Feature ist neu in Isotope eCommerce 2.6</p></docrobot_new_in_version>
            </td>
        </tr>
        <tr>
            <td>Saferpay API-Passwort</td>
            <td>-</td>
            <td>
                Hier kannst du das Saferpay JSON API-Passwort eingeben.
                <docrobot_new_in_version version="2.6"><p>Dieses Feature ist neu in Isotope eCommerce 2.6</p></docrobot_new_in_version>
            </td>
        </tr>
		<tr>
			<td>Checkout-Beschreibung</td>
			<td>-</td>
			<td>Diese Beschreibung wird der Kunde auf der Saferpay Checkout-Seite sehen.</td>
		</tr>
		<tr>
			<td>Konfiguration Zahlungsseite (VTCONFIG)</td>
			<td>-</td>
			<td>
				In einem Saferpay-Account kannst du mehrere Payment Pages konfigurieren. Hier gibst du den Namen der Payment Page-Konfiguration an, die verwendet werden soll.
			</td>
		</tr>
        <tr>
            <td>Zahlungsarten</td>
            <td>-</td>
            <td>
                Hier kannst du die verfügbaren Zahlungsmethoden einschränken (z. B. nur MasterCard). Wenn du hier nichts auswählst, sind alle Zahlungsmethoden erlaubt.<br>
                Folden Zahlunsmethoden stehen zur Auswahl:
                <ul>
                    <li>MasterCard</li>
                    <li>Visa</li>
                    <li>American Express</li>
                    <li>Diners Club</li>
                    <li value="5">JCB</li>
                    <li>>Saferpay Testkarte</li>
                    <li>Laser Card</li>
                    <li>Bonus Card</li>
                    <li>PostFinance E-Finance</li>
                    <li>PostFinance Card</li>
                    <li>Maestro International</li>
                    <li>MyOne</li>
                    <li>Lastschrift</li>
                    <li>Rechnung</li>
                    <li>Sofortüberweisung</li>
                    <li>PayPal</li>
                    <li>giropay</li>
                    <li>iDEAL</li>
                    <li>ClickandBuy</li>
                    <li>Homebanking AT (eps)</li>
                    <li>Mpass</li>
                    <li>ePrzelewy</li>
                </ul>
                <docrobot_new_in_version version="2.6"><p>Dieses Feature ist neu in Isotope eCommerce 2.6</p></docrobot_new_in_version>
            </td>
        </tr>
	</tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-saferpay/psp_config.png" alt="Saferpay im Backend">

## Konfiguration der Payment Page

Im Login-Bereich von Saferpay können unter _Administration_ > _Payment Page Konfiguration_ die Payment Pages (PP) erstellt und konfiguriert werden.

### Payment Page Konfiguration

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
			<td>Name der Konfiguration</td>
			<td>-</td>
			<td>
			    Ein frei wählbarer Name.
			    <docrobot_message type="info">Dieser Wert wird in der Konfiguration des Zahlungsanbieters in Contao im Feld <i>Konfiguration Zahlungsseite (VTCONFIG)</i> angegeben.</docrobot_message>
            </td>
		</tr>
		<tr>
			<td>Beschreibung</td>
			<td>-</td>
			<td>
				Beschreibung die dem Kunden auf der PP angezeigt wird.
				<br><br>
				Zusätzlich kannst du hier einstellen, ob die PP aktiv oder inaktiv ist.
			</td>
		</tr>
		<tr>
            <td>Modusauswahl</td>
            <td>PayInit</td>
            <td>
                Hier kannst du auswählen, welche Attribute Vorrang haben:
                <ul>
                    <li><strong>PayInit</strong><br>
                        Attribute im PayInit haben Vorrang gegenüber den im Formular angegeben Werten.
                    </li>
                    <li><strong>VTConfig</strong><br>
                        Die im Formular angegeben Werte haben Vorrang gegenüber den PayInit-Attributen.
                    </li>
                </ul>
                <docrobot_message type="warning">Damit Isotope eCommerce die Bestellung richtig verarbeiten kann, muss hier die Option <i>PayInit</i> ausgewählt werden. Andernfalls wird zwar die Zahlung ausgeführt und die Bestellung angelegt, jedoch eine Fehlermeldung auf der <docrobot_route name="setting-site-structure">Bestelldetails-Seite</docrobot_route> im Shop angezeigt.</docrobot_message>
            </td>
        </tr>
		<tr>
			<td>Standard-Sprache der PP</td>
			<td>-</td>
			<td>
				Hier kannst du die Sprache einstellen, in der die PP standardmässig angezeigt werden soll. Zusätzlich gibt es über die Checkbox die Möglichkeit, dem Kunden eine Sprachauswahl anzuzeigen.
			</td>
		</tr>
	</tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-saferpay/pp_config_1.png" alt="Payment Page-Konfiguration">

### Inhalt der Konfiguration

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
			<td>Adresse der AGB</td>
			<td>-</td>
			<td>
			    Hier kommt der URL zu den AGBs des Shops rein. Zusätzlich kann über die Checkbox eingestellt werden, ob eine Checkbox zum Bestätigen der AGBs auf der Payment Page angezeigt werden soll.
            </td>
		</tr>
		<tr>
			<td>Adressfelder</td>
			<td>-</td>
			<td>Verschiedene Angaben zu den Feldern, die der Kunde auf der Payment Page ausfüllen muss.<br>
			    <ul>
			        <li>Name des Karteninhabers abfragen</li>
			        <li>Adresse des Karteninhabers abfragen</li>
			        <li>Art der Adresse<br>
			        	Angabe ob es sich um die Kunden-, Rechnungs- oder Lieferadresse handelt.</li>
					<li>Pflicht- und optionale Felder<br>
						Welche Felder sollen als Pflichtfeld oder optionales Feld behandelt werden?</li>
			    </ul>
			</td>
		</tr>
	</tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-saferpay/pp_config_2.png" alt="Inhalt der Konfiguration">

### Weiterleitung & Bestätigungsseite

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
			<td>Weiterleitung aktivieren</td>
			<td>-</td>
			<td>
			    Wenn die Checkbox aktiv ist, wird der Kunde nach dem Zahlungsvorgang zum Shop weitergeleitet. Zusätzlich kann die Verzögerung bis zur Weiterleitung in Sekunden angegeben werden.
            </td>
		</tr>
		<tr>
			<td>Adresse der Bestätigungsseite nach <b>erfolgreicher</b> Zahlung</td>
			<td>-</td>
			<td>URL zur Bestelldetailsseite des Shops.</td>
		</tr>
		<tr>
			<td>Adresse der Bestätigungsseite nach <b>nicht</b> erfolgreicher Zahlung</td>
			<td>-</td>
			<td>URL zur Shopseite, die den Kunden auf eine nicht erfolgreiche Zahlung hinweist.</td>
		</tr>
		<tr>
			<td>Adresse der Bestätigungsseite bei <b>Zahlungsabbruch</b> durch den Kunden</td>
			<td>-</td>
			<td>URL zur Shopseite, die den Kunden den Zahlungsabbruch bestätigt.</td>
		</tr>
		<tr>
			<td>E-Mail-Bestätigung senden</td>
			<td>-</td>
			<td>
				Wenn diese Checkbox aktiviert wird, kannst du angeben wer eine Benachrichtigung über den Zahlungsvorgang erhält. Diese Funktion ist nur für den Shopbetreiber relevant, nicht für den Kunden.
			</td>
		</tr>
	</tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-saferpay/pp_config_3.png" alt="Weiterleitungen">

### Datenübergabe

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
			<td>PP soll Server benachrichtigen</td>
			<td>-</td>
			<td>
				Wenn aktiviert, kann hier der URL zur postsale.php angegeben werden. Saferpay benachrichtigt dann den Shop über den erfolgreichen Zahlungsvorgang.

			    <docrobot_message type="info">Diese Option muss nicht aktiviert werden, damit die Bestellung in Isotope eCommerce angelegt wird.</docrobot_message>
            </td>
		</tr>
	</tbody>
</table>

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-saferpay/pp_config_4.png" alt="Datenübergabe">

[1]: https://www.six-payment-services.com/de/site/e-commerce/solutions/paymentsolution.html
