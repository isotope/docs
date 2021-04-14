---
title: "Gateways"
description: "Die Shop-Konfiguration - Allgemeine Einstellungen - Benachrichtigszentrum - Gateways."
aliases:
    - /de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-gateways/
weight: 10    
---


Ein Gateway bezeichnet den Weg, mit dem eine <docrobot_route name="notifications_messages">Nachricht</docrobot_route> seinen Empfänger erreicht.
Beispiele für Gateways:

* E-Mail
* SMS
* Brieftaube
* File Transfer Protocol (FTP)

> Warum benötige ich das?

* SMS-Benachrichtigung einer bestimmten Abteilung?
* Abspeichern von Daten als CSV-Datei?
* E-Mail an Shop-Admin via anderen SMTP-Server als Bestellbestätigung an Besucher?

> Was mache ich jetzt?

Es ist davon auszugehen, dass dir das mitgelieferte Email-Gateway völlig ausreicht. Du legst dir also im Prinzip einfach nur folgende Konfiguration an und speicherst diese:

![E-Mail Gateway](email_gateway.png)

{{% notice warning %}}<p>Ohne spezielle Einstellungen versucht Contao die E-Mails über sendmail (https://en.wikipedia.org/wiki/Sendmail) zu versenden. Je nach Hosting-Anbieter steht sendmail allerdings nicht zur Verfügung und es muss auf eine Alternative ausgewichen werden. Dies könnte bspw. der direkte Versand via SMTP sein. Hier hast du die Möglichkeit entweder via <code>parameters.yml</code> die globalen Contao-Einstellungen zu überschreiben (Richtige Einrückung beachten und Leerzeichen statt Tabs verwenden) oder eben für nur ein spezifisches Gateway die Einstellungen anzupassen.</p>{{% /notice %}}
