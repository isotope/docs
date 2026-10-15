# Preisbeispiele

Diese Beispiele erweitern das [Trail-T-Shirt-Beispiel](../concepts/example-shop.md). Alle Preise enthalten die fiktive Steuer von 10 %. Lass vor der täglichen Bearbeitung deine Shopadministration erweiterte Preise für Bekleidung aktivieren und die benötigten [Regeln](../setup/rules.md) vorbereiten. Grundlagen der Bearbeitung erklärt [Preise](prices.md).

## Ein Geschäftskundenpreis

**Ziel:** Angemeldete Mitglieder der Gruppe Geschäftskunden erhalten einen anderen Stückpreis.

1. Prüfe, ob die Mitgliedergruppe Geschäftskunden und die passende Regel verfügbar sind.
2. Öffne die erweiterten Preise des Trail-T-Shirts.
3. Ergänze zuerst einen Eintrag mit Geschäftskundenregel, Steuerklasse Standardwaren und Preis 17,60 ab Menge 1.
4. Ergänze darunter einen uneingeschränkten normalen Eintrag mit Preis 22,00 ab Menge 1 und derselben Steuerklasse.
5. Teste abgemeldet, als normales Mitglied und als Geschäftsmitglied.

Der erste passende Eintrag gewinnt. Steht der normale Eintrag zuerst, verdeckt er den Sondereintrag. Entscheide separat, ob die aktive Konfiguration Netto- oder Bruttopreise anzeigt.

## Ein Mengenrabatt

**Ziel:** Ein Trail-T-Shirt kostet 22,00, ab fünf Stück kostet jedes 19,80.

Verwende einen passenden erweiterten Preiseintrag mit Staffeln 1 → 22,00 und 5 → 19,80. Halte die Beträge in diesem Modell fallend, da Isotope den niedrigsten berechtigten Betrag auswählt.

Teste Mengen 1, 4, 5 und 6. Erwarte bei Menge 5 einen Warenbetrag von 99,00 einschließlich 9,00 Steuer, vor Versand oder anderen Kosten. Der Rabatt gilt für die Einheiten der berechtigten Position und nicht nur für den fünften Artikel.

Zeigt ein Produkttyp die niedrigste Staffel als „Ab“-Preis, mache die Mengenbedingung in der Darstellung deutlich.

## Ein zeitlich begrenzter Preis

**Ziel:** Ein Produkt verwendet in einem geplanten Zeitraum einen Sonderpreis.

Erstelle eine Datumsregel mit dem gewünschten Intervall. Setze den Aktionspreiseintrag vor einen uneingeschränkten Rückfallpreis. Teste unmittelbar vor, innerhalb und nach dem Zeitraum mit einer geeigneten Testkonfiguration und der Zeitzone der Website.

Eine Datumsregel erzeugt keine Werbetexte. Aktualisiere und teste Seiteninhalt und angezeigten Preis gemeinsam, damit sie übereinstimmen.

## Ein separater Währungspreis

Erstelle eine Regel für die betreffende Shopkonfiguration und einen passenden Preiseintrag. Prüfe Währung und Preisfaktor der Konfiguration. Ist der Eintrag bereits im Zielbetrag angegeben, kann ein zusätzlicher Umrechnungsfaktor ihn nochmals multiplizieren.

[Internationale Shops](../setup/general/international.md) erklärt das Wechselverhalten.

## Wann du eine Erweiterung benötigst

Gutscheineingabe, Einmalcodes, Einlösezähler, automatische Gratiszugaben und die Kombination von Aktionen brauchen eine Implementierung mit ausdrücklicher Unterstützung. Lege vor Auswahl oder Entwicklung fest, wie Rabatte mit Steuern, Versand, Erstattungen und mehreren Währungen zusammenwirken.
