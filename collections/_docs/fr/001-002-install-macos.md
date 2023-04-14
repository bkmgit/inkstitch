---
title: "Install Ink/Stitch"
permalink: /fr/docs/install-macos/
excerpt: "How to quickly install Ink/Stitch."
last_modified_at: 2022-06-12
toc: true
---
{% comment %}
## Guide vidéo

Nous fournissons aussi aux débutants des tutoriels vidéo sur notre <i class="fab fa-youtube"></i> [chaine YouTube](https://www.youtube.com/c/InkStitch). Les vidéos sont en anglais. Mais il y a des sous-titres en français.

* <i class="fab fa-apple"></i> [macOS](https://www.youtube.com/watch?v=gmOVLNh9cu8&list=PLvlbfDmZyXG1ORmeqHdp4aP7J71e7icJP&index=3)
{% endcomment %}

## Télécharger
Téléchargez la dernière version d'Ink/Stitch pour votre version de macOS :

<p><a href="{{ site.github.releases_url }}/latest/download/inkstitch-{{ site.github.latest_release.tag_name }}-osx.pkg" class="btn btn--info btn--large"><i class="fa fa-download " ></i> Télécharger Ink/Stitch {{ site.github.latest_release.tag_name }} pour macOS<br /><span style="color:lightblue;">Big Sur / Monterey</span></a></p>
<p><a href="{{ site.github.releases_url }}/latest/download/inkstitch-{{ site.github.latest_release.tag_name }}-sierra-capitan-catalina-osx.pkg" class="btn btn--info btn--large"><i class="fa fa-download " ></i> Télécharger Ink/Stitch {{ site.github.latest_release.tag_name }} pour macOS<br /><span style="color:lightblue;">El Capitan / Sierra / High Sierra / Mojave / Catalina</span></a></p>

Mojave - Monterey: Cliquez sur le fichier téléchargé pour lancer l'installateur.

El Capitan - High Sierra: Ctrl+Click  sur le fichier téléchargé et Cliquez sur Ouvrir

Click on Continue.

**Dernière version:** [Ink/Stitch {{ site.github.latest_release.tag_name }} ({{ site.github.latest_release.published_at | date: "%Y-%m-%d" }})](https://github.com/inkstitch/inkstitch/releases/latest)

## Installation

Ink/Stitch est une extension pour Inkscape. Téléchargez et installez  [Inkscape](https://inkscape.org/release/) Version 1.0.2 ou supérieure avant d'installer Ink/Stitch. Vérifiez que vous avez bien **installé et la lancé Inkscape** avant d'installer Ink/Stitch. Sinon l'installation va échouer.<br><br>

Attention, Inkscape 1.2 ne marche pas avec **El Capitan** and **Sierra**.  Si vous utlilisez une de ces versions de macOS, merci d'installer [Inkscape 1.1.2](https://inkscape.org/release/1.1.2/platforms/).
{: .notice--warning .bold--warning }

**Big Sur - Monterey:** Lancez l'installateur en cliquant sur le fichier que vous avez téléchargé.

**El Capitan - Catalina:** `Ctrl+Click` sur le fichier téléchargé et cliquez sur  `ouvrir`.

Cliquez sur `Continuer`.

![Install Ink/Stitch](/assets/images/docs/fr/macos-install/installer01.png)

Cliquez sur `Installer`.

![Install Ink/Stitch](/assets/images/docs/fr/macos-install/installer02.png)

 A l'invitation de saisir votre mot de passe, entrez votre mot de passe utilisateur et cliquez sur `Installer le logiciel`.

![Install Ink/Stitch](/assets/images/docs/fr/macos-install/installer03.png)


Dans certains cas, votre système vous demandera si vous autorisez l'installateur à sauvegarder des fichiers dans votre répertoire utilisateur (home directory). Ink/Stitch doit être installé dans le dossier des extensions d'Inkscape. Répondez donc 'Oui' à la question.
 
{: .notice--info }

Votre installation est maintenant terminée.

![Install Ink/Stitch](/assets/images/docs/fr/macos-install/installer04.png)


A la dernière question :Voulez vous placer le fichier d'installation dans la corbeille?, répondez ce que vous voulez. Ink/Stitch n'en a plus besoin.

![Install Ink/Stitch](/assets/images/docs/fr/macos-install/installer05.png)

## Exécuter Ink/Stitch

Ouvrez Inkscape. Vous trouverez alors Ink/Stitch dans `Extensions > Ink/Stitch`.

![Ink/Stitch menu](/assets/images/docs/fr/macos-install/inkstitch-extensions-menu.png)

## Mise à jour

Quand une nouvelle version d'Ink/Stitch est disponible, téléchargez là et lancez l'installateur comme décrit ci-dessus. Cela supprimera aussi l'ancienne version.
Les installations antérieures à 2.1.0 doivent être supprimées manuellement. Il faut supprimer les fichiers et dossiers inkstitch* du dossier d'extensions.

**Astuce:** Inscrivez-vous aux news pour avoir connaissance des mises à jour d'Ink/Stitch:<br />
 <i class="fas fa-fw fa-rss-square" aria-hidden="true" style="color: #ffb400;"></i> [GitHub Feed on new Releases](https://github.com/inkstitch/inkstitch/releases.atom)<br>
 <i class="fas fa-fw fa-rss-square" aria-hidden="true" style="color: #ffb400;"></i> [Ink/Stitch News](/feed.xml)<br />
{: .notice--info }

<p class="notice--info" style="margin-top: -3.5em !important;">Ou regardez l'intégralité du projet sur GitHub:<br /><iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=inkstitch&repo=inkstitch&type=watch&count=true&v=2" frameborder="0" scrolling="0" width="170px" height="20px"></iframe></p>

## Problème d'installation Ink/Stitch

### 'xxxx' ne peut pas être ouvert, car l'identité du développeur ne peut pas être confirmée

Ceci peut arriver si vous avez installé une version de developpement. Faites `Ctrl+Click` sur le fichier téléchargé et cliquez sur `Ouvrir`.

### Installation fails

We also provide a zip download file which can be extraced in the the user extensions folder (see below: confirm installation path).

For Big Sur and Monterey [dowload ZIP]({{ site.github.releases_url }}/latest/download/inkstitch-{{ site.github.latest_release.tag_name }}-osx.zip)

For older macOS versions [download ZIP]({{ site.github.releases_url }}/latest/download/inkstitch-{{ site.github.latest_release.tag_name }}-capitan-cataline-osx.zip)

### Ink/Stitch ne fonctionne pas!

**M1 processors (Apple Silicon Mac)**

Most common issue is a missing Rosetta installation. To fix the issue run this command in your terminal: `softwareupdate --install-rosetta --agree-to-license`

**Vérifier le chemin d'installation**

Vérifiez que vous avez bien extrait Ink/Stitch dans le bon répertoire. Si votre repertoire "Extensions utilisateur" ne fonctionne pas correctement, vous pouvez aussi essayer d'utiliser le repertoire des extensions d'Inkscape.
Vous pouvez trouver leur localisation sous `Inkscape > Preferences > Systeme`.

**Vérifier la  version**

Merci de vérifier que vous avez bien téléchargé la version d'Ink/Stitch compatible avec votre version macOS ([Download](#download)).

### J'ai installé Ink/Stitch mais le menu est grisé (désactivé)

C'est souvent le cas si une mauvaise version Ink/Stitch a été installée.
Veuillez vérifier si vous avez téléchargé la bonne version Ink/Stitch pour votre système d'exploitation.

### Les fenêtres de dialogue sont affichées en anglais!

Premièrement, il est possible que tous les textes n'aient pas été traduits. Ceci est le cas si **certaines parties sont en anglais et d'autres dans votre langue maternelle**.

Si vous souhaitez terminer la traduction, consultez notre [description pour les traducteurs](/developers/localize/).

Si Ink/Stitch n'est pas sûr de la langue à prendre en charge, il choisira l'anglais.
Vous pouvez indiquer explicitement à Inkscape d'utiliser votre langue maternelle comme suit:
  * Allez à Inkscape > Preferences > Interface (Ctrl + Shift + P)
  * Choisissez votre langue
  * Redémarrez Inkscape

![Preferences > Interface](/assets/images/docs/fr/preferences_language.png)

## Désinstaller Ink/Stitch

Dans Inkscape, allez à  `Inkscape > Préférences > Système` et cherchez dans ce tableau où se trouve votre dossier `Extensions utilisateur`.

![Extensions Utilisateur](/assets/images/docs/fr/extensions-folder-location-macos.jpg)

Supprimez chaque dossier ou fichier inkstitch*.