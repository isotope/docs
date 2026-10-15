# Fehlerbehebung

Beginne beim kleinsten fehlschlagenden Schritt. Erfasse URL, installierte Versionen, Kundenzustand, aktive Shopkonfiguration, Warenkorbinhalt und letzte Änderungen. Verwende Testdaten zur Reproduktion.

## Ein Produkt fehlt

| Prüfung | Warum sie wichtig ist |
| --- | --- |
| Produktveröffentlichung und Daten | Ein gespeichertes Produkt kann dennoch nicht verfügbar sein |
| Kategorieseitenzuweisung | Listen lesen seitenbasierte Kategorien |
| Kategorieumfang der Liste | Die aktuelle Seite schließt Unterseitenzuweisungen möglicherweise nicht ein |
| Veröffentlichung von Seite/Artikel/Element | Umgebende Contao-Inhalte müssen sichtbar sein |
| Produkt-/Mitgliederschutz | Der Besucher gehört möglicherweise nicht zur erlaubten Gruppe |
| Aktive Filter | Ein vorheriger Filter kann das Produkt ausschließen |
| Varianten | Benötigte Kindprodukte sind möglicherweise unveröffentlicht oder unvollständig |

Teste mit einer neuen Besuchersitzung und einer einfachen Liste, bevor du die Datenbank änderst.

## Produktdetails öffnen sich nicht

Prüfe den Lesermodus der Kategorie. Konfiguriere bei separaten Leserseiten die Leserseite für **jede** Kategorie. Die Einstellung wird nicht vererbt. Prüfe, ob das Ziel ein Produktleser-Element enthält und der Produktalias gültig ist.

Teilen sich Liste und Leser eine Seite, aktiviere das Ausblenden der Liste im Lesermodus. Ist der Lesermodus deaktiviert, sind Detaillinks für diese Kategorie absichtlich nicht verfügbar.

## Der Preis ist falsch oder fehlt

Prüfe die Preisfelder des Produkttyps und ob Preise zum Elternprodukt oder zu Varianten gehören. Prüfe bei erweiterten Preisen ersten passenden Eintrag, Staffel ab Menge 1 und Rückfallpreis.

Prüfe enthaltenen Satz, zusätzliche Sätze und Regeln der Steuerklasse. Untersuche dann Netto-/Brutto-/Fest-Modus und Währungsfaktor der aktiven Konfiguration. Ändere jeweils nur eine Variable und vergleiche Netto, Steuer und Brutto getrennt.

Eine höhere Mengenstaffel erzwingt bei Isotopes Berechnung des niedrigsten berechtigten Preises keinen höheren Stückpreis.

## Eine Versand- oder Zahlungsart fehlt

1. Prüfe, ob die Methode aktiviert ist.
2. Prüfe ihre Auswahl in der aktiven Shopkonfiguration.
3. Prüfe, ob ihre Regel aktiviert ist und zutrifft.
4. Prüfe Produkttypeinschränkungen für den gesamten Warenkorb.
5. Prüfe beim Versand Gewichte und Versandbedarf.
6. Prüfe bei Zahlung erlaubte Versandkombinationen einschließlich Warenkörben ohne Versand.
7. Prüfe, ob der Methodentyp tatsächlich durch das installierte Release oder die Erweiterung registriert ist.

Eine leere Methodenliste ist meist ein Konfigurations-/Verfügbarkeitsproblem und kein fehlendes Kassentemplate.

## Die Kasse leitet um oder schließt nicht ab

Prüfe, ob das Ziel nach Bestellabschluss Bestelldetails statt nur eines Dankestexts enthält. Prüfe Pflichtformulare und verfügbare Methoden.

Teste bei Mitgliedspflicht mit einem angemeldeten Mitglied. Lass bei wiederholter Anmeldung deine technische Betreuung den [Versionshinweis zur Mitgliederbestellung](../developers/version-notes.md) prüfen.

Existiert nach einem Fehler bereits eine Bestellung, prüfe diese, bevor du den Kunden erneut bestellen lässt. Der Fehler könnte nach dem Anlegen in Benachrichtigungs- oder Zahlungsabwicklung liegen.

## Die Zahlung bleibt ungeklärt

Lies Zahlungsstatus und Transaktionsverlauf der Bestellung und prüfe dann den Anbieter. Prüfe mit den Integrationsverantwortlichen Kontokonfiguration, Betrag/Währung, Erreichbarkeit von Rückrufen und Statuszuordnungen.

Markiere eine Bestellung nicht allein deshalb manuell als Bezahlt, weil der Kunde eine wie ein Erfolg aussehende Seite erreicht hat. Gleiche den maßgeblichen Zahlungsnachweis ab.

## Es kommt keine E-Mail an

Prüfe die in der Kasse gewählte Benachrichtigung, Benachrichtigungstyp, aktive Nachricht, Sprache, Empfängertoken und Mailtransport. Sieh Mailprotokolle oder Zustellergebnisse ein.

Eine Gastbenachrichtigung kann keine Mitgliederdaten voraussetzen. Roher Text `##token##` weist auf nicht unterstützte Syntax bzw. Kontext oder einen Schreibfehler hin. Eine leere Ersetzung kann fehlende Daten anzeigen.

## Ein Dokument ist kein PDF

Der Dokumenttyp Standard erzeugt HTML. Lass bei PDF-Bedarf deine technische Betreuung einen kompatiblen PDF-Dokumenttyp konfigurieren.

## Mit hilfreichen Nachweisen weitergeben

Liefere genaue Reproduktionsschritte, Soll-/Istergebnis, Testbestellreferenz, Versionen und den relevanten Fehlerauszug. Entferne private Kundendaten und Zugangsdaten. Gib an, ob das Problem mit Standardtemplates und ohne die beteiligte optionale Integration auftritt.
