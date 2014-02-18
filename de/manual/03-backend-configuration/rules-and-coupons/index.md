# Regeln & Gutscheine

<docrobot_incomplete>

Isotope bringt wichtige Funktionen für Aktions-Regeln, Rabatt-Regeln und Gutscheine mit.

 Um eine **Regel für Produkte** anzulegen, für eine Produktgruppe zum Beispiel, wähle im ersten Auswahlmenü "Typ" **"Produkt"** aus. Das Namensfeld erwartet eine sinnvolle Bezeichnung.

Trage im folgenden Feld **"Ermässigung"** den numerischen Wert ein, welcher verrechnet werden soll. Es kann eine Geldeinheit oder ein Prozentwert eintragen werden. Ein Plus oder Minus davor bestimmt die mathematische Operation die ausgeführt werden soll. Der Wert "-30%" ergibt also einen Abzug von 30% auf den Produktpreis.  
Weitere Einstellungsbereiche sind "Nutzungen einschränken", "Datum & Zeit Einschränkungen", "Erweiterte Einschränkungen". Unter Nutzungen einschränken können Werte für "Benutzung pro Kunde", "Benutzung pro Shop-Konfiguration", "Geringste Produktanzahl", "Höchste Produktanzahl" definiert werden. Im **"Mengen-Berechnungsmodus"**-Auswahlfeld kann festgelegt werden auf welche Menge genau sich die **Ermässigung** beziehen soll. Zur Auswahl stehen "Menge der Produkte im Warenkorb", "Gesamte der Produkte im Warenkorb" und "Gesamtmenge im Warenkorb". Die Einstellungen sind Relevant, wenn die Ermässigung in einer Geldeinheit angegeben wird. **"Menge der Produkte im Warenkorb"** heisst dann, dass die Geldeinheit nur einmal pro Produkt abgezogen wird, auch wenn von einem Produkt mehrere im Warenkorb liegen. **"Gesamte der Produkte im Warenkorb"** bedeutet, das wenn zehn mal das selbe Produkt im Warenkorb liegt, die Geldeinheit mal zehn multipliziert wird und als Gesamtbetrag abgezogen wird. **"Gesamtmenge im Warenkorb"** - Es gibt nur einen Warenkorb. Die Geldeinheit wird also nur Einmal insgesamt abgezogen.

 Die Produktregelung kann auch im Bereich **"Datum & Zeit Einschränkungen"** zeitlich begrenzt werden. Mit der Eingabe von Datum und Zeit kann bestimmt werden ab wann die Regelung angewendet werden soll und ab wann nicht mehr.


Um die Regel individuell gestalten zu können gibt es im Bereich **"Erweiterte Einschränkungen"** noch viele weitere Möglichkeiten, um eine spezielle Shop-Konfiguration auszuwählen, um Zugriffsrechte zu bestimmen oder um die Produkte zu Filtern auf welche die Regel angewendet werden sollen. Interessant sind vor Allem die Produktflter-Möglichkeiten. Bedingung für die Anwendung können "Produkttypen", "Bestimmte Kategorien", "Bestimmte Produkte", "Products & Variants" oder "Product attribute" sein.


Die **Bedingungsabfragen** lassen sich sogar negativ anwenden. Es kann also zwischen "true" und "false" gewählt werden. In der Anwendung "false", hiesse das "Wende die Regel auf alle Produkte an, **ausser** auf …".  Im letzten Schritt muss die Regel nur noch unter "Verfügbarkeit" aktiviert werden.

 Auf der Einstellungsseite für Regeln und Gutscheine finden sich keine fertigen Gutscheine zum Veröffentlichen vor. Prinzipiell können mit den zur Verfügung stehenden Funktionen Geschenk-Gutscheine mit **Indentifizierungs-Code** erstellt werden.  Gutscheine werden im Warenkorb vor dem  Bestellprozess eingelöst. Deshalb im ersten Auswahlmenü "Typ" "Warenkorb" auswählen.

 Nachdem der Typ Warenkorb festgelegt wurde, kann über das Dropdown **"Ermässigung hinzufügen zu"** ausgewählt werden auf was der Gutscheinrabatt im Warenkorb angewendet werden soll. Zur Auswahl stehen "Für jedes Produkt", "Für jede Einheit eines Produktes" und "Für den Warenkorb-Gesamtwert". Diese Einstellung spielt nur eine Rolle, wenn der Geschenkgutscheinwert, **"Ermässigung"**, nicht in Form von Prozent festlegt wurde. Ein Beispiel wäre: Ein Geschenkgutschein von fünf Euro mit der Einstellung **"Für jedes Produkt"**. Wenn zwei verschiedene Produkte im Warenkorb sind, von denen aber Mehrere, werden zwei mal fünf Euro abgezogen. Ist die Einstellung **"Für jede Einheit eines Produktes"** gewählt, wird die Gesamtanzahl an verschiedenen Produkten mit den fünf Euro multipliziert und abgezogen. Ist die Einstellung  **"Für den Warenkorb-Gesamtwert"** werden die fünf Euro nur einmal abgezogen.

 Neben dem Namensfeld kann eine **Bezeichnung** eingegeben werden für die Ausgabe im Frontend. Diese Bezeichnung wird bei der **Ausgabe im Warenkorb** der allgemeinen Namensgebung vorgezogen. Neben dem Ermässigung-Feld kannst eine vordefinierten Steuerklassen der **Ermässigung** zugeordnet werden.