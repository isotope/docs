# Stornierungen, Rücksendungen und Erstattungen

Diese Aktionen beschreiben unterschiedliche Teile des Geschäftsprozesses.

Eine **Stornierung** stoppt weitere Bearbeitung. Eine **Rücksendung** betrifft zurückkommende Waren. Eine **Erstattung** betrifft zurückfließendes Geld. Eine Aktion kann ohne alle anderen stattfinden.

## Unbezahlte Bestellung stornieren

1. Identifiziere die richtige Bestellung und prüfe die Zahlungssituation.
2. Stoppe Kommissionierung oder Lieferung im betrieblichen Prozess.
3. Verwende einen erlaubten, zur Stornierung passenden Bestell-/Zahlungsübergang.
4. Erfasse den Grund und teile dem Kunden das Ergebnis mit.
5. Prüfe, ob ein externer Zahlungsversuch noch läuft.

Ein verzögertes Anbieterergebnis kann nach Abbruch des Bestellvorgangs eintreffen. Gleiche ungeklärte Transaktionen ab, bevor du von ausbleibender Zahlung ausgehst.

## Rücksendung bearbeiten

Halte fest, welche Artikel warum zurückgesendet werden. Prüfe den tatsächlichen Eingang und ob ein Teil der Bestellung geliefert bleibt. Verwende gegebenenfalls die verfügbaren Versandstatus Zurückgesendet oder Teilweise zurückgesendet.

Entscheide separat, ob gemäß deinem vereinbarten Prozess eine Erstattung, ein Ersatz oder eine andere Lösung erforderlich ist. Dieses Handbuch beschreibt Datensatzbearbeitung und legt keine Rückgaberichtlinie fest.

## Erstattung ausführen und erfassen

Führe die Erstattung über den Zahlungsanbieter oder den Offline-Zahlungsprozess aus, der das Geld tatsächlich bewegt. Verwende die Erstattungsaktion der Integration, falls sie eine solche ausdrücklich unterstützt. Bestätige Ergebnis und Betrag.

Aktualisiere dann Zahlungsdatensatz/-status über den unterstützten Workflow, bewahre die externe Referenz und sende die vorgesehene Nachricht. **Die Statusänderung zu Erstattet allein belegt keine Geldrückzahlung.**

Mache bei Teilerstattungen deutlich, welchen Betrag und welche Artikel sie betreffen. Leite aus einem Status Teilweise bezahlt oder Teilweise erstattet keine automatische artikelbezogene Buchhaltung ab.

## Bestand, Versand und Dokumente

Prüfe bei Lager- oder Buchhaltungsintegrationen, ob diese auf den gewählten Übergang reagieren und wiederholte Aktualisierungen sicher sind. Zurückgesendete Ware ist nicht zwangsläufig sofort wieder verkaufbar.

Bewahre bestehende Dokumente auf und folge dem geschäftlichen Korrekturbelegprozess. Das Löschen einer Bestellung zur Beseitigung eines Fehlers entfernt auch den für den Transaktionsabgleich benötigten Kontext.

## Ausnahmefälle testen

Übe vor dem Start mit Testdaten eine unbezahlte Stornierung, die Wiederholung einer fehlgeschlagenen Zahlung, eine vollständige Rücksendung und eine Teilerstattung. Halte fest, welche Aktionen in Isotope, beim Zahlungsanbieter und in einem anderen System stattfinden.

Verwandte Themen: [Bestellstatus](../setup/general/order-status.md), [Bestellungen bearbeiten](orders.md).
