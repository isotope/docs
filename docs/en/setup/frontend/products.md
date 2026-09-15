# Displaying products

Products are catalog data. Product content elements turn that data into pages customers can browse.

The main elements are the **product list**, which displays several products, and the **product reader**, which displays one product in detail. In Contao, create them inside the appropriate page's article.

## Build a category page

1. Create and publish a regular page, such as T-shirts, in the Contao page structure.
2. Assign a published product to that page using its Categories selection.
3. Add a product-list content element to an article on the page.
4. Choose a category scope. For the simplest case, use the current category.
5. Choose the intended sorting and pagination.
6. Select the buttons and quantity behavior you want to show.
7. Open the page as a visitor.

If the list is empty, confirm the product's page assignment, publication dates, member protection, and list scope before changing templates.

## Understand list scope

“Current category” reads products assigned to this page. Scopes that include the first child level or all children also include those descendants. “All categories” covers products assigned within the active root's page tree, rather than every unrelated shop in the installation.

Choose scope deliberately on a shop landing page. A landing page with no direct assignments needs a child-inclusive scope if it should show its subcategories' products.

## Choose a reader arrangement

**On the current page:** Place both list and reader elements in the article. Enable the list's **Hide in reader mode** setting. The reader displays details when a product is selected. This is the simplest starting setup.

**On a separate page:** Create a page with the reader element and select it in each category page's reader configuration. This allows different layouts and surrounding content. The reader-page setting is **not inherited** by child categories, so configure every category that needs it.

**Disabled:** A category can suppress product detail pages. This is useful for simple buy-from-list experiences, but make sure the customer still receives enough information to choose correctly.

## Sorting, canonical links, and presentation

A product in multiple categories can have more than one browsing context. Decide which product URL should be primary and test the primary-link option if used. Maintain useful product aliases and metadata.

List/reader templates and galleries can be selected through product types and element overrides. Check both levels if a presentation change seems ineffective.

If your list does not display options, enable **Disable product options** to avoid generating unnecessary option and variant data. Do not use that optimization when the list needs interactive choices.

## Add filtering

Mark the relevant attributes as frontend filterable or searchable. Add the product-filter element, select the fields to offer, and connect it to the intended list using the configured filter association/key. Then test a choice that returns results and one that returns none.

The category-filter element serves page/category navigation. A product-attribute filter narrows products by values such as material or size. Use clear labels so customers understand the distinction.

## Acceptance check

From the category page, open a product, select options, add it to the cart, and verify the selected item there. Also test a product without an image, a protected product, and an unavailable URL.
