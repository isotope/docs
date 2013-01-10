# Frontend-Einrichtung

Die Darstellung für Produkte, Warenkorb, Kasse usw. erfolgt über die von anderen Contao-Erweiterungen bekannten Frontend-Module. Wie bei den Nachrichten verwenden wir Listen- und Detail-Module für die Darstellung der Produkte, dazu gibt es weitere Module für Warenkorb, Kasse, Adressverwaltung usw.

Ihre Seitenstruktur sollte mindestens in etwa folgende Seiten enthalten:
- Produkte
    - Kategorie 1
    - Kategorie 2
    - usw...
- Produkt-Details (unsichtbar)
- Warenkorb
- Kasse (unsichtbar)
    - Bestellung abgeschlossen (unsichtbar)


## Modul „Produktliste“

Das Produktlisten-Modul zeigt alle der aktuellen Seite (und/oder je nach Konfiguration deren Unterseiten) zugewiesenen Produkte an. Die wichtigste Einstellung in diesem Modul ist die „Weiterleitungs-Seite für Produktleser“, wählen Sie hier die „Produkt-Details“ Seite aus der Seitenstruktur aus.

Platzieren Sie dieses Modul am besten in einem Seitenlayout, da es in allen Kategorien-Seiten aufgeführt werden muss. Alternativ können Sie es natürlich auch in einem Artikel/Inhaltselement einsetzen.


## Modul „Produktdetails“
Dieses Modul wird die Detail-Anzeige eines Produktes benötigt. Platzieren Sie dieses Modul auf der „Produkt-Details“-Seite.


## Modul „Warenkorb“

Das Warenkorb-Modul erfüllt zwei Zwecke. Mittels Auswahl des Mini-Templates können Sie eine Darstellung der Warenkorb-Produkte für die Seitenspalte auf jeder Seite erstellen. Das Full-Template benötigen Sie für die „Warenkorb“-Seite in Ihrer Seitenstruktur. Auch hier sollten Sie unbedingt die Weiterleitungs-Seiten entsprechend Ihrer Seitenstruktur definieren.


## Modul „Kasse“

In der Kasse findet die gesamte Bestellabwicklung statt. Hier wählen Sie welche Zahlungs- und Versandmodule dem Kunden zur Verfügung stehen, ob ein Mitglied angemeldet sein muss und auch welche E-Mail Vorlage bei einer Bestellung versendet werden soll. Platzieren Sie dieses Modul auf der entsprechenden „Kasse“-Seite.


## Weitere Module

Die beschriebenen vier Frontend-Module reichen grundsätzlich aus, um einen Online-Shop mit Isotope eCommerce in Betrieb zu nehmen. Natürlich werden je nach Kundenanforderungen weiter Module benötigt. Beispielsweise kann ein angemeldetes Mitglied über das Modul „Adressbuch“ seine eigenen Adressen verwalten, oder über „Vergangene Bestellungen“ seine Kundenhistorie einsehen.