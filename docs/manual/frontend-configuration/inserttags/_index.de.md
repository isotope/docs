---
title: "InsertTags"
description: "Die Frontend-Konfiguration - InsertTags"
aliases:
    - /de/frontend-konfiguration-inserttags/
weight: 30
---


Isotope eCommerce bietet eine Vielzahl an InsertTags, welche du im Frontend verwenden kannst.

{{< version "2.3" >}}

Die InsertTags wurden in Isotope eCommerce 2.3 vereinheitlicht. Es kann deshalb sein, dass du noch alte InsertTags nutzt. Diese funktionieren noch bis zur Version 3.0, suche dir also schon heute den passenden, neuen InsertTag aus der untenstehenden Liste aus!

## InsertTags für den aktuellen Warenkorb

<table>
	<thead>
		<tr>
			<th>InsertTag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>{{cart::items}}</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte im Warenkorb zurück. Die Mengenangaben werden hier ignoriert. Wurde also <code>Mein Produkt 1</code> vier Mal in den Warenkorb gelegt, so wird dieser InsertTag es nur ein Mal zählen.</td>
		</tr>
		<tr>
			<td><code>{{cart::items_label}}</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte im Warenkorb inklusive der Übersetzung zurück. Beispiel: <code>1 Produkt</code></td>
		</tr>
		<tr>
			<td><code>{{cart::quantity}}</code></td>
			<td>Gibt die totale Anzahl der Produkte im Warenkorb zurück. Die Mengenangaben werden hier berücksichtigt. Wurde also <code>Mein Produkt 1</code> vier Mal in den Warenkorb gelegt, so wird dieser InsertTag es vier Mal zählen.</td>
		</tr>
		<tr>
			<td><code>{{cart::quantity_label}}</code></td>
			<td>Gibt die totale Anzahl der Produkte im Warenkorb inklusive der Übersetzung zurück. Beispiel: <code>4 Produkte</code></td>
		</tr>
		<tr>
			<td><code>{{cart::subtotal}}</code></td>
			<td>Gibt das Subtotal des Warenkorbs zurück. Dieser InsertTag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>{{cart::taxfree_subtotal}}</code></td>
			<td>Gibt das Subtotal des Warenkorbs zurück. Dieser InsertTag berücksichtigt die Steuern nicht.</td>
		</tr>
		<tr>
			<td><code>{{cart::total}}</code></td>
			<td>Gibt das Total des Warenkorbs zurück. Dieser InsertTag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>{{cart::taxfree_total}}</code></td>
			<td>Gibt das Total des Warenkorbs zurück. Dieser InsertTag berücksichtigt die Steuern nicht.</td>
		</tr>
		<tr>
			<td><code>{{cart::billing_address::~}}</code></td>
			<td>Gibt ein gewünschtes Feld von der Rechnungsadresse des Warenkorbs zurück. Beispiel: <code>{{cart::billing_address::firstname}}</code>.</td>
		</tr>
		<tr>
			<td><code>{{cart::shipping_address::~}}</code></td>
			<td>Gibt ein gewünschtes Feld von der Versandadresse des Warenkorbs zurück. Beispiel: <code>{{cart::shipping_address::firstname}}</code>.</td>
		</tr>
		<tr>
			<td><code>{{cart::~}}</code></td>
			<td>Alle Parameter die nicht auf einen der vorangehenden zutreffen, werden direkt auf der Datenbank-Tabelle <code>tl_iso_product_collection</code> gesucht, wobei sich der Platzhalter auf die entsprechende Spalte bezieht. Nutze diesen InsertTag z.B. um die Währung zu erhalten: <code>{{cart::currency}}</td>
		</tr>
	</tbody>
</table>

## InsertTags für die aktuelle Bestellung

{{% notice warning %}}<p>Um die aktuelle Bestellung ermitteln zu können, muss der GET-Parameter "uid" in der URL stehen. Dies ist beispielsweise auf der Bestellbestätigungsseite der Fall. Aussehen würde das in etwa so: "complete.html?uid=550af3fe73763"</p>{{% /notice %}}

