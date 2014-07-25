# Konfiguration

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
			<td>Name der Shop-Konfiguration</td>
			<td>-</td>
			<td>Eindeutiger Name welcher nur im Backend verwendet wird.</td>
		</tr>
		<tr>
			<td>Bezeichnung</td>
			<td>-</td>
			<td>Wird für die Ausgabe im Frontend verwendet, z. B. beim <docrobot_route name="store-config-switcher">Shopkonfigurations-Wechsler</docrobot_route>.</td>
		</tr>
		<tr>
			<td>Standard-Konfiguration</td>
			<td>-</td>
			<td>Wenn mehrere Konfigurationen bestehen muss eine dieser Konfigurationen als Standard-Konfiguration aktiviert werden.</td>
		</tr>
	</tbody>
</table>

## Adresse

Hier gibst du die rechtskonforme Adresse des Shop-Betreibers ein.

## Kasse

Hier können die zur Verfügung stehenden Felder für die Rechnungs- und Versandadresse beim Bezahlen ausgewählt werden.

Zur Auswahl stehen:

- Deaktiviert
- Aktiviert (Nicht verpflichtend)
- Aktiviert (Verpflichtend) 

<docrobot_image path="backend-configuration/store-configuration/general-settings/configuration/kasse.png" alt="Felder der Rechnungs- und Versandadresse">

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
			<td>Standard Rechnungsland</td>
			<td>-</td>
			<td>Definiere hier, welches Land, bei der Erstellung einer Rechnungsadresse vorausgewählt sein soll, oder lasse das Feld leer, falls keine Vorauswahl gewünscht ist.</td>
		</tr>
		<tr>
			<td>Standard Versandland</td>
			<td>-</td>
			<td>Definiere hier, welches Land, bei der Erstellung einer Versandadresse vorausgewählt sein soll, oder lasse das Feld leer, falls keine Vorauswahl gewünscht ist.</td>
		</tr>
		<tr>
			<td>Rechnungs-Länder</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, welche Länder für die Rechnungsadresse im Bestellvorgang zur Verfügung stehen.</td>
		</tr>
		<tr>
			<td>Versand-Länder</td>
			<td>-</td>
			<td>Hier kannst du bestimmen, welche Länder für die Versandadresse im Bestellvorgang zur Verfügung stehen.</td>
		</tr>
		<tr>
			<td>Mitgliederländer einschränken</td>
			<td>-</td>
			<td>Hier kannst du die Registrierung bzw. die Verwaltungsmaske persönlicher Daten (seitens Contao) auf die Länder einschränken, welche als Rechnungsadresse bzw. Versandadresse unter <code>Rechnungs-Länder</code> und <code>Versand-Länder</code> angegeben wurden.</td>
		</tr>
	</tbody>
</table>

## Währungs-Formatierung

 <docrobot_message type="info"><p>Achte bei der Währungs-Formatierung auf die ländertypischen Unterschiede.</p></docrobot_message>

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
			<td>Rundungspräzision</td>
			<td>2</td>
			<td>Die zugelassene Dezimal-Präzision bei den Beträgen (z. B. Preis, Mehrwertsteuer, Total) bestimmen. <docrobot_message type="warning"><p>Um die Kompatibilität mit allen Zahlungsmodulen zu Gewährleisten, empfehlen wir dir, einen Wert zwischen 0 und 2 zu verwenden.</p></docrobot_message></td>
		</tr>
		<tr>
			<td>Rundungszuschlag</td>
			<td>0.01</td>
			<td>Definiere hier, welches die kleinste deklarierte Einheit in der jeweiligen Währung ist. Der Schweizer Franken erlaub z. B. nur einen Rundungszuschlag von 0.05.</td>
		</tr>
		<tr>
			<td>Währung</td>
			<td>-</td>
			<td>Hier kannst du die Währung für deinen Shop auswählen.</td>
		</tr>
		<tr>
			<td>Währungs-Formatierung</td>
			<td>-</td>
			<td>Definiere hier, wie Beträge dargestellt werden, d. h. ob ein Komma oder ein Punkt für Dezimalstellen verwendet und wie tausender Gruppierungen gemacht werden sollen.</td>
		</tr>
		<tr>
			<td>Position der Währungsbezeichung/-symbol</td>
			<td>Links des Preises</td>
			<td>Definiere hier, auf welcher Seite der Preisangabe die Währung steht. Beispiel für "Links des Preises" CHF 1'000.00 oder für "Rechts des Preises" 1.000,00 EURO.</td>
		</tr>
		<tr>
			<td>Währungssymbol verwenden</td>
			<td>-</td>
			<td>Definiere hier, ob, falls vorhanden, ein Währungssymbol verwendet werden soll. z. B. € für Euro oder $ für Dollar.</td>
		</tr>
		<tr>
			<td>Leerzeichen einfügen</td>
			<td>-</td>
			<td>Hier kannst du zwischen dem Preis und dem Währungssymbol ein Leerzeichen einfügen lassen.</td>
		</tr>
	</tbody>
