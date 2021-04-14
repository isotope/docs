---
menuTitle: "PayOne"
title: "Zahlungsart PayOne"
description: "Die Shop-Konfiguration - Bestellablauf - Zahlungsarten - PayOne."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-zahlungsarten-payone/
weight: 175    
---


Diese Zahlungsmethode ermöglicht die Integration mit PayOne (https://www.payone.de/).

## Informationen zum PAYONE Merchant Interface (PMI)

* Isotope verwendet den Channel "Frontend", daher muss dieser (nennt sich "FinanceGate Frontend") angehakt sein.
* Isotope verschlüsselt mit md5, daher muss bei "Verfahren Hashwert-Prüfung" sinngemäss  "md5" ausgewählt sein.
* Bei "TransactionStatus URL" muss die postsale.php mit weiteren Parametern angegeben werden: `http(s)://(www.)domain.tld/system/modules/isotope/postsale.php?mod=pay&id=(ID des Isotope-Kassenmoduls)`

{{% notice warning %}}Stelle sicher, dass der Pfad zur "postsale.php" korrekt und von Aussen erreichbar ist (beliebter Fehler: .htaccess Schutz auf Entwicklungsumgebungen etc.).{{% /notice %}}


## Konfiguration des Zahlungsanbieters

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
			<td>Transaktions-Typ</td>
			<td>Autorisieren und Einnehmen</td>
			<td>Hier kannst du den Transaktions-Typ bestimmen.<br><br>
				<ul>
				<li><strong>Autorisieren und Einnehmen</strong><br>
				Transaktionen von diesem Typ werden für die Authorisierung gesendet. Die Transaktion wird automatisch zur Begleichung geleitet wenn die Transaktion erfolgreich war.</li>
				<li><strong>Nur Autorisieren</strong><br>
				Transaktionen dieses Typs werden übertragen, wenn der Händler die Kreditkarte auf die Menge der verkauften Waren prüfen lassen möchte. Wenn der Händler nicht genügend Waren im Lager hat oder die Bestellungen vor der Warenlieferung prüfen möchte, wird dieser Transaktiontyps übertragen.</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>Abwicklungsart</td>
			<td>-</td>
			<td>Für PAYONE ist es erforderlich, eine Abwicklungsart anzugeben. Hier kannst du z.B. "Kreditkarte" auswählen, womit diese Zahlungsmethode für die Abwicklung von Kreditkarten zuständig wird. Es ist insofern auch sinnvoll, der Zahlungsmethode einen entsprechenden Titel für den Kunden zu geben. Dupliziere die Zahlungsmethode einfach so oft du möchtst und wähle hier jeweils eine andere Abwicklungsart aus, um deinen Kunden weitere Möglichkeiten anzubieten.</td>
		</tr>
		<tr>
			<td>PAYONE Sub-Account ID (aid)</td>
			<td>-</td>
			<td>Die PAYONE Sub-Account ID ergibt sich aus dem PMI (Sub-Account muss dort angelegt werden, dadurch wird die ID automatisch generiert).</td>
		</tr>
		<tr>
			<td>PAYONE Portal ID</td>
			<td>-</td>
			<td>Die PAYONE Portal ID ergibt sich ebenfalls aus dem PMI.</td>
		</tr>
		<tr>
			<td>Sicherheitsschlüssel</td>
			<td>-</td>
			<td>Der Sicherheitsschlüssel ergibt sich ebenfalls aus dem PMI (nennt sich "Key").</td>
		</tr>
	</tbody>
</table>

## Freigabe

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
			<td>Testsystem verwenden</td>
			<td>-</td>
			<td></td>
		</tr>
        <tr>
            <td>Aktiviere das Logging</td>
            <td>-</td>
            <td>Schreiben Sie Transaktionsinformationen in die Systemprotokolldateien.</td>
        </tr>
	</tbody>
</table>
