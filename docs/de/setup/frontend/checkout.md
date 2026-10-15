# Warenkorb- und Kassenseiten

Die Kasse verbindet die Produktauswahl mit einer erfassten Bestellung und Zahlungsabwicklung. Sie benötigt funktionierende Zielseiten, nicht nur ein Kasse-Element auf einer ansonsten leeren Website.

## Seitenkette erstellen

| Seite | Inhaltselement | Wichtigste Verbindung |
| --- | --- | --- |
| Kategorie-/Produktseite | Produktliste und Leser | Verhalten beim Hinzufügen zum Warenkorb |
| Warenkorb | Warenkorb | Kassenziel |
| Kasse | Kasse | Ziel nach Bestellabschluss |
| Bestelldetails | Bestelldetails | Zeigt die gewählte Bestellung und verarbeitet die Zahlung |

Erstelle und veröffentliche Seiten und Artikel, bevor du sie als Ziele wählst. Halte Bestelldetails aus der normalen Navigation heraus, wenn die Seite nur mit Bestellkennung sinnvoll ist.

## Warenkorb konfigurieren

Platziere das Warenkorb-Element auf der Warenkorbseite. Wähle das Kassenziel und prüfe die Aktualisierungs- und Entfernenfunktionen des Warenkorbtemplates. Entscheide mit der betreffenden Weiterleitungseinstellung, ob Kunden nach dem Hinzufügen auf der Produktseite bleiben oder zum Warenkorb gelangen.

Teste Mengenänderungen und Entfernen. Kunden sollten ihre Auswahl vor dem Bestellen korrigieren können. Zeige bei leerem Warenkorb einen hilfreichen Hinweis und einen Weg zurück zum Stöbern.

## Kasse konfigurieren

1. Füge der Kassenseite ein Kasse-Element hinzu.
2. Wähle Gast, Mitglied oder beides als Bestellmethode.
3. Konfiguriere für Mitgliederbestellungen Anmeldeziel und Kontobereich.
4. Wähle das Ziel nach Bestellabschluss mit dem Element **Bestelldetails**.
5. Wähle konfigurierte Bestellbenachrichtigungen.
6. Beginne mit sichtbaren Adress-, Versand- und Zahlungsschritten.
7. Ergänze bei Bedarf erforderliche Formulare für Bestellbedingungen.

Das Ziel nach Bestellabschluss gehört zur Zahlungsabwicklung. Isotope öffnet dort die Bestellung und startet den Zahlungsablauf. Eine reine „Vielen Dank“-Textseite ersetzt das Bestelldetails-Element nicht.

## Was Kunden ausfüllen

Isotope stellt Adress-, Versand- und Zahlungsschritte sowie die Bestellübersicht bereit. Manche Schritte entfallen bei bestimmten Warenkörben, etwa der Versand bei einer versandbefreiten Dienstleistung.

Der Kunde muss die relevanten Schritte vor der Bestellung abschließen. Die Übersicht ist seine letzte Gelegenheit, Produkte, Mengen, Adressen, Gebühren und Gesamtbetrag zu prüfen.

Kassenbenachrichtigungen werden nach dem Anlegen der Bestellung versendet. Sie sollten die Bestellung bestätigen und keinen Zahlungserfolg behaupten, sofern nicht ein separates geprüftes Zahlungsereignis diese Nachricht liefert.

## Schritte erst nach Tests überspringen

Optionen können die Adresse eines angemeldeten Mitglieds verwenden, die Rechnungsadresse immer als Lieferadresse übernehmen oder bei nur einer Methode die Auswahl überspringen. Das spart Aufwand, nimmt aber auch Korrekturmöglichkeiten.

Teste vor der Aktivierung alle relevanten Kundentypen. Ein Geschäftskunde, der ein Geschenk bestellt, benötigt möglicherweise eine andere Lieferadresse.

## Formulare für Bestellbedingungen

Erstelle das passende Formular in Contao und wähle es in den Bestellbedingungseinstellungen der Kasse. Wähle Schritt und Position. Produkttypbedingungen können das Erscheinen einschränken.

Verwende Pflichtvalidierung, wenn die Antwort tatsächlich erforderlich ist. Prüfe, ob das Formular bei unvollständiger Eingabe blockiert und die Werte den benötigten Bestell-/Benachrichtigungskontext erreichen. Formularfelder können zu `form_*`-Benachrichtigungstokens werden.

## Alle Ziele prüfen

Gib eine Gastbestellung auf, öffne deren Details und prüfe das Zahlungsverhalten. Wiederhole dies gegebenenfalls als Mitglied. Teste eine fehlende Kennung, eine fremde Mitgliederbestellung und einen leeren Warenkorb. Die [Checkliste zur Shoperöffnung](../../getting-started/launch.md) erweitert diese Tests.
