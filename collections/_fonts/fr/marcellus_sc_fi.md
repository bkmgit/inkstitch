---
title: "Marcellus SC FI "
permalink: /fr/fonts/marcellus_sc_fi/
last_modified_at: 2022-06-12
toc: false
preview_image:
  - url: /assets/images/fonts/marcellus_sc_fi.jpg
    height: 29
data_title:
  - marcelusSC_FI
---
{%- assign font = site.data.fonts.marcelusSC_FI.font -%}
![MarcellusSCFI](/assets/images/fonts/marcellus_sc_fi.jpg)


# Glyphes

Cette fonte comporte  {{ font.glyphs.size }} glyphes:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

Notez que les minuscules sont ici en fait des petites majuscules.

## Dimensions

A une échelle de  100% cette fonte a une hauteur approximative de  {{ font.size }} mm. 

Elle peut être redimensionnée  de {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).


Le paramètrage de la broderie vous permet d'aller au-delà de 200%, mais alors pour éviter les points trop longs, les colonnes satin utiliseront le "split satin", vous pouvez ou non aimer cet effet.

## Dans la vraie vie

{% include folder-galleries path="fonts/marcellus/" %}



[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/marcelusSC_FI/LICENSE)
