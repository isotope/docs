# Shopkonfigurationen

Eine Shopkonfiguration bündelt Einstellungen für das Verhalten einer Einkaufssitzung: Währung, Preisanzeige, Adressfelder, erlaubte Länder und verfügbare Bestellmethoden.

Verwende **Isotope eCommerce → Konfiguration → Shopkonfigurationen**. Erstelle für deinen ersten Shop eine Konfiguration mit erkennbarem Namen wie „Trail Supply Inland“.

## Identität und Adresse

Gib die geschäftlichen Kontaktdaten ein, die du in Shopnachrichten und Dokumenten verwenden möchtest. Bankdaten sind für Offline-Zahlungsanweisungen hilfreich. Das Ausfüllen dieser Felder sendet keinen Zahlungsauftrag an deine Bank.

Der Konfigurationsname hilft Mitarbeitern. Die Bezeichnung kann Kunden angezeigt werden, etwa in einer Konfigurationsauswahl.

## Adressmöglichkeiten

Die Rechnungsadresse identifiziert den Käufer für die Abrechnung. Die Lieferadresse bestimmt das Lieferziel. Beide können gleich sein, aber Kunden versenden gelegentlich Geschenke oder bestellen an eine Geschäftsadresse.

Wähle die benötigten Felder je Adresse und lege Pflichtfelder fest. Unnötige Pflichtangaben machen jedem Kunden zusätzliche Arbeit. Das Ausblenden benötigter Lieferinformationen erzeugt später manuelle Rückfragen.

Setze Standardländer für Rechnung und Lieferung. Wähle danach ausdrücklich die akzeptierten Länder. **Eine leere Auswahl erlaubter Länder bedeutet alle Länder**, nicht keine Länder. Standardländer sind Ausgangswerte und keine geografische Einschränkung.

Wenn du Mitgliedsländer beschränkst, können Contao-Mitgliederregistrierung und persönliche Daten auf die zusammengefassten Rechnungs- und Lieferländer beschränkt werden.

## Preisanzeige und Währung

Wähle Währung und Preisanzeige Netto, Brutto oder Fest. Fest behält den eingegebenen Anzeigepreis bei und behandelt anwendbare Steuern als enthalten. Dadurch kann der Nettoerlös mit der Steuer variieren. Stimme Anzeigeformat und Rundung auf Buchhaltung und Zahlungsintegration ab. Die Formatierung steuert das Aussehen eines Betrags. Die [Steuerklasse](../checkout/tax-classes.md) beschreibt die bereits im eingegebenen Preis enthaltene Steuer.

Der Preisfaktor bleibt normalerweise `1`. Er kann Preise für eine andere Konfiguration multiplizieren, ist aber kein automatischer Wechselkursdienst. Ausdrückliche Preise je Konfiguration lassen sich bei stabilen Verkaufspreisen oft leichter kontrollieren. Siehe [Mehrere Sprachen und Währungen](international.md).

## Bestellmethoden auswählen

Erstelle Datensätze für [Versand](../checkout/shipping.md) und [Zahlung](../checkout/payment.md), aktiviere sie und wähle sie dann in dieser Konfiguration aus. Eine Methode muss außerdem ihre Verfügbarkeitsbedingungen erfüllen.

Kehre nach dem Hinzufügen einer Methode hierher zurück. Diese zusätzliche Auswahl ist ein häufiger Grund dafür, dass eine neue Option an der Kasse nicht erscheint.

## Konfiguration mit der Website verbinden

Wähle die Shopkonfiguration in der Contao-Seitenstruktur für den betreffenden Websitebereich. Prüfe auch die **Shop-ID** im Startpunkt. Sie gruppiert zusammengehörige Startpunkte für gemeinsame Warenkörbe und Adressen. Sie unterscheidet sich von der Datenbank-ID des Konfigurationsdatensatzes.

Beginne mit einem Startpunkt und einer Konfiguration. Wenn du Startpunkte oder eine Konfigurationsauswahl ergänzt, teste denselben Warenkorb beim Wechsel. Ein Konfigurationswechsel kann den Warenkorb neu berechnen und anwendbare Preise und Bestellmöglichkeiten beeinflussen.

## Prüfen

Öffne eine neue Gastsitzung. Prüfe Währung, angezeigten Preis, Standardländer, erlaubte Adressländer und Versand- und Zahlungsmöglichkeiten. Wiederhole dies nach Eingabe eines tatsächlichen Testziels.
