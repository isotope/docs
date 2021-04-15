---
menuTitle: "Versandgruppierung"
title: "Versandart Versandgruppierung"
description: "Die Shop-Konfiguration - Bestellablauf - Versandarten - Versandgruppierung."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-versandarten-versandgruppierung/
weight: 110    
---


Die Versandart "Versandgruppierung" gruppiert bzw. kombiniert mehrere 
[Pauschalversand-Methoden](/de/backend-konfiguration-shop-bestellablauf-versandarten-pauschalversand/) und kann so zu 
einem sehr mächtigen Instrument werden. Beispiele die mit dieser Versandart erreicht werden können:

* Bis Warenkorb-Betrag € 100.- kostet der Versand € xx.xx und ab € 100.- kostet er € xx.xx
* Nach Deutschland kostet der Versand € xx.xx, in die Schweiz € xx.xx
* etc.


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
			<td>Versandarten</td>
			<td>-</td>
			<td>Hier werden alle anderen Versandarten aufgelistet. Hier kannst du bestimmen aus welchen Versandarten zu eine Gruppierung vornehmen willst. Ausserdem kannst du sie sortieren, was einen Einfluss auf "Gruppen-Berechnung" haben kann. {{% notice info %}}<p>Du kannst folglich auch Versandgruppierungen gruppieren und so beliebig komplexe und mächtige Versandarten konfigurieren.</p>{{% /notice %}}</td>
		</tr>
	</tbody>
</table>

## Preis-Grenzwert und Steuerklassen-Anwendbarkeit

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
			<td>Gruppen-Berechnung</td>
			<td>Preis der ersten verfügbaren Methode</td>
			<td>Hier kannst du den Preis-Berechnungsmethode bestimmen.<br><br>
				<ul>
				<li><strong>Preis der ersten verfügbaren Methode</strong><br>
				Bei dieser Methode geht Isotope eCommerce die gewählten Versandarten gemäss der Sortierung durch und nimmt den Preis der ersten verfügbaren Versandart.</li>
				<li><strong>Niedrigster Preis der verfügbaren Versandarten</strong><br>
				Bei dieser Methode ermittelt Isotope eCommerce die günstigste aller zutreffenden gewählten Versandarten.</li>
				<li><strong>Höchster Preis der verfügbaren Versandarten</strong><br>
				Bei dieser Methode ermittelt Isotope eCommerce die teuerste aller zutreffenden gewählten Versandarten.</li>
				<li><strong>Summierter Preis der verfügbaren Versandarten</strong><br>
				Bei dieser Methode ermittelt Isotope eCommerce die Summe aller zutreffenden gewählten Versandarten.</li>
				</ul>
			</td>
		</tr>
	</tbody>
</table>


## Beispiele

{{% notice info %}}<p>Hast du ein Beispiel für eine Kombination aus Versandarten, welche immer mal wieder gebraucht wird? Das wäre hier sehr passend!</p>{{% /notice %}}
