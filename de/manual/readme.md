# Standards im Handbuch

## Generelles

Für die Dokumentation verwenden wir die Du-Form und die generelle Notation von [Markdown](http://daringfireball.net/projects/markdown/syntax). Die Dokumentation wird automatisch verarbeitet und auf [isotopeecommerce.org](isotopeecommerce.org) dargestellt. Nebst der generellen Markdown-Notation gibt es einige zusätzliche, Isotope eCommerce spezifische Schlüsselwörter, welche in diesem Dokument ebenfalls dokumentiert sind.

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

### "Neu in Version x.x"

Um zu dokumentieren, was in einer Version neu hinzugefügt wurde, kann folgende Notation verwendet werden:

```
[new_in_version::2.0] Dieses Feature ist neu in Isotope eCommerce 2.0
```

### Link zu einer anderen Seite in der Dokumentation

Die `config.json` bestimmt den Aufbau des Handbuches und verwendet Routen. Um zu einer gewissen Route zu verlinken, kann folgende Notation verwendet werden:

```
[route::routenname]Optionale Linkbezeichnung
```