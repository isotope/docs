# Preise und Steuern verstehen

Ein Preis ist mehr als eine Zahl. Du musst seine Währung kennen, wissen, ob er Steuer enthält und ob zusätzliche Kosten anfallen.

Alle folgenden Prozentsätze und Beträge sind fiktive Lernbeispiele. Sie erklären das Berechnungsmodell von Isotope und legen nicht die steuerliche Behandlung deines Geschäfts fest.

## Netto und brutto

**Netto** bedeutet vor Steuer. **Brutto** bedeutet einschließlich Steuer.

Für das Trail-T-Shirt zu 22,00 EUR mit einem fiktiven Satz von 10 %:

| Berechnung | Betrag |
| --- | ---: |
| Nettopreis | 20,00 |
| Steuer, 10 % von 20,00 | 2,00 |
| Bruttopreis | 22,00 |

Um die Steuer aus 22,00 herauszurechnen, teilst du durch 1,10. Ziehe nicht 10 % von 22,00 ab. Das würde 2,20 abziehen und einen falschen Nettopreis ergeben.

## Was ein Steuersatz ist

Ein **Steuersatz** speichert einen Prozentsatz und kann auf eine Regel verweisen, die seine Anwendbarkeit bestimmt. Sein Backendname hilft Mitarbeitern bei der Zuordnung. Seine Bezeichnung erklärt ihn Kunden.

Ein fiktiver Satz „Beispiel Standard 10 %“ könnte beispielsweise gelten, wenn die Lieferadresse im inländischen Liefergebiet liegt. Für ein anderes Ziel könnte ein anderer Satz gelten. Die passende Adresse und die Bedingungen ergeben sich aus der Steuerkonfiguration deines Geschäfts.

Steuersätze existieren getrennt von Produkten, damit du dieselbe Behandlung wiederverwenden kannst, ohne bei jedem Produkt Prozentsätze einzugeben.

## Was eine Steuerklasse ist

Eine **Steuerklasse** verbindet einen Produktpreis mit seiner steuerlichen Behandlung. Denkbar sind „Standardwaren“, „Ermäßigte Waren“ und eine separate Klasse für Versandkosten.

In Isotope kann eine Klasse Folgendes festlegen:

- Den Satz, der bereits in der eingegebenen Zahl **enthalten** ist.
- Weitere Sätze, die **angewendet** werden, wenn ihre Regeln zutreffen.

Die Klasse beantwortet „Wie soll dieser Preis interpretiert und besteuert werden?“. Der Satz beantwortet „Welcher Prozentsatz gilt unter diesen Bedingungen?“. Ein Produkttyp beantwortet eine ganz andere Frage zu Produktfeldern und Verhalten.

## Nettopreise eingeben

Angenommen, du gibst 20,00 ein und meinst einen Betrag ohne Steuer. Lass den enthaltenen Satz der Klasse leer und ergänze den fiktiven Satz von 10 % unter **Steuersätze anwenden**. Wenn er zutrifft, ergibt sich ein Bruttopreis von 22,00.

## Bruttopreise eingeben

Angenommen, du gibst 22,00 ein und meinst einen Betrag einschließlich des inländischen Satzes von 10 %. Wähle diesen Satz als **Im Produktpreis enthaltener Steuersatz** der Klasse.

Isotope rechnet die enthaltene Steuer heraus, um den Nettobetrag zu bestimmen. Wenn die Regel des enthaltenen Satzes zutrifft, wird dieser Satz auch angewendet. Wähle denselben Satz nicht nochmals als zusätzlich anzuwendenden Satz.

Trifft der enthaltene Satz nicht mehr zu, wird seine Steuer entfernt. Gilt dann ein anderer Satz von 20 %, werden aus denselben 20,00 netto 24,00 brutto. Eine Adressänderung kann daher den angezeigten Preis verändern.

## Die Anzeige ist eine separate Einstellung

Die Shopkonfiguration bietet die Preisanzeigen Netto, Brutto und Fest. Die obigen Beispiele verwenden Brutto. Diese Auswahl ändert nicht die Bedeutung eines einschließlich Steuer eingegebenen Katalogpreises. Die Steuerklasse muss die eingegebene Zahl weiterhin korrekt beschreiben.

Bevor der Kunde eine Adresse angibt, verwendet der Shop einen Standardadresskontext. Die Kasse kann genauere Angaben liefern. Teste sowohl Preise beim Stöbern als auch Kassensummen, insbesondere bei Regeln für Zielländer.

## Feste Preisanzeige

Die feste Preisanzeige behält den eingegebenen Kundenpreis bei und berechnet anwendbare Steuern als darin enthalten. Bei eingegebenen 22,00 ergibt ein fiktiver Satz von 10 % einen Nettobetrag von 20,00. Bei 20 % ergeben dieselben 22,00 ungefähr 18,33 netto. Dein Nettoerlös verändert sich, während der angezeigte Produktbetrag fest bleibt.

Verwende Fest nur, wenn das deiner Preispolitik entspricht. Der Modus unterscheidet sich von Brutto, das im obigen Zielbeispiel die Nettobasis beibehält. Währungsfaktoren und andere Preisregeln können den Ausgangsbetrag weiterhin beeinflussen.

## Versand, Gebühren und Rundung

Versand- und Zahlungsgebühren können eigene Steuerklassen haben. Die Produktsteuerkonfiguration legt nicht automatisch die Behandlung aller Gebühren fest.

Auch Rundung ist relevant. Die Rundung der Steuer je Position kann leicht von der Rundung der zusammengefassten Steuer am Ende abweichen. Isotope bietet horizontale und vertikale Berechnung. Die praktischen Auswirkungen erklärt [Steuersätze](../setup/checkout/tax-rates.md).

Als Nächstes: [Regeln](../setup/rules.md), dann [Steuersätze](../setup/checkout/tax-rates.md) und [Steuerklassen](../setup/checkout/tax-classes.md). Das [durchgerechnete Steuerbeispiel](../setup/checkout/tax-example.md) ist eine optionale Übung nach der Grundeinrichtung.
