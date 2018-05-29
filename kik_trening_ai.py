from kik_plansza import *
from kik_kom import *
from kik_ai import *
import os
import random

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
    # print(kom_koniec(wygrany_gracz))
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
        # print("partia osobnika: " + str(i))
        fitness = 0
        for j in range(len(population)):
            fitness += (5**(partia(population[i], population[j]) + 1))
        populationFitness.append(fitness)
    return populationFitness


def pickHighestFitness(fitness, population):
    highestIndex = 0
    for i in range(len(fitness)):
        if(fitness[i] > fitness[highestIndex]):
            highestIndex = i
    return highestIndex


def pickWeightedRandomDna(fitness, population):
    while(True):
        randomIndex = random.randint(0, len(population)-1)
        if (random.uniform(0, fitness[pickHighestFitness(fitness, population)]) < fitness[randomIndex]):
            return population[randomIndex]


def mutacja(dna, percentage):
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            if(random.uniform(0, 1) < percentage):
                dna[i][j] += random.randint(-1, 1)
    return dna


def makeNewPopulation(fitness, population):
    newPopulation = []
    for i in range(len(population)):
        parent1 = pickWeightedRandomDna(fitness, population)
        parent2 = pickWeightedRandomDna(fitness, population)
        child = mutacja(crossover(parent1, parent2), 0.01)
        newPopulation.append(child)

    return newPopulation


def trening(liczbaPokolen):
    population = inizjalizacjaPopulacji(600)
    fitness = calculatePopulationFitness(population)

    for i in range(liczbaPokolen):
        population = makeNewPopulation(fitness, population)
        fitness = calculatePopulationFitness(population)
        print(i)
        print(population[pickHighestFitness(fitness, population)])
        print(fitness[pickHighestFitness(fitness, population)])


trening(100)
