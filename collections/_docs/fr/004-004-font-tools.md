---
title: "Outils de police"
permalink: /fr/docs/font-tools/
last_modified_at: 2025-04-12
toc: true
---
Un ensemble d'outils adaptés aux créateurs de polices ou à ceux qui souhaitent ajouter des polices supplémentaires dans [l'outil de lettrage](/docs/lettering) d'Ink/Stitch.

Lisez le [Tutoriel de création de police pour Ink/Stitch](/fr/tutorials/font-creation) pour des instructions approfondies.
{: .notice--info }

## Répertoire personnalisé de polices {#custom-font-directory}

Cette extension vous permet de définir un répertoire dans votre système de fichiers dans lequel vous souhaitez stocker les polices supplémentaires pour l'outil de lettrage.

Placez chaque police dans un sous-répertoire de votre répertoire personnalisé de polices. Chaque dossier de polices doit contenir au moins une variante de police et un fichier json.
De plus, il est recommandé d'enregistrer également un fichier de licence. 

Les variantes de police doivent être nommées avec une flèche, indiquant la direction de broderie pour laquelle elles ont été créées (`→.svg`, `←.svg`, etc.). 
Il est aussi possible pour une direction donnée de créer un repertoire dont le nom est la flêche de direction et de répartir les glyphes de cette direction dans plusieurs fichiers dont le nom est alors quelconque.

Le fichier json doit inclure au minimum le nom des polices.

## Editer JSON

{% include upcoming_release.html %}

