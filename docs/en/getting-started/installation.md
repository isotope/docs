# Install Isotope

**You will need:** access to Contao Manager and a compatible Contao website. If someone maintains the website for you, ask them to complete the hosting checks below.

**When you finish:** Isotope's administration tools are available in the Contao backend. The next chapter creates your first product and checkout pages.

## 1. Check the website is ready

This manual covers Isotope 3 with PHP 8.3 or newer within PHP 8, and Contao 5.7.4 or newer within Contao 5. The hosting environment must also satisfy Contao's requirements and provide the PHP DOM extension. Your maintainer can check the [technical installation requirements](../developers/installation.md).

If you do not have Contao yet, follow the official [Contao installation instructions](https://docs.contao.org/5.x/manual/en/installation/install-contao/). Choose a version compatible with the requirements above. You should be able to log in to the backend and open a published page before adding Isotope.

If you already have a Contao website, back up its files and database before adding software. If you are upgrading an existing Isotope shop, have your maintainer follow the [upgrade guide](../developers/upgrading.md) on a copy first.

## 2. Add Isotope with Contao Manager

1. Open Contao Manager for your website. It is separate from the backend where you edit page content.
2. Search for **`isotope/isotope-core`** in the packages section.
3. Add the package and check that the selected version belongs to Isotope 3, the version this manual describes.
4. Apply the package changes and wait for the installation to finish.
5. Run the database update offered by Contao Manager and review the proposed changes.
6. Return to the Contao backend and sign in as an administrator.

Contao Manager installs the supporting packages as well. One of them is Notification Center, which you will use later for order emails.

If the required version is not available or Manager reports a version conflict, keep the message and ask your maintainer to resolve it. Do not choose an older major version and expect this walkthrough to match it.

## 3. Check the result

In the backend, look for **Isotope eCommerce**. You should see these areas:

| Area | What you will do there |
| --- | --- |
| Products | Create the Trail T-shirt and later manage the catalog |
| Orders | Find and process purchases |
| Rules | Set conditions for prices, taxes, and checkout choices |
| Configuration | Set up product types, taxes, shipping, and payment |

Open **Configuration** and confirm it loads. Also open an existing page on the public website to check it still works.

If another staff account cannot see Isotope but the administrator can, check [staff access](../setup/general/access.md). If the database update failed, resolve that before creating shop records.

## 4. Build your first shop

Installation gives you the shop tools. You now supply the product, prices, delivery choices, and pages customers will use.

Continue directly with **[Your first shop](first-shop.md)**. It uses the same Trail T-shirt from [Our example shop](../concepts/example-shop.md) and takes you through a complete test purchase.

For command-line installation, see the separate [developer instructions](../developers/installation.md).
