# Simple Tokens

Simple Tokens ist womöglich eines der meistunterschätzten Features innerhalb von Contao und wird im Kern von Contao leider auch nur für das Newsletter-Modul verwendet.

Simple Tokens werden deshalb [in der offiziellen Dokumentation][1] auch nur kurz angerissen.

In Isotope eCommerce werden die Tokens oft verwendet, weil sie dir viel Flexibilität geben.
Sie werden unter anderem hier verwendet:

* Im gesamten <docrobot_route name="notifications">Benachrichtigungszentrum</docrobot_route>
* Für die Darstellung der Adressen der verschiedenen Länder (bspw. PLZ vor oder nach Ort etc.)
* In den <docrobot_route name="documents">Dokumenten</docrobot_route>, um den Dokumententitel sowie den Dokumenten-Dateinamen zu individualisieren

<docrobot_message type="info"><p>Im Benachrichtigungszentrum kriegst du übrigens durch einfaches Tippen von `##` einen Autocompleter, der dich bei der Auswahl der Tokens assistiert.</p></docrobot_message>

Simple Tokens unterstützen im Gegensatz zu Inserttags auch einfache If-Else-Abfragen wodurch z.B. in Bestellbestätigungs-E-Mails auch sowas möglich wäre:

<pre>
{if billing_address_gender=="male"}
Sehr geehrter Herr ##billing_address_lastname##,
{elseif billing_address_gender=="female"}
Sehr geehrte Frau ##billing_address_lastname##,
{else}
Sehr geehrte Damen und Herren,
{endif}
</pre>

## Isotope-spezifische Felder

<table>
	<thead>
		<tr><th>Simple Token</th><th>Beschreibung</th></tr>
	</thead>
	<tbody>
		<tr><td><code>##uniqid##</code></td><td>Eindeutige ID der Bestellung.</td></tr>
		<tr><td><code>##order_status##</code></td><td>Bezeichnung des derzeitigen Status der Bestellung.</td></tr>
		<tr><td><code>##order_status_old##</code></td><td>Bezeichnung des vorherigen Bestellstatus. Nützlich beispielsweise für "Bestellstatus änderte sich von x zu y".</td></tr>
		<tr><td><code>##order_status_id##</code></td><td>Die ID des derzeitigen Status der Bestellung.</td></tr>
		<tr><td><code>##order_status_id_old##</code></td><td>ID des vorherigen Status der Bestellung.</td></tr>
		<tr><td><code>##recipient_email##</code></td><td>Die E-Mail-Adresse des Empfängers.</td></tr>
		<tr><td><code>##order_id##</code></td><td>Die ID der Bestellung.</td></tr>
		<tr><td><code>##order_items##</code></td><td>Die Anzahl der Artikel (Anzahl aufsummiert) in der Bestellung.</td></tr>
		<tr><td><code>##order_products##</code></td><td>Die Anzahl von individuellen Produkten in der Bestellung.</td></tr>
		<tr><td><code>##order_subtotal##</code></td><td>Zwischensumme der Bestellung.</td></tr>
		<tr><td><code>##order_total##</code></td><td>Gesamtsumme der Bestellung.</td></tr>
		<tr><td><code>##document_number##</code></td><td>Die Dokumentennummer der Bestellung.</td></tr>
		<tr><td><code>##cart_text##</code></td><td>Bestellung/Warenkorb im Text-Format.</td></tr>
		<tr><td><code>##cart_html##</code></td><td>Bestellung/Warenkorb in HTML.</td></tr>
		<tr><td><code>##document##</code></td><td>Das Dokument, welches angehängt werden soll (z. B. eine Rechnung).</td></tr>
		<tr><td><code>##form_*##</code></td><td>Alle im Formulargenerator angelegten Felder.</td></tr>
		<tr><td><code>##payment_id##</code></td><td>ID der Zahlungsart.</td></tr>
		<tr><td><code>##payment_label##</code></td><td>Zahlungsart-Beschriftung.</td></tr>
		<tr><td><code>##payment_note##</code></td><td>Notiz zur Zahlungsart.</td></tr>
		<tr><td><code>##shipping_id##</code></td><td>ID der Versandart.</td></tr>
		<tr><td><code>##shipping_label##</code></td><td>Versandart-Name.</td></tr>
		<tr><td><code>##shipping_note##</code></td><td>Versandart-Hinweis.</td></tr>
	</tbody>
</table>


## Rechnungsadressfelder

