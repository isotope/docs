# Integritätscheck

<docrobot_new_in_version version="2.2"><p>Dieses Feature ist neu in Isotope eCommerce 2.2</p></docrobot_new_in_version>

<docrobot_image path="backend-configuration/store-configuration/miscellaneous/integrity-check/integritaetscheck.png" alt="Screenshot des Integritätschecks">

Der Integritätscheck versucht Ungereimtheiten in der Datenbank zu eruieren und bietet wenn möglich auch die Option das Problem automatisiert zu beheben. Ein Beispiel wäre die Konfiguration eines Produkttyps mit Varianten, welcher später wieder auf "variantenlos" umgestellt wird. Dies ergibt überflüssige Varianten in der Datenbank, welche der Integritätscheck erkennt und auf Klick bereinigt.