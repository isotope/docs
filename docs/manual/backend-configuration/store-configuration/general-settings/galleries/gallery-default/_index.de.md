---
title: "Standard Galerie"
description: "Die Shop-Konfiguration - Allgemeine Einstellungen - Standard Galerie."
aliases:
    - /de/backend-konfiguration-shop-allgemein-galerie-standard/
weight: 10   
---


Die `Standard Galerie` zeigt eine normale Bildergalerie an, wie man sie sich vorstellt. Sie gibt kleine Vorschaubilder (Thumbnails) und eine Grossansicht eines Bildes aus. Optional kann auch die Grossansicht in einer Lightbox gewählt werden.

## Grundkonfiguration

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
			<td>Bildanker</td>
			<td>-</td>
			<td>Hier kannst du einstellen, was bei Klick auf die Grossansicht des Bildes geschehen soll. Verwendest du diese Galerie in der <docrobot_route name="product-list">Produktliste</docrobot_route> so bietet sich an, dass du hier <code>Link zu den Produktdetails</code> auswählst. Typischerweise lässt man beim <docrobot_route name="product-reader">Produktleser</docrobot_route> dann eine <code>Lightbox/Mediabox öffnen</code>. Du kannst aber auch gar <code>keine Link-Aktion</code> ausführen lassen, ganz wie du möchtest.</td>
		</tr>
		<tr>
			<td>Platzhalter-Bild</td>
			<td>-</td>
			<td>Typischerweise gibt es gerade während der Entwicklungsphase eines Shops immer mal wieder Produkte, die noch über kein Produktbild verfügen. Hier kannst du optional einen Platzhalter definieren.</td>
		</tr>
	</tbody>
</table>

## Bildgrössen

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
			<td>Hauptbildgrösse</td>
			<td>-</td>
			<td>Hier stellst du ein, wie die Grossansicht eines Bildes zugeschnitten werden soll. Ein Bild ist in diesem Galerietyp immer das Hauptbild. Diese Einstellung bezieht sich auf dieses Bild.</td>
		</tr>
		<tr>
			<td>Galeriegrösse</td>
			<td>-</td>
			<td>Hier stellst du ein, wie die restlichen Bilder zugeschnitten werden sollen. Alle weiteren Bilder ausser dem Hauptbild sind Galeriebilder. Diese Einstellung bezieht sich auf diese Bilder.</td>
		</tr>
	</tbody>
</table>

## Wasserzeichen

Wasserzeichen können gerade beim Verkauf von Bildprodukten ganz hilfreich sein.

{{% notice warning %}}<p>Wasserzeichen werden <strong>nicht</strong> mit den jeweiligen Bildern verkleinert sondern 1:1 so angewendet, wie du sie erstellt hast!</p>{{% /notice %}}

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
			<td>Hauptbild-Wasserzeichen</td>
			<td>-</td>
			<td>Hier kannst du ein Wasserzeichen-Bild auswählen, welches auf dein Hauptbild angewendet wird.</td>
		</tr>
		<tr>
			<td>Hauptbild-Wasserzeichen-Position</td>
			<td>-</td>
			<td>Die Position eines Wasserzeichens kann wichtig sein. Hier kannst du definieren, wie Isotope eCommerce dieses für dein Hauptbild positionieren soll.</td>
		</tr>
		<tr>
			<td>Galeriebilder-Wasserzeichen</td>
			<td>-</td>
			<td>Hier kannst du ein Wasserzeichen-Bild auswählen, welches auf deine Galeriebilder angewendet wird.</td>
		</tr>
		<tr>
			<td>Galeriebilder-Wasserzeichen-Position</td>
			<td>-</td>
			<td>Die Position eines Wasserzeichens kann wichtig sein. Hier kannst du definieren, wie Isotope eCommerce dieses für deine Galeriebilder positionieren soll.</td>
		</tr>
	</tbody>
</table>


## Template-Einstellungen

{{< version "2.2" >}}

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
			<td>Eigenes Galerie-Template</td>
			<td>-</td>
			<td>Hier kannst du ein eigenes Galerie-Template auswählen und so die HTML-Ausgabe im Frontend beeinflussen.</td>
		</tr>
	</tbody>
</table>
