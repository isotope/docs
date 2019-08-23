# Steuerklassen

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
			<td>Lege für die Steuerklasse einen Namen an, der beschreibt wofür sie eingesetzt wird.</td>
		</tr>
		<tr>
			<td>Standard</td>
			<td>-</td>
			<td>Klicke hier, wenn es sich um die Standard-Steuerklasse handelt.</td>
		</tr>
	</tbody>
</table>

## Steuersätze

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
			<td>Steuerklasse im Produktpreis enthalten</td>
			<td>-</td>
			<td>Wähle ob Produktpreise mit dieser Steuerklasse einen Steuersatz enthalten. Dieser Steuersatz wird vom Produktpreis abgezogen, wenn er nicht passt.</td>
		</tr>
		<tr>
			<td>Beschriftung einbinden</td>
			<td>-</td>
			<td>Eine Beschriftung für Bestellungen um abgezogene Steuern anzuzeigen (falls eingebundene Steuern nicht passen). Wenn dieses Feld leer ist, wird die Beschriftung des Standard-Steuersatzes angezeigt.</td>
		</tr>
		<tr>
			<td>Steuersätze hinzufügen</td>
			<td>-</td>
			<td>Diese Steuersätze zu Produkten mit diesen Steuerklassen hinzufügen.</td>
		</tr>
		<tr>
			<td>Rundungszuschlag verwenden</td>
			<td>-</td>
			<td>Rundungszuschlag der Shop-Konfiguration verwenden.</td>
		</tr>
		<tr>
			<td>Nicht negativ</td>
			<td>-</td>
			<td>Verhindert negative Beträge für diese Steuer (negative Zahl wird auf 0.00 aufgerundet).</td>
		</tr>
	</tbody>
</table>

## Beispiel 1:

Für den Verkauf an Endverbraucher in Deutschland wird der Bruttopreis angezeigt und die enthaltene Mehrwertsteuer lediglich ausgewiesen.

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-classes/steuerklasse_inklusive_mwst.png" alt="Endverbraucher">


## Beispiel 2:

Für den Verkauf an Gewerbekunden in Deutschland wird der Nettopreis angezeigt und die normale Mehrwertsteuer addiert.

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-classes/steuerklasse_exklusive_mwst.png" alt="Gewerbekunden">