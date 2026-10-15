# Produkttypen

Ein Produkttyp ist eine wiederverwendbare Bearbeitungs- und Darstellungskonfiguration für eine Produktfamilie. Er bestimmt die auszufüllenden Attribute, das Vorhandensein von Varianten, die Preiskonfiguration sowie Templates und Galerien.

Er ist **keine Kategorie**. Eine Kategorie steuert, wo ein Produkt gefunden wird. Ein Typ steuert seine Modellierung. Das Trail-T-Shirt kann mit einem Typ „Bekleidung“ sowohl in T-Shirts als auch in Geschenke erscheinen.

## Wenige Typen planen

Beginne mit einem einfachen Typ für gewöhnliche physische Waren. Ergänze einen weiteren Typ, wenn Bearbeitungsbedarf oder Verhalten deutlich abweichen.

| Beispiel | Sinnvolle Typkonfiguration |
| --- | --- |
| Trail-T-Shirt, erster Shop | Bekleidung mit Name, Artikelnummer, Beschreibung, Preis und Bildern |
| Trail-T-Shirt und Trail-Hoodie, erweiterter Katalog | Bekleidung, erweitert um gemeinsame Beschreibungen und Größen-/Farbvarianten |
| Textilwaschmittel | Ein eigener Pflegeprodukttyp mit Packungsvolumen und Grundpreis |

Erstelle nicht für jedes Produkt einen neuen Typ. Gemeinsame Typen erleichtern einheitliche Bearbeitung.

## Typ erstellen

1. Öffne **Konfiguration → Produkttypen** und erstelle einen Datensatz.
2. Gib ihm einen Namen und eine Beschreibung, die anderen Redakteuren bei der Auswahl hilft.
3. Wähle die geeignete, in der Installation verfügbare Produktklasse.
4. Wähle die benötigten Attribute. Gruppiere verwandte Felder für ein verständliches Formular.
5. Nimm für gewöhnlich kaufbare Produkte ein Preisfeld auf.
6. Wähle, soweit angeboten, Listen- und Leser-Templates und Galerien.
7. Speichere und erstelle ein Beispielprodukt dieses Typs.

Fehlt ein Feld im Produktformular, prüfe zuerst den Typ, bevor du ein doppeltes Attribut anlegst.

## Erweiterte Preise

Aktiviere erweiterte Preise, wenn du mehrere bedingte Preissätze oder Mengenstaffeln benötigst. Ein Produkt mit einem einzigen Preis braucht diese zusätzliche Komplexität nicht. [Preise](../../usage/prices.md) erklärt das Verhalten des ersten passenden Preises.

## Varianten und Vererbung

Aktiviere Varianten für Produkte in Kombinationen wie Größe und Farbe. Wähle die Variantenoptionsattribute zur Identifikation jeder Kombination. Weitere Variantenattribute ermöglichen eigene Daten im Kindprodukt, etwa eine abweichende Artikelnummer oder einen Preis.

Nicht als Variantenattribute konfigurierte Felder werden vom Elternprodukt geerbt. Entscheide bewusst, welche Angaben zum Elternprodukt gehören und welche sich zwischen Varianten ändern. [Varianten einrichten](variants.md) enthält ein vollständiges Beispiel.

## Versandbehandlung

Der Typ kann normalen Versand, Versandbefreiung oder Abholung beschreiben. Eine versandbefreite Dienstleistung sollte keinen Paketversand erfordern. Abholung kann die Lieferadresse unterdrücken.

Versandbefreiung allein implementiert keine digitale Dateiauslieferung. Dafür benötigst du die passende Erweiterung und deren Zugriffsregeln. Teste immer einen gemischten Warenkorb, da bei einer Dienstleistung zusammen mit einem Versandartikel der physische Artikel weiter geliefert werden muss.

## Typen vorsichtig ändern

Eine Änderung eines gemeinsamen Typs beeinflusst Bearbeitung und Darstellung seiner Produkte. Ein neues Pflichtfeld kann bei bestehenden Produkten ohne sinnvollen Wert bleiben. Eine Verlagerung von Preisen auf Varianten kann Varianten ohne Preise hinterlassen. Prüfe nach Typänderungen vorhandene Katalogartikel erneut.
