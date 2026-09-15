"""Check the manual's navigation, links, YAML examples, and optional source links."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import markdown
import tomli
import yaml

ROOT = Path(__file__).resolve().parents[1]


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get('id'):
            self.ids.add(attributes['id'])
        if tag in ('a', 'link') and attributes.get('href'):
            self.links.append(attributes['href'])
        if tag in ('img', 'script') and attributes.get('src'):
            self.links.append(attributes['src'])


def parse_page(contents):
    page = PageLinks()
    page.feed(contents)
    return page


def navigation_paths(items):
    for item in items:
        for value in item.values():
            if isinstance(value, list):
                yield from navigation_paths(value)
            else:
                yield value


def check_navigation(project, docs, errors):
    paths = list(navigation_paths(project['nav']))
    local_paths = [p for p in paths if not urlsplit(p).scheme]
    for value in local_paths:
        if value == '#' or not (docs / value).is_file():
            errors.append(f'Navigation target does not exist: {value}')
    expected = {str(p.relative_to(docs)) for p in docs.rglob('*.md')}
    for missing in sorted(expected - set(local_paths)):
        errors.append(f'Page is missing from navigation: {missing}')
    for path in set(local_paths):
        if local_paths.count(path) > 1:
            errors.append(f'Duplicate navigation target: {path}')


def check_link(origin, value, pages, base, errors, site_prefix=None):
    link = urlsplit(value)
    if link.scheme or link.netloc:
        return
    if value == '#':
        if site_prefix is None:
            errors.append(f'{origin.relative_to(base)}: placeholder link')
        return
    path = unquote(link.path)
    if site_prefix is not None and path.startswith('/'):
        if site_prefix and path.startswith(site_prefix):
            path = path[len(site_prefix):]
        target = (base / path.lstrip('/')).resolve()
    else:
        target = (origin.parent / path).resolve() if path else origin
    if target.is_dir():
        target = target / ('index.html' if site_prefix is not None else 'index.md')
    if not target.is_file():
        errors.append(f'{origin.relative_to(base)}: missing target {value}')
    elif link.fragment and target in pages:
        if unquote(link.fragment) not in pages[target].ids:
            errors.append(f'{origin.relative_to(base)}: missing anchor {value}')


def check_yaml(path, text, errors):
    for block in re.findall(r'^```ya?ml\n(.*?)^```', text, re.M | re.S):
        try:
            yaml.safe_load(block)
        except yaml.YAMLError as exc:
            errors.append(f'{path}: invalid YAML example: {exc}')


def check_source_links(pages, core, errors):
    references = set()
    for page in pages.values():
        for link in page.links:
            match = re.match(r'https://github.com/isotope/core3/(?:blob|tree)/([0-9a-f]{40})/(.+)', link)
            if match:
                references.add((match[1], urlsplit(match[2]).path))
    for revision, path in sorted(references):
        result = subprocess.run(
            ['git', '-C', str(core), 'cat-file', '-e', f'{revision}:{path}'],
            capture_output=True,
        )
        if result.returncode:
            errors.append(f'Source reference does not exist: {revision}:{path}')
    print(f'Checked {len(references)} pinned core source references')


def check_site(directory, project, errors):
    base = directory.resolve()
    pages = {p.resolve(): parse_page(p.read_text()) for p in base.rglob('*.html')}
    if not pages:
        errors.append(f'No generated HTML pages in {base}')
        return
    prefix = urlsplit(project['site_url']).path
    for path, page in pages.items():
        for link in page.links:
            check_link(path, link, pages, base, errors, site_prefix=prefix)
    print(f'Checked links and anchors in {len(pages)} generated HTML pages')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core-source', type=Path)
    parser.add_argument('--site', type=Path)
    args = parser.parse_args()
    project = tomli.loads((ROOT / 'zensical.en.toml').read_text())['project']
    docs = (ROOT / project['docs_dir']).resolve()
    errors = []
    pages = {}
    words = 0
    for path in sorted(docs.rglob('*.md')):
        text = path.read_text()
        words += len(text.split())
        if len(re.findall(r'^# ', text, re.M)) != 1:
            errors.append(f'{path.relative_to(docs)}: expected one page title')
        check_yaml(path.relative_to(ROOT), text, errors)
        pages[path] = parse_page(markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc']))
    check_navigation(project, docs, errors)
    for path, page in pages.items():
        for link in page.links:
            check_link(path, link, pages, docs, errors)
    for path in (ROOT / '.github/workflows').glob('*.yml'):
        yaml.safe_load(path.read_text())
    if args.core_source:
        check_source_links(pages, args.core_source, errors)
    if args.site:
        check_site(args.site, project, errors)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Passed: {len(pages)} pages, {words:,} words, complete navigation and valid local links')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
