from kik_plansza import *
from kik_kom import *
from kik_ai_los import *


def wyswietl_plansze(plansza):
    print("-------------------")
    for i in range(len(plansza)):
        print("|  " + pionek(plansza[i][0]) + "  |  " +
              pionek(plansza[i][1]) + "  |  " + pionek(plansza[i][2]) + "  |")

        print("-------------------")


## tryb 0 - człowiek vs człowiek
## tryb 1 - człowiek vs komputer
## tryb 2 - komputer vs komputer

def partia(tryb,pierwszy_gracz):

    plansza = nowa_pusta_plansza()
    czy_ruch_wykonany = False
    czy_gra_skonczona = False
    gracz = pierwszy_gracz
    wygrany_gracz = 0
    while(not czy_gra_skonczona):
        wyswietl_plansze(plansza)
        print(plansza)
        print(kom_ruch(gracz))
        if(tryb == 0 or (tryb == 1 and gracz == pierwszy_gracz)):
            wiersz = int(input("podaj wiersz: "))
            kolumna = int(input("podaj kolumne: "))
        else:
            wiersz, kolumna = wybierz_ruch(plansza,gracz)
            print(kom_ruch_przeciw(gracz, wiersz, kolumna))

        czy_ruch_wykonany, plansza, gracz = wykonaj_ruch(
            plansza, gracz, wiersz, kolumna)

        if(not czy_ruch_wykonany):
            print(kom_zly_ruch())

        print(plansza)
        czy_gra_skonczona, wygrany_gracz = koniec_gry(plansza)
    
    print(kom_koniec(wygrany_gracz))


def gra():
    graj = True
    print("tryb 0 - człowiek vs człowiek")
    print("tryb 1 - człowiek vs komputer")
    print("tryb 2 - komputer vs komputer")
    tryb = int(input("Wybierz tryb (0,1,2): "))
    print()
    print("O: -1")
    print("X: 1")
    
    gracz1 = int(input("czym chcesz zaczynać? -1/1: "))
    
    
    while(graj):    
        partia(tryb,pierwszy_gracz)
        x = input("Czy chcesz zagrać jeszcze raz? y/n: ")
        if(x != "y" and x != "Y"):
            graj = False





gra()



