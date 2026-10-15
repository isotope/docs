# Isotope installieren

**Du benötigst:** Zugriff auf Contao Manager und eine kompatible Contao-Website. Wenn jemand deine Website betreut, lass diese Person die folgenden Hostingprüfungen durchführen.

**Das Ergebnis:** Die Verwaltungswerkzeuge von Isotope stehen im Contao-Backend zur Verfügung. Im nächsten Kapitel erstellst du dein erstes Produkt und die Seiten für den Bestellvorgang.

## 1. Bereitschaft der Website prüfen

Dieses Handbuch behandelt Isotope 3 mit PHP ab 8.3 innerhalb von PHP 8 und Contao ab 5.7.4 innerhalb von Contao 5. Die Hostingumgebung muss auch die Anforderungen von Contao erfüllen und die PHP-Erweiterung DOM bereitstellen. Deine technische Betreuung kann die [technischen Installationsanforderungen](../developers/installation.md) prüfen.

Wenn du Contao noch nicht hast, folge der offiziellen [Contao-Installationsanleitung](https://docs.contao.org/5.x/manual/de/installation/contao-installieren/). Wähle eine Version, die die genannten Anforderungen erfüllt. Bevor du Isotope hinzufügst, solltest du dich im Backend anmelden und eine veröffentlichte Seite öffnen können.

Sichere bei einer bestehenden Contao-Website Dateien und Datenbank, bevor du Software hinzufügst. Wenn du einen bestehenden Isotope-Shop aktualisierst, lass deine technische Betreuung die [Updateanleitung](../developers/upgrading.md) zunächst an einer Kopie durcharbeiten.

## 2. Isotope mit Contao Manager hinzufügen

1. Öffne Contao Manager für deine Website. Er ist vom Backend zur Seitenbearbeitung getrennt.
2. Suche im Paketbereich nach **`isotope/isotope-core`**.
3. Füge das Paket hinzu und prüfe, dass die gewählte Version zu Isotope 3 gehört, das dieses Handbuch beschreibt.
4. Wende die Paketänderungen an und warte auf den Abschluss der Installation.
5. Führe das von Contao Manager angebotene Datenbankupdate aus und prüfe die vorgeschlagenen Änderungen.
6. Kehre ins Contao-Backend zurück und melde dich als Administrator an.

Contao Manager installiert auch die benötigten weiteren Pakete. Eines davon ist Notification Center, das du später für Bestell-E-Mails verwendest.

Falls die benötigte Version nicht verfügbar ist oder Manager einen Versionskonflikt meldet, bewahre die Meldung auf und lass den Konflikt von deiner technischen Betreuung lösen. Wähle keine ältere Hauptversion in der Erwartung, dass diese Anleitung dazu passt.

## 3. Ergebnis prüfen

Suche im Backend nach **Isotope eCommerce**. Du solltest diese Bereiche sehen:

| Bereich | deine Aufgaben dort |
| --- | --- |
| Produkte | Das Trail-T-Shirt anlegen und später den Katalog verwalten |
| Bestellungen | Käufe finden und bearbeiten |
| Regeln | Bedingungen für Preise, Steuern und Auswahlmöglichkeiten an der Kasse festlegen |
| Konfiguration | Produkttypen, Steuern, Versand und Zahlung einrichten |

Öffne **Konfiguration** und prüfe, ob der Bereich lädt. Öffne außerdem eine bestehende Seite der öffentlichen Website, um deren Funktion zu prüfen.

Wenn ein anderes Mitarbeiterkonto Isotope nicht sieht, der Administrator aber schon, prüfe die [Mitarbeiterberechtigungen](../setup/general/access.md). Behebe ein fehlgeschlagenes Datenbankupdate, bevor du Shopdatensätze anlegst.

## 4. Deinen ersten Shop erstellen

Die Installation stellt die Shopwerkzeuge bereit. Jetzt ergänzt du Produkt, Preise, Liefermöglichkeiten und Kundenseiten.

Fahre direkt mit **[Dein erster Shop](first-shop.md)** fort. Das Kapitel verwendet das Trail-T-Shirt aus [Unser Beispielshop](../concepts/example-shop.md) und führt durch einen vollständigen Testkauf.

Für eine Installation über die Kommandozeile gibt es die separate [Entwickleranleitung](../developers/installation.md).
