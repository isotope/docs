---
title: 'Installation via Composer'
description: 'The installation via Composer.'
aliases:
    - /en/installation/via_composer/
weight: 40
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Isotope eCommerce can also be installed via [Composer](http://c-c-a.org/ueber-composer)[(questions in the forum](https://community.contao.org/de/forumdisplay.php?168-composer) &amp; [information in the wiki)](http://de.contaowiki.org/Composer). To do so, click on `Erweiterungsverwaltung` in the backend.

On a fresh Contao installation it looks like this:

![Extension management overview](er.png)

Click on `Erweiterung installieren` in the top right corner.

Then enter `composer` as the name of the extension, make sure the spelling is correct and that Isotope eCommerce is compatible with your Contao version.

![Select extension management Composer](er_composer.png)

After clicking `Weiter` you can choose the version you want to use. You should use the latest stable version. Look for the keyword `stable` when selecting the version. This will install the version `0.8.12 stable`:

![Extension management Select Composer version](er_composer_stable.png)

Follow the next steps. After successful installation, the navigation item `Paketverwaltung` should replace the `Erweiterungsverwaltung` and the `Erweiterungskatalog`.

![The new Package Management navigation item](system_paketverwaltung.png)

Then click on `Paketverwaltung` and you will be asked to install Composer.

![Install Composer Library completely](composer_installieren.png)

In the next window, `Preconditions` will show you if your server meets the system requirements. At `Migration setup` you can choose between `Remove packages` (for an installation without extensions) or `Upgrade packages to Composer` and `For production use`.

![System requirements for Composer](composer_voraussetzung.png)

Click below on `do migration`.

![Composer was successfully installed](composer_erforlgreich_installiert.png)

Now you come to the actual installation of Isotope eCommerce.

At "Package name or search term" type `isotope/isotope-core` and confirm with a click on `Suchen`.

![Package management Select isotopes](paketname_isotope.png)

Mark the package for installation by clicking on the name.

![Mark package for installation](paket_installation.png)

Select the version `<docrobot_current_version>.*` and do not change the setting `Bugfix Releases <docrobot_current_version>.*` and click `Paket zur Installation vormerken`.

![Install package isotope/isotope-core](paketverwaltung_isotope.png)

Click`Paket aktualisieren` and wait.

![Update package](paket_aktualisieren.png)

If the installation of Isotope eCommerce was successful, you should now see the new navigation items:

![Isotope was successfully installed](isotope_erfolgreich_installiert.png)

In the last step, update the database. To do this, go to `http://www.domain.tld/contao/install.php`, enter the `Passwort` you chose during the installation and click on `Datenbank aktualisieren` and then return to the backend.

![Update database](datenbank-aktualisieren.png)

Now you can start [configuring your webshop](/de/backend/).
