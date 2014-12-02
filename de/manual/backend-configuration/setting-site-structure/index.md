# Anlegen der Seitenstruktur

In jedem Shop unabhängig von der Grösse und Produktart werden mindestens diese Seiten für das System benötigt:

* Produktübersicht (Produktliste)
* Produktdetails (Produktleser)
* Warenkorb
* Rechtliche Informationen (z. B. Zahlung und Versand)
* Kasse 
* Bestellung abgeschlossen

<docrobot_new_in_version version="2.0"><p>Neu können die Module `Produktliste` und `Produktleser` auf einer Seite untergebracht werden.</p></docrobot_new_in_version>

<docrobot_message type="warning"><p>Beim Anlegen des Modules `Produktliste` bei den Template-Einstellungen **Ausblenden bei Produktansicht** markieren, damit die Liste in der Detailansicht nicht angezeigt wird.</p></docrobot_message>


Wenn für die Bestellungen ein Zugriffsschutz bestehen soll, werden zusätzlich diese Seiten für die Mitglieder benötigt.

* Registrierung
* Registrierung erfolgreich
* Mein Account
* Bestellhistorie
* Bestelldetails
* Passwort vergessen
* Logout

Weiterhin ist in Shops oft eine Suchfunktion vorhanden. Dafür wird die Suchergebnisse-Seite benötigt.


**Übersicht der in diese Seiten zu integrierende Module**

<table>
<thead>
<tr>
	<th>Seitenname</th>
	<th>Modul</th>
	<th>Bemerkungen</th>
</tr>
</thead>
<tbody>
<tr>
	<td>Produktübersicht<br>Produktdetails</td>
	<td><docrobot_route name="product-list">Produktliste</docrobot_route> (Isotope)<br><docrobot_route name="product-reader">Produktleser</docrobot_route> (Isotope)</td>
	<td></td>
</tr>
<tr>
	<td>Warenkorb</td>
	<td><docrobot_route name="shopping-cart">Warenkorb</docrobot_route> (Isotope)</td>
	<td></td>
</tr>
<tr>
	<td>Rechtliche Informationen<br>(z.B Zahlung und Versand)</td>
	<td>Inhaltselemente <code>Text</code> (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Kasse</td>
	<td><docrobot_route name="checkout">Kasse</docrobot_route> (Isotope)</td>
	<td></td>
</tr>
<tr>
	<td>Bestellung abgeschlossen</td>
	<td><docrobot_route name="order-details">Bestellungsdetails</docrobot_route> (Isotope)<br>Inhaltselemente <code>Text</code> (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Registrierung</td>
	<td>Registrierung (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Registrierung erfolgreich</td>
	<td>Inhaltselemente <code>Text</code> (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Mein Account</td>
	<td>Persönliche Daten (Contao)<br><docrobot_route name="order-history">Vergangene Bestellungen</docrobot_route> (Isotope)<br>Konto schliessen (Contao)</td>
	<td>Die Module können in Accordion-Sektionen eingeschlossen werden.</td>
</tr>
<tr>
	<td>Bestellhistorie</td>
	<td><docrobot_route name="order-history">Vergangene Bestellungen</docrobot_route> (Isotope)</td>
	<td>Wenn das Modul schon auf der "Mein Account"-Seite ist, kann die separate Seite "Bestellhistorie" auch weggelassen werden.</td>
</tr>
<tr>
	<td>Bestelldetails</td>
	<td><docrobot_route name="order-details">Bestellungsdetails</docrobot_route> (Isotope)</td>
	<td></td>
</tr>
<tr>
	<td>Passwort vergessen</td>
	<td>Passwort vergessen (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Logout</td>
	<td>Automatischer Logout (Contao)</td>
	<td></td>
</tr>
<tr>
	<td>Suchergebnisse</td>
	<td>Suchmaschine (Contao)
</td>
	<td></td>
</tr>
</tbody>
</table>