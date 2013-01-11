# Product Management

After you’ve done the basic setup of the pages and modules, you can focus on the products. Depending on the product type you choose, different attribute fields will be offered for editing.

Each product can be assigned to several categories, and categories correspond to the site structure. For example you can define that a product is displayed both on the "T-shirts" and on the Home Page. The attributes that are displayed in the front end will depend on which list and detail template you are using. Only the default attributes are displayed automatically.


## Product Photos

Isotope eCommerce has its own image management system, which does not correspond to the Contao standard. Product images are not uploaded through the file manager, but directly within the product itself. The main reason for this special method is that if you had 1000 products with 5 images each, there would be over 5000 pictures in the file management. This would make standard file management almost useless.

Files are stored in the root directory /isotope/. If you upload a file, it is copied into the appropriate directory. If you upload the same image for multiple products, it will be stored only once, provided they have each used the same filename. Different files with the same file names are automatically detected and uniquely named.

![](https://raw.github.com/isotope/docs/1.4/en/manual/images/4-products_01.png)

To upload a new picture, select the file and save the product. After successfully uploading, a preview of the image is displayed directly in the product, and next to it you can enter its alternative text and a description. For more pictures, you can click on the arrows to the right and change their order, and the top image is used as the main image of each product.


### Importing assets

In the main product management area, you will see a Tools menu, where you can select "Import assets". Using this function, you can store images which are already on the system (for example, have been uploaded via FTP) and assign them to the corresponding products. The file name must either begin with the SKU/Item Number of the product, or else be located in an appropriately named subfolder.

Note that this feature is still in the testing phase and has not been sufficiently tested. It will not delete any data, but you may find that not all images are properly assigned.


## Languages

Unfortunately, the standard method for using multiple languages in Contao - creating multiple versions of content/products - is not possible in the case of products. Products could have a stock number which is identical across all languages, and would require a lot of duplicate content. For this reason we have developed a different solution. If you have activated multiple languages in your product type you will now see the following options:

![](https://raw.github.com/isotope/docs/1.4/en/manual/images/4-products_02.png)

When you edit a product the selection of language is offered in the upper left corner. Choose a specific language, Contao shows only those attributes which can be translated. The front end output automatically detects this and loads the translations of the corresponding fields in the display of a product.


## Creating Variants

Product variants are available for appropriate product types and are added by selecting "Add Variant". With this method you can create variant products for suitable products.


### Variant Generator

To simplify create the many variations, you can use the variant generator. Click on the magic wand icon and in the submenu that appears on the appropriate option. In the next screen, you can choose which option combinations are to be generated. Naturally, already existing combinations are not produced again.


### Quick Edit

Immediately after generating the variants appear in the Quick Edit mode. You can also access this via the magic wand icon. The Quick-Edit mode allows basic editing options, and in each case you can configure the SKU, price and the publishing status.


### Inherited Attributes

Variants may contain attributes other than those that are available in the Quick Edit mode, such as a variant product description. Since some fields are empty (and perhaps mandatory) upon generation of these variant products, there is the option "Use default value". If this hook is active, the value is automatically inherited from the parent element. The Quick Edit attributes (SKU, published and price,) cannot be inherited!


## Other Features


### Related Products

You can a list of products which relate to the current product for visitors to view on the frontend. Related products need to be categorized. You will first need to set up a related product category in the shop configuration, and then the related products option will be available from the magic wand menu when editng a product. Each category can only be used once per product.

To ensure clarity when a large number of products are loaded, we do not list all of the products, instead, you can search for products. In the search you can use any of the known standard fields such as item number, name and description. Then in the search results use the checkbox to add the product to list of related products.

You can then create and add the appropriate Related products module to the product detail page.


### Downloads

Isotope eCommerce offers you the ability to offer paid downloads to your customers. You can add downloads on a per-product basis if the corresponding option is set in the product type. At present it is not possible to offer different downloads for product variants.

Downloadable items are available to the user after a successful order through the order history / order details modules are available on the frontend. Downloads can only be downloaded if the order status is "complete" or a "paid" date is available.

**Make absolutely sure that you protect your download file in the file manager!** Otherwise, users can go straight to the URL of the file and download without paying. Contao provides the ability to protect entire directories (lock icon) in the File Manager. Checking this is essential but you should also check whether it functions correctly.