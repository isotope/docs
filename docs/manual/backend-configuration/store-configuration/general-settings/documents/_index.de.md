---
title: "Dokumente"
description: "Die Shop-Konfiguration - Allgemeine Einstellungen - Dokumente."
aliases:
    - /de/backend-konfiguration-shop-allgemein-dokumente/
weight: 20    
---


In Isotope eCommerce dienen `Dokumente` immer zur Darstellung einer Produktsammlung.
Im Kern von Isotope sprechen wir hier von PDF-Dateien. Es wäre aber auch denkbar, beliebige Ausgabeformate (von `.docx` bis zu `.odt`) zu unterstützen, sofern die entsprechenden Hilfsmittel auf dem Server zur Verfügung stehen.

Im Kern von Isotope eCommerce wird aktuell nur der Dokumententyp `Standard` zur Verfügung gestellt. Er ist vergleichbar mit der Druckfunktion für Artikel des Contao Kerns: Er versucht aus HTML-Code ein PDF zu generieren.

Du kannst beliebig viele Dokumente anlegen und sie dann in anderen Teilen von Isotope eCommerce auswählen. Denkbar sind etwa:

* Rechnung
* Bestellbestätigung
* Versandbestätigung
* etc.

Da in den meisten Fällen eine Rechnung gewünscht ist, wird nachfolgend die Konfiguration einer solchen veranschaulicht.

![Beispieleinstellung für ein Rechnungsdokument](invoice.png)

## Name & Typ

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
			<td>Dokumentname</td>
			<td>-</td>
			<td>Hier kannst du eine interne Bezeichnung für das Dokument eingeben.</td>
		</tr>
		<tr>
			<td>Dokumententyp</td>
			<td>-</td>
			<td>Wähle hier den gewünschten Dokumenttypen aus.</td>
		</tr>
	</tbody>
</table>

{{% notice info %}}<p>Der Programmierer deines Vertrauens kann Dokumenttypen programmieren und sie dir hier zur Auswahl zur Verfügung stellen. Sollten dir also die bestehenden Dokumenttypen nicht ausreichen, bietet dir Isotope eCommerce die Flexibilität, das zu korrigieren.</p>{{% /notice %}}

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
			<td>Dokumententitel</td>
			<td>-</td>
			<td>Hier kannst du definieren, wie der Titel des Dokuments lauten soll. Er steht im Template als Variable zur Verfügung und stellt die Überschrift dar. Nutze <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> (<code>collection_*</code>), wobei <code>*</code> für die Zeile der Datenbank-Tabelle <code>tl_iso_product_collection</code> steht. Ein klassisches Beispiel wäre die generierte Dokumenten-Nummer oder in diesem Fall die Rechnungsnummer: <code>Ihre Rechnung ##collection_document_number##</code>.</td>
		</tr>
		<tr>
			<td>Dateiname</td>
			<td>-</td>
			<td>Hier kannst du definieren, wie der generierte Dateiname des Dokuments lauten soll. Nutze <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> (<code>collection_*</code>), wobei <code>*</code> für die Zeile der Datenbank-Tabelle <code>tl_iso_product_collection</code> steht. Ein klassisches Beispiel wäre die generierte Dokumenten-Nummer oder in diesem Fall die Rechnungsnummer: <code>rechnung_##collection_document_number##</code>.</td>
		</tr>
	</tbody>
</table>

## Template

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
			<td>Dokumenten-Template</td>
			<td>-</td>
			<td>Diese Einstellung bezieht sich auf das HTML-Template rund um das <code>Sammlung-Template</code>. Hier kannst du also ein Template auswählen, in dem du bspw. die Rechnungsadresse anderswo platzierst oder etwa ein Logo deines Unternehmens hinzufügst.</td>
		</tr>
		<tr>
			<td>Galerie</td>
			<td>-</td>
			<td>Hier kannst du die Galerie auswählen, mit der die Produktbilder in dem Dokument verarbeitet werden. Wählst du hier nichts aus, wird das Template des jeweiligen Produkttyps gewählt (empfohlen).</td>
		</tr>
		<tr>
			<td>Sammlung-Template</td>
			<td>iso_collection_invoice</td>
			<td>Hier kannst du ein Produktsammlung-Template auswählen und so die Darstellung der Produkte in deinem Dokument beliebig verändern.
			Auswahl Möglichkeiten:
			<ul>
				 - iso_collection_default
				 - iso_collection_favorites
				 - iso_collection_invoice
				 - iso_collection_mini
			</ul>
			</td>
		</tr>
		<tr>
			<td>Sortierung</td>
			<td>nach Datum hinzugefügt (aufsteigend)</td>
			<td>Diese Auswahl ermöglicht dir, die Reihenfolge in der die Produkte in diesem Dokument aufgelistet werden, zu bestimmen.
			Auswahl Möglichkeiten:
			<ul>
				 - nach Datum hinzugefügt (aufsteigend)
				 - nach Datum hinzugefügt (absteigend)
				 - nach Datum aktualisiert (aufsteigend)
				 - nach Datum aktualisiert (absteigend)
				 - nach Produktnamen (aufsteigend)
				 - nach Produktnamen (absteigend)
				 - nach Preis (aufsteigend)
				 - nach Preis (absteigend)
			</ul>
			</td>
		</tr>
	</tbody>
</table>
