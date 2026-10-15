# Bestellbenachrichtigungen

Benachrichtigungen informieren Kunden und Mitarbeiter. Eine Bestellbestätigung beantwortet „Hat der Shop meine Bestellung erhalten?“. Eine Zahlungsbestätigung beantwortet eine andere Frage.

Isotope verwendet Notification Center als Paketabhängigkeit. Die Installation konfiguriert weder Mailtransport noch Absender, Empfänger oder Nachrichteninhalt für dein Geschäft.

## Bestellbestätigung konfigurieren

1. Richte den E-Mail-Transport der Website ein und teste ihn.
2. Erstelle in Notification Center eine Benachrichtigung mit dem in der Installation verfügbaren Isotope-Bestellbenachrichtigungstyp.
3. Konfiguriere Nachricht, Gateway/Transport, Absender, Empfänger, Sprache und Text-/HTML-Inhalt.
4. Verwende unterstützte [Simple Tokens](simple-tokens.md) für Bestelldaten.
5. Aktiviere die erforderlichen Nachrichtendatensätze.
6. Wähle die Benachrichtigung im Kasse-Element unter **Bestellbenachrichtigungen**.
7. Gib eine Testbestellung auf und prüfe Zustellung und Inhalt.

Isotope versendet ausgewählte Benachrichtigungen nach dem Anlegen der Bestellung, bevor der anschließende Zahlungsablauf abgeschlossen ist. Formuliere etwa „Wir haben deine Bestellung erhalten“ statt „deine Zahlung war erfolgreich“.

## Nützliche Inhalte

Nimm Bestellreferenz, Produkte und Mengen, Gesamtbetrag und Währung, Rechnungs-/Lieferdaten, gewählte Methoden und nächste Schritte auf. Gib bei Offline-Zahlung klare Anweisungen und eine vom Kunden verwendbare Referenz an.

Häufige Tokens sind `##document_number##`, `##order_total##`, `##cart_text##`, `##cart_html##`, `##billing_address##`, `##shipping_address##` und `##payment_note##`. Deine Verfügbarkeit hängt vom Benachrichtigungskontext ab. Mitgliedertokens können bei Gastbestellungen leer sein.

Verwende den HTML-Warenkorbtoken im HTML-Text und die Textversion im reinen Text. Teste beide Formate, statt einem Textempfänger rohes HTML zu senden.

## Mitarbeiterbenachrichtigungen

Du kannst mehrere Kassenbenachrichtigungen auswählen. Verwende für Mitarbeiter eine eigene Nachricht oder Benachrichtigung, wenn Inhalt oder Empfänger abweichen. Ein Mitarbeiterhinweis sollte auf die anstehende Arbeit verweisen, ohne bereits eingegangenes Geld zu behaupten.

## Nachrichten bei Statusänderungen

Erstelle dafür eine Isotope-Bestellaktualisierungsbenachrichtigung. Aktiviere im Bestellaktualisierungsformular den Benachrichtigungsversand, wähle die Benachrichtigung und fülle gegebenenfalls Sendungsnummern und Kundenhinweise aus. Eine Statusbezeichnung allein versendet keine Nachricht automatisch. Lass für automatische Integrationen den gewünschten ereignisbasierten Auslöser entwickeln und testen.

Teste den Versandzeitpunkt und das Verhalten bei wiederholter gleicher Statusaktualisierung. Versprich keinen Versand, bevor das Paket tatsächlich übergeben wurde.

## Zustellprobleme beheben

Prüfe zuerst, ob die Bestellung existiert. Prüfe dann gewählte Benachrichtigung, aktive Nachricht, Sprache, aufgelösten Empfänger und Mailprotokolle. Erfolgreiches Anlegen einer Bestellung und erfolgreiche E-Mail-Zustellung sind getrennte Ergebnisse.

Sende den Bestellvorgang eines Kunden nicht wiederholt ab, nur um E-Mails zu testen. Verwende kontrollierte Testbestellungen und prüfe das vorhandene Benachrichtigungsergebnis.
