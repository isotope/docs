# Vor der Shoperöffnung

Ein Shop ist bereit, wenn Kunden die unterstützten Kaufabläufe abschließen und Mitarbeiter die daraus entstehenden Bestellungen bearbeiten können. Eine funktionierende Startseite ist erst der Anfang.

Der Shopbetreiber prüft Produkte, Preise, Kundennachrichten und tägliche Abläufe. Lass deine technische Betreuung gemeinsam mit dir Zahlungsanbindung, Zugriffsschutz, Sicherungen und technische Prüfungen kontrollieren. Kennzeichne nicht angebotene Funktionen als nicht zutreffend.

Halte bei jedem Abnahmetest Testperson, Datum, Ergebnis und Bestellreferenz fest. Verwende vor Live-Tests eine Kopie oder die unterstützte Testumgebung des Zahlungsanbieters.

## Katalog und Navigation

- [ ] Kategorien zeigen die vorgesehenen veröffentlichten Produkte.
- [ ] Leserlinks funktionieren aus jeder Kategorie, auch von Unterseiten.
- [ ] Namen, Beschreibungen, Bilder, Mengen und Lieferumfang sind korrekt.
- [ ] Jede angebotene Variante hat die richtige Artikelnummer, den richtigen Preis und das richtige Bild.
- [ ] Kundendefinierte Optionen werden validiert und in der Bestellung gespeichert.
- [ ] Fehlende Produkte und ungültige URLs liefern ein hilfreiches Ergebnis.
- [ ] Geschützte Produkte sind nur für die vorgesehenen Mitgliedergruppen sichtbar.

## Preise und Steuern

- [ ] Währung, Preisfaktor und der Modus Netto/Brutto/Fest sind bewusst gewählt.
- [ ] Enthaltene und zusätzliche Steuern ergeben manuell überprüfte Beträge.
- [ ] Preise mit Standardadresse und endgültiger Adresse verhalten sich wie erwartet.
- [ ] Jedes relevante Zielland und jede Steuerklasse ist getestet.
- [ ] Versand- und Zahlungsgebühren verwenden die vorgesehene steuerliche Behandlung.
- [ ] Staffelgrenzen und Rückfallpreise bei bedingten Preisen funktionieren.
- [ ] Rundungen stimmen in Warenkorb, Bestellung, Zahlung und Dokumenten überein.

## Bestellabläufe

| Testfall | Was zu prüfen ist |
| --- | --- |
| Neuer Gast | Adresseingabe und Bestellabschluss |
| Angemeldetes Mitglied | Anmeldung, Wiederverwendung von Adressen und vollständiger Bestellablauf |
| Abweichende Rechnungs- und Lieferadressen | Korrekter Liefer- und Steuerkontext |
| Warenkorb nur mit physischen Produkten | Versandmöglichkeiten und Kosten |
| Nur versandbefreite Produkte, falls angeboten | Keine unnötigen Paketanforderungen |
| Gemischter Warenkorb | Gültige Kombinationen aus Versand und Zahlung |
| Mengenänderung | Neu berechnete Preise und Verfügbarkeit |
| Leerer Warenkorb | Verständlicher Weg zurück zum Stöbern |

- [ ] Für jede unterstützte Kombination gibt es einen verfügbaren Versand- und Zahlungsweg.
- [ ] Nicht erlaubte Länder und Produktkombinationen werden angemessen abgewiesen.
- [ ] Pflichtformulare an der Kasse verhindern unvollständiges Absenden.
- [ ] Das Ziel nach Bestellabschluss zeigt die Bestellung und verarbeitet die Zahlung.

## Zahlungsergebnisse

- [ ] Bei Erfolg werden die richtige Bestellung, Betrag, Währung und Zahlungsstatus erfasst.
- [ ] Bei Fehlern und Abbruch gibt es verständliche Möglichkeiten zum Fortfahren.
- [ ] Eine unterbrochene Rückkehr vom Anbieter wird korrekt abgeglichen.
- [ ] Verzögerte oder wiederholte Anbietermeldungen werden sicher verarbeitet.
- [ ] Anweisungen zur Offline-Zahlung und der Abgleich durch Mitarbeiter sind klar.
- [ ] Live-Zugangsdaten und Endpunkteinstellungen sind für die geplante Freigabe geprüft.

## Kommunikation und Betrieb

- [ ] Die Bestellbestätigung behauptet nicht fälschlich einen Zahlungserfolg.
- [ ] Kunden- und Mitarbeiterbenachrichtigungen kommen mit ersetzten Tokens an.
- [ ] Jede unterstützte Benachrichtigungssprache ist geprüft.
- [ ] Dokumente haben den vorgesehenen Inhalt, das richtige Format, die richtige Nummerierung und Ablage.
- [ ] Mitarbeiter können Zahlung, Versand, Stornierung und Rücksendung bearbeiten.
- [ ] Sendungsverfolgungslinks führen zu den richtigen Informationen des Versanddienstleisters.
- [ ] Produktinformationen, Kassentexte und Geschäftsbedingungen wurden von den Verantwortlichen geprüft.

## Zugriff, Wiederherstellung und Wartung

- [ ] Ein anderer Kunde kann nicht auf Bestellungen oder das Adressbuch eines Mitglieds zugreifen.
- [ ] Private Bestellseiten und kundenspezifische Antworten werden nicht über Caches geteilt.
- [ ] Mitarbeiterkonten haben passende Berechtigungen.
- [ ] HTTPS, E-Mail-Versand und geplante Aufgaben funktionieren.
- [ ] Für Datenbank, Dateien und erzeugte Dokumente gibt es einen getesteten Wiederherstellungsprozess.
- [ ] Jemand ist für laufende Updates und Fehlerüberwachung verantwortlich.

Behebe Fehler, bevor du die betroffene Art von Bestellung annimmst. Deine technische Betreuung sollte die [versionsspezifischen Prüfungen](../developers/version-notes.md) in die technische Abnahme aufnehmen.
