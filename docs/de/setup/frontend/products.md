# Produkte anzeigen

Produkte sind Katalogdaten. Produkt-Inhaltselemente machen daraus Seiten, auf denen Kunden stöbern können.

Die wichtigsten Elemente sind die **Produktliste**, die mehrere Produkte zeigt, und der **Produktleser**, der ein Produkt im Detail zeigt. Erstelle sie in Contao im Artikel der jeweiligen Seite.

## Kategorieseite aufbauen

1. Erstelle und veröffentliche eine reguläre Seite wie T-Shirts in der Contao-Seitenstruktur.
2. Weise ein veröffentlichtes Produkt über dessen Kategorieauswahl dieser Seite zu.
3. Füge einem Artikel auf der Seite ein Produktlisten-Inhaltselement hinzu.
4. Wähle einen Kategorieumfang. Verwende im einfachsten Fall die aktuelle Kategorie.
5. Wähle Sortierung und Seitennavigation.
6. Wähle die gewünschten Schaltflächen und das Mengenverhalten.
7. Öffne die Seite als Besucher.

Ist die Liste leer, prüfe Seitenzuweisung, Veröffentlichungsdaten, Mitgliederschutz und Listenumfang des Produkts, bevor du Templates änderst.

## Listenumfang verstehen

„Aktuelle Kategorie“ liest Produkte dieser Seite. Ein Umfang mit erster Unterebene oder allen Unterseiten schließt diese Nachfahren ein. „Alle Kategorien“ erfasst Produkte innerhalb des Seitenbaums des aktiven Startpunkts und nicht jeden unabhängigen Shop der Installation.

Wähle den Umfang auf einer Shopstartseite bewusst. Eine Startseite ohne direkte Zuweisungen benötigt einen Umfang mit Unterseiten, wenn sie deren Produkte zeigen soll.

## Leseranordnung wählen

**Auf der aktuellen Seite:** Platziere Liste und Leser im Artikel. Aktiviere in der Liste **Im Lesermodus ausblenden**. Der Leser zeigt Details, sobald ein Produkt ausgewählt ist. Dies ist die einfachste Anfangskonfiguration.

**Auf einer separaten Seite:** Erstelle eine Seite mit Leser-Element und wähle sie in der Leserkonfiguration jeder Kategorieseite. Dies ermöglicht unterschiedliche Layouts und umgebende Inhalte. Die Leserseiteneinstellung wird **nicht** an Unterkategorien **vererbt**. Konfiguriere deshalb jede Kategorie, die sie benötigt.

**Deaktiviert:** Eine Kategorie kann Produktdetailseiten unterdrücken. Das eignet sich für einfache Käufe aus der Liste. Stelle dennoch ausreichend Informationen für die richtige Auswahl bereit.

## Sortierung, kanonische Links und Darstellung

Ein Produkt in mehreren Kategorien kann mehrere Navigationskontexte haben. Entscheide, welche Produkt-URL vorrangig sein soll, und teste gegebenenfalls die Option für den primären Link. Pflege sinnvolle Produktaliase und Metadaten.

Listen-/Leser-Templates und Galerien lassen sich über Produkttypen und Elementüberschreibungen wählen. Prüfe beide Ebenen, wenn eine Darstellungsänderung unwirksam erscheint.

Wenn deine Liste keine Optionen anzeigt, aktiviere **Produktoptionen deaktivieren**, um unnötige Options- und Variantendaten zu vermeiden. Verwende diese Optimierung nicht, wenn die Liste interaktive Auswahlmöglichkeiten braucht.

## Filter ergänzen

Markiere die betreffenden Attribute als im Frontend filter- oder durchsuchbar. Ergänze das Produktfilter-Element, wähle die angebotenen Felder und verbinde es über die konfigurierte Filterzuordnung bzw. den Schlüssel mit der gewünschten Liste. Teste anschließend eine Auswahl mit und eine ohne Ergebnisse.

Der Kategoriefilter dient der Seiten-/Kategorienavigation. Ein Produktattributfilter schränkt Produkte anhand von Werten wie Material oder Größe ein. Verdeutliche den Unterschied mit klaren Bezeichnungen.

## Abnahmeprüfung

Öffne von der Kategorieseite aus ein Produkt, wähle Optionen, lege es in den Warenkorb und prüfe dort den ausgewählten Artikel. Teste auch ein Produkt ohne Bild, ein geschütztes Produkt und eine nicht verfügbare URL.
