# Durchgerechnetes Beispiel: Inlands- und Zielsteuern

Diese Übung zeigt, warum Steuerklassen und Steuersätze getrennt sind. Sie verwendet fiktive Sätze und zwei Ziele namens A und B. Ersetze sie in den Adressregeln durch deine gewählten Testländer. Übernimm diese Prozentsätze nicht in eine echte Steuerpolitik.

Arbeite mit dem T-Shirt von Trail Supply aus [Dein erster Shop](../../getting-started/first-shop.md) weiter. Verwende eine Testkopie, da eine gemeinsame Steuerklasse alle damit verbundenen Preise beeinflusst.

**Ergebnis:** Das zu 22,00 einschließlich 10 % Steuer eingegebene T-Shirt hat eine Nettobasis von 20,00. Sein Bruttobetrag wird 24,00, wenn eine andere Zielsteuer von 20 % gilt.

## 1. Bruttoanzeige verwenden

Wähle **Brutto** in der Shopkonfiguration und belasse den Währungsfaktor auf `1`. Die feste Preisanzeige verhält sich anders und wird hier nicht verwendet.

Erlaube beide Testziele und setze A als Standardlieferland. Verwende ein physisches Produkt, damit du eine Lieferadresse eingeben kannst.

## 2. Zwei Regeln erstellen

Erstelle und aktiviere eine Regel für Lieferland A und eine für Lieferland B. Jede verwendet eine Warenkorbadressbedingung zur Prüfung der Lieferadresse.

Diese Regeln müssen sich für die Übung gegenseitig ausschließen. Teste zunächst nur das Land, ohne Regions- oder Postleitzahleinschränkungen.

## 3. Steuersätze vorbereiten

| Satzname | Prozentsatz | Regel |
| --- | ---: | --- |
| Beispiel Standard 10 % | 10 | Lieferland A |
| Beispiel Ziel 20 % | 20 | Lieferland B |

Bearbeite den bestehenden Satz Beispiel Standard 10 % und weise die Regel für A zu. Erstelle Beispiel Ziel 20 % mit der Regel für B. Gib beiden eine kundenverständliche Bezeichnung und speichere.

## 4. Klasse aktualisieren

Bearbeite „Standardwaren“ auf deiner Testkopie. Setze den Satz von 10 % für A als enthaltenen Satz. Wähle unter **Steuersätze anwenden** nur den Satz von 20 % für B.

Wähle A nicht ein zweites Mal in der zusätzlichen Liste. Als enthaltener Satz wird er bereits angewendet, wenn seine Regel zutrifft.

## 5. Produktpreis zuweisen

Belasse den Trail-T-Shirt-Preis bei `22.00` und wähle Standardwaren. Verwende einen Artikel und entferne für die einfachste Berechnung andere Gebühren. Falls deine Versandart Kosten hinzufügt, vergleiche die Produktposition separat.

## 6. Erwartete Ergebnisse prüfen

| Kontext | Eingegebener Preis | Nettobasis | Anwendbare Steuer | Bruttoproduktpreis |
| --- | ---: | ---: | ---: | ---: |
| Adresse A | 22,00 | 20,00 | 2,00 | 22,00 |
| Adresse B | 22,00 | 20,00 | 4,00 | 24,00 |
| Keine Regel trifft zu | 22,00 | 20,00 | 0,00 | 20,00 |

Die letzte Zeile zeigt das Softwareverhalten, wenn kein Satz zutrifft. Sie empfiehlt keine Steuerbefreiung anderer Ziele.

Die Berechnung beginnt mit `22 / 1.10 = 20`. Danach wird der passende Satz auf 20 angewendet. Der im Produkt eingegebene Preis bleibt 22,00.

## 7. Vor und nach der Adresseingabe testen

Prüfe das Produkt vor der Adresseingabe und schließe den Bestellvorgang dann mit A ab. Wechsle zu B und betrachte die neu berechnete Produktposition. Prüfe, ob du die **Lieferadresse** geändert hast, denn diese prüfen die Regeln.

Wiederhole den Test mit Nettoanzeige, wenn du mit derselben Konfiguration den Nettobetrag von 20,00 sehen möchtest. Die Behandlung der enthaltenen Steuer bleibt durch die Klasse festgelegt.

## 8. Komplexität schrittweise ergänzen

Teste eine zweite Steuerklasse, besteuerten Versand, mehrere Mengen und Rundung erst, wenn das einfache Beispiel funktioniert. Führe für die echten Shopkonfigurationen eine kleine Tabelle erwarteter Ergebnisse und wiederhole sie nach Steuer- oder Preisänderungen.

Verwandte Themen: [Steuerklassen](tax-classes.md), [Steuersätze](tax-rates.md), [Preisanzeige](../../concepts/prices-and-taxes.md).
