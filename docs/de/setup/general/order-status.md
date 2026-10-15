# Bestell-, Zahlungs- und Versandstatus

Isotope 3 führt drei Statusverläufe. Zusammen zeigen sie Mitarbeitern, was geschehen ist und was noch zu tun bleibt.

| Verlauf | Typische Werte | Zweck |
| --- | --- | --- |
| Bestellung | Ausstehend, In Bearbeitung, Abgeschlossen, Zurückgestellt, Storniert | Gesamte Bearbeitung |
| Zahlung | Offen, In Bearbeitung, Bezahlt, Fehlgeschlagen, Erstattet | Geld und Zahlungsversuche |
| Versand | Offen, Versendet, Teilweise versendet, Zurückgesendet | Lieferfortschritt |

Eine Bestellung kann beispielsweise In Bearbeitung, Bezahlt und beim Versand Offen sein. Mitarbeiter können sie dann für den Versand vorbereiten.

## Mit den mitgelieferten Status beginnen

Die Migration stellt Standarddatensätze für fehlende Statustypen bereit. Prüfe diese unter **Konfiguration → Bestellstatus**, bevor du eigene ergänzt.

Halte technische Namen stabil. Code, gespeicherte Bestellungen, Zahlungsarten und Workflowübergänge können darauf verweisen. Ändere eine Kundenbezeichnung, wenn nur ein anderer Wortlaut nötig ist.

## Nächste mögliche Zustände

Jeder Datensatz legt die zulässigen Folgezustände fest. Diese Übergänge bilden einen Workflow.

Eine offene Zahlung kann beispielsweise je nach Fall zu In Bearbeitung, Bezahlt oder Fehlgeschlagen wechseln. Ein Versanddatensatz kann von Offen zu Versendet wechseln. Fehlt bei der Bestellbearbeitung ein gewünschter Folgestatus, prüfe die erlaubten Übergänge des aktuellen Status und die Mitarbeiterberechtigungen.

Eine Farbe erleichtert die Übersicht im Backend. Sie ändert nicht die Wirkung des Status.

## Technischer Zahlungszustand und Zahlungsbezeichnung

Ein Zahlungsstatus wird zusätzlich einem technischen Zustand zugeordnet:

- **Pending** erlaubt einen Zahlungsversuch oder eine Wiederholung.
- **Processing** bedeutet, dass das Ergebnis ungeklärt ist.
- **Complete** beendet den aktiven Zahlungsablauf.

Setze den technischen Zustand Complete nicht mit einem Zahlungseingang gleich. Auch der mitgelieferte Zahlungsstatus Storniert verwendet Complete. Mitarbeiter müssen den tatsächlichen Zahlungsstatus und Zahlungsnachweis lesen.

Ordne Ergebnisse von Zahlungsarten bewusst zu. Die Offline-Methode Barzahlung setzt lediglich ihren konfigurierten Bearbeitungsstatus. Sie erkennt keinen Geldeingang.

## Statusänderungen führen nicht jede Geschäftsaktion aus

Versendet zu setzen bucht kein Paket. Erstattet zu setzen löst nicht zwingend eine Erstattung beim Anbieter aus. Eine Bestellung auf Abgeschlossen zu setzen belegt nicht, dass Zahlung und Lieferung abgeschlossen sind.

Definiere die reale Handlung, führe oder prüfe sie und aktualisiere dann den zugehörigen Datensatz. Automatisiert eine Integration diese Folge, dokumentiere und teste deren Auslöser.

## Workflow testen

Gehe mit einer Testbestellung normale Abwicklung, fehlgeschlagene Zahlung, Stornierung und Rücksendung durch. Prüfe, ob Mitarbeiter nötige Übergänge wählen können und durch die gewählten Berechtigungen und Verfahren keine kritischen Geschäftsschritte versehentlich überspringen.

Als Nächstes: [Bestellungen bearbeiten](../../usage/orders.md).
