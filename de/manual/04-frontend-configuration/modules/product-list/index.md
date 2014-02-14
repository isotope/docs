# Produktliste

Das Modul `Produktliste` ist für die Ausgabe von Produkten zuständig. Es bietet eine Vielzahl an Einstellungen welche nachfolgend beschrieben sind.

## Modul-Konfiguration

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
			<td>Gesamtzahl der Beiträge</td>
			<td>0</td>
			<td>Wenn du eine Zahl grösser als 0 eingibst, werden maximal diese Anzahl an Produkten aufgelistet. Das kann beispielsweise nützlich sein, um die neusten 4 Produkte auf der Startseite anzuzeigen.</td>
		</tr>
		<tr>
			<td>Elemente pro Seite</td>
			<td>0</td>
			<td>Änderst du hier nichts, werden alle gefundenen Produkte ohne Pagination auf der Seite ausgegeben. Ansonsten findet ein Seitenumbruch nach der eingegebenen Anzahl an Produkten statt.</td>
		</tr>
		<tr>
			<td>Kategorie-Anwendungsbereich</td>
			<td>-</td>
			<td>Jede einzelne Option ist im Contao-internen Helpwizard (<img src="[docrobot_root]/images/helpwizard.gif" width="14" height="14" alt="helpwizard">) beschrieben.</td>
		</tr>
		<tr>
			<td>Bedingung</td>
			<td>-</td>
			<td>Hier kannst du selber eigene SQL-Bedingungen eingeben, welche an den entsprechenden Query angehängt und ausgeführt werden.</td>
		</tr>
		<tr>
			<td>Filter-Module</td>
			<td>-</td>
			<td>Da du potenziell mehrere Filtermodule und Produktlisten auf einer Seite einsetzt, kannst du hier auswählen, auf welche Filtermodule die Produktliste reagieren soll.</td>
		</tr>
		<tr>
			<td>Filterung für neue Produkte</td>
			<td>Zeige alle Produkte</td>
			<td>Diese Einstellung bezieht sich auf die in der <docrobot_route name="configuration">Shop-Konfiguration</docrobot_route> optional zu konfigurierende Einstellung für neue Produkte. Solltest du dort z.B. 30 Tage eingestellt haben, kan nst du hier "Zeige nur die neuen Produkte" auswählen. Tust du das, werden nur die Produkte aufgelistet, die innerhalb der letzten 30 Tage angelegt wurden. Die Option "Zeige alte Produkte" bezieht sich logischerweise auf das Gegenteil.</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierfeld</td>
			<td>-</td>
			<td>Hier kannst du einstellen, nach welchem Produktattribut beim ersten Seitenaufruf sortiert werden soll. Dein Shopbesucher kann durch das Filtermodul die Sortierung später selbstständig ändern.</td>
		</tr>
		<tr>
			<td>Anfängliches Sortierrichtung</td>
			<td>Abwärts</td>
			<td>Falls du ein Sortierfeld ausgewählt hast, kannst du hier bestimmen, ob aufwärts oder abwärts danach sortiert werden soll.</td>
		</tr>
	</tbody>
</table>

<docrobot_message type="warning">Sortieren nach `Preis` ist ein äusserst aufwändiger Vorgang. Isotope eCommerce kennt die Möglichkeit, den Preis aufgrund von Regeln anzupassen und es ist deshalb nicht möglich, die Produkte bereits auf der Datenbank vorzufiltern. Insofern muss sich Isotope eCommerce in einem solchen Fall zuerst **alle** Produkte aus der Datenbank laden und sie anschliessend auf PHP-Ebene sortieren!</docrobot_message>

## Weiterleitung

