# Lottospiel

Ein Lotto-Spiel für die Konsole, geschrieben in Python. Entstanden als Projekt in der Münchner Coding Akademy.

## Funktionen

- 1 bis 12 Tippfelder mit je 6 eindeutigen Zahlen (1-49)
- Pro Feld wahlweise manuelle Eingabe oder automatischer Tipp
- Superzahl (0-9)
- Zufällige Ziehung und Auswertung aller Felder
- Eingabeprüfung: keine Buchstaben, Wertebereich wird geprüft, doppelte Zahlen werden abgelehnt

## Starten

Voraussetzung ist Python 3. Zusätzliche Pakete werden nicht benötigt.

```
python lottospiel.py
```

## Spielregeln und Gewinne

| Richtige Zahlen | Ergebnis    |
|-----------------|-------------|
| 0 bis 2         | kein Gewinn |
| 3               | 100 €       |
| 4               | 1.000 €     |
| 5               | 10.000 €    |
| 6               | Jackpot     |

Die Superzahl wird zusätzlich verglichen und gesondert gemeldet.

## Beispielablauf

```
Wie viele Felder möchtest du spielen? (1-12): 2

Feld 1:
Manuell oder automatisch? (1 = manuell, 2 = automatisch): 1
Bitte gib deine 1. Zahl von 6 ein: 3
Bitte gib deine 2. Zahl von 6 ein: 7
Bitte gib deine 3. Zahl von 6 ein: 12
Bitte gib deine 4. Zahl von 6 ein: 25
Bitte gib deine 5. Zahl von 6 ein: 33
Bitte gib deine 6. Zahl von 6 ein: 49

Feld 2:
Manuell oder automatisch? (1 = manuell, 2 = automatisch): 2
Automatischer Tipp: [2, 10, 23, 24, 35, 48]
Was ist deine Superzahl? (0-9): 5

Die Gewinnerzahlen sind: [3, 7, 12, 18, 24, 34]

Ergebnis für Feld 1:
Übereinstimmung: [3, 7, 12]
Du hast 100€ gewonnen!

Ergebnis für Feld 2:
Übereinstimmung: [24]
Leider kein Gewinn.
Du hast die Superzahl falsch getippt. Die Superzahl war 9.
```

## Gelernte Konzepte

Funktionen, Schleifen, Listen (auch geschachtelt), Fehlerbehandlung mit `try/except`, f-Strings, das Modul `random`.

## Lizenz

MIT, siehe [LICENSE](LICENSE).
