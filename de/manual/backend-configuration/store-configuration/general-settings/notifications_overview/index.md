# Benachrichtigungen (Übersicht)

<docrobot_image path="backend-configuration/store-configuration/general-settings/notifications_overview/navigation.png" alt="Navigation des Benachrichtigungszentrums">

<docrobot_new_in_version version="2.0"><p>Die Isotope eCommerce-eigenen E-Mail-Benachrichtigungen wurden in das `Benachrichtigungszentrum` ausgelagert. Du wirst feststellen, dass du bei Klick auf `Benachrichtigungen` zum entsprechenden Menüpunkt weitergeleitet wirst. Dies wurde eingebaut, um den Einstieg für Isotope 1.4-Kenner zu erleichtern.</p></docrobot_new_in_version>

Stellst du dir das `Benachrichtigungszentrum` losgelöst von Isotope eCommerce vor, so sollte einiges von Beginn weg klarer erscheinen. Es wurde unabhängig entwickelt und hat sich zum Ziel gesetzt, als zentrale Komponente für beliebige andere Erweiterungen und deren Benachrichtigungen zu fungieren. Die Anforderungen für Benachrichtigungen lassen sich nämlich gemeinsam festhalten:

* Eine Benachrichtigung hat immer einen Auslöser und da bei diesem Auslöser potenziell mehrere verschiedene Nachrichten ausgelöst werden sollen, besteht eine Benachrichtigung aus einer oder mehreren Nachrichten.

<docrobot_message type="warning">Merke dir die unterschiedliche Verwendung von <code>Benachrichtigung</code> und einer einzelnen <code>Nachricht</code>. Eine <code>Benachrichtigung</code> ist ein Gefäss von einer oder mehreren <code>Nachrichten</code>.</docrobot_message>

* Eine Nachricht muss potenziell in verschiedene Sprachen übersetzbar sein.
* Eine Nachricht definiert sich nicht durch das Wort "E-Mail". Es ist folglich für eine Nachricht irrelevant wohin oder mit welchem Hilfsmittel (Gateway) sie verschickt wird.
* Eine Nachricht besteht nicht zwingend aus menschenlesbarem Text. Ein Austausch von Maschine zu Maschine kann ebenso als "Nachricht" bezeichnet werden.

Es ergibt sich folgendes Verhalten:

Zu einer einzelnen <docrobot_route name="notifications">Benachrichtigung</docrobot_route> gehören eine oder mehrere <docrobot_route name="notifications_messages">Nachrichten</docrobot_route>, welche in verschiedenen <docrobot_route name="notifications_languages">Sprachen</docrobot_route> über ein beliebiges <docrobot_route name="notifications_gateways">Gateway</docrobot_route> versendet werden.
