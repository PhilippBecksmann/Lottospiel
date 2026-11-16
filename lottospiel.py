"""Lottospiel für die Konsole.

Der Spieler tippt 1 bis 12 Felder mit je 6 Zahlen (1-49), manuell oder
automatisch, und wählt eine Superzahl (0-9). Danach zieht der Computer
die Gewinnzahlen und wertet alle Felder aus.
"""
import random


def liefere_ganze_zahl(frage, minimum, maximum):
    while True:
        try:
            zahl = int(input(frage))
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")
            continue

        if minimum <= zahl <= maximum:
            return zahl

        print(f"Bitte gib eine Zahl zwischen {minimum} und {maximum} ein.")


def generiere_lotto_zahlen():
    lotto_zahlen = list(range(1, 50))
    ziehung = []
    zaehler = 0

    while zaehler < 6:
        zahl = random.choice(lotto_zahlen)
        ziehung.append(zahl)
        lotto_zahlen.remove(zahl)
        zaehler += 1

    return sorted(ziehung)


def generiere_super_zahl():
    super_zahlen = list(range(0, 10))
    super_zahl = random.choice(super_zahlen)
    return super_zahl


def liefere_spieler_zahlen():
    spieler_zahlen = []
    zaehler = 1

    while zaehler <= 6:
        zahl = liefere_ganze_zahl(f"Bitte gib deine {zaehler}. Zahl von 6 ein: ", 1, 49)

        if zahl in spieler_zahlen:
            print("Diese Zahl hast du bereits eingegeben.")
        else:
            spieler_zahlen.append(zahl)
            zaehler += 1

    return sorted(spieler_zahlen)


def lotto_ziehung_mit_superzahl():
    lotto_zahlen = generiere_lotto_zahlen()
    super_zahl = generiere_super_zahl()
    return lotto_zahlen, super_zahl


def vergleiche_lotto_zahlen_mit_spieler_zahlen(lotto_zahlen, spieler_zahlen):
    ergebnis = []

    for zahl in lotto_zahlen:
        if zahl in spieler_zahlen:
            ergebnis.append(zahl)

    return ergebnis


def bewerte(ergebnis):
    print("Übereinstimmung:", ergebnis)
    laenge = len(ergebnis)

    if laenge < 3:
        print("Leider kein Gewinn.")
    elif laenge == 3:
        print("Du hast 100€ gewonnen!")
    elif laenge == 4:
        print("Du hast 1000€ gewonnen!")
    elif laenge == 5:
        print("Du hast 10000€ gewonnen!")
    elif laenge == 6:
        print("Du hast den Jackpot gewonnen!")


def erstelle_tippfelder():
    anzahl_felder = liefere_ganze_zahl("Wie viele Felder möchtest du spielen? (1-12): ", 1, 12)
    tippfelder = []
    zaehler = 1

    while zaehler <= anzahl_felder:
        print(f"\nFeld {zaehler}:")
        auswahl = liefere_ganze_zahl("Manuell oder automatisch? (1 = manuell, 2 = automatisch): ", 1, 2)

        if auswahl == 1:
            spieler_zahlen = liefere_spieler_zahlen()
        else:
            spieler_zahlen = generiere_lotto_zahlen()
            print("Automatischer Tipp:", spieler_zahlen)

        tippfelder.append(spieler_zahlen)
        zaehler += 1

    return tippfelder


def vergleiche_alle_tippfelder(tippfelder, lotto_zahlen):
    alle_ergebnisse = []

    for spieler_zahlen in tippfelder:
        ergebnis = vergleiche_lotto_zahlen_mit_spieler_zahlen(lotto_zahlen, spieler_zahlen)
        alle_ergebnisse.append(ergebnis)

    return alle_ergebnisse


def bewerte_alle_tippfelder(alle_ergebnisse):
    feldnummer = 1

    for ergebnis in alle_ergebnisse:
        print(f"\nErgebnis für Feld {feldnummer}:")
        bewerte(ergebnis)
        feldnummer += 1


def vergleiche_super_zahl(gezogene_super_zahl, getippte_super_zahl):
    if gezogene_super_zahl == getippte_super_zahl:
        print("Du hast die Superzahl richtig getippt.")
    else:
        print(f"Du hast die Superzahl falsch getippt. Die Superzahl war {gezogene_super_zahl}.")


def start():
    tippfelder = erstelle_tippfelder()
    getippte_super_zahl = liefere_ganze_zahl("Was ist deine Superzahl? (0-9): ", 0, 9)
    gezogene_lotto_zahlen, gezogene_super_zahl = lotto_ziehung_mit_superzahl()

    print("\nDie Gewinnerzahlen sind:", gezogene_lotto_zahlen)

    alle_ergebnisse = vergleiche_alle_tippfelder(tippfelder, gezogene_lotto_zahlen)
    bewerte_alle_tippfelder(alle_ergebnisse)
    vergleiche_super_zahl(gezogene_super_zahl, getippte_super_zahl)


if __name__ == "__main__":
    start()