Cette extension permet d'éditer les informations existantes sur une police.  Si la police n'a pas encore de fichier json, il faut en créer un avec  [generer le fichier JSON](#generate-json)

### Usage

* Lancez `Extensions > Ink/Stitch > Gestion des polices > Editer JSON`
* Choisir une police dans la liste des polices
* Metttre à jour les information tels que le nom, la description, les mots clés ou les information de crénage.
* Cliquez sur `Appliquer`

## Test de police {#font-sampling}

Cette extension crée un calque qui contient toutes les lettres d'une fonte. Elle aide les créateurs de fontes à tester leurs nouvelles fonte.

### Usage

* Lancer  `Extensions > Ink/Stitch > Gestion des polices  > Test de police...`
* Choisir une fonte et ajuster les réglages
* Cliquer sur Appliquer

### Options

* Fonte: choisir la fonte à utiliser
* Direction du texte:  par défaut de gauche à droite
* Échelle:  en pourcentage
* Largeur du texte: des sauts de lignes seront ajoutés pour ne  pas dépasser cette largeur
* Tri des couleurs: choisir si une fonte multicolore est triée ou nonn (la fonte doit utiliser [l'indice de tri des couleurs](#set-color-index))

## Forcer des points d'arrêt {#force-lock-stitches}

Les petites fontes se défont parfois si les fils sont coupés après la broderie. 

Il est donc important que les diacritiques qui sont plus proches du corps de la lettre que la valeur de la longueur minimum de saut définie dans les préférences (3mm par défaut) aient des points d'arrêt. 

Ceci peut être obtenu en leur ajoutant un attribut forcer les points d'arrêt. Il est possible de restreindre cet ajout aux seules colonnes satin.

Pour la même raison, lorsque les lettres sont détachées, il peut être utile de forcer les points d'arrêts sur le dernier élément de chaque glyphe.

### Usage

* Lancer  `Extensions > Ink/Stitch > Gestion des polices  > Forcer des points d'arrêt...`
* Choisir les paramètres en fonction de la fonte
* Cliquer sur appliquer

### Options

* Restreindre au satin

* Ajouter des points d'arrêt forcés par la distance
  * Mininum distance (mm)
  * Maximum distance (mm)

* Ajouter l'attribut "forcer les points d'arrêts" au dernier élément de chaque glyphe

## Générer le fichier JSON {#generate-json}

Cette extension est destinée à vous aider à créer le fichier json.
Selon la façon dont vous avez généré votre fichier de police, il peut permettre d'inclure des informations de crénage supplémentaires dans le fichier json.
Lire [**comment générer une police svg avec des informations de crénage**](/tutorials/font-creation).

Si vous avez généré votre fichier svg sans informations de crénage, cette extension peut quand même vous aider à configurer votre fichier json avec des informations de base.

### Information sur la police

|Options                            |Description        |
|-----------------------------------|-------------------|
|Nom (obligatoire)                  |le nom de votre police (obligatoire).
|Description                        |informations supplémentaires sur votre police (telles que des informations de taille, etc.)
|Fichier de police (obligatoire)    | Si vous avez utilisé FontForge pour générer votre fichier de police svg, Ink/Stitch lira les informations de crénage de votre police pour les inclure dans le fichier json.<br/>De plus, le fichier de police sera utilisé pour déterminer le chemin de sortie.<br/><br/>Un fichier `font.json` sera enregistré dans le dossier de votre fichier de fonte svg.
|Keywords                           |Enable the categories that apply to your font

### Paramètres de la police

|Options                            |Description        |
|-----------------------------------|-------------------|
|Agencement automatique des colonnes Satin|▸ activé<br/>Ink/Stitch générera une organisation raisonnable pour les colonnes de satin de votre police lorsqu'elle est utilisée dans l'outil de lettrage. [Plus d'information sur Agencement automatique des colonnes Satin](/fr/docs/satin-tools/#auto-route-satin-columns)<br/><br/>▸ désactivé<br/>Ink/Stitch utilisera les glyphes tels quels. Désactivez l'option, si vous vous avez créé vous-même l'agencement des colonnes satin dans votre police.
|Réversible                         |si votre police peut être brodée vers l'avant et vers l'arrière ou seulement vers l'avant. Ne cocher cette case que si vous avez effectivement créé plusieurs variantes de la police pour des directions différentes.
|Triable                       |si les couleurs de votre police sont triables. Pour fonctionner, cela necessite que les éléments de votre police portent un  [indice de tri des couleurs ](#set-color-index)
|Combiner des  indices                    |une liste d'indice de tri des couleurs séparés par des virgules. Les élements porteurs d'un de ces indices seront regroupés. Utile pour réduire le nombre de couleurs des polices multicolores comme les polices tartan.
|Forcer la casse                    |▸ Non<br/>choisissez cette option si votre police contient des lettres majuscules et minuscules (par défaut).<br/<<br/>▸ Majuscule: Choisissez cette option si votre police ne contient que des majuscules.<br/><br/>▸ Minuscule: Choisissez cette option si votre police ne contient que des minuscules.
|Glyphe par défaut                  |le glyphe à afficher si le glyphe demandé par l'utilisateur n'est pas disponible dans le fichier de police (glyphe manquant)
|Echelle minimum /Echelle maximum   |Défini dans quelle mesure vos glyphes peuvent être agrandis ou diminués sans perdre en qualité une fois brodés

### Crénage

Les champs suivants sont facultatifs, uniquement nécessaires lorsque votre fichier svg ne contient pas d'informations de crénage.
Si les informations de crénage ne peuvent être trouvées, ces valeurs seront utilisées en remplacement.

|Options                      |Description        |
|-----------------------------|-------------------|
|Forcer des valeurs de crénage| Ne pas utiliser l'information de crénage du fichier svg, mais utiliser plutôt ces valeurs:
|Hauteur de ligne (px)        | Défini la hauteur d'une ligne de votre fonte. Si vous laissez à 0, Ink/Stitch lit la valeur dans votre fichier de fonte svg (si aucune info ne peut être trouvé,  100 est la valeur par défaut).
|Espacement des mots (px)     |La largeur du caractère "espace"

## Lettres vers police {#letters-to-font}

"Lettres vers police" est un outil pour convertir un ensemble de lettres pré-digitalisées en broderie en une police utilisable par l'outil Lettrage d'Ink/Stitch.

La fonte pré-digitalisée doit remplir certaines **conditions** pour être importée:

* A chaque glyphe doit correspondre un fichier dans un format de broderie que Ink/Stitch peut lire
* Le nom du fichier doit terminer par le nom du glyphe. Par exemple un nom de fichier valide pour la majuscule A pourrait être  `A.pes` ou `Example_Font_A.pes`.

Souvent les fontes de broderie achetées sont organisées en sous dossiers car chaque lettre est fournie dans différenst formats de broderie. Vous n'avez pas besoin de modifier la structure des fichiers. "Lettres vers police" cherchera les lettres dans les sous-dossiers.
{: .notice--info }

### Usage

* Choisissez le format de broderie des lettres que vous souhaitez importer (idéalement choisissez un format qui contient les informations de couleurs).
* Choisissez le dossier qui contient les lettres. Si les lettres sont organisées par sous dossiers, choisissez le dossier principal.
* Choisissez si vous souhaitez importez les commandes (coupe par exemple) ou pas (attention :importer les commandes lorsqu'elles sont nombreuses va causer un très fort ralentissement
* Cliquez sur "appliquer" et..... attendre.....
* Après l'importation déplacez la ligne de base à un endroit correct et positionnez les lettres en fonction. La position des lettres par rapport au  bord gauche de la page influence aussi le positionnement des lettres par l'outil de lettrage.
* Sauvegardez votre fonte dans un fichier  `→.svg` dans un nouveau répertoire de votre  [répertoire personnalisé de polices](#custom-font-directory)
* Exécutez  [`Génerer JSON`](#generate-json) pour rendre la police disponible dans l'outil de Lettrage et sauvegarder le fichier json dans le même dossier que votre fonte.  Ne pas cocher  "Agencement automatique de colonnes satin" pour les fontes pré-digitalisées et laisser l'échelle à 1.

## Supprimer les informations de crénage {#remove-kerning}

**⚠ Attention**: Les modifications effectuées par cet outil sont irréversibles. N'oubliez pas de faire **une copie** de votre fichier svg avant d'utiliser cet outil.
{: .notice--warning }

Votre fonte est prête pour l'utilisation. Toutefois lorsque vous avez créé votre fichier de fonte avec Fontforge, il contient beaucoup d'informations qui ne sont plus nécessaires et qui peuvent ralentir légèrement le travail.

Ink/Stitch contient un outil de nettoyage de votre fichier de fonte.

1. Faites une **copie** de votre fonte. Les informations additionnelles ne sont pas utiles pour se servir de la fonte, mais pourront vous être utiles si vous souhaitez ajouter de nouveaux glyphes.
2. Exécutez `Extensions > Ink/Stitch > Gestion des polices > Supprimer les informations de crénage`
3. Sélectionnez votre fichier de fonte
4. Cliquez sur `Appliquer`


## Définir l'indice de tri des couleurs {#set-color-index}

{% include upcoming_release.html %}

Défini un indice qui permet à l'outil de lettrage de savoir où positionner les éléments lorsque tri des couleurs est activé.

* Dans un ficier de police, séléctionner les éléments d'une même couleur
* Lancez `Extensions > Ink/Stitch > Gestion des police > Définir l'indice de tri des couleurs`
* Choisir la valeur de l'indice
* `Appliquer`

Le fichier json doit spécifier que la police est triable. Utilisez  [Editer JSON](#edit-json) and cochez l'option `Triable` dans l'onglet `Paramètres dela font`.
{: .notice--warning }

## Mettre à jour la liste des glyphes  {#update-glyph-list}

Permet d'insérer dans le fichier json la liste des glyphes définis . Cette opération doit être effectuée une première fois, puis chaque fois que la liste des glyphes effectivement programmés est modifiée.
