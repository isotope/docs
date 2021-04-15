# Contributing

## General rules

* Only use ATX style headlines (e.g. `# H1` or `### H3`).
* See [learn.netlify.com/en/cont/markdown/](https://learn.netlify.com/en/cont/markdown/)
  and [learn.netlify.com/en/shortcodes/notice/](https://learn.netlify.com/en/shortcodes/)
  for available markdown and shortcode syntax.
* Always add two empty lines above each headline.
* Add line breaks after 80 characters in paragraphs.
* Code examples should follow the Symfony Best Practices Book.
* When using examples for PHP code , include the example
  path to the file as a comment as the very first line. Do not use the `<?php` open
  tag and also do not use the `declare()` statement.

Example for link references:
```
Lorem ipsum dolor [sit amet](https://isotopeecommerce.org/) consectetuer adipiscing elitr. Aenean massa.
Cum sociis [natoque](https://www.google.com/) penatibus et magnis dis.
```

## Commonly used words

In Contao and Isotope eCommerce, some words are used regularly. To maintain a certain consistency, please follow these examples:

<table>
<thead>
<tr>
<th>Correct</th>
<th>Wrong</th>
</tr>
</thead>
<tbody>
<tr>
<td>Isotope eCommerce</td>
<td>e-Commerce, Ecommerce, ECommerce</td>
</tr>
<tr>
<td>Frontend</td>
<td>Front end, Front-End</td>
</tr>
<tr>
<td>Backend</td>
<td>Back end, Back-End</td>
</tr>
<tr>
<td>du, dich, deine</td>
<td>Du, Dich, Deine</td>
</tr>
<tr>
<td>z. B.</td>
<td>zum Beispiel, z.B.</td>
</tr>
<tr>
<td>Gross, Strasse</td>
<td>Groß, Straße (bitte nie ß verwenden)</td>
</tr>
</tbody>
</table>


## New features

Since we will not maintain different versions of the documentation for each minor
Isotope version, some features will be documented which are only available in a newer
Isotope version. In such a case, document the _old_ way first (if applicable), then
show the new way with a notice of the minimum Isotope version required.

You can use the following short code to automatically add a note for features of a
specific Isotope version:

```
{{< version "2.7" >}}
```


## Some notes about your markdown contribution

* All paths and filenames should be in English.
* Consider that all markdown headings are added to the navigation. Write your headings accordingly.
* Do not try to embed external images or reuse already existing images from other articles. External images might
  be removed over time and the same applies for images of other articles.
* Avoid belittling words: People read documentation because they know very little about a specific topic or are even
  completely new to it. Things that seem "obvious" or "simple" for the person documenting it, can be the exact opposite
  for the reader. To make sure everybody feels comfortable when reading the documentation, try to avoid words like:

    * basically
    * clearly
    * easy/easily
    * just
    * logically
    * merely
    * obviously
    * of course
    * quick/quickly
    * simply
    * trivial


## The Hugo front matter variables

Every file needs at least the following [Hugo front matter](https://gohugo.io/content-management/front-matter/)
variables on top of your markdown content:

* `title`: A title for the file (language specific). The title will be used in the main left navigation as well.
* `description`: The content description (language specific).
* `url` (optional): The URL path (language specific). This should only be used if you want the URL to be different from
  the effective file path. E.g. for the German translation.
* `aliases`: Aliases can be used to create redirects to your page. On multilingual sites, each translation
  of a post can have unique aliases. To use the same alias across multiple languages, prefix it with the language code.
* `weight` (optional): Used for the sorting order in the left main navigation of the documentation.
  The weight might not be necessary everywhere. It's only necessary, when files need to be sorted according to something
  different from the default sorting (= different from the filename).
* `menuTitle` (optional): The optional menuTitle reflects an alternative label in the main left navigation.
  This is especially helpful if the original title is too long to look nice in the navigation.


## Applying changes

If you want to contribute changes to a page, simply use the "Edit this page" link
at the top right of the documentation. Given that you have a GitHub account and
are logged in, GitHub will automatically create a fork where you can create your
changes in the respective markdown file. After committing your changes, GitHub will
offer you to create a Pull Request.

When changes to your Pull Request are requested, you can directly edit the files
within the Pull Request.


## Manual: English Translation Revision

On April 15th, 2021 the missing articles for the English translation of the manual
were added, using machine translation.
These automatically translated articles have a warning at the top. The quality of
the translation is fairly good, there are a few limitations however:

* The DeepL API often does not deal well with inline HTML tags. So there are many
  instances, where there is a space missing in front of or behind of `<code>` or
  `<a>` tags.
* Sometimes DeepL even shuffles an inline tag around, breaking words up (that should
  be pretty rare though).
* No 80 to 140 character line breaks.
* Any `` `…` `` content is not translated. Sometimes that's an issue, because it
  was used to emphasize regular words that are not code.
* The translation script caused some closing shortcode tags to be missing.

These articles now need to be reviewed and revised. When working on/fixing an article make sure that you:

* look over the translations themselves,
* look for specific terminologies, that should not be translated or should be translated
  in a specific way,
* fix any white space errors,
* provide English versions of screenshots (if applicable),
* look for any missing shortcode tags,
* review the result locally,
* and remove the warning at the top once finished

before submitting the Pull Request.
