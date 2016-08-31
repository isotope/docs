# Installation via Composer

Isotope eCommerce lässt sich auch über [Composer][1] ([Fragen im Forum][2] & [Informationen im Wiki][3]) installieren. Klicke dazu auf `Erweiterungsverwaltung` im Backend.

Auf einer ganz frischen Contao Installation sieht das ungefähr so aus:

<docrobot_image path="installation/via_composer/er.png" alt="Erweiterungsverwaltung Übersicht">

Klicke oben rechts auf `Erweiterung installieren`.

Danach gebe als Name der Erweiterung `composer` ein, achte auf die korrekte Schreibweise und das Isotope eCommerce mit deiner Contao-Version kompatibel ist. 

<docrobot_image path="installation/via_composer/er_composer.png" alt="Erweiterungsverwaltung Composer auswählen">

Nach einem Klick auf `Weiter` kannst du die gewünschte Version auswählen. Du solltest die letzte Stable-Versionen einsetzen. Achte auf das Schlüsselwort `stable` beim auswählen der Version. Hier wird die Version `0.8.12 stable` installiert:

<docrobot_image path="installation/via_composer/er_composer_stable.png" alt="Erweiterungsverwaltung Composer Version auswählen">

Folge den weiteren Schritten. Nach erfolgreicher Installation, sollte der Navigationspunkt `Paketverwaltung` die `Erweiterungsverwaltung` und den `Erweiterungskatalog` ersetzen.

<docrobot_image path="installation/via_composer/system_paketverwaltung.png" alt="Der neue Navigationspunkt Paketverwaltung">

Danach klickst du auf `Paketverwaltung` und wirst gebeten Composer zu installieren.

<docrobot_image path="installation/via_composer/composer_installieren.png" alt="Composer Library vollständig installieren">

Im nächsten Fenster wird unter `Preconditions` angezeigt ob dein Server die Systemvoraussetzung erfüllt. Beim `Migration setup` wählst du zum einen `Remove packages` (bei einer Installation ohne Erweiterungen) oder `Upgrade packages to Composer` und zum anderen `For production use`.

<docrobot_image path="installation/via_composer/composer_voraussetzung.png" alt="Systemvoraussetzung für Composer">

Klicke unten auf `do migration`.

<docrobot_image path="installation/via_composer/composer_erforlgreich_installiert.png" alt="Composer wurde erfolgreich installiert">

Jetzt kommst du zur eigentlichen Installation von Isotope eCommerce.

Bei "Paketname oder Suchbegriff" tippst du `isotope/isotope-core` ein und bestätigst mit einem klick auf `Suchen`.

<docrobot_image path="installation/via_composer/paketname_isotope.png" alt="Paketverwaltung Isotope auswählen">

Das Paket zur Installation vormerken, indem du auf den Namen klickst.

<docrobot_image path="installation/via_composer/paket_installation.png" alt="Paket zur Installation vormerken">

Du wählst die Version `2.3.3` aus und änderst nichts an der Einstellung `Bugfix Releases 2.3.*` und klickst `Paket zur Installation vormerken`.

<docrobot_image path="installation/via_composer/paketverwaltung_isotope.png" alt="Paket isotope/isotope-core installieren">

`Paket aktualisieren` klicken und warten.

<docrobot_image path="installation/via_composer/paket_aktualisieren.png" alt="Paket aktualisieren">

War die Installation von Isotope eCommerce erfolgreich, solltest du nun die neuen Navigationspunkte sehen:

<docrobot_image path="installation/via_composer/isotope_erfolgreich_installiert.png" alt="Isotope wurde erfolgreich installiert">

Im letzten Schritt, aktualisierst du noch die Datenbank. Dazu rufst du `http://www.domain.tld/contao/install.php` auf, gibst dein bei der Installation gewähltes `Passwort` ein und klickst auf `Datenbank aktualisieren` und kehrst danach ins Backend zurück.

<docrobot_image path="installation/via_composer/datenbank-aktualisieren.png" alt="Datenbank aktualisieren">

Nun kannst du mit dem <docrobot_route name="backend-configuration">konfigurieren deines Webshops beginnen</docrobot_route>.

[1]: http://c-c-a.org/ueber-composer
[2]: https://community.contao.org/de/forumdisplay.php?168-composer
[3]: http://de.contaowiki.org/Composer
