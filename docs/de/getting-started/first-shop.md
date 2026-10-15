# Dein erster Shop: ein Trail-T-Shirt verkaufen

**Du benötigst:** [installiertes Isotope](installation.md), eine funktionierende Contao-Website mit Seitenlayout und Administratorzugriff. Verwende eine Testwebsite und eine E-Mail-Adresse, auf die du Zugriff hast.

**Das Ergebnis:** Ein Besucher kann ein Trail-T-Shirt kaufen und du findest die Bestellung im Backend. Du verwendest eine Währung, ein Lieferland und eine Offline-Zahlungsart zum Testen.

Die folgenden Werte stammen aus [Unser Beispielshop](../concepts/example-shop.md). Zunächst gibt es das T-Shirt nur in Blau und Größe M. Auswählbare Varianten ergänzt du später.

## 1. Shopkonfiguration erstellen

Öffne **Isotope eCommerce → Konfiguration → Shopkonfigurationen** und erstelle **Trail Supply Inland**.

Wähle **EUR**, die Preisanzeige **Brutto** und den Preisfaktor `1`. Brutto bedeutet, dass der angezeigte Betrag die Steuer enthält.

Wähle dein inländisches Testland als Standardland für Rechnungs- und Lieferadresse. Wähle dasselbe Land ausdrücklich in den Listen erlaubter Rechnungs- und Lieferländer. Eine leere Liste erlaubter Länder lässt jedes Land zu.

Aktiviere die benötigten Adressfelder, darunter Name, Straße, Postleitzahl, Ort, Land und E-Mail. Mache die E-Mail der Rechnungsadresse zur Pflichtangabe, damit die Testbestellung eine Kontaktadresse hat. Speichere die Konfiguration.

Wähle diese Shopkonfiguration in der Contao-Seitenstruktur für den Startpunkt deiner Website. Verwende für diesen Testshop eine einzige Shop-ID.

**Prüfung:** Die Konfiguration ist gespeichert und der Website zugewiesen. Versand- und Zahlungsauswahl können leer bleiben, bis du diese Methoden in Schritt 6 erstellst.

## 2. Beispielsteuer einrichten

Das T-Shirt kostet **22,00 einschließlich einer fiktiven Steuer von 10 %**. Der Nettobetrag beträgt 20,00 und die Steuer 2,00. Lies [Preise und Steuern](../concepts/prices-and-taxes.md), wenn die Unterscheidung neu für dich ist.

1. Erstelle unter **Konfiguration → Steuersätze** den Satz **Beispiel Standard 10 %**.
2. Gib den Satz `10` und eine Bezeichnung wie „Beispielsteuer 10 %“ ein. Lass die Regel für diese Übung mit einem Land leer.
3. Erstelle unter **Konfiguration → Steuerklassen** die Klasse **Standardwaren**.
4. Wähle Beispiel Standard 10 % als **Im Produktpreis enthaltener Steuersatz**.
5. Lass **Steuersätze anwenden** leer und speichere. Der enthaltene Satz gilt bereits und soll nicht nochmals ausgewählt werden.

In dieser Übung weist du Standardwaren sowohl dem T-Shirt als auch den Versandkosten zu. Satz und Behandlung sind fiktiv und dienen dem Lernen. Verwende vor dem Start die für dein Geschäft passende Steuerkonfiguration.

**Prüfung:** Beide Datensätze existieren. Die Steuerklasse kennzeichnet den Prozentsatz, der bereits in den später eingegebenen Preisen enthalten ist.

## 3. Produkttyp und Galerie vorbereiten

Erstelle unter **Konfiguration → Galerien** eine Galerie namens **Bekleidungsbilder**. Wähle einen Galerietyp und eine zum Seitenlayout passende Bildgröße und speichere.

Erstelle unter **Konfiguration → Produkttypen** den Typ **Bekleidung**. Verwende die von der Installation angebotene Standardproduktklasse. Aktiviere die Felder für Name, Artikelnummer, Beschreibung, Preis, Bilder und Veröffentlichung. Nimm das Versandgewicht hinzu, falls spätere Versandarten es verwenden.

Lass Varianten und erweiterte Preise deaktiviert. Wähle die mitgelieferten Listen- und Reader-Templates sowie die Galerie Bekleidungsbilder. Ein Produkttyp ist die wiederverwendbare Bearbeitungskonfiguration für Produkte wie dieses T-Shirt.

**Prüfung:** Speichere einen Produktentwurf mit dem Typ Bekleidung und prüfe, ob die benötigten Felder erscheinen. Du kannst diesen Entwurf in Schritt 5 verwenden.

## 4. Shopseiten erstellen

Erstelle in der Contao-Seitenstruktur diese regulären Seiten unter dem Startpunkt der Website. Gib jeder Seite einen Artikel und veröffentliche sie mit deinem vorhandenen Seitenlayout.

| Seite | Hinzuzufügende Inhaltselemente |
| --- | --- |
| T-Shirts | Produktliste und Produktleser |
| Warenkorb | Warenkorb |
| Kasse | Kasse |
| Bestelldetails | Bestelldetails |

Ein Inhaltselement ist ein Block innerhalb eines Artikels. Wähle in der Typauswahl das passende Isotope-Element.

Wähle auf T-Shirts den Lesermodus auf der aktuellen Seite. Verwende in der Produktliste den Kategorieumfang für die aktuelle Kategorie und aktiviere **Im Lesermodus ausblenden**. Die Liste zeigt verfügbare Produkte, der Leser das ausgewählte Produkt. Lass im Leser die Schaltfläche **In den Warenkorb** ausgewählt.

