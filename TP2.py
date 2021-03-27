# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:28:14 2021

@author: antoc
"""
from math import sin
from math import log #sur python log=ln
from math import acos
from math import exp
from math import atan

def g0 (x):
    return (1+sin(x))/2 #test du programme point fixe ave  la fonction étudié au TP1
def g1 (x):
    return (9-3*x)**(1/4) #g(x) pour la 1)
def i2g1 (x):
    return -((9-3*x)**(1/4)) #-g(x) pour la 1)
def g2(x):
    return acos((2+x)/3) #g(x) pour la 2)
def g3 (x):
    return(log(7/x)) #g(x) pour la 3)
def g4 (x):
    return exp(x)-10 #g(x) pour la 4)
def g5 (x):
    return atan((x+5)/2) #g(x) pour la 5)
def g6 (x):
    return log(x**2 +3) #g(x) pour la 6)
def g7 (x):
    return ((7-4*log(x))/3) #g(x) pour la 7)
def g8 (x):
    return (2*x**2-4*x+17)**(1/4) #g(x) pour la 8) 
def i2g8 (x):
    return -(2*x**2-4*x+17)**(1/4) #-g(x) pour la 8)
def g9 (x):
    return log(2*sin(x)+7) #g(x) pour la 9)
def g10 (x):
    return log(10/log(x**2 +4)) #g(x) pour la 10)


def ptf(g,X0,epsilon,Nitermax):
    """ Programme du point fixe qui compare l'ecart entre g(xn)[xold] et g(xn+1) [xnew] 
    cet écart est comparé à epsilon qui nous permet de définir la précision 
    de la solution g(alpha)=alpha
    on inplémente aussi un compteur d'itération pour sorir de la boucle si il n'y a pas de solution trouvé au bout de Niermax essai
    cela nous permet aussi de savoir à quelle vitesse la méthode du point fixe trouve alpha 
    """
    n=0
    xold=X0
    xnew=1
    erreur=g(xold)-xold
    while abs(erreur)>epsilon and n<Nitermax:
        xnew=g(xold)
        n+=1
        erreur=xnew-xold
        xold=xnew
        print(n)
    return xnew

print(ptf(g0,1,1e-10,5e4))   # affiche alpha et le nombre d'itération pour le test avec la fonction du TP1

print(ptf(g1,1,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 1)

print(ptf(i2g1,-1.9,1e-10,5e4))   # affiche  le second alpha et le nombre d'itération pour la 1)

print(ptf(g2,0.54,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 2)

print(ptf(g3,1.5,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 3)

print(ptf(g4,2.5,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 4)

print(ptf(g5,1.25,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 5)

print(ptf(g6,1.9,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 6)

print(ptf(g7,1.5,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 7)

print(ptf(g8,2,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 8)

print(ptf(i2g8,-2,1e-10,5e4))   # affiche le second alpha et le nombre d'itération pour la 8)

print(ptf(g9,1.8,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 9)

print(ptf(g10,2,1e-10,5e4))   # affiche alpha et le nombre d'itération pour la 10)