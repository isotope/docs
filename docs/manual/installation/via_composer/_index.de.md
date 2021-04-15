---
title: "Installation via Composer"
description: "Die Installation via Composer."
aliases:
    - /de/installation-composer/
weight: 40    
---


Isotope eCommerce lässt sich auch über [Composer][1] ([Fragen im Forum][2] & [Informationen im Wiki][3]) installieren. Klicke dazu auf `Erweiterungsverwaltung` im Backend.

Auf einer ganz frischen Contao Installation sieht das ungefähr so aus:

![Erweiterungsverwaltung Übersicht](er.png)

Klicke oben rechts auf `Erweiterung installieren`.

Danach gebe als Name der Erweiterung `composer` ein, achte auf die korrekte Schreibweise und das Isotope eCommerce mit deiner Contao-Version kompatibel ist. 

![Erweiterungsverwaltung Composer auswählen](er_composer.png)

Nach einem Klick auf `Weiter` kannst du die gewünschte Version auswählen. Du solltest die letzte Stable-Versionen einsetzen. Achte auf das Schlüsselwort `stable` beim auswählen der Version. Hier wird die Version `0.8.12 stable` installiert:

![Erweiterungsverwaltung Composer Version auswählen](er_composer_stable.png)

Folge den weiteren Schritten. Nach erfolgreicher Installation, sollte der Navigationspunkt `Paketverwaltung` die `Erweiterungsverwaltung` und den `Erweiterungskatalog` ersetzen.

![Der neue Navigationspunkt Paketverwaltung](system_paketverwaltung.png)

Danach klickst du auf `Paketverwaltung` und wirst gebeten Composer zu installieren.

![Composer Library vollständig installieren](composer_installieren.png)

Im nächsten Fenster wird unter `Preconditions` angezeigt ob dein Server die Systemvoraussetzung erfüllt. Beim `Migration setup` wählst du zum einen `Remove packages` (bei einer Installation ohne Erweiterungen) oder `Upgrade packages to Composer` und zum anderen `For production use`.

![Systemvoraussetzung für Composer](composer_voraussetzung.png)

Klicke unten auf `do migration`.

![Composer wurde erfolgreich installiert](composer_erforlgreich_installiert.png)

Jetzt kommst du zur eigentlichen Installation von Isotope eCommerce.

Bei "Paketname oder Suchbegriff" tippst du `isotope/isotope-core` ein und bestätigst mit einem klick auf `Suchen`.

![Paketverwaltung Isotope auswählen](paketname_isotope.png)

Das Paket zur Installation vormerken, indem du auf den Namen klickst.

![Paket zur Installation vormerken](paket_installation.png)

Du wählst die Version `<docrobot_current_version>.*` aus und änderst nichts an der Einstellung `Bugfix Releases <docrobot_current_version>.*` und klickst `Paket zur Installation vormerken`.

![Paket isotope/isotope-core installieren](paketverwaltung_isotope.png)

`Paket aktualisieren` klicken und warten.

![Paket aktualisieren](paket_aktualisieren.png)

War die Installation von Isotope eCommerce erfolgreich, solltest du nun die neuen Navigationspunkte sehen:

![Isotope wurde erfolgreich installiert](isotope_erfolgreich_installiert.png)

Im letzten Schritt, aktualisierst du noch die Datenbank. Dazu rufst du `http://www.domain.tld/contao/install.php` auf, gibst dein bei der Installation gewähltes `Passwort` ein und klickst auf `Datenbank aktualisieren` und kehrst danach ins Backend zurück.

![Datenbank aktualisieren](datenbank-aktualisieren.png)

Nun kannst du mit dem [konfigurieren deines Webshops](/de/backend/) beginnen.

[1]: http://c-c-a.org/ueber-composer
[2]: https://community.contao.org/de/forumdisplay.php?168-composer
[3]: http://de.contaowiki.org/Composer