Blende Bestelldetails aus der normalen Navigation aus. Kunden erreichen die Seite über ihren individuellen Bestelllink.

**Prüfung:** du kannst T-Shirts und Warenkorb als Besucher öffnen. Eine leere Produktliste und ein leerer Warenkorb sind zu erwarten, solange das Produkt fehlt.

## 5. Trail-T-Shirt hinzufügen

Öffne **Produkte** und bearbeite deinen Entwurf oder erstelle ein Produkt mit dem Typ Bekleidung.

| Feld | Eingabe |
| --- | --- |
| Name | Trail-T-Shirt |
| Artikelnummer | `TSHIRT-BLUE-M` |
| Beschreibung | Baumwoll-T-Shirt, Blau, Größe M. Enthalten ist ein T-Shirt. |
| Preis | `22.00` |
| Steuerklasse | Standardwaren |
| Kategorien | T-Shirts |

Füge ein Foto hinzu, speichere und veröffentliche das Produkt. Lass Start- und Enddatum für diese Übung leer.

**Prüfung:** Das T-Shirt erscheint auf der Kategorieseite, öffnet sich im Leser und zeigt 22,00 EUR. Größe und Farbe stehen in der Beschreibung. Auswahlfelder sind noch nicht nötig.

## 6. Versand und Testzahlung hinzufügen

Erstelle unter **Konfiguration → Versandarten** die **Standardlieferung**. Wähle den pauschalen Versandtyp, die pauschale Berechnung, den Preis `5.50` und die Steuerklasse Standardwaren. Aktiviere und speichere die Versandart.

Wähle unter **Konfiguration → Zahlungsarten** den Typ **Barzahlung** und nenne die Methode **Testzahlung**. Wähle aus den mitgelieferten Zahlungsstatus **In Bearbeitung** für eine laufende Zahlung. Lass die Zahlungsgebühr leer. Ergänze den Hinweis „Dies ist eine Testbestellung. Es wird kein Geld eingezogen.“ Aktiviere und speichere die Methode.

Mit dem Typ Barzahlung übst du einen Offline-Zahlungsablauf. Er zieht kein Geld ein und prüft kein Bankkonto.

Kehre zu **Shopkonfigurationen → Trail Supply Inland** zurück und wähle Standardlieferung und Testzahlung. Speichere.

**Prüfung:** Beide Methoden sind aktiviert und in der Konfiguration ausgewählt. Sie erscheinen an der Kasse, sobald die Seiten verbunden sind.

## 7. Seiten verbinden

Setze im Produktleser **Weiterleitungsseite nach dem Hinzufügen** auf Warenkorb, damit Kunden zum Warenkorb gelangen. Setze das Kassenziel auf Kasse.

Wähle im Warenkorb-Element Kasse als Kassenziel. Wähle im Kasse-Element die Gastbestellung und setze das Ziel nach Bestellabschluss auf Bestelldetails. Lass die Schritte für Adresse, Versand und Zahlung bei diesem ersten Test sichtbar.

Die Seite Bestelldetails benötigt ihr Isotope-Element. Es zeigt den Kauf an und setzt nach der Bestellung die Zahlungsabwicklung fort.

**Prüfung:** Füge das T-Shirt hinzu und öffne den Warenkorb. Von dort sollte der Kassenlink die Kasse öffnen.

## 8. Testbestellung aufgeben

Verwende eine separate Besuchersitzung. Kaufe ein T-Shirt, gib fiktive Adressdaten in deinem gewählten Testland ein und verwende deine eigene E-Mail-Adresse. Wähle Standardlieferung und Testzahlung.

Die Zusammenfassung sollte Folgendes zeigen:

| Bestandteil | Bruttobetrag |
| --- | ---: |
| Ein Trail-T-Shirt | 22,00 EUR |
| Standardlieferung | 5,50 EUR |
| Gesamt | 27,50 EUR |

Der Gesamtbetrag enthält 2,50 EUR Beispielsteuer. Es fällt keine Zahlungsgebühr an. Weichen die Werte ab, prüfe Steuerklasse, Preise, Konfiguration und ausgewählte Methoden vor dem Absenden.

Sende die Bestellung einmal ab. Du solltest die Detailseite erreichen und eine Bestellreferenz sehen.

**Prüfung:** Die Details entsprechen deiner Auswahl. Der Zahlungsstatus kann In Bearbeitung sein, da diese Testmethode kein Geld eingezogen hat.

## 9. Bestellung als Shopbetreiber finden

Öffne im Backend **Bestellungen** und suche die Testbestellung. Prüfe Artikelnummer, Menge, Adressen, Gesamtbetrag und die getrennten Status für Bestellung, Zahlung und Versand.

Damit ist bestätigt, dass der Kauf im Shop angekommen ist. Das separate Kapitel [Bestellungen bearbeiten](../usage/orders.md) erklärt die tägliche Prüfung von Zahlungen und Vorbereitung des Versands.

## 10. Shopvorbereitung abschließen

Richte eine [Bestellbestätigung](../setup/general/notifications.md) ein, wähle sie im Kasse-Element und gib eine weitere Testbestellung auf, um Zustellung und Wortlaut zu prüfen.

Verwende dann [Shop einrichten](../setup/index.md) für benötigte Funktionen wie auswählbare Größen und Farben, echte Zahlungsarten oder Dokumente. Arbeite [Vor der Shoperöffnung](launch.md) durch, bevor du echte Käufe zulässt.

Nach dem Start findest du unter **[Tägliche Arbeit](../usage/index.md)** Anleitungen zum Hinzufügen von Produkten, Ändern von Preisen und Bearbeiten von Bestellungen. Dafür musst du diese Installationsanleitung nicht wiederholen.
