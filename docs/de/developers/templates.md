# Twig-Templates

Isotope 3 verwendet Twig. Seine Shopfunktionen sind Contao-Inhaltselemente. Produkt- und Collection-Rendering sind in wiederverwendbare Templates und Komponenten aufgeteilt.

## Die richtige Ebene finden

Ein Produktlisten-Inhaltselement steuert den Listencontainer. Das Produktlisten-/Leser-Template steuert ein einzelnes Produkt. Galerie- und Preiskomponenten rendern kleinere Teile.

Prüfe vor Templateänderungen den gewählten Produkttyp und Inhaltselementüberschreibungen. Die Änderung eines Leser-Templates verändert nicht zwingend eine Listenkarte mit anderem Template.

Die Quellcodestandards enthalten `isotope/product/list` und `isotope/product/reader`. Das gemeinsame `isotope/product.html.twig` enthält Blöcke für Bilder, Optionen, Preis, Menge und Aktionen.

## Einen kleinen Block erweitern

Erstelle mit Contaos Twig-Anpassungsmechanismus eine auswählbare Variante. Eine Produktleservariante kann den Core-Leser erweitern und dessen Preisausgabe beibehalten:

```twig
{% extends '@Contao/isotope/product/reader.html.twig' %}

{% block product_price %}
    {{ parent() }}
    <p class="delivery-information">Die Liefermöglichkeiten werden an der Kasse angezeigt.</p>
{% endblock %}
```

Speichere die Variante in der Templatestruktur der Anwendung, wähle sie als Leser-Template für den vorgesehenen Produkttyp bzw. das Element und baue bei Bedarf den Anwendungscache neu auf. Ersetze bei mehrsprachigen Websites den festen Satz durch eine passende Übersetzung.

Dieses Beispiel ergänzt nur die Darstellung. Es berechnet keine Lieferkosten und ändert keinen Produktpreis.

## Funktionales Markup erhalten

Das Standardprodukttemplate enthält Formularkennungen, Request-Tokens, Aktionsrendering und Stimulus-Datenattribute. Das Entfernen dieser Bestandteile kann Optionsaktualisierungen oder das Hinzufügen zum Warenkorb beschädigen, selbst wenn die Seite korrekt aussieht.

Überschreibe vorzugsweise kleine Blöcke und rufe `parent()` auf, wenn du Verhalten bewahren musst. Lass Escaping für Kundeneingaben aktiv. Verwende `raw` nicht bloß zur Unterdrückung unerwünschten Escapings, ohne die Herkunft des Werts zu verstehen.

## Den berechneten Preis verwenden

Core-Templates verwenden Helfer wie `isotope_price(product)`, `isotope_baseprice(product)` und `isotope_gallery(product, 'images')`.

Gib keinen unverarbeiteten Datenbankpreis als Zahlbetrag aus. Das kann Steuern, Varianten, Mengenstaffeln, Regeln, Währungsfaktoren und Formatierung umgehen.

## Eigene Ausgabe prüfen

Prüfe Produktlisten, Leser, Varianten, Validierungsfehler, fehlende Bilder, lange Bezeichnungen und mobile Layouts. Lege nach Darstellungsänderungen das Produkt in den Warenkorb und gib eine Bestellung auf. Teste Standard- und mitgliederspezifische Preiskontexte.

Prüfe für Dokumente und Benachrichtigungen deren separate Templates und verfügbaren Kontext. Variablen eines Produktlesers stehen nicht automatisch im Dokumenttext zur Verfügung.

Quelle: [Gemeinsames Produkttemplate](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/templates/isotope/product.html.twig).
