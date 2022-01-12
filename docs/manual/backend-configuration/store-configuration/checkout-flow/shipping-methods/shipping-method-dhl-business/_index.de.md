---
menuTitle: "DHL Business"
title: "Versandart DHL-Business"
description: "Die Shop-Konfiguration - Bestellablauf - Versandarten - DHL-Business."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-versandarten-dhlbusiness/
weight: 120    
---

{{< version "2.5" >}}

## Voraussetzung 

Einen DHL Vertrag mit der Freischaltung der API 2.2. 
Das Plugin funktioniert noch nicht mit der API 3 von DHL. Gegebenenfalls muss eine Freischaltung bei DHL angefragt werden.


## Installation 

Diese Versandart setzt voraus dass die entsprechende API-Bibliothek installiert wird. Dies kann über den Befehl <code>composer require petschko/dhl-php-sdk</code> oder im Contao Manager über die Empfehlungen der Isotope-Erweiterung erfolgen.


## Einrichtung 

Nach der Installation findet ihr unter: Shop-Konfiguration > Versandarten beim erstellen einer neuen Versandart die Möglichkeit „DHL-Business-Versand“ unter „Versandart-Typ“. Nachdem ihr diese ausgewählt habt müsste ihr noch die API-Konfiguration mit euren DHL Daten konfigurieren. Diese Zugangsdaten erhaltet ihr auf Anfrage bei DHL.

Dazu zählen:
 - Benutzername (bspw. „shopuser“)
 - Passwort (bspw. 123456789)
 - Die Kontonummer (14 Zeichen)
 - Die Auswahl der DHL Produkts (Standardmäßig: Nationales Paket)
 - Die Anwendungs-ID (Alias ohne Leerzeichen)
 - Ein API-Token

Danach gebt ihr noch wie gewohnt alle weiteren Versanddaten an.

Mit der Option „Logging aktivieren“ ganz unten rechts in diesen Versandeinstellungen könnt ihr eventuelle Fehler im Ordner: var > logs > isotope_dhl_business.log einsehen.

Erfolgt nun eine Bestellung in Contao wird das dazugehörige Versandlabel automatisch generiert und steht euch im DHL Geschäftskundenportal (https://geschaeftskunden.dhl.de/) zur Verfügung.

Loggt euch dazu einfach ein und geht auf: Paket & Waren > Sendungsübersicht

Das Vorgehen nach einer Bestellung ist also folgendes. 
 1. Lieferschein und Rechnung in Contao generieren und drucken
 2. Im DHL Geschäftskundenportal Versandlabel drucken

