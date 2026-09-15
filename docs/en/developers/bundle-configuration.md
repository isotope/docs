# Bundle configuration

Most shop settings belong in the Contao backend. Bundle configuration is for the technical maintainer and is stored in the Contao project's Symfony configuration.

The documented bundle defines the root key `isotope` with `cart_timeout` and `currency_formats`. Do not copy an assumed configuration tree from another Isotope version.

## Guest cart retention

In the application's `config/config.yaml`:

```yaml
isotope:
    cart_timeout: '30 days'
```

The default is `30 days`. The value must be a time expression accepted by PHP's date parser. Prefer an ordinary positive duration such as `14 days` or `30 days`.

The daily cleanup job removes expired guest carts and carts whose member has been deleted. Existing members' carts are not subject to the guest timeout condition. This setting does not define order or document retention.

Verify that Contao's scheduled jobs run. Changing the duration does not itself execute a cleanup immediately.

## Currency formats

A named format defines decimal places and separators. For example:

```yaml
isotope:
    currency_formats:
        '10,000.00':
            decimals: 2
            decimal_separator: '.'
            thousands_separator: ','
        '10.000,00':
            decimals: 2
            decimal_separator: ','
            thousands_separator: '.'
```

Treat a custom map as your intended set of available formats and verify the resolved configuration. The bundle's defaults include ungrouped decimal-dot, comma-grouped, decimal-comma, and apostrophe-grouped formats.

Formatting is separate from currency choice, conversion factors, tax calculation, and rounding policy. Select and test the desired format in the store configuration after changing the available definitions.

## Validate changes

On the target Contao application, use its configuration inspection and YAML lint commands:

```bash
php vendor/bin/contao-console lint:yaml config
php vendor/bin/contao-console debug:config isotope
php vendor/bin/contao-console cache:clear --env=prod
```

Review the resolved values and test a new cart and displayed price. These commands require a complete Contao installation, not just the core source checkout.

Source: [IsotopeBundle configuration definition](https://github.com/isotope/core3/blob/96240eaa65c33a51e37951fe9833d9db1bd5980d/src/IsotopeBundle.php).
