# Contao essentials for shop owners

Contao is the website system around your shop. You do not need to become a developer, but a few concepts explain where Isotope belongs.

## Pages, articles, and content elements

The **page structure** is the website's tree of pages. A website root identifies a site and its language settings. Regular pages hold content such as Home, Drinkware, Cart, and Checkout.

An **article** groups content on a page. A **content element** is a block inside an article, such as text, an image, or an Isotope product list. In Isotope 3, storefront features are content elements. Older guides that instruct you to create Isotope frontend modules describe an earlier architecture.

A **theme** and **page layout** control the site's presentation and regions. Creating products does not automatically add a product list to a page. Both catalog data and page content are needed.

## Why categories are pages

Isotope uses Contao pages as product categories. You might create Shop → Drinkware and Shop → Clothing. Assign mugs to Drinkware and T-shirts to Clothing. A product can belong to more than one page.

This lets categories use normal site navigation and page content. You can place an introductory paragraph above a product list without maintaining a second navigation system.

The product list's **category scope** decides which assigned products it reads. “Current category” only reads the current page. A scope that includes children also reads the chosen descendants. A published product assigned to a different page will not magically appear in the current category.

## Staff and customers

**Users** work in the backend. Give product editors, order processors, and administrators permissions appropriate to their tasks.

**Members** use the frontend. Isotope can use these accounts for checkout, saved addresses, and order history. Member groups can also be used for protected products or pricing conditions.

A registration form, login form, and password recovery experience belong to the broader Contao site setup. Selecting member checkout does not design those pages for you.

## Publication and access

Both Contao pages and Isotope products can be unpublished or protected. Check the entire chain when a product is missing: website root, page, article, element, product, and any relevant member permissions.

Preview is useful while editing. Final testing should also happen while logged out, using the public URL.

## Where to continue

- [Displaying products](../setup/frontend/products.md) connects categories to lists and readers.
- [Checkout](../setup/frontend/checkout.md) connects the cart and order pages.
- [Members and guests](../setup/frontend/customers.md) explains customer accounts.
- The [Contao manual](https://docs.contao.org/5.x/manual/en/) covers the CMS itself.
