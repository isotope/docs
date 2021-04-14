---
title: "Warenkorb"
description: "Regeln & Gutscheine für Warenkorb."
aliases:
    - /de/backend-regeln-warenkorb/
weight: 20    
---


## Basis-Regeleinstellungen

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
            <td>Typ</td>
            <td>Warenkorb</td>
            <td>Du hast <code>Warenkorb</code> gewählt um eine Regel anzulegen.</td>
        </tr>
        <tr>
            <td>Ermässigung hinzufügen zu</td>
            <td>-</td>
            <td>Hier kannst du auswählen, wie die Ermässigung hinzugefügt werden soll.<ul>
            <li>für jedes Produkt</li>
            <li>für jede Einheit eines Produktes</li>
            <li>für den Warenkorb-Gesamtwert</li>
            </li>
            </ul></td>
        </tr>
        <tr>
            <td>Name</td>
            <td>-</td>
            <td>Wähle hier einen aussagekräftigen Namen für diese Regel, damit du auch bei mehreren die Übersicht behältst.</td>
        </tr>
        <tr>
            <td>Bezeichnung</td>
            <td>-</td>
            <td>Diese Bezeichnung wird als Text im Warenkorb angezeigt, sobald der Gutscheincode hinzugefügt wurde. Auf dem Bild ist die Bezeichnung <code>Gutschrift</code> zu sehen.</td>
        </tr>
        <tr>
            <td>Ermässigung</td>
            <td>-</td>
            <td>Stelle einer Dezimalzahl oder einer ganzen Zahl ein Minus voran, wahlweise kannst du auch ein Prozentzeichen an die Zahl anhängen.
            <ul>
            <li>31.50 statt 32.00 / Ermässigung: -0.5</li>
            <li>27.00 statt 32.00 / Ermässigung: -5</li>
            <li>28.80 statt 32.00 / Ermässigung: -10%</li>
            </ul></td>
        </tr>
    </tbody>
</table>

![Bezeichnung im Warenkorb](warenkorb_bezeichnung.png)


## Geschenkgutschein

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
            <td>Gutscheincode freischalten</td>
            <td>-</td>
            <td>Hier kannst du festlegen, dass ein Code eingegeben werden muss um diese Regel als Gutschein zu aktivieren.</td>
        </tr>
        <tr>
            <td>Regel (Gutschein) Code</td>
            <td>-</td>
            <td>Hier kannst du den Code eingeben, mit welchem der Kunde diese Regel als Gutschein aktivieren kann.</td>
        </tr>
        <tr>
            <td>Einmalige Nutzung</td>
            <td>-</td>
            <td>
            {{< version-tag "2.6" >}}
            Hier kannst du verhindern, dass dieser Gutscheincode verwendet wird, wenn bereits ein anderer Code angewendet wurde.
            </td>
        </tr>
    </tbody>
</table>




## Nutzungen einschränken

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
            <td>Benutzungen pro Kunde</td>
            <td>0</td>
            <td>Die Benutzung der Regel pro Kunde auf den eingegebenen Wert beschränken. Lässt du die Null stehen, profitiert der Kunde beliebig oft von der Regel.</td>
        </tr>
        <tr>
            <td>Benutzungen pro Shop-Konfiguration</td>
            <td>0</td>
            <td>Die Benutzung der Regel pro Shop-Konfiguration auf den eingegebenen Wert beschränken. Lässt du die Null stehen, profitiert der Kunde in jeder Shop-Konfiguration beliebig oft von der Regel.</td>
        </tr>
        <tr>
            <td>Mindestbetrag Zwischensumme</td>
            <td>0</td>
            <td>Die Regel wird erst angewendet, wenn die Zwischensumme mindestens dem von dir eingegebenem Wert entspricht.</td>
        </tr>
        <tr>
            <td>Höchstbetrag Zwischensumme</td>
            <td>0</td>
            <td>Die Regel wird erst angewendet, wenn die Zwischensumme über dem von dir eingegebenen Wert liegt.</td>
        </tr>
        <tr>
            <td>Geringste Produktanzahl</td>
            <td>0</td>
            <td>Die Regel wird erst angewendet, wenn die Zwischensumme unter dem von dir eingegebenem Wert liegt.</td>
        </tr>
        <tr>
            <td>Höchste Produktanzahl</td>
            <td>0</td>
            <td>Die Regel wird erst angewendet, wenn die Produktanzahl höchstens den von dir eingegebenem Wert entspricht.</td>
        </tr>
        <tr>
            <td>Mengen-Berechnungsmodus</td>
            <td>Menge der Produkte im Warenkorb</td>
            <td>Hier kannst du den Berechnungsmodus für die minimale/maximale Menge bestimmen.
            <ul>
            <li>Menge der Produkte im Warenkorb</li>
            <li>Menge der verschiedenen Produkte im Warenkorb</li>
            <li>Gesamtmenge im Warenkorb</li>
            </ul></td>
        </tr>
    </tbody>
</table>


## Datum & Zeit Einschränkungen

