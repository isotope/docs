# Produkt-Management

Um die Produkte nach Kategorie sortiert verwalten zu können, kann der Produktverwalter/die Produktverwalterin **Produktgruppen** anlegen. Sinnvoll ist es diese nach einen bestimmten System zu benennen. Zum Beispiel können die Gruppen den Produktkategorien entsprechend benannt werden.

 Die verschiedenen Produktordner können ineinander verschachtelt werden. Immer wenn ein neues Produkt erstellt, ein Produkt kopiert oder verschoben wird, erscheinen die Produktgruppen zur Auswahl. Ist noch kein Produkt in einer der Produktgruppenordner, wird dieser **Ordner** in der normalen Produktübersicht nicht angezeigt. Die **Produkte** können mit den Produktgruppen übersichtlich verwaltet werden.

<p>Zugewiesen werden die Gruppen nachdem diese angelegt sind wie gewohnt per Icon (<docrobot_image path="backend-configuration/product-management/folder-network.png" alt="Prduktgruppen zuweisen Zeichen">)</p>

##Ansicht
###1. Filtermöglichkeiten Gruppen und Kategorien  
Im oberen Bereich der Produktübersicht siehst du die Filtermöglichkeiten. Zwar groß genug aber nicht gleich offensichtlich befindet sich der Button „**Gruppen**“ und daneben rechts der Button „**Seiten**“. Wenn du die Buttons klickst öffnet sich ein PopUp mit einer Radiobuttonauswahl. Hier kannst du wählen wie du die Produkte gefiltert haben möchtest. Den Filter kannst du danach wieder löschen durch die Auswahl von „Auswahl aufheben“.

Im Bereich Erweiterten Filter sind noch weitere Filtermöglichkeiten, welche sich auf Bilder, Kategorien und Einstellzeit beziehen.

###2. Sortieren 

Sortieren kannst du hier deine Produkte standardmäßig nach Name, Artikelnummer oder Alias.

<p>Unter Sortieren findest du auch ein Seitenstruktur-Icon (<docrobot_image path="backend-configuration/product-management/page.gif" alt="Produkte manuell sortieren Zeichen">)</p>
   
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

#### Übersicht über die Bearbeitungsmöglichkeiten eines Produktes

##### Pflicht-Attribute, nicht ausblendbar

<table>
	<thead>
		<tr>
			<th>Einstellung</th>
			<th>Standardeinstellung</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Produkttyp</td>
			<td>Als Standard deklarierter Produkttyp</td>
			<td>Produkttypen sind im Produkttypen-Manager definiert</td>
		</tr>
		<tr>
			<td>Kategorien</td>
			<td>-</td>
			<td>Wählen Sie eine Kategorie für dieses Produkt. Seitenbasierte Kategorien nutzen die Vorteile der Contao-Seitenfunktionen wie Navigationsautomatik, Seitenschutz, Templates und volle Einbindung mit Inhaltselementen.</td>
		</tr>
		<tr>
			<td>Alias</td>
			<td>Wird anhand des Namens generiert</td>
			<td>Muss eindeutig sein.</td>
		</tr>
		
		<tr>
			<td>Name</td>
			<td>-</td>
			<td>Name des Produktes</td>
		</tr>
		<tr>
			<td>Bilder</td>
			<td>-</td>
			<td>Bildauswahl per Upload vom PC</td>
		</tr>
		<tr>
			<td>Produkt veröffentlichen</td>
			<td>0</td>
			<td>Wenn Checkbox ausgewählt ist ist das Produkt veröffentlich</td>
		</tr>
		<tr>
			<td>Startdatum</td>
			<td>-</td>
			<td>Hier lässt sich ein Datum einstellen für den Tag an dem das Produkt veröffentlicht werden soll.</td>
		</tr>
		<tr>
			<td>Stopdatum</td>
			<td>-</td>
			<td>Hier lässt sich ein Datum einstellen für den Tag an dem das Produkt deaktiviert werden soll.</td>
		</tr>
		<tr>
			<td>Artikelnummer</td>
			<td>-</td>
			<td>Wird nicht automatisch generiert. Es muss im Produkttyp konfiguriert werden ob das Attribut hier zur Verfügung steht oder in den Produktvarianten.</td>
		</tr>
		
	</tbody>
