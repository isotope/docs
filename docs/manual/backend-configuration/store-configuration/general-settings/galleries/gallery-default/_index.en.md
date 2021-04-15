---
title: 'Standard gallery'
description: 'The shop configuration - General settings - Standard gallery.'
aliases:
    - /en/backend-configuration/store-configuration/general-settings/galleries/gallery-default/
weight: 10
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

The `Standard Galerie` displays a normal image gallery as you would imagine it. It displays small thumbnails and a large view of an image. Optionally the large view in a lightbox can be selected.

## Basic configuration

|      Setting      | Default setting |                                                                                                                                                            Description                                                                                                                                                             |
|-------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image anchor      | -               | Here you can set what should happen when you click on the large view of the image. If you use this gallery in the product list, you can select <code>Link zu den Produktdetails</code> here. Typically, you leave the product reader then a <code>Lightbox/Mediabox öffnen</code>. But you can also execute <code>keine Link-Aktion</code>, just as you like. |
| Placeholder image | -               | Typically, especially during the development phase of a shop, there are always products that do not yet have a product image. Here you can optionally define a placeholder.                                                                                                                                                        |

## Image sizes

|     Setting     | Default setting |                                                                           Description                                                                           |
|-----------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main image size | -               | Here you set how the large view of an image should be cropped. An image is always the main image in this gallery type. This setting applies to this image.      |
| Gallery size    | -               | Here you can set how the rest of the images should be cropped. All other images except the main image are gallery images. This setting applies to those images. |

## Watermark

Watermarks can be quite helpful, especially when selling image products.

{{% notice warning %}}
Watermarks are **not** resized with the respective images but applied 1:1 as you created them!
{{% /notice %}}

|              Setting              | Default setting |                                                             Description                                                             |
|-----------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Main image watermark              | -               | Here you can select a watermark image to apply to your main image.                                                                  |
| Main image watermark position     | -               | The position of a watermark can be important. Here you can define how Isotope eCommerce should position it for your main image.     |
| Gallery Image Watermark           | -               | Here you can select a watermark image to apply to your gallery images.                                                              |
| Gallery Images Watermark Position | -               | The position of a watermark can be important. Here you can define how Isotope eCommerce should position it for your gallery images. |

## Template Settings

{{< version "2.2" >}}

|         Setting         | Default setting |                                         Description                                         |
|-------------------------|-----------------|---------------------------------------------------------------------------------------------|
| Custom gallery template | -               | Here you can select your own gallery template to influence the HTML output in the frontend. |
