# Mitglieder und Gäste

Ein Gast kauft ohne angemeldetes Konto. Ein Mitglied verwendet ein Contao-Frontend-Konto. Wähle den Ansatz passend zu deiner Kundenbeziehung.

Gastbestellungen ersparen Gelegenheitskäufern die Kontoeinrichtung. Mitgliedskonten sind für Stammkunden, gespeicherte Adressen, geschützte Kataloge und kundenspezifische Bedingungen hilfreich.

## Bestellmethode wählen

Das Kasse-Element bietet nur Gäste, Mitgliedschaft erforderlich oder beides an. Diese Einstellung steuert den Bestellablauf. Sie erstellt nicht automatisch einen vollständigen Registrierungs- und Kontobereich.

Bereite für Mitgliederbestellungen Contao-Anmeldung, gegebenenfalls Registrierung, Passwortwiederherstellung und Seiten für persönliche Daten vor. Konfiguriere ein sinnvolles Ziel nach der Anmeldung.

Teste den vollständigen Bestellvorgang eines angemeldeten Mitglieds, bevor du eine Mitgliedschaft vorschreibst. Wenn ein angemeldeter Kunde immer zur Anmeldung zurückkehrt, lass deine technische Betreuung den [Versionshinweis zur Mitgliederbestellung](../../developers/version-notes.md) prüfen.

## Adressbuch

Platziere das Adressbuch-Element im Mitgliederbereich. Prüfe, ob Kunden die für die Kasse benötigten Adressen verwalten können und ein Mitglied keine fremden Daten sieht.

Die Shopkonfiguration bestimmt Rechnungs- und Lieferfelder, Pflichtangaben und erlaubte Länder. Kontoformulare und Kasse sollten übereinstimmende Auswahlmöglichkeiten bieten.

## Bestellverlauf und Details

Verwende das Bestellverlauf-Element in einem geeigneten Mitgliederbereich, wähle die anzuzeigenden Shopkonfigurationen und verbinde das Detailziel. Ohne ausgewählte Konfigurationen zeigt das Element nichts. Verwende das Bestelldetails-Element für eine einzelne Bestellung.

Das Detailelement bietet eine Anmeldepflicht für Mitgliederbestellungen. Ein anderes angemeldetes Mitglied erhält keinen Zugriff. Bei einem nicht angemeldeten Besucher hängt der Zugriff auf eine Mitgliederbestellung auch von der Anmeldepflicht ab. Aktiviere und teste den gewünschten Schutz.

Gastbestellungen verwenden individuelle Bestelllinks statt Mitgliederzugehörigkeit. Behandle diese Links als private Kundendaten und halte Bestelldetails aus öffentlichen Indizes und gemeinsamen Caches heraus.

## Mitgliedergruppen

Gruppen können Produktsichtbarkeit und regelbasierte Preise oder Methoden steuern. Teste ein gruppengeschütztes Produkt abgemeldet, als Mitglied außerhalb und innerhalb der Gruppe.

Ein Gruppenname wie „Geschäftskunden“ erzeugt nicht automatisch einen Rabatt. Weise einem erweiterten Preiseintrag eine Mitgliedergruppenregel zu und prüfe den resultierenden Preis.

## Mitarbeiterkonten

Backendbenutzer sind von Mitgliedern getrennt. Produktredakteure und Bestellbearbeiter benötigen Backendberechtigungen. Gib Kunden keine Backendkonten, um einen Bestellverlauf bereitzustellen.

Verwandte Einrichtungsthemen findest du unter [Mitarbeiterzugriff](../general/access.md) und [Internationale Shops](../general/international.md).
