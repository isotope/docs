# Entwicklerleitfaden

Die Kapitel für Shopbetreiber erklären das Verhalten, das deine Implementierung bewahren muss. Lies vor Änderungen an Preisen, Kasse oder Bestellbearbeitung das passende Einrichtungskapitel.

Dieser Abschnitt bezieht sich auf die dokumentierte Isotope-3-Quellcoderevision. Mehrere Klassen tragen `@internal`- oder `@experimental`-Annotationen. Prüfe diese Markierungen und die installierte Version, bevor du eine Klasse als stabilen Erweiterungsvertrag behandelst.

## Dem technischen Ablauf folgen

Die Seitennavigation folgt Vorbereitung, Implementierung und Prüfung. Installation und Update sind je nach vorhandenem Shop alternative Einstiege.

1. **Zielversion prüfen.** Lies [Versionshinweise](version-notes.md), bevor du Integrationen wählst oder Migrationen anwendest.
2. **Anwendung vorbereiten.** Folge für einen neuen Shop [Technische Installation](installation.md). Beginne bei einem bestehenden Shop mit [Updates](upgrading.md). Prüfe danach die [Bundle-Konfiguration](bundle-configuration.md).
3. **Anpassen und integrieren.** Beginne für Darstellung mit [Twig-Templates](templates.md), für bestehende Prozesse mit [Events](events.md) oder für neues Verhalten mit [Erweiterungen](extensions.md). Dies sind zur Änderung passende Alternativen und keine drei obligatorischen Implementierungsschritte.
4. **Prüfen und warten.** Teste die betroffenen Kundenabläufe, prüfe [Performance](performance.md) und verwende die [Quellcodeübersicht](source-map.md), um die Dokumentation mit der installierten Version abzugleichen.

Die technische Betreuung verantwortet auch vollständige Sicherungen und Wiederherstellungstests. Sichere vor einer Änderung Datenbank, hochgeladene Dateien, erzeugte Dokumente, Konfiguration, eigenen Code und die Lockdatei der Abhängigkeiten. Teste auf einer separaten Installation und plane die Wiederherstellung ohne Verlust neuer Bestellungen oder Zahlungen.

Regelmäßige Produkt- und Bestellarbeit gehört zu [Tägliche Arbeit](../usage/index.md).

## Architekturübersicht

| Bereich | Hauptverantwortung |
| --- | --- |
| `Controller/ContentElement` | Contao-Inhaltselemente für den Shop |
| `Product` | Produktdaten, Factories, Konfiguration, Rendering und Events |
| `ProductCollection` | Warenkörbe, Bestellungen, Positionen und Zahlungstransaktionsverarbeitung |
| `Store/Context` | Währungs-, Konfigurations-, Mitglieder-, Adress- und Warenkorbkontext |
| `Store/Price` und `Store/Tax` | Preisdefinitionen, Berechnungen und Formatierung |
| `Checkout` | Schritte sowie Versand- und Zahlungsarten |
| `RuleBuilder` | Wiederverwendbare kontextabhängige Bedingungen |
| `Document` und `Store/Document` | Rendering, Nummerierung und Dokumentablage |
| `contao/dca` | Backendfelder und Bearbeitungsformulare |
| `contao/templates` | Twig-Templates und Komponenten |

Eine DCA (Data Container Array) ist Contaos Definition einer Bearbeitungsoberfläche und ihrer Felder. Sie belegt, was Administratoren tatsächlich konfigurieren können. Übersetzte Hilfetexte können der Implementierung hinterherhinken. Prüfe deshalb beides.

## Erweiterungspunkt wählen

- Beginne für Darstellung mit [Twig-Templates](templates.md).
- Prüfe zum Beobachten oder Ergänzen bestehender Prozesse die [Events](events.md).
- Verwende für neue Methoden oder Verhaltensfamilien das passende registrierte Typ-/Factory-Muster aus [Erweiterungen](extensions.md).
- Verwende für globale Konfiguration die dokumentierten [Bundle-Einstellungen](bundle-configuration.md).

Belasse eigenen Code in der Anwendung oder einem dedizierten kompatiblen Bundle. Änderungen innerhalb installierter Abhängigkeiten erschweren reproduzierbare Updates.

## Testumfang

Verwende eine vollständige Contao-Anwendung für Integrations- und Browsertests. Das reine Core-Repository ist ein Bundle und kein konfigurierter Shop. Teste gegebenenfalls Gast-/Mitgliederkontext, mehrere Mengen, Adressänderungen, Wiederholungen und Fehler externer Anbieter.

Das Core-Repository enthält PHPStan, Rector, ECS, Abhängigkeitsanalyse, PHPUnit, ESLint-/stylelint-Konfiguration und Asset-Buildwerkzeuge. Seine CI verwendet gemeinsame Contao-Buildwerkzeuge und führt PHPUnit mit PHP 8.3–8.5 und Contao 5.7 aus. Folge den tatsächlichen Werkzeugen und Versionen des ausgecheckten Projekts, statt einen universellen Befehl anzunehmen.

Die [Quellcodeübersicht](source-map.md) nennt die Grundlagen dieses Handbuchs. Die [Implementierungshinweise](version-notes.md) beschreiben ungeklärtes Verhalten dieser Revision.
