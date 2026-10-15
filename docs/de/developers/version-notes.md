# Versions- und Implementierungshinweise

Dieses Handbuch wurde gegen die Isotope-Core-Revision `96240eaa65c33a51e37951fe9833d9db1bd5980d` geprüft. Es dokumentiert den bereitgestellten Quellcode und kein unabhängig zertifiziertes Produktionsrelease.

Die folgenden Punkte unterscheiden bestätigte Implementierungsdetails von Annahmen älterer Texte. Sie sind besonders hilfreich, wenn Integrationsverantwortliche die dokumentierte Revision für einen echten Shop vorbereiten.

## Aktuelle Architektur

Shopfunktionen sind Inhaltselemente und Templates verwenden Twig. Preise und Anwendbarkeit nutzen das aktuelle Preis-/Regelmodell. Bestellungen haben separate Felder für Bestell-, Transaktions- und Lieferstatus.

Alte Bezeichnungen können noch „Modul“ verwenden oder auf entfernte Integrationen verweisen. Folge den tatsächlichen Felddefinitionen und registrierten Implementierungen.

## Widerspruch bei Zahlungsintegrationen

`UPGRADE.md` sagt, dass Drittanbieterzahlungsarten entfernt wurden. `CashPayment` und `PaypalPayment` tragen jedoch beide Registrierungsattribute und `CorePaymentFactory` erzeugt beide. Die Zahlungs-DCA enthält auch eine PayPal-Palette.

Zusätzlich hat das PayPal-Kontofeld dieser Revision eine Eingabekonfiguration, aber keine SQL-Definition in dieser DCA. Das muss im resultierenden Schema einer vollständigen Anwendung geprüft werden, bevor funktionierende Konfigurationsspeicherung angenommen wird.

Das Handbuch beschreibt deshalb die registrierte Implementierung und verlangt releasespezifische Validierung, statt alle historischen Zahlungsschnittstellen als unterstützt oder sämtliche Anbietermethoden als fehlend zu erklären.

Quellen: [Updatehinweise](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md), [Zahlungsfactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CorePaymentFactory.php), [Zahlungs-DCA](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_payment.php).

## Umleitung bei Mitgliedspflicht

In `CheckoutController::enforceMemberLogin()` leitet der Modus mit Mitgliedspflicht bedingungslos zur konfigurierten Anmeldeseite um. Die Methode prüft nicht, ob der aktuelle Kunde bereits authentifiziert ist.

Dies ist ein Befund im Quellcode für Bestellungen mit Mitgliedspflicht und kein getesteter Fehlerbericht für jede veröffentlichte Isotope-3-Version. Prüfe und behebe ihn in der installierten Revision, bevor du diesen Ablauf aktivierst. Die Einführungsanleitung verwendet Gastbestellungen.

Quelle: [Kassencontroller](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/CheckoutController.php).

## Regionen in Adressregeln

Die geprüfte `CartAddressCondition` weist eine Adresse ab, wenn deren Unterregion im konfigurierten Unterregionsarray enthalten ist. Das weicht von der scheinbar einschließenden Bedeutung der Regionsauswahl ab.

Die reinen Länderbeispiele dieses Handbuchs vermeiden diese Mehrdeutigkeit. Prüfe und behebe regionsabhängige Regeln im Zielrelease, bevor du sie für Steuern oder Bestellverfügbarkeit verwendest.

Quelle: [Adressbedingung](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder/Condition/CartAddressCondition.php).

## Migration historischer Lieferstatus

In `OrderstatusMigration::migrateOrders()` aktualisiert der Zweig, der `delivery_status` erstellt, anschließend `transaction_status` auf `shipped`. Prüfe diese Zuweisung vor der Anwendung dieser Revision auf historische Bestellungen.

Dieses Handbuch ändert die Core-Migration nicht. Ein Produktionsupdate erfordert eine getestete Korrektur oder ein geprüftes Release, in dem das Problem behoben ist.

Quelle: [Statusmigration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Migration/OrderstatusMigration.php).

## Dokumente und Preisverhalten

- Standarddokumente enthalten HTML, unabhängig vom Suffix `.pdf` einer Vorschauroute.
- Der erste passende erweiterte Preiseintrag gewinnt.
- Unter berechtigten Mengenstaffeln wählt der Preisrechner den niedrigsten Betrag.
- Die feste Anzeige behält den anfänglichen Anzeigebetrag bei und rechnet anwendbare Steuer daraus heraus.
- Das Grundpreisfeld bleibt verfügbar, obwohl die alte spezielle Attributklasse entfernt wurde.

Dies ist in den entsprechenden Einrichtungskapiteln berücksichtigt. Es sind keine Gründe, entfernte Isotope-2-Komponenten nachzubauen.

## Umfang der Validierung

Links, Navigation, Beispiele und statischer Websitebuild des Handbuchs lassen sich im Dokumentationsrepository prüfen. Der vollständige Shopablauf benötigt eine konfigurierte Contao-Anwendung, Datenbank, Mailkonfiguration und Anbieterintegrationen. Die [Checkliste zur Shoperöffnung](../getting-started/launch.md) definiert diese Abnahmetests.
