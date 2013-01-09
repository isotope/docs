# Einführung

Dieses Handbuch liefert eine erste Hilfe zur Installation und Konfiguration von Isotope eCommerce, der Online-Shop Erweiterung für Contao Open Source CMS.

**Um den neuen Namen von TYPOlight zu fördern, nennen wir das System bereits Contao Open Source CMS!**


## Voraussetzungen

Um diese Erweiterung erfolgreich einsetzen zu können, sollten Sie bereits mit dem Contao Open Source CMS vertraut sein. Isotope eCommerce hält sich sehr stark an die Strukturen von Contao, beispielsweise den Einsatz von Listen- und Detail-Modulen für die Frontend-Ausgabe.


## Systemanforderungen

Isotope eCommerce kann nicht auf allen Contao-Installationen betrieben werden.
Die folgenden Voraussetzungen müssten zwingend erfüllt sein (ältere Versionen *funktionieren nicht*):
- Contao 2.8.2 oder neuer wird eingesetzt
- PHP 5.2 ist vorhanden
- Die im Extension Repository aufgelisteten, abhängigen Erweiterungen „ajax“ und „conditionalselectmenu“ sind installiert


## Anmerkungen zur Datenbank
Grundsätzlich wurde Isotope eCommerce so entwickelt, dass die Datenbank-Abstraktion von Contao genutzt und die Erweiterung somit mit verschiedenen Datenbank-Servern betrieben werden. In der Praxis wurde dies jedoch nie getestet, deshalb wird MySQL als Datenbank-Server empfohlen.

Über die Verwaltungsoberfläche des Shops kann die Datenbank angepasst werden. Benutzer können zusätzliche Datenbankfelder (Spalten) erzeugen, es werden jedoch niemals Daten/Felder gelöscht. Nicht mehr benötigten Spalten müssen manuell über das Install-Tool entfernt werden.


## Installation

Isotope eCommerce kann – wie viele andere Contao-Erweiterungen – aus dem Extension Repository auf Knopfdruck installiert werden. Installieren Sie das Packet direkt über‘s Backend in Ihrem System, oder laden Sie das Packet vom Extension Repository unter http://www.typolight.org/erweiterungsliste/view/isotope.html herunter.


## Darstellung / Templates
Wie auch bei Contao selber ist das Frontend von Isotope eCommerce mittels Templates aufgebaut. An vielen Stellen lassen sich eigene Templates wählen, um die Darstellung zu individualisieren. Um einen Standard-Shop in Betrieb zu nehmen, sind Template-Anpassungen nicht zwingend nötig. Für erweiterte Funktionen wie z.B. eigene Produktfelder (Attribute) ist dies allerdings erforderlich, Sie sollten deshalb mit Template-Anpassungen zumindest ansatzweise vertraut sein.