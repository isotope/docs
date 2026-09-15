
# Isotope eCommerce documentation

This documentation is built using [**Zensical**](https://zensical.org/).

## Installation

Zensical requires Python 3.10 or newer. Install
[`uv`](https://docs.astral.sh/uv/getting-started/installation/) or follow the
[Zensical installation guide](https://zensical.org/docs/get-started/#installation).

## Preview

To preview the documentation, run:

```bash
uvx --python 3.14 zensical serve --config-file zensical.en.toml --open
```

The preview is available at <http://localhost:8000>. To use an automatically
selected free port instead, run:

```bash
port=$(python3 -c 'import socket; s = socket.socket(); s.bind(("", 0)); print(s.getsockname()[1])')
uvx --python 3.14 zensical serve --config-file zensical.en.toml --dev-addr "localhost:${port}" --open
```
