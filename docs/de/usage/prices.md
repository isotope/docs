# Produktpreise und Mengenstaffeln

Beginne mit einem einfachen Preis, sofern das Produkt keine bedingten Preise benötigt. Entscheide vor der Betragseingabe, wie Steuer enthalten ist. Siehe [Preise und Steuern](../concepts/prices-and-taxes.md).

Die folgenden Beträge verwenden das [Trail-T-Shirt](../concepts/example-shop.md) mit Standardwaren und enthaltener fiktiver Steuer von 10 %.

## Einfacher Preis

Ein einfacher Preis kombiniert Betrag und Steuerklasse. Die aktive Shopkonfiguration liefert Währungskontext und Anzeigeverhalten.

Prüfe nach dem Speichern das angezeigte Ergebnis. Eingegebene 22,00 mit enthaltener Steuer unterscheiden sich von 22,00 vor Steuer, obwohl die Zahl im Formular gleich aussieht.

## Erweiterte Preise

Lass vor diesem Abschnitt die für [Produkttypen](../setup/products/types.md#erweiterte-preise) verantwortliche Person erweiterte Preise für Bekleidung aktivieren. Jeder Eintrag kann eine Steuerklasse, eine Regel und Staffelpreise enthalten.

Isotope verwendet den **ersten erweiterten Preiseintrag mit passender Regel**. Ein Eintrag ohne Regel trifft uneingeschränkt zu. Setze spezifische Einträge zuerst und einen uneingeschränkten Rückfallpreis zuletzt.

Zum Beispiel:

| Reihenfolge | Regel | Stückpreis ab Menge 1 |
| --- | --- | ---: |
| 1 | Mitglied gehört zu Geschäftskunden | 17,60 |
| 2 | Keine Regel | 22,00 |

Steht der uneingeschränkte Eintrag zuerst, verhindert er die Auswahl des Geschäftskundeneintrags. Die numerische Regelpriorität ersetzt bei Produktpreisen nicht die Eintragsreihenfolge.

## Mengenstaffeln

Gib für ein gewöhnlich kaufbares Produkt immer eine Staffel ab Menge 1 an. Ergänze dann Schwellen wie:

| Mindestmenge | Stückpreis |
| --- | ---: |
| 1 | 22,00 |
| 5 | 19,80 |
| 10 | 17,60 |

Dies sind Stückpreise für die qualifizierende Menge, keine separaten Versandgebühren oder progressiven Blöcke. In diesem Beispiel mit sinkenden Preisen verwendet Menge 5 einen Stückpreis von 19,80 und ergibt 99,00 einschließlich fiktiver 10 % Steuer, vor Versand.

Isotope wählt den **niedrigsten Betrag unter den berechtigten Staffeln**, statt blind den letzten Schwellenwert zu nehmen. Verwende keine steigenden Staffelpreise in der Erwartung, dass eine spätere Schwelle einen höheren Stückpreis erzwingt. Teste ungewöhnliche Preisgestaltung mit deiner Entwicklung.

Der Produkttyp kann die niedrigste Staffel in einen „Ab“-Preis einfließen lassen. Ein „Ab“-Betrag bedeutet nicht, dass Kunden ihn ab Menge 1 erhalten.

## Varianten und Preise

Ein Typ kann gemeinsame Elternpreise oder separate Variantenpreise verwenden. Sind eigene Preise aktiviert, fülle jede erforderliche Variante aus. Prüfe die Preisspanne des Elternprodukts und den genauen Preis nach Auswahl einer Variante.

## Shopkonfigurationen und Zeiträume

Verwende Regeln für Konfiguration, Mitgliedergruppe, Datum oder anderen unterstützten Kontext. Behalte einen Rückfallpreis für Kunden ohne passende Sondereinträge. Teste Beginn und Ende zeitlicher Angebote sowie die Zeitzone der Website.

Prüfe bei Währungen neben bedingten Preisen den Shoppreisfaktor. Ein unbeabsichtigter Faktor kann einen bereits umgerechneten Preis multiplizieren.

## Abnahmetests

Teste Menge 1, jeweils eine Menge unter jeder Schwelle, die Schwelle selbst und eine darüber. Wiederhole dies für passende und nicht passende Kundengruppen und relevante Varianten. Prüfe Warenkorb- und Bestellsummen ebenso wie Produktlistenpreise.
