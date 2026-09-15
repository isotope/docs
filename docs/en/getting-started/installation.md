# Installation

Install Isotope into a working Contao website. If this is an existing shop, follow [Upgrading](../guides/upgrading.md) first and rehearse the changes on a copy.

## Requirements for the documented source

The core package declares these requirements:

| Component | Requirement |
| --- | --- |
| PHP | `^8.3`, meaning PHP 8.3 or later within PHP 8 |
| Contao core bundle | `^5.7.4`, meaning Contao 5.7.4 or later within Contao 5 |
| Composer runtime API | Version 2 |
| PHP DOM extension | Required explicitly by Isotope |

Contao and the other dependencies have additional hosting requirements. These are package constraints for the documented revision, not a promise that every combination of extensions is compatible. The core CI tests PHP 8.3, 8.4, and 8.5 with Contao 5.7.

The package manager installs dependencies such as Notification Center. You still need to configure notifications and mail delivery.

Source: [core package requirements](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/composer.json).

## If you do not have Contao yet

Follow the official [Contao installation instructions](https://docs.contao.org/5.x/manual/en/installation/install-contao/). Choose a Contao version compatible with the table above. Set the web server's document root to the installation's `public` directory, configure the database, and create a backend administrator.

Before adding Isotope, confirm that you can log in to the backend and display a published page. This separates hosting problems from shop configuration problems.

## Install with Contao Manager

1. Back up the database and website files if the installation already contains work.
2. Open Contao Manager for this website.
3. Search for `isotope/isotope-core` and add the package.
4. Select the intended compatible Isotope release. The unqualified package name alone does not ensure you receive the source version described by this manual.
5. Apply the package changes and wait for completion.
6. Run the database update offered by Contao Manager. Review the proposed changes before applying them.
7. Sign in to the Contao backend again.

You should now find the **Isotope eCommerce** administration group. A new shop does not yet have a complete storefront.

## Install from the command line

For an administrator comfortable with a terminal, run this from the Contao project directory, where `composer.json` is located:

```bash
composer require isotope/isotope-core
php vendor/bin/contao-console contao:migrate
```

The first command resolves the release allowed by your project's constraints. Check the selected version before continuing with this Isotope 3 manual. For a specific release, use the version constraint agreed for your project. Do not lower project-wide stability requirements simply to make a development version install.

The migration command updates the database. Read its prompts, especially on an existing installation. Never resolve a package conflict by ignoring platform requirements.

The package installation sequence is also documented in the [core README](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/README.md).

## Verify the installation

- Isotope appears in the backend for an administrator.
- **Configuration** opens without an error.
- The database update completes successfully.
- Existing Contao pages still load.
- Installed package versions match the project requirements.

If Isotope is visible to an administrator but not to another staff account, check that account's backend permissions. If tables or columns are missing, check migration output. If package installation fails, retain the dependency conflict message and resolve the named version conflict.

Next: [Setup roadmap](../setup/index.md), then [Your first shop](../guides/first-shop.md).
