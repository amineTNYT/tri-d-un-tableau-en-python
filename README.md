# Algorithme de Tri par Sélection
par{amineTNYT}

Programme Python qui implémente le tri par sélection pour ordonner un tableau d'entiers.

## Exemple d'exécution :
Donner le taille du tableau: 4
t[0]=: 9
t[1]=: 2
t[2]=: 7
t[3]=: 1

le tableau avant le tri
9|2|7|1|

le tableau après le tri
1|2|7|9|
from numpy import array

# Algorithme de Tri par Sélection - Développé par [Votre Nom]
def sasir():
    n=int(input("Donner le taille du tableau=:"))
    while not (3<=n<=5):
        n=int(input("Donner taille du tableau=:"))
    return n

def remplir(t,n):
    for i in range(0,n):
        t[i]=int(input("t["+str(i)+"]=:"))
 
def tri(t,n):
    for i in range(n):
        for j in range(i+1,n):
            if t[i]>t[j]:
                aux=t[j]
                t[j]=t[i]
                t[i]=aux
            
def afficher(t,n):
    for i in range(0,n):
        print(t[i],end="|")

# Programme Principal - Tri par Sélection
n=sasir()
t=array([int()]*n)
remplir(t,n)
print("le tableau avant le tri")
afficher(t,n)
print()
tri(t,n)
print("le tableau aprés le tri")
afficher(t,n)
