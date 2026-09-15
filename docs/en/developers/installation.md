# Technical installation

This chapter is for the person maintaining the Contao application. Shop owners can use the [Contao Manager installation flow](../getting-started/installation.md).

## Requirements

The documented Isotope 3 revision declares:

| Component | Constraint |
| --- | --- |
| PHP | `^8.3` |
| Contao core bundle | `^5.7.4` |
| Composer runtime API | `^2` |
| PHP DOM extension | Required |

Contao and other dependencies add hosting requirements. Verify the resolved package set, rather than treating these few constraints as the entire platform check. Core CI tests PHP 8.3, 8.4, and 8.5 with Contao 5.7.

Source: [package requirements](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/composer.json).

## Install into the application

Run from the Contao project directory containing `composer.json`:

```bash
composer require isotope/isotope-core
php vendor/bin/contao-console contao:migrate
```

The unqualified package name resolves the version allowed by the project. Confirm that it selects the intended Isotope 3 release. Use the project's agreed version constraint when targeting a particular release, and do not weaken project-wide stability settings merely to install a development checkout.

Review migration prompts and preserve a restorable backup for an existing application. Do not ignore platform requirements to bypass dependency conflicts.

For an existing Isotope shop, rehearse the [upgrade](upgrading.md) and inspect historical records before production changes.

## Hand over to the shop owner

Confirm that an administrator can open Isotope Configuration, ordinary Contao pages still load, and database updates have finished. Grant the intended [staff permissions](../setup/general/access.md).

Provide the backend and test-site addresses and the installed version. The shop owner can then continue with [Your first shop](../getting-started/first-shop.md). Keep provider credentials and deployment procedures in the appropriate protected project records.
