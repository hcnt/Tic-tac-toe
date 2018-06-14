import tkinter as tk
from plan_ix import Window
from kik_plansza import *
from kik_ai_los import wybierz_ruch
okno = Window("XO")

okno.vars.plansza = nowa_pusta_plansza()
okno.vars.gracz = None
okno.vars.tryb = None
okno.vars.czyGraTrwa = False
okno.vars.pionekGracza = None
okno.vars.planszaStartRow = 8
okno.vars.planszaStartCol = 0



def setup(app,name,row,col):
    if(not app.vars.czyGraTrwa):
        ktoZaczyna = app.getR("ktoZaczyna")
        tryb = app.getR("wybierzTryb")
        kimGraGracz = app.getR("kimGra")

        if(ktoZaczyna == "X"):
            okno.vars.gracz = 1
        else:
            okno.vars.gracz = -1

        if(tryb == "Człowiek vs Człowiek"):
            okno.vars.tryb = 1
        else:
            okno.vars.tryb = -1
        
        if(kimGraGracz == "X"):
            okno.vars.pionekGracza = 1
        else:
            okno.vars.pionekGracza = -1

        if(okno.vars.pionekGracza != okno.vars.gracz and okno.vars.tryb == -1):
            graj(app,name,row,col)

        togglePolaState("normal")

        app.vars.czyGraTrwa = True

        app.config(name = name,text = "Stop")
    else:
        okno.vars.plansza = nowa_pusta_plansza()
        togglePolaState("disabled")
        app.vars.czyGraTrwa = False
        app.config(name = name,text = "Start")
        resetImages()



def graj(app,name,row,col):

    plansza = app.vars.plansza

    cellRow = (row - app.vars.planszaStartRow)//2
    cellCol = (col - app.vars.planszaStartCol)//2

    if(plansza[cellRow][cellCol] == 0):
        if(app.vars.pionekGracza == app.vars.gracz or app.vars.tryb == 1):
            plansza[cellRow][cellCol] = app.vars.gracz
            app.config(row = row,col = col, image = str(app.vars.gracz) + ".gif")
            okno.vars.gracz *= -1

        czyGraZakonczona, wygranyGracz = koniec_gry(plansza)
        
        if(app.vars.tryb == -1 and app.vars.pionekGracza != app.vars.gracz and not czyGraZakonczona):
            guessRow, guessCol = wybierz_ruch(plansza,app.vars.gracz)
            plansza[guessRow][guessCol] = app.vars.gracz

            row = guessRow * 2 + app.vars.planszaStartRow 
            col = guessCol * 2  + app.vars.planszaStartCol 

            app.config(row = row,col = col, image = str(app.vars.gracz) + ".gif")
            okno.vars.gracz *= -1
    
        
    czyGraZakonczona, wygranyGracz = koniec_gry(plansza)
    
    if(czyGraZakonczona):
        togglePolaState("disabled")


def togglePolaState(value):
    startRow = okno.vars.planszaStartRow
    startCol = okno.vars.planszaStartCol
    for i in range (startRow,startRow+3*2,2):
         for j in range (startCol,startCol+3*2,2):
             okno.config(row = i, col = j, state = value)

def resetImages():
    startRow = okno.vars.planszaStartRow
    startCol = okno.vars.planszaStartCol
    for i in range (startRow,startRow+3*2,2):
         for j in range (startCol,startCol+3*2,2):
             okno.config(row = i, col = j, image = "pusty.gif")



def dodajPola(row,col,colspan,rowspan):
    for i in range(3):
        for j in range(3):
            okno.add("B",image = "pusty.gif",
                     row = row + i * rowspan,
                     col = col + j * rowspan ,
                     colspan = colspan,
                     rowspan = rowspan,command=graj)


def toggleKimGra(app,name,row,col):
    if(app.getR("wybierzTryb") == "Człowiek vs Człowiek" ):
        app.config(name = "kimGraX",state = "disabled")
        app.config(name = "kimGraY",state = "disabled")
        app.config(name = "kimGra",fg = "grey")
    else:
        app.config(name = "kimGraX",state = "normal")
        app.config(name = "kimGraY",state = "normal")
        app.config(name = "kimGra",fg = "black")
        

def stworzOkno():
    
    okno.add("L",text = "Wybierz tryb", name = "tryb",row = 0,col = 2,colspan = 2,width = 10)
    okno.add('R', text = "Człowiek vs Komputer",radio_group = "wybierzTryb", name = "CvK",
             row = 1,col = 1,colspan = 4,command = toggleKimGra)
    okno.add('R', text = "Człowiek vs Człowiek",radio_group = "wybierzTryb", name = "CvC",
             row = 2,col = 1,colspan = 4,command = toggleKimGra)

    okno.add("L",text = "Kim chcesz grać?", name = "kimGra",row = 3,col = 1,colspan = 4,width = 20)
    okno.add('R', text = "X",radio_group = "kimGra", name = "kimGraX",row = 4,col = 2)
    okno.add('R', text = "O",radio_group = "kimGra",name = "kimGraY",row = 4,col = 3)

    okno.add("L",text = "Kto zaczyna?", name = "ktoZaczyna",row = 5,col = 2,colspan = 2,width = 10)
    okno.add('R', text = "X",radio_group = "ktoZaczyna",row = 6,col = 2)
    okno.add('R', text = "O",radio_group = "ktoZaczyna",row = 6,col = 3)

    okno.add('B', text = "Start",name = "start/stop",row = 7,col = 1,colspan = 4, width = 20,command=setup)

    dodajPola(okno.vars.planszaStartRow,okno.vars.planszaStartCol,2,2)
    
    togglePolaState("disabled")

    
    
    okno.start()


stworzOkno()