</table>


##### Standard-Attribute, ein- und ausblendbar
	Es muss im Produkttyp konfiguriert werden ob das Attribut hier zur Verfügung steht oder in den Produktvarianten.	

<table>
	<thead>
		<tr>
			<th>Einstellung</th>
			<th>Standardeinstellung</th>
			<th>Beschreibung</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Artikelnummer</td>
			<td>-</td>
			<td>Wird nicht automatisch generiert. Es muss im Produkttyp konfiguriert werden ob das Attribut hier zur Verfügung steht oder in den Produktvarianten.</td>
		</tr>
		<tr>
			<td>Teaser</td>
			<td>-</td>
			<td>Kurze Produktbeschreibung für den Käufer. Wird in der Produktliste im Frontend angezeigt.</td>
		</tr>
		<tr>
			<td>Beschreibung</td>
			<td>-</td>
			<td>Ausführliche Produktbeschreibung für den Käufer. Wird in dem Produktleser im Frontend angezeigt.</td>
		</tr>
		<tr>
			<td>Meta-Beschreibung</td>
			<td>-</td>
			<td>SEO (Suchmaschinenoptimierung) Beschreibung für das Produkt</td>
		</tr>
		<tr>
			<td>Meta keywords</td>
			<td>-</td>
			<td>SEO (Suchmaschinenoptimierung) Keywords für das Produkt</td>
		</tr>
		<tr>
			<td>Meta-Titel</td>
			<td>-</td>
			<td>SEO (Suchmaschinenoptimierung) Titel für das Produkt</td>
		</tr>
		<tr>
			<td>Produkt schützen</td>
			<td>-</td>
			<td>Wenn Checkbox aktiviert können bestimmte Mitgliedergruppen ausgewählt werden.</td>
		</tr>
		<tr>
			<td>Nur für Gäste anzeigen</td>
			<td>-</td>
			<td>Wenn Checkbox aktiviert, wird das Produkt nur Gästen angezeigt.</td>
		</tr>
		<tr>
			<td>CSS-ID/Klasse</td>
			<td>-</td>
			<td>Links kann dem Produkt eine ID zugewiesen werden und Rechts CSS-Klassen.</td>
		</tr>
		<tr>
			<td>Preis</td>
			<td>-</td>
			<td>Preis des Produktes</td>
		</tr>
		<tr>
			<td>Grundpreis-Menge</td>
			<td>-</td>
			<td>Ein Grundpreis für eine bestimmte Menge.</td>
		</tr>
		<tr>
			<td>Versandgewicht</td>
			<td>-</td>
			<td>Spielt für die Versandkostenberechnung eine Rolle.</td>
		</tr>
		<tr>
			<td>Vom Versand ausschliessen </td>
			<td>-</td>
			<td>Hilfreich für Download-Artikel oder Produkte welche nicht Versendet werden.</td>
		</tr>


	</tbody>
</table>

##### Eigene Attribute, ein- und ausblendbar
	Es muss im Produkttyp konfiguriert werden ob das Attribut hier zur Verfügung steht oder in den Produktvarianten. 
	
Siehe dazu auch <docrobot_route name="attributes">Attribute</docrobot_route> 
	


##Redakteur Rechte
### Nur bestimmte Produktgruppen für einen Redakteur freigeben.
Unter Sortieren findest du auch ein Seitenstruktur-Icon <docrobot_image path="backend-configuration/product-management/isotope-rechteverwaltung.png" alt="Bereich Isotope in der Rechteverwaltung Zeichen">  

Mehr zur Contao-Rechteverwaltung: <a href="https://contao.org/de/manual/3.2/system-administration.html#benutzer-und-gruppen" >Contao Handbuch - Benutzer und Gruppen</a>
