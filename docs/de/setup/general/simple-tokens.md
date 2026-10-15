# Simple Tokens in Nachrichten

Ein Simple Token ist ein Platzhalter, der beim Erzeugen einer unterstützten Nachricht durch Daten ersetzt wird. Beispielsweise kann `##order_total##` in einer Isotope-Bestellbenachrichtigung zum formatierten Gesamtbetrag werden.

Tokens sind keine Twig-Ausdrücke oder Contao-Inserttags. Sie haben eine andere Syntax und sind in anderen Kontexten verfügbar.

## Eine kurze Bestellnachricht

Verwende dies als Ausgangspunkt im Nachrichtentext einer Isotope-Bestellbenachrichtigung:

```text
Vielen Dank für deine Bestellung ##document_number##.

Deine Bestellung enthält folgende Artikel:

##cart_text##

Gesamtbetrag: ##order_total##
Zahlungsart: ##payment_label##

##payment_note##
```

Dies bestätigt den Eingang der Bestellung. Es behauptet keinen Zahlungserfolg.

Verwende für HTML-Nachrichten geeignetes HTML und den unterstützten Token `##cart_html##` für die Bestelltabelle. Teste Text- und HTML-Version unabhängig voneinander.

## Häufige Bestellbenachrichtigungstokens

| Token | Bedeutung |
| --- | --- |
| `##recipient_email##` | Für diesen Kontext bereitgestellte Empfänger-E-Mail |
| `##order_id##` | Interne Datenbank-ID der Bestellung |
| `##document_number##` | Formatierte Bestellreferenznummer |
| `##uniqid##` | Eindeutige Kennung für den Bestellzugriff |
| `##order_total##` | Formatierter Gesamtbetrag |
| `##order_subtotal##` | Formatierte Zwischensumme |
| `##order_items##` | Summierte Mengen |
| `##order_products##` | Anzahl der Bestellpositionen, auch Nichtproduktpositionen möglich |
| `##billing_address##` / `##shipping_address##` | Formatierte HTML-Adressen |
| `##billing_address_text##` / `##shipping_address_text##` | Adressen als reiner Text |
| `##payment_label##` / `##payment_note##` | Gewählter Zahlungstext |
| `##shipping_label##` / `##shipping_note##` | Gewählter Versandtext |
| `##order_status##` | Bestellstatusbezeichnung |
| `##transaction_status##` | Zahlungsstatusbezeichnung |
| `##delivery_status##` | Versandstatusbezeichnung |

Die Tokenauswahl und der tatsächliche Benachrichtigungstyp sind die Referenz dafür, wo Tokens akzeptiert werden. Prüfe die in deiner Nachricht ausgegebene Kennung, statt bei allen Referenztokens dieselbe Nummer anzunehmen.

## Tokenfamilien

Familien wie `billing_address_*`, `shipping_address_*` und `config_*` stellen unterstützte Felder dieser Datensätze bereit. Ersetze den Stern durch einen tatsächlichen Feldnamen. Er ist keine wörtlich in die Nachricht einzufügende Syntax.

`member_*`-Daten hängen von einer Mitgliederbestellung ab. `form_*`-Daten hängen von konfigurierten Bestellbedingungsfeldern ab. Tokens für vorherige Status gehören zum Bestellaktualisierungs-Benachrichtigungstyp und existieren möglicherweise nicht in der anfänglichen Bestellbestätigung. Dieser Typ registriert außerdem `tracking_numbers` und `customer_notes`.

Verwende `collection_*` nicht in Bestellbenachrichtigungen. Nutze die obigen Bestelltokens. Dokumenttitel- und Dateinamenfelder haben eine eigene dokumentierte Unterstützung für Collection-Tokens. Kopiere keinen beliebigen Benachrichtigungstoken in jedes Textfeld in der Erwartung, dass er aufgelöst wird.

## Fehlende Daten testen

Sende je eine Gast- und Mitgliedertestbestellung. Prüfe optionale Adressfelder, fehlenden Versand bei versandbefreiten Produkten, übersetzte Bezeichnungen und einen leeren Zahlungshinweis.

Bleibt ein Token sichtbar, prüfe Schreibweise, Benachrichtigungstyp und Einfügefeld. Wird er leer, prüfe, ob die Quelldaten in diesem Kontext existieren.
