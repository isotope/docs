# Produkt-Verwaltung

Nachdem Sie die Grundkonfiguration des Shops vorgenommen haben, können Sie sich um die Produkte kümmern. Entsprechend dem gewählten Produkttyp werden beim Erstellen eines Produktes verschiedene Attribute (Eingabefelder) angeboten.

Jedes Produkt kann mehreren Kategorien zugewiesen werden, Kategorien entsprechen hierbei der Seitenstruktur. Sie können beispielsweise definieren, dass ein Produkt sowohl auf der Seite „T-Shirts“ als auch auf der Startseite des Shops angezeigt wird. Welche Attribute im Frontend ausgegeben werden, hängt vom verwendeten Listen- und Detail-Template ab. Nur die Standard-Attribute werden automatisch ausgegeben.


## Produktbilder

Isotope eCommerce verfügt über eine Bildverwaltung, welche nicht dem Contao-Standard entspricht. Produktbilder werden nicht über die Dateiverwaltung hinaufgeladen, sondern direkt im Produkt selber. Der wichtigste Grund für dieses Spezialverfahren ist, dass bei 1000 Produkte mit jeweils 5 Bildern über 5000 Bilder in der Dateiverwaltung wären. Dadurch wäre die Dateiverwaltung nahezu unbrauchbar.

Dateien werden im Root-Verzeichnis /isotope/ gespeichert. Wenn Sie eine Datei hinauf laden, wird diese ins entsprechende Verzeichnis kopiert. Laden Sie dasselbe Bild für mehrere Produkte hinauf, wird dieses nur einmal gespeichert, vorausgesetzt Sie haben jeweils denselben Dateinamen verwendet. Unterschiedliche Dateien mit demselben Dateinamen werden dabei automatisch erkannt und eindeutig benannt.

