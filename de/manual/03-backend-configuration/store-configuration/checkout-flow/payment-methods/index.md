# Zahlungsarten

Das Einstellen der Zahlungsmöglichkeiten ist sehr eindeutig. Einfach anlegen, Möglichkeiten im Formular checken und ausprobieren.

Zur Auswahl stehen:

1. Barzahlung
2. PayPal Standart
3. Postfinance (Schweizer Post)
4. Authorize.net 

 Je nachdem welche der oben genannten Zahlungsmöglichkeiten ausgewählt wird, werden weitere Einstellungsmöglichkeiten geladen, welche sich auf den jeweiligen Typ beziehen.


Der **Bestellhinweis** zur Zahlungsart kann im folgenden Textfeld eingetragen werden. Die Hinweise können in der Bestätigungs-Mail mitgesendet werden, indem `##payment_note##` oder `##payment_note_text##` in die Mail-Vorlage geschrieben wird.

Im Auswahlmenü **Status für neue Bestellungen** kann der Status ausgewählt werden, welcher die Bestellung nach der Zahlung haben soll. Zur Verfügung stehen *Ausstehend*, *inBearbeitung*, *Erledigt* und *Zurückgestellt*. Bei Vorkasse wäre hier *inBearbeitung* angebracht, bei Paypal zum Beispiel *Erledigt*, wenn es ein Download-Artikel ist.
  Weiterhin bietet Isotope bei jeder Zahlungsart die Optionen, **Minimaler** und **Maximaler Betrag**. Angewendet bedeutet dass, wenn ein minimaler Betrag eingetragen ist, kann der potenzielle Käufer diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von mindestens diesen Wert im Warenkorb hat.


Die jeweilige Zahlungsart kann in den Zugänglichkeit für bestimmte Länder eingeschränkt werden. Wähle dazu die zugänglichen Länder unter **Aktive Länder** aus. 


**Versandarten** und **Produkttypen** können genauso wie die Länder eingeschränkt werden. Mit einem Unterschied - Wenn bei **Ländern** nichts ausgewählt wird, heisst das dass Zahlungsmöglichkeit aus allen Ländern heraus benutzt werden dürfen. Für den Fall das bei Versandart oder Produkttyp nichts ausgewählt wird, dann steht die Zahlungsmöglichkeit dementsprechend nicht zur Verfügung.


In das Feld **Preis** kann der Preis für die Zahlungsmöglichkeit pro Bestellung mit dieser eingetragen werden.


Im Dropdown-Menü **Steuerklasse** kann eine passende Steuerklasse ausgewählt werden. Die Steuerklassen- und -sätze müssen im Vorfeld angelegt werden.


Unter **Experteneinstellungen** - schon von den Contao Core-Einstellungen bekannt – kann einen Zugriffsschutz für bestimmte Mitglieder-Gruppen festgelegt, oder Mitgliedergruppen von der Zahlungsmöglichkeit ausgeschlossen werden.


Damit die Zahlungsmöglichkeit dann im **Kasse-Modul** zur Verfügung steht muss die Checkbox **Modul aktivieren** aktiviert werden.
