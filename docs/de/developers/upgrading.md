# Auf Isotope 3 aktualisieren

Behandle ein Update auf eine neue Hauptversion als Migrationsprojekt. Seitenarchitektur, Templates, Integrationen und Datenstrukturen können sich ändern, selbst wenn der Shop für Kunden ähnlich aussieht.

## Bestehenden Shop erfassen

Erfasse die Versionen von Isotope, Contao, PHP und Erweiterungen. Liste eigene Templates, Hooks, Zahlungs-/Versandintegrationen, Produktattributtypen, Dokumente, Aktionen, Analysen und externe Lager-/Buchhaltungsverbindungen auf.

Sichere Datenbank und Dateien und teste die Wiederherstellung. Führe das Update auf einer separaten Kopie durch, bevor du Produktionsarbeiten planst.

## Im Quellcode genannte Änderungen

Die dokumentierten [Core-Updatehinweise](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md) umfassen:

| Frühere Einrichtung | Zu beachten bei Isotope 3 |
| --- | --- |
| Isotope-Frontend-Module | Als Inhaltselemente neu implementiert |
| Alte Templates | In Twig neu geschrieben |
| `@IsotopeHook`-Annotationen | Durch `#[AsIsotopeHook]` ersetzt |
| Alter PostSale-Einstiegspunkt | Entfernt, geeigneten Controller bzw. Integration verwenden |
| Automatischer Währungsumrechner | Entfernt |
| Alte Preisanzeige | Entfernt, aktuelles Netto-/Brutto-/Fest-Verhalten prüfen |
| ElevateZoom und Bildwasserzeichen | Entfernt |
| Eingebaute Google-Analytics-Integration | Entfernt |
| Favoriten | In eine Erweiterung ausgelagert |
| Wunschliste | Entfernt |
| Downloads-/FileTree-/Media-Attribute | In eine Erweiterung ausgelagert |
| Bereichs-/kumulative Filter und Variantenlistenfunktion | Entfernt |
| Eigene SQL-Produktlistenabfragen | Entfernt |

Die Hinweise entfernen auch alte spezielle Attributklassen für nun anders dargestellte Werte wie Preis, Grundpreis und Versandgewicht/-preis. Prüfe die aktuellen Produktfelder, statt veraltete Klassen nachzubauen.

Die Zahlungsintegrationshinweise widersprechen dem registrierten PayPal-Code dieses Checkouts. Lies [Versionshinweise](version-notes.md) und validiere das genaue Zielrelease.

## Migrationen üben

1. Installiere kompatible Abhängigkeitsversionen auf der Kopie.
2. Führe den Datenbankmigrationsablauf aus und prüfe die Ausgabe.
3. Prüfe Produkte, Kategoriezuweisungen, Varianten und Preise.
4. Prüfe historische Bestellungen und alle drei Statusverläufe.
5. Erstelle oder überarbeite Twig-Templates und Seitenelemente.
6. Konfiguriere oder ersetze nicht unterstützte Integrationen.
7. Schließe die [Starttests](../getting-started/launch.md) einschließlich Fehler- und Rückkehrpfaden ab.

Gehe nicht davon aus, dass automatische Datenmigrationen alten eigenen Code kompatibel machen. Prüfe resultierende Datensätze und Darstellung.

## Historische Bestellungen und Status

Isotope 3 trennt Bestell-, Zahlungs- und Lieferstatus. Prüfe zugeordnete historische Werte anhand bekannter Bestellungen, einschließlich bezahlter, unbezahlter, stornierter und versendeter Beispiele.

Die geprüfte Migration enthält ein in den Versionshinweisen dokumentiertes Problem bei der Lieferstatuszuweisung. Lass die technische Betreuung es prüfen und beheben, bevor du diese Revision auf historische Produktionsdaten anwendest.

## Produktivumstellung

Vereinbare, wann während des Deployments Bestellungen angenommen werden können und wie Anbieteraktivitäten um dieses Zeitfenster abgeglichen werden. Stelle getestete Versionen, Templates und Konfiguration bereit und führe dann die festgelegten Funktionstests aus.

Bewahre Zugriff auf die vorherige Sicherung und das genaue Migrations-/Deploymentprotokoll. Ein Rollback mit Datenbank muss neue Bestellungen und Zahlungen berücksichtigen, statt aktuelle Daten einfach durch eine ältere Kopie zu ersetzen.
