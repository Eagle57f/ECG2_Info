# I.Exercices

# 1)

n=0 # int(input("n:"))
l=[i**3 for i in range(n+1)]
print(l)
print(sum(l)) # Parfois interdit, donc il faut utiliser le programme suivant:
s=0
for i in l:
    s+=i
print(s)


# 2)

def f(l):
    return [1/i for i in l if i!=0]
print(f(range(30))) # Exemple pour la liste des entiers entre 0 et 29


# 3)

# Version "normale":

def f(n,c):
    S=0
    for i in range(len(n)):
        S+=n[i]*c[i]
    return S/len(n)
print(f([19,12,7,20], [1,2,4,1]))

# Version en une ligne (difficle à comprendre):

def f(n,c):
    return sum([i*j for i,j in zip(n,c)])/len(n)
print(f([19,12,7,20], [1,2,4,1]))

# 4)

def f(l,i,j):
    if i in range(len(l)) and j in range(len(l)):
        l[i], l[j] = l[j], l[i]
        return l
    return "Impossible"
print(f([1,2,3,4,5,6], 2, 4))

# 5)

def f(l:list,x):
    for _ in range(l.count(x)):
        l.remove(x)
    return l
print(f([1,2,3,4,5,4,3,2,1,2,3,4,5,6,1,1,1,1], 1))

# 6)

def f(l:list, x, i):
    l.insert(i,x)
    return l
print(f([1,2,3,4,5,4,3,2,1,2,3,4,5,6,1,1,1,1], "ttttt", 3))

# 7)

def f(l):
    return max(l), l.count(max(l))
print(f([1,2,3,4,5,4,3,2,1,2,3,4,5,1,1,1,1]))

# 8)

# Version "normale":

def f(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2
print(f([1,2,3,"t", "ttt", "tttttt", 1, 2, 3, "t", "ttt"]))

# Version en une ligne (difficle à comprendre, mais très efficace):

def f(l):
    return list(dict(zip(l,range(len(l)))))
print(f([1,2,3,"t", "ttt", "tttttt", 1, 2, 3, "t", "ttt"]))

# 9)

def f(l):
    x,y=l[0],l[1]
    for i in l:
        for j in l:
            if abs(i-j)<abs(x-y) and i!=j:
                x,y=i,j
    return x,y
print(f([1,3,6,8,10,15,18,20,25,30,35,40,45,50]))


# 10)
def f(n):
    S=0
    for i in range(n+1):
        for j in range(n+1):
            if i<j:
                S+=i+j
    return S
print(f(4))

# II. Quelques extraits de concours

# Ex 1:
from math import factorial
import matplotlib.pyplot as plt

n=100

def u(n):
    return factorial(n)/(n**n)

# plt.plot([u(i) for i in range(0,n+1)], range(0,n+1))
# plt.show()

# Ex 2:
import matplotlib.pyplot as plt

N=10
def f(n,x):
    return x**n+x-1
x=range(0,1*1000)
x=[i/1000 for i in x]


for n in range(1,N+1):
    y=[f(n,i) for i in x]
    x0=x[0]
    for i in x:
        if abs(f(n,i))<abs(f(n,x0)):
            x0=i
    plt.plot(x,y)
    plt.annotate(f"X", xy=(x0, f(n,x0)), color="red", verticalalignment="center", horizontalalignment="center")

plt.show()


# Ex 3

# a)

from math import sqrt
def u(n):
    return 0 if n==0 else 1 if n==1 else u(n-1)+u(n-2)
print(u(10))

# b)

n=1
while abs(u(n+1)/u(n)-(1+sqrt(5))/2)>10**-10:
    n+=1
print(u(n), n)


# Ex 4

# a)

from math import sqrt # Ou de numpy

u = 1
S = u
n = 0

while S < 1000:
    n += 1
    u = sqrt(u**2 + u)
    S += u
print(n)



n = 0
while (n**2)/4 < 1000:
    n += 1
print(n) # valeur approchée de n

# Ex 5
def calcul(n):
    I=1 # Valeur de I_0
    for k in range(1, n+1):
        I = I * (2*k*(2*k-1)/((2*k)**2+1))
    return I

# Pour afficher le graphique (pas demandé):
import matplotlib.pyplot as plt
N=200
plt.scatter(range(1,N+1),[sqrt(i)*calcul(i) for i in range(1,N+1)], marker='+', color='green', s=15, linewidths=0.7)
plt.show()