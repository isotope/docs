# Produkte erstellen und pflegen

Ein Produktdatensatz enthält die Informationen, die Kunden für ihre Kaufentscheidung benötigen. Die verfügbaren Felder stammen aus seinem [Produkttyp](../setup/products/types.md).

## Bevor du beginnst

Halte geeigneten Produkttyp, Kategorieseite, Preis-/Steuerkonfiguration und Produktbilder bereit. Verwende für das Trail-T-Shirt Bekleidung, die Kategorie T-Shirts, den Preis 22,00 und Standardwaren. Die Ausgangswerte stehen in [Unser Beispielshop](../concepts/example-shop.md).

## Produkt erstellen

1. Öffne **Isotope eCommerce → Produkte** und erstelle ein Produkt.
2. Wähle seinen Produkttyp.
3. Gib einen klaren Namen und deine Artikelnummer ein.
4. Ergänze einen kurzen Teaser und eine hilfreiche vollständige Beschreibung.
5. Gib Preis und Steuerklasse ein oder konfiguriere erweiterte Preise, falls der Typ diese benötigt.
6. Weise eine oder mehrere Kategorieseiten zu.
7. Ergänze Bilder und speichere nach der Dateiauswahl.
8. Fülle die von deinen Methoden benötigten Versandinformationen aus.
9. Veröffentliche das Produkt und prüfe Start-/Enddaten.
10. Besuche Kategorie und Leser als Kunde und lege das Produkt in den Warenkorb.

Wenn du Varianten benötigst, folge [Varianten](variants.md), bevor du das Elternprodukt als fertigen verkaufbaren Artikel behandelst.

## Name, Artikelnummer, GTIN und Alias

Der Name ist für Menschen. Die Artikelnummer (SKU) ist deine interne Kennung und sollte Artikel unterscheiden, die Mitarbeiter getrennt kommissionieren oder abgleichen müssen. Eine GTIN ist eine standardisierte externe Handelskennung und kein Ersatz für dein internes Benennungskonzept.

Der Alias dient lesbaren Produkt-URLs und kann aus dem Namen erzeugt werden. Eine Änderung etablierter Aliase kann Lesezeichen und Suchergebnisse betreffen. Plane beim Ersetzen öffentlicher URLs Weiterleitungen über das Routing der Website.

## Für Käufer schreiben

Erkläre Lieferumfang, gegebenenfalls Maße oder Passform, Materialien, Kompatibilität und nötige Auswahlmöglichkeiten. Ein Teaser hilft auf der Listenseite. Die Beschreibung liefert ausreichend Informationen zur Entscheidung.

Nenne Grenzen klar. Ist ein fotografiertes Zubehör nicht enthalten, sage es. Erkläre bei personalisierten Produkten die benötigte Eingabe und die praktischen Einschränkungen.

## Kategorien und Sichtbarkeit

Kategorien sind Contao-Seiten. Ein Produkt kann auf mehreren erscheinen. Das Listenelement muss diese Zuweisungen über seinen Kategorieumfang lesen.

Die Veröffentlichung kann von der Veröffentlichungseinstellung und einem Zeitraum abhängen. Geschützte Produkte hängen zusätzlich von Mitgliedergruppen ab. Prüfe bei unterschiedlichem Zugriff abgemeldet und als vorgesehenes Mitglied.

## Erwartungen an die Lagerverwaltung

Artikelnummer und Versandgewicht bieten keine Bestandskontrolle. Reservierungen, Bestandsabzüge und Schutz vor Überverkäufen benötigen eine Lagererweiterung oder Warenwirtschaftsintegration. Prüfe diese separat, einschließlich gleichzeitiger Käufe und Stornierungen.

## Produkte pflegen

Teste nach Preis-, Typ-, Bild- oder Optionsänderungen den Leser und einen neuen Warenkorb. Nimm beim Ausmustern eines Produkts die Veröffentlichung zurück oder folge deinem Katalogverfahren, bevor du historische Referenzen löschst. Bestehende Bestellungen und erzeugte Dokumente müssen verständlich bleiben.

Verwende für Importe oder Massenänderungen eine kompatible Integration und übe auf einer Kopie. Direkte Datenbankänderungen können Validierung, Kategoriebeziehungen, Varianten und Indexierungsverhalten umgehen.
