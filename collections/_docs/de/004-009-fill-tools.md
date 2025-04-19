---
title: Füllstich Werkzeuge
permalink: /de/docs/fill-tools/
last_modified_at: 2025-03-19
toc: true
---
## Füllstich-Objekte zerlegen

Füllstich Objekte sollten aus Objekten bestehen, deren Randlinien sich nicht kreuzen. Manchmal ist es wirklich nicht einfach, diese Regel zu erfüllen, denn oft entstehen winzige Schleifen, die man in Inkscape gar nicht sehen kann. Aus diesem Grund können Füllstiche oft ärgerliche Fehlermeldungen hervorrufen.

Diese Erweiterung soll dir helfen, kaputte Objekte zu repaireren. Nutze diese Funktion einfach für alle Füllstich-Bereiche die eine Fehlermeldung ausgeben. Sie wird kleine Schleifen entfernen und wenn nötig, deine Form in kleinere Unterabschnitte unterteilen.

### Funktionsweise

* Wähle ein oder mehrere Füllobjekte aus
* Öffne das Dialogfenster unter `Erweiterungen > Ink/Stitch  > Füllstich Werkzeuge  > Füllstich-Objekte zerlegen`

## Einfach oder Komplex

* *Einfach* kann mit Löchern, unverbundenen Objekten und sich überkreuzenden Rändern arbeiten. Kombinierte Pfade werden in einzelne Pfade zerlegt.

* *Komplex* agiert genauso wie "einfach", kann aber zusätzlich mit Objekten mit mehreren sich überschneidenden Pfaden umgehen.

![Break apart fill objects](/assets/images/docs/en/break_apart.jpg)
[Download SVG](/assets/images/docs/en/break_apart.svg)

## Farbverlauf in Blöcke aufteilen

Diese Erweiterung teilt ein Füllobjekt mit einem linearen Farbverlauf in mehrere einfarbige Blöcke auf und setzt den zuvor bestimmten Wert für `Reihenabstand Ende`.

### Anwendung

1. Setze einen linearen Farbverlauf

   ![linear gradient](/assets/images/docs/en/linear-gradient.png)
2. `Erweiterungen > Ink/Stitch > Werkzeuge: Füllung > Farbverlauf in Blöcke aufteilen...`

   ![color blocks](/assets/images/docs/color_blocks.png)
3. Setze einen Wert für den Reihenabstand am Ende der Füllung. Bei einem Wert von 0.00 wird der doppelte Wert des ursprünglichen Reihenabstandes angenommen.

## Knockdown Füllung

{% include upcoming_release.html %}

Hilfsmethode zum Erzeugen eines Füllbereichs unterhalb aller ausgewählten Elemente, optional mit einem Versatz. Dies kann bei der Arbeit mit hochflorigen Stoffen sehr nützlich sein.

![Eine Figure mit einem sie umgebenden Knockdown-Stich](/assets/images/docs/knockdown.png)

* Elemente auswählen
* `Erweiterungen > Ink/Stitch > Werkzeuge: Füllung > Auswahl zu Knockdown-Stich`
* Einstellungen anpassen
* Auf `Anwenden` klicken
* Füllparameter im Parameterdialog anpassen (`Erweiterungen > Ink/Stitch > Parameter`)

  Wenn du die gleiche Struktur behalten willst, das Muster aber skalieren möchtest,
  aktualisiere den Reihenabstand für die Deckschicht, als auch für die Unterlage und berechne die maximale Stichlänge: `spacing / sin(60)`<br><br>
  **Beispiel**: Wenn der Reihenabstand 1.8 mm beträgt, ist die maximale Stichlänge `1.8 / sin(60) ≈ 2.08`
  {: .notice--info }

### Einstellungen

* Löcher erhalten: bestimmt ob die neue Füllfläche Löcher enthält
* Versatz: der Versatz (mm) um die Auswahl
* Methode (rund, Gehrung, Abschrägung): Beeinflusst das Ergebnis um die Ecken herum
* Gehrungslimit: Beeinflusst das Ergebnis um die Ecken herum

## Tartan

Der Farbeditor ist unter `Erweiterungen > Ink/Stitch > Werkzeuge: Füllung > Tartan` zu finden.

![Ein Seepferdchen mit einem Tartan-Muster](/assets/images/docs/de/tartan_stripe_editor.png)

### Muster anpassen

#### Position

Das Muster kann als Ganzes rotiert, skaliert (%) und verschoben (mm) werden.

#### Muster Einstellungen

* Symmetrie: Muster können gespiegelt (symmetrisch) oder wiederholt (asymmetrisch) werden.
  * Ein gespiegeltes Muster kehrt die Farbreihenfolge in jeder zweiten Iteration um (ohne den äußeren Streifen, den Drehpunkt, zu wiederholen)
    Dies würde ein Muster mit drei Farben (grün, schwarz, gelb) wie folgt ausgeben: grün, schwarz, gelb, schwarz, grün, schwarz, gelb, ...
  * Ein wiederholtes Muster wird das gesamte Muster einfach immer wieder wiederholen: grün, schwarz, gelb, grün, schwarz, gelb, grün, ...
