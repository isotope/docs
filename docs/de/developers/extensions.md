# Isotope erweitern

Isotope registriert mehrere Verhaltensfamilien über PHP-Attribute und Factories. Folge der jeweiligen Core-Implementierung von der Registrierung über die Backendkonfiguration bis zum Laufzeitverhalten.

## Registrierte Typfamilien

| Attribut | Erweiterungsbereich |
| --- | --- |
| `AsPayment` | Zahlungsarten |
| `AsShipping` | Versandarten |
| `AsDocument` | Dokumentrenderer |
| `AsGallery` | Produktgalerien |
| `AsRuleCondition` | Regelbedingungen |
| `AsCheckoutStep` | Kassenschritte |
| `AsProductFactory` | Produktkonstruktion |
| `AsAttribute` | Produktattribute |
| `AsProductFilter` | Produktabfrage-/Filterverhalten |
| `AsProductAction` | Produktaktionen |
| `AsProductCollectionAction` | Warenkorb-/Bestell-Collection-Aktionen |
| `AsProductCollectionItemAction` | Aktionen auf Collection-Positionen |

Diese liegen in `Isotope\CoreBundle\DependencyInjection\Attribute`. Autokonfiguration und Compiler-Passes des Bundles verbinden sie mit den jeweiligen Registries. Prüfe vor der Implementierung Konstruktor und Schnittstelle jedes Typs, da sich die Verträge unterscheiden.

## Eine vollständige eigene Methode benötigt mehrere Teile

Plane für Zahlungs- oder Versandtypen Laufzeitimplementierung, Factory, Backendfelder/-palette, Übersetzungen, Konfigurationsspeicherung sowie Verfügbarkeit und Preisverhalten. Eine zusätzliche Bezeichnung in der Typauswahl reicht nicht.

Verwende die aktuelle Core-Factory als Beispiel. Prüfe vor Abhängigkeiten, ob eine Basisklasse intern ist, und binde und teste gegen unterstützte Isotope-Versionen.

## Aufgaben einer Zahlungsintegration

Eine Anbieterintegration muss Konfiguration, Zahlungsinitiierung, Erfolgs-/Fehler-/Rückkehrverarbeitung, maßgebliche Anbietermeldungen, Betrags-/Währungsabgleich und doppelte Zustellung behandeln. Sie muss Ergebnisse der richtigen Bestelltransaktion zuordnen.

Vertraue keinem Browser-Abfrageparameter als Zahlungsbestätigung. Verwende das verifizierte Anbieterergebnis und definiere Wiederholungs-, Stornierungs- und Erstattungsverhalten ausdrücklich.

## Dokumentrenderer

Ein Dokumenttyp erzeugt ein `OrderDocument` mit Nummer, Erstellungszeit, Dateiname, Inhaltstyp und Inhalt. Der Standardtyp ist HTML. Ein PDF-Renderer muss tatsächlichen PDF-Inhalt mit korrektem Medientyp zurückgeben und Schriften und Layout selbst behandeln.

Verwende bestehende Nummerierungs- und Speicherdienste über den vorgesehenen Workflow, damit erzeugte Datensätze der richtigen Bestellung zugeordnet bleiben.

## Hooks

Das PHP-Attribut `AsIsotopeHook` ersetzt die alte Annotationssyntax. Registriere nur einen Hook, der in der installierten Version tatsächlich ausgelöst wird, und implementiere dessen genauen Argument-/Rückgabevertrag.

Bevorzuge das zweckspezifische Event, wenn es das benötigte Verhalten bereitstellt. Übersetze einen alten Hooknamen nicht mechanisch in ein neues Serviceattribut in der Annahme, dass seine Auslösung weiter existiert.

## Integrationsabnahme

Teste normalen Ablauf, nicht verfügbare Konfiguration, ungültige Eingabe, Anbieterausfall, wiederholte Rückrufe und Wiederholungen. Teste gegebenenfalls gemischte Produkttypen, Mitglieder-/Gastkontext und Währungswechsel.

Halte integrationsspezifische Einrichtungsanweisungen bei der Erweiterung und verlinke sie aus den Betriebsunterlagen des Shops. Kennzeichne klar, welches Verhalten der Core und welches die Erweiterung liefert.

Quelle: [Registrierung im IsotopeBundle](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php).
