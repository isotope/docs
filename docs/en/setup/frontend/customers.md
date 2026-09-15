# Members and guests

A guest buys without a signed-in account. A member uses a Contao frontend account. Choose the approach that fits your customer relationship.

Guest checkout reduces account setup work for occasional buyers. Member accounts are useful for repeat customers, saved addresses, protected catalogs, and customer-specific conditions.

## Choose a checkout method

The checkout element offers guest-only, member-required, or both. This setting governs the checkout experience. It does not automatically create a complete registration and account area.

For member checkout, prepare Contao login, registration if offered, password recovery, and personal-data pages. Configure a sensible destination after login.

Test a signed-in member’s full checkout before enabling member-required mode. If a signed-in customer keeps returning to login, ask your maintainer to check the [member-checkout version note](../../developers/version-notes.md).

## Address book

Place the address-book element in the member area. Verify that customers can manage the addresses your checkout needs and that one member cannot see another's information.

The store configuration decides which billing and shipping fields exist, which are required, and which countries are allowed. Account forms and checkout should present consistent choices.

## Order history and details

Use the order-history element in an appropriate member area, select the store configurations whose orders it should show, and connect its detail destination. Without selected configurations, the element displays nothing. Use the order-details element to display an individual order.

The details element has a login requirement option for member orders. A different signed-in member is denied access. For an unauthenticated visitor, access to a member order also depends on the login requirement setting. Enable and test the intended protection.

Guest orders rely on their individual order links rather than member ownership. Treat those links as private customer information and keep order details out of public indexes and shared caches.

## Member groups

Groups can control product visibility and rule-based prices or methods. A product protected for a group should be tested while logged out, as a member outside the group, and as a member inside it.

A group name such as “Trade customers” does not automatically establish a discount. Attach a member-group rule to an advanced price entry and check the resulting price.

## Staff accounts

Backend users are separate from members. Product editors and order processors need backend permissions. Do not give customers backend accounts to provide order history.

See [Staff access](../general/access.md) and [International shops](../general/international.md) for related setup.
