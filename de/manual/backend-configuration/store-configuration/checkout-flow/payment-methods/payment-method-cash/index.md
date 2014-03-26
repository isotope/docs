# Zahlungsart "Bar"

Der **Bestellhinweis** zur Zahlungsart kann im folgenden Textfeld eingetragen werden. Die Hinweise können in der Bestätigungs-Mail mitgesendet werden, indem `##payment_note##` oder `##payment_note_text##` in die Mail-Vorlage geschrieben wird.

Im Auswahlmenü **Status für neue Bestellungen** kann der Status ausgewählt werden, welcher die Bestellung nach der Zahlung haben soll. Zur Verfügung stehen *Ausstehend*, *inBearbeitung*, *Erledigt* und *Zurückgestellt*. Bei Vorkasse wäre hier *inBearbeitung* angebracht, bei Paypal zum Beispiel *Erledigt*, wenn es ein Download-Artikel ist.
  Weiterhin bietet Isotope bei jeder Zahlungsart die Optionen, **Minimaler** und **Maximaler Betrag**. Angewendet bedeutet das, wenn ein minimaler Betrag eingetragen ist, kann der potenzielle Käufer diese Zahlungsmöglichkeit erst dann nutzen, wenn er Produkte von mindestens diesem Wert im Warenkorb hat.


Die jeweilige Zahlungsart kann in der Zugänglichkeit für bestimmte Länder eingeschränkt werden. Wähle dazu die zugänglichen Länder unter **Aktive Länder** aus. 


**Versandarten** und **Produkttypen** können genauso wie die Länder eingeschränkt werden. Mit einem Unterschied - wenn bei **Ländern** nichts ausgewählt wird, heisst das dass Zahlungsmöglichkeit aus allen Ländern heraus benutzt werden dürfen. Falls bei Versandart oder Produkttyp nichts ausgewählt wird, steht die Zahlungsmöglichkeit dementsprechend nicht zur Verfügung.


In das Feld **Preis** kann der Preis für die Zahlungsart pro Bestellung eingetragen werden.

z. B.
- Einen Betrag: 2
- Einen Prozentwert: 2%
- Einen Prozentwert mit einem Minus -2% (bei Vorauskasse)




Im Dropdown-Menü **Steuerklasse** kann eine passende Steuerklasse ausgewählt werden. Die Steuerklassen- und -sätze müssen im Vorfeld angelegt werden.


Unter **Experteneinstellungen** - schon von den Contao Core-Einstellungen bekannt – kann ein Zugriffsschutz für bestimmte Mitglieder-Gruppen festgelegt oder Mitgliedergruppen von der Zahlungsmöglichkeit ausgeschlossen werden.


Damit die Zahlungsmöglichkeit dann im **Kasse-Modul** zur Verfügung steht, muss die Checkbox **Modul aktivieren** aktiviert werden.
