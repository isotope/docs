# Standards im Handbuch

## Generelles

Für die Dokumentation verwenden wir die du-Form und die generelle Notation von [Markdown](http://daringfireball.net/projects/markdown/syntax). Die Dokumentation wird automatisch verarbeitet und auf [isotopeecommerce.org](isotopeecommerce.org) dargestellt. Nebst der generellen Markdown-Notation gibt es einige zusätzliche, Isotope eCommerce spezifische Schlüsselwörter, welche in diesem Dokument ebenfalls dokumentiert sind.

## Häufig verwendete Wörter

In Contao und Isotope eCommerce kommen einige Wörter sehr häufig vor. Um eine gewisse einheitliche Verwendung zu garantieren, werden diese anschliessend festgehalten:

<table>
<thead>
<tr>
<th>Korrekte Schreibweise</th>
<th>Falsche Schreibweisen</th>
</tr>
</thead>
<tbody>
<tr>
<td>Isotope eCommerce</td>
<td>e-Commerce, Ecommerce, ECommerce</td>
</tr>
<tr>
<td>Frontend</td>
<td>Front end, Front-End</td>
</tr>
<tr>
<td>Backend</td>
<td>Back end, Back-End</td>
</tr>
</tbody>
</table>

## Spezielle Markdown-Anweisungen

### Aktuelle Version

Für die Ausgabe der aktuellen Version kannst du folgende Notation verwenden:

```
<docrobot_current_version>
```

### Root der Dokumentation

Um das Referenzieren von Bildern zu vereinfachen und keine relativen Pfade verwenden zu müssen, kannst du jeweils immer vom Repository-Root ausgehen und folgende Notation verwenden:

```
<docrobot_root>
```

### Sitemap der Dokumentation

Gibt eine komplette Sitemap der Dokumentation aus:

```
<docrobot_sitemap>
```

### Bilder

Möchtest du ein Bild nutzen, so verwende die folgende Notation:

```
<docrobot_image path="~" alt="~">
```

Dem Pfad wird immer automatisch der Root der Dokumentation vorangestellt. Die Attribute `width` sowie `height` werden automatisch hinzugefügt.

Beispiel:

```
<docrobot_image path="images/isotope.png" alt="Isotope Logo">
```


### Hinweise

Möchtest du den Leser darauf hinweisen, eine gewisse Vorsicht walten zu lassen, so kannst du folgende Notation verwenden:


```
<docrobot_message type="~"><p>Dies ist eine Warnung, sei vorsichtig!</p></docrobot_message>
```

Folgende Typen (type="~") stehen zur Verfügung:

* warning (gelb)
* info (blau)
* success (grün)


### "Neu in Version x.x"

Um zu dokumentieren, was in einer Version neu hinzugefügt wurde, kann folgende Notation verwendet werden:


```
<docrobot_new_in_version version="~"><p>Dieses Feature ist neu in Isotope eCommerce 2.0</p></docrobot_new_in_version>
```

`version="~"` muss dabei die Version enthalten (bspw. `2.0`).

### Link zu einer anderen Seite in der Dokumentation

Die `config.json` bestimmt den Aufbau des Handbuches und verwendet Routen. Um zu einer gewissen Route zu verlinken, kann folgende Notation verwendet werden:

#### Link

```
<docrobot_route name="~">Linkbezeichnung</docrobot_route>
```

`name="~"` muss dabei den Routen-Namen beinhalten.

#### Link mit Anker

```
<docrobot_route name="~">Linkbezeichnung</docrobot_route>
```

`name="~"` muss dabei den Routen-Namen und `path="~"` den Ankerpukt beinhalten.  


Beispiel:

```
<docrobot_route name="products" path="#anker">Anker</docrobot_route>
```
