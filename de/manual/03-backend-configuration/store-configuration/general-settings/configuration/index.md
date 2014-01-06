# Konfiguration


## Shop-Konfiguration

### Name

Vergebe einen Namen für die Konfiguration. Wenn mehrere Konfigurationen bestehen muss eine dieser Konfigurationen als **Standard-Konfiguration aktiviert** werden.


### Adresse

Hier wird eine **rechtskonforme Adresse** angeben. Diese Adressdaten stehen dann auf den automatisch generierten Rechnungen dieser Shop-Konfiguration.


### Konfiguration

Im nächsten Schritt kann ein **Präfix für die Bestellnummer** vergeben werden. Das kann ein Länderkürzel oder etwas anderes Sinngebendes sein.

Im Feld daneben kann die **Länge der Bestellnummer** bestimmt werden. Diese sollte natürlich lang genug sein, dass die Bestellnummern auf bestimmte Zeit eindeutig sein werden. Das richtet sich nach der voraussichtlichen Anzahl an Bestellungen.
 Wenn die Checkbox bei **Templates-Ordner** aktiviert ist, kann ein bestimmter Ordner im Ordner Templates ausgewählt werden. Die Templates in diesen Ordner werden dann automatisch, wenn sie im Namen unverändert sind, vom System bevorzugt. 

### Checkout

Beschränke in den folgenden Select-Listen die Versand- und Rechnungsländer.


#### Rechnungs-Länder

Definiere hier, welche Länder für die Rechnungsadresse zugelassen sind, wenn keine Länder erfasst werden, werden alle zugelassen.


#### Versand-Länder

Definiere hier, welche Länder für die Versandaddresse zugelassen sind, wenn keine Länder erfasst werden, werden alle zugelassen.


#### Rechnungs-Adressfelder

1. Bestimme hier welche Felder aktiv sind
2. Bestimme hier alternative Beschriftungen z. B. "Name" anstatt Nachname
3. Handelt es sich um ein Pflichtfeld, dh. muss der/die Kund(e)in hier zwingend angaben machen?
4. Über die beiden Pfeile wird die Reihenfolge in der Adressmaske bestimmt (beeinflusst sämtliche Rechnungsadressangaben, z. B. im Bestellvorgang, oder in einer separaten Adressverwaltung)

Die Reihenfolge der Felder kann über die grünen Pfeilsymbole verändert werden.



# Achtung Bild: Screenshot mit den Spalten der Tabelle, mit Legende


#### Versand-Adressfelder

(wie Rechnungs-Adressfelder)


#### Standard Rechnungsland

Definiere hier, welches Land, bei der Erstellung einer Rechnungsadresse vorausgewählt wird, oder lasse es offen, falls keine Vorauswahl gewünscht.


#### Standard Versandlang

Definiere hier, welches Land, bei der Erstellung einer Versandadresse vorausgewählt wird, oder lasse es offen, falls  keine Vorauswahl gewünscht.


#### Mitgliederländer einschränken

Hiermit können die Registierung bzw. die Verwaltungsmaske persönlicher Daten (seitens Contao) auf die Länder beschränkt werden, welche als Rechnungs bzw. Versandadresse gewählt wurden (siehe: Rechnungs-Länder, Versand-Länder).


### Preise

Im Einstellungsbereich Preise können die **Rundungspräzision**, einen **Rundungszuschlag** sowie ein **Mindestbestelltwert** eingeben werden.

#### Rundungspräzision

Die zugelassene Kommastellen bei den Beträgen (z. B. Preis, Mehrwertsteuer, Total) Beispiel: 200.00.


#### Rundungszuschlag

Definiere hier, welches die kleinste deklarierte Einheit in der jeweiligen Währung ist. z. B. 0.05 für CHF.


#### Mindestbestellwert

Definiere hier, ab welchem Betrag eine Bestellung ausgeführt werden kann.


### Währungs-Formatierung
 Bei der **Währungs-Formatierung** sollte auf die ländertypischen Unterschiede geachtet werden.

#### Währung

Definiere hier in welcher Währung die Preise sind, z. B. "CHF - Schweizer Franken" für die Schweiz.


#### Währungsformat

Definiere hier, wie Beträge dargestellt werden, d. h. ob ein Komma oder ein Punkt für Dezimalstellen verwendet werden und wie tausender Gruppierungen gemacht werden. Beispiel: CHF 10'000.00


#### Position der Währungsbezeichung/-symbol

Definiere hier, auf welcher Seite der Preisangabe die Währung steht. Beispiel für "Links des Preises" CHF 1'000.00 oder für "Rechts des Preises" 1.000,00 EURO.

Die Positionierung der Währungsbezeichnung/-symbol im Preis gibt im deutschen Raum darüber auskunft, ob der Produkt-Preis als Netto oder Brutto angegeben ist. Bei Bruttopreisen sollte "Rechts des Preises" ausgewählt werden.


#### Währungssymbol verwenden

Definiere hier, ob, falls vorhanden, ein Währungssymbol verwendet wird? z. B. € für Euro oder $ für Dollar.


### Währungsumrechnung

Unter Währungsumrechnung kann ein Faktor für die Umrechnung eingetragen werden. Der Faktor "1" wird eingetragen, wenn kein bestimmter Umrechnungsfaktor festgelegt werden soll. Ob  Multiplizieren oder Dividieren ausgewählt wird ist egal.
 Zudem gibt es die Möglichkeit einen automatischen Währungsrechner zu aktivieren.


### Bestellungen

In diesem Bereich wird der Status für eine neue Bestellung und der Status für eine fehlerhafte Bestellung gesetzt. Zusätzlich kann ein Rechnungslogo aus der Dateiverwaltung ausgewählt werden.


### Bilder

Es gibt drei verschiedene Arten von Produkt-Galerien. Zum einen die "Inline-Galerie", die  "Inline-Galerie mit Zoom-Effekt“ oder die Standard-Galerie von Contao.

Im nachstehenden Bereich kann ein Platzhalter für Produktbilder aus der Dateiverwaltung gewählt werden. Dieses Bild wird dann dargestellt, wenn ein Produkt kein Produktbild hat.
 Es gibt folgende CSS-Klassen: 
* **gallery** alle Vorschaubilder der Galerie
* **thumbnail** das Vorschaubild in der Produktliste
* **large** die Grossansicht des Bildes in der Galerie.
* **medium** das erste Vorschaubild der Galerie

Zusätzlich können noch die Breite und Höhe des Bildes sowie der Modus, die Position und ein allfälliges Wasserzeichen bestimmt werden. 
Falls die Galerie angepasst werden soll, funktioniert das über das Standard-Template für den Produktleser "iso_reader_default". Im Modul Produktleser kannst das angepasste Template zugewiesen werden.