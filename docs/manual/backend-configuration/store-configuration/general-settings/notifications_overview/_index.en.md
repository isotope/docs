---
title: 'Notification Center'
description: 'The shop configuration - General settings - Notification center.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/notifications_overview/
weight: 30
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

![Navigation of the Notification Center](navigation.png)

Isotope eCommerce's own email notifications have been moved out to the `Benachrichtigungszentrum` {{< version-tag "2.0" >}} You'll notice that clicking `Benachrichtigungen` will take you to the appropriate menu item. This was built in to make it easier to get started for those familiar with Isotope 1.4.

If you imagine `Benachrichtigungszentrum` detached from Isotope eCommerce, some things should seem clearer from the start. It was developed independently and aims to act as a central component for any other extensions and their notifications. In fact, the requirements for notifications can be stated together:

- A notification always has a trigger, and since that trigger should potentially trigger several different messages, a notification consists of one or more messages.

{{% notice warning %}}Note the different usage of `Benachrichtigung` and a single `Nachricht`. A `Benachrichtigung` is a vessel of one or more `Nachrichten`.
{{% /notice %}}

- A message must be potentially translatable into different languages.
- A message is not defined by the word "email". It is therefore irrelevant for a message where or with which means (gateway) it is sent.
- A message does not necessarily consist of human-readable text. A machine-to-machine exchange can equally be called a "message".

The following behavior results:

A single [notification](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-benachrichtigungen/)includes one or more [messages](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-nachrichten/), which are sent in different [languages](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-sprachen/) via any [gateway](/de/backend-konfiguration-shop-allgemein-benachrichtigszentrum-gateways/).
