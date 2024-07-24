---
menuTitle: 'PayPal Standard Checkout'
title: 'Payment method PayPal Standard Checkout'
description: 'The shop configuration - order process - payment methods - PayPal Standard Checkout.'
aliases:
    - /en/backend-configuration/store-configuration/checkout-flow/payment-methods/payment-method-PayPal-Standard-Checkout/
weight: 107
---

{{% notice info %}}<p>This lacks a general description.</p>{{% /notice %}}

 {{< version "2.9" >}}


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
        <td>Client ID</td>
        <td>-</td>
        <td>These are live API credentials from your PayPal PLUS account. You can find them in your PayPal Developer account: Dashboard &gt; My Apps &amp; Credentials. [How do I create the Client ID and Secret?](https://www.paypalobjects.com/webstatic/de_DE/downloads/Dokumentation_REST_API_Zugangsdaten.pdf)</td>
    </tr>
    </tbody>
</table>


## Publishing

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
			<td>Use test system </td>
			<td>-</td>
			<td>Check this box if you want to work in test mode. Requests will then automatically go to the test system and not the production system.</td>
		</tr>
		<tr>
			<td>Enable logging</td>
			<td>-</td>
			<td>Write transaction information to the system log files.</td>
		</tr>
	</tbody>
</table>
