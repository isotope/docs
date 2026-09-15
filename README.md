# Isotope eCommerce documentation

A beginner-friendly Isotope 3 manual, from installation and shop concepts to catalog setup, checkout, daily operations, and development.

Start reading at [the manual homepage](docs/en/index.md). The practical entry point is [Your first shop](docs/en/getting-started/first-shop.md).

## Source baseline

The manual was checked against `isotope/core3` revision `96240eaa65c33a51e37951fe9833d9db1bd5980d`. Important implementation inconsistencies are recorded in [Version notes](docs/en/developers/version-notes.md). Update those notes alongside the relevant chapters when the source changes.

## Install the documentation tools

Use Python 3.10 or newer in a virtual environment outside `.cache`, which the site builder may delete when cleaning. The package versions are pinned in `requirements-docs.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. The [Zensical installation guide](https://zensical.org/docs/get-started/) describes other supported setups.

## Preview

```bash
zensical serve --config-file zensical.en.toml
```

Open the local address printed by Zensical. The configuration is for the English manual. No German translation is included yet.

## Validate and build

```bash
python scripts/check_docs.py
zensical build --config-file zensical.en.toml --strict
python scripts/check_docs.py --site .build
```

The checker verifies page titles, complete navigation, local links and anchors, YAML examples, and workflow YAML parsing. The final command also checks links and anchors in the generated HTML, including the not-found page. Zensical writes the static site to `.build`.

When the source checkout is available, also verify every pinned source reference:

```bash
python scripts/check_docs.py --core-source /path/to/isotope-core3
```

The documentation GitHub Actions workflow runs the same source-page and generated-site checks with a strict build. It builds without publishing.

## Writing guidelines

Explain what a feature is and why it exists before giving configuration steps. Use concrete examples and a way to verify the outcome. Keep core behavior separate from extension-specific capabilities and business decisions. Use fictional tax percentages for teaching examples.

Keep links relative within `docs/en`, add every page to `zensical.en.toml`, and preserve applicable inline comments. Do not use semicolons in prose or comments.

The core repository has its own PHPStan, Rector, ECS, dependency-analysis, PHPUnit, and frontend tooling. Those checks apply to core code changes. This repository changes documentation, its navigation, and its build/check tooling.

## Validation boundary

A successful documentation build checks the manual, not a live shop. The source-based instructions still need acceptance testing in a configured Contao application with its database, mail delivery, payment integrations, and custom templates. Use the [launch checklist](docs/en/getting-started/launch.md).

## Editorial conventions

Write for a shop owner who may be new to eCommerce and Contao. Explain the purpose of a concept before its settings. Procedures should name prerequisites, give ordered steps, and show what a successful result looks like.

- **Getting started** covers orientation, installation through Contao Manager, a first purchase, and launch.
- **Shop setup** covers reusable configuration and choices that affect several products or orders.
- **Daily use** starts from an already configured shop and covers product editing, pricing, orders, and operational checks. Link to setup prerequisites rather than repeating them.
- **Developers** contains command-line work, configuration files, templates, extension code, upgrades, performance, and source-specific implementation notes.

Use [Trail Supply](docs/en/concepts/example-shop.md) throughout. The Trail T-shirt is the main product. Use the Trail hoodie only when a second product is useful and garment wash for comparison pricing by volume. Keep SKU, price, tax, shipping, and quantity examples consistent with that page. Clearly label any variation from the first-shop baseline. All teaching tax rates are fictional.

Keep customer-facing prose free of implementation detail unless it changes a decision the reader must make. Preserve source evidence in the developer source map. Do not use semicolons in prose or comments. Run the documentation checks after changing pages or navigation.

Navigation must follow the section’s workflow. Keep each overview, sidebar, and explicit next-step link in agreement. For sequential setup, put prerequisites before the settings that use them and optional features after the basic path. For daily work, group recurring tasks in operational order. Treat installation and upgrading as alternative developer entry points.
