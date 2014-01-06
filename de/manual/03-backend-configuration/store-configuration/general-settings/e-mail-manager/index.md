# E-Mail-Vorlagen

Die Bestätigungsmail kann als HTML und/oder Reintext erstellt werden. Dynamische Inhalte werden über die Insert-Syntax integriert. So zum Beispiel `{{user::username}}` oder über die Isotope eigenen Simple-Tokens.


## Simple-Tokens
<table>
<tr>
	<th>Simple-Token</th>
	<th>Beschreibung</th>
</tr>
<tr>
	<td>`##order_id##`</td>
	<td>Eindeutige Nummer dieser Bestellung</td>
</tr>
<tr>
	<td>`##items##`</td>
	<td>Anzahl Artikel im Warenkorb</td>
</tr>
<tr>
	<td>`##products##`</td>
	<td>Anzahl Produkte im Warenkorb</td>
</tr>
<tr>
	<td>`##subTotal##`</td>
	<td>Subtotal der Bestellung</td>
</tr>
<tr>
	<td>`##grandTotal##`</td>
	<td>Gesamttotal der Bestellung</td>
</tr>
<tr>
	<td>`##cart_html##`<br>`##cart_text##`</td>
	<td>Liste der bestellten Artikel im HTML- oder Text-Format</td>
</tr>
<tr>
	<td>`##billing_address##`<br>`##billing_address_text##`</td>
	<td>Rechnungsadresse im HTML- oder Text-Format</td>
</tr>
<tr>
	<td>`##shipping_address##`<br>`##shipping_address_text##`</td>
	<td>Versandadresse im HTML- oder Text-Format</td>
</tr>
<tr>
	<td>`##shipping_method##`</td>
	<td>Bezeichnung der Versandmethode (wie im Backend eingegeben)</td>
</tr>
<tr>
	<td>`##shipping_note##`<br>`##shipping_note_text##`</td>
	<td>Hinweismeldung der gewählten Versandmethode (auch als Nur-Text abrufbar)</td>
</tr>
<tr>
	<td>`##payment_method##`</td>
	<td>Bezeichnung der Zahlungsmethode (wie im Backend eingegeben)</td>
</tr>
<tr>
	<td>`##payment_note##`<br>`##payment_note_text##`</td>
	<td>Hinweismeldung der gewählten Zahlungsart (auch als Nur-Text abrufbar)</td>
</tr>
<tr>
	<td>`##billing_firstname##`<br>`##billing_lastname##`<br>etc.</td>
	<td>Einzelne Felder der Rechnungsadresse</td>
</tr>
<tr>
	<td>`##shipping_firstname##`<br>`##shipping_lastname##`<br>etc.</td>
	<td>Einzelne Felder der Versandadresse</td>
</tr>
<tr>
	<td>`##form_…##`</td>
	<td>Verwenden Sie den Präfix "form_" und den Feldnamen, um Daten aus dem Formular der Bestellbestätigung zu verwenden</td>
</tr>
<tr>
	<td>`##note##`<br>`##note_text##`</td>
	<td>Notiz im HTML- oder Text-Format</td>
</tr>
</table>

 Die fertigen E-Mail-Vorlagen können auch exportiert und in einer anderen Installation importiert und somit wiederverwendet werden.

 Mehr dazu im [Contao-Wiki][1]. 


[1]: http://de.contaowiki.org/Insert-Tags.