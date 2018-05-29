from kik_plansza import *
from kik_kom import *
import kik_ai
import kik_ai_los
import os


def wyswietl_plansze(plansza):
    print("-------------------")
    for i in range(len(plansza)):
        print("|  " + pionek(plansza[i][0]) + "  |  " +
              pionek(plansza[i][1]) + "  |  " + pionek(plansza[i][2]) + "  |")

        print("-------------------")


# tryb 0 - człowiek vs człowiek
# tryb 1 - człowiek vs komputer
# tryb 2 - komputer vs komputer

def partia(tryb, symbol_gracza, zaczynajacySymbol):

    dna = [[9.192329406738281, 8.324653625488281], [9.721359252929688, 7.469078063964844], [9.496025085449219, 9.840873718261719], [9.514266967773438, 11.944732666015625], [8.434219360351562, 13.248138427734375], [
        8.639129638671875, 11.634796142578125], [7.7268218994140625, 11.596717834472656], [10.829757690429688, 10.24554443359375], [14.114982604980469, 11.238487243652344], [9.053512573242188, 11.372337341308594]]
    plansza = nowa_pusta_plansza()
    czy_ruch_wykonany = False
    czy_gra_skonczona = False
    gracz = zaczynajacySymbol
    wygrany_gracz = 0
    while(not czy_gra_skonczona):
        print()
        wyswietl_plansze(plansza)
        if(tryb == 0 or (tryb == 1 and gracz == symbol_gracza)):
            # print(kom_ruch(gracz))
            # kolumna = int(input("podaj kolumne: "))
            # wiersz = int(input("podaj wiersz: "))
            wiersz, kolumna = kik_ai_los.wybierzRuch(plansza, gracz)
            print(kom_ruch_przeciw(gracz, wiersz, kolumna))

        else:
            wiersz, kolumna = kik_ai.wybierzRuch(plansza, gracz, dna)
            print(kom_ruch_przeciw(gracz, wiersz, kolumna))

        czy_ruch_wykonany, plansza, gracz = wykonaj_ruch(
            plansza, gracz, wiersz, kolumna)

        if(not czy_ruch_wykonany):
            print(kom_zly_ruch())

        czy_gra_skonczona, wygrany_gracz = koniec_gry(plansza)
    wyswietl_plansze(plansza)
    print(kom_koniec(wygrany_gracz))
    return(wygrany_gracz)


def zamienZaczynajacySymbol(symbol):
    if(symbol == -1):
        return 1
    else:
        return -1


def gra():
    gracz1 = 0

    wygrany = 0
    punkty = [0, 0, 0]

    numer_partii = 0
    ile_partii = 0

    print("tryb 0 - człowiek vs człowiek")
    print("tryb 1 - człowiek vs komputer")
    print("tryb 2 - komputer vs komputer")
    tryb = int(input("Wybierz tryb (0,1,2): "))
    print()
    print("O: 1")
    print("X: -1")

    if(tryb != 2):
        gracz1 = int(input("wybierz symbol (-1/1): "))
        zaczynajacySymbol = gracz1
    else:
        zaczynajacySymbol = -1

    print()
    ile_partii = int(input("Ile partii chcesz zagrać? "))

    while(numer_partii < ile_partii):
        numer_partii += 1
        print()
        print("Partia: " + str(numer_partii))
        wygrany = partia(tryb, gracz1, zaczynajacySymbol)
        punkty[wygrany] += 1
        print()
        print("Zwycięstwa X: " + str(punkty[2]))
        print("Zwycięstwa 0: " + str(punkty[1]))
        print("Remisy: " + str(punkty[0]))
        zaczynajacySymbol = zamienZaczynajacySymbol(zaczynajacySymbol)
    return punkty


gra()
