# Steuersätze konfigurieren

Ein Steuersatz speichert einen Prozentsatz, eine Bezeichnung und eine optionale Bedingungsregel. Steuerklassen verweisen auf Sätze. Der Steuersatzdatensatz selbst wird nicht jedem Produkt einzeln zugewiesen.

## Steuersatz erstellen

1. Öffne **Konfiguration → Steuersätze**.
2. Vergib einen klaren internen Namen.
3. Gib eine Bezeichnung für Kunden ein.
4. Gib den Prozentsatz als Zahl ein, etwa `10` für ein fiktives Beispiel mit 10 %.
5. Wähle eine Regel, wenn der Satz nur in einem bestimmten Kontext gelten soll.
6. Speichere und wähle ihn in der passenden [Steuerklasse](tax-classes.md).

Ein Satz ohne Regel trifft ohne Bedingungseinschränkung zu. Eine ausgewählte Regel muss aktiviert sein und ihre Bedingungen müssen zutreffen.

## Anwendbarkeit mit Regeln steuern

Steuersätze verwenden den [Regelbaukasten](../rules.md). Für ein zielabhängiges Beispiel verwendest du eine Adressbedingung und wählen Rechnungs- oder Lieferadresse als Prüfziel.

Prüfe bei Regionseinschränkungen den [Implementierungshinweis](../../developers/version-notes.md) zum Abgleich von Unterregionen in dieser Revision, bevor du dich darauf verlässt.

Übernimm keine alten Anleitungen, die Land- und Postleitzahlfelder direkt am Steuersatz erwarten. Erstelle diese Bedingung in einer Regel und verweise vom Satz darauf.

Der Shop verwendet auch vor der Kasse einen Adresskontext, einschließlich der Standardwerte der Shopkonfiguration. Prüfe, was Kunden vor der Adresseingabe und nach deren Änderung sehen.

## Überschneidende Steuersätze

Isotope kann mehrere passende Sätze einer Klasse sammeln. Es entscheidet nicht anhand ähnlicher Namen, dass zwei Sätze Alternativen sind. Wenn genau einer gelten soll, müssen sich ihre Bedingungen gegenseitig ausschließen.

Im dokumentierten Rechner werden Sätze auf den Nettobetrag berechnet. Gehe nicht von einer aufeinanderfolgenden, kumulierten Besteuerung bereits versteuerter Beträge aus. Lass darüber hinausgehende Anforderungen von einem Entwickler beurteilen.

## Horizontale und vertikale Berechnung

Die Shopkonfiguration bietet zwei Modi:

- **Horizontal** rundet die berechnete Steuer auf der einzelnen Berechnungsstufe, bevor Beträge zusammengeführt werden.
- **Vertikal** behält dort die Genauigkeit bei und rundet später im gemeinsamen Berechnungs- und Anzeigeprozess.

Ein kleines Beispiel zeigt den Unterschied. Zwei separate Nettobeträge von 0,05 ergeben bei fiktiven 10 % jeweils 0,005 Steuer. Auf jeweils 0,01 gerundet ergeben sie zusammen 0,02. Erst zusammengefasst ergeben sie 0,01.

Dies veranschaulicht Rundung und ist keine Zusage darüber, wie jeder Warenkorb seine Positionen gruppiert. Teste deine tatsächlichen Positionsmengen und Steuerklassen. Wähle einen zur Buchhaltung und Zahlungsabwicklung passenden Modus und bleibe dabei.

## Einen Steuersatz ändern

Ändere einen laufenden Prozentsatz nicht beiläufig. Lege das Gültigkeitsdatum fest und teste Bedingungen, Preise und neue Bestellungen zunächst auf einer Kopie. Bewahre historische Bestell- und Dokumentdatensätze auf. Eine aktuelle Katalogeinstellung ersetzt nicht die Steuerinformationen einer früheren Bestellung.
