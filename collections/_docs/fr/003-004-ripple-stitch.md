---
title: "Broderie Ondulée"
permalink: /fr/docs/stitches/ripple-stitch/
last_modified_at: 2024-04-28
toc: true
---
# De quoi s'agit-il ?

[![Ripple butterfly](/assets/images/docs/ripplefly.jpg){: width="200x"}](/assets/images/docs/ripplefly.svg){: title="Download SVG File" .align-left download="ripplefly.svg" }La broderie ondulée tient à la fois du point droit et du remplissage : elle se comporte comme un point droit (on peut l'exécuter  en point triple par exemple), elle est définie à partir d'un trait, mais elle produit à l'arrivée une broderie qui s'étend sur une surface. Utilisée de manière lâche, le résultat ressemble à des ondes, d'où son nom. 


Regardez cette  appétissante video: {% include video id="cyvby3KJM10" provider="youtube" %}

Si  le chemin initial est fermé la forme sera remplie par une spirale (ondulations  circulaires). S'il est ouvert, la broderie se fera en va et vient (ondulations linéaires)



## Ondulations  circulaires 

* Créer **un chemin fermé simple avec une couleur de contour et sans couleur de remplissage** (pas une combinaison de sous-chemins)
* Créer  [une  cible ou des guides](#guider-les-ondulations) (optionel)
* Sélectionner ce chemin
* Ouvrir le dialogue de paramètrage (`Extensions > Ink/Stitch > Paramètres`) et sélectionner `Broderie ondulée` comme méthode.
* Définir les  [paramètres](#comment-la-paramètrer) à votre convenence et Appliquer



![Exemples d'ondulations circulaires](/assets/images/docs/en/circular-ripple.svg)

[Télécharger les examples](/assets/images/docs/en/circular-ripple.svg)

## Ondulations linéaires

Les ondulations linéaires peuvent être créées de différentes manières. Le point de départ peut être un chemin simple ou bien être construit comme une colonne satin


* Créer une  forme ouverte ( un chemin simple, deux chemins combinés ou même une  colonne satin)
* Créer   [une  cible ou des guides](#guider-les-ondulations) (optionel)
* Sélectionner ce chemin
* Ouvrir le dialogue de paramètrage (`Extensions > Ink/Stitch > Paramètres`) et sélectionner `Broderie ondulée` comme méthode.
* Définir les  [paramètres](#comment-la-paramètrer) à votre convenence et Appliquer

![Exemples d'ondulations linéaires](/assets/images/docs/en/linear-ripple.svg)

[Télécharger les examples](/assets/images/docs/en/linear-ripple.svg)

## Ondulations avec boucles

Les boucles sont autorisées et bienvenues pour toutes les ondulations.
Utilisez les pour toutes  sortes d'effets spéciaux....

![Ondulations avec boucles](/assets/images/docs/en/ripple-loops.svg)

[Télécharger les examples](/assets/images/docs/en/ripple-loops.svg)


##  Guider les ondulations

Les ondulations construites à partir d'un chemin simple  (une forme fermée ou une courbe de bézier simple) peuvent être guidées en utilisant l'une quelconque de ces trois méthodes.

###  Guidage par cible
Il est possible de définir le point cible de l'ondulation grace aux [commandes visuelles](/fr/docs/commands/).

* Ouvrir `Extensions > Ink/Stitch > Commandes  > Attacher des  commandes à des objets selectionnés  ...`
* Sélectionner `Position de la cible` et appliquer.
* Sélectionner le symbole et le déplacer à la position souhaitée.

En l'absence de  toute information de guidage, c'est le centre de l'ondulation initiale qui tient lieu de point cible.


###  Guidage selon un chemin

* Directement dans le même groupe que la broderie ondulée (pas dans un sous-groupe), utilisez l'outil courbe de Beziers pour créer un chemin qui commence proche de l'ondulation puis s'en éloigne. 
* Selectionner cette courbe et exécuter  `Extensions > Ink/Stitch > Edition > Sélection vers guide`.
* Sélectionner la broderie ondulée.
* Ouvrir le dialogue de paramètrage (`Extensions > Ink/Stitch > Paramètres`) et sélectionner `Broderie ondulée` comme méthode.
* Définir les  [paramètres](#params) à votre convenence et Appliquer.


La position des centres des réplications de l'ondulation initale est alors déterminée par le guide.


### Guidage Satin 

Avec le guidage satin, vous pouvez  guider précisément les ondulations en utilisant une colonne satin pour guider au lieu d'un simple chemin. La largeur de la colonne satin a un effet sur la largeur des ondulations. 

* Directement dans le même groupe que la broderie ondulée (pas dans un sous-groupe), créez un objet similaire à une [colonne satin](/fr/docs/stitches/satin-column/) avec rails et traverses.
* Sélectionner ce nouvel objet et exécutez  `Extensions > Ink/Stitch > Edition > Sélection vers guide`.
* Sélectionner la broderie ondulée.
* Ouvrir le dialogue de paramètrage (`Extensions > Ink/Stitch > Paramètres`) et sélectionner `Broderie ondulée` comme méthode.
* Définir les  [paramètres](#params) à votre convenence et Appliquer.




## Comment la paramétrer

Paramètres||Description
---|---|---
Points droits le long des chemins   |  ☑  |Doit être activé pour que ces paramètres prennent effet.
Méthode      || Choisir Broderie Ondulée
Répétitions                     || Définir combien de fois le chemin final de broderie est exécuté en va et vient le long du parcours <br />◦ par défaut: 1 (aller une fois du début à la fin du chemin)<br />◦ Nombre impair: les points se termineront à la fin du chemin<br />◦ Nombre pair: la couture va revenir au début du chemin
Nombre de répétitions du point triple || Activer [Mode point triple](/fr/docs/stitches/bean-stitch/)<br />◦ Repasse sur chaque point le nombre de fois indiqué.<br />◦ Une valeur de 1 triplera chaque point (avant, arrière, avant).<br />◦ Une valeur de 2 permettra de quintupler chaque point, etc..<br />
Longueur du point droit||Longueur des points dans le [Mode Point Droit](/fr/docs/stitches/running-stitch/)
Tolérance du point droit||Tous les points doivent rester au plus à cette distance du chemin. Une tolérance plus faible signifie que les points seront plus rapprochés. Une tolérance plus élevée signifie que les angles vifs peuvent être arrondis.
Nombre de lignes|<img src="/assets/images/docs/ripple_only_lines.svg" alt="Nombre de lignes"/>|Choisir le nombre de réplications de l'ondulation dans la broderie. La valeur par défaut est 10.
Distance minimum entre les lignes        || Est prioritaire sur le nombre de lignes.
Décaler les lignes ce nombre de fois avant de répéter.    ||  Longueur du cycle de décalage des lignes successives. Les fractions sont autorisées et peuvent produire des diagonales moins visibles que les valeurs entières. La valeur par défaut (0) désactive le décalage. Ne concerne que les ondulations linéaires.
◦Sauter les premières lignes <br /> ◦Sauter les dernières lignes  |<img src="/assets/images/docs/ripple_only_skip.svg" alt="Sauter"/>| Permet de sauter (ne pas broder)  ce nombre de réplications au début et/ou à la fin. Sans effet sur les ondulations circulaires.
Exposant de la distance entre les lignes|<img src="/assets/images/docs/ripple_only_exponent.svg" alt="Exposant"/>| ◦ La valeur par défaut de 1 espace les réplications de manière constante<br />◦ Avec une valeur supérieure à  1 l'espace  entre deux réplications consécutives augmente au fur et à mesure qu'on s'éloigne du chemin qui définit l'ondulation  <br />◦ Avec une valeur inférieure à  1 l'espace  entre deux réplications consécutives diminue au fur et à mesure qu'on s'éloigne du chemin qui définit l'ondulation.
Inverser effet exposant |☑  ou ▢| Échange le rôle de la  première et de la dernière réplication pour le calcul de la distance entre les réplications
Changer le sens |☑  ou ▢|  Change le sens du  chemin final de broderie . N'a pas d'effet sur les autres paramètres.
Inverser la  direction des rails||Inverse les rails d'une ondulation satin. Par défaut détecte automatiquement, et corrige la direction d'un des rails.
Taille de la  grille |<img src="/assets/images/docs/ripple_only_grid.svg" alt="Distance"/>| Si une distance positive est spécifiée, les ondulations de la broderie sont complétées  en une "grille", par un chemin "perpendiculaire" aux ondulations. Le paramètre contrôle l'écart de ces perpendiculaires. Intervertir  n'a pas  d'influence sur ce paramètre.
Mettre à l'echelle sur l'axe |XY ou X ou Y ou rien|seulement pour des ondulations guidées.
Démarrer à| seulement pour des ondulations guidées|Taille de la première ondulation en pourcentage.
Finir à| seulement pour des ondulations guidées |Taille de la dernière ondulation en pourcentage.
Tourner| ☑  ou ▢| seulement pour des ondulations guidées
Style de Jointure|<img src="/assets/images/docs/flat_or_point.svg" alt="Join Stile"/> |pour des ondulations ouvertes,les réplications peuvent être jointes par un segment (en haut) ou en un seul point (en bas)
Longueur minimum de point||Est prioritaire par rapport à la valeur de la longueur minimum de point définie dans les préférences. Les points plus courts seront supprimés.
Longueur minimum de saut||Est prioritaire par rapport à la valeur de la longueur minimum de saut définie dans les préférences. Si la distance à l'objet suivant est inférieure, il n'y aura pas de points d'arrêt, sauf si les points d'arrêts sont forcés.
Autoriser les points d'arrêts | ☑  ou ▢|Choix de l'ajout d'un point d'arrêt en début et en fin de broderie.
Forcer les points d'arrêts | ☑ ou ▢| Force un point d'arrêt après l'objet indépendament de la valeur de "Saut de fil" dans les Préférences d'Ink/Stitch.
Point d'arrêt initial                  ||Choisir le  [style désiré](/fr/docs/stitches/lock-stitches/)
Point d'arrêt  final                  ||Choisir le  [style désiré](/fr/docs/stitches/lock-stitches/)
Couper après 	| ☑ ou ▢| Si coché, le fil est coupé après avoir brodé cet objet
Arrêter après 	| ☑ ou ▢|Si coché, la machine fait une pause après avoir brodé cet objet. Si une position d'arrêt a été définie, la machine la rejoint avant de s'arrêter.
{: .params-table }



Il existe de nombreuses manières d'exploiter toutes les possibilitéss :

![Ondulations diverses](/assets/images/docs/fr/rippleways_fr.svg)
[Download](/assets/images/docs/en/rippleways_fr.svg){: download="rippleways.svg" }





##  Exemples de fichiers qui utilisent la broderie ondulée 
{% include tutorials/tutorial_list key="stitch-type" value="Ripple Stitch" %}
