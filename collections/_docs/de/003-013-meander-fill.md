---
title: "Mäander Füllung"
permalink: /de/docs/stitches/meander-fill/
last_modified_at: 2023-05-01
toc: true
---
## Beschreibung

Mäanderfüllung hat seinen Ursprung in Quilt-Techniken. Für das Maschinensticken ergibt sich ein schöner gemusterter Effekt. Große Bereiche können mit relativ wenigen Stichen befüllt werden.

![Meander stitch detail](/assets/images/docs/meander-fill.png)

## Funktionsweise

* Erstelle einen geschlossenen Pfad mit einer Füllung. Aussparungen innerhalb der Form sind möglich.
* In den Parametereinstellungen (`Erweiterungen > Ink/Stitch > Parameter`) `Mäanderfüllung` als Füllmethode auswählen. Es gibt eine Menge an verschiedenen Mustern von denen ausgewählt werden kann. Alle Muster können über Skalierung, Glätten, Stichlänge- und Toleranz beeinflusst werden.

## Anfangs- und Endpunkt festlegen

Ink/Stitch erlaubt es über visuelle Befehle den [Anfangs- und Endpunkt eines Füllobjekts](/de/docs/commands) zu kennzeichnen.

## Parameter

Öffne `Erweiterungen > Ink/Stitch  > Parameter` um das Stickbild deinen Bedürfnissen anzupassen.

Einstellung          ||Beschreibung
---|---|---
Automatisch geführte Füllstiche | ☑ |Muss aktiviert sein
Füllmethode          | Mäanderfüllung|Für diesen Stichtyp bitte Mäanderfüllung auswählen
Muster               ||Various patterns to choose from
Muster skalieren     ||Skaliert das Muster (%)
Erweitern            |![Expand example](/assets/images/docs/params-fill-expand.png)  |Erweitert die Ursprungsform. Diese Option kann genutzt werden um Lücken zwischen angrenzenden Objekten zu verringern. Negative Werte verkleinern die Form.
Glätten              ||Glättet den Stichpfad. Diese Einstellung zeigt an, wie weit der geglättete Stichpfad vom ursprünglichen Pfad abweichen darf. Versuche niedrige Zahlen wie z.B. 0,2. Hinweis: Eventuell ist auch eine geringere Geradstich-Toleranz erforderlich.
Auf Pfad beschränken || Nützlich bei der Verwendung von Glätten und Erweitern. Sorgt dafür, dass keine Stiche außerhalb der ursprünglichen Form liegen.
Stichlänge           ||Definiert die maximale Stichlänge. Minimale Stichlänge bitte über die Geradstich-Toleranz festlegen.
Geradstich-Toleranz  ||Alle Stiche müssen innerhalb dieser Distanz vom Ursprungspfad liegen. Ein geringerer Toleranzwert bedeutet, dass Stiche enger zusammenliegen. Ein höherer Wert kann zu abgerundeten Ecken führen.
Wiederholungen                       || ◦ Legt fest, wie oft der Pfad durchlaufen werden soll<br/>◦ Standard: 1 (einmal vom Anfang bis zum Ende des Pfades)<br/>◦ Ungerade Zahl: Stiche enden am Ende des Pfades<br/>◦ Gerade Zahl: Die Naht kehrt zum Anfang des Pfades zurück
**Mehrfach Geradstitch Anzahl der Wiederholungen** || ◦ Jeden Stich vervielfachen.<br/>◦ Ein Wert von 1 würde jeden Stich verdreifachen (vorwärts, rückwärts, vorwärts).<br/>◦ Ein Wert von 2 würde jeden Stich fünffach ausführen, usw.<br/>◦ Durch die Eingabe mehrerer durch ein Leerzeichen getrennte Werte, kann ein Wiederholungsmuster erstellt werden.
Vernähen erlauben    || Vernäht bei Bedarf an den ausgewählten Positionen
Vernähen erzwingen   || Vernäht den Faden nach diesem Element, auch dann, wenn der Abstand zum Folgeobjekt geringer ist als in den [Ink/Stitch Einstellungen](/de/docs/preferences/) definiert.
Anstecher            ||Wähle die [Anstecher](/docs/stitches/lock-stitches) Variante (Anfang).
Verstecher           ||Wähle die [Verstecher](/docs/stitches/lock-stitches) Variante (Ende).
Fadenschnitt         || Schneidet den Faden nachdem dieses Objekt genäht wurde
Stopp                || Stoppt die Maschine nachdem dieses Objekt genäht wurde und springt zur Stopp-Position (sofern vorhanden)

## Unterlage

Die Unterlage für geführte Füllstiche folgt nicht der Führungslinie sondern nutzt den Füllwinkel der in den [Unterleger-Parametern](/de/docs/stitches/fill-stitch/#unterlage) festgelegt werden kann.

## Beispiele mit Mäanderfüllung

{% include tutorials/tutorial_list key="stichart" value="Mäanderfüllung" %}
