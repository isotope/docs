# Zahlungsarten

Das Einstellen der Zahlungsmöglichkeiten ist sehr eindeutig. Einfach anlegen, Möglichkeiten im Formular checken und ausprobieren.

##Zur Auswahl stehen:

1. Cash
2. Datatrans
3. ExperCash
4. PayOne
5. Paypal Standard Checkout
6. Postfinance (Schweizer Post)
7. VIVEUM
8. Saferpay
9. sofortüberweisung.de
10. WorldPay

 
Hinweis:
Authorize.net ist nicht mehr dabei.




##Allgemeine Einstellungen



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


##Konfiguration des Zahlungsanbieters

Je nachdem welche der oben genannten Zahlungsmöglichkeiten ausgewählt wird, werden weitere Einstellungsmöglichkeiten geladen, welche sich auf den jeweiligen Typ beziehen.
Nachfolgend sind diese im Detail aufgelistet.


####2. Datatrans

#####Spezifische Angaben zu dieser Zahlmöglichkeit:
1. Transfertyp (Auswahl zwischen Autorisieren und einnehmen ODER Nur Autorisieren)
2. Händler-ID*
3. HMAC Schlüssel* 
4. Testsystem verwenden


####3. ExperCash

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. ExperCash Popup-ID*
(Gebe die Popup-ID aus Ihrem ExperCash Portal ein.)

2. ExperCash Profil*
(Gebe die dreistellige Profilnummer ein.)

3. ExperCash Popup-Schlüssel*
(Gebe den Popup-Key aus Ihrem ExperCash Portal ein.)

4. Transaktionsart*
(Auswahl der Zahlart durch den Endkunden)

	1. Auswahl der Zahlart durch den Endkunden
	2. Zahlung per Lastschrift (ELV)
	3. Prüfung und Speicherung von Kontodaten zum späteren Einzug
	4. Kreditkartenzahlung
	5. verbindliche Reservierung auf eine Kreditkarte zum späteren Einzug
	6. Transaktion über giropay
	7. Transaktion über Sofortüberweisung

	Sie können eine Transaktionsart vordefinieren oder den Kunden wählen lassen.

#####Template
CSS-Vorlage aus der Dateiverwaltung (Wählen Sie eine CSS-Datei für die Übergabe an ExperCash).

####4. PayOne
#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. Transaktions-Typ* (Den Hilfe-Assistent aufrufen)
	1. Autorisieren und Einnehmen
	2. Nur Autorisieren

	Wählen Sie, ob Sie das Geld sofort einnehmen oder für eine spätere Transaktion (z. B. wenn versandt wird) autorisieren (und abwarten) wollen.


2. Abwicklungsart*
	
	1. Einziehen mit Drawal
	2. Kreditkarte
	3. Bankomatkarte
	4. Vorauszahlung
	5. Rechnung
	6. Online Banktransfer
	7. e-Wallet

	Bitte wählen Sie eine Abwicklungsart.


3. PAYONE Account-ID*
Bitte geben Sie ihre eindeutige PAYONE Account ID ein.

4. PAYONE Portal-ID*
Bitte geben Sie die eindeutige PAYONE Portal ID ein.

5. Sicherheitsschlüssel*
Geben Sie den Sicherheitsschlüssel für dieses Portal ein.

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.

####5. Paypal Standard Checkout

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. PayPal-Konto*

Geben Sie die E-Mail Adresse ein, welche als Standard ihres Paypalkontos aktiviert ist.

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.

####6. Postfinance

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. PSPID*
Die PSPID ist Ihr eindeutiger Erkennungsname im Postfinance-System.
2. HTTP Methode* (Auswahl POST oder GET)
Typ der HTTP Daten von und zu den Servern.
3. Hash-Methode* 
	1. SHA-1
	2. SHA-256
	3. SHA-512
	
	Hash-Algorithmus für Datentransfer von und zu Servern.

4. SHA-IN Signatur*
Dies wird zum Validieren der Server-zu-Server-Verbindung genutzt.
5. SHA-OUT Signatur*
Dies wird zum Validieren der Server-zu-Server-Verbindung genutzt.
6. Dynamische Template URL

Geben Sie eine absolute URL zu einem dynamischen Template ein.

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.

