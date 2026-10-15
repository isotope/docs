# Grundpreise und Bezugsmengen

Ein Grundpreis ist ein Vergleichspreis für eine Standardmenge. Er hilft Kunden, unterschiedlich große Packungen zu vergleichen.

Das Textilwaschmittel von Trail Supply mit 250 ml zu 6,60 hat beispielsweise einen Grundpreis von 2,64 pro 100 ml. Eine 500-ml-Flasche zu 11,00 hat einen Grundpreis von 2,20 pro 100 ml. Die größere Flasche hat trotz höherem Packungspreis den niedrigeren Preis pro Milliliter.

Dies unterscheidet sich von Nettopreis, Großhandelspreis und Mengenrabatt. Der Kunde kauft weiterhin die Packung zum Packungspreis.

## Die Berechnung

```text
Grundpreis = Produktstückpreis / Produktmenge × Bezugsmenge
6,60 / 250 × 100 = 2,64
```

Verwende für beide Mengen dieselbe Maßeinheit. Bei einer Bezugsmenge von 100 Millilitern muss eine 1,5-Liter-Flasche für diese Berechnung als 1500 Milliliter angegeben werden.

## Einrichtung

1. Erstelle unter **Konfiguration → Grundpreise** eine Definition.
2. Gib ihr einen erkennbaren Namen wie „Pro 100 Milliliter“.
3. Gib die Bezugsmenge `100` ein.
4. Verwende eine Bezeichnung wie `%s pro 100 ml`. An der Stelle `%s` erscheint der formatierte Grundpreis.
5. Aktiviere das Grundpreisfeld im Produkttyp. Wähle am Produkt die Bezugsdefinition und gib die Packungsmenge wie `250` ein.
6. Prüfe, ob das gewählte Produkttemplate den Grundpreis ausgibt.

Fehlt das Grundpreisfeld, prüfe die aktivierten Attribute des gewählten Produkttyps.

## Ein Beispiel prüfen

Verwende eine Packung mit einfacher Berechnung und vergleiche das angezeigte Ergebnis manuell. Teste eine zweite Packungsgröße, Varianten mit unterschiedlichen Mengen sowie Mitglieder- oder Mengenpreise. Ein Grundpreis sollte dem tatsächlich im jeweiligen Kontext verwendeten Stückpreis folgen.

Entscheide gemeinsam mit der für Produktinformationen verantwortlichen Person, welche Produkte Grundpreise benötigen. Dieses Kapitel erklärt den Mechanismus, keine landesspezifischen Anzeigevorschriften.
