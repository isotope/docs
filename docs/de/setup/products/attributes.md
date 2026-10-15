# Attribute und Produktoptionen

Ein Attribut ist ein Feld, das ein Produkt beschreibt oder eine Kundenauswahl erfasst. Beispiele sind Name, Material und Farbe. Die Attributkonfiguration bestimmt Bearbeitung, Validierung, Übersetzung und Filtermöglichkeiten eines Felds.

## Art der Information bestimmen

| Information | Modellieren als |
| --- | --- |
| „Aus Baumwolle“ | Ein redaktionell gepflegtes beschreibendes Attribut |
| „Blau, Größe M“ mit eigener Artikelnummer | Variantenoptionsattribute und eine Variante |
| „Bitte Sam aufdrucken“ | Eine kundendefinierte Textoption |

Eine Farbbezeichnung allein macht noch keine Produktvariante. Ein Textfeld allein verwaltet keinen eigenständigen Lagerartikel.

## Attribut erstellen

1. Öffne **Konfiguration → Attribute**.
2. Wähle einen klaren Anzeigenamen und einen stabilen, eindeutigen internen Namen.
3. Wähle den Feldtyp, etwa Text oder Auswahlfeld.
4. Lege Validierung und Pflichtangabe fest.
5. Wähle, ob das Feld mehrsprachig ist.
6. Konfiguriere bei Auswahlfeldern Quelle und Optionen.
7. Füge das Attribut dem passenden [Produkttyp](types.md) hinzu.
8. Bearbeite ein Testprodukt und prüfe Formular und Frontend.

Behandle den internen Namen als technische Kennung. Integrationen und Templates können davon abhängen. Lass Änderungen etablierter interner Namen von deiner technischen Betreuung planen.

## Auswahlwerte und Bezeichnungen

Eine Option hat einen gespeicherten Wert und eine lesbare Bezeichnung. Verwende stabile Werte wie `blue` und übersetze bei Bedarf die Bezeichnung. Eine Bezeichnungsänderung unterscheidet sich vom Ersetzen eines bereits in Produkten und Bestellungen verwendeten Werts.

Der Optionsmanager ist sinnvoll, wenn mehrere Produkte eine feste Auswahlliste teilen. Produktspezifische Optionen eignen sich bei unterschiedlichen gültigen Auswahlen je Produkt. Individuelle Datenbankquellen erfordern einen Entwickler. Verwende für neue gemeinsame Listen den Optionsmanager.

## Kundendefinierte Felder

Aktiviere **Vom Kunden definiert**, wenn der Käufer den Wert eingibt. Verwende eine sinnvolle Bezeichnung, einen hilfreichen Hinweis und realistische Validierung. Lege für einen aufgedruckten Namen eine Maximallänge fest, die in der Produktion tatsächlich umsetzbar ist.

Teste einen leeren Wert, den längsten akzeptierten Wert und einen abgelehnten Wert. Füge zwei Ausführungen mit unterschiedlichen Eingaben hinzu und prüfe, ob Warenkorb und Bestelldetails beide getrennt bewahren.

Gehe nicht davon aus, dass ein Feld automatisch den Preis ändert. Optionspreise müssen vom konfigurierten Attribut und der Preisverarbeitung der Installation unterstützt werden. Teste den Gesamtbetrag, statt aus dem vorhandenen Feld darauf zu schließen.

## Suche und Filter

Ein Attribut muss für Frontendsuche oder -filterung aktiviert sein, bevor du es im jeweiligen Filterelement anbietest. Konfiguriere auch dieses Element und verbinde es mit der Produktliste. Backendsuche und -filterung sind separate Einstellungen für Redakteure.

Ein beschreibender Wert benötigt Templateunterstützung, um an der gewünschten Stelle zu erscheinen. Die Aktivierung im Produkttyp stellt ein Feld in erster Linie dem Produktmodell und Bearbeitungsformular bereit.

## Bestehende Felder ändern

Änderungen oder Löschungen eines etablierten Attributs können bestehende Produkte und deren Anzeige betreffen. Lass erforderliche Datenbankupdates von deiner technischen Betreuung durchführen und kläre die Folgen für gespeicherte Werte. Prüfe nach der Änderung bestehende Produkte.
