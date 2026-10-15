# Steuerklassen konfigurieren

Eine Steuerklasse beschreibt die steuerliche Behandlung eines Preises. Weise sie Produktpreisen und gegebenenfalls Versand- oder Zahlungsgebühren zu. Lies zuerst [Preise und Steuern verstehen](../../concepts/prices-and-taxes.md), wenn die Begriffe neu sind.

## Zuerst Steuersätze erstellen

Eine Klasse verweist auf bestehende [Steuersätze](tax-rates.md). Erstelle Sätze und Regeln vor der Klasse.

Stelle dir für die folgenden Beispiele einen fiktiven Inlandssatz von 10 % und einen fiktiven Zielsatz von 20 % vor. Dies sind Lernwerte.

## Klasse für Nettokatalogpreise

Wenn du einen Produktpreis von 20,00 vor Steuer eingibst:

1. Erstelle eine Klasse „Standardwaren, netto eingegeben“.
2. Lass **Im Produktpreis enthaltener Steuersatz** leer.
3. Wähle den anwendbaren Satz unter **Steuersätze anwenden**.
4. Weise diese Klasse dem Produktpreis zu.

Trifft nur der Satz von 10 % zu, ergeben sich 20,00 netto und 22,00 brutto.

## Klasse für Bruttokatalogpreise

Wenn du 22,00 einschließlich des Inlandssatzes von 10 % eingibst:

1. Verwende die Klasse „Standardwaren“ aus dem ersten Shopbeispiel.
2. Wähle den Satz von 10 % als **Im Produktpreis enthaltener Steuersatz**.
3. Ergänze einen anderen Zielsatz unter **Steuersätze anwenden** nur, wenn deine vorgesehenen Regeln dies erfordern.
4. Lass Inlands- und Zielregeln einander ausschließen, wenn nur ein Satz gelten soll.
5. Weise die Klasse dem Produktpreis zu.

Der enthaltene Satz wird aus dem eingegebenen Betrag herausgerechnet. Trifft seine Regel zu, wird er auch angewendet. **Wähle denselben Satz nicht nochmals in der Liste zusätzlicher Sätze.** Eine doppelte Auswahl kann die Steuer doppelt hinzufügen.

Trifft die Inlandsregel nicht mehr zu, wird die Inlandssteuer entfernt. Trifft stattdessen der Satz von 20 % zu, wird der Bruttopreis bei derselben Nettobasis von 20,00 zu 24,00.

## Bezeichnung für enthaltene Steuer

Die Klasse stellt eine Bezeichnung für den Fall bereit, dass enthaltene Steuer entfernt wird. Verwende für Kunden verständliche Formulierungen. Ist die Klassenbezeichnung leer, wird gegebenenfalls die Bezeichnung des Satzes verwendet.

## Standardwerte und Ausnahmen

Markiere eine Klasse nur als Standard, wenn sie die beabsichtigte übliche Auswahl ist. Prüfe die tatsächlich mit jedem Preis gespeicherte Steuerklasse, auch bei erweiterten Preisen und Varianten. Ein Standardwert erklärt oder korrigiert bestehende Daten nicht automatisch.

Verwende eine separate Klasse, wenn Produkte unterschiedlich besteuert werden. Verwende weder Produkttyp noch Kategoriename als Ersatz für eine Steuerklasse.

## Vor der Massenerfassung prüfen

Teste ein Produkt jeder Klasse, jede Ziellandregel sowie den anfänglichen Kontext beim Stöbern und den vollständigen Adresskontext. Prüfe Netto, Steuer und Brutto getrennt. Sobald das Ergebnis stimmt, verwende dieselbe Konfiguration einheitlich im Katalog.

Als Nächstes auf dem Einrichtungsweg: [Attribute und Optionen](../products/attributes.md). Die [durchgerechnete Steueranleitung](tax-example.md) ist eine optionale Übung zur zielabhängigen Besteuerung.