<table>
	<thead>
		<tr><th>Simple Token</th><th>Beschreibung</th></tr>
	</thead>
	<tbody>
		<tr><td><code>##billing_address_gender##</code></td><td>Das Rechnungsadressfeld für "Geschlecht".</td></tr>
		<tr><td><code>##billing_address_salutation##</code></td><td>Das Rechnungsadressfeld für "Anrede".</td></tr>
		<tr><td><code>##billing_address_firstname##</code></td><td>Das Rechnungsadressfeld für "Vorname".</td></tr>
		<tr><td><code>##billing_address_lastname##</code></td><td>Das Rechnungsadressfeld für "Nachname".</td></tr>
		<tr><td><code>##billing_address_dateOfBirth##</code></td><td>Das Rechnungsadressfeld für "Geburtsdatum".</td></tr>
		<tr><td><code>##billing_address_company##</code></td><td>Das Rechnungsadressfeld für "Firma".</td></tr>
		<tr><td><code>##billing_address_vat_no##</code></td><td>Das Rechnungsadressfeld für "USt-IdNr.".</td></tr>
		<tr><td><code>##billing_address_street_1##</code></td><td>Das Rechnungsadressfeld für "Strasse".</td></tr>
		<tr><td><code>##billing_address_street_2##</code></td><td>Das Rechnungsadressfeld für "Strasse 2".</td></tr>
		<tr><td><code>##billing_address_street_3##</code></td><td>Das Rechnungsadressfeld für "Strasse 3".</td></tr>
		<tr><td><code>##billing_address_postal##</code></td><td>Das Rechnungsadressfeld für "Postleitzahl".</td></tr>
		<tr><td><code>##billing_address_city##</code></td><td>Das Rechnungsadressfeld für "Ort".</td></tr>
		<tr><td><code>##billing_address_subdivision##</code></td><td>Das Rechnungsadressfeld für "Staat".</td></tr>
		<tr><td><code>##billing_address_country##</code></td><td>Das Rechnungsadressfeld für "Land".</td></tr>
		<tr><td><code>##billing_address_phone##</code></td><td>Das Rechnungsadressfeld für "Telefonnummer".</td></tr>
		<tr><td><code>##billing_address_email##</code></td><td>Das Rechnungsadressfeld für "E-Mail-Adresse".</td></tr>
	</tbody>
</table>


## Versandadressfelder

<table>
	<thead>
		<tr><th>Simple Token</th><th>Beschreibung</th></tr>
	</thead>
	<tbody>
		<tr><td><code>##shipping_address_gender##</code></td><td>Das Versandadressfeld für "Geschlecht".</td></tr>
		<tr><td><code>##shipping_address_salutation##</code></td><td>Das Versandadressfeld für "Anrede".</td></tr>
		<tr><td><code>##shipping_address_firstname##</code></td><td>Das Versandadressfeld für "Vorname".</td></tr>
		<tr><td><code>##shipping_address_lastname##</code></td><td>Das Versandadressfeld für "Nachname".</td></tr>
		<tr><td><code>##shipping_address_dateOfBirth##</code></td><td>Das Versandadressfeld für "Geburtsdatum".</td></tr>
		<tr><td><code>##shipping_address_company##</code></td><td>Das Versandadressfeld für "Firma".</td></tr>
		<tr><td><code>##shipping_address_vat_no##</code></td><td>Das Versandadressfeld für "USt-IdNr.".</td></tr>
		<tr><td><code>##shipping_address_street_1##</code></td><td>Das Versandadressfeld für "Strasse".</td></tr>
		<tr><td><code>##shipping_address_street_2##</code></td><td>Das Versandadressfeld für "Strasse 2".</td></tr>
		<tr><td><code>##shipping_address_street_3##</code></td><td>Das Versandadressfeld für "Strasse 3".</td></tr>
		<tr><td><code>##shipping_address_postal##</code></td><td>Das Versandadressfeld für "Postleitzahl".</td></tr>
		<tr><td><code>##shipping_address_city##</code></td><td>Das Versandadressfeld für "Ort".</td></tr>
		<tr><td><code>##shipping_address_subdivision##</code></td><td>Das Versandadressfeld für "Staat".</td></tr>
		<tr><td><code>##shipping_address_country##</code></td><td>Das Versandadressfeld für "Land".</td></tr>
		<tr><td><code>##shipping_address_phone##</code></td><td>Das Versandadressfeld für "Telefonnummer".</td></tr>
		<tr><td><code>##shipping_address_email##</code></td><td>Das Versandadressfeld für "E-Mail-Adresse".</td></tr>
	</tbody>
</table>


## Shop-Konfigurationfelder

