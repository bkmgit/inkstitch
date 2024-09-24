---
title: "Roman AGS"
permalink: /fr/fonts/roman_ags/
last_modified_at: 2022-05-27
toc: false
preview_image:
  - url: /assets/images/fonts/roman_AGS.jpg
    height: 28
  - url: /assets/images/fonts/roman_AGS_bicolor.jpg
    height: 28
data_title:
  - roman_ags
---
{%- assign font1 = site.data.fonts.roman_ags.font -%}
{%- assign font2 = site.data.fonts.roman_ags_bicolor.font -%}

<img 
     src="/assets/images/fonts/roman_AGS.jpg"
     alt="Roman AGS" height="60">
     
<img 
     src="/assets/images/fonts/roman_AGS_bicolor.jpg"
     alt="Roman AGS_bicolor" height="60">



## Glyphes
### Roman AGS 
Cette fonte comporte  {{ font1.glyphs.size }} glyphes:

```
{{ font1.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

### Roman AGS Bicolor
Cette fonte comporte  {{ font2.glyphs.size }} glyphes:

```
{{ font2.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

## Dimensions

A une échelle de  100% ces fontes ont une hauteur approximative de  {{ font.size }} mm. 

Elles peuvent être redimensionnées  de {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).


## Mélanger les deux polices

Les contours des glyphes des deux fontes étant exactement identiques pour les glyphes communs, il est très facile  d'utiliser les deux fontes conjointement :
- Faire un lettrage en Roman AGS avec l'ensemble du texte
- Faire un lettrage en Roman AGS bicolore avec  uniquement les glyphes que l'on souhaite bicolores
- Superposer exactement  chaque lettre colorée sur la lettre monochrome correspondante 
- Supprimer les lettres monochromes cachées par les bicolores

## Tri des couleurs 
Si vous utilisez des lettres bicolores, vous pouvez souhaiter trier les couleurs. C'est possible à condition de respecter leur ordre relatif à l'intérieur de chaque lettre. [Voici comment faire](https://inkstitch.org/fr/docs/lettering/#tri-des-couleurs)




## Dans la vraie vie
{% include folder-galleries path="fonts/roman_AGS/" %}

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/roman_ags_bicolor/LICENSE)

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/roman_ags/LICENSE)
