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

def f(l):
    return list(dict(zip(l,range(len(l))))), dict(zip(l,range(len(l))))
print(f([1,2,3,"t", "ttt", "tttttt", 1, 2, 3, "t", "ttt"]))