# Backend Configuration

Setup of Isotope eCommerce can be boiled down to a few steps:
- Basic configuration of the shop and the product types
- Setting up the ordering processes, (taxes, payment and shipping options)
- Setting up the site structure and the frontend modules
- Adding the products

After installing the system, you should now see the following new menu items:

![](https://raw.github.com/isotope/docs/1.4/en/manual/images/2-backend_01.png)

Store setup can be configured in the “Store Configuration” module, and preferably from the bottom up:

1. Configuration & Email Templates
2. Tax Rates and Tax Classes
3. Shipping Methods
4. Payment Methods
5. Attributes
6. Product Types

Only begin adding products AFTER you have completed the setup process!


## Configurations

Different configurations include various settings such as currency, pricing and product image sizes. You can create multiple configurations for different stores within a Contao installation, or to allow switching between several different currencies. Take note of the following for each configuration:
- The primary configuration should be set as the “Default Configuration.” At least one default configuration is required.
- The country in the address of the configuration is used as the primary country for tax calculations and shipping.
- Take careful note of the possible countries/provinces for the allowed shipping and billing setings. Customer addresses can ONLY include those countries, and invalid addresses will not be available in the ordering process.


## E-Mail Templates

E-mail templates are used to send order confirmations and other messages to customers and shop owners. You will first need to create at least one email template and fallback language, as you will need this later for the ordering process when setting up the checkout module.

For a list of placeholders for use in text, please click on the "Help Wizard" located to the right of the field names. Each template can be created in multiple languages, so do not forget to set the main language fallback.


## Tax Rates

Tax rates correspond to universal sales taxes, which accrue differently in separate countries/states/regions. In Massachusetts, for example, you must create a sales tax of 6.25% on applicable goods.

Tax rates are the basic formulas for calculating the tax. You can choose for the rate to be valid on particular countries and/or states, and also which address (billing/shipping) and even what order subtotal ranges should be considered.

If you want to define a fixed price rate ($5.00 as opposed to 5%) first select a shop configuration. Then you will be able to select the configuration currency from the dropdown. However, this is taken into account only on this particular shop configuration and for other currencies you will need to set up separate shop configurations and separate tax rates.


## Tax Classes

Several tax rates can be grouped into an individual tax class, sorted and then assigned to each product. If you choose "tax included", it will be deducted from the price of the product (as is common in European stores), and will not be applied on checkout (for example, to a specific country in the billing address).


## Shipping Methods

With shipping methods, you can add the cost of shipping within the order process. This allows you to set up multiple shipping methods and rates for different countries/regions at once. For most basic cases you can use "Flat Rate Shipping", although there are other specific modules available for various shipping carriers such as UPS.

*If items in the cart do not require shipping (for example, a downloadable product), then the shipping address and shipping options will not appear in the checkout process.*


## Payment Methods

Payment methods define how people are able to pay for their purchases in the checkout process. Payment types are organized into several modules, each of which has their own characteristics.


### Cash

The cash module is used for all payments that are not automated in the system. This includes invoice and payment in advance. This module is useful for times when you want to collect order information and store it for billing at a later date, but not conduct an immediate transaction.


### Other Payment Modules

All other payment modules always refer to a provider, known as the Payment Provider. The Payment Provider will define which payment options (eg credit cards) are available. These modules will allow you to enter specific account and technical information such as API passwords / access codes.


## Attributes

You can define different attributes for products, and define their database field types. It is similar to Contao’s Form Generator module, only here we are creating additional custom fields to be entered on each product. If you want to define product variants such as size and/or color, then you will need to set up custom attributes. These custom attributes will get automatically added to the product DCA, so they do not need to hard-coded into the application.

The most important option in the attributes is "is used for variants”. Check this box if this attribute should be applied as a variant option. You can also define your own fields, which are not based on variants, such as a text field for the ISBN number for books.

Keep in mind that new attributes are - apart from variant options - not automatically displayed in the front end! You will need to edit the the listing and/or reader template, and add the appropriate variable in the desired position.


## Product Types

Product types are meant to be used for categorization, access control and configuration for different products.


### Overview

For each product type you can select your own lists and detail templates. In this way, two different item types represent different ways of displaying a product and its information. For example, you may have an attribute for books' such as an ISBN number that you do not necessarily want displaying on T-shirt products.


### Languages

You have the ability to define whether multiple languages will be recognized for product attributes. Typically, you will set up a shop with each product type the same language, but it can also be different if you have multiple stores on a single installation. For more information on managing the languages per product, read the chapter "Product Management".


### Attributes

The base installation of isotope eCommerce already includes the most important standard attributes that are typically needed for the shop to operate normally. But since not all global attributes are needed for each product, this can be configured in the product type.

The CheckBox Wizard will display all known attributes according to their legend groups. You can add attributes to your product type and sort them within each legend group using the up/down arrows. Some fields are mandatory and will not be able to be deselected as they are required for the system to function properly.


### Variants

If your product type has variant attributes, you can enable those in the product type as well. Select the attributes for variants which differ from the base product (eg price). Attributes that are not selected in the variants section are not available for editing on a variant product and will be inherited from the parent product.

*Note:* In isotope eCommerce a variant is a sub-product, which inherits most of the information (eg description) from the base product, but instead has individual attributes (eg price) which are different.


### Downloads

If you want to offer downloads, activate it in the product type. For more information on handling downloaded products, see the chapter "Product Management".


### Permissions per Product Type

You can choose to allow individual product types In the user groups preferences and on individual users. Here you can restrict access so that individual users can only manage certain product types, so that if you have several product managers in the backend they can each be assigned their own editable product type so that one cannot see the products of the other.