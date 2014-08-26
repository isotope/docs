# Systemvoraussetzungen

## Isotope eCommerce

Isotope eCommerce benötigt nachfolgende Erweiterungen, um reibungslos funktionieren zu können. Diese Abhängigkeiten werden bei der Installation automatisch mitinstalliert.

* [conditionalselectmenu][1]
* [dcawizard][2]
* [haste][3]
* [MultiColumnWizard][4]
* [NamespaceClassLoader][5]
* [notification_center][6]
* [tablelookupwizard][7]

## Contao

Da sich Isotope eCommerce nahtlos in Contao integriert, muss Contao zuerst **vollständig** aufgesetzt worden sein. 
Danach kann Isotope eCommerce problemlos wahlweise via <docrobot_route name="via_extension_repository">Extension Repository</docrobot_route> oder <docrobot_route name="via_composer">Composer</docrobot_route> installiert werden.

Wie sich Contao installieren lässt, findest du [in der entsprechenden Dokumentation auf der offiziellen Webseite von Contao][8].

<docrobot_message type="warning"><p>Beachte, dass die Systemvoraussetzungen von Contao zurzeit auch diejenigen von Isotope eCommerce sind. Prüfe folglich ob die entsprechende PHP-Version auf dem Server läuft. Dazu hilfreich kann auch der Contao Check sein. Weitere Informationen zu den <a href="https://contao.org/de/manual/3.3/installation.html#contao-systemvoraussetzungen" target="_blank">Systemvoraussetzungen von Contao</a>.</docrobot_message>

## MooTools

Aus historischen Gründen und der MooTools-Vergangenheit von Contao, wird für die vorliegende Version von Isotope eCommerce MooTools benötigt! Du musst folglich MooTools in deinen Seitenlayouts von Contao aktivieren.

[1]: https://contao.org/de/extension-list/view/conditionalselectmenu.de.html
[2]: https://contao.org/de/extension-list/view/dcawizard.de.html
[3]: https://contao.org/en/extension-list/view/haste.en.html
[4]: https://contao.org/de/extension-list/view/MultiColumnWizard.de.html
[5]: https://contao.org/de/extension-list/view/NamespaceClassLoader.de.html
[6]: https://contao.org/de/extension-list/view/notification_center.de.html
[7]: https://contao.org/de/extension-list/view/tablelookupwizard.de.html
[8]: https://contao.org/de/manual/3.3/installation.html#contao-installieren