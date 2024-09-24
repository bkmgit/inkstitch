---
title: "Violin Serif"
permalink: /fonts/violin_serif/
last_modified_at: 2024-04-23
toc: false
preview_image:
  - url: /assets/images/fonts/violin_serif.jpg
    height: 19
data_title:
  - violin_serif
---
{%- assign font = site.data.fonts.violin_serif.font -%}
![violin serif](/assets/images/fonts/violin_serif.jpg)

## Glyphs

This font contains  {{ font.glyphs.size }} glyphs:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

## Dimensions

At a scale of 100% this font has an approximate height of {{ font.size }} mm. 

It can be scaled from {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
up to {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).

## In real life

{% include folder-galleries path="fonts/violin_serif/" %}

## License

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/violin_serif/LICENSE.txt)
