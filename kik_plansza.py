def nowa_pusta_plansza():
    tab = []
    for i in range(3):
        col = [0, 0, 0]
        tab.append(col)
    return tab


def zamienRuch(ruch):
    if(ruch == 1):
        return -1
    else:
        return 1


def wykonaj_ruch(plansza, czyj_ruch, wiersz, kolumna):
    if(wiersz > 2 or kolumna > 2 or plansza[wiersz][kolumna] != 0):
        return False, plansza, czyj_ruch

    plansza[wiersz][kolumna] = czyj_ruch

    return True, plansza, zamienRuch(czyj_ruch)


def czy_cala_plansza_zapelniona(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if(plansza[i][j] == 0):
                return False
    return True


def koniec_gry(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if(plansza[0][j] == plansza[1][j] == plansza[2][j] and plansza[0][j] != 0):
                return True, plansza[0][j]

        if(plansza[i][0] == plansza[i][1] == plansza[i][2] and plansza[i][0] != 0):
            return True, plansza[i][0]

    if((plansza[0][0] == plansza[1][1] == plansza[2][2] or plansza[0][2] == plansza[1][1] == plansza[2][0]) and plansza[1][1] != 0):
        return True, plansza[1][1]

    if(czy_cala_plansza_zapelniona(plansza)):
        return True, 0

    return False, 0
