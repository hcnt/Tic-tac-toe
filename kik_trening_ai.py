from kik_plansza import *
from kik_kom import *
from kik_ai import *
import os

dna = [[8, 6], [2, 15], [15, 20], [15, 20], [12, 20],
       [2, 14], [4, 17], [12, 3], [2, 2], [3, 1]]


def wyswietl_plansze(plansza):
    print("-------------------")
    for i in range(len(plansza)):
        print("|  " + pionek(plansza[i][0]) + "  |  " +
              pionek(plansza[i][1]) + "  |  " + pionek(plansza[i][2]) + "  |")

        print("-------------------")


def partia(dna1, dna2):
    plansza = nowa_pusta_plansza()
    czy_ruch_wykonany = False
    czy_gra_skonczona = False
    gracz = 1
    wygrany_gracz = 0
    while(not czy_gra_skonczona):
        # print()
        # wyswietl_plansze(plansza)
        if(gracz == 1):
            wiersz, kolumna = wybierzRuch(plansza, gracz, dna1)
            # print(kom_ruch_przeciw(gracz, wiersz, kolumna))
        else:
            wiersz, kolumna = wybierzRuch(plansza, gracz, dna2)
            # print(kom_ruch_przeciw(gracz, wiersz, kolumna))

        czy_ruch_wykonany, plansza, gracz = wykonaj_ruch(
            plansza, gracz, wiersz, kolumna)

        czy_gra_skonczona, wygrany_gracz = koniec_gry(plansza)
    # wyswietl_plansze(plansza)
    print(kom_koniec(wygrany_gracz))
    return(wygrany_gracz)


def inizjalizacjaPopulacji(wielkosc):
    populacja = []
    for i in range(wielkosc):
        populacja.append(generujDna())
    return populacja


def crossover(dna1, dna2):
    dna = []
    for i in range(10):
        new = []
        for j in range(2):
            new.append((dna1[i][j] + dna2[i][j])/2)
        dna.append(new)
    return dna


def calculatePopulationFitness(population):
    populationFitness = []
    for i in range(len(population)):
        fitness = 0
        for j in range(len(population)):
            print("partia osobnika: " + str(i))
            fitness += ((partia(population[i], population[j]) + 1)**2)
        populationFitness.append(fitness)
    return populationFitness


def pickHighestFitness(fitness, population):
    highestIndex = 0
    for i in range(len(fitness)):
        if(fitness[i] > fitness[highestIndex]):
            highestIndex = i
    print(fitness[highestIndex])
    return population[highestIndex]


def mutacja(dna):
    return dna


def trening():
    populacja = inizjalizacjaPopulacji(500)
    fitness = calculatePopulationFitness(populacja)
    print(fitness)
    highest = pickHighestFitness(fitness, populacja)
    print(highest)


trening()
