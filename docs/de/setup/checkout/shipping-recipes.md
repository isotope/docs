# Versandbeispiele

Versandeinrichtung kombiniert Berechnung, Verfügbarkeitsregeln und Auswahl in der Shopkonfiguration. [Versandarten](shipping.md) erklärt die verfügbaren Typen.

## Eine Inlandspauschale

**Ziel:** Feste Paketkosten für ein Lieferland anbieten.

1. Erstelle eine aktive Lieferadressregel für das Land.
2. Erstelle eine pauschale Versandart Standardlieferung mit pauschaler Berechnung und Kosten von 5,50.
3. Weise Standardwaren und die Länderregel zu. So bleibt die fiktive Steuer von 10 % in den Kosten enthalten.
4. Aktiviere die Methode und wähle sie in der aktiven Shopkonfiguration.
5. Teste ein physisches Produkt mit passenden und nicht passenden Zielen.

Wähle auch erlaubte Lieferländer in der Shopkonfiguration. Die Adressländerliste und die Methodenregel haben unterschiedliche Zwecke.

## Standard und Express

Erstelle zwei Methoden mit unterschiedlichen Bezeichnungen, Hinweisen und Kosten. Wähle beide in der Shopkonfiguration. Beschreibe die Lieferleistung, statt interne Tarifnamen anzuzeigen.

Teste den Wechsel und prüfe den Endbetrag. Wenn eine Zahlungsart vom Versand abhängt, prüfe, ob ein Versandwechsel die gültigen Zahlungsmöglichkeiten aktualisiert.

Eine Bezeichnung wie Express erzeugt keine Versanddienstleisterintegration und garantiert keinen Liefertermin. Dein betrieblicher Ablauf muss die beworbene Leistung erbringen.

## Kostenloser Versand ab einem Schwellenwert

Eine Methode ohne Kosten kann kostenlosen Versand darstellen. Wenn eine Warenkorbgesamtbetragsregel die Berechtigung prüft, beachte, dass sie den berechneten Gesamtbetrag liest und keine ausdrücklich getrennte Warenzwischensumme.

Ein Schwellenwert kann mit der Versandgebühr selbst wechselwirken. Teste darunter, genau darauf und darüber. Ändere danach Mengen und Methoden. Prüfe, ob kostenpflichtige und kostenlose Methoden gleichzeitig sichtbar sind und ob das beabsichtigt ist.

Wenn dein Geschäft „kostenlose Lieferung ab einer Warenzwischensumme ohne Versand- und Zahlungsgebühren“ verlangt, lass genau diese Bedingung entwickeln und testen. Ersetze sie nicht stillschweigend durch den Warenkorbgesamtbetrag.

## Abholung

Konfiguriere das gewünschte Abholverhalten für die betreffenden Produkte oder Typen und eine klar bezeichnete Auswahl an der Kasse. Erkläre Ort und Ablauf der Abholung. Prüfe, ob die Lieferadresse wie vorgesehen unterdrückt wird.

Beschränke eine Offline-Zahlungsart „Zahlung bei Abholung“ auf die passenden Versandmöglichkeiten, wenn sie bei Paketen nicht erscheinen soll. Teste einen Warenkorb mit Abhol- und normalen Produkten, bevor du diese Kombination anbietest.

## Gewichtsabhängige Kosten

Gib genaue Produktgewichte mit Einheiten ein. Teste Gewichtsbasis und Mindest-/Höchstgrenzen der Methode. Die pauschale Berechnung pro Gewicht ist proportional und bildet nicht automatisch alle Rundungsstufen eines Versanddienstleisters ab.

Verwende für diskrete Tarifstufen eine Implementierung entsprechend der veröffentlichten Dienstleisterberechnung und prüfe Beispielpakete. Verpackungsgewicht und Produktgewicht fließen nicht unbedingt in jede Berechnung gleich ein.

Halte erwartete Ergebnisse repräsentativer Warenkörbe fest, damit du nach Tarifänderungen erneut testen kannst.
