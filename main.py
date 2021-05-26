from random import randint
from turtle import *

def jeu(mise):
    lancer1 = randint(1, 8)
    if lancer1 == 1:
        gain = mise
    else:
        lancer2 = randint(1,8)
        if lancer2 <= 4:
            gain = 6
        else:
            gain = 0
    return gain

def simNJeux(mise, n):
    resultat = {}
    for i in range(n):
        gain = jeu(mise)
        if gain in resultat:
            resultat[gain] += 1
        else:
            resultat[gain] = 1
    return resultat

def gainMoyen(mise, n):
    gainTotal = 0
    for i in range(n):
        gainTotal += jeu(mise)
    return gainTotal/n

def esperance(X, P):
    E = 0
    for i in range(len(X)):
        E += X[i] * P[i]
    return E

def ecartType(X, P):
    E = esperance(X, P)
    V = 0
    for i in range(len(X)):
        V += P[i] * ((X[i] - E) ** 2)
    return V ** 0.5

def visualisationJeux(resultats):
    n = 0
    Nomsresultats = []
    for resultat in resultats:
        n += resultats[resultat]
        Nomsresultats.append(resultat)
    Nomsresultats = sorted(Nomsresultats)
    setup(startx=0, starty=0)
    title("Pour {} parties".format(n))
    tracer(0, 0)
    speed(0)
    setworldcoordinates(-5, -5, 110, 110)
    forward(100)
    setpos(0, 0)
    left(90)
    forward(100)
    setpos(0, 0)
    right(90)
    for resultat in Nomsresultats:
        forward(90 / len(resultats) - 10)
        left(90)
        forward((resultats[resultat] * 100) / n)
        right(90)
        forward(5)
        penup()
        left(90)
        forward(5)
        write(resultat, align="center")
        left(180)
        forward(5 + (((resultats[resultat] * 100) / n) / 2))
        write(resultats[resultat], align="center")
        left(180)
        forward(((resultats[resultat] * 100) / n) / 2)
        right(90)
        pendown()
        forward(5)
        right(90)
        forward((resultats[resultat] * 100) / n)
        left(90)
    hideturtle()
    update()
    done()

mise = 10
X = [mise, 6, -mise]
P = [1/8, 7/16, 7/16]

resultats = simNJeux(10, 1000)

visualisationJeux(resultats)