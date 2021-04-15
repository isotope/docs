---
title: 'Inline gallery'
description: 'The shop configuration - General settings - Inline gallery.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/galleries/gallery-inline/
weight: 20
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

Compared to the [standard gallery](/de/backend-konfiguration-shop-allgemein-galerie-standard/), the `Inline Galerie` does not generate a large view of images or redirects. It is therefore normally only suitable for the[product reader](/de/frontend-konfiguration-module-Produktleser/) and replaces the large view of the image when clicking on a gallery image. It displays it "inline", which is the origin of the name of this gallery type.

## Basic configuration

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Placeholder image</td> <td>-</td> <td>Typically, especially during the development phase of a shop, there are always products that do not yet have a product image. Here you can optionally define a placeholder.</td></tr></tbody></table>

## Image sizes

{{% notice warning %}}This gallery type does **not** support the Responsive Images and the Picture element in Contao. {{% /notice %}}

 <table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Main image size</td> <td>-</td> <td>Here you set how the large view of an image should be cropped. An image is always the main image in this gallery type. This setting applies to this image.</td> </tr><tr><td>Gallery size</td> <td>-</td> <td>Here you can set how the rest of the images should be cropped. All other images except the main image are gallery images. This setting applies to those images.</td></tr></tbody></table>

## Watermark

Watermarks can be quite helpful especially when selling image products.

{{% notice warning %}}
Watermarks are **not** resized with the respective images but applied 1:1 as you created them!
{{% /notice %}}

 <table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Main image watermark</td> <td>-</td> <td>Here you can select a watermark image to apply to your main image.</td> </tr><tr><td>Main image watermark position</td> <td>-</td> <td>The position of a watermark can be important. Here you can define how Isotope eCommerce should position it for your main image.</td> </tr><tr><td>Gallery Image Watermark</td> <td>-</td> <td>Here you can select a watermark image to apply to your gallery images.</td> </tr><tr><td>Gallery Images Watermark Position</td> <td>-</td> <td>The position of a watermark can be important. Here you can define how Isotope eCommerce should position it for your gallery images.</td></tr></tbody></table>

## Template Settings

{{< version "2.2" >}}

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Custom gallery template</td> <td>-</td> <td>Here you can select your own gallery template to influence the HTML output in the frontend.</td></tr></tbody></table>
