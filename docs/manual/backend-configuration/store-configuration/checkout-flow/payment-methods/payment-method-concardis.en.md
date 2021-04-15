---
menuTitle: Concardis
title: 'Payment method Concardis'
description: 'The shop configuration - order process - payment methods - Concardis.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-concardis/
weight: 135
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{% notice info %}}
This lacks a general description.
{{% /notice %}}

 {{< version "2.5" >}}

## Configuration of the payment provider

<table>
    <thead>
    <tr>
        <th>Setting</th>
        <th>Default setting</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>PSPID</td>
        <td>-</td>
        <td>Here you have to enter your PSPID. You will receive the PSPID from PostFinance. If you are in test mode, please make sure that the PSPID ends with "DEMO".</td>
    </tr>
    <tr>
        <td>HTTP Method</td>
        <td>POST</td>
        <td>Concardis supports the exchange of data via POST as well as GET.</td>
    </tr>
    <tr>
        <td>Hash Method</td>
        <td>SHA-1</td>
        <td>Hash method to encrypt the exchanged data. Choices are:
        <ul>
        <li>**SHA-1**</li>
        <li>**SHA-256**</li>
        <li>**SHA-512**</li>
        </ul>
        </td>
    </tr>
    <tr>
        <td>SHA-IN Signature</td>
        <td>-</td>
        <td>Here you have to enter an arbitrary hash which will be used to sign the exchanged data. Make sure that you use the same algorithm as you selected in "Hash Method". There are [many hash generators](http://hash.online-convert.com) that can generate a hash from any security key. Also, make sure you enter the hash as a lowercase hexadecimal string. The hash you enter here must also be entered in the PSP interface under "SHA-IN Signature". This allows both the PSP and Isotope eCommerce to verify the accuracy of the data.</td>
    </tr>
    <tr>
        <td>SHA-OUT Signature</td>
        <td>-</td>
        <td>Here you need to enter any hash which will be used to sign the exchanged data. Make sure you use the same algorithm as you selected in "Hash Method". There are [many hash generators](http://hash.online-convert.com) that can generate a hash from any security key. Also, make sure you enter the hash as a lowercase hexadecimal string. The hash you enter here must also be entered in the PSP interface at "SHA-OUT Signature". This allows both the PSP and Isotope eCommerce to verify the accuracy of the data.</td>
    </tr>
    <tr>
        <td>Dynamic Template URL</td>
        <td>-</td>
        <td></td>
    </tr>
    </tbody>
</table>

## Publishing

|     Setting     | Default Setting |                                                              Description                                                               |
|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Use test system | -               | Check this box if you want to work in test mode. Requests will then automatically go to the test system and not the production system. |
| Enable logging  | -               | Write transaction information to the system log files.                                                                                 |
