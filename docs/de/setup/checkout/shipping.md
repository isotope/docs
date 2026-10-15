# Versandarten

Eine Versandart erklärt Kunden, wie sie ihre Waren erhalten und was die Auswahl kostet. Sie kann Standardlieferung, Expresslieferung oder Abholung darstellen.

Die Methode berechnet angebotene Kosten und Verfügbarkeit. Die Buchung eines Versanddienstleisters, Etikettendruck und der tatsächliche Paketversand sind separate Aufgaben, sofern keine installierte Integration sie übernimmt.

## Erste Versandart erstellen

1. Öffne **Konfiguration → Versandarten**.
2. Wähle für einfache feste Kosten einen pauschalen Versandtyp.
3. Gib einen internen Namen und eine klare Kundenbezeichnung ein.
4. Ergänze einen Hinweis zu den Liefererwartungen.
5. Wähle pauschale Berechnung und gib die Kosten ein.
6. Weise bei Bedarf die Steuerklasse zu.
7. Ergänze bei Bedarf eine Zielregel oder Produkteinschränkungen.
8. Aktiviere die Methode.
9. Wähle sie in der aktiven [Shopkonfiguration](../general/stores.md).
10. Füge ein physisches Produkt zum Warenkorb hinzu und prüfe die Kasse.

Beginne mit einer einzigen unkomplizierten Methode. Ergänze Alternativen, nachdem du die erste durchgehend geprüft hast.

## Berechnungstypen im Core

**Pauschaler Versand** beginnt mit dem konfigurierten Preis. Seine Modi können einmalig, pro Produktposition, pro Artikelmenge oder nach Gewicht berechnen.

Bei einem Warenkorb mit drei identischen blauen T-Shirts in Größe M und einem Trail-Hoodie ergeben beispielhafte Kosten von 5,50 im Pauschalmodus 5,50, für zwei Produktpositionen 11,00 oder für vier Artikel 22,00. Mit Standardwaren enthalten diese Beträge die fiktive Steuer von 10 %. Dies vergleicht alternative Berechnungsmodi. Die Anleitung zum ersten Shop verwendet den Pauschalmodus. Produkttypeinschränkungen und versandbefreite Artikel können die berücksichtigten Positionen verändern.

Der Gewichtsmodus verwendet die konfigurierte Gewichtsbasis. Die Kosten sind proportional zum Gewicht und können Gewichtsbruchteile abschneiden. Gehe nicht davon aus, dass auf das nächste Paket oder Kilogramm aufgerundet wird. Teste Bruchteile und Grenzen vor der Verwendung für einen Versandtarif.

**Produktpreisversand** verwendet Versandpreise, die bei Produkten gespeichert sind. Seine Modi wählen den höchsten oder niedrigsten Preis oder summieren Preise, entweder pro Produktposition oder mit der Menge multipliziert.

**Gruppierter Versand** kombiniert verfügbare untergeordnete Methoden mit dem ersten, niedrigsten, höchsten oder summierten Betrag. So lassen sich mehrere interne Berechnungen als eine Kundenauswahl darstellen. Teste die Gruppe, wenn eine untergeordnete Methode nicht mehr verfügbar ist.

## Verfügbarkeit und Preis sind getrennt

Eine Methode kann einen gültigen Preis haben und trotzdem nicht verfügbar sein. Prüfe:

- Aktivierung und Auswahl in der aktiven Shopkonfiguration.
- Die zugewiesene Regel, insbesondere die Lieferadresse.
- Produkttypbedingungen für den gesamten Warenkorb.
- Konfigurierte Mindest- und Höchstgewichte.
- Ob der Warenkorb überhaupt Versand benötigt.

Ein Test mit nur einem Produkt reicht nicht, wenn Warenkörbe Produkttypen mischen können.

## Abholung und Versandbefreiung

Ein reines Abholprodukt kann die Lieferadresse unterdrücken. Ein versandbefreites Produkt wie eine Dienstleistung benötigt keinen Paketversand. Dies sind Produkt- oder Typverhalten, nicht bloß Methodenbezeichnungen. Teste die tatsächlich angezeigten Felder für Abholung und gemischte Warenkörbe.

Wird nur bei Abholung bezahlt, beschränke die Zahlungsart auf die vorgesehene Versandregelung. Siehe [Zahlungsarten](payment.md).

## Sendungsverfolgung

Eine Tracking-URL kann `%s` an der Stelle der Sendungsnummer enthalten. Teste sie mit einer formal realistischen Beispielnummer und prüfe den erzeugten Link. Das Eintragen von Trackinginformationen in eine Bestellung bucht oder versendet selbst keine Sendung.
