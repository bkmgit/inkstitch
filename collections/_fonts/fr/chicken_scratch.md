---
title: "Chicken Scratch"
permalink: /fr/fonts/chicken_scratch/
last_modified_at: 2024-04-24
toc: false
preview_image:
  - url: /assets/images/fonts/chicken_scratch.jpg
    height: 28
---
{%- assign font = site.data.fonts.chicken_scratch.font -%}


{% include upcoming_release.html %} 

![Chicken Scratch](/assets/images/fonts/chicken_scratch.jpg)

## Glyphes

Cette fonte comporte  {{ font.glyphs.size }} glyphes:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }


## Dimensions

A une échelle de  100% cette fonte a une hauteur approximative de  {{ font.size }} mm. 

Elle peut être redimensionnée  de {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).



## Dans la vraie vie

{% include folder-galleries path="fonts/chicken_scratch/" %}



[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/violin_serif/LICENSE)