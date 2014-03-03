# Simple Tokens

Simple Tokens ist womöglich eines der meistunterschätzten Features innerhalb von Contao und wird im Kern von Contao leider auch nur für das Newsletter-Modul verwendet.

Simple Tokens werden deshalb [in der offiziellen Dokumentation][1] auch nur kurz angerissen.

In Isotope eCommerce werden die Tokens oft verwendet, weil sie dir viel Flexibilität geben.
Sie werden unter anderem hier verwendet:

* Im gesamten <docrobot_route name="notifications">Benachrichtigungszentrum</docrobot_route>
* Für die Darstellung der Adressen der verschiedenen Länder (bspw. PLZ vor oder nach Ort etc.)
* In den <docrobot_route name="documents">Dokumenten</docrobot_route>, um den Dokumententitel sowie den Dokumenten-Dateinamen zu individualisieren

Simple Tokens unterstützen im Gegensatz zu Inserttags auch einfache If-Else-Abfragen wodurch z.B. in Bestellbestätigungs-E-Mails auch sowas möglich wäre:

```
{if billing_gender=="male"}
Sehr geehrter Herr ##billing_lastname##,
{elseif billing_gender=="female"}
Sehr geehrte Frau ##billing_lastname##,
{else}
Sehr geehrte Damen und Herren,
{endif}
```


[1]: https://contao.org/de/manual/3.2/managing-content.html#newsletter-personalisieren