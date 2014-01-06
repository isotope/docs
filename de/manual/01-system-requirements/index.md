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
wobei wir für eine bessere Performance MySQL 5 empfehlen. Ausserdem werden die PHP-Erweiterungen "GDlib" (Bildbearbeitung), "DOM" (XML-Dateien) und
"SOAP" (Extension Repository) sowie optional "mbstring" (internationale Zeichen)
und "mcrypt" (Verschlüsselung) benötigt. Contao wurde erfolgreich in allen modernen
Browsern wie Firefox (ab Version 2) oder Internet Explorer (ab Version 7) getestet.


## Der Contao-Check

Lade den Contao-Check herunter und finde heraus, ob der Server die
Contao-Systemvoraussetzungen erfüllt. Der Contao-Check prüft, ob das
Extension Repository und das Live Update zur Verfügung stehen und ob der Safe Mode
Hack benötigt wird. Je nach Systemkonfiguration kann mit Hilfe des
Web-Installers eine neue Contao-Installation aufgesetzt oder eine bestehende
Installation geprüft werden.

![](https://raw.github.com/contao/docs/2.11/manual/de/images/contao-check.jpg)

Entpacke die Zip-Datei, übertrage den Ordner `check` in das Contao-Verzeichnis und 
öffne ihn in einem Browser.

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