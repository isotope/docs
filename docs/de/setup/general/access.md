# Mitarbeiterzugriff und Verantwortlichkeiten

Mitarbeiter arbeiten mit Contao-Backend-Benutzerkonten. Kunden verwenden Frontend-Mitgliedskonten. Halte beide getrennt.

In einem kleinen Shop erledigt möglicherweise ein Administrator alles. Verteile den Zugriff nach Aufgaben, wenn weitere Personen hinzukommen.

## Vorgeschlagene Verantwortlichkeiten

| Rolle | Typische Arbeit |
| --- | --- |
| Katalogredakteur | Produkte, Bilder, Beschreibungen, Kategorien und freigegebene Preise |
| Bestellbearbeiter | Bestellungen prüfen, Zahlungsinformationen abgleichen, Lieferung vorbereiten, Status aktualisieren |
| Shopadministrator | Produkttypen, Steuern, Bestellmethoden, Shopkonfigurationen und Mitarbeiterzugriff |
| Entwickler/technische Betreuung | Softwareupdates, Templates, Integrationen, Hosting und technische Diagnose |

Dies sind Vorschläge für Verantwortlichkeiten und keine automatisch angelegten Rollenvorlagen.

## Berechtigungen konfigurieren und testen

Vergib mit Contao-Benutzern und Benutzergruppen die benötigten Backendmodule sowie Feld- und Datensatzberechtigungen. Isotope enthält Berechtigungssteuerungen für Shopkonfigurationsdatensätze und Produkt- und Bestellarbeit.

Teste mit einem echten Konto jeder Gruppe. Ein erfolgreicher Administratortest belegt nicht, dass ein anderer Benutzer einen Preis bearbeiten, eine Bestellung ansehen oder ein Dokument erzeugen kann.

Fehlt jemandem ein Backendbereich, prüfe den Modulzugriff. Ist der Bereich sichtbar, aber ein Datensatz oder Feld lässt sich nicht öffnen, prüfe auch die jeweiligen Datensatz- und Feldberechtigungen.

## Gemeinsame Konfiguration schützen

Steuerklassen, Produkttypen, Zahlungszuordnungen und Workflowübergänge wirken sich auf den ganzen Shop aus. Gib regulären Redakteuren Zugriff auf benötigte Datensätze, ohne jedes Konto zum Administrator zu machen.

Ermittle vor Änderungen gemeinsamer Konfiguration die betroffenen Produkte und Bestellabläufe. Ändere zunächst eine Testkopie und prüfe repräsentative Fälle.

## Kundendaten

Bestellungen enthalten Adressen, Kontaktdaten und gelegentlich kundendefinierte Texte. Verwende in Vorführungen und Screenshots Testdaten. Begrenze den Zugriff auf Bestellexporte, gespeicherte Dokumente und Sicherungen auf die Personen und Systeme, die ihn benötigen.

Für tägliche Abläufe fahre mit [Bestellungen bearbeiten](../../usage/orders.md) und [Wartung](../../usage/maintenance.md) fort.
