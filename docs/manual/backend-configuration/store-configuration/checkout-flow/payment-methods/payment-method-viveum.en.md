---
menuTitle: VIVEUM
title: 'VIVEUM payment method'
description: 'The shop configuration - Order process - Payment methods - VIVEUM.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-viveum/
weight: 185
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}

## Configuration of the payment provider

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>PSPID</td> <td>-</td> <td></td> </tr><tr><td>HTTP Method</td> <td>POST</td> <td>VIVEUM supports the exchange of data using both POST and GET.</td> </tr><tr><td>Hash method</td> <td>SHA-256</td> <td>Hash method to encrypt the exchanged data. The choices are: - **SHA-1**
- **SHA-256**
- **SHA-512**
</td> </tr><tr><td>SHA-IN Signature</td> <td>-</td> <td>Here you have to enter an arbitrary hash which will be used to sign the exchanged data. Make sure that you use the same algorithm as you selected in "Hash Method". There are [many hash generators](http://hash.online-convert.com) that can generate a hash from any security key. Also, make sure you enter the hash as a lowercase hexadecimal string. The hash you enter here must also be entered in the PSP interface under "SHA-IN Signature". This allows both the PSP and Isotope eCommerce to verify the accuracy of the data.</td> </tr><tr><td>SHA-OUT Signature</td> <td>-</td> <td>Here you need to enter any hash which will be used to sign the exchanged data. Make sure you use the same algorithm as you selected in "Hash Method". There are [many hash generators](http://hash.online-convert.com) that can generate a hash from any security key. Also, make sure you enter the hash as a lowercase hexadecimal string. The hash you enter here must also be entered in the PSP interface at "SHA-OUT Signature". This allows both the PSP and Isotope eCommerce to verify the accuracy of the data.</td> </tr><tr><td>Dynamic Template URL</td> <td>-</td> <td></td></tr></tbody></table>

## Publishing

|     Setting      | Default Setting |                    Description                     |
|------------------|-----------------|----------------------------------------------------|
| Use test system  | -               |                                                    |
| Activate logging | -               | Write transaction information to system log files. |
