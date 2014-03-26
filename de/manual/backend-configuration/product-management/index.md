# Produkt-Management

Um die Produkte nach Kategorie sortiert verwalten zu können, kann der Produktverwalter/die Produktverwalterin **Produktgruppen** anlegen. Sinnvoll ist es diese nach einen bestimmten System zu benennen. Zum Beispiel können die Gruppen den Produktkategorien entsprechend benannt werden.

 Die verschiedenen Produktordner können ineinander verschachtelt werden. Immer wenn ein neues Produkt erstellt, ein Produkt kopiert oder verschoben wird, erscheinen die Produktgruppen zur Auswahl. Ist noch kein Produkt in einer der Produktgruppenordner, wird dieser **Ordner** in der normalen Produktübersicht nicht angezeigt. Die **Produkte** können mit den Produktgruppen übersichtlich verwaltet werden.

Die neue Produktverwaltung in Isotope 2.  
Zugewiesen werden die Gruppen nachdem diese angelegt sind wie gewohnt per Icon <docrobot_image path="backend-configuration/product-management/folder-network.png" alt="Prduktgruppen zuweisen Zeichen">

##Ansicht
###1. Filtermöglichkeiten Gruppen und Kategorien  
Im oberen Bereich der Produktübersicht siehst du die Filtermöglichkeiten. Zwar groß genug aber nicht gleich offensichtlich befindet sich der Button „**Gruppen**“ und daneben rechts der Button „**Seiten**“. Wenn du die Buttons klickst öffnet sich ein PopUp mit einer Radiobuttonauswahl. Hier kannst du wählen wie du die Produkte gefiltert haben möchtest. Den Filter kannst du danach wieder löschen durch die Auswahl von „Auswahl aufheben“.

Im Bereich Erweiterten Filter sind noch weitere Filtermöglichkeiten, welche sich auf Bilder, Kategorien und Einstellzeit beziehen.

###2. Sortieren 

Sortieren kannst du hier deine Produkte standardmäßig nach Name, Artikelnummer oder Alias.

Unter Sortieren findest du auch ein Seitenstruktur-Icon <docrobot_image path="backend-configuration/product-management/page.gif" alt="Produkte manuell sortieren Zeichen">   
Damit kannst du eine Kategorieseite auswählen. Nachdem du das hast kannst du die **Produkte manuell sortieren**.


##Bearbeitungsmöglichkeiten
###1. Allgemein

Der Bearbeiten-Button "**Produktgruppen**" ist ja selbsterklärend. Mit "**Anlagen importieren**" können Produktbilder schon im Vorfeld hochgeladen werden um das Produkte Einpflegen zu erleichtern.

Isotope speichert die Produktbilder unabhängig von der Dateiverwaltung aus performance-technischen Gründen in dem Ordner root/isotope ab.

Die Namen der Bilder müssen die Artikelnummer beinhalten oder den dazugehörigen Produktnamen. Isotope gleicht das ab. Programmierer können diesen Abgleich auch anpassen.

###2. Einzelnes Produkt

Als Bearbeitungsmöglichkeiten stehen hier neben dem Contao-Core bekannten **Varianten ansehen**, **Ähnliche Produkte zuweisen** und **Gruppe zuweisen**.

###3. Produktvarianten

Die Varianten kannst du **automatisch generieren** lassen oder einzeln anlegen.


##Redakteur Rechte
### Nur bestimmte Produktgruppen für einen Redakteur freigeben.
Unter Sortieren findest du auch ein Seitenstruktur-Icon <docrobot_image path="backend-configuration/product-management/isotope-rechteverwaltung.jpg" alt="Bereich Isotope in der Rechteverwaltung Zeichen">  

Mehr zur Contao-Rechteverwaltung:
https://contao.org/de/manual/3.2/system-administration.html#benutzer-und-gruppen