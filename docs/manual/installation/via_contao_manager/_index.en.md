---
title: 'Installation via Contao Manager'
description: 'The installation via Contao Manager.'
aliases:
    - /en/installation/via_contao_manager/
weight: 30
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Like many other extensions for Contao, Isotope eCommerce can be easily installed via the Contao Manager.

To do so, open the Contao Manager. You have already installed the desired Contao version via the Contao Manager.

`https://www.domain.tld/contao-manager.phar.php`

After the system check, we start the Contao Manager.

Click on the button `Pakete suchen`.

Type `Isotope` into the search field and click on `Paket hinzufügen` at `Isotope eCommerce - isotope/isotope-core`.

![Search and add extensions in the Contao Manager](cm-suchen.png)

Now we have 1 unconfirmed change, which we can check by clicking on `Änderungen prüfen`.

![Checking changes in the Contao Manager](cm-pruefen.png)

Clicking `Änderungen anwenden` will install Isotope eCommerce on your system.

![Apply changes in the Contao Manager](cm-anwenden.png)

![Confirming the installation in the Contao Manager](cm-install.png)

The last step is to update the database. To do this, go to `https://www.domain.tld/contao/install`, enter the `Passwort` you chose during the installation, click on Update Database and then return to the backend.

![Update the database](install-db.png)

Have fun with Isotope eCommerce!
