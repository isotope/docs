# Mehrere Sprachen, Währungen und Märkte

Sprache, Währung, Lieferregion und Shopidentität hängen zusammen, sind aber unterschiedliche Entscheidungen. Ein englischsprachiger Kunde möchte nicht zwangsläufig in einer bestimmten Währung zahlen oder in ein bestimmtes Land liefern lassen.

## Mehrere Sprachen

Verwende die Startpunkte und Sprachstruktur von Contao. Konfiguriere den zugehörigen Shopkontext und übersetze Produktinformationen dort, wo Attribute mehrsprachige Werte unterstützen.

Plane Übersetzungen für Produktnamen und -beschreibungen, Attributoptionen, Kassenbezeichnungen und Hinweise, Benachrichtigungen und Dokumenttexte. Prüfe Alternativtexte und Fotos mit sprachabhängigem Inhalt.

Ein übersetztes Produkt sollte stabile technische Kennungen behalten, soweit dein Katalogmodell das erfordert. Erstelle nicht allein zur Übersetzung einer Bezeichnung ein unabhängiges zweites Produkt, sofern dies nicht bewusst Teil deines Katalogkonzepts ist.

## Gemeinsame Shop-ID

Zusammengehörige Startpunkte können dieselbe Shop-ID verwenden, um Shopkontext wie Mitgliederwarenkörbe und Adressen zu teilen. Eigenständige Shops sollten bewusst getrennt werden.

Teste Sprachwechsel mit bestehendem Warenkorb. Prüfe Warenkorb, Produktlinks, Adressen und Bestelldetailzugriff. Eine gemeinsame Shop-ID übersetzt nicht selbst Produktinhalte und synchronisiert keine getrennten Produktdatensätze.

## Mehrere Shopkonfigurationen

Erstelle für jedes gewünschte Währungs- oder Marktverhalten eine Konfiguration. Lege Währung, Anzeigeformat, Adressmöglichkeiten, Methoden und Preisfaktor fest. Weise der jeweiligen Seitenstruktur Standardwerte zu.

Das Element zur Konfigurationsauswahl kann Kunden zwischen ausgewählten Konfigurationen wählen lassen. Beim Wechsel berechnet es den Warenkorb neu. Ist nur eine Konfiguration ausgewählt, kann das Element diese ohne sichtbare Auswahl anwenden. Setze ein solches Element deshalb bewusst ein.

## Preisumrechnung und ausdrückliche Preise

Ein Preisfaktor multipliziert Beträge. Er ist kein Live-Wechselkursdienst. Ausdrückliche erweiterte Preise mit einer Konfigurationsregel ermöglichen stabile Geschäftspreise je Konfiguration.

Wähle einen klaren Ansatz und teste das Ergebnis. Wenn du einen umgerechneten Preis eingibst und zusätzlich einen Umrechnungsfaktor anwendest, rechnest du möglicherweise doppelt um. Prüfe feste Gebühren, Versand, Preisspannen und Mengenstaffeln ebenso wie einfache Produktpreise.

## Steuern und Adressen

Verwende ausdrückliche Regeln für deine geprüfte steuerliche Behandlung. Standardländer beeinflussen den Kontext beim Stöbern, bevor die Kasse die tatsächliche Adresse liefert. Leite die Besteuerung nicht allein aus der Oberflächensprache ab.

Dieses Handbuch legt keine grenzüberschreitenden Steuerpflichten fest. Übertrage die freigegebenen Geschäftsregeln in Isotope-Bedingungen und teste eine Matrix aus Zielländern und Kundentypen.

## Testmatrix

Prüfe für jede unterstützte Sprach-/Konfigurationskombination Produktliste, Variantenauswahl, Warenkorb, Adresseingabe, Versand- und Zahlungsverfügbarkeit, Bestellbenachrichtigung und Dokument. Berücksichtige auch Wechsel bei bereits gefülltem Warenkorb.

Verwandte Themen: [Shopkonfigurationen](stores.md), [Steuerbeispiel](../checkout/tax-example.md).
