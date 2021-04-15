---
title: Video/Audio
description: 'The shop configuration - video/audio.'
aliases:
    - /en/backend-configuration/store-configuration/products/attributes/video-audio/
weight: 145
---

{{% notice warning %}}
This article is machine translated.
{{% /notice %}}

{{< version "2.2" >}}

This attribute behaves identically to the content element known from Contao Core, so you can easily use videos or audio files for the product presentation.

{{% notice warning %}}
The

 *j\_mediaelement template*

 must be included in the page layout. 
{{% /notice %}}
 ## Description

<table><thead><tr><th>Setting</th> <th>Default setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Description</td> <td>-</td> <td>This description serves as a hint to the backend user and is displayed below the input field.</td></tr></tbody></table>

## Attribute Configuration

<table><thead><tr><th>Setting</th> <th>Default Setting</th> <th>Description</th> </tr></thead><tbody><tr><td>Base Directory</td> <td>-</td> <td>Specify here from which directory the folder structure should be displayed.</td> </tr><tr><td>Mandatory field</td> <td>-</td> <td>The product cannot be saved (backend) or added to the shopping cart (frontend) without this information.</td> </tr><tr><td>Multilingual</td> <td>-</td> <td>Select whether this attribute must be translated into other languages.</td></tr></tbody></table>

The attribute is created in the backend via the [product types](/de/backend-konfiguration-shop-Produkttypen/). In the fontend you can output the attribute in the desired isotope template with the following code `<?php echo $this->generateAttribute('interner_name'); ?>`.

The attribute can also be given further options:

```
<?php
$arrOptions = array();
$arrOptions['autoplay'] = true; // Video automatisch abspielen
$arrOptions['width'] = 640; // Breite des Video-Players
$arrOptions['height'] = 480; // Höhe des Video-Players

echo $this->generateAttribute('interner_name', $arrOptions);
?>
```

{{% notice info %}}
 The following video and audio files are supported: **mp4**, **m4v**, **mov**, **wmv**, **webm**, **ogv**, **m4a**, **mp3**, **wma**, **mpeg**, **wav** and **ogg**. In  
addition, you can store a still image for the video or the audio file in the following formats: **jpg**, **jpeg**, **gif**, **png**, **tif**, **tiff** and **bmp**. 
{{% /notice %}}
