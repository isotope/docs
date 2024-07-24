---
title: 'Evaluations & Statistics'
description: 'Evaluations & Statistics.'
aliases:
    - /en/backend-configuration/reports-and-statistics/
weight: 30
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Sales overview

{{< version "2.9" >}}

Here Isotope eCommerce displays a list of products ordered: 

* in the last 24 hours
* this month
* this year 

The total of sales, as well as the average order values (AVO) are output as net value and without discounts.
The discounts given for the above periods are listed separately.

Only orders with the flag `The order has been paid` in the order status are taken into account.

## Sales statistics

### Total

Here you get an overview of all sold products.

You can influence the output by the following filters:

- Time period
- From one date to the other
- [Order status](/de/backend-konfiguration-shop-allgemein-bestellstatus/) (all statuses you have created)
- [Shop configuration](/de/backend-konfiguration-shop-allgemein-konfiguration/) (if you have created more than one)

### Per product

Here you get an overview of the sales figures per product.

You can influence the output with the following filters:

- Variants (if you have created products with variants)
- Time period
- Columns (number of columns for the time period)
- From this date
- [Order status](/de/backend-konfiguration-shop-allgemein-bestellstatus/) (all statuses you created)
- Sort by product name (alphabetical) or sales total (sum)
