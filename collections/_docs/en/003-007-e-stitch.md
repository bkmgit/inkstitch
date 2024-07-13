---
title: "E-Stitch"
permalink: /docs/stitches/e-stitch/
last_modified_at: 2024-04-30
toc: true
---
## What it is

[![E-Stitch Dolphin](/assets/images/docs/e-stitch-example.jpg){: width="200x"}](/assets/images/docs/e-stitch.svg){: title="Download SVG File" .align-left download="e-stitch.svg" }

It's biggest purpose is for a simple (and yet deceivingly strong) cover stitch for applique items. Mainly for baby cloths as their skin tends to be more sensitive.

![E-Stitch Detail](/assets/images/docs/e-stitch-detail.jpg)

## How to Create

Prepare your path exactly as you would with a [Satin Column](/docs/stitches/satin-column). But in Params enable `"E" stitch`. Don't forget to enlarge the zig-zag spacing for this stitch type.

![Params Satin Column.jpg](/assets/images/docs/en/params-e-stitch.jpg)

**Tip:** If the points are facing into the wrong direction, just use the ["flip satin column rails"](/docs/satin-tools/#flip-satin-column-rails) extension. Or enable the `Swap rails` option in te params dialog.
{: .notice--info }

## Params

Settings||Description
---|---|---
Custom satin column   | ☑ |Must be enabled for these settings to take effect.
Method                | |Chose `E-Stitch`
Short stitch inset    | ![Short Stitch example](/assets/images/docs/params-satin-short_stitch_inset.png) | Stitches in areas with high density will be inset by this amount (%)
Short stitch distance | ![Short Stitch example](/assets/images/docs/params-satin-short_stitch_distance.png) | Inset stitches if the distance between stitches is smaller than this (mm).
Zig-Zag spacing       |![Zig-zag spacing example](/assets/images/docs/params-satin-zig-zag-spacing.png)|the peak-to-peak distance between zig-zags
Pull compensation percentage |![Pull compensation example](/assets/images/docs/params-satin-pull_compensation.png)|Additional pull compensation which varies as a percentage of stitch width. Two values separated by a space may be used for an aysmmetric effect.
Pull compensation     |![Pull compensation example](/assets/images/docs/params-satin-pull_compensation.png)|Satin stitches [pull the fabric together](/tutorials/push-pull-compensation/), resulting in a column narrower than you draw in Inkscape. This setting expands each pair of needle penetrations outward from the center of the satin column by a fixed length. Two values separated by a space may be used for an aysmmetric effect.
Reverse rails         |![Reverse Rung](/assets/images/docs/satin-reverse-rung.png) | Enabling this may help if your satin renders very strangely. <br />Options are :<br /> ◦ Automatic, the default value aims to detect and fix the problem <br />◦ Don't reverse , disable automatic detection <br />◦ Reverse first rail <br />◦ Reverse second rail <br />◦ Reverse both rails
Swap rails            |☑ | Swaps the first and the second rails of a satin column. Affecting which side the thread finishes on as well as any other sided property.
Minimum stitch length         ||Overwrite global minimum stitch length setting. Shorter stitches than that will be removed.
Minimum  jump stitch  length             ||Overwrite global minimum jump stitch length setting. Shorter distances to the next object will have no lock stitches
Allow lock stitches   |☑ |Enables lock stitches in only desired positions
Force lock stitches   |☑ | Sew lock stitches after sewing this element, even if the distance to the next object is smaller than defined in the collapse length value value in the Ink/Stitch prefreneces.
Tack stitch           | |Chose your [favorite style](/docs/stitches/lock-stitches/)
Lock stitch           | |Chose your [favorite style](/docs/stitches/lock-stitches/)
Stop After            |☑ | Stop the machine after sewing this object. Before stopping it will jump to the stop position (frame out) if defined.
Trim After            |☑ | Trim the thread after sewing this object.


Random percentage of satin width increase |![Random width increase](/assets/images/docs/params-satin-random-width-increase.png)| Lengthen stitch across rails at most this percent. Two values separated by a space may be used for an asymetric effect.
Random percentage of satin width decrease |![Random width decrease](/assets/images/docs/params-satin-random-width-decrease.png)| Shorten stitch across rails at most this percent. Two values separated by a space may be used for an aysmmetric effect.
Random zig-zag spacing percentage         |![Random zigzag spacing](/assets/images/docs/params-satin-random-zigzag-spacing.png)|Amount of random jitter added to zigzag spacing
Split Method |![default](/assets/images/docs/param_split_satin_default.png) ![simple](/assets/images/docs/param_split_satin_simple.png) ![stager](/assets/images/docs/param_split_satin_stagered.png) | Options:<br /> ◦ default  <br />◦ Simple <br />◦ Staggered
Maximum stitch length | ![Maximum stitch length](/assets/images/docs/params-satin-maximum_stitch_length.png) | Stitches wider than this will be split up (split stitches).
Random Jitter for split stitches          |![Random split stitch jitter](/assets/images/docs/params-satin-random-split-stitch-jitter.png)| Randomizes split stitch length if random phase is enabled, stitch position if disabled.
Random Phase for split stitches           |☑ | Controls whether split stitches are centered or with a random phase (which may increase stitch count).
Stagger this many times before repeating|![Stagger example](/assets/images/docs/params-fill-stagger.png) |Stitches are staggered so that neighboring rows of stitches don't all fall in the same column (which would create a distracting valley effect). Setting this dictates the length of the cycle by which successive stitch rows are staggered. Fractional values are allowed and can have less visible diagonals than integer values. **Active only when split method is staggered**
Minimum length for random-phase split     |  | Defaults to maximum stitch length. Smaller values allow for a transition between single-stitch and split-stitch.
Random seed           | | Use a specific seed to compute stitch plan. If empty, the seed is the element ID . Re-roll if you are not happy with the result.



For the underlay params have a look at the [satin stitch params](/docs/stitches/satin-column/#params).

## Sample Files Including E-Stitch

{% include tutorials/tutorial_list key="stitch-type" value="E-Stitch" %}

