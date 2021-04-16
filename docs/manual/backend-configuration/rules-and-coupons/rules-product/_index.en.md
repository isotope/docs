---
title: Product
description: 'Rules & coupons for products.'
aliases:
    - /en/backend-configuration/rules-and-coupons/rules-product/
weight: 10
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

## Basic control settings

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Type</td> <td>Product</td> <td>You have selected `Produkt` to create a rule.</td> </tr><tr><td>Name</td> <td>-</td> <td>Choose a meaningful name for this rule, so that you can keep track of several rules.</td> </tr><tr><td>Discount</td> <td>-</td> <td>Prefix a decimal number or a whole number with a minus sign, optionally you can also add a percent sign to the number. - 31.50 instead of 32.00 / reduction: -0.5
- 27.00 instead of 32.00 / reduction: -5
- 28.80 instead of 32.00 / discount: -10%
 
</td></tr></tbody></table>

## Restrict uses

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Usages per customer</td> <td>0</td> <td>Limit the use of the rule per customer to the value entered. If you leave zero, the customer will benefit from the rule as many times as they want.</td> </tr><tr><td>Uses per shop configuration</td> <td>0</td> <td>Limit the use of the rule per shop configuration to the value entered. If you leave the zero, the customer benefits from the rule as often as they want in each shop configuration.</td> </tr><tr><td>Lowest number of products</td> <td>0</td> <td>The rule is only applied when the number of products is at least the value you entered.</td> </tr><tr><td>Highest number of products</td> <td>0</td> <td>The rule is only applied when the number of products is at most equal to the value you entered.</td> </tr><tr><td>Quantity calculation mode</td> <td>Quantity of products in the shopping cart</td> <td>Here you can set the calculation mode for the minimum/maximum quantity. - Quantity of products in the shopping cart
- Quantity of different products in the shopping cart
- Total quantity in the shopping cart
 
</td></tr></tbody></table>

## Date &amp; time restrictions

{{% notice warning %}}
Note

that the dates and times behave like opening hours of a shop or office.  
E.g. in the period of 01/11/2015 - 10/11/2015 from 10:00 am to 6:00 pm respectively, the rule/voucher is valid.

{{% /notice %}}
 <table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Start date</td> <td>-</td> <td>If the rule should only be applied from a certain date, you can specify the start date here.</td> </tr><tr><td>End date</td> <td>-</td> <td>If the rule should only be applied until a certain date, you can specify the end date here.</td> </tr><tr><td>Start time</td> <td>-</td> <td>If the rule should only be applied from a certain date, you can specify the start time here.</td> </tr><tr><td>End time</td> <td>-</td> <td>If the rule should only be applied until a certain time, you can specify the end time here.</td></tr></tbody></table>

## Advanced restrictions

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Restrictions of the shop configuration</td> <td>-</td> <td>Here you can restrict the rule to specific <docrobot_route name="configuration">shop configurations</docrobot_route>.</td> </tr><tr><td>Shop configurations</td> <td>-</td> <td>Select to which configuration this rule should be restricted.</td> </tr><tr><td>Shop configuration condition</td> <td>True</td> <td>Choose whether the selection should match `Wahr` or not `Falsch`.</td> </tr><tr><td>Member Restrictions</td> <td>No restrictions</td> <td>- No restrictions
- Guests only
- Specific groupsHereyou can restrict the rule to specific groups. All member groups that you created in the user management of Contao are available for selection.
- Specific membersHere you can restrict the rule to specificmembers. You can use a search field to find users by first name, last name, username or email address.
 
</td> </tr><tr><td>Condition for members</td> <td>True</td> <td>Choose if the selection should match `Wahr` or not `Falsch`.</td> </tr><tr><td>Product Restrictions</td> <td>No restrictions</td> <td>- No restrictions
- Product typesHereyou can restrict the rule to certain product types. All <docrobot_route name="product-types">product types</docrobot_route>you have created in Isotope are available for selection.
- CategoriesHere you can restrict the rule tocertain categories by selecting the desired category page in the page tree.
- ProductsHere you can restrict the rule tocertain <docrobot_route name="product-management">products</docrobot_route>. A search field can be used to find products by product type, name or article number.
- Products &amp; VariantsHere you can limit the rule tocertain products &amp; variants. To do this, you need the product or variant IDs, which you can access by clicking on the blue icon (<img src="/de/images/show.gif?classes=icon">) behind the product or variant. You can enter the IDs in a comma-separated list.</docrobot_image>
- Product attributesHere you can restrict therule to certain product attributes. Select the product attribute and specify the attribute conditions:
  - is equal to
  - is not equal to
  - less
   
  than
  - greater
   
  than
  - less than or
  is equal to - greater than or is
   
  equal to
  - starts
   
  with
  - ends
   
  with
  - includes
   
  depending on which attribute you have selected a text or selection field is available.
 
</td> </tr><tr><td>Product conditions</td> <td>True</td> <td>Choose if the selection should match `Wahr` or not `Falsch`.</td></tr></tbody></table>

## Availability

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Active</td> <td>-</td> <td>Here you can choose if the rule is currently active.</td></tr></tbody></table>
