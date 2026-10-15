# Regeln und Bedingungen

Eine Regel ist eine benannte, wiederverwendbare Prüfung der aktuellen Einkaufssituation. Preise, Steuern, Versand- und Zahlungsarten können darauf verweisen.

„Inlandslieferung“ kann beispielsweise das Lieferland prüfen. Eine Versandart kann anhand dieser Regel ihre Verfügbarkeit bestimmen. Die Regel selbst versendet nichts und setzt keinen Preis.

## Regel erstellen

1. Öffne **Isotope eCommerce → Regeln**.
2. Gib der Regel einen aussagekräftigen Namen.
3. Öffne ihre Bedingungen und ergänze die benötigten Prüfungen.
4. Wähle je Prüfung den Operator und trage die Werte ein.
5. Aktiviere die Regel.
6. Wähle sie beim Preis, Steuersatz oder der Methode, die sie verwenden soll.
7. Teste einen passenden und einen nicht passenden Fall.

Eine Regel wirkt erst auf einen Preis, Steuersatz oder eine Methode, wenn du sie dort zuweist.

## Wie Bedingungen zusammenwirken

Der dokumentierte Matcher verlangt, dass **jede Bedingung** einer Regel zutrifft. Verstehe mehrere Bedingungen als „und“. Eine Regel mit Lieferland- und Mitgliedergruppenbedingung erfordert beide.

Wenn eine Bedingung eine Liste und einen Operator wie „eines von“ unterstützt, steuert dieser die Werte innerhalb dieser Bedingung. Gehe nicht von einem beliebig verschachtelten „oder“-Regelbaukasten aus.

Eine aktive Regel ohne Bedingungen trifft zu. Eine deaktivierte oder fehlende Regel trifft nicht zu. Ungültige Bedingungen lassen die Prüfung scheitern. Das ist relevant, wenn du eine Regel deiner einzigen Zahlungsart deaktivierst.

## Bedingungsfamilien im Core

| Bedingung | Typische Verwendung |
| --- | --- |
| Shopkonfiguration | Ein Preis für eine Konfiguration |
| Währung | Eine auf eine Währung beschränkte Auswahl |
| Datum oder Zeit | Ein zeitlich geplantes Angebot |
| Kunde angemeldet | Eine Auswahl nur für Mitglieder |
| Mitgliedergruppen | Ein Geschäftskundenpreis |
| Warenkorbadresse | Einschränkungen nach Land, Region oder Postleitzahl |
| Warenkorbmenge | Summe der Artikelmengen |
| Warenkorbprodukte | Anzahl der Produktpositionen |
| Warenkorbgesamtbetrag | Eine Bedingung anhand des berechneten Warenkorbgesamtbetrags |

Die Bedingung für den Warenkorbgesamtbetrag heißt nicht „Warenzwischensumme“ und sollte nicht so behandelt werden. Versandkosten und Neuberechnungen können das Verhalten an Schwellenwerten beeinflussen. Teste beide Seiten einer Grenze und nach Methodenwechseln.

## Beispiel: Inlandsversand

Erstelle eine Adressbedingung für die Lieferadresse und dein gewünschtes Land. Weise sie einer pauschalen Versandart zu. Ein Kunde mit anderem Lieferland sollte diese Methode nicht sehen. Wenn du auch erlaubte Lieferländer in der Shopkonfiguration einschränkst, prüfe beide Ebenen.

## Regeln sind nicht automatisch Gutscheine

Regeln beschreiben Bedingungen. Sie erzeugen keine Gutscheincodes und verfolgen keine Einlösungen. Verwende bedingte [erweiterte Preise](../usage/prices.md) für unterstützte Preisänderungen. Gutscheincodes, Einlöselimits und die Kombination von Aktionen erfordern eine kompatible Implementierung.

## Priorität und Preisreihenfolge

Regelpriorität ersetzt nicht die Reihenfolge der Produktpreiseinträge. Isotope nimmt den **ersten passenden erweiterten Preiseintrag**. Stelle spezifische Einträge vor einen uneingeschränkten Rückfallpreis und teste das tatsächliche Ergebnis.