####7. VIVEUM (gleich wie 6. Postfinance)

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. PSPID*
(Die PSPID ist Ihr eindeutiger Erkennungsname im Postfinance-System.)
2. HTTP Methode* (Auswahl POST oder GET)
Typ der HTTP Daten von und zu den Servern.
3. Hash-Methode* 
	1. SHA-1
	2. SHA-256
	3. SHA-512
	
	Hash-Algorithmus für Datentransfer von und zu Servern.

4. SHA-IN Signatur*
	(Dies wird zum Validieren der Server-zu-Server-Verbindung genutzt.)
5. SHA-OUT Signatur*
(Dies wird zum Validieren der Server-zu-Server-Verbindung genutzt.)
6. Dynamische Template URL
(Geben Sie eine absolute URL zu einem dynamischen Template ein.)

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.


####8. Saferpay

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. Saferpay Account-ID*
(Bitte geben Sie Ihre eindeutige Saferpay Account ID ein.)

2. Transaktions-Typ* 
	1. Authorisieren und Einnehmen
	2. Nur Authorisieren
	
	Wählen Sie ob Sie das Geld sofort einnehmen oder für eine spätere Transaktion (z. B. wenn versandt wird) authorisieren (und abwarten) wollen.

3. Checkout-Beschreibung*
(Der Kunde wird diese Beschreibung auf der Saferpay Checkout-Seite sehen.)
4. Konfiguration Zahlungsseite (VTCONFIG)

	(Sie können verschiedene Zahlseiten-Konfigurationen erstellen. Wenn Sie eine spezielle verwenden möchten, geben Sie den Wert des Request-Parameters hier ein.)


####9. Sparkasse

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. Zahlungsart*
	1. Kreditkarte
	2. Abbuchungkarte
	3. Bankeinzug

	Bitte wählen Sie eine Zahlungsart.
	
2. Transaktions-Typ* Den Hilfe-Assistent aufrufen
	1. Authorisieren und Einnehmen
	2. Nur Authorisieren

	Wählen Sie ob Sie das Geld sofort einnehmen oder für eine spätere Transaktion (z. B. wenn versandt wird) authorisieren (und abwarten) wollen.
	
3. Verkäufer ID*
(Bitte geben Sie Ihre Verkäufer ID ein (Händlerkennung).)

4. Passwort*
(Bitte geben Sie Ihr SSL-Passwort ein.)

5. Referenz

	Eine Referenz, welche auf der Detailseite des Verkäufers anstelle der Warenkorbnummer angezeigt wird.

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.

####10. Sofortüberweisung.de

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. Transaktions-Typ* 
	1. Authorisieren und Einnehmen
	2. Nur Authorisieren
	
	Wählen Sie ob Sie das Geld sofort einnehmen oder für eine spätere Transaktion (z. B. wenn versandt wird) authorisieren (und abwarten) wollen.

2. Kunden ID*
(Ihre Kunden ID bei sofortüberweisung.de)

3. Projekt ID*
(Ihre Projekt ID bei sofortüberweisung.de)

4. Projekt-Passwort*
(Ihr Projekt-Passwort bei sofortüberweisung.de)


####11. WorldPay

#####Spezifische Angaben zu dieser Zahlmöglichkeit:

1. Installation ID*
(Bitte geben Sie die WorldPay Installation's ID ein.)

2. Transaktions-Passwort*
(Geben Sie dasselbe Passwort ein, das Sie bei Ihrer WorldPay-Konfiguration eingegeben haben.)

3. Signaturfelder*
(Geben Sie denselben Wert für das Signaturfeld ein, den Sie bei Ihrer WorldPay-Konfiguration eingegeben haben.)

4. MD5 Geheim*
(Geben Sie denselben MD5 Geheimwert ein, den Sie bei Ihrer WorldPay-Konfiguration eingegeben haben.)

5. Beschreibung*
(Geben Sie eine Beschreibung für Ihren Shop ein. Diese wird den Kunden während dem Worldpay Checkout gezeigt.)

#####Aktivierte Einstellungen
1. Testsystem verwenden

Aktivieren Sie diese Option, um ein Testsystem zu verwenden, auf dem keine echten Zahlungen ausgeführt werden.

