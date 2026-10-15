# Events und Lebenszyklus

Events erlauben einem Dienst, einen bestehenden Prozess zu beobachten oder zu ergänzen. Wähle das Event nach Auslösestelle und Zeitpunkt, nicht allein nach Klassenname.

## Nützliche Eventfamilien

| Event | Zweck |
| --- | --- |
| `Store\Event\ContextCreatedEvent` | Mit neu erzeugtem Shopkontext arbeiten |
| `Product\Event\ProductCreatedEvent` | Ein konstruiertes Produktobjekt und dessen Daten/Kontext beobachten |
| `Product\Event\ProductConfigurationEvent` | Mit Produktkonfiguration für das Rendering arbeiten |
| `Product\Event\ProductPriceEvent` | Einen berechneten Produktpreis prüfen oder ändern |
| `Checkout\Event\CheckoutStepEvent` | Einen Kassenschritt ergänzen oder validieren |
| `Store\Event\OrderValidationEvent` | Bedingungen zur Bestellvalidierung ergänzen |
| `Store\Event\CollectOrderNotificationTokensEvent` | Bestellbenachrichtigungstokens ergänzen |

Diese Namen sind relativ zu `Isotope\CoreBundle`. `ProductCreatedEvent` beschreibt die Konstruktion eines Produktobjekts. Nimm nicht an, dass ein Händler gerade einen neuen Katalogdatensatz angelegt hat.

## Beispiel: einen Benachrichtigungstoken ergänzen

In einer Anwendung mit aktivierter Service-Autokonfiguration kann ein gezielter Listener einen statischen Unterstützungshinweis ergänzen:

```php
<?php

declare(strict_types=1);

namespace App\EventListener;

use Isotope\CoreBundle\Store\Event\CollectOrderNotificationTokensEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener]
final class OrderSupportTokenListener
{
    public function __invoke(CollectOrderNotificationTokensEvent $event): void
    {
        $event->addToken('support_message', 'Antworte auf diese E-Mail, wenn du Hilfe benötigst.');
    }
}
```

Das Event wird bewusst über seine verändernde Methode `addToken()` ergänzt. Validiert Notification Center Tokennamen für das Nachrichtenfeld, erweitere auch die erlaubte Tokendefinition des Benachrichtigungstyps, bevor du dort `##support_message##` verwendest. Prüfe Registrierung, Validierung erlaubter Tokens und eine zugestellte Nachricht in einer vollständigen Contao-Anwendung.

Nimm keine Zugangsdaten oder unnötigen Kundendaten in Tokens auf. Übersetze mehrsprachige Nachrichten im passenden Bestellkontext, statt den Beispieltext fest einzubauen.

## Kassenvalidierung

`CheckoutStepEvent` stellt Schritttyp, Request, Kontext, Bearbeitungs-/Absendestatus und ein Fehlerflag bereit. Es unterstützt außerdem Markup vor und nach dem Schritt. Prüfe, ob dein Listener für Adresse, Versand, Zahlung oder `_summary` läuft.

`OrderValidationEvent` akzeptiert Symfony-Validierungsbedingungen. Verwende es zur Validierung von Bestelldaten, statt für eine einzige Prüfung einen ganzen Kassencontroller zu ersetzen.

## Transaktionslebenszyklus-Events

Isotopes Transaktionsdispatcher verwendet benannte Phasen:

- `<name>.pre` vor der Operation.
- `<name>.error`, wenn die umschlossene Operation eine Ausnahme auslöst.
- `<name>.post`, nachdem der Dispatcher die Operation bzw. den behandelten Fehlerpfad beendet hat.

Beispielsweise ist `OrderTransactionEvent::NAME` gleich `isotope.order`, während `OrderStatusTransactionEvent::NAME` gleich `isotope.order_status` ist.

Diese Phasen werden unter ausdrücklichen Stringnamen ausgelöst. Abonniere den tatsächlichen Phasennamen und nicht nur die Eventklasse. Der Dispatcher kann einen Fehlerlistener ein Ergebnis liefern lassen. Deshalb belegt ein Post-Event allein weder Zahlungserfolg noch eine allgemeine Garantie, dass die Datenbanktransaktion bereits bestätigt wurde.

## Externe Nebenwirkungen

Definiere für Buchhaltungs-, Abwicklungs- und Anbieterintegrationen Wiederholungs- und Duplikatbehandlung anhand stabiler Bestell-/Transaktionsreferenzen. Validiere Zahlungsnachweise an der Anbieterschnittstelle. Vermeide irreversible externe Aktionen aus einer Phase, die vor erfolgreicher Speicherung laufen kann.

Quellen: [Transaktionsdispatcher](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/EventDispatcher/TransactionEventDispatcher.php), [Benachrichtigungstoken-Event](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Event/CollectOrderNotificationTokensEvent.php).
