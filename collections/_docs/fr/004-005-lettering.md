---
title: "Outil lettrage"
permalink: /fr/docs/lettering/
last_modified_at: 2025-03-14
toc: true
---

Le module de lettrage crée du texte sur plusieurs lignes. Choisissez la bonne police pour votre projet dans une grande variété de polices déjà digitalisées.

![Lettrage Extensions](/assets/images/docs/fr/lettering.png)

## Usage

* Faire `Extensions > Ink/Stitch  > Lettrage`
* Entrez votre texte (multi-ligne possible)
* Définir la police et l'échelle
    **⚠ Attention**: Pour des résultats optimaux, tenir compte des limites de redimensionement mentionnées dans le descriptif des fontes.
* Cliquer sur `Appliquer et Quitter`


## Filtres de fonte

* **Filtrage par taille**
  Les fontes sont conçues pour être  brodées dans  un intervalle de tailles donné. Le filtrage par taille vous aide en réduisant la liste des fontes à uniquement les fontes qui peuvent être brodées dans les dimensions choisies.
  Un filtre actif (pas à 0) déterminera  automatiquement la bonne échelle pour que la fonte sélectionnée soit dans la dimension souhaitée.

* **Glyphs**<br>
si l'option est cochée, seules les fontes contenant tous les glyphes de votre texte apparaissent dans le menu déroulant des fontes

* **Famille de fonte**<br>
Filtre les fontes par famille, par exemple les fontes d'appliqué ou les fontes d'écriture manuelle.

## Options

* **Broder les lignes de texte en aller retour**
 Lorsque cette option est activée, la première ligne sera brodée de gauche à droite et la seconde de droite à gauche, etc.
   Cela donnera à votre machine des déplacements plus courts.

* **Ajouter des commandes de coupes**
  Si cette option est activée, Ink/Stitch ajoutera des commandes de coupe  au choix pour chaque lettre, ou après chaque mot ou après chaque ligne.

## Préconfigurations

Vous pouvez enregistrer et rouvrir vos paramètres de police préférés.

## Lettrage le long d'un chemin  {#lettering-along-path}

Les lettres d'ink/stitch ont été soigneusement dessinées pour une broderie optimale. Si vous essayez de les modifier avec les outils usuels d'inkscape, il se peut que cela ne fonctionne pas comme vous le souhaitez. Placez les lettres le long  d'un chemin est un gros travail. Cet outil va vous aider à le faire.

![A text aligned along a path while using the various options](/assets/images/docs/text_along_path_alignment.png)

### Usage

* Sélectionnez un chemin et un groupe de lettrage 
* Exécutez `Extensions > Ink/Stitch > Lettrage le long d'un chemin ...`
* Si `Etendre` est coché Ink/Stitch va étendre les espaces entre les lettres pour que le texte utilise tout le chemin. Sinon il gardera les distances du texte original. 
* Cliquez sur 'Appliquer'

Lettering will follow the path direction. Reverse the path if needed (`Path > Reverse`).
{: .notice--info}

## Bibliothèque de polices

Un aperçu de toutes les polices disponibles se trouve dans la [bibliothèque de polices](/fr/fonts/font-library/).

## Tri des couleurs
Si vous utilisez plusieurs lettres d'une police multicolore, vous pouvez trier les couleurs afin d'éviter de multiples changements de fil. Ce tri ne doit toutefois pas modifier l'ordre des couleurs d'une lettre pour ne pas modifier la broderie. 

Lorsqu'à l'intérieur de chaque lettre les couleurs ne sont utilisées que sur des chemins consécutifs et toujours dans le même ordre (ce qui est le cas des polices multicolores actuellement présentes dans Ink/Stitch, sauf *Abril en Fleur* et peut-être *Infinipicto*), et que toutes les lettres utilisent toutes les couleurs  voici une manière rapide de trier si votre fichier ne contient que le lettrage :

Dans la fenêtre objet, choisir une lettre (peu importe laquelle) :
* Sélectionner le chemin qui sera brodé en premier (le dernier de la lettre dans cette fenêtre donc...)
* Edition/Sélectionner même/Couleur de contour (ceci va sélectionner tout ce qui est de cette couleur dans toutes les lettres, il y a probablement beaucoup de chemins par lettre)
* Grouper : ce groupe va se trouver dans ce qui était la dernière lettre à broder, éventuellement donner à ce groupe le nom de la couleur
* Faites monter ce groupe le plus haut possible dans cette dernière lettre
et recommencer jusqu'a qu'il n'y ait plus que des groupes de couleurs, en partant à chaque fois du dernier chemin d'une lettre

## Créer de nouvelle polices pour Ink/Stitch
Lire le [tutoriel de création de police](/fr/tutorials/font-creation/).

Contactez nous  sur  [GitHub](https://github.com/inkstitch/inkstitch/issues) si vous souhaitez publier votre police dans l'outil de lettrage d'Ink/Stitch.

## Fichiers example concernant  le lettrage

{% include tutorials/tutorial_list key="techniques" value="Lettering" %}
