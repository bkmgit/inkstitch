---
title: "Pacificlo"
permalink: /fr/fonts/pacificlo/
last_modified_at: 2022-05-27
toc: false
preview_image:
  - url: /assets/images/fonts/pacificlo_tiny.jpg
    height: 8
  - url: /assets/images/fonts/pacificlo.jpg
    height: 20
data_title:
  - pacificlo
  - pacificlo_tiny
---
{%- assign font = site.data.fonts.pacificlo.font -%}
![Pacificlo](/assets/images/fonts/pacificlo.jpg)

![Pacificlo tiny](/assets/images/fonts/pacificlo_tiny.jpg)

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


![Dimensions Pacificlo](/assets/images/fonts/Sizing/pacificlosizing.jpg)

N'essayez pas de broder cette fonte à une dimension inférieure, vous auriez beaucoup de problèmes. 

La fonte Pacificlo tiny est une déclinaison de Pacificlo avec des paramètres de broderie différents. La densité, la compensation et les sous-couches ont été modifiées pour permettre de broder cette fonte en plus petite taille.

C'est pourquoi dans la fenêtre de dialogue du lettrage, il vous sera demandé  si vous utilisez Pacificlo tiny d'indiquer un redimensionnement entre 25 et 55% de la taille de Pacificlo, passant ainsi de lettres d'environ 20 mm de haut à des lettres entre 5 et 11 mm.


Contrairement à Pacificlo, Pacificlo tiny **DOIT** être brodée avec un fil et une aiguille plus fins que d'ordinaire. Une aiguille de taille 8 (USA), 60(EUR) et un fil 60 WT **DOIVENT** être utilisés.


## Dans la vraie vie
{% include folder-galleries path="fonts/pacificlo/" %}

[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/pacificlo/LICENSE)
