---
title: "Manuelle Stichplatzierung"
permalink: /de/docs/stitches/manual-stitch/
last_modified_at: 2024-04-28
toc: true
---
## Beschreibung
[![Manual Stitch Flowers](/assets/images/docs/manual-stitch.jpg){: width="200x"}](/assets/images/docs/manual-stitch.svg){: title="Download SVG File" .align-left download="manual-stitch.svg" }
Im manuellen Stichmodus stellt jeder Knoten des Pfades einen Nadeleinstich dar. So ist es möglich jeden Stich genau zu planen.

## Funktionsweise

1. Erstelle einen Pfad mit mehreren Knoten. Breite und Strichlinien-Einstellung haben keine Auswirkungen im manuellen Stichmodus.
2. Öffne `Erweiterungen > Ink/Stitch  > Parameter`.
3. Wähle als Methode `Manuelle Stichpositionierung`.

Jeder Knoten repräsentiert einen Nadeleinstich. Kurven werden dementsprechend nicht berechnet.

![Manual Stitch Placement](/assets/images/docs/manual-stitch-placement.png)

Für eine genaue Planung macht es deshalb Sinn, schon beim Zeichnen Kurven direkt ganz zu vermeiden, oder den Pfad vor dem Sticken entsprechend zu bearbeiten:
1. Wähle alle Knotenpunkte an (`F2` dann `Ctrl`+`A`)
2. Klicke auf ![Die gewählten Knoten in Ecken umwandeln](/assets/images/docs/tool-controls-corner.jpg){: title="Die gewählten Knoten in Ecken umwandeln" } in der `Werkzeugeinstellungsleiste`.g

## Params

Einstellung|Beschreibung
---|---
Geradstich                            | Muss aktiviert sein, damit diese Einstellungen wirksam werden.
Methode                               | `Manuelle Stichpositionierung` auswählen
Mehrfachgeradstich Anzahl der Wiederholungen | ◦ Jeden Stich vervielfachen.<br/>◦ Ein Wert von 1 würde jeden Stich verdreifachen (vorwärts, rückwärts, vorwärts).<br/>◦ Ein Wert von 2 würde jeden Stich fünffach ausführen, usw.<br/>◦ Gilt nur für den Geradstich.
Maximale Stitchlänge                  | Unterteilt Stiche die länger sind als dieser Wert. Leer lassen für keine Unterteilungen. Kurze Stiche werden gemäß den [Einstellungen](/docs/preferences/) herausgefiltert.
Minimale Stichlänge                   | Überschreibt die globale Einstellung für die minimale Stichlänge. Stiche, die kleiner sind als dieser Wert werden entfernt.
Minimale Länge für Sprungstiche       | Überschreibt die globale Einstellung für die minimale Länge für Sprungstiche. Kleinere Entfernungen zum nächsten Objekt haben keine Vernähstiche.
Vernähen erlauben                     | Bei manueller Stichpositionierung wird normalerweise kein Vernähstich automatisch hinzugefügt. Vernähstiche können jedoch über die Einstellung `Vernähstiche erzwingen` aktiviert werden.
Vernähen erzwingen                    | Aktiviert Vernähstiche für Pfade mit manueller Stichpositionierung.
Fadenschnitt                          | Schneidet den Faden nachdem dieses Objekt genäht wurde
Stopp                                 | Stoppt die Maschine nachdem dieses Objekt genäht wurde und springt zur Stopp-Position (sofern vorhanden)

## Tipps

### Faden vernähen

Im manuellen Modus muss auch das Vernähen von Hand angelegt werden. Wenn du den Faden vernähen willst, plane den Pfad entsprechend.

## Beispieldateien die den manuellen Stichmodus beinhalten

{% include tutorials/tutorial_list key="stichart" value="Manueller Stich" %}

