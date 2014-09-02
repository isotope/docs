# Inserttags

Isotope eCommerce bietet eine Vielzahl an Inserttags, welche du im Frontend verwenden kannst.

## Generelle Inserttags

<table>
	<thead>
		<tr>
			<th>Inserttag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>[{]isotope::cart_items[}]</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte im Warenkorb zurück. Die Mengenangaben werden hier ignoriert. Wurde also <code>Mein Produkt 1</code> vier Mal in den Warenkorb gelegt, so wird dieser Inserttag es nur ein Mal zählen.</td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_items_label[}]</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte im Warenkorb inklusive der Übersetzung zurück. Beispiel: <code>1 Produkt</code></td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_quantity[}]</code></td>
			<td>Gibt die totale Anzahl der Produkte im Warenkorb zurück. Die Mengenangaben werden hier berücksichtigt. Wurde also <code>Mein Produkt 1</code> vier Mal in den Warenkorb gelegt, so wird dieser Inserttag es vier Mal zählen.</td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_quantity_label[}]</code></td>
			<td>Gibt die totale Anzahl der Produkte im Warenkorb inklusive der Übersetzung zurück. Beispiel: <code>4 Produkte</code></td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_subtotal[}]</code></td>
			<td>Gibt das Subtotal des Warenkorbs zurück. Dieser Inserttag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_taxfree_subtotal[}]</code></td>
			<td>Gibt das Subtotal des Warenkorbs zurück. Dieser Inserttag berücksichtigt die Steuern nicht.</td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_total[}]</code></td>
			<td>Gibt das Total des Warenkorbs zurück. Dieser Inserttag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>[{]isotope::cart_taxfree_total[}]</code></td>
			<td>Gibt das Total des Warenkorbs zurück. Dieser Inserttag berücksichtigt die Steuern nicht.</td>
		</tr>
	</tbody>
</table>

## Produktspezifische Inserttags

<table>
	<thead>
		<tr>
			<th>Inserttag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>[{]product::~[}]</code></td>
			<td>Gibt ein bestimmtes Attribut des aktuellen Produkts (Produkt-Alias in der URL) zurück. Beispiel: <code>[{]product::name[}]</td>
		</tr>
		<tr>
			<td><code>[{]product::~::~[}]</code></td>
			<td>Gibt ein bestimmtes Attribut eines bestimmten Produkts (Produkt-ID) zurück. Beispiel: <code>[{]product::name::42[}]</td>
		</tr>
	</tbody>
</table>

## Bestellungsspezifische Inserttags

<table>
	<thead>
		<tr>
			<th>Inserttag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>[{]order::~[}]</code></td>
			<td>Dieser Inserttag geht direkt auf die Datenbank-Tabelle <code>tl_iso_product_collection</code>, wobei sich der Platzhalter auf die entsprechende Spalte bezieht. Nutze diesen Inserttag z.B. um die Bestellnummer zu erhalten: <code>[{]order::document_number[}]</td>
		</tr>
	</tbody>
</table>

## Inserttags für Übersetzungen

Für weitere Informationen zu den Übersetzung verweisen wir dich an dieser Stelle zur <docrobot_route name="translations">entsprechenden Dokumentation</docrobot_route>.

<table>
	<thead>
		<tr>
			<th>Inserttag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>[{]isolabel::~[}]</code></td>
			<td>Gibt die Übersetzung einer bestimmten Zeichenfolge in der Sprache der aktuellen Seite zurück. Beispiel: <code>[{]isolabel::Meine Zeichenfolge[}]</td>
		</tr>
		<tr>
			<td><code>[{]isolabel::~::~[}]</code></td>
			<td>Gibt die Übersetzung einer bestimmten Zeichenfolge in einer bestimmten Sprache zurück. Beispiel: <code>[{]isolabel::Meine Zeichenfolge::en_US[}]</td>
		</tr>
	</tbody>
</table>


## Simple Token Timestamp mit Inserttag formatieren


