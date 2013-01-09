# Introduction

This guide is a handbook for the installation and configuration of Isotope eCommerce, an online store extension for Contao Open Source CMS.

**To promote TYPOlight’s new name, we will refer to the system as Contao Open Source CMS!**


## Conditions

To use this extension successfully, you should already be familiar with Contao Open Source CMS. Isotope eCommerce adheres strongly to the Contao framework, such as the use of listing and reader modules for the frontend.


## System Requirements

Isotope eCommerce can not be operated with all Contao installations.
The following conditions are required (older versions *will not work*):
- Contao 2.8.2 or later
- PHP 5.2
- The latest editions of “ajax“ and “conditionalselectmenu“ as found in the extension repository


## Database Notes

In principle, Isotope eCommerce was designed to follow the database abstraction used by Contao and thus the different database servers that it supports. However, in practice this has never been tested, so we recommend using MySQL as a database server.

The management interface of the shop and the database can be customized. Users may create additional database fields (columns), but data / fields should never be deleted. Columns need to be removed manually via the install tool.


## Installation

Isotope eCommerce - like many other Contao extensions - can be installed from the extension repository with a few clicks. Install the package directly into your system, or download the package from the extension repository at http://www.typolight.org/extension-list/view/isotope.html


## Presentation / Templates

As with the frontend of Contao itself Isotope eCommerce is built using templates. In many places users can choose their own templates to customize the presentation. If you are creating a standard shop, template changes are not necessary. For advanced functionality (such as custom product fields or attributes) this is necessary, however, you should be familiar with template changes within Contao before attempting to do so.