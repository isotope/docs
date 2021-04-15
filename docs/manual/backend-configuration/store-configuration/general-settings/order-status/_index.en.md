---
title: 'Order status'
description: 'The shop configuration - General settings - Order status.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/order-status/
weight: 40
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

When Isotope eCommerce is installed, the following `Bestellstatus` is also created:

- Pending
- Processing
- Complete
- On Hold
- Cancelled

## Name

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Name</td> <td>-</td> <td>Here you can enter a name for the order status, this will be displayed in the backend <docrobot_route name="orders">(orders</docrobot_route>) and frontend <docrobot_route name="order-history">(past orders</docrobot_route> and <docrobot_route name="order-details">order details</docrobot_route>).</td> </tr><tr><td>Color</td> <td>-</td> <td>Here you can set a color for the order status to increase the clarity in the backend.</td> </tr><tr><td>The order has been paid</td> <td>-</td> <td>If this field is selected, the order will be marked as paid when reaching this status. This allows you to download a download product, for example.</td> </tr><tr><td>Show on welcome page</td> <td>-</td> <td>Displays the number of orders when reaching this status on the backend welcome page of Contao.</td></tr></tbody></table>

### Color

![Order status with colors under orders](bestellstatus.png)

### Show on welcome page

![Display on the home page](willkommensseite.png)

## Notification

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Notification</td> <td>-</td> <td>Here you can select a notification created in the <docrobot_route name="notifications_overview">notification center</docrobot_route>.</td></tr></tbody></table>
