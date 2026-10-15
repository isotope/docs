# Einrichtungsplan

Die Konfiguration bestimmt die Auswahlmöglichkeiten für Produktredakteure und Kunden. Arbeite die Abhängigkeiten der Reihe nach ab, damit du bereits angelegte Datensätze auswählen kannst.

## Der Navigation von oben nach unten folgen

Die nummerierten Stufen der Seitennavigation folgen der untenstehenden Reihenfolge. Schließe die Stufen 1–6 für den grundlegenden Shop ab. Stufe 7 enthält optionale Funktionen, die du bei Bedarf ergänzt.

Für einen geführten ersten Kauf mit genauen Werten verwendest du [Dein erster Shop](../getting-started/first-shop.md). Dieser Plan erklärt dieselben Abhängigkeiten ausführlicher.

### 1. Shopgrundlage anlegen

Erstelle die [Shopkonfiguration](general/stores.md) und weise sie dem Startpunkt der Website zu. Wähle Währung, Preisanzeige und Adressländer. Lass Versand- und Zahlungsauswahl offen, bis du die Methoden in Stufe 5 angelegt hast.

### 2. Preise und Steuern konfigurieren

Lies [Preise und Steuern verstehen](../concepts/prices-and-taxes.md) und lerne dann, wie [Regeln](rules.md) die Anwendbarkeit einer Einstellung bestimmen. Erstelle benötigte Regeln vor den [Steuersätzen](checkout/tax-rates.md), die sie verwenden. Erstelle [Steuerklassen](checkout/tax-classes.md) nach den Sätzen.

Verwende für die erste Trail-T-Shirt-Bestellung den fiktiven Satz von 10 % und die Klasse Standardwaren aus der Anleitung. Dieses Beispiel mit einem Land benötigt keine Regel.

### 3. Katalog vorbereiten

Richte eigene [Attribute](products/attributes.md), dann [Galerien](general/galleries.md) und schließlich [Produkttypen](products/types.md) ein. Ein Produkttyp wählt bestehende Attribute und Galerien aus und kommt deshalb in dieser Stufe zuletzt.

Bereite für Trail Supply Bekleidungsbilder und den Typ Bekleidung vor. Lass Varianten und erweiterte Preise für den ersten Kauf deaktiviert.

### 4. Shopoberfläche aufbauen

Folge [Produkte anzeigen](frontend/products.md), um Kategorieseiten anzulegen und Produktlisten und Leser zu verbinden. [Erstelle dann das Trail-T-Shirt](../usage/products.md), weise es T-Shirts zu und prüfe als Besucher Beschreibung, Bild und den Preis 22,00. Die Produktbearbeitung steht unter Tägliche Arbeit, weil du diese Aufgabe nach dem Start wiederholst.

### 5. Kasse anbinden

Prüfe [Bestellstatus](general/order-status.md), bevor du [Versand](checkout/shipping.md) und [Zahlung](checkout/payment.md) einrichtest. Zahlungsarten benötigen die Status ihrer Ergebnisse und können von Versandmöglichkeiten abhängen.

Kehre zur [Shopkonfiguration](general/stores.md) zurück und wähle die erstellten Methoden aus. Eine gespeicherte Methode wird nicht automatisch angeboten.

Entscheide, wie [Mitglieder und Gäste](frontend/customers.md) einkaufen, und verbinde dann [Warenkorb und Kasse](frontend/checkout.md), einschließlich der Zielseite für Bestelldetails. Gib die erste Testbestellung auf und prüfe, ob sie unter Bestellungen erscheint.

### 6. Täglichen Betrieb vorbereiten

Konfiguriere [Benachrichtigungen](general/notifications.md) mit [Simple Tokens](general/simple-tokens.md) für bestellspezifische Angaben. Kehre zum Kasse-Element zurück, wähle die Bestellbestätigung und gib eine weitere Testbestellung auf, um Zustellung und Wortlaut zu prüfen.

Bereite benötigte [Dokumente](general/documents.md) vor und gib Mitarbeitern passende [Berechtigungen](general/access.md). Prüfe, ob sie die [Testbestellung bearbeiten](../usage/orders.md) können.

### 7. Shop bei Bedarf erweitern

Diese Funktionen sind optional. Wähle nach dem ersten funktionierenden Kauf die benötigten aus:

- [Varianten](products/variants.md) für auswählbare T-Shirt-Größen und -Farben.
- [Ähnliche Produkte](products/relations.md), um den Trail-Hoodie zu empfehlen.
- [Grundpreise](products/base-prices.md), um Flaschengrößen des Textilwaschmittels zu vergleichen.
- [Versandbeispiele](checkout/shipping-recipes.md) für weitere Liefermöglichkeiten.
- [Das durchgerechnete Steuerbeispiel](checkout/tax-example.md), um Ziellandregeln zu üben.
- [Internationale Shops](general/international.md) für weitere Sprachen, Währungen oder Märkte.

Ist eine dieser Funktionen für deinen Shop unverzichtbar, schließe sie vor dem Start ab und wiederhole die betroffenen Bestelltests.

## Bevor du Kunden empfängst

Schließe die [Checkliste zur Shoperöffnung](../getting-started/launch.md) ab. Verwende danach [Tägliche Arbeit](../usage/index.md) für Produktpflege und Bestellbearbeitung. Kehre zur Shopeinrichtung zurück, wenn das Geschäft eine Konfigurationsänderung erfordert.

## Konfiguration und tägliche Arbeit

Einen Produkttyp anzulegen ist Einrichtungsarbeit. Ein weiteres T-Shirt dieses Typs hinzuzufügen ist tägliche Arbeit. Festzulegen, welche Versandstatus aufeinander folgen dürfen, ist Einrichtung. Eine konkrete Bestellung als versendet zu markieren ist tägliche Arbeit.

Beschränke den Konfigurationszugriff auf Personen, die diese weiterreichenden Folgen verstehen. Eine Änderung an einer gemeinsamen Steuerklasse, einem Attribut oder einer Shopkonfiguration kann viele Produkte und künftige Warenkörbe betreffen.

## Namen und Bezeichnungen

Viele Datensätze haben einen Namen und eine Bezeichnung. Verwende für Mitarbeiter erkennbare Namen wie „Inlandspaket, Standardtarif“. Verwende für Kunden klare Bezeichnungen wie „Standardlieferung“. Vermeide interne Kennungen in den Auswahlmöglichkeiten für Kunden.

## Jeweils eine Änderung prüfen

Wähle einen angelegten Datensatz überall aus, wo er verwendet wird, und teste das zugehörige Frontendverhalten. Eine Methode kann existieren und dennoch fehlen, weil sie deaktiviert, in der aktiven Konfiguration nicht ausgewählt oder durch eine Regel ausgeschlossen ist.