![](https://raw.github.com/isotope/docs/1.4/de/manual/images/4-products_01.png)

Um ein neues Bild hinauf zu laden, wählen Sie die Datei und speichern Sie das Produkt. Nach erfolgreichem Upload wird eine Vorschau des Bildes direkt im Produkt angezeigt, daneben können Sie einen Alternativtext und eine Beschreibung eingeben. Bei mehreren Bilder können Sie rechts über die Pfeile die Reihenfolge wählen, das oberste Bild wird jeweils als Hauptbild des Produktes verwendet.


### Import assets

In der Übersicht der Produkte finden Sie im Tools-Menü die Option „Import assets“. Mit Hilfe dieser Funktionen können Sie Bilder, welche sich bereits auf dem System befinden (z.B. via FTP hochgeladen wurden) den entsprechenden Produkten zuordnen. Der Dateiname muss entweder mit der Artikelnummer des Produktes beginnen, oder sich in einem entsprechend benannten Unterordner befinden.

Beachten Sie dass sich diese Funktion noch in der Testphase befindet und noch nicht ausreichend getestet wurde. Es werden keine Daten gelöscht, allerdings kann es sein dass nicht alle Bilder korrekt zugewiesen werden.


## Sprachen

Leider ist die bei Contao übliche Mehrsprachigkeit – das mehrfache Anlegen eines Inhaltes – bei Produkten nicht möglich. Produkte können einen Lagerbestand haben, welcher über alle Sprachen hinweg identisch ist. Aus diesem Grund wurde für Produkte eine andere Lösung entwickelt. Wenn Sie im Produkttyp zusätzliche Sprachen aktiviert haben, stehen die entsprechenden Optionen zur Verfügung.

![](https://raw.github.com/isotope/docs/1.4/de/manual/images/4-products_02.png)

Beim Bearbeiten eines Produktes wird in der linken oberen Ecke eine Auswahl der Sprache angeboten. Wählen Sie hier eine bestimmte Sprache, zeigt Contao nur noch Attribute an, welche übersetzt werden können. Die Frontend-Ausgabe erkennt dies automatisch und lädt die Übersetzungen der entsprechenden Felder beim Anzeigen eines Produktes.


## Varianten anlegen

Sind Produkte mit entsprechendem Produkttyp vorhanden, steht in der Produktliste eine neue Option „Variante hinzufügen“
zur Auswahl. Mittels dieser Operation können Sie bei passenden Produkte eine neue Variante anlegen.


### Varianten-Generator

Um das Anlegen von vielen Varianten zu vereinfachen, können Sie den Varianten-Generator benutzen. Klicken Sie dazu auf das Zauberstab-Symbol und im erscheinenden Untermenü auf die entsprechende Option. In der folgenden Anzeige können Sie wählen, welche Options-Kombinationen generiert werden sollen. Selbstverständlich werden bereits vorhandene Kombinationen nicht nochmals erzeugt.


### Quick-Edit

Direkt nach dem Generieren von Varianten erscheint der Quick-Edit Modus. Sie können diesen auch über das Zauberstab-Symbol aufrufen. Der Quick-Edit Modus erlaubt das übersichtliche Bearbeiten von Varianten, es kann jeweils die Artikelnummer, der Preis sowie der Veröffentlicht-Status konfiguriert werden.


### Vom Basisprodukt erben

Varianten können bekanntlich nicht nur die Attribute enthalten, welche im Quick-Edit Modus bearbeitet werden können. Sie können in einer Variante auch die Beschreibung anpassen. Da beim Generieren von Produkten diese – möglicherweise obligatorischen – Felder leer wären, gibt es die Option „Use default value“. Ist dieser Haken aktiv, wird der Wert vom Elternelement automatisch geerbt. Die Quick-Edit Attribute (Artikelnummer, Preis, veröffentlicht) können nicht vererbt werden!


## Weitere Funktionen


### Verknüpfte Produkte

Sie können dem Besucher im Frontend eine Liste von Produkten anzeigen, welche zum aktuellen Produkttyp passt. Verknüpfte Produkte müssen kategorisiert werden. Legen Sie zuerst über die Shop-Konfiguration entsprechende Kategorien (z.B. „Zubehör“, „Passt dazu“) an, danach können Sie in der Produktverwaltung die verknüpften Produkte über das
Zauberstab-Menü öffnen. Jede Kategorie kann nur einmal pro Produkt verwendet werden.

Um die Übersichtlichkeit bei einer hohen Anzahl an Produkten zu gewährleisten, wird nicht eine Liste aller Produkte angezeigt, stattdessen Sie können nach Produkten suchen. In der Suche werden die bekannten Standardfelder wie Artikelnummer, Name und Beschreibung berücksichtigt. Klicken Sie dann in den Suchresultaten das gewünschte Produkt an, um es zur Liste der verknüpften Produkte hinzu zu fügen.

Verknüpfte Produkte können Sie danach über das entsprechende Frontend-Modul auf der Produkt-Detailansicht ausgeben.


### 	Downloads

Wenn Sie Ihren Kunden bezahlte Download-Artikel anbieten wollen, können Sie dies mit Isotope eCommerce tun. Sie können pro Basis-Produkt mehrere Downloads hinzufügen, wenn die entsprechende Option im Produkttyp aktiv ist. Zur Zeit ist es noch nicht möglich, verschiedene Downloads für Produkt-Varianten anzubieten.

Download-Artikel stehen dem Benutzer nach erfolgreicher Bestellung über das Frontend-Modul der Bestellhistorie/Bestelldetails zur Verfügung. Downloads können erst herunter geladen werden, wenn der Bestellstatus auf „abgeschlossen“ steht, oder ein „Bezahlt“-Datum vorhanden ist.

**Stellen Sie unbedingt sicher, dass Sie Ihre Download-Artikel in der Dateiverwaltung geschützt sind!** Andernfalls kann über ein direktes Aufrufen der URL die Datei herunter ohne bezahlen geladen werden. Contao bietet über die Dateiverwaltung die Möglichkeit, ganze Verzeichnisse zu schützen (Schloss-Symbol). Prüfen Sie aber unbedingt auch, ob es korrekt funktioniert.