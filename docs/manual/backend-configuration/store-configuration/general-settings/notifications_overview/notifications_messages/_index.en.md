---
title: Messages
description: 'The shop configuration - General settings - Notification center - Messages.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/notifications_overview/notifications_messages/
weight: 30
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

A `Nachricht` specifies a certain content that is sent via a certain [gateway](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-gateways/).

`Nachrichten` can, but does not necessarily have to be multilingual. If we make the mistake again and think of a message only as an e-mail, this always seems to be intentional. However, if we take into account a machine-to-machine message, it is unlikely to be written in multiple languages.

This is how you create a message to the orderer:

![Detail of a message to the orderer](message.png)

### Title &amp; Gateway

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Title</td> <td>-</td> <td>Here you can enter a title for your message. It is only used for the backend.</td> </tr><tr><td>Gateway</td> <td>-</td> <td>Each message is sent via a specific <docrobot_route name="notifications_gateways">gateway</docrobot_route>, which you can select here.</td></tr></tbody></table>

### Configuration for the gateway "E-Mail"

{{% notice info %}}
The [languages](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-sprachen/) are covered in the corresponding chapter
{{% /notice %}}

### Expert settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Priority</td> <td>normal</td> <td>Here you can set the priority with which the email is sent.</td> </tr><tr><td>Template file</td> <td>mail\_default</td> <td>Here you can select the template with which the email will be generated.</td></tr></tbody></table>

### Publish settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Publish message</td> <td>-</td> <td>Here you can determine whether or not this message should be included when sending a notification.</td></tr></tbody></table>
