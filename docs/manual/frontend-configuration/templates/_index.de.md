---
title: Templates
---

{{% notice warning %}}<p>Isotope eCommerce liefert seit Version 2.0 nur noch <code>.html5</code>-Templates mit. Einerseits reduziert das den Pflegeaufwand und andererseits gibt es kaum Gründe, weshalb man XHTML verwenden müsste. Selbstverständlich kannst du die Templates aber wie gewohnt überschreiben und auch als <code>.xhtml</code>-Variante anlegen.{{% /notice %}}

<table>
    <thead>
        <tr>
            <th>Modul</th>
            <th>Templates</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><docrobot_route name="product-list">Produktliste</docrobot_route></td>
            <td>mod_iso_productlist.html5<br>
            mod_iso_productlist_caching.html5<br>
            iso_list_default.html5</td>
            <td>Modul Template<br>
            Ausgabe beim Laden einer Liste (Ajax)<br>
            Standard Ausgabe der Liste</td>
        </tr>
        <tr>
            <td><docrobot_route name="product-variant-list">Produktvarianten-Liste</docrobot_route></td>
            <td>mod_iso_productlist.html5<br>
            iso_list_variants.html5</td>
            <td>Modul Template<br>
            Ausgabe der Liste mit Varianten</td>
        </tr>
        <tr>
            <td><docrobot_route name="product-reader">Produktleser</docrobot_route></td>
            <td>mod_iso_productreader.html5<br>
            iso_reader_default.html5</td>
            <td>Modul Template<br>Ausgabe der Leser-Seite</td>
        </tr>
        <tr>
            <td><docrobot_route name="shopping-cart">Warenkorb</docrobot_route></td>
           	<td>mod_iso_cart.html5<br>
           	iso_collection_default.html5<br>
           	iso_collection_mini.html5</td>
            <td>Modul Template<br>
            Standard Ausgabe der Liste<br>
            Minimierte Ausgabe der Liste</td>
        </tr>
        <tr>
            <td><docrobot_route name="checkout">Kasse</docrobot_route></td>
            <td>mod_iso_checkout.html5<br>
            iso_collection_default.html5<br>
            iso_checkout_address.html5<br>
            iso_checkout_shipping_method.html5<br>
            iso_checkout_payment_method.html5<br>
            iso_checkout_order_info.html5<br>
            iso_checkout_order_conditions.html5</td>
            <td>Modul Template<br>
            Standard Ausgabe der Liste<br>
            Schritt 1 in der Kasse<br>
            Schritt 2 in der Kasse<br>
            Schritt 3 in der Kasse<br>
            Schritt 4 in der Kasse<br>
            Anpassen des Formulars</td>
        </tr>
        <tr>
            <td><docrobot_route name="product-filter">Produkt-Filter</docrobot_route></td>
            <td>iso_filter_default.html5</td>
            <td>Filter Ausgabe</td>
        </tr>
        <tr>
            <td><docrobot_route name="cumulative-filter">Einschränkender Filter</docrobot_route></td>
            <td>mod_iso_cumulativefilter.html5<br>
            nav_default.html5 <em>Contao</em></td>
            <td>Modul Template<br>
            Standard Navigations-Template</td>
        </tr>
        <tr>
            <td><docrobot_route name="order-history">Vergangene Bestellungen</docrobot_route></td>
            <td>mod_iso_orderhistory.html5</td>
            <td>Modul Template</td>
        </tr>
        <tr>
            <td><docrobot_route name="order-details">Bestellungsdetails</docrobot_route></td>
            <td>mod_iso_orderdetails.html5<br>
            iso_collection_default.html5<br>
            <td>Modul Template<br>
            Standard Ausgabe der Liste</td>
        </tr>
        <tr>
            <td><docrobot_route name="store-config-switcher">Shopkonfigurations-Wechsler</docrobot_route></td>
            <td>mod_iso_configswitcher.html5</td>
            <td>Modul Template</td>
        </tr>
        <tr>
            <td><docrobot_route name="address-book">Adressbuch</docrobot_route></td>
            <td>mod_iso_addressbook.html5<br>
            member_default.html5 <em>Contao</em><br>
            member_grouped.html5 <em>Contao</em></td>
            <td>Modul Template<br>
            Standard Mitglieder-Liste<br>
            Gruppierte Mitglieder-Liste (z.B. Personendaten, Adressdaten etc.)</td>
        </tr>
        <tr>
            <td><docrobot_route name="related-products">Ähnliche Produkte</docrobot_route></td>
            <td>mod_iso_productlist.html5<br>
            iso_list_default.html5</td>
            <td>Modul Template<br>
            Standard Ausgabe der Liste</td>
        </tr>
        <tr>
            <td><docrobot_route name="messages">Nachrichten</docrobot_route></td>
            <td>mod_iso_messages.html5</td>
            <td>Modul Template</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>Sonstige</th>
            <th>Templates</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Galerien</td>
            <td>iso_gallery_standard.html5<br>
            iso_gallery_inline.html5</td>
            <td>Ausgabe einer Standard Galerie<br>
            Ausgabe einer Inline Galerie</td>
        </tr>
        <tr>
            <td>Dokumente</td>
            <td>iso_document_default.html5</td>
            <td>Ausgabe eines Dokumentes</td>
        </tr>
    </tbody>
</table>
