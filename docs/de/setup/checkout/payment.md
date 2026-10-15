# Zahlungsarten

Eine Zahlungsart beschreibt, wie ein Kunde bezahlt. Eine Offline-Methode wie Zahlung bei Abholung erfordert den Geldabgleich durch Mitarbeiter. Eine Online-Methode übergibt einen Zahlungsversuch an einen Anbieter und erhält ein Ergebnis.

Eine Bestellung kann vor Zahlungsabschluss existieren. Konfiguriere [Zahlungsstatus](../general/order-status.md) und teste Fehler ebenso sorgfältig wie Erfolg.

## Mit Offline-Zahlung beginnen

Isotope enthält den Zahlungstyp Barzahlung (Cash). Du kannst ihn mit passender Bezeichnung und Anleitung für einen Offline-Ablauf verwenden.

1. Öffne **Konfiguration → Zahlungsarten**.
2. Wähle den Typ Barzahlung.
3. Gib Namen und Kundenbezeichnung ein, etwa „Zahlung bei Abholung“.
4. Ergänze einen Zahlungshinweis mit den nächsten Kundenschritten.
5. Wähle den Zahlungsstatus für den Verarbeitungsbeginn. Er sollte deinen tatsächlichen Offline-Ablauf abbilden.
6. Beschränke bei Bedarf Versandarten oder Produkttypen.
7. Ergänze Gebühr und Steuerklasse nur, wenn vorgesehen.
8. Aktiviere die Methode und wähle sie in der Shopkonfiguration.
9. Gib eine Testbestellung auf und prüfe gespeicherten Zahlungsstatus und Anweisungen.

Der Typ Barzahlung aktualisiert den konfigurierten Status und kehrt zum Shop zurück. Er prüft kein Bankkonto und zieht kein Geld ein. Mitarbeiter müssen den Eingang im tatsächlichen Zahlungsprozess bestätigen, bevor sie die Zahlung entsprechend markieren.

Verwende für Banküberweisung eine passende Kundenbezeichnung und nimm die benötigten Bankdaten in eine getestete Benachrichtigung auf. Die Bankfelder des Shops allein zeigen nicht überall Zahlungsanweisungen an.

## Online-Zahlungen

Verfügbare Anbieter hängen von Release und Erweiterungen ab. Lass deine Integrationsverantwortlichen Anbieterkonto, Testverbindung und Zahlungsstatuszuordnungen vor Live-Zahlungen vorbereiten. Für PayPal sollten sie auch die [versionsspezifischen Integrationshinweise](../../developers/version-notes.md) prüfen.

Sobald die Integration bereit ist, wähle sie in der Shopkonfiguration und führe die folgenden Tests gemeinsam mit der für Zahlungen verantwortlichen Person aus.

## Ergebnisse zuordnen

Ein Anbieter kann Verarbeitung, Erfolg oder Fehler melden. Ordne diese den passenden **Zahlungsstatus** zu. Der Gesamtstatus der Bestellung ist ein separater Workflow.

Eine Rückkehr zum Shop klärt die Zahlung nicht immer abschließend. Manche Anbieter melden das maßgebliche Ergebnis separat. Prüfe sowohl das gespeicherte Transaktionsergebnis als auch die vom Kunden gesehene Seite.

## Verfügbarkeit einschränken

Eine Zahlungsart kann durch eine Regel, erlaubte Versandarten und Produkttypbedingungen eingeschränkt sein. „Barzahlung bei Abholung“ sollte nicht bei einer normalen Paketbestellung erscheinen, sofern dies nicht beabsichtigt ist.

Prüfe auch Warenkörbe ohne Versandbedarf. Eine zu enge Versandartauswahl kann eine Zahlungsoption für Dienstleistungen entfernen.

## Vor dem Start testen

Teste Erfolg, Kundenabbruch, Fehler und eine unterbrochene Rückkehr zum Shop mit dem unterstützten Testverfahren des Anbieters. Prüfe Betrag, Währung, Bestellzuordnung und resultierenden Status. Stelle sicher, dass wiederholte Meldungen in deiner Integration keine doppelten Geschäftsaktionen auslösen.

Trenne Test- und Live-Zugangsdaten. Führe nach dem Wechsel in den Live-Modus das mit Anbieter und Shopbetreiber vereinbarte Abnahmeverfahren durch.
