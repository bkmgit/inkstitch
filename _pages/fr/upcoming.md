---
title: "Changements, Mises à jour et Corrections pour Ink/Stitch v3.0.0"
permalink: /fr/upcoming/
last_modified_at: 2023-05-12
sidebar:
  nav: pages
toc: true
---
## General
Ink/Stitch sera significativement plus rapide pour recalculer le plan de broderie grace à des caches.

## Nouvelles fontes

* [Abril En Fleur AGS](/fr/fonts/abril/)

  ![Abril En Fleur AGS](/assets/images/fonts/abril_en_fleur.jpg)
* [Apex Simple AGS](/fr/fonts/apex-lake/)

  ![Apex Simple AGS](/assets/images/fonts/apex_simple_AGS.jpg)
* [AGS Γαραμου Garamond](/fr/fonts/AGS_greek_garamond/)

  ![AGS Γαραμου Garamond](/assets/images/fonts/garamond.png)
* [Emilio 20 simple](/fr/fonts/emilio-20/)

  ![Emilio 20 simple](/assets/images/fonts/emilio_simple.png)
* [Emilio 20 bold](/fr/fonts/emilio-20/)

  ![Emilio 20 bold](/assets/images/fonts/emilio_20_bold.png)
* [Emilio 20 Applique](/fr/fonts/emilio-20/)

  ![Emilio 20 Applique](/assets/images/fonts/emilio_20_applique.png)

* La fonte `Grand Hotel` a été renommée `Auberge`

* D'autres fontes ont été améliorées

## Elements / Types de points

### Nouveaux types de point

#### Remplissage en méandres

[Le remplissage en méandres](/fr/docs/stitches/meander-fill)  est originaire des techniques de quilting. Il produit un beau résultat en broderie machine. De grandes zones peuvent être remplies avec relativement peu de points. 
![Meander Fill](/assets/images/tutorials/tutorial-preview-images/meandering_writing.jpg)

#### Remplissage circulaire

[Le remplissage circulaire](/fr/docs/stitches/circular-fill) remplit une forme avec une spirale. Le centre de la spirale est positionné au centre de la forme. Il et possible de personnaliser la position du centre de la spirale à l’aide d’une cible.

![Circular Fill](/assets/images/tutorials/tutorial-preview-images/circular_monogram.jpg)

### Nouveaux paramètres

