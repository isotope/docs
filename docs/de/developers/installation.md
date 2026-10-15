# Technische Installation

Dieses Kapitel richtet sich an die technische Betreuung der Contao-Anwendung. Shopbetreiber können die [Installation mit Contao Manager](../getting-started/installation.md) verwenden.

## Anforderungen

Die dokumentierte Isotope-3-Revision gibt Folgendes vor:

| Komponente | Versionsvorgabe |
| --- | --- |
| PHP | `^8.3` |
| Contao Core Bundle | `^5.7.4` |
| Composer Runtime API | `^2` |
| PHP-Erweiterung DOM | Erforderlich |

Contao und weitere Abhängigkeiten ergänzen Hostinganforderungen. Prüfe den aufgelösten Paketsatz, statt diese wenigen Vorgaben als vollständige Plattformprüfung zu behandeln. Die Core-CI testet PHP 8.3, 8.4 und 8.5 mit Contao 5.7.

Quelle: [Paketanforderungen](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/composer.json).

## In der Anwendung installieren

Führe im Contao-Projektverzeichnis mit `composer.json` aus:

```bash
composer require isotope/isotope-core
php vendor/bin/contao-console contao:migrate
```

Der Paketname ohne Versionsangabe löst die vom Projekt erlaubte Version auf. Prüfe, ob das gewünschte Isotope-3-Release gewählt wird. Verwende beim Zielen auf ein bestimmtes Release die vereinbarte Versionsvorgabe des Projekts. Lockere nicht projektweite Stabilitätseinstellungen nur zur Installation eines Entwicklungsstands.

Prüfe Migrationsabfragen und bewahre bei bestehenden Anwendungen eine wiederherstellbare Sicherung auf. Ignoriere keine Plattformanforderungen, um Abhängigkeitskonflikte zu umgehen.

Übe bei einem bestehenden Isotope-Shop das [Update](upgrading.md) und prüfe historische Datensätze vor Produktionsänderungen.

## An den Shopbetreiber übergeben

Prüfe, ob ein Administrator die Isotope-Konfiguration öffnen kann, normale Contao-Seiten weiter laden und Datenbankupdates abgeschlossen sind. Vergib die vorgesehenen [Mitarbeiterberechtigungen](../setup/general/access.md).

Gib Backend- und Testwebsiteadressen sowie installierte Version weiter. Der Shopbetreiber kann dann mit [Dein erster Shop](../getting-started/first-shop.md) fortfahren. Bewahre Anbieterzugangsdaten und Deploymentverfahren in den geeigneten geschützten Projektunterlagen auf.
