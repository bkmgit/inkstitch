---
title: "コリンの書き方"
permalink: /fr/fonts/honoka/
last_modified_at: 2024-05-23
toc: false
preview_image:
  - url: /assets/images/fonts/honoka.jpg
    height: 20
---

{%- assign font = site.data.fonts.honoka.font -%}

{% include upcoming_release.html %} 

![Honoka](/assets/images/fonts/honoka.jpg)

## Glyphes

Cette fonte comporte  {{ font.glyphs.size }} glyphes:

```
{{ font.glyphs | sort | join: ' ' }}
```
{: .font-glyphs }

Pour l'instant cette  fonte ne contient que  les  hiragana, les katakana et les symboles  de ponctuation. Ultérieurement, elle sera complétée pour inclure des kanji.
## Dimensions

A une échelle de  100% cette fonte a une hauteur approximative de  {{ font.size }} mm. 

Elle peut être redimensionnée  de {{ font.min_scale | times: 100 | floor }}% ({{ font.size | times: font.min_scale }} mm)
à {{ font.max_scale | times: 100 | floor }}% ({{ font.size | times: font.max_scale }} mm).



## Dans la vraie vie


{% include folder-galleries path="fonts/honoka/" %}



[Download Font License](https://github.com/inkstitch/inkstitch/tree/main/fonts/honoka/LICENSE)