#### Commandes de coupe et de stop
  * Il  n'est plus obligatoire d'utiliser des commandes visuelles pour les commandes de  coupe et de stop, elles peuvent être ajoutées dans le dialogue de paramètrage.

  * [La mise à l'échelle des commandes](/fr/docs/commands/#mise-%C3%A0-lechelle-des-symboles-de-commande) mets aussi à jour les marqueurs  (ligne - guide et symbole de texture)

#### Points de sûreté
  * Possibilité de choisir dans une liste de points d'ancrage et points d'arrêt prédéfinis
  * Mise à l'échelle possible
  * Possibilité de définir ses propre points de sûreté 

### Clones
  * Correction : positionnement
  * Correction : calcul automatique de l'angle de remplissage

    ![Clone fill angle](/assets/images/docs/clone_fill_angle.png)

### Point multiple

  * Ajout [des motifs de répétitions personnalités](/fr/docs/stitches/bean-stitch/#paramètres) (1 0: ☰-☰-☰-)

    ![Bean pattern](/assets/images/docs/bean_pattern.jpg)

### Point Manuel
  * Ajout automatique de points de d'arrêt possible via l'option *Forcer les points d'arrêt*
  * Ajout d'une *longueur maximum de points*

### Remplissage
  * Possibilité de [valeur non entière pour le décalage des rangées](/fr/docs/stitches/fill-stitch/#parametres)
  * [Espacement final entre les rangées](/fr/docs/stitches/fill-stitch/#parametres) est maintenant exposé  et non plus caché (utile pour mélanger des couleurs)
  * [Les valeurs multiples d'angle de sous-couche](/fr/docs/stitches/fill-stitch/#sous-couche) sont maintenant séparées par un espace et non plus par une virgule


  * Correction de l'erreur: 'LineString' object has no attribute 'geoms'
  * Correction de l'erreur: 'Point' object has no attribute 'geoms'
  * Correction de l'erreur: ZeroDivisionError in intersect_region_with_grating
  * Correction de l'erreur: ZoneClose segments can not be changed into curves.
  * Correction :  décalage incorrect du remplissage guidé

### Colonne satin/ E-Stitch
  * [Options aléatoires](/fr/docs/stitches/satin-column/#couche-supérieure-du-satin): longueur, espacement, découpe
    ![Bee](/assets/images/docs/random_satin.jpg)

  * [Compensation d'étirement](/fr/docs/stitches/satin-column/#couche-supérieure-du-satin)
	* Possibilité d'appliquer deux valeurs différentes aux deux rails en les séparant par un espace
	* Peut  être exprimée en mm et en %
    
    * Ajout de l'option [Inverser les rails](/fr/docs/stitches/satin-column/#couche-supérieure-du-satin) pour une action rapide dans le dialogue de paramètrage

  * Correction: Pas d'échec si la colonne satin a aussi un remplissage, mais rendu de la colonne satin et du remplissage

### Trait

  * Le paramètrage est plus flexible. Il est plus facile de basculer du point droit au zigzag : plus besoin de mettre un pointillé pour le point droit. 
   
  * Amélioration de l'algorithme de calcul du point droit (la longueur de point est plus régulière)
  *  Les éléments de type `svg:line` sont maintenant reconnus comme des traits normaux

### Point zigzag
  * Ajout d'une compensation d'étirement

### Broderie ondulée

Ajout de  [paramètres](/fr/docs/stitches/ripple-stitch/#comment-la-paramétrer):
* *décalage* : pour un meilleur positionnement des points
* *distance minimum entre les lignes* : pour une densité constante en cas de redimensionnement  (prioritaire sur le nombre de lignes)

## Extensions

### Nouveau : Convertir en blocs de dégradés

Divise une forme munie d'un  dégradé de couleur en plusieurs blocs monochromes qui peuvent être utilisés pour broder le  dégradé


![Gradient](/assets/images/docs/color_blocks.png)

Extensions > Ink/Stitch > Outils: Remplissage > [Convertir en blocs de dégradés](/fr/docs/fill-tools/#convertir-en-blocs-de-dégradés)


### Nouveau: Lettrage le long d'un chemin

Place un groupe de lettrage le long d'un chemin sans déformer les glyphes.


![Lettering along path](/assets/images/docs/lettering_along_path.png)

Extensions > Ink/Stitch > [Lettrage le long d'un chemin](/fr/docs/lettering/#lettrage-le-long-dun-chemin)

### Nouveau: Saut en Trait

Génère un point droit  rectiligne entre la fin et le début d'éléments consécutifs
G
![Jump to Stroke](/assets/images/docs/jump_to_stroke.png)

*1: Original 2: Saut en chemin 3: Chemin ajusté manuellement*

Extensions > Ink/Stitch > Outils: Trait > [Saut en Trait](/fr/docs/stroke-tools/#saut-en-trait)

### Nouveau : Remplissage en Trait

Génère  une ligne centrale pour les remplissages



![Fill to Stroke](/assets/images/docs/fill_to_stroke.png)

Extensions > Ink/Stitch > Outils: Traite > [Remplissage en Trait](/fr/docs/stroke-tools/#remplissage-en-trait)

### Nouveau: Trait en  Effet de Chemin  Satin

Converti un trait en effet de chemin satin


![LPE Satins](/assets/images/docs/lpe_patterns.png)

Extensions > Ink/Stitch > Outils: Satin: [Trait en effet de chemin Satin](/fr/docs/satin-tools/#trait-en-effet-de-chemin-satin)

### Nouveau: Ligne Zigzag en Satin

Converti une ligne en zigzag ou en dents de scie en colonne satin. s

![Zigzag to Satin](/assets/images/docs/zigzag-line-to-satin.png)

Extensions > Ink/Stitch > Outils: Satin > [Ligne Zigzag en Satin](/fr/docs/satin-tools/#ligne-zigzag-en-satin)

### Nouveau: Mettre à jour le svg d'Ink/Stitch 

Ink/Stich mets automatiquement à jour les anciens fichiers de dessin. N'utilisez cette extension que si vous savez ce que vous faite.a

Extensions > ink/Stitch > Résolution de problèmes > [Mettre a jour le svg d'Ink/Stitch](/fr/docs/troubleshoot/#mettre-%C3%A0-jour-le-svg-dinkstitch)

### Nouveau: Sélectionner les éléments de broderie 

Sélectionner les éléments par type de points (non disponible pour macOS)

Extensions > Ink/Stitch > Edition > Selectionner les éléments de broderie 

### Agencement automatique de points droits
  * Correction: Garde la même valeur de tolérance pour les chemins de dessous.

### Trait en Satin
  * Correction: N'échoue plus sur des éléments de broderie mixte
  * Correction macOS: les deux rails ont bien la même orientation.

### Richelieu
  * Ajout de l'information sur les aiguilles dans les fichiers .inf afin que les
[machines Bernina/Bernette machines affichent correctement les numéros d'aiguille](/fr/docs/cutwork/#broderie-richelieu-avec--berninabernette)
  * Correction: Plus d'échec si la forme n'a qu'un remplissage

### Lettrage
  * Ajout d'un [filtre selon la taille de la fonte](/fr/docs/lettering/#options)
  * Ajout de diverses [options pour inclure des commandes de coupe](/fr/docs/lettering/#options) sur toutes les fontes (et non plus uniquement sur les fontes dont les colonnes satin sont autoroutées)
  * Possibilité de dossier de fontes aux fichiers multiples. Dans ce cas, les dossiers sont nommés avec les flèches.
    Ceci permets aux auteurs de partager une fonte et accelerre les documents lourds

  * Correction: plus d'échec sur un glyphe invalide, il est simplement ignoré
  * Correction: plus d'échec, mais ignorer l'autoroutage si l'auteur de la fonte l'a défini sur un remplissage (utile si l'auteur n'a pas fini de convertir tous les glyphes mais veut commencer à tester la nouvelle fonte)

### Simulateur du paramètrage
  * Le simulateur est rechargé plus rapidement lorsque les paramètres sont changés.
  * Le simulateur tient maintenant compte de la *longueur minimum de point*

### Préferences
  * Il est maintenant possible de définir des valeurs par défaut pour la *longueur minimum de point* et la *longueur minimum de saut* 
  * Définition de la taille du cache 

### Impression PDF
  * Nouvelle vue: vue du motif sur une page entiere
  * Présélectionne le format  PDF dans le dialogue de sauvegarde

### Simulateur
  * Utilise la couleur de fond de la page Inkscape
  * Ajout de bouton de zoom (zoomer sur le dessin, zoomer sur la page)

### Plan de broderie
  * Ajout de l' [option de verrouiller le plan de broderie](/fr/docs/visualize/#simulation-du-plan-de-broderie)
(pour le rendre insensible aux interactions)

### Résolution de problèmes
  * Ajout d'options de taille

## Formats de broderie
  * Ajout du nom de fichier dans l'entête de certains formats de fichier
  * Résolution d'un problème ou les commandes de stop résultait en un désaccord entre les couleurs et les blocs de couleur