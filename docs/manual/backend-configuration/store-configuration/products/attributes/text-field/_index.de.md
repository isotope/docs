---
title: "Textfeld"
description: "Die Shop-Konfiguration - Textfeld."
aliases:
    - /de/backend-konfiguration-shop-Attribute-Textfeld/
weight: 100    
---


## Attribut-Name & -Typ

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Standardeinstellung</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Durch den Kunden auswählbar</td>
            <td>-</td>
            <td>Dieses Feld musst du auswählen, falls der Kunde im Frontend die Möglichkeit haben sollte, eine Eingabe zu tätigen.</td>
        </tr>
    </tbody>
</table>


## Beschreibung

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Standardeinstellung</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Beschreibung</td>
            <td>-</td>
            <td>Dieses Beschreibung dient dem Backend-Nutzer als Hinweis und wird unter dem Eingabefeld ausgegeben.</td>
        </tr>
    </tbody>
</table>


## Attribut-Konfiguration

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Standardeinstellung</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
           <td>Mindestlänge</td>
           <td>0</td>
           <td>{{< version-tag "2.2" >}} Hier kannst du eine minimale Zeichenzahl erforderlich machen.</td>
       </tr>
       <tr>
           <td>Maximallänge</td>
           <td>0</td>
           <td>Hier kannst du die Feldlänge auf eine bestimmte Zeichenzahl beschränken.</td>
       </tr>
        <tr>
            <td>Eingabeprüfung</td>
            <td>-</td>
            <td>Die einzelnen Option entnimmst du der folgenden Tabelle <code>Eingabeprüfung</code>.</td>
        </tr>
        <tr>
            <td>Platzhalter</td>
            <td>-</td>
            <td>{{< version-tag "2.2" >}} Hier kannst du einen HTML5-Platzhalter für das Feld definieren.</td>
        </tr>
        <tr>
            <td>Pflichtfeld</td>
            <td>-</td>
            <td>Falls <code>Durch den Kunden auswählbar</code> ausgewählt ist kann das Produkt ohne die Angabe nicht in den Warenkorb gelegt werden. Ansonsten wird das Feld beim Anlegen eines Produktes als Pflichtfeld im Backend ausgegeben.</td>
        </tr>
        <tr>
            <td>Mehrsprachig</td>
            <td>-</td>
            <td>Macht das Textfeld bei einer mehrsprachigen Webseite im Backend übersetzbar.</td>
        </tr>
        <tr>
            <td>Datumsauswahl</td>
            <td>-</td>
            <td>Fügt dem Textfeld im Backend oder Frontend eine Datumsauswahl (<img src="/de/images/datepicker.gif?classes=icon">) hinzu.</td>
        </tr>
    </tbody>
</table>


### Eingabeprüfung

<table>
	<thead>
		<tr>
			<th>Eingabeprüfung</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Numerische Zeichen</td>
			<td>Erlaubt numerische Zeichen, Minus (-), Punkt (.) und Leerzeichen ( ).</td>
		</tr>
		<tr>
			<td>Alphabetische Zeichen</td>
			<td>Erlaubt alphabetische Zeichen, Minus (-), Punkt (.) und Leerzeichen ( ).</td>
		</tr>
		<tr>
			<td>Alphanumerische Zeichen</td>
			<td>Erlaubt alphanumerische Zeichen, Minus (-), Punkt (.) und Leerzeichen ( ).</td>
		</tr>
		<tr>
			<td>Erweiterte alphanumerische Zeichen</td>
			<td>Erlaubt alles außer Spezialzeichen die normalerweise aus Sicherheitsgründen kodiert werden (#/()&lt;=&gt;).</td>
		</tr>
		<tr>
			<td>Datum</td>
			<td>Prüft ob die Eingabe dem globalen Datumsformat entspricht.</td>
		</tr>
		<tr>
			<td>Zeit</td>
			<td>Prüft ob die Eingabe dem globalen Zeitformat entspricht.</td>
		</tr>
		<tr>
			<td>Datum und Zeit</td>
			<td>Prüft ob die Eingabe dem globalen Datums- und Zeitformat entspricht.</td>
		</tr>
		<tr>
			<td>Telefonnummer</td>
			<td>Erlaubt numerische Zeichen, Plus (+), Minus (-), Querstrich (/), Klammerzeichen () und Leerzeichen ( ).</td>
		</tr>
		<tr>
			<td>E-Mail-Adresse</td>
			<td>Prüft ob die Eingabe eine gültige E-Mail-Adresse ist.</td>
		</tr>
		<tr>
			<td>URL-Format</td>
			<td>Prüft ob die Eingabe eine gültige URL ist.</td>
		</tr>
		<tr>
			<td>Preis</td>
			<td>Prüft ob die Eingabe ein gültiger Preis ist.</td>
		</tr>
		<tr>
			<td>Ermäßigung</td>
			<td>Prüft ob die Eingabe eine gültige Ermäßigung ist.<br>Beispiel: -10%, -10, +10, +10%</td>
		</tr>
		<tr>
			<td>Preisaufschlag</td>
			<td>Prüft ob die Eingabe ein gültiger Preisaufschlag ist.<br>Beispiel: 10.00, 10%</td>
		</tr>
	</tbody>
</table>


## Suche- & Filter-Einstellungen

<table>
    <thead>
        <tr>
            <th>Einstellung</th>
            <th>Standardeinstellung</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Durchsuchbar im Frontend</td>
            <td>-</td>
            <td>Macht das Feld, falls es im Backend gepflegt wurde, für die Suchmaschine durchsuchbar.</td>
        </tr>
        <tr>
            <td>Zur "Sortieren nach"-Optionsliste hinzufügen</td>
            <td>-</td>
            <td>Macht das Feld, falls es im Backend gepflegt wurde und für den Kunden sichtbar ist, im Listenmodul sortierbar.</td>
        </tr>
        <tr>
            <td>Durchsuchbar im Backend</td>
            <td>-</td>
            <td>Die Backend-Suchfunktion durchsucht dieses Feld nach Suchbegriffen.</td>
        </tr>
        <tr>
            <td>Filterbar im Backend</td>
            <td>-</td>
            <td>Macht, dass das Feld im Backend als Filter genutzt werden kann.</td>
        </tr>
    </tbody>
</table>

Die Ausgabe des angelegten Attributs im Backend erfolgt über die [Produkttypen](/de/backend-konfiguration-shop-Produkttypen/). Wenn du das Textfeld `Durch den Kunden auswählbar` gemacht hast wird es automatisch im Frontend (mittels `$this->options` im Template) angezeigt. Andernfalls kannst du im gewünschten Isotope-Template das Attribut mit folgendem Code `<?php echo $this->generateAttribute('InternerName'); ?>` ausgeben.
