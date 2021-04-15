---
title: 'Address book'
description: 'The Frontend Configuration - Modules - Address Book'
aliases:
    - /en/frontend-configuration/modules/address-book/
weight: 180
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The `Adressbuch` module is used to manage members' addresses. This allows you to simplify the ordering process for your returning visitors, as they can select a delivery or billing address from their address book.

If you want the given addresses to be stored in the address book every time a member places an order, this must be set in the [checkout module](/de/frontend-konfiguration-module-Kasse/).

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Notification</td> <td>-</td> <td>Here you can choose which <docrobot_route name="notifications_overview">notification</docrobot_route> should be sent when submitting the order.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Form-Template</td> <td>member\_default</td> <td>Here you can select a form template. Note: This setting only applies to the edit mode. Options: - member\_default
- member\_grouped&lt;/li
 
</td> </tr><tr><td>Tableless layout</td> <td>-</td> <td>Determines if the form should be displayed without HTML tables in edit mode.</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is activated, the errors and hints are output directly in the module and not as a JavaScript overlay.</td></tr></tbody></table>
