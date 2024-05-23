---
title: "Garnfarben-Verwaltung"
permalink: /de/docs/thread-color/
last_modified_at: 2024-05-09
toc: true
---
## Handhabung von Farbpaletten

Die Inkscape Farbpaletten befinden sich unten rechts neben den Farbfeldern.

![Inkscape Farbpaletten](/assets/images/docs/palettes-location.png)

Klicke auf den kleinen Pfeil, um eine Liste der installierten Paletten zu öffnen und wähle die Herstellerfarbpalette abhängig von dem Garn, das verwendet werden soll.

Die Auswahl wirkt sich auch auf die in der Druckvorschau angezeigten Garnnamen aus.

## Farbpaletten installieren

### Vordefinierte Farbpaletten für Insckape installieren

Ink/Stitch enthält viele Farbpaletten der üblichen Garnhersteller. Diese können installiert werden, damit sie in Inkscape nutzbar sind.
Das erlaubt dir dein Design mit den richtigen Farben zu planen. Die Farben werden in die PDF-Ausgabe übernommen und auch in der Stickdatei abgespeichert, sofern dein Stickformat dies unterstützt.

**Installation**

* Gehe zu `Erweiterungen -> Ink/Stitch -> Garnfarben Verwaltung > Installiere Erweiterungen für Inkscape`
* Wähle "Installieren"
* Starte Inkscape neu

## Benutzerdefinierte Farbpalette installieren

Wenn du eine `.gpl` Liste hast, die deine Garnfarben abbildet, kannst du sie mit dieser Erweiterung einfach in Inkscape verfügbar machen: `Erweiterungen > Ink/Stitch > Garnfarben Verwaltung > Benutzerdefinierte Farbpalette installieren`.
Inkscape muss nach diesem Vorgang neu gestartet werden.

Farbpaletten können mit Ink/Stitch erstellt werden. Wie das geht wird auf dieser Seite weiter unten beschrieben.

## Farbpalette erstellen

Inkscape kann `.gpl` Farbpaletten erstellen. Aber es ist nicht möglich, die Farben zu sortieren.

Diese Erweiterung exportiert die Farben von Textelementen, während der Text selbst als Farbname und Nummer abgespeichert wird.

1. Importiere ein Bild mit den Garnfarben, die die neue Farbpalette enthalten soll.
2. Aktiviere das Text-Werkzeug und füge die Farbnamen ein (wenn vorhanden) oder tippe sie ein.
   Benutze eine Zeile pro Farbe.
   Wenn der letzte Teil des Farbnamens eine Nummer ist, wird er als Katalognummer interpretiert und abgespeichert.
3. `Erweiterungen > Ink/Stitch > Garnfarben Verwaltung > Palette erstellen > Text zerlegen` teilt den Text in einzelne Textelemente.
4. Aktiviere das Farbwahl-Werkzeug (D) und färbe die einzelnen Textelemente ein.
   Nutze dabei die Tabulator-Taste um das jeweils nachfolgende Textelement auszuwählen.
5. Wähle alle Text-Elemente aus und führe die Funktion `Erweiterungen > Ink/Stitch > Garnfarben Verwaltung > Palette erstellen > Farbpalette erstellen ...` aus.
6. Gib einen Namen für die Farbpalette ein und klicke auf Anwenden.
7. Inkscape neu starten um die neue Farbpalette verfügbar zu machen

{% include video id="4bcRVoKvzAw" provider="youtube" %}

### Farbpalette zu Text

Bereits bestehende Farbpaletten können mit Ink/Stitch als Text bearbeitet werden.

* Importiere Farben und Farbnamen mit `Erweiterungen > Ink/Stitch > Garnfarben verwalten > Palette zu Text`
* Ändere Farben, Farbnamen, Katalognummern oder füge weitere Farben hinzu.
* Exportiere die Palette mit `Erweiterungen > Ink/Stitch > Garnfarben Verwaltung > Palette erstellen > Farbpalette erstellen ...`
* Inkscape neu starten

## Farben auf ein geöffnetes Design übertragen

### Farbpalette anwenden

{% include upcoming_release.html %}

Diese Erweiterung wendet die ähnlichsten Farben einer gewählten Farbpalette auf das geöffnete Design an.
Die Farben werden entsprechend in die Stickdatei gespeichert und in der PDF-Ausgabedatei angezeigt.

* Öffne `Erweiterung > Ink/Stitch > Garnfarben Verwaltung > Farbpalette anwenden`
* Wähle eine Farbpalette
* Klicke auf `Anwenden`

### Garnfarben-Liste anwenden

Ink/Stitch kann Garnlisten auf ein Design anwenden. Das ist besonders dann nützlich, wenn du mit bestehenden Stickdateien arbeitest, die keine Farbinformationen speichern (z.B. DST).

Außerdem könnte diese Funktion dazu dienen, verschiedene Farbvariationen auszuprobieren. Du kannst Garnlisten importieren und exportieren wie es dir gefällt. Wichtig ist nur, dass sich die Stickreihenfolge- und anzahl der Objekte nicht ändert. In einem solchen Fall solltest du auf das Speichern der kompletten SVG-Datei zurückgreifen (das ist auch sonst nie eine schlechte Idee).

* Run `Extensions > Ink/Stitch > Thread Color Management > Apply Threadlist`
* Choose a file with the thread color information to match the elements in the current document
* Define wether the color infomration file has been generated with Ink/Stitch or otherwise.
  If otherwise: Select the Ink/Stitch color palette to match colors to.
* Click on Apply

## Garnliste Exportieren

Garnlisten können nur über eine ZIP-Datei exportiert werden ([batch export](/de/docs/import-export/#batch-export))
