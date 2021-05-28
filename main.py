from random import randint
from turtle import *
import turtle
from tkinter import *
from PIL import Image
import os

#Fonctions

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
    screensize(1000, 1000)
    title("Pour {} parties".format(n))
    tracer(0, 0)
    setworldcoordinates(-5, -5, 110, 110)
    forward(100)
    pen(pensize=3)
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
        write(resultat, align="center", font=("Calibri", 16, "bold"))
        left(180)
        forward(5 + (((resultats[resultat] * 100) / n) / 2))
        write(resultats[resultat], align="center", font=("Calibri", 16, "bold"))
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
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file=("visu.eps"))
    imgEPS = Image.open("visu.eps")
    converted = imgEPS.convert('RGBA')
    converted.save("visu.png")
    converted.close()
    imgEPS.close()
    os.remove("visu.eps")
    done()

#Variables

#mise = int(input("Entrer la mise: "))
mise = 10
X = [mise, 6, -mise]
P = [1/8, 7/16, 7/16]

#Programme principale

resultats = simNJeux(10, 10000)

visualisationJeux(resultats)