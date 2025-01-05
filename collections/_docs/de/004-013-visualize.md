---
title: "Visualisierung"
permalink: /de/docs/visualize/
last_modified_at: 2024-03-13
toc: true
---
## Simulator

Wähle die Objekte aus, die in der simulierten Vorschau angezeigt werden sollen. Wenn das gesamtes Design simuliert werden soll, wähle alles (`Strg + A`) oder nichts aus.

Dann starte `Erweiterungen -> Ink/Stitch -> Simulation -> Visualisieren und Exportieren` und lehne dich zurück.

![Simulator](/assets/images/docs/en/simulator.jpg)
{: style="border: 2px solid gray; padding: 5px;"}

### Tastenkombinationen der Simulation

tastenkombination | Beschreibung
-------- | --------
<key>Leertaste</key> | Animation starten
<key>p</key> | Animation pausieren
<key>→</key> | vorwärts
<key>←</key> | rückwärts
<key>↑</key> | schneller
<key>↓</key> | langsamer
<key>+</key> | ein Frame vorwärts
<key>-</key> | ein Frame rückwärts
<key>Page down</key> | zum voherigen Befehl springen
<key>Page up</key> | zum nächsten Befehl springen

Es ist auch möglich die Simulation mit der Maus zu **zoomen** und zu **verschieben**.

## Stich-Plan Vorschau

Führe den Befehl `Erweiterungen > Ink/Stitch > Visualisierung und Export > Stichplan Vorschau` aus.
Anstatt die Vorschau einzufügen, reicht manchmal auch die Option `Live Preview`.

Wird der Stickplan jedoch eingefügt, kann das Design genauer untersucht und ggf. angepasst und ergänzt werden. Es ist immer noch möglich, den Stickplan später durch die Option `Erweiterungen > Ink/Stitch > Visualisieren und Exportieren > Stich-Plan Vorschau aufheben` zu entfernen.

Es gibt die folgenden Optionen:

- **Design-Layer Sichtbarkeit** definiert die Sichtbarkeit, bzw. Transparenz der Design-Layer
  - **unverändert** die Design-Layer bleiben unverändert
  - **versteckt** das Original-Design wird versteckt
  - **Verrinerte Deckkraft** das Original wird mit 40%-Transparenz dargestellt
- **Render Modus**
  - **Einfach**: einfache Liniendarstellung
  - **Realistisch**: Realistische Vorschau als in Inkscape eingebundene PNG-Bilddatei (8-bit)
  - **Realistisch (hohe Qualität)** Realistische Vorschau als in Inkscape eingebundene PNG-Bilddatei (16-bit)
  - **Realistisch Vektor (langsam)** Vektor-Ausgabe mit realistischen Filtern
- **Stickplan an der Seite platzieren** Der Stichplan wird rechts neben dem Canvas abgebildet.
  Ist diese Option nicht aktiviert, wird der Stichplan direkt über das Design gelegt.
  In diesem Fall ist es nützlich die Sichtbarkeit des Designs anzupassen.
- **Nadeleinstichstellen** zeigt Punkte an den Einstichstellen
- **Lock** Stichplan reagiert nicht auf Mausinteraktionen. Das ist praktisch, wenn mit aktiviertem Stichplan das Original-Design bearbeitet werden soll
- **Zeige visuelle Befehle**
- **Letzten Stichplan überschreiben**
  Überschreibt den letzten Stichplan wenn aktiviert. Soll der alte Stichplan erhalten bleiben, deaktiviere diese Option.

{% include folder-galleries path="stitch-plan/" captions="1:Stitch plan beside canvas;2:Layer visibility set to hidden;3:Layer visibility set to lower opacity;4:Needle points enabled | disabled" caption="<i>Example image from [OpenClipart](https://openclipart.org/detail/334596)</i>" %}

## Stich-Plan Vorschau aufheben

Wird der Stichplan über dem Design mit verringerter Deckkraft angezeigt, hilft es eine visuelle Idee zu bekommen, wie das Design am Ende aussehen wird. Manchmal ist es hilfreich, in einen angezeigten Stichplan hineinzuarbeiten. Dies jedoch, kann es schwieriger machen, den Stichplan wieder zu entfernen und da auch die Deckkraft wieder zurückgesetzt werden muss. Mit dieser Erweiterung kann auch der Stichplan nach erfolgten Änderungen am Dokument einfach wieder entfernt werden.

`Erweiterungen > Ink/Stitch > Visualisieren und Exportieren > Stich-Plan Vorschau aufheben`

## Dichte Indikator

Zeigt Punkte in frei wählbaren Farben (Standart: rot, gelb, grün) über dem Design. Sie helfen Stellen mit hoher Dichte ausfindig zu machen.

* Wähle die Objekte aus, bei denen die Dichte angezeigt werden soll. Wird keine Auswahl getroffen, analysiert diese Erweiterung das gesamte Dokument
* Öffne `Erweiterungen > Ink/Stitch > Visualisieren und Exportieren > Dichte Indikator`
* Setze die Farben wie gewünscht und klicke auf `Anwenden`
* Untersuche das Design (evtl. ist es nötig stärker in das Design hineinzuzoomen)
* Entferne die Dichte-Punkte mit `Ctrl + Z` (rückgängig machen)

### Optionen

* Rot / gelbe Markierungen

  Definiere ab vielen Stichen in welchem Radius die Markerungen rot / gelb gefärbt werden sollen
* Design-Layer Sichtbarkeit

  Definiere ob Ink/Stitch die Design-Ebene unverändert belassen soll, sie verstecken oder die Deckkraft verringern soll
* Indikator-Größe

  Lege die Größe der eingefügten Markierungen in Dokumenteinheit fest

## Stickreihenfolge anzeigen

Diese Erweiterung fügt nummerierte Beschriftungen für ausgewählte Elemente in das Dokument ein, um die Stichreihenfolge zu visualisieren.

* Öffne `Erweiterungen > Ink/Stitch > Visualisieren und Exportieren > Stickreihenfolge anzeigen...`
* Wähle die Schriftgröße
* Klicke auf "Anwenden".

![Display stacking order](/assets/images/docs/stacking_order.png)

## PDF-Export

Die Informationen zum PDF-Export sind auf einer gesonderten Seite zusammengefasst: [mehr Informationen zum PDF-Export](/de/docs/print-pdf)