* Gleiche Farbkombination für Kette und Schuss
  * Ist diese Funktion deaktiviert, können für Kette und Schuss jeweils unterschiedliche Farben festgelegt werden
  * Ist diese Funktion deaktiviert, folgen Kette und Schuss der gleichen Farbkombination

#### Streifen

* Farben können über die Schaltfläche `Hinzufügen` hinzugefügt werden
* Hinter jedem Farbstreifen befindet sich ein `X` mit dem Farben gelöscht werden können
* Die Streifenpositionen kann durch Klicken und Ziehen auf der Schaltfläche `⁝` geändert werden (mit Vorsicht verwenden).
* Soll eine Farbe nur als Platzhalter dienen, kann die Ausgabe als Stickpfad über das Kontrollkästchen deaktiviert werden (☑)
* Soll Kette und Schuss nicht gleich sein, so werden die Farben für die Kettfäden vertikal und für Schussfäden horiztonal ausgegeben
* Über das Farbfeld kann die Farbe des jeweiligen Streifens geändert werden
* Gleiche Farben können gleichzeitig geändert werden, wenn das Kontrollkästchen `Farben verlinken` aktiviert ist

### Palettencode

Der Ink/Stitch Code ist die Information die in die SVG-Datei eingespeichert wird. Hierüber können alle Parameter des Tartanmusters direkt angepasst werden.

Ein Palettencode sieht beispielsweise so aus: `(#000000)/5.0 (#FFFFFF)/?5.0`. 

* Streifen sind durch Leerzeichen getrennt
* Jede Farbdefinition ist in runde Klammern eingeschlossen `(#000000)`
* Ein Schrägstrich (`/`) definiert das Muster als symmetrisch (gespiegelt), während drei Punkte (`...`) ein sich wiederholendes (asymmetrisches) Muster repräsentieren `...(#000000)5.0 (#FFFFFF)?5.0...`.
* Ein senkrechter Strich (`|`) trennt Kette von Schuss und wird nur dann eingesetzt wenn diese nicht gleich sind.

**Hinweis**: Das [Scottish Register of Tartans](https://www.tartanregister.gov.uk/) hatte eine große Sammlung and registrierten Tartan-Mustern. Ink/Stitch ist fähig den Code den man sich per Mail zuschicken lassen kann in Ink/Stitch Palettencode umzusetzen. Bitte beachtet dabei die entsprechenden Lizenz-Regulierungen. 

The [Scottish Register of Tartans](https://www.tartanregister.gov.uk/) has a huge collection of registered tartan patterns. Ink/Stitch is capable to use their code which they send out per mail and convert it into the Ink/Stitch color code. Please respect their particular license regulations. Definiere die Breite eines Tartanfadens, bevor du auf „Code anwenden“ klickst.<br><br>Hier ist ein Beispiel zum Ausprobieren: `...B24 W4 B24 R2 K24 G24 W2...` ([Quelle](https://www.tartanregister.gov.uk/threadcount))
{: .notice--info}

### Stickeinstellungen

In den Stickeinstellungen kann festgelegt werden, ob das Tartanmuster als ein einziges Stickelement ausgegeben werden soll oder ob es in SVG-Elemente umgewandelt wird, die im Anschluss einzelnd bearbeitet werden können.

#### Füllstich-Element

Tartan als Stickelement führt zu einem einheitlichen Erscheinungsbild mit optimaler Stichplatzierung. Es können verschiedene Parameter eingestellt werden, die im Anschluss im Parameterdialog verfeinert werden können.

Die Parameter sind auf der Seite für die [Tartanfüllung](/de/docs/stitches/tartan-fill/) genauer beschrieben.

Der einzige Parameter der nur über dieses Menu eingestellt werden kann ist `Minimale Streifenbreite für Füllstich`. Streifen die schmaler sind als dieser Wert werden als Geradstich ausgegeben.

#### SVG Elemente

* Definiere die Stichart (veraltete Füllung oder Füllstich) und setzte die Parameter den persönlichen Vorlieben entsprechend. Streifen die schmaler sind als `Minimale Streifenbreite für Füllstich` werden als Geradstich ausgegeben. Die einzelnen Elemente können nach einem Klick auf `Anwenden` in Inkscape bearbeitet werden.

**Hinweis**: Für Füllstich-Elemente wird der Stickpfad nach dem Anwenden etwas optimiert und nicht so viele Sprungstiche enthalten wie in der Tartan-Simulation. Trotzdem können Anpassungen nötig sein.
{: .notice--info}

## Tutorials zu Füllwerkzeugen

{% include tutorials/tutorial_list key="werkzeug" value="Füllung" %}
