from kik_plansza import *
from kik_kom import *


def wyswietl_plansze(plansza):
    print("-------------------")
    for i in range(len(plansza)):
        print("|  " + pionek(plansza[i][0]) + "  |  " +
              pionek(plansza[i][1]) + "  |  " + pionek(plansza[i][2]) + "  |")

        print("-------------------")


def gra():

    plansza = nowa_pusta_plansza()
    czy_ruch_wykonany = False
    czy_gra_skonczona = False
    gracz = -1
    wygrany_gracz = 0
    while(not czy_gra_skonczona):
        wyswietl_plansze(plansza)
        print(kom_ruch(gracz))
        wiersz = int(input("podaj wiersz: "))
        kolumna = int(input("podaj kolumne: "))
        czy_ruch_wykonany, plansza, gracz = wykonaj_ruch(
            plansza, gracz, wiersz, kolumna)

        if(not czy_ruch_wykonany):
            print(kom_zly_ruch())

        print(plansza)
        czy_gra_skonczona, wygrany_gracz = koniec_gry(plansza)

    print(kom_koniec(wygrany_gracz))


graj = True
while(graj):
    gra()
    x = input("Czy chcesz zagrać jeszcze raz? y/n: ")
    if(x != "y" and x != "Y"):
        graj = False
