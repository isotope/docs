# Backend-Konfiguration

Die Einrichtung von Isotope eCommerce ist einfach und lässt sich in wenigen Schritten zusammenfassen:
- Grundkonfiguration des Shops und der Produkttypen
- Einrichtung des Bestellablaufs, (Steuern, Zahlungs- und Versandoptionen)
- Einrichtung der Seitenstruktur und der Frontend-Module
- Erfassen der Produkte

Nachdem Sie die Erweiterung im System installiert haben, erscheinen im Menü zusätzliche Navigationspunkte.

![](https://raw.github.com/isotope/docs/tree/1.4/de/manual/images/2-backend_01.png)

Die Einrichtung erfolgt im Modul „Shop-Konfiguration“, und zwar am besten *von unten nach oben*.

1. Konfigurationen & E-Mail Vorlagen
2. Steuersätze & Steuerklassen
3. Versandarten
4. Zahlungsarten
5. Attribute
6. Produkttypen

Erst nachdem Sie alles eingerichtet haben, sollten Sie sich um die Produkte kümmern!


## Konfigurationen

Konfigurationen enthalten verschiedene Einstellungen wie Währung, Preisberechnung und Produktbild-Grössen. Sie können mehrere Konfigurationen anlegen um verschiedene Shops innerhalb einer Contao-Installation zu betreiben, oder um z.B. eine Umschaltung zwischen mehreren Währungen zu ermöglichen. Folgendes ist zur Konfiguration zu beachten:
- Die primäre Konfiguration sollte immer als „Standard-Konfiguration“ markiert sein. Mindestens eine „Standard-Konfiguration“ wird zwingend benötigt.
- Das Land in der Adresse der Konfiguration wird als primäres Land für Steuerberechnungen und Versand verwendet.
- Legen Sie mögliche Länder und Adressfelder für Versand und Rechnung fest. Neue Adressen können nur diese Länder enthalten, unpassende Adressen aus dem Adressbuch eines Mitgliedes werden im Bestellprozess nicht angeboten.


## E-Mail Vorlagen

E-Mail Vorlagen werden für den Versand von Bestellbestätigungen und anderen Nachrichten an Kunden und Shop-Betreiber verwendet. Legen Sie mindestens eine E-Mail Vorlage an, Sie benötigen diese später für den Bestellprozess.

Eine Liste der Platzhalter für die Verwendung im Text finden Sie durch klicken auf den „Help Wizard“ rechts neben den Feldbezeichnungen. Jede Vorlage kann in mehreren Sprachen angelegt werden, vergessen Sie nicht bei der Hauptsprache den Sprachen-Fallback zu aktivieren.


## Steuersätze

Steuersätze entsprechen im Normalfall den Steuern, welche in verschiedenen Ländern/Regionen anfallen. Für Deutschland müssen Sie beispielsweise eine Umsatzsteuer mit 19% anlegen.

Steuersätze sind die Grundformeln für die Steuerberechnung. Sie können festlegen, für welches Land und ggf. Region die Steuer gültig ist und welche Adresse (Rechnung und/oder Versand) berücksichtigt werden soll.

Wenn Sie einen Festpreis-Zuschlag definieren wollen, wählen Sie zuerst eine Shop-Konfiguration. Danach können Sie im Auswahl-Menü des Steuersatzes die Währung wählen. Der Zuschlag wird dann natürlich nur bei der entsprechenden Shop-Konfiguration berücksichtigt.


## Steuerklassen

In Steuerklassen werden mehrere Steuersätze gruppiert, sortiert und später den einzelnen Produkten zugewiesen. Wählen Sie einen „enthaltenen Steuersatz“, wird dieser vom Preis des Produktes abgezogen, sollte er nicht zutreffend sein (z.B. anderes Land in der Rechnungsadresse).


## Versandarten
Über Versandarten können Sie die Kosten für Versand im Bestellprozess hinzufügen. Legen Sie mehrere Versandarten an, sobald Sie verschiedene Beträge z.B. für Länder benötigen. In den meisten Fällen reicht das Modul „Pauschalversand“ aus.

*Wenn im Warenkorb nur Artikel enthalten sind, welche keinen Versand erfordern (z.B. Download-Artikel), wird die Versandadresse und Versandart in der Kasse nicht angezeigt.*


## Zahlungsarten

Mittels Zahlungsarten definieren Sie, welche Zahlungsmöglichkeiten im Bestellprozess zur Verfügung stehen. Zahlungsarten sind in verschiedene Module organisiert, welches jedes über eigene Eigenschaften verfügt.


### Barzahlung

Das Barzahlungsmodul wird für alle Zahlungen verwendet, die im System nicht automatisiert sind. Dazu gehören auch Rechnung und Vorauskasse. Besonders bei diesem Modul ist das Feld für die Zahlungshinweise nützlich, hiermit können Sie später dem Kunden z.B. die Bankdaten für eine Überweisung mitteilen.


### Andere Zahlungsmodule

Alle weiteren Zahlungsmodule beziehen sich immer auf einen Anbieter, den so genannten Payment Provider. Der Payment Provider definiert, welche Zahlungsmöglichkeiten (z.B. Kreditkarten) zur Verfügung bestehen. Dieser stellt Ihnen auch die benötigten technischen Informationen und Passwörter/Zugangscodes zur Verfügung.


## Attribute

Als Attribute bezeichnen wir eigene, in der Datenbank angelegte Feldtypen. Ähnlich zum Formulargenerator können damit eigene Felder für Produkte angelegt werden. Sobald Sie Varianten wie z.B. Grösse und Farbe für ein Produkt zur Auswahl anbieten wollen, benötigen Sie eigene Attribute. Technisch gesehen werden die als Attribut definierten Felder später im DCA angelegt, weshalb es keinen Unterschied macht ob Attribute per Programmcode oder über‘s Backend angelegt werden.

Die wichtigste Option in den Attributen ist „Für Varianten verwenden“. Aktivieren Sie diese Checkbox, wenn dieses Attribut als Varianten-Option angewendet werden soll. Sie können auch eigene Felder definieren, welche nicht auf Varianten bezogen sind, beispielsweise ein Textfeld für die ISBN-Nummer bei Büchern.

Neue Attribute werden – abgesehen von Varianten-Optionen – nicht automatisch im Frontend angezeigt! Sie müssen dazu das das Listen- und/oder Detail-Template anpassen, und die entsprechende Variable an der gewünschten Position einfügen.


## Produkttypen

Produkttypen sind gleichzeitig eine Kategorisierung, Zugriffskontrolle und Konfiguration für verschiedene Produkte.


### Darstellung

Für jeden Produkttyp können Sie eigene Listen- und Detail-Templates wählen. Auf diese Weise lassen sich zwei verschiedene Artikeltypen unterschiedlich darstellen. Beispielsweise sollte bei Büchern ein eigenes Attribut „ISBN-Nummer“ mit ausgegeben werden, bei T-Shirts natürlich nicht.


### Sprachen

Pro Produkttyp können Sie definieren, ob mehrere Sprachen für einen Artikel erfasst werden können. In der Regel haben Sie für einen Shop bei jedem Produkttypen dieselben Sprachen, es kann aber auch unterschiedlich sein wenn Sie mehrere Shops in einer Installation betreiben. Wie Sie die Sprachen pro Produkt verwalten, lesen Sie im Kapitel „Produkt-Verwaltung“.


### Attribute

Die Grundinstallation von Isotope eCommerce verfügt bereits standardmässig über die wichtigsten Attribute, welche für den Shopbetrieb normalerweise benötigt werden. Da aber nicht immer alle Attribute für ein Produkt benötigt werden, lässt sich dies im Produkttyp konfigurieren.

Attribute verwenden einen von Contao bekannten CheckboxWizard, der zusätzlich Gruppen enthält. Diese Gruppen sind für jedes Feld festgelegt, innerhalb einer Gruppe können Sie die Felder mittels auf- und ab-Pfeilen sortieren. Einige Felder sind Pflicht und lassen sich nicht deaktivieren, wenn sie für den ordnungsgemässen Betrieb des Systems benötigt werden.


### Varianten

Wenn Ihr Produkt über Varianten verfügt, können Sie dies im Produkttyp aktivieren. Wählen Sie für Varianten die Attribute, welche sich vom Basis-Produkt unterscheiden (z.B. Preis). Varianten-Felder müssen Sie beim Basis-Produkt aktivieren, diese stehen in den Varianten-Attributen nicht zur Verfügung.

*Zum Verständnis:* In Isotope eCommerce ist eine Variante ein Unter-Produkt, welches die meisten Informationen (z.B. Beschreibung) vom Basis-Produkt erbt, aber einzelne Attribute (z.B. der Preis) sich unterscheiden.


### Downloads

Wenn Sie Downloads anbieten wollen, aktivieren Sie dies im jeweiligen Produkttyp. Weitere Informationen zur Handhabung von Download-Produkten finden Sie im Kapitel „Produkt-Verwaltung“.


### Zugriffsrechte pro Produkttyp

In den Einstellungen von Benutzergruppen und Benutzern müssen Sie einzelne Produkttypen erlauben. Mit dieser Funktion lassen sich Produkte von mehreren Backend-Benutzern verwalten, ohne dass der Eine die Produkte des Anderen sieht.