</table>

## Währungsumrechnung

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
			<td>Berechnungsfaktor</td>
			<td>1</td>
			<td>Hier kannst du einen Faktor für die Währungsumrechnung bestimmen.</td>
		</tr>
		<tr>
			<td>Berechnungsmodus</td>
			<td>Multiplizieren</td>
			<td>Hier kannst du bestimmen ob der Preis mit dem Faktor dividiert oder multipliziert werden soll.</td>
		</tr>
		<tr>
			<td>Automatischer Währungsrechner</td>
			<td>-</td>
			<td>Hier kannst du einen automatischen Währungsrechner aktivieren.</td>
		</tr>
		<tr>
			<td>Herkunftswährung</td>
			<td>-</td>
			<td>Hier kannst du die Währung für die Berechnung bestimmen.</td>
		</tr>
		<tr>
			<td>Anbieter der Währungsdaten</td>
			<td>European Central Bank</td>
			<td>Hier kannst du dich für einen Anbieter von online Währungsdaten entscheiden.</td>
		</tr>
	</tbody>
</table>

## Bestellungen

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
			<td>Bestellnummer-Präfix</td>
			<td>-</td>
			<td>Hier kannst du der automatisch hochzählenden Bestellnummer ein Präfix hinzufügen.</td>
		</tr>
		<tr>
			<td>Bestellnummern-Länge</td>
			<td>4</td>
			<td>Hier kannst du die minimale Länge der Bestellnummer bestimmen.
			<docrobot_message type="info"><p><code>Bestellnummer-Präfix</code> wird nicht mitgezählt.</p></docrobot_message></td>
		</tr>
		<tr>
			<td>Status für neue Bestellungen</td>
			<td>-</td>
			<td>Hier kannst du den <docrobot_route name="order-status">Status</docrobot_route> für neue Bestellungen bestimmen. <docrobot_message type="warning"><p>Diese Angaben können von einer <docrobot_route name="payment-methods">Zahlungsart</docrobot_route> überschrieben werden.</p></docrobot_message></td>
		</tr>
		<tr>
			<td>Bestellstatus bei einem Fehler</td>
			<td>-</td>
			<td>Hier kannst du den <docrobot_route name="order-status">Status</docrobot_route> für fehlgeschlagene Bestellungen bestimmen.</td>
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
			<td>Templates-Ordner</td>
			<td>-</td>
			<td>Wenn die Checkbox aktiviert ist, kann ein bestimmter Ordner im Templates-Ordner ausgewählt werden. Die Templates in diesem Ordner werden dann automatisch vom System bevorzugt, wenn ihre Namen unverändert sind.</td>
		</tr>
		<tr>
			<td>Mindestbetrag Zwischensumme</td>
			<td>0.00</td>
			<td>Wird der von dir eingegebene Wert im Warenkorb nicht erreicht, kann die Bestellung nicht abgeschlossen werden. <docrobot_message type="info"><p>Mit dem Standardwert <code>0.00</code> wird diese Funktion deaktiviert.</p></docrobot_message></td>
		</tr>
	</tbody>
</table>

## Produkte

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
			<td>Dauer, für die ein Produkt als "Neu" angezeigt wird</td>
			<td>- Tage</td>
			<td>Hier kannst du festlegen, wie lange du ein Produkt in deinem Shop als neu hervorheben möchtest. <docrobot_message type="info"><p>Für den gewählten Zeitraum wird dem Produkt eine CSS-Klasse <code>new</code> hinzugefügt.</p></docrobot_message></td>
		</tr>
	</tbody>
</table>

## Analytics

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
			<td>Google Analytics aktivieren</td>
			<td>-</td>
			<td>Hier kannst du das Tracking mit Google Analytics aktivieren.</td>
		</tr>
		<tr>
			<td>Konto</td>
			<td>-</td>
			<td>Hier musst du deine Google Analytics-Kontonummer mit dem Format <code>UA-XXXXXXXX-X</code> eingeben.</td>
		</tr>
		<tr>
			<td>Mitglieder tracken</td>
			<td>-</td>
			<td>Hier kannst du <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> verwenden, um Mitglieder (z. B. <code>##firstname##</code>) zu tracken. <docrobot_message type="warning"><p>Natürlich musst du die Befugnis zum tracken im Vorfeld bei den Mitgliedern einfordern.</p></docrobot_message></td>
		</tr>
	</tbody>
</table>


 