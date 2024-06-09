---
title: "Outils Satin"
permalink: /fr/docs/satin-tools/
last_modified_at: 2024-05-05
toc: true
---
`Extensions > Ink/Stitch  > Outils :  Satin` inclut un certain nombre d’aides utiles, facilitant le travail avec [les colonnes satin](/fr/docs/stitches/satin-column/).

**Exemple:**
* Créer un chemin à l'aide de l'outil courbes de Bézier (`B`)
* Faire [Ligne en Satin](#ligne-en-satin)
* Utiliser le [Dialogue de Paramètres ](/fr/docs/params/#paramètres-satin) pour choisir une sous-couche
* Lancer [Agencement automatique des colonnes satin](#agencement-automatique-de-colonnes-satin) pour obtenir des colonnes de satin bien organisées

[![Convertir Ligne en Satin](/assets/images/docs/en/satin-tools.svg)](/assets/images/docs/en/satin-tools.svg){: title="Télécharger le fichier SVG" download="satin-tools.svg" }

**Astuce** Pour un accès plus rapide [activer les raccourcis](/fr/docs/customize/) des outils satin spécifiques.
{: .notice--info}


## Agencement automatique de Colonnes Satin {#auto-route-satin-columns}

Cet outil remplacera vos colonnes satin par un nouvel ensemble de colonnes satin dans un ordre d'assemblage logique. Des sous-chemins et les sauts de points seront ajoutés si nécessaire et les colonnes seront scindées pour faciliter les sauts. Les points satins résultants conserveront tous les paramètres que vous avez définis sur les points satins originaux, y compris la sous-couche, l’espacement en zigzag, etc.

### Usage

1. Sélectionnez les colonnes satin (préparées avec sous-couche, etc.)
2. Lancer `Extensions > Ink/Stitch  > Outils de Satin > Agencement automatique de Colonnes Satin...`
3. Activer les options souhaitées et cliquez sur Appliquer

**Astuce:** Par défaut, le point à l'extrême gauche sera choisi comme départ et celui à l'extrême droite comme fin (même s'ils se trouvent à mi-chemin dans un satin, tel que le bord gauche de la lettre "o"). Vous pouvez le remplacer en activant les [commandes de "Position de départ/fin pour l'agencement automatique de colonnes satin "](/fr/docs/commands/).
{: .notice--info }

### Options

* Activer **Couper les sauts de fil** pour couper les fils au lieu de créer des sauts de fil. Tout saut de fil au-dessus de 1mm est coupé. Les commandes de coupe sont ajoutées au SVG, vous pouvez donc les modifier / supprimer à votre guise.

* Si vous préférez conserver votre ordre initial (ce qui pourrait être le cas si vous avez superposé des satins), activez l'option ** **Préserver l'ordre des colonnes satin**.


## Intervertir les rails des colonnes satin

C'est un petit outil pour vous aider à planifier votre chemin de points avec précision: par exemple, retourner les colonnes satin pour raccourcir les connexions entre deux sections.

Une colonne satin qui commence à l'origine sur le rail de gauche et se termine à droite commence sur le rail de droite et se termine à gauche.
![Retourner la colonne satin](/assets/images/docs/en/flip-satin-column.jpg)

Il est aussi possible de faire la même opération à partir du paramètrage.

### Usage

* Sélectionnez une ou plusieurs colonnes satin
* Lancez `Extensions > Ink/Stitch  > Outils Satin > Intervertir les rails satin`

## "Ligne  Zigzag" en Satin {#zigzag-line-to-satin}

Quand vous tracez manuellement une colonne satin, cet outil vous aidera à le faire en une seule étape : au lieu de dessiner d'abord deux rails puis des traverses, cet outil vous permet de dessiner une ligne en zigzag ( ou en dents de scie, ou en carrés) qui pourra ensuite être convertie en colonne satin normale.

### Usage

* Dessinez votre forme avec votre style de zigzag préféré.
* Sélectionnez la forme et lancez  `Extensions > Ink/Stitch > Outis: Satin > "Ligne  Zigzag" en Satin`
  * Sélectionnez votre style de zigzag 
  * Choisissez si votre chemin doit être adouci ou constitué de segments de droites
  * Choisissez si les traverses doivent être inserrées ou non. Les colonnes satin créées auront toujours autant de noeuds sur les deux rails.

### Style de zigzag

* Toutes les lignes de zigzag commencent et se terminent par une traverse.
* Pour **Carré (1)** et **dents de scie (2)** dessinez les traverses les unes après les autres.
*  **zigzag (3)** crée des traverses de chaque pic d'un rail vers le milieu d'un pic sur l'autre rail.
![Styles de zigzags](/assets/images/docs/zigzag-line-to-satin.png)

Si vous voyez quelque chose comme le dessin ci-dessous, vous avez probablement choisi le mauvais style de zigzag pour votre dessin.
![Mauvais choix de style de zigzag](/assets/images/docs/zigzag-line-to-satin-wrong-pattern.png)


## Satin Multicolore {#multicolor-satin}

Cette extension crée des copies des satins  sélectionnés pour imiter une colone satin multicolore.
![Multicolor Satin](/assets/images/tutorials/multicolor_satin/solution.png)

Vous pouvez  lire [ceci](/fr/tutorials/multicolor_satin.md), si vous souhaitez comprendre comment cette extension fonctionne.

### Usage

* Sélectionnez  une ou plusieurs colonnes satin
* `Extensions > Ink/Stitch > Outils: Satin > Satin Multicolore`
* Set the desired options dans l'onglet `Colorer`
* Click on `Apply`

## Options

* Choisir si les couleurs sont équidistantes ou si elles ont des largeurs différentes.

  If checked the color width and margins are defined for all colors by the `monochrome color width` value.

  Si la case est décochée il devient possible de choisir individuellement la largeur de chaque couleur **ET** d'ajouter une zone où deux couleurs se mélangent.
* Ajouter un  dépassement à gauche  (en pourcentage)

  Adds a jagged edge to the left side of the satin
* Ajouter un dépassement à droite (en pourcentage)

  Adds a jagged edge to the right side of the satin
* Ajouter des couleurs

  Width values are given in percentages. Make sure all numbers for all colors add up to 100%.

  Please note that the first input field in each color definition sets the width of the area with only one color. The second input box defines the margin to the next color. This is the width of the area with the "color transition". When `equidistant colors` colors is checked, reduce the value for `monochrome color width` to receive a wider field of bicolor sections.
  {: .notice--info}

  ![Multicolor satin ui](/assets/images/docs/en/multicolor_satin_ui_01.png)

  ![Multicolor satin ui](/assets/images/docs/en/multicolor_satin_ui_02.png)


## Scinder une colonne Satin

Scinder une colonne Satin à un point précis. La coupure a lieu à la limite d'un point pour que les deux satins résultants soient cousus exactement comme l'original. Tous les paramètres définis sur le satin d'origine restent sur les deux nouveaux satins et toutes les traverses sont conservées. Si l'un des satins n'a plus de traverse, de nouvelles sont ajoutées.

### Usage

1. Sélectionnez une colonne satin (le satin simple ne fonctionne pas)
2. Ajouter la commande "Point de partage..." avec `Extensions > Ink/Stitch  > Commandes > Attacher des Commandes à un objet sélectionné`.
3. Déplacez le symbole (ou simplement l'extrémité de la ligne de connexion) pour pointer sur l'endroit exact où vous souhaitez diviser le satin.
4. Sélectionnez à nouveau la colonne satin.
5. Faire `Extensions > Ink/Stitch  > Outils de Satin > Scinder colonne Satin`.
6. La commande de point de partage et la ligne de connexion disparaissent et il semble que rien ne s'être passé. Sélectionnez votre satin et vous verrez qu'il a été divisé.


## Trait en Effet de Chemin Satin {#stroke-to-live-path-effect-satin}

Converti une ligne en colonne satin, en utilisant un Effet de Chemin. Cela rend le satin plus adaptable en forme et en largeur qu'une conversion en colonne satin normale. La ligne reste une ligne, mais un effet de chemin lui est appliqué. Si vous utilisez l'éditeur de noeud, vous pourrez agir sur les noeuds de la ligne, même après application de l'effet.

### Usage

1. Sélectionner une ligne ou un Effect de Chemin Satin
2. Lancez `Extensions > Ink/Stitch > Outils: Satin > Trait en Effet de Chemin Satin...`
3. Choisir les paramètres qui vous conviennent
5. Cliquez sur Appliquer

## Options

--|--|--
Motif                  | ![LPE-Patterns](/assets/images/docs/lpe_patterns.png) | Choix du motif à appliquer repétivement à la colonne satin
Largeur minimum (mm)   | ![Min width](/assets/images/docs/lpe_min_width.png)   | Largeur du motif là où il est le plus étroit
Largeur maximum (mm)   | ![Max width](/assets/images/docs/lpe_max_width.png)   | Largeur du motif là où il est le plus large
Longueur du motif (mm) | ![Length](/assets/images/docs/lpe_length.png)         | Longueur du motif à répeter
Étiré                  | ![Stretched](/assets/images/docs/lpe_stretched.png)   | Si coché le motif sera étiré pour que ses répétitions de motif occupent exactement la longueur de la ligne, sinon, il pourra rester un vide en fin de ligne
Ajouter des traverses  | ![Rungs](/assets/images/docs/lpe_rungs.png)           | Les motifs ayant tous le même nombre de noeuds sur les deux rails, les traverses sont facultatives. Choisissez d'en ajouter ou non
Chemin privé           |                                                       | Si coché, la colone satin dispose de son propre motif. Une modification du modif n'influence que cette colonne. Sinon, le motif est commun à toutes les colonnes satin utilisant cet effet et ce motif. Modifier le motif pour l'une d'elle le modifie pour toutes.

### Appliquer l'effet de chemin

Utilisez `Chemin > Objet en chemin` pour convertir en colonne satin standard. 

### Modifier ou changer le motif

Vous pouvez changer le motif de plusieurs manières :

* Modifier le chemin comme n'importe quel chemin à l'aide de l'outil noeud.
* Modifier le motif en ouvrant le dialogue de l'effet de chemin (via `Chemin > Effets de Chemin`):
  * Modifier la largeur du satin via le réglage "Largeur"
  * Modifier le motif en cliquant sur `Modifier sur la zone de travail` dans `Source du motif`.
    
    ![Modifier sur la zone de travail](/assets/images/tutorials/pattern-along-path/edit_french.png)
* Changer de motif en relançant à nouveau `Convertir Ligne en Effet de Chemin Satin`.
* Convertir en chemin normal  (`Shift + Ctrl + C`)  et raffiner manuellement le chemin (ceci perdra la fonctionnalité Effet de Chemin)


## Trait en Satin

Cette extension convertira un trait en une (ou plusieurs) colonne satin avec une largeur spécifiée. Après la conversion, vous verrez les deux rails et (éventuellement) de nombreuses traverses de direction, en fonction de la forme de votre ligne.

### Usage

1. Tracer une courbe de Bézier (`B`)
2. Définir une largeur de trait
2. Lancer `Extensions > Ink/Stitch  > Outils: Satin > Trait en Satin`


## Tutoriaux utilisant Outils: Satin

{% include tutorials/tutorial_list key="tool" value="Satin" %}
