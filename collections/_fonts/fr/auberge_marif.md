---
title: "Auberge Marif"
permalink: /fr/fonts/auberge_marif/
last_modified_at: 2023-04-25
toc: false
preview_image:
  - url: /assets/images/fonts/auberge_small.jpg
    height: 20
  - url: /assets/images/fonts/auberge_marif.jpg
    height: 50
data_title:
  - auberge_marif
  - auberge_small
---
{%- assign font = site.data.fonts.auberge_marif.font -%}
![auberge_marif](/assets/images/fonts/auberge_marif.jpg)

![auberge_small](/assets/images/fonts/auberge_small.jpg)

## Glyphes
Cette fonte comporte  {{ font.glyphs.size }} glyphes:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

## Dimensions

Utilisée à  100%, la hauteur de cette fonte est d'environ {{ font.size }} mm. 

Elle peut être redimensionnée de  {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).


![Dimensions Auberge Marif](/assets/images/fonts/Sizing/aubergesizing.jpg)

N'essayez pas de broder cette fonte à une dimension inférieure, vous auriez beaucoup de problèmes. 

La fonte Auberge Small est une déclinaison de Auberge Marif avec des paramètres de broderie différents . La densité, la compensation et les sous-couches ont été modifiées pour permettre de broder cette fonte en plus petite taille.

Dans la fenêtre de dialogue du lettrage si vous choisissez Auberge Small , il vous sera demandé d'indiquer un redimensionnement entre 25 et 55% de la taille de la fonte Auberge Marif, passant ainsi de lettres d'environ 50 mm de haut à des lettres entre 12 et 28 mm.

Contrairement à Auberge Marif, cette fonte diminuée **DOIT** être brodée avec un fil et une aiguille plus fins que d'ordinaire. Une aiguille de taille 8 (USA), 60(EUR) et un fil 60 WT **DOIVENT** être utilisés.



## Dans la vraie vie
De 25% sur le T shirt  à 100% sur le tablier.

{% include folder-galleries path="fonts/grand_hotel_marif/" %}

[Télécharger la License](https://github.com/inkstitch/inkstitch/tree/main/fonts/auberge_marif/LICENSE)
