---
title: 'Past orders'
description: 'The frontend configuration - Modules - Past orders'
aliases:
    - /en/frontend-configuration/modules/order-history/
weight: 150
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The module `Vergangene Bestellungen` displays past orders of shop visitors.

{{% notice warning %}}
Of course this module only works if a member is logged in, because only a logged in member can be assigned orders.
{{% /notice %}}

## Module configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Configurations</td> <td>-</td> <td>Since you can have any number of shop configurations and the module `Vergangene Bestellungen` does not necessarily have to refer only to the currently active shop configuration (personal areas are usually centralized), you can check here the shop configurations that should be considered for the search of past orders.</td></tr></tbody></table>

## Forwarding

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Forwarding page</td> <td>-</td> <td>Select the page where the <docrobot_route name="order-details">Order Details</docrobot_route> module is located.</td> </tr><tr><td>Forwarding page for shopping cart</td> <td>-</td> <td>Select here the page to which the visitor will be redirected if he wants to see the complete shopping cart.</td></tr></tbody></table>

## Template settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Individual template</td> <td>-</td> <td>Here you can override the default template.</td> </tr><tr><td>Include messages</td> <td>-</td> <td>If this option is activated, the errors and hints will be displayed directly in the module and not as a JavaScript overlay.</td></tr></tbody></table>
