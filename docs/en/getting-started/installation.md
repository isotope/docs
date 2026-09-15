
# Installation

Choose the installation method that matches your workflow!

## Installation via Contao Manager

Search for `isotope/isotope-core` in the Contao Manager and add it
to your installation. Apply changes to update the packages.

## Manual installation

Add a composer dependency for this bundle. Therefore, change in the project root and run the following:

```bash
composer require isotope/isotope-core
```

Depending on your environment, the command can differ, i.e. starting with `php composer.phar …` if you do not have
composer installed globally.

Then, update the database via the `contao:migrate` command or the Contao install tool.
