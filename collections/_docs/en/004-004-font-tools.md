---
title: "Font Tools"
permalink: /docs/font-tools/
last_modified_at: 2024-12-28
toc: true
---
A collection of tools suitable for font creators or those who want to add additional fonts to the Ink/Stitch [lettering tool](/docs/lettering).

Read the [Ink/Stitch font creation tutorial](/tutorials/font-creation) for in-depth instrustions.
{: .notice--info }

## Custom Font Directory

This extension allows you to define a directory in your file system where you want to store additional fonts to be used with the lettering tool.

Place each font in a subdiretory of your custom font directory. Each font folder should contain at least one font variant and one json file.
Additionally it is recommended to save a license file as well.

**Font variants** have to be named with an arrow, indicating the stitch direction it has been created for (`→.svg`, `←.svg`, etc.). It is also possible to create a folder named with an arrow name instead and insert multiple font files for a specific direction.

The json file has to include as a minimum requirement the fonts name.

## Edit JSON

{% include upcoming_release.html %}

This extension allows you do edit an existing font information file. If the font doesn't have a json file file, create one with generated with [generate JSON](#generate-json)

### Usage

* Run `Extensions > Ink/Stitch > Font Management > Edit JSON`
* Finetune your font details such as name, description, keywords and kerning information
* Click on apply

## Font Sampling

This extension creates a list of all letters in a font. It helps font creators to test the outcome of a new font.

Options are :

* Font : the one you want to use
* Stitch direction :  default is left to right
* Scale : in percent
* Max line width : line breaks will  be chosen accordingly

## Force lock stitches

Small fonts will sometimes unravel if threads are cut after the embroidery machine has finished the work.

Therefore it is important that also diacritics with a smaller distance to the font body than defined by the minimum jump stitch length (default: 3mm) have lock stitches.

This extension helps adding forced lock stitches. One may chose to restrict the addition of lock stitches only to satin columnns.

### Usage

* Run `Extensions > Ink/Stitch > Font Management > Force lock stitches...`
* Update settings according to the font
* Click on apply

### Options

* Mininum distance (mm)
* Maximum distance (mm)
* Restrict to satin
* Add force lock stitches attribute to the last element of each glyph

## Generate JSON

This extension was created to help you to create the json file.
Depending on the way you generated your font file it can include additional kerning information into the json file.
Read [**how to generate a svg font with kerning information**](/tutorials/font-creation).
If you generated your svg file without kerning information this extension can still help you to set up your json file with basic information.

### Font Info

|Option                 |Description|
|-----------------------|-------------------------------------|
|Name (mandatory)       |The name of your font 
|Description            |Additional information about your font
|Font File (mandatory)  |When you have been using FontForge to generate your svg font file, Ink/Stitch will read the kerning information from your font to include it into the json file.<br />Additionally the font file will be used to determine the output path.<br/><br/>A file `font.json` will be saved into the folder of your svg font file.
|Keywords               |Enable the categories that apply to your font

### Font Settings

|Option                 |Description|
|-----------------------|-------------------------------------|
|Default Glyph          |the glyph to be shown if the user requested glyph isn't available in the font file (missing glyph)
|AutoRoute Satin        |▸ Enabled<br/>Ink/Stitch will generate a reasonable [routing for satin columns](/docs/satin-tools/#auto-route-satin-columns) in your font when used in the lettering tool.<br/><br/>▸ Disabled<br/>Ink/Stitch will use the glyphs as is. Disable this option, if you took care for the routing in your font by yourself.
|Reversible             |wether your font can be stitch forwards and backwards or only forwards. Check this only if you do have created font variants.
|Sortable               |wether your font can be color sorted or not. This only works, when the elements in your font carry a [color sort index](#set-color-index)
|Combine indices        |a comma separated list of of color sort indices. Elements with this index will be combined into a single element. Useful to reduce color changes for multi-color stitch types such as tartan.
|Force letter case      |▸ No<br/>Choose this option if your font contains upper and lower case letters (default).<br/><br/>▸ Upper<br/>Choose this option if your font only contains upper case letters.<br/><br/>▸ Lower<br/>Choose this option if your font only contains lower case letters.
|Min Scale / Max Scale  |Define how much can your glyphs can be scaled without loosing quality when stitched out


### Kerning

The following fields are optional only necessary, when your svg file doesn't contain kerning information.

If the kerning information cannot be found, these values will be used instead.

|Option                 |Description|
|-----------------------|-------------------------------------|
|Force defined values   |Do not use the font file information, but the values defined below.
|Leading (px)           |Defines the line height of your font. Leave to `0` to let Ink/Stitch read it from your font file (defaults to 100 if the information cannot be found).
|Word spacing (px)      |The width of the "space" character


## Letters to font

"Letters to font" is a tool to convert predigitized embroidery letters into a font for use with the Ink/Stitch lettering tool.

The digitized font needs to meet certain **conditions** to be imported:
* One file for each glyph in an embroidery format that Ink/Stitch can read
* The glyph name needs to be positioned at the end of the file name. A valid file name for the capital A would be e.g. `A.pes` or `Example_Font_A.pes`.

You will often see, that bought fonts are organized in subfolders, because each letter comes in various embroidery file formats. You don't need to change the file structure in this case. Letters to font will search the font files also within the subfolders.
{: .notice--info }

### Usage

* Set the embroidery file format from which you want to import the letters (ideally choose a file format which is capable to store color information)
* Select the font folder in which the letters are stored. If they are organiszed in subfolders, choose the main folder.
* Choose wether you want to import commands or not (warning: imported commands on a large scale will cause a slow down)
* Click on apply - and wait ...
* After the import move the baseline to the correct place and position the letters accordingly. The left border of the canvas will also influence the positioning of the letters through the lettering tool.
* Save your font as `→.svg` in a new folder within your [custom font directory](#custom-font-directory)
* Run [`Generate JSON`](#generate-json) to make the font available for the lettering tool and save the json file into the same folder as your font. Do not check "AutoRoute Satin" for predigitized fonts and leave scaling to 1.

## Remove Kerning

**⚠ Warning**: Changes made by this tool cannot be reverted. Make sure to save a **copy** of your file before performing these steps.
{: .notice--warning }

Your font is ready to be used. But when you created your font with FontForge it now contains a lot information which isn't necessary for your font to work and could possibly slow it down a little.
Ink/Stitch comes with a tool to clean up your svg font.

1. Make sure you save a **copy** of your font. The additional information may not be necessary for the font to be used, but it can become handy when you want to add additional glyphs.
2. Run `Extensions > Ink/Stitch > Font Tools > Remove Kerning`
3. Choose your font file(s)
4. Click on apply

## Set color index

{% include upcoming_release.html %}

Sets an index to inform the lettering tool on where to position the selected elements when color sorting is enabled.

* In a font file select elements of the same color
* Open the extension `Extensions > Ink/Stitch > Font Management > Set color index`
* Set the index number
* Apply

The JSON-file must specify if a font is color sortable. Use [Edit JSON](#edit-json) and enable the option `Sortable` in the `Font Settings` tab.
{: .notice--warning }

## Update glyph list

This extension insert the list of the glyphs into the json file. Must be done a first time when all the glyphs are present in the  svg file, and must be redone if glyphs are added or deleted.
