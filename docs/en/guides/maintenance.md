# Keeping the shop running

Maintenance keeps the software, data, and business workflow recoverable. Assign an owner and a schedule before launch.

## Back up the complete shop

Include the database, uploaded product files, generated document storage, site configuration, custom templates/code, and the dependency lock file. Protect credentials through your hosting's secret-management process.

A backup is useful only when it can be restored. Rehearse restoration to a separate environment and verify a product image, historical order, generated document, and customer access behavior.

Do not restore only an old database over a busy live shop without a plan for orders and payments received since that backup.

## Update on a copy first

Record the installed versions and read the relevant upgrade notes. Resolve compatible versions for Isotope, Contao, and extensions together. Run package installation and database migrations on a copy, then execute the checkout acceptance tests.

For production, use a deployment procedure that preserves orders arriving around the change. Keep the tested dependency lock file and a rollback/recovery plan.

See [Upgrading](upgrading.md) for Isotope 3-specific changes.

## Check operational signals

Review failed notifications, unresolved payments, application errors, and reports from customers. Agree how long a payment may remain processing before staff investigate it.

Keep contact details and checkout instructions current. Test a small representative order periodically and after changing providers, mail transport, taxes, or shipping tariffs.

## Scheduled cart cleanup

Isotope's daily cleanup removes guest carts older than the configured timeout and carts whose member no longer exists. The default guest timeout is 30 days.

This is cart cleanup, not an order-retention policy. It does not mean orders or generated documents are deleted after 30 days. Decide historical-data handling separately through the appropriate business process.

## Changes to catalog structure

Deleting an attribute or changing a product type can affect existing data and templates. Keep a backup, inspect schema changes, and test existing products. Do not approve column deletions simply because they appear in a migration proposal.

## Keep an operations note

Record where backups live, who owns the payment account, how to inspect failed mail, which integrations run, how stock is managed if applicable, and who can restore service.

This note should contain procedures and contacts, with credentials kept in the approved secure location.

Implementation: [PurgeCartsCron](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/Cron/PurgeCartsCron.php).
