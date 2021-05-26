from random import randint

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

def gainMoyen(mise, n):
    gainTotal = 0
    for i in range(n):
        gainTotal += jeu(mise)
    return gainTotal/n

def esperance(X, P):
    E = 0
    for i in range(len(X)):
        E += X[i] - P[i]
    return E

def ecartType(X, P):
    E = esperance(X, P)
    V = 0
    for i in range(len(X)):
        V += P[i] * (X[i] - E) ** 2
    return V ** 0.5

mise = 10
X = [mise, 6, -mise]
P = [1/8, 7/16, 7/16]
