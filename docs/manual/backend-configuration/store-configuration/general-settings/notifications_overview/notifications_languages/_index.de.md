---
title: Sprachen
---

`Sprachen` sind, wie in vorderen Kapiteln bereits erwähnt, nicht zwingend in jedem Gateway oder Benachrichtigungstyp vorhanden.
Für menschliche Empfänger von Nachrichten sind sie jedoch logischerweise von grosser Bedeutung und das `Benachrichtigungszentrum` erlaubt dir einige Einstellungen.

{{% notice info %}}In diesem Kapitel wird immer wieder auf <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> Bezug genommen. Im Benachrichtigungszentrum wurde eine Autocomplete-Funktion eingefügt, die die Verwendung eben dieser vereinfachen soll. Durch Tippen von "##" erhältst du eine Auswahl der zur Verfügung stehenden <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> sowie eine Beschreibung dazu.{{% /notice %}}

{{% notice warning %}}Die nachfolgenden Einstellungen beziehen sich auf das Gateway "E-Mail". Andere Gateways besitzen selbstverständlich womöglich andere Einstellungen (bspw. mit grosser Wahrscheinlichkeit weder "CC-Adressfelder" noch "BCC-Adressfelder").{{% /notice %}}


![Generelle Einstellungen einer Sprache](general.png)

### Generelle Spracheinstellungen

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
			<td>Sprache</td>
			<td>-</td>
			<td>Hier wählst du eine Sprache aus, für die du die Nachricht gerne verfassen möchtest. Isotope eCommerce ist mehrsprachig, du kannst deshalb mehrere Sprachen oder aber auch nur eine definieren.</td>
		</tr>
		<tr>
			<td>Fallback-Sprache</td>
			<td>-</td>
			<td>Wie bei den Wurzelseiten von Contao selbst auch, kannst du hier definieren, ob die definierte Sprache als Fallback fungieren soll. Isotope wird versuchen, die Nachricht in der gerade aktuellen Sprache zu versenden. Sollte es sie nicht geben, wird die Fallback-Sprache verwendet.</td>
		</tr>
	</tbody>
</table>

### Meta-Informationen

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
			<td>Absendername</td>
			<td>-</td>
			<td>Hier kannst du einen Absendernamen erfassen. Denkbar wäre zum Beispiel der Name deines Webshops.</td>
		</tr>
		<tr>
			<td>Absender-Email</td>
			<td>-</td>
			<td>Hier kannst du die Absender-E-Mail-Adresse erfassen.</td>
		</tr>
		<tr>
			<td>Empfänger</td>
			<td>-</td>
			<td>Hier kannst entweder eine E-Mail-Adresse eingeben oder <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> verwenden. Mehrfachangaben sind komma-separiert erlaubt.</td>
		</tr>
		<tr>
			<td>CC-Empfänger</td>
			<td>-</td>
			<td>Hier kannst du eine CC-E-Mail-Adresse eingeben. Mehrfachangaben sind komma-separiert erlaubt.</td>
		</tr>
		<tr>
			<td>BCC-Empfänger</td>
			<td>-</td>
			<td>Hier kannst du eine BCC-E-Mail-Adresse eingeben. Mehrfachangaben sind komma-separiert erlaubt.</td>
		</tr>
	</tbody>
</table>

![Inhalts-Einstellungen einer Sprache](content.png)

### Inhalt

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
			<td>Betreff</td>
			<td>-</td>
			<td>Hier kannst du den Betreff für deine E-Mail eingeben. Es stehen dir einige <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> per Autocomplete-Funktion zur Verfügung.</td>
		</tr>
		<tr>
			<td>Modus</td>
			<td>Nur Text</td>
			<td>Hier kannst du auswählen, ob du die E-Mail nur als Text-Version oder auch als HTML-Version versenden möchtest. {{% notice warning %}}Beachte, dass einige Tokens HTML beinhalten und andere nicht wie bspw. <code>cart_text</code> und <code>cart_html</code>.</td>
		</tr>
		<tr>
			<td>Rohtext bzw. HTML</td>
			<td>-</td>
			<td>Hier kannst du den Inhalt für deine E-Mail eingeben. Es stehen dir einige <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> per Autocomplete-Funktion zur Verfügung.</td>
		</tr>
	</tbody>
</table>

![Einstellungen zu den Anhängen einer Sprache](attachments.png)

### Anhänge

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
			<td>Anhänge vom Dateisystem</td>
			<td>-</td>
			<td>Hier kannst du optional statische Dateien anhängen. Denkbar wären etwa AGB.</td>
		</tr>
		<tr>
			<td>Anhänge via Simple Token</td>
			<td>-</td>
			<td>Hier kannst du eine komma-separierte Liste von <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> eingeben. Diese <docrobot_route name="simple-tokens">Simple Tokens</docrobot_route> werden von Isotope dynamisch zur Verfügung gestellt. <docrobot_message info="warning">Das Token <code>##document##</code> bezieht sich auf die Dokument-Einstellung welche im Kapitel <docrobot_route name="notifications">Benachrichtigungen</docrobot_route> vorgestellt wurde.</td>
		</tr>
	</tbody>
</table>
