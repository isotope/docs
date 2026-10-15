# Bestelldokumente

Ein Dokument ist ein erzeugtes Schriftstück zu einer Bestellung, etwa eine Rechnung oder ein Packdokument. Eine Dokumentdefinition beschreibt die Erzeugung. Die erzeugte Datei gehört zu einer bestimmten Bestellung und hat einen eigenen Erstellungszeitpunkt und eine eigene Nummer.

Eine Bestellnummer identifiziert den Kauf. Eine Dokumentnummer identifiziert ein erzeugtes Dokument. Halte diese Rollen in Templates und internen Verfahren auseinander.

## Definition konfigurieren

1. Öffne **Konfiguration → Dokumente**.
2. Erstelle eine Definition und wähle den verfügbaren Dokumenttyp.
3. Gib internen Namen, Dokumenttitel und Dateinamenmuster ein.
4. Lege bei Bedarf Nummernpräfix und Mindestnummernlänge fest.
5. Wähle Template und vom Typ unterstützte optionale Galerie-/Logoeinstellungen.
6. Speichere und zeige eine Vorschau für eine repräsentative Testbestellung an.

Ein Dateinamenmuster kann unterstützte Collection-Tokens verwenden, etwa das dokumentierte Muster `invoice_##collection_document_number##`. Prüfe Vorschau und erzeugten Dateinamen in deinem Release. Nimm nicht an, dass Benachrichtigungstokens in jedem Dokumentfeld gleich funktionieren.

## Vorschau und Erstellung

Die Vorschau prüft Aussehen und Inhalt. Das Erstellen vergibt eine Dokumentnummer und speichert die erzeugte Datei bei der Bestellung.

Verwende beim Anpassen des Templates die Vorschau. Wiederholtes Erstellen zum Layouttest kann zusätzliche nummerierte Datensätze erzeugen. Lege fest, wann Mitarbeiter die Endfassung erstellen und wie Korrekturen behandelt werden.

Erzeugte Dateien müssen zusammen mit ihren Datenbankdatensätzen gesichert werden. Eine Datenbankzeile allein enthält nicht den gespeicherten Dokumentinhalt.

## Ausgabeformat wählen

Der Dokumenttyp Standard erzeugt **HTML**. Prüfe, ob dieses Format zur Nutzung durch Mitarbeiter und Kunden passt.

Wenn dein Ablauf PDF-Dateien benötigt, lass deine technische Betreuung einen kompatiblen PDF-Dokumenttyp konfigurieren. Teste Schriften, Seitenumbrüche und Anhänge vor dem Einsatz für Kundendokumente.

## Repräsentative Bestellungen prüfen

Prüfe Vorschauen kurzer und langer Bestellungen, langer Adressen, Varianten, Kundenoptionen, gegebenenfalls Rabatte, gemischter Steuern und Versandkosten. Achte darauf, dass Dokumenttitel und Summen das gewünschte Dokument beschreiben und keine irreführenden Formulierungen übernehmen.

Lass erforderliche Geschäftsinformationen und Nummerierung für deinen Shop prüfen. Eine vorhandene Rechnungsvorlage belegt nicht ihre Eignung für jedes Geschäft.

## Dokumente anhängen

Die Benachrichtigungsunterstützung hängt von der gewählten Benachrichtigungs- und Dokumentintegration ab. Prüfe, ob ein erzeugter Anhang korrekt öffnet und zur richtigen Bestellung gehört. Ein Tokenname allein belegt nicht, dass eine Datei automatisch erzeugt und angehängt wird.
