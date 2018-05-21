import random

def wybierz_ruch(plansza,gracz):

    ruch_wybrany = False

    while(not ruch_wybrany):
        kolumna = random.randint(0,2)
        wiersz = random.randint(0,2)

        if(plansza[wiersz][kolumna] == 0):
            ruch_wybrany = True
            return wiersz, kolumna
