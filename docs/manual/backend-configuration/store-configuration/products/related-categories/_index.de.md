---
title: Verknüpfte Kategorien
---

`Verknüpfte Kategorien` werden ausschliesslich im Zusammenhang mit dem Modul <docrobot_route name="related-products">Ähnliche Produkte</docrobot_route> verwendet.

Sie bildet die Basis für die von vielen Webshops bekannte Funktion für Dinge wie

* "Kunden die dieses Produkt gekauft haben, kauften auch"
* Zubehör zu diesem Produkt
* etc.

Eine `verknüpfte Kategorie` ist aber nicht für jedes Produkt immer gleich.
Nehmen wir als Beispiel die "Zubehör"-Funktion. Für Produkt A ist das Zubehör die Produkte X und Y, aber für Produkt B sind es Produkte K und L.

Deshalb wird die Zuordnung für die Kategorien im Produkt selbst vorgenommen.
Sobald du **mindestens eine** `verknüpfte Kategorie` angelegt hast, kannst du bei den <docrobot_route name="product-management">Produkten selbst</docrobot_route>, die Verknüpfungen vornehmen.

## Vorgehen beim Einrichten von ähnlichen Produkten

1. Isotope eCommerce > Shop-Konfiguration > <docrobot_route name="related-categories">Verknüpfte Kategorien</docrobot_route>  
`Neue Kategorie` mit dem Namen `Related` anlegen.  
![Neue Kategorie anlegen](kategorie_anlegen.png)
3. Isotope eCommerce > <docrobot_route name="product-management">Produkte</docrobot_route>  
Zuerst musst du IDs der ähnlichen Produkte herausfinden, fahre dafür über das blaue Icon (![Sitemap-Icon](../../../../images/sitemap.png)). Danach auf `Kategorie hinzufügen`, wähle die Kategorie `Related` aus und füge die Produkte-IDs unter `Produkte` ein.  
![Produkte-IDs hinzufügen](kategorie_hinzufuegen.png)
4. Module > <docrobot_route name="related-products">Ähnliche Produkte</docrobot_route>  
Modul anlegen und unter Modul-Konfiguration `Related` auswählen.  
![Modul Ähnliche Produkte anlegen](modul_anlegen.png)
5. Inhalte > Artikel  
Jetzt das angelegte Modul im Artikel mit <docrobot_route name="product-list">Produktliste</docrobot_route> und <docrobot_route name="product-reader">Produktleser</docrobot_route> platzieren.  
![Angelegtes Modul platzieren](angelegtes_modul.png)
