# Performance

Ein schneller Katalog erleichtert das Stöbern. Die Kasse muss auch bei wechselndem Kundenkontext korrekt bleiben. Miss Performance, ohne benötigtes Einkaufsverhalten zu entfernen.

## Mit Nachweisen beginnen

Identifiziere die langsame Seite und erfasse Produktanzahl, Filter, Variantenkomplexität, Bildgrößen und Anmeldestatus. Vergleiche eine einfache und eine große Kategorie, einen Produktleser und die Kasse.

Lass die technische Betreuung Serverzeit und Abfragen in einer Testumgebung messen. Ein langsamer Bilddownload und eine langsame Datenbankabfrage benötigen unterschiedliche Lösungen.

## Produktlisten gezielt halten

Verwende Seitennavigation, statt einen großen Katalog auf einer Seite zu rendern. Wähle einen zur Seite passenden Kategorieumfang. Lade nicht alle Nachfahren, wenn eine Startseite nur eine kleine Auswahl benötigt.

Zeigt eine Liste keine Produktoptionen, aktiviere **Produktoptionen deaktivieren**. Diese Elementeinstellung vermeidet ausdrücklich die Erzeugung von Optionswidgets und das Laden von Varianten dafür. Lass Optionen aktiv, wenn Kunden direkt in der Liste auswählen müssen.

Beschränke Frontendfilter und Suchfelder auf nützliche Auswahlmöglichkeiten. Ein Dutzend selten genutzter Filter kann Komplexität erzeugen, ohne Kunden zu helfen.

## Geeignete Bilder verwenden

Konfiguriere getrennte Galeriegrößen für Liste und Leser. Kleine Listenkarten sollten keine unnötig großen Originale laden. Prüfe nach Größenänderungen Beschnitt und Schärfe auf echten Geräten.

Prüfe Produkte mit vielen Bildern und Varianten. Eine Galerie sollte nützliche Details liefern, ohne die Anfangsseite schwer zu machen.

## Kundenspezifisches Verhalten erhalten

Preise und Methodenverfügbarkeit können von Mitgliedergruppen, Adressen, Währung, Warenkorbinhalt und Regeln abhängen. Lege Warenkorb, Kasse, Bestelldetails und Mitgliederdaten nicht in einen gemeinsamen statischen Cache.

Lass bei Einführung eines Reverse-Proxys oder anderen Caches die technische Betreuung Contaos Cache-/Sitzungsverhalten prüfen und zwei unabhängige Kundensitzungen testen. Eine Sitzung darf niemals Warenkorb oder persönliche Daten der anderen erhalten.

## Geplante Wartung funktionsfähig halten

Der Core registriert eine tägliche Aufgabe für alte Gastwarenkörbe und Warenkörbe gelöschter Mitglieder. Der Gastablauf beträgt standardmäßig 30 Tage. Prüfe, ob Contaos geplante Aufgaben tatsächlich laufen, statt anzunehmen, dass die Ablaufzeit allein Datensätze entfernt.

Die Einstellung erklärt [Bundle-Konfiguration](bundle-configuration.md).

## Funktion erneut prüfen

Teste nach Optimierungen Varianten, Kundenoptionen, Such-/Filterkombinationen, bedingte Preise und Kasse. Eine schnellere Seite, die eine benötigte Option verliert oder einen falschen Preis zeigt, ist keine abgeschlossene Verbesserung.
