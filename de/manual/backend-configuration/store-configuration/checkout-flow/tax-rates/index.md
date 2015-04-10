# Steuersätze

Für eine Shop-Konfiguration muss mindestens ein Steuersatz vorhanden sein.

  Klicke auf "Neuer Steuersatz" und fülle einfach die Pflichtfelder **Steuersatz-Name**, "Steuersatz" und "Adressbasis für die Berechnung" aus. **Adressbasis für die Berechnung** klingt erstmal seltsam. Steuersätze können von Land zu Land oder Staat zu Staat unterschiedlich sein. Daher wird hier ausgewählt ob die Rechnungs- oder Lieferadresse als Referenz bevorzugt werden soll, oder ob beide Adressen miteinbezogen werden sollen. 

<docrobot_new_in_version version="2.3">
	<p>Dieses Feature ist neu in Isotope eCommerce 2.3</p>
	<p>Neu kann die USt-IdNr. geprüft werden, falls diese gültig ist kann durch auswählen der entsprechenden Option im Steuersatz verhindert werden, dass die Steuer angewendet wird.</p>
</docrobot_new_in_version>

 Die **Steuersatz-Bezeichnung** wird anstelle des Steuersatz-Namens im Frontend beim Bestellprozess angezeigt.


## Beispiel:

Für den Verkauf in Deutschland kommen zwei Steuersätze in Frage, der normale und der ermässigte (für z. B. Lebensmittel, Bücher, Zeitschriften).

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-rates/steuersaetze_normal.jpg" alt="Normaler Steuersatz">

<docrobot_image path="backend-configuration/store-configuration/checkout-flow/tax-rates/steuersaetze_ermaessigt.jpg" alt="Ermässigter Steuersatz">
