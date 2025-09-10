# Merci à Bérénice pour avoir recopié la correction du prof
#
# Date de dernière mise à jour de la correction: 03.09.2025
# ===========================================================



import numpy as np  # pour calcul matriciel
import matplotlib.pyplot as plt  #ma biblio pour la représenta graphique en 2D
from math import*

#Exo 1

#1) Correction

#version1
n=int(input('Donner un entier naturel n:'))
L=[k**3 for k in range (n+1)]
S=sum(L)
print("La liste L est",L,"et la somme est",S)


#version 2

n=int(input('Donner un entier naturel n:'))
L=[]  #liste vide
s=0
for k in range(n+1):
    L=L+[k**3]  #construction d'une liste à l'aide d'une concaténation
    s=s+k**3  # calcul de la somme

#2)  Correction

#version 1

def inverse1(L):
    M=[1/k for k in L if k!=0]
    return M
    
#version 2

def inverse2(L):
    L_inv=[]
    for k in L:
        if k!=0:
            L_inv.append(1/k)
    return L_inv


#3)

#version 1
n=int(input('le nmbre de notes est:'))
notes=[]
listecoeffs=[]  #initialisation de la liste
Sprod=0  #initialisation de la somme
Scoeffs=0
for k in range(n):
    print('note', k+1,' :')
    note=float(input(' '))
    print('Coef', k+1, ' :')
    coeff=float(input(' '))
    Scoeffs= Scoeffs+coeff
    Sprod= Sprod+note*coeff
print("La moyenne est ", Sprod/Scoeffs)


#version 2

notes= eval(input('donner la liste des notes:'))
listecoeffs=eval(input('Donner la liste des coefs:'))
S=0
for k in range (len(notes)):
    S=S+notes[k]*listecoeffs[k]
    M=S/sum(listecoeffs, notes)
print("La moyenne est", M)


#4)

def echange(L,i,j):
    if 0<=i<=len(L)-1 and 0<=j<=len(L)-1:
        #les indices vont de 0 à longueur -1
        L[i], L[j]=L[j]=L[i]
    else:
        L='changer i ou j'
    return L
    
    
    
def echange2(L,i,j):
    if 0 <=i<=len(L)-1 and 0<=j<=len(L)-1:
        X=L[i]
        L[i]=L[j]
        L[j]=X
    else:
        L="changer l'un des argument-s i ou j"
    return L
    
