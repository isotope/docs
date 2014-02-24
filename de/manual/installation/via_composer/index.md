# Installation via Composer

Isotope eCommerce lässt sich auch über [Composer][1] ([Fragen im Forum][2] & [Informationen im Wiki][3]) installieren. Klicke dazu auf `Erweiterungsverwaltung` im Backend.

Auf einer ganz frischen Contao Installation sieht das ungefähr so aus:

<docrobot_image path="installation/via_composer/er.png" alt="Erweiterungsverwaltung Übersicht">

Klicke oben rechts auf `Erweiterung installieren`.

Danach geben wir als Name der Erweiterung `composer` ein. 

<docrobot_image path="installation/via_composer/er_composer.png" alt="Erweiterungsverwaltung Composer auswählen">

Nach einem Klick auf `Weiter` können wir die gewünschte Version auswählen. Du solltest die letzte Stable-Versionen einsetzen. Achte auf das Schlüsselwort `stable` beim auswählen der Version. Hier wird die Version `0.8.12 stable` installiert:

<docrobot_image path="installation/via_composer/er_composer_stable.png" alt="Erweiterungsverwaltung Composer Version auswählen">

Folge den weiteren Schritten. Nach erfolgreicher Installation, sollte der Navigationspunkt `Paketverwaltung` die `Erweiterungsverwaltung` und den `Erweiterungskatalog` ersetzen.

<docrobot_image path="installation/via_composer/system_paketverwaltung.png" alt="Der neue Navigationspunkt Paketverwaltung">

Danach klicken wir auf `Paketverwaltung` und werden gebeten Composer zu installieren.

<docrobot_image path="installation/via_composer/composer_installieren.png" alt="Composer Library vollständig installieren">

Im nächsten Fenster wird unter `Preconditions` angezeigt ob unser Server die Systemvoraussetzung erfüllt. Beim `Migration setup` wählen wir zum einen `Remove packages` (bei einer Installation ohne Erweiterungen) oder `Upgrade packages to Composer` und zum anderen `For production use`.

<docrobot_image path="installation/via_composer/composer_voraussetzung.png" alt="Systemvoraussetzung für Composer">

Wir klicken unten auf `do migration`.

<docrobot_image path="installation/via_composer/composer_erforlgreich_installiert.png" alt="Composer wurde erfolgreich installiert">

Jetzt kommen wir zur eigentlichen Installation von Isotope eCommerce.

Bei "Paketname oder Suchbegriff" tippen wir `isotope/isotope-core` ein und bestätigen mit einem klick auf `Suchen`.

<docrobot_image path="installation/via_composer/paketname_isotope.png" alt="Paketverwaltung Isotope auswählen">

Das Paket zur Installation vormerken, indem wir auf den Namen klicken.

<docrobot_image path="installation/via_composer/paket_installation.png" alt="Paket zur Installation vormerken">

Wir wählen die Version `2.0.3` aus und ändern nichts an der Einstellung `Bugfix Releases 2.0.*` und klicken `Paket zur Installation vormerken`.

<docrobot_image path="installation/via_composer/paketverwaltung_isotope.png" alt="Paket isotope/isotope-core installieren">

`Paket aktualisieren` klicken und warten.

<docrobot_image path="installation/via_composer/paket_aktualisieren.png" alt="Paket aktualisieren">

War die Installation von Isotope eCommerce erfolgreich, solltest du nun die neuen Navigationspunkte sehen:

<docrobot_image path="installation/via_composer/isotope_erfolgreich_installiert.png" alt="Isotope wurde erfolgreich installiert">

Nun kannst du mit dem <docrobot_route name="backend-configuration">konfigurieren deines Webshops beginnen</docrobot_route>.

[1]: http://c-c-a.org/ueber-composer
[2]: https://community.contao.org/de/forumdisplay.php?168-composer
[3]: http://de.contaowiki.org/Composer
