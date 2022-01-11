---
menuTitle: "DHL Business"
title: "Versandart DHL-Business"
description: "Die Shop-Konfiguration - Bestellablauf - Versandarten - DHL-Business."
aliases:
    - /de/backend-konfiguration-shop-bestellablauf-versandarten-dhlbusiness/
weight: 120    
---

Voraussetzung 

Einen DHL Vertrag mit der Freischaltung der API 2.2. 

Das Plugin funktioniert noch nicht mit der API 3 von DHL. Gegebenenfalls muss eine Freischaltung bei DHL angefragt werden.

Eine Installation der aktuellen Version 0.5 erfolgt über composer require petschko/dhl-php-sdk

Danach findet ihr unter: Shop-Konfiguration > Versandarten beim erstellen einer neuen Versandart die Möglichkeit „DHL-Business-Versand“ unter „Versandart-Typ“.

Nachdem ihr diese ausgewählt habt müsste ihr noch die API-Konfiguration mit euren DHL Daten konfigurieren.

Diese Zugangsdaten erhaltet ihr auf Anfrage bei DHL.

Dazu zählen:
	1. Benutzername (bspw. „shopuser“)
	2. Passwort (bspw. 123456789)
	3. Die Kontonummer (14 Zeichen)
	4. Die Auswahl der DHL Produkts (Standardmäßig: Nationales Paket)
	5. Die Anwendungs-ID (Alias ohne Leerzeichen)
	6. Der API-Token

Danach gebt ihr noch wie gewohnt alle weiteren Versanddaten an.

Mit der Option „Logging aktivieren“ ganz unten rechts in diesen Versandeinstellungen könnt ihr eventuelle Fehler im Ordner: var > logs > isotope_dhl_business.log einsehen.

Erfolgt nun eine Bestellung im CONTAO wird das dazugehörige Versandlabel automatisch generiert und steht euch im DHL Geschäftskundenportal (https://geschaeftskunden.dhl.de/) zur Verfügung.

Loggt euch dazu einfach ein und geht auf: Paket & Waren > Sendungsübersicht

Das Vorgehen nach einer Bestellung ist also folgendes. 

Lieferschein und Rechnung im CONTAO generieren und drucken
Im DHL Geschäftskundenportal Versandlabel drucken

Diese Anleitung gilt für CONTAO Version 4.12.2 und ISOTOPE Version 2.7.4

{{< version "2.5" >}}

{{% notice warning %}}<p>Diese Versandart setzt Composer voraus und ist kein Contao Paket, deshalb kann es nicht über den Contao Manager installiert werden.</p><p><code>composer require petschko/dhl-php-sdk</code></p>{{% /notice %}}

