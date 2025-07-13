# RogueLiteTutorial

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/status-learning-informational)
![tcod](https://img.shields.io/badge/based_on-tcod_tutorial-green)

🎮 Ein kleines Roguelike-Spiel in Python – entstanden im Rahmen des [tcod Roguelike-Tutorials](https://rogueliketutorials.com/tutorials/tcod/v2/), Schritt für Schritt umgesetzt und mit viel Freude ausprobiert.

## Was ist das?

Dies ist **mein persönliches Ergebnis des RogueLite-Tutorials**. Es basiert auf:
- Python 3
- `tcod` (libtcod) als ASCII-Grafik- und Game-Engine
- zufälliger Dungeon-Generierung
- simplen Gegnern, Gegenständen und Spielmechaniken

Das Spiel läuft aktuell im Terminal – klassisch und charmant.  
Und obwohl ich wahrscheinlich nur 20 % des Codes wirklich verstanden habe, **funktioniert’s erstaunlich gut**. 😄

## Zielgruppe

Jede Person, die selbst das Tutorial macht (oder gemacht hat) und neugierig ist, wie es bei anderen aussieht.  
Oder die einfach gerne durch Dungeons streift und ASCII-Monster vermöbelt.

## Ausführen

1. Python installieren (am besten 3.10+)
2. Virtuelle Umgebung anlegen:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # oder .venv\Scripts\activate unter Windows
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
4. Spiel starten:
   ```bash
   python main.py
   ```

## Abhängigkeiten

Alle benötigten Pakete sind in der Datei `requirements.txt` aufgelistet.  
Darin enthalten sind unter anderem:

```
tcod==18.1.0
numpy==2.0.2
cffi==1.17.1
pycparser==2.22
typing_extensions==4.14.1
```

## Noch nicht enthalten

- Sound  
- Grafiken  
- Windows-exe  
- Tieferes Verständnis 😉

Aber hey – das kommt vielleicht später.

## Lizenz

Da es sich im Kern um Tutorial-Code handelt, orientiert sich dieses Projekt an der Lizenz des Original-Tutorials.  
Für alles Weitere gilt: Feel free to fork, spielen, anpassen, kaputtmachen und wieder reparieren.
