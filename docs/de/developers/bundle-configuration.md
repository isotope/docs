# Bundle-Konfiguration

Die meisten Shopeinstellungen gehören ins Contao-Backend. Die Bundle-Konfiguration richtet sich an die technische Betreuung und liegt in der Symfony-Konfiguration des Contao-Projekts.

Das dokumentierte Bundle definiert den Wurzelschlüssel `isotope` mit `cart_timeout` und `currency_formats`. Kopiere keinen vermuteten Konfigurationsbaum aus einer anderen Isotope-Version.

## Aufbewahrung von Gastwarenkörben

In `config/config.yaml` der Anwendung:

```yaml
isotope:
    cart_timeout: '30 days'
```

Der Standard ist `30 days`. Der Wert muss ein vom PHP-Datumsparser akzeptierter Zeitausdruck sein. Bevorzuge eine gewöhnliche positive Dauer wie `14 days` oder `30 days`.

Die tägliche Bereinigung entfernt abgelaufene Gastwarenkörbe und Warenkörbe gelöschter Mitglieder. Warenkörbe vorhandener Mitglieder unterliegen nicht der Gastablaufbedingung. Diese Einstellung definiert keine Aufbewahrung von Bestellungen oder Dokumenten.

Prüfe, ob geplante Contao-Aufgaben laufen. Eine geänderte Dauer führt nicht sofort eine Bereinigung aus.

## Währungsformate

Ein benanntes Format definiert Dezimalstellen und Trennzeichen. Zum Beispiel:

```yaml
isotope:
    currency_formats:
        '10,000.00':
            decimals: 2
            decimal_separator: '.'
            thousands_separator: ','
        '10.000,00':
            decimals: 2
            decimal_separator: ','
            thousands_separator: '.'
```

Behandle eine eigene Zuordnung als die gewünschte Menge verfügbarer Formate und prüfe die aufgelöste Konfiguration. Die Standardwerte des Bundles umfassen Formate ohne Gruppierung mit Dezimalpunkt sowie mit Kommagruppierung, Dezimalkomma und Apostrophgruppierung.

Formatierung ist von Währungsauswahl, Umrechnungsfaktoren, Steuerberechnung und Rundungsrichtlinie getrennt. Wähle und teste nach Definitionsänderungen das gewünschte Format in der Shopkonfiguration.

## Änderungen validieren

Verwende in der Zielanwendung die Befehle zur Konfigurationsprüfung und YAML-Validierung:

```bash
php vendor/bin/contao-console lint:yaml config
php vendor/bin/contao-console debug:config isotope
php vendor/bin/contao-console cache:clear --env=prod
```

Prüfe die aufgelösten Werte und teste einen neuen Warenkorb und die Preisanzeige. Die Befehle benötigen eine vollständige Contao-Installation, nicht nur den Core-Quellcode.

Quelle: [Konfigurationsdefinition des IsotopeBundle](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php).
