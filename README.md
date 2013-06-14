# How to contribute

This repository is used to document Isotope eCommerce.
You are invited to contribute to it using pull requests.

We do have several different books, such as

* manual
* cookbook
* etc.

Every book can have it's own pages. The `config.json` file in the root defines, how the book is being parsed on the official website (isotopeecommerce.org).

## config.json

A route directly after the root directory has to be defined as follows:

```json
{
    "system_requirements": {
        "type": "regular",
        "title": "Systemvoraussetzungen"
    }
}
```

The route (in this case `system_requirements`) can be of two different `type`s.

`regular` for a normal content page.
`redirect` for a page that should redirect to another route (scroll down to read about this).

`title` defines the title this page will get in the navigation module on isotopeecommerce.org.

### Defining sub pages (children)

You can use as many levels as you like. Just define the `children` for any route.
Example:

```json
{
    "system_requirements": {
        "type": "regular",
        "title": "Systemvoraussetzungen",
        "children": {
            "installation": {
                "type":"regular",
                "title": "Installation"
            }
        }
    }
```

### Redirecting routes

You can redirect to a specific target route using the `type` and `targetRoute` configuration parameters:

```json
"redirect_page": {
    "type": "redirect",
    "title": "I am a redirect page",
    "targetRoute": "system_requirements"
}
```

### Why is every page a folder and contains an index.md instead of just being one file?

This is a feature as if the documentation gets bigger, we might want to split one page in different files, so we're ready for the future :-)