# Quellcodeübersicht und Dokumentationspflege

Das Handbuch basiert auf der Core-Revision `96240eaa65c33a51e37951fe9833d9db1bd5980d`. Die folgenden Links zeigen Implementierungsbereiche, die bei Verhaltensänderungen erneut zu prüfen sind.

| Thema | Hauptquelle |
| --- | --- |
| Anforderungen | [composer.json](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/composer.json) |
| Updateänderungen | [UPGRADE.md](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/UPGRADE.md) |
| Bundle-Einstellungen und registrierte Typen | [IsotopeBundle](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php) |
| Backendfelder | [DCA-Definitionen](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca) |
| Bezeichnungen und Hilfe | [Englische Sprachdateien](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en) |
| Produktkonstruktion und Preise | [Product](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Product) |
| Preisberechnung | [Store/Price](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price) |
| Steuern | [TaxCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Tax/TaxCalculator.php) |
| Regelauswertung | [RuleBuilder](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder) |
| Shopoberfläche | [Inhaltselement-Controller](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement) |
| Zahlung und Versand | [Checkout](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout) |
| Statusworkflows | [WorkflowManager](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Order/WorkflowManager.php) |
| Bestellnachrichten | [DefaultOrderNotificationTokensListener](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/EventListener/DefaultOrderNotificationTokensListener.php) |
| Dokumente | [DocumentManager](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/DocumentManager.php) |
| Templates | [Twig-Templates](https://github.com/isotope/core3/tree/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/templates) |
| Core-Prüfungen | [CI-Workflow](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/.github/workflows/ci.yml) |

## Ein Kapitel aktualisieren

1. Prüfe das Verhalten der Zielversion einschließlich Felddefinitionen und Auslösepfaden.
2. Erkläre das Konzept vor den Konfigurationsschritten.
3. Nenne Voraussetzungen, gewünschtes Ergebnis und eine Prüfmöglichkeit.
4. Aktualisiere betroffene Anleitungen und Fehlerbehebungseinträge gemeinsam.
5. Führe die in der Repository-README beschriebenen Dokumentationsprüfungen und den strikten Build aus.
6. Aktualisiere die Basisrevision erst nach Prüfung des betroffenen Handbuchumfangs.

Mache erweiterungsspezifische Funktionen nicht stillschweigend zu Core-Zusagen. Halte Widersprüche zwischen Quellcode und Hilfetexten bis zur Behebung in [Versionshinweise](version-notes.md) fest.

## Weitere Kapitelreferenzen

- [PurgeCartsCron](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Cron/PurgeCartsCron.php)
- [Registrierte Benachrichtigungstokens](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/NotificationCenter/OrderNotificationType.php)
- [Beschreibungen der Bestelltokens](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en/nc_tokens.xlf)
- [CashPayment](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CashPayment.php)
- [CorePaymentFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Payment/CorePaymentFactory.php)
- [FlatShipping](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Checkout/Shipping/FlatShipping.php)
- [Versandfelder](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_shipping.php)
- [Steuersatzfelder](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_tax_rate.php)
- [CheckoutController](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/CheckoutController.php)
- [OrderDetailsController](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Controller/ContentElement/OrderDetailsController.php)
- [Seitenhilfe](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/languages/en/tl_page.xlf)
- [StandardDocument](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Document/StandardDocument.php)
- [OrderNotifier](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Order/OrderNotifier.php)
- [Standardstatusmigration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Migration/OrderstatusMigration.php)
- [Shopkonfigurationsfelder](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_config.php)
- [Attributkonfiguration](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_attribute.php)
- [Grundpreisformatierung](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceFormatter.php)
- [Produkttypmodell](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Model/ProductTypeModel.php)
- [RuleMatcher](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/RuleBuilder/RuleMatcher.php)
- [DefaultPriceFactory](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Product/DefaultPriceFactory.php)
- [PriceCalculator](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Store/Price/PriceCalculator.php)
- [Produktfelder](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/contao/dca/tl_iso_product.php)
