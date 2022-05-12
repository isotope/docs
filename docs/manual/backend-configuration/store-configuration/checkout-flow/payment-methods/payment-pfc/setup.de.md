---
title: "Einrichtung von PostFinance Checkoout Flex"
description: "Einrichtung von PostFinance Checkoout Flex"
aliases:
- /de/backend-konfiguration-shop-bestellablauf-zahlungsarten-pfc-einrichtung/
weight: 100
hidden: true
---

PostFinance Checkout bietet eine kostenlose Testversion, für welche man sich auf der [Webseite][website] frei registrieren
kann. Mit dem Testkonto kann die volle Funktionalität in Isotope eCommerce getestet werden, erst nach Vertragsabschluss
werden tatsächliche Kosten berechnet und können echte Transaktionen durchgeführt werden.


## Zahlungsmethode konfigurieren

Für die Einrichtung im Isotope Backend werden folgende Zugangsdaten benötigt:
1. Space ID
2. User ID
3. Api Secret (Authentication Key)

![Isotope Modulkonfiguration](../zugangsdaten.png)


### Space anlegen

Das PostFinance Checkout System ist so ausgelegt, dass mit demselben Benutzerkonto mehrere Shops oder andere
Zahlungssysteme bedient werden können. Diese werden jeweils über eigene sogenannte _Spaces_ konfiguriert.

Nach der Einrichtung eines Spaces ist dessen ID im Dashboards ersichtlich.

![Space-ID](../space-id.png)


### Applikationsbenutzer anlegen

Ausserdem benötigen wir einen Applikationsbenutzer, um Isotope Zugang zur PostFinance API zu geben.

![Applikationsbenutzer anlegen](../api-benutzer.png)

Geben Sie dem Benutzer einen Namen der sich auf den Shop bezieht, z.B. die verwendete Domain. Danach erhalten Sie die
Zugriffsdetails, welche im Isotope Zahlungsmodul konfiguriert werden müssen. Notieren Sie sich die **Benutzer-ID** sowie
den **Authentication Key**.

Ausserdem muss der Applikationsbenutzer eine Rolle für den Zugriff auf den entsprechenden Space erhalten. Fügen Sie
dazu eine neue Space-Rolle hinzu.
![Applikationsbenutzer-Rollen zuweisen](../api-rollen.png)



[website]: https://checkout.postfinance.ch/