{{% notice warning %}}<p>Zu beachten ist, dass die Datum- und Zeitangaben sich wie Öffnungszeiten eines Geschäftes oder Büros verhalten.<br>Z. B. im Zeitraum vom 01.11.2015 - 10.11.2015 jeweils von 10:00 bis 18:00 Uhr ist die Regel/der Gutschein gültig.</p>{{% /notice %}}

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
            <td>Startdatum</td>
            <td>-</td>
            <td>Falls die Regel erst ab einem bestimmten Datum angewendet werden soll, kannst du hier das Startdatum angeben.</td>
        </tr>
        <tr>
            <td>Enddatum</td>
            <td>-</td>
            <td>Falls die Regel nur bis zu einem bestimmten Datum angewendet werden soll, kannst du hier das Enddatum angeben.</td>
        </tr>
        <tr>
            <td>Startzeit</td>
            <td>-</td>
            <td>Falls die Regel erst ab zu einem bestimmten Zeitpunkt angewendet werden soll, kannst du hier die Startzeit angeben.</td>
        </tr>
        <tr>
            <td>Endzeit</td>
            <td>-</td>
            <td>Falls die Regel nur bis zu einem bestimmten Zeitpunkt angewendet werden soll, kannst du hier die Endzeit angeben.</td>
        </tr>
    </tbody>
</table>


## Erweiterte Einschränkungen

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
            <td>Einschränkungen der Shop-Konfiguration</td>
            <td>-</td>
            <td>Hier kannst du die Regel auf bestimmte <docrobot_route name="configuration">Shop-Konfigurationen</docrobot_route> einschränken.</td>
        </tr>
        <tr>
            <td>Shop-Konfigurationen</td>
            <td>-</td>
            <td>Wähle auf welche Konfiguration diese Regel beschränkt werden soll.</td>
        </tr>
        <tr>
            <td>Bedingung der Shop-Konfiguration</td>
            <td>Wahr</td>
            <td>Wähle ob die Auswahl passen soll <code>Wahr</code> oder nicht <code>Falsch</code>.</td>
        </tr>
        <tr>
            <td>Mitglieder-Einschränkungen</td>
            <td>Keine Einschränkungen</td>
            <td><ul>
            <li>Keine Einschränkungen</li>
            <li>Nur für Gäste</li>
            <li>Bestimmte Gruppen<br>Hier kannst du die Regel auf bestimmte Gruppen beschränken. Alle Mitgliedergruppen welche du in der Benutzerverwaltung von Contao angelegt hast, stehen zur Auswahl.</li>
            <li>Bestimmte Mitglieder<br>Hier kannst du die Regel auf bestimmte Mitglieder beschränken. Über ein Suchfeld können Benutzer anhand von Vorname, Nachname, Benutzername oder E-Mail-Adresse gefunden werden.</li>
            </ul></td>
        </tr>
        <tr>
            <td>Bedingung für Mitglieder</td>
            <td>Wahr</td>
            <td>Wähle ob die Auswahl passen soll <code>Wahr</code> oder nicht <code>Falsch</code>.</td>
        </tr>
        <tr>
            <td>Produkt-Einschränkungen</td>
            <td>Keine Einschränkungen</td>
            <td><ul>
            <li>Keine Einschränkungen</li>
            <li>Produkttypen<br>Hier kannst du die Regel auf bestimmte Produkttypen beschränken. Alle <docrobot_route name="product-types">Produkttypen</docrobot_route> die du in Isotope angelegt hast, stehen zur Auswahl.</li>
            <li>Kategorien<br>Hier kannst du die Regel auf bestimmte Kategorien beschränken, indem du im Seitenbaum die gewünschte Kategorie-Seite auswählst.</li>
            <li>Produkte<br>Hier kannst du die Regel auf bestimmte <docrobot_route name="product-management">Produkte</docrobot_route> beschränken. Über ein Suchfeld können Produkte anhand von Produkttyp, Name oder Artikelnummer gefunden werden.</li>
            <li>Produkte & Varianten<br>Hier kannst du die Regel auf bestimmte Produkte & Varianten beschränken. Dazu benötigst du die Produkte- oder Varianten-IDs, an diese kommst du, indem du hinter dem Produkt oder der Variante über das blaue Icon (<docrobot_image path="images/show.gif" alt="Show Icon">) fährst. Die IDs kannst du in einer kommaseparierten Liste angeben.</li>
            <li>Produktattribute<br>Hier kannst du die Regel auf bestimmte Produktattribute beschränken. Wähle das Produktattribut und bestimme die Attributbedingungen:<ul>
            <li>ist gleich</li>
            <li>ist nicht gleich</li>
            <li>weniger als</li>
            <li>größer als</li>
            <li>weniger als oder ist gleich</li>
            <li>größer als oder ist gleich</li>
            <li>Beginnt mit</li>
            <li>Endet mit</li>
            <li>beinhaltet</li>
            </ul>
            je nachdem welches Attribut du gewählt hast steht dir ein Text- oder Auswahlfeld zur Verfügung.
            </li>
            </ul></td>
        </tr>
        <tr>
            <td>Produktbedingungen</td>
            <td>Wahr</td>
            <td>Wähle ob die Auswahl passen soll <code>Wahr</code> oder nicht <code>Falsch</code>.</td>
        </tr>
    </tbody>
</table>


## Verfügbarkeit

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
            <td>Aktiv</td>
            <td>-</td>
            <td>Hier kannst du wählen ob die Regel zur Zeit aktiv ist.</td>
        </tr>
    </tbody>
</table>
