# pygame-example
kurzes Beispiel eines einfachen Labyrinth-Spiels in Python mit PyGame

Hinweise
========
Um dieses Projekt auszuführen wird Python und PyGame benötigt (www.python.org & www.pygame.org).

Dieses "Spiel" entstand während des Technik-Camps 2019 in Überlingen am Bodensee als einfaches Beispiel,
wie man in Python mithilfe der PyGame-Library Spiele programmiert. Es stand vor allem kurzer, einfacher
Code im Vordergrund, d.h. es ging darum, so schnell wie möglich etwas auf den Bildschirm zu bekommen
was sich spielen lässt. Daher wurde auf Klassen und Funktionen usw. verzichtet.

Als Besonderheit befindet sich in diesem Projekt ein Algorithmus, mit dem die Spielfigur sauber um die Ecke
gleitet, wenn sie sich vor einem schmalen Durchgang befindet. Der Spieler drückt lediglich die Richtungstaste in
die er eigentlich laufen will, und die Figur läuft notfalls einen kleinen Bogen um die Mauerecke, um dann
in den Gang zu "rutschen".

Mit F12 lässt sich der Debug-Modus ein- und ausschalten, welcher die Tiles (Kacheln), welche zur Bestimmung
von Kollisionen herangezogen werden, mithilfe von gelben Rahmen visualisiert werden.
