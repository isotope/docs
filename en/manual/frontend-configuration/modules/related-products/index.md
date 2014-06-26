# Ähnliche Produkte

Das Modul `Ähnliche Produkte` gibt die ähnlichen Produkte des aktuell angezeigten Produkts aus.
Als Basis für dieses Modul werden die <docrobot_route name="related-categories">verknüpften Kategorien</docrobot_route> verwendet.

Nehmen wir an, du hast eine `verknüpfte Kategorie` namens `Zubehör` definiert.
In den Produkteinstellungen hast du für dein Produkt `Gitarre` für die `verknüpfte Kategorie` `Zubehör` die Produkte `Kapodaster` sowie `Stimmgabel` ausgewählt, so kann dieses Modul die beiden Produkte `Kapodaster` sowie `Stimmgabel` ausgeben, sofern du bei der Modul-Konfiguration die Kategorie `Zubehör` ausgewählt hast.

<docrobot_message type="info"><p>Da das Modul `Ähnliche Produkte` im Endeffekt auch nur eine <docrobot_route name="product-list">Produktliste</docrobot_route> darstellt, wird darauf verzichtet, hier noch einmal alle identischen Einstellungen zu dokumentieren.</docrobot_message>

## Modul-Konfiguration

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
			<td>Ähnliche Kategorien</td>
			<td>-</td>
			<td>Hier wählst du aus, welche <code>verknüpften Kategorien</code> für dieses Modul berücksichtigt werden sollen. Es bietet sich beispielsweise nicht an, die Kategorien <code>Zubehör</code> sowie <code>Kunden haben auch gekauft</code> in der selben Liste anzuzeigen. Vielleicht solltest du in diesem Fall zwei Module auf der Seite platzieren. Alles ist möglich.</td>
		</tr>
	</tbody>
</table>