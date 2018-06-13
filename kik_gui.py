from plan_ix import Window
okno = Window("XO")

def dodajPola(row,col,colspan,rowspan):
    for i in range(3):
        for j in range(3):
            okno.add("B",image = "pusty.gif",
                     row = row + i * rowspan,
                     col = col + j * rowspan ,
                     colspan = colspan,
                     rowspan = rowspan)

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

    okno.add('B', text = "Start",row = 7,col = 1,colspan = 4, width = 20)

    dodajPola(8,0,2,2)


stworzOkno()
