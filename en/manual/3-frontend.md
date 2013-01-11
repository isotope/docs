# Frontend Setup

Much like other Contao extensions, Isotope has several modules that are used on the frontend for things like products, shopping cart, checkout, etc. As with other setups we use lister and detail/reader modules for the display of products, and the process of adding the cart and checkout modules is similar.

Your site structure should contain at least some of the following pages:
- Products
    - Category 1
    - Category 2
    - etc...
- Product Details/Reader (hidden from navigation)
- Cart
- Checkout
    - Order Completed (hidden from navigation)


## Product Listing Module

The Product List module shows all of the current page (and / or depending on the configuration, its sub-) assigned products. The most important setting in this module is the “Product reader jump to page” where you will select your Product Details page from the site structure. It is best to place this module in a page layout because it will likely be included in all store listing pages. Alternatively, you can always use it in an article/content element.


## Product Details Module

This module is required to display the details of a product. Place this module on the "Product Details" page.


## Shopping Cart Module

The shopping cart module serves two purposes. By selecting the cart-mini template you can create a tiny cart for products on the side column on every page. You will need the cart-full template for the primary "Shopping Cart" page in your site structure. Again, you should define the redirect pages according to your page structure.


## Checkout Module

The Checkout Module is used for the entire ordering process. Here you choose which payment and shipping modules are available to the customer, whether a member must be registered and which e-mail template should be sent on a completed order. Place this module on the appropriate "Checkout" page.


## Other Modules

The four frontend modules described above are sufficient in principle for creating a basic Isotope eCommerce shop. Of course, depending on customer requirements there may be a need for more modules. For example, managing a registered member’s addresses with the "Address Book" module, or referencing a customer’s "Order History" with their previous orders.