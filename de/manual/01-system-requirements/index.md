# Systemanforderungen

## Isotope eCommerce

Isotope in der [Version 1.4][1] benötigt [Contao 2.11][2] und folgende Erweiterungen.

* [ajax][3]
* [backend_tabletree][4]
* [conditionalselectmenu][5]
* [dcawizard][6]
* [MultiColumnWizard][7]
* [tablelookupwizard][8]


## Contao

Contao benötigt einen Webserver wie Apache oder IIS mit PHP- und MySQL-Support.
PHP muss mindestens in der Version 5.2.7 vorliegen und MySQL in der Version 4.1,
wobei wir für eine bessere Performance MySQL 5 empfehlen. Außerdem benötigen
Sie die PHP-Erweiterungen "GDlib" (Bildbearbeitung), "DOM" (XML-Dateien) und
"SOAP" (Extension Repository) sowie optional "mbstring" (internationale Zeichen)
und "mcrypt" (Verschlüsselung). Contao wurde erfolgreich in allen modernen
Browsern wie Firefox (ab Version 2) oder Internet Explorer (ab Version 7) getestet.


## Der Contao-Check

Laden Sie den Contao-Check herunter und finden Sie heraus, ob Ihr Server die
Contao-Systemvoraussetzungen erfüllt. Der Contao-Check prüft, ob Sie das
Extension Repository und das Live Update nutzen können und ob Sie den Safe Mode
Hack benötigen oder nicht. Je nach Systemkonfiguration können Sie mit Hilfe des
Web-Installers eine neue Contao-Installation aufsetzen oder eine bestehende
Installation prüfen.

![](https://raw.github.com/contao/docs/2.11/manual/de/images/contao-check.jpg)

Entpacken Sie die Zip-Datei, übertragen Sie den Ordner
`check` in Ihr Contao-Verzeichnis und öffnen Sie ihn in einem Browser.

[Den Contao-Check herunterladen][9] | [Zum Projekt auf GitHub][10]


[1]: https://contao.org/de/extension-list/view/isotope.10040089.de.html
[2]: https://github.com/contao/core/archive/support/2.11.zip
[3]: https://contao.org/de/extension-list/view/ajax.de.html
[4]: https://contao.org/de/extension-list/view/backend_tabletree.de.html
[5]: https://contao.org/de/extension-list/view/conditionalselectmenu.de.html
[6]: https://contao.org/de/extension-list/view/dcawizard.de.html
[7]: https://contao.org/de/extension-list/view/MultiColumnWizard.de.html
[8]: https://contao.org/de/extension-list/view/tablelookupwizard.de.html
[9]: https://github.com/contao/check/zipball/master
[10]: https://github.com/contao/check