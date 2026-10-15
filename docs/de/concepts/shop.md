# So funktioniert ein Shop

Ein Shop macht aus den Entscheidungen eines Kunden eine Bestellung, die du erfüllen kannst. Wenn du die beteiligten Objekte verstehst, lässt sich das Backend viel leichter bedienen.

## Vom Katalog zur Lieferung

1. Du erstellst ein **Produkt**, etwa das Trail-T-Shirt, mit Beschreibung und Preis.
2. Du weist es einer **Kategorie** wie T-Shirts zu, damit Kunden es finden.
3. Ein Kunde öffnet die Produktdetails und wählt gegebenenfalls Optionen.
4. Das Hinzufügen zum **Warenkorb** hält fest, was er derzeit kaufen möchte.
5. An der **Kasse** gibt der Kunde Adressen ein und wählt verfügbare Versand- und Zahlungsarten.
6. Der Kunde prüft die Summen und gibt eine **Bestellung** auf.
7. Je nach Methode wird die Zahlung versucht oder vereinbart.
8. Du prüfst die Zahlungssituation, bereitest die Ware vor und erfasst den Lieferfortschritt.

Ein Warenkorb ist vorläufig. Adressen, Mengen und gewählte Methoden können seine Summen ändern. Eine Bestellung ist ein erfasster Kaufwunsch. Deine bloße Existenz belegt keinen Zahlungseingang.

## Produkt, Variante und Option

Ein **Produkt** ist ein Artikel, den du beschreibst und anbietest. Eine **Variante** ist eine konkrete Ausführung, etwa ein blaues T-Shirt in Größe M. Varianten sind sinnvoll, wenn Kombinationen eine eigene Artikelnummer, einen eigenen Preis oder andere Daten haben.

Eine **kundendefinierte Option** erfasst eine Eingabe des Kunden, etwa einen aufgedruckten Namen. Sie erzeugt nicht automatisch einen separat verwalteten Katalogartikel.

Ein **Attribut** ist ein Feld mit Informationen. Farbe kann je nach Produktmodell ein beschreibendes Attribut, eine Variantenauswahl oder eine Option sein. Ein **Produkttyp** ist die wiederverwendbare Konfiguration, die Felder und Verhalten einer Produktfamilie festlegt.

## Produkte und Bestellpositionen

Eine Warenkorbposition kombiniert normalerweise ein ausgewähltes Produkt oder eine Variante, deren Konfiguration und eine Menge. Drei identische blaue T-Shirts in Größe M können als eine Position mit Menge 3 erscheinen. Ein anderer aufgedruckter Name kann eine separate Position erfordern, selbst beim selben zugrunde liegenden Produkt.

Deshalb können sich „Anzahl der Produkte“ und „Anzahl der Artikel“ unterscheiden. Regeln und Versandberechnungen können Positionen zählen oder Mengen summieren. Wähle das Maß, das deiner geschäftlichen Absicht entspricht.

## Preis, Steuer und zusätzliche Kosten

Der **Stückpreis** ist der Preis eines einzelnen Artikels. Zusammen mit der Menge ergibt er die Positionssumme. Versand und Zahlung können zusätzliche Kosten verursachen. Steuern beschreiben den Steueranteil der jeweiligen Beträge.

Ein **Nettopreis** schließt Steuer aus. Ein **Bruttopreis** enthält Steuer. Ein **Steuersatz** ist ein Prozentsatz mit Bedingungen. Eine **Steuerklasse** bündelt die steuerliche Behandlung, die du einem Preis zuweist. Lies [Preise und Steuern](prices-and-taxes.md), bevor du deinen Katalog erfasst.

Eine **Zwischensumme** muss nicht dem Endbetrag entsprechen. Zeige Kunden vor dem Bestellen immer den Endbetrag, die Währung und die gewählten Methoden.

## Drei Arten von Fortschritt

| Status | Welche Frage er beantwortet | Beispiel |
| --- | --- | --- |
| Bestellung | Was geschieht mit dem Kauf insgesamt? | In Bearbeitung |
| Zahlung | Was geschieht mit dem Geld? | Offen oder Bezahlt |
| Versand | Was geschieht mit der Lieferung? | Offen oder Versendet |

Eine Bestellung kann bezahlt, aber noch nicht versendet sein. Bei einer gelieferten Bestellung auf Rechnung kann die Zahlung noch ausstehen. Die Trennung hilft Mitarbeitern, Doppelversand zu vermeiden und Bestellbestätigungen nicht mit Zahlungsbelegen zu verwechseln.

Als Nächstes: [Unser Beispielshop](example-shop.md), dann [Isotope installieren](../getting-started/installation.md).
