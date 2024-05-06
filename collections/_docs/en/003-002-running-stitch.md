---
title: "Running Stitch"
permalink: /docs/stitches/running-stitch/
last_modified_at: 2024-05-06
toc: true
---
## What it is

[![Running Stitch Butterfly](/assets/images/docs/running-stitch.jpg){: width="200x"}](/assets/images/docs/running-stitch.svg){: title="Download SVG File" .align-left download="running-stitch.svg" }

Running stitch produces a series of small stitches following a line or curve.

![Running Stitch Detail](/assets/images/docs/running-stitch-detail.jpg)

## How to Create

Running stitch is created by a path with a stroke color.

The stitch direction can be influenced by the [path direction](/docs/customize/#enabling-path-outlines--direction). If you want to swap the starting and ending point of your running stitch run `Path > Reverse`.

If an object consists of multiple paths, they will be stitched in order with a jump between each.

## Params

Open `Extensions > Ink/Stitch  > Params` to change parameters to your needs.

Settings|Description
---|---
Running stitch along paths    |Must be enabled for these settings to take effect.
Method                        |Choose `Running stitch / Bean stitch` for the running stitch type
Repeats                       |◦ Defines how many times to run down and back along the path<br />◦ Default: 1 (traveling once from the start to the end of the path)<br />◦ Odd number: stitches will end at the end of the path<br />◦ Even number: stitching will return to the start of the path
Bean stitch number of repeats |◦ Enable [Bean Stitch Mode](/docs/stitches/bean-stitch/)<br />◦ Backtrack each stitch this many times.<br />◦ A value of 1 would triple each stitch (forward, back, forward).<br />◦ A value of 2 would quintuple each stitch, etc.
Running stitch length         |Length of stitches
Running stitch tolerance      |All stitches must be within this distance from a path. A lower tolerance means stitches will be closer together. A higher tolerance means sharp corner may be rounded.
Randomize stitches  |Randomize stitch length and phase instead of dividing evenly or staggering. This is recommended for closely-spaced curved fills to avoid Moiré artefacts.
Random stitch length jitter|Amount to vary the length of each stitch by when randomizing.
Random Seed|Rolling the dice or setting a new value will change the random stitches
Minimum stitch length         |Overwrites global minimum stitch length setting. Shorter stitches than that will be removed.
Minimum  jump stitch  length  |Overwrites global minimum jump stitch length setting. Shorter distances to the next object will have no lock stitches.
Allow lock stitches           |Enables lock stitches in only desired positions
Force lock stitches           |Sew lock stitches after sewing this element, even if the distance to the next object is smaller than defined in the collapse length value value in the Ink/Stitch preferences.
Tack stitch                   |Chose your [favorite style](/docs/stitches/lock-stitches/)
Lock stitch                   |Chose your [favorite style](/docs/stitches/lock-stitches/)
Trim After                    |Trim the thread after sewing this object.
Stop After                    |Stop the machine after sewing this object. Before stopping it will jump to the stop position (frame out) if defined.

## Routing

For a better stitch routing try the extension `Autoroute Running Stitch` in the [stroke tools](/docs/stroke-tools/).

## Patterned Running Stitch

Read the [tutorial](/tutorials/patterned-unning-stitch/) how to easily create a patterned running stitch.

![patterned running stitch](/assets/images/tutorials/pattern-along-path/copy-paste.png)

## Sample Files Including Running Stitch

{% include tutorials/tutorial_list key="stitch-type" value="Running Stitch" %}