<table>
	<thead>
		<tr>
			<th>InsertTag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>{{order::items}}</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte in der Bestellung zurück. Die Mengenangaben werden hier ignoriert. Wurde also <code>Mein Produkt 1</code> vier Mal bestellt, so wird dieser InsertTag es nur ein Mal zählen.</td>
		</tr>
		<tr>
			<td><code>{{order::items_label}}</code></td>
			<td>Gibt die Anzahl der einzelnen Produkte in der Bestellung inklusive der Übersetzung zurück. Beispiel: <code>1 Produkt</code></td>
		</tr>
		<tr>
			<td><code>{{order::quantity}}</code></td>
			<td>Gibt die totale Anzahl der Produkte in der Bestellung zurück. Die Mengenangaben werden hier berücksichtigt. Wurde also <code>Mein Produkt 1</code> vier Mal bestellt, so wird dieser InsertTag es vier Mal zählen.</td>
		</tr>
		<tr>
			<td><code>{{order::quantity_label}}</code></td>
			<td>Gibt die totale Anzahl der Produkte in der Bestellung inklusive der Übersetzung zurück. Beispiel: <code>4 Produkte</code></td>
		</tr>
		<tr>
			<td><code>{{order::subtotal}}</code></td>
			<td>Gibt das Subtotal der Bestellung zurück. Dieser InsertTag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>{{order::taxfree_subtotal}}</code></td>
			<td>Gibt das Subtotal der Bestellung zurück. Dieser InsertTag berücksichtigt die Steuern nicht.</td>
		</tr>
		<tr>
			<td><code>{{order::total}}</code></td>
			<td>Gibt das Total der Bestellung zurück. Dieser InsertTag berücksichtigt auch die Steuern.</td>
		</tr>
		<tr>
			<td><code>{{order::taxfree_total}}</code></td>
			<td>Gibt das Total der Bestellung zurück. Dieser InsertTag berücksichtigt die Steuern nicht.</td>
		</tr>
		<tr>
			<td><code>{{order::billing_address::~}}</code></td>
			<td>Gibt ein gewünschtes Feld von der Rechnungsadresse der Bestellung zurück. Beispiel: <code>{{order::billing_address::firstname}}</code>.</td>
		</tr>
		<tr>
			<td><code>{{order::shipping_address::~}}</code></td>
			<td>Gibt ein gewünschtes Feld von der Versandadresse der Bestellung zurück. Beispiel: <code>{{order::shipping_address::firstname}}</code>.</td>
		</tr>
		<tr>
			<td><code>{{order::~}}</code></td>
			<td>Alle Parameter die nicht auf einen der vorangehenden zutreffen, werden direkt auf der Datenbank-Tabelle <code>tl_iso_product_collection</code> gesucht, wobei sich der Platzhalter auf die entsprechende Spalte bezieht. Nutze diesen InsertTag z.B. um die Bestellnummer zu erhalten: <code>{{order::document_number}}</td>
		</tr>
	</tbody>
</table>

## Produktspezifische InsertTags

<table>
	<thead>
		<tr>
			<th>InsertTag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>{{product::~}}</code></td>
			<td>Gibt ein bestimmtes Attribut des aktuellen Produkts (Produkt-Alias in der URL) zurück. Beispiel: <code>{{product::name}}</td>
		</tr>
		<tr>
			<td><code>{{product::~::~}}</code></td>
			<td>Gibt ein bestimmtes Attribut eines bestimmten Produkts (Produkt-ID) zurück. Beispiel: <code>{{product::name::42}}</td>
		</tr>
	</tbody>
</table>

## InsertTags für Übersetzungen

Für weitere Informationen zu den Übersetzung verweisen wir dich an dieser Stelle zur entsprechenden
[Dokumentation](/de/backend-konfiguration-shop-verschiedenes-Übersetzungen/).

<table>
	<thead>
		<tr>
			<th>InsertTag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>{{isolabel::~}}</code></td>
			<td>Gibt die Übersetzung einer bestimmten Zeichenfolge in der Sprache der aktuellen Seite zurück. Beispiel: <code>{{isolabel::Meine Zeichenfolge}}</td>
		</tr>
		<tr>
			<td><code>{{isolabel::~::~}}</code></td>
			<td>Gibt die Übersetzung einer bestimmten Zeichenfolge in einer bestimmten Sprache zurück. Beispiel: <code>{{isolabel::Meine Zeichenfolge::en_US}}</td>
		</tr>
	</tbody>
</table>


## Simple Token Timestamp mit InsertTag formatieren

Über folgende Anpassung des InsertTag kann die Ausgabe des Datums und der Uhrzeit anhand der Date-Funktion (weiterführender Link: [PHP Date-Funktion][1]) beeinflusst werden:

<table>
	<thead>
		<tr>
			<th>InsertTag</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>{{formatted_datetime::##collection_locked##::<strong>d.m.Y</strong>}}</code></td>
			<td>Gib hier das gewünschte Format über die Date-Funktion ein. Bei <code>d.m.Y</code> sieht die Ausgabe wie folgt aus <code>01.09.2014</code>.</td>
		</tr>
		<tr>
			<td><code>{{formatted_datetime::##collection_locked##::<strong>date</strong>}}</code></td>
			<td>Mit <code>date</code> wird das Datumsformat welches du unter Einstellungen oder im Starpunkt der Seite festgelegt hast, verwendet.</td>
		</tr>
		<tr>
			<td><code>{{formatted_datetime::##collection_locked##::<strong>time</strong>}}</code></td>
			<td>Mit <code>time</code> wird das Zeitformat welches du unter Einstellungen oder im Starpunkt der Seite festgelegt hast, verwendet.</td>
		</tr>
		<tr>
			<td><code>{{formatted_datetime::##collection_locked##::<strong>datim</strong>}}</code></td>
			<td>Mit <code>datim</code> wird das Datums- und Zeitformat welches du unter Einstellungen oder im Starpunkt der Seite festgelegt hast, verwendet.</td>
		</tr>
	</tbody>
</table>

[1]: http://php.net/manual/de/function.date.php#refsect1-function.date-parameters
