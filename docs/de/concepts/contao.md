# Contao-Grundlagen für Shopbetreiber

Contao ist das Websitesystem rund um deinen Shop. Du musst kein Entwickler werden, aber einige Konzepte erklären, wo Isotope hingehört.

## Seiten, Artikel und Inhaltselemente

Die **Seitenstruktur** ist der Seitenbaum der Website. Ein Startpunkt kennzeichnet eine Website und ihre Spracheinstellungen. Reguläre Seiten enthalten Inhalte wie Startseite, T-Shirts, Warenkorb und Kasse.

Ein **Artikel** bündelt Inhalte auf einer Seite. Ein **Inhaltselement** ist ein Block innerhalb eines Artikels, etwa Text, ein Bild oder eine Isotope-Produktliste. In Isotope 3 sind Shopfunktionen Inhaltselemente. Ältere Anleitungen, die Isotope-Frontend-Module erstellen lassen, beschreiben eine frühere Architektur.

Ein **Theme** und ein **Seitenlayout** steuern Darstellung und Bereiche der Website. Das Anlegen von Produkten fügt nicht automatisch eine Produktliste zu einer Seite hinzu. Katalogdaten und Seiteninhalte werden beide benötigt.

## Warum Kategorien Seiten sind

Isotope verwendet Contao-Seiten als Produktkategorien. Du könntest Shop → T-Shirts und Shop → Hoodies anlegen. Weise das Trail-T-Shirt T-Shirts und den Trail-Hoodie Hoodies zu. Ein Produkt kann mehreren Seiten angehören.

Dadurch verwenden Kategorien die normale Navigation und Seiteninhalte. Du kannst einen Einleitungstext über einer Produktliste platzieren, ohne ein zweites Navigationssystem zu pflegen.

Der **Kategorieumfang** der Produktliste bestimmt, welche zugewiesenen Produkte sie liest. „Aktuelle Kategorie“ liest nur die aktuelle Seite. Ein Umfang mit Unterseiten liest auch die ausgewählten untergeordneten Seiten. Ein veröffentlichtes Produkt auf einer anderen Seite erscheint nicht automatisch in der aktuellen Kategorie.

## Mitarbeiter und Kunden

**Benutzer** arbeiten im Backend. Gib Produktredakteuren, Bestellbearbeitern und Administratoren Berechtigungen passend zu ihren Aufgaben.

**Mitglieder** verwenden das Frontend. Isotope kann diese Konten für Bestellungen, gespeicherte Adressen und den Bestellverlauf nutzen. Mitgliedergruppen können auch geschützte Produkte oder Preisbedingungen steuern.

Registrierung, Anmeldung und Passwortwiederherstellung gehören zur allgemeinen Contao-Websiteeinrichtung. Die Auswahl der Mitgliederbestellung gestaltet diese Seiten nicht automatisch.

## Veröffentlichung und Zugriff

Sowohl Contao-Seiten als auch Isotope-Produkte können unveröffentlicht oder geschützt sein. Prüfe bei einem fehlenden Produkt die gesamte Kette: Startpunkt, Seite, Artikel, Element, Produkt und relevante Mitgliederberechtigungen.

Die Vorschau ist beim Bearbeiten hilfreich. Teste abschließend auch abgemeldet über die öffentliche URL.

## Mit den ersten Schritten fortfahren

Als Nächstes: [So funktioniert ein Shop](shop.md), dann [Unser Beispielshop](example-shop.md). Die Shopoberfläche richtest du nach der Installation ein.

## Referenz für die spätere Einrichtung

- [Produkte anzeigen](../setup/frontend/products.md) verbindet Kategorien mit Listen und Lesern.
- [Kasse](../setup/frontend/checkout.md) verbindet Warenkorb und Bestellseiten.
- [Mitglieder und Gäste](../setup/frontend/customers.md) erklärt Kundenkonten.
- Das [Contao-Handbuch](https://docs.contao.org/5.x/manual/de/) behandelt das CMS selbst.
