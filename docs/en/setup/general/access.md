# Staff access and responsibilities

Staff work with Contao backend user accounts. Customers use frontend member accounts. Keep the two separate.

A small shop may have one administrator doing everything. As more people join, divide access by the work they perform.

## Suggested responsibilities

| Role | Typical work |
| --- | --- |
| Catalog editor | Products, images, descriptions, categories, and approved prices |
| Order processor | Review orders, reconcile payment information, prepare delivery, update statuses |
| Shop administrator | Product types, taxes, checkout methods, store configurations, and staff access |
| Developer/maintainer | Software updates, templates, integrations, hosting, and technical diagnostics |

These are suggested responsibilities, not automatically created role presets.

## Configure and test permissions

Use Contao users and user groups to grant the required backend modules and field/record permissions. Isotope includes permission controls for shop configuration records and product/order work.

Test with a real account in each group. An administrator's successful test does not prove another user can edit a price, view an order, or generate a document.

If someone cannot see a backend section, check module access. If they can see the section but cannot open a record or field, check the relevant record and field permissions as well.

## Protect shared configuration

Tax classes, product types, payment mappings, and workflow transitions affect the whole shop. Give routine editors access to the records they need without making every account an administrator.

Before changing a shared configuration, identify affected products and order processes, make the change on a test copy, and verify representative cases.

## Customer information

Orders contain addresses, contact information, and sometimes customer-defined text. Use test data in demonstrations and screenshots. Keep access to order exports, stored documents, and backups within the people and systems that need them.

For day-to-day procedures, continue with [Processing orders](../../usage/orders.md) and [Maintenance](../../guides/maintenance.md).
