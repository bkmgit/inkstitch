---
title: "Glacial tiny 60 AGS"
permalink: /fr/fonts/glacial_tiny/
last_modified_at: 2022-06-12
preview_image:
  - url: /assets/images/fonts/glacial_tiny_60_AGS.jpg
    height: 8
data_title:
  - glacial_tiny
---
{%- assign font = site.data.fonts.glacial_tiny.font -%}
![glacial_tiny](/assets/images/fonts/glacial_tiny_60_AGS.jpg)

## Glyphes

Cette fonte comporte  {{ font.glyphs.size }} glyphes:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }


## Remarque 
Cette fonte permet de broder des textes multilignes alternativement de la gauche vers  la droite et de la droite vers la gauche.

## Avertissement

Cette fonte est extrêmement petite. Sa toute petite taille n'est possible que parce qu'elle est conçue pour être brodée avec des aiguilles fines (60 en europe, 8 aux USA) et du fil fin (60 wt) et non pas avec le fil de broderie usuel (40 wt). Passer outre ces recommandations risque de causer de gros problèmes à la broderie.

## Dimensions

A une échelle de  100% cette fonte a une hauteur approximative de  {{ font.size }} mm. 

Elle peut être redimensionnée  de {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).



![Dimensions Glacialtiny](/assets/images/fonts/Sizing/glacialsizing.jpg)

## Dans la vraie vie

Sur un coussin, un T Shirt et avec *Grand Hotel Marif* sur un tablier.

{% include folder-galleries path="fonts/glacial_tiny/" %}

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/glacial_tiny/LICENSE)
