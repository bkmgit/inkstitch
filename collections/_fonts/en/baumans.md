---
title: "Baumans FI"
permalink: /fonts/baumans/
last_modified_at: 2024-04-20
toc: false
preview_image:
  - url: /assets/images/fonts/baumans_fi.jpg
    height: 32
  - url: /assets/images/fonts/baumans_FI_small.jpg
    height: 10
---

{%- assign font = site.data.fonts.baumans_FI.font -%}
![Baumans](/assets/images/fonts/baumans_fi.jpg)
![Baumans](/assets/images/fonts/baumans_FI_small.jpg)

## Glyphs

This font contains  {{ font.glyphs.size }} glyphs:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }
 
## Remark

Baumans FI is reversible : a multi line embroidery  may be  embroidered in alternate directions

## Dimensions
At a scale of 100% this font has an approximate height of {{ font.size }} mm. 

It can be scaled from {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
up to {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).

Baumans FI Small is a variation of this font with different embroidery settings. Pull compensation, density and underlays are different to allow to scale down between 30% (10 mm, 0.4 inch) and 15% (5mm ,1/5 inch). 
That's why in the lettering dialog window, if using Baumans FI Small, you will have to pick up a scale between 15 and 30%. 

Contrarly to Baumans FI, Baumans FI Small  **MUST** be embroidered with thread and needle smaller than usual.
A USA 8 (EUR 60) size needle, and 60WT thread **MUST** be used.


## In real life

{% include folder-galleries path="fonts/baumans/" %}

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/baumans_FI/LICENSE)
