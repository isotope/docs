---
title: 'Integrity Check'
description: 'The shop configuration - Miscellaneous - Integrity check.'
aliases:
    - /en/backend-configuration/store-configuration/miscellaneous/integrity-check/
weight: 105
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{< version "2.2" >}}

![Screenshot of the integrity check](integritaetscheck.png)

The integrity check tries to detect inconsistencies in the database and, if possible, also offers the option to fix the problem automatically. An example would be the configuration of a product type with variants, which is later changed back to "variantless". This results in superfluous variants in the database, which the integrity check detects and cleans up with a click.