<table>
	<thead>
		<tr><th>Simple Token</th><th>Beschreibung</th></tr>
	</thead>
	<tbody>
		<tr><td><code>##config_address_firstname##</code></td><td>Das Shop-Konfigurationfeld für "Vorname".</td></tr>
		<tr><td><code>##config_address_lastname##</code></td><td>Das Shop-Konfigurationfeld für "Nachname".</td></tr>
		<tr><td><code>##config_address_company##</code></td><td>Das Shop-Konfigurationfeld für "Firma".</td></tr>
		<tr><td><code>##config_address_vat_no##</code></td><td>Das Shop-Konfigurationfeld für "USt-IdNr.".</td></tr>
		<tr><td><code>##config_address_street_1##</code></td><td>Das Shop-Konfigurationfeld für "Strasse".</td></tr>
		<tr><td><code>##config_address_street_2##</code></td><td>Das Shop-Konfigurationfeld für "Strasse 2".</td></tr>
		<tr><td><code>##config_address_street_3##</code></td><td>Das Shop-Konfigurationfeld für "Strasse 3".</td></tr>
		<tr><td><code>##config_address_postal##</code></td><td>Das Shop-Konfigurationfeld für "Postleitzahl".</td></tr>
		<tr><td><code>##config_address_city##</code></td><td>Das Shop-Konfigurationfeld für "Ort".</td></tr>
		<tr><td><code>##config_address_subdivision##</code></td><td>Das Shop-Konfigurationfeld für "Staat".</td></tr>
		<tr><td><code>##config_address_country##</code></td><td>Das Shop-Konfigurationfeld für "Land".</td></tr>
		<tr><td><code>##config_address_phone##</code></td><td>Das Shop-Konfigurationfeld für "Telefonnummer".</td></tr>
		<tr><td><code>##config_address_email##</code></td><td>Das Shop-Konfigurationfeld für "E-Mail-Adresse".</td></tr>
	</tbody>
</table>


## Contao-Mitgliederfelder

<table>
	<thead>
		<tr><th>Simple Token</th><th>Beschreibung</th></tr>
	</thead>
	<tbody>
		<tr><td><code>##member_address_firstname##</code></td><td>Das Contao-Mitgliederfeld für "Vorname".</td></tr>
		<tr><td><code>##member_address_lastname##</code></td><td>Das Contao-Mitgliederfeld für "Nachname".</td></tr>
		<tr><td><code>##member_address_dateOfBirth##</code></td><td>Das Contao-Mitgliederfeld für "Geburtsdatum".</td></tr>
		<tr><td><code>##member_address_gender##</code></td><td>Das Contao-Mitgliederfeld für "Geschlecht".</td></tr>
		<tr><td><code>##member_address_company##</code></td><td>Das Contao-Mitgliederfeld für "Firma".</td></tr>
		<tr><td><code>##member_address_street##</code></td><td>Das Contao-Mitgliederfeld für "Strasse".</td></tr>
		<tr><td><code>##member_address_postal##</code></td><td>Das Contao-Mitgliederfeld für "Postleitzahl".</td></tr>
		<tr><td><code>##member_address_city##</code></td><td>Das Contao-Mitgliederfeld für "Ort".</td></tr>
		<tr><td><code>##member_address_state##</code></td><td>Das Contao-Mitgliederfeld für "Staat".</td></tr>
		<tr><td><code>##member_address_country##</code></td><td>Das Contao-Mitgliederfeld für "Land".</td></tr>
		<tr><td><code>##member_address_phone##</code></td><td>Das Contao-Mitgliederfeld für "Telefonnummer".</td></tr>
		<tr><td><code>##member_address_mobile##</code></td><td>Das Contao-Mitgliederfeld für "Handynummer".</td></tr>
		<tr><td><code>##member_address_fax##</code></td><td>Das Contao-Mitgliederfeld für "Faxnummer".</td></tr>
		<tr><td><code>##member_address_email##</code></td><td>Das Contao-Mitgliederfeld für "E-Mail-Adresse".</td></tr>
		<tr><td><code>##member_address_website##</code></td><td>Das Contao-Mitgliederfeld für "Webseite".</td></tr>
		<tr><td><code>##member_address_language##</code></td><td>Das Contao-Mitgliederfeld für "Sprache".</td></tr>
		<tr><td><code>##member_address_username##</code></td><td>Das Contao-Mitgliederfeld für "Benutzername".</td></tr>
		<tr><td><code>##member_address_dateAdded##</code></td><td>Das Contao-Mitgliederfeld für "Hinzugefügt am".</td></tr>
	</tbody>
</table>


[1]: https://contao.org/de/manual/3.2/managing-content.html#newsletter-personalisieren