# Performance

Isotope eCommerce wurde mit dem Ziel der vollen Flexibilität gebaut. Flexibilität bedeutet zwar unbegrenzte Möglichkeiten, allerdings geht Flexibilität auch zu Lasten von Performance.

Dieses Kapitel zeigt dir, was du machen kannst um deinen Webshop zu beschleunigen.

## Server

Meistens geht dieser Aspekt verloren. Performance ist nicht alleine die Aufgabe von Isotope eCommerce oder Contao sondern auch zu einem grossen Teil von der Server-Umgebung.

1. **Webhosting:** Wer billig kauft, kriegt billig. Ein gutes Webhosting ist die Basis für einen gut funktionierenden Webshop. Ein Webhosting für € 1,- im Monat ist also mit sehr grosser Wahrscheinlichkeit nicht die richtige Grundlage für Isotope eCommerce.
2. **Safe Mode Hack:** Benötigst du den Safe Mode Hack, dann heisst das PHP hat keine Rechte, Dateien auf dem Server zu schreiben und muss deshalb den (langsamen) Umweg über das FTP-Login nehmen. In einfachen Worten: Dein Server ist falsch konfiguriert. Du bist besser bedient, wenn du es gar nicht erst versuchst und du solltest dir Punkt 1 noch einmal zu Gemüte führen.
3. **Datenbank:** Wenn die Schnittstelle zu deiner Datenbank langsam ist, bedeutet das, jede einzelne Abfrage der Datenbank ist langsam. Du kannst dir vorstellen, dass Isotope durch die Flexibilität ziemlich viele Anfragen an die Datenbank stellen muss und wenn bei 100 Anfragen jede einzelne zwei Millisekunden mehr kostet als bei einer guten Anbindung, verspielst du bei jedem Aufruf bereits zwei Zehntelsekunden.
4. **PHP-Version:** Die PHP-Entwickler versorgen uns laufend mit neuen Versionen. Selbstverständlich haben auch Sie ein Auge auf Performance und Speicherverbrauch. Du solltest deshalb wenn möglich immer auf der neusten, verfügbaren Version arbeiten auch wenn Isotope bzw. Contao auf einer tieferen Version ebenfalls funktionieren würden. Die Unterschiede sind zum Teil gravierend.


## Isotope eCommerce

1. **Der interne Cache**: Wenn der interne Cache nicht aufgebaut ist bzw. in den Einstellungen `Internen Cache umgehen` angehakt ist, wird die Ladezeit der gesamten Webseite sofort exponentiell anspringen. Wenn du also Perfromance-Testing betreiben willst, muss der interne Cache immer aktiviert sein!
2. **Der Debugmodus**: Der Debugmodus ist praktisch während der Entwicklung von Contao-Erweiterungen. Allerdings werden dann auch sämtliche Isotope eCommerce-internen Caches umgangen und eine Menge Zeit geht für die Debugging-Ausgabe drauf.
3. **Die Frontend-Vorschau mit unveröffentlichten Elementen**: Durch Optimierung von Abfragen an die Datenbank (Stichwort: SQL-Keys) kann die Geschwindigkeit jener beschleunigt werden. Wenn du die Frontend-Vorschau nutzt und `unveröffentlichte Elemente anzeigen` aktiviert hast, ändern sich die Abfragen leicht und die Optimierungen greifen nicht mehr. Performance-Testing also niemals mit aktivierter Frontend-Vorschau.
4. **Regeln:** Regeln sind praktisch, aber sie können sehr komplex werden. Sie kosten dementsprechend Zeit. Brauchst du die Regeln nicht, solltest du deshalb `isotope_rules` in den Systemeinstellungen deaktivieren!
5. **Preisberechnung:** In Isotope eCommerce können Produktpreise zur Laufzeit dynamisch verändert werden. Beispiele dafür sind etwa zeitlich beschränkte Rabatte oder Rabatte für bestimmte Mitglieder. Es ist deshalb nicht möglich, die Preise bereits auf Datenbank-Ebene zu filtern bzw. sortieren. Wenn möglich solltest du also für eine "Sortieren nach Preis"-Funktion bzw. "Filtern nach Preis"-Funktion in der Produktliste dafür sorgen, dass immer nur eine überschaubare Anzahl an Produkten gefiltert bzw. sortiert werden müssen.


<docrobot_message type="info">Mit entsprechendem Budget und dem/der Entwickler(in) deines Vertrauen lassen sich selbstverständlich auch immer kundenspezifische Performance-Analysen und -Optimierungen vornehmen.</docrobot_message>
