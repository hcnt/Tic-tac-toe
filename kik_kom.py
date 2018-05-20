def pionek(wartosc):
    if(wartosc == 0):
        return " "
    elif(wartosc == -1):
        return "X"
    elif(wartosc == 1):
        return "O"

def kom_zly_ruch():
    return "zły ruch"

def kom_koniec(kto):
    if(kto == 0):
        return "Remis!"
    else:
        return pionek(kto) + " wygrał!"  

def kom_ruch(kto):
    return "Ruch gracza %s" % pionek(kto) 

def kom_ruch_przeciw(kto, wiersz, kolumna):
    return "Przeciwnik (%s) wykonuje ruch: %d, %d " % (pionek(kto), wiersz, kolumna) 
