---
title: "Ripplestich"
permalink: /de/docs/stitches/ripple-stitch/
last_modified_at: 2024-04-28
toc: true
---
## Beschreibung

[![Ripple butterfly](/assets/images/docs/ripplefly.jpg){: width="200x"}](/assets/images/docs/ripplefly.svg){: title="Download SVG" .align-left download="ripplefly.svg" }
Ripple stich ist zum Teil Geradstich und zum Teil Füllstich: es verhält sich wie ein Geradstich (es kann beispielsweise als Dreifach-Geradstich genutzt werden) und definiert sich über eine Linie, aber das Stickergebnis erstreckt sich über eine Oberfläche. Ripples werden für lose Stickereien verwendet und sehen ein bisschen wie Wellen aus, daher auch der Name.

<p style="clear: both;">&nbsp;</p>

{% include video id="e1426a71-486a-4e62-a4c7-3b2f25dd1fc0" provider="diode" %}

Geschlossene Formen werden mit einer Spirale gefüllt (z.B. Kreis). Bei offenen Formen (Linie mit Anfang und Ende) wird hin und her gestickt. Schauen wir uns beide Formen genauer an.

## Geschlossene Formen

* Erstelle einen einfachen geschlossenen Pfad mit einer Linienfarbe (keine kombinierten Pfade aus mehreren Teilen)
* (Optional) Erstelle eine [Zielposition oder Führungslinien](#ripple-stiche-führen)
* Öffne die Parametereinstellungen (`Erweiterungen > Ink/Stitch > Parameter`) und setze die `Methode` auf `Ripple`.
* Stelle die übrigen [Parameter](#parameter) nach deinen Wünschen ein und klicke auf Anwenden

![Circular ripple examples](/assets/images/docs/en/circular-ripple.svg)

[Beispieldatei herunterladen](/assets/images/docs/en/circular-ripple.svg)

## Offene Formen

Lineare Ripples können auf verschiedene Weise erstellt werden. Sie können aus einer einfachen Kurve bestehen oder sogar wie eine Satinsäule konstruiert werden.

* Erstelle eine offene Form (einfache Linie, kombinierte Linien oder Satinsäule)
* (Optional) Erstelle eine [Zielposition oder Führungslinien](#ripple-stiche-führen)
* Öffne die Parametereinstellungen (`Erweiterungen > Ink/Stitch > Parameter`) und setze die `Methode` auf `Ripple`.
* Stelle die übrigen [Parameter](#parameter) nach deinen Wünschen ein und klicke auf Anwenden

![Linear ripple examples](/assets/images/docs/en/linear-ripple.svg)

[Beispieldatei herunterladen](/assets/images/docs/en/linear-ripple.svg)

## Schleifen

Schleifen (also sich selbst kreuzende Pfade) sind bei Ripple-Stichen erlaubt und willkommen. Nutze Schleifen um besondere, interessante Effekte zu erzielen.

![Looping ripple stitches](/assets/images/docs/en/ripple-loops.svg)

[Beispieldatei herunterladen](/assets/images/docs/en/ripple-loops.svg)

##  Ripple-Stiche führen

Ripples mit nur **einem Unterpfad** (geschlossene Formen oder einfache Bézier-Kurven) können mit jeder der folgenden Methoden geführt werden.

### Zielposition

Definiere eine Zielposition mit einem [visuellen Befehl](/de/docs/commmands/):

* Öffne `Erweiterungen > Ink/Stitch > Befehle > Befehle mit gewählten Objekten verknüpfen...`
* Wähle `Zielposition` und clicke auf Anwenden
* `Strg + Klick` auf das Symbol des Befehls um es auszuwählen, dann bewege es zur gewünschten Position

Wenn keine Zielposition definiert wurde, läuft der Pfad auf die Mitte des Objektes zu.

### Führungslinie

* Erstelle mit dem Bézier-Werkzeug eine Linie die in der Nähe der Ripple-Form startet und von ihr wegführt. Die neue Linie muss sich genau in der gleichen Gruppen (auch keine Untergruppe) befinden, wie die Ripple-Form.
* Wähle die Linie aus und wandel sie mit `Erweiterungen > Ink/Stitch > Bearbeiten > Auswahl zu Führungslinie` in eine Führungslinie um.
* Wähle die Ripple-Form aus und öffne die Parametereinstellungen. Ändere die Parameter bis das Ergebnis den Wünschen entspricht.

### Satin-Führung

Die Satin-Führung eröffnet die Möglichkeit die Ripplestiche genauer zu führen. Sowohl die Satin-Querstreben, als auch die Breite der Satinkolumne selber wirken sich auf die Ripplestiche aus. Ausschlaggebend für die spätere Positionierung ist nicht die Ripple-Form selbst, sondern die Position der Führungslinie. Zur Vereinfachung der Steuerung der finalen Breite ist es ratsam (aber nicht notwendig) die Satin-Führung so anzulegen, dass sie zu Beginn ungefähr der Breite der Ripple-Form entspricht.

* Erstelle eine [Satinsäule](/de/docs/stitches/satin-column/) mit Richtungslinien. Die Satinsäule muss sich genau in der gleichen Gruppen (auch keine Untergruppe) befinden, wie die Ripple-Form.
* Wähle die Satinsäule aus und wandel sie mit `Erweiterungen > Ink/Stitch > Bearbeiten > Auswahl zu Führungslinie` in eine Führungslinie um.
* Wähle die Ripple-Form aus und öffne die Parametereinstellungen. Ändere die Parameter bis das Ergebnis den Wünschen entspricht.

## Parameter

Parameter||Beschreibung
---|---|---
Geradstich                     | ☑ | Muss aktiviert sein, damit diese Einstellungen wirksam werden.
Methode                        || Bitte `Ripple` wählen
Wiederholungen                 || ◦ Legt fest, wie oft der Pfad durchlaufen werden soll<br/>◦ Standard: 1 (einmal vom Anfang bis zum Ende des Pfades)<br/>◦ Ungerade Zahl: Stiche enden am Ende des Pfades<br/>◦ Gerade Zahl: Die Naht kehrt zum Anfang des Pfades zurück
Mehrfach Geradstich Anzahl der Wiederholungen || ◦ Aktiviert den [Mehrfachgeradstich Modus](/de/docs/stitches/bean-stitch/)<br />◦ Jeden Stich vervielfachen.<br />Ein Wert von 1 verdreifacht jeden Stich (vorwärts, rückwärts, vorwärts).<br/>◦ Ein Wert von 2 verfünffacht jeden Stich, usw.
Stichlänge                     || Länge der Stiche
Geradstich Toleranz            || Alle Stiche müssen innerhalb dieser Distanz zum Pfad liegen. Eine niedrigere Toleranz verkürzt die Stiche. Eine höhere Toleranz kann scharfe Ecken abrunden.
Zufällige Stichlänge                  | Anstatt einer gleichmäßigen Verteilung, erfolgt die Stichlänge und -phase nach dem Zufallsprinzip. Dies wird besonders für eng beieinander liegende Kurvenfüllungen empfohlen, um Moiré-Artefakte zu vermeiden.
Zufallsabweichung von der Stichlänge  | Maximale randomisierte Abweichung der Stichabstände in Prozent. Zufällige Stichlänge randomisieren muss aktiviert sein.
Anzahl der Linien|<img src="/assets/images/docs/ripple_only_lines.svg" alt="Nombre de lignes"/>| Anzahl der Wiederholungen der Ripple-Form. Voreinstellung: 10.
Minimaler Linienabstand        || Diese Einstellung überschreibt den Wert "Anzahl der Linien"
Reihenanzahl bis sich das Muster wiederholt   ||  Dieser Wert beschreibt, nach wie vielen Reihen die Einstichstellen übereinander liegen. Dezimalwerte sind zulässig und zeigen weniger deutliche Diagonalen im Stickbild. Nur für lineare Ripples.
◦ Erste Linien überspringen <br /> ◦ Letzte Linien überspringen |<img src="/assets/images/docs/ripple_only_skip.svg" alt="Sauter"/>| Die ersten / letzten Ripple-Wiederholungen werden übersprungen und die Gesamtanzahl der Wiederholungen verringert sich.
Linienabstand Exponent|<img src="/assets/images/docs/ripple_only_exponent.svg" alt="Exponant"/>| ◦ Mit der Voreinstellung von 1 ist der Abstand zwischen den Linien konstant<br />◦ Mit einem Wert größer als 1 erhöht sich der Abstand zwischen den Linien sukzessiv<br />◦ Mit einem Wert kleiner als 1 verringert sich der Abstand zwischen den Linien.
Exponent umkehren              |☑  oder ▢| Kehrt den Effekt des Exponent-Wertes um.
Umkehren                       |☑  oder ▢| Kehrt den gesamten Pfad um (Start = Ende). Andere Parameter bleiben von dieser Einstellung unberührt.
Konturlinien umkehren|| Außenkonturen der Satin-Führungslinie umkehren. In der Standardeinstellung werden gegenläufig verlaufende Linien automatisch korrigiert.
Größe des Gitters              |<img src="/assets/images/docs/ripple_only_grid.svg" alt="Distance"/>| Fügt quer verlaufende Linien hinzu, die zu einem Gittereffekt führen. Die Größe des Gitters kann auch Auswirkungen auf die Genauigkeit des Linienverlaufs haben.
Skalieren                      | XY, X, Y oder Keine | Nur für geführte Ripples
Start-Skalierung               | Prozentwert | Definiert die Skalierung der ersten Linie. Nur für geführte Ripples.
End-Skalierung                 | Prozentwert | Definiert die Skalierung der letzten Linie. Nur für geführte Ripples.
Rotieren                       | ☑  oder ▢| Nur für geführte Ripples
Kantenstil                     |<img src="/assets/images/docs/flat_or_point.svg" alt="Join Stile"/> | Verbindungen zwischen den Linien: flach (oben) oder spitz (unten). Nur für offene Ripples.
Minimale Stichlänge                   || Überschreibt die globale Einstellung für die minimale Stichlänge. Stiche, die kleiner sind als dieser Wert werden entfernt.
Minimale Länge für Sprungstiche       || Überschreibt die globale Einstellung für die minimale Länge für Sprungstiche. Kleinere Entfernungen zum nächsten Objekt haben keine Vernähstiche.
Vernähen erlauben              || Vernäht bei Bedarf an den ausgewählten Positionen
Vernähen erzwingen             | ☑  oder ▢| Vernäht den Faden nach diesem Element, auch dann, wenn der Abstand zum Folgeobjekt geringer ist als in den [Ink/Stitch Einstellungen](/de/docs/preferences/) definiert.
Anstecher                      ||Wähle die [Anstecher](/de/docs/stitches/lock-stitches) Variante (Anfang).
Verstecher                     ||Wähle die [Verstecher](/de/docs/stitches/lock-stitches) Variante (Ende).
Fadenschnitt                   | ☑  oder ▢| Schneidet den Faden nachdem dieses Objekt genäht wurde
Stopp                          | ☑  oder ▢| Stoppt die Maschine nachdem dieses Objekt genäht wurde und springt zur Stopp-Position (sofern vorhanden)
{: .params-table }

## Ripple-Übersicht

![Many ripples](/assets/images/docs/en/rippleways_en.svg)

[Download](/assets/images/docs/en/rippleways_en.svg){: download="rippleways.svg" }

### Beispieldateien mit Ripple Stitch

{% include tutorials/tutorial_list key="stichart" value="Ripplestich" %}
