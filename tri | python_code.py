from numpy import array

# procédure pour saisir et valider la taille du tableau
def sasir():
    n=int(input("Donner le taille du tableau=:"))
    while not (3<=n<=5):
        n=int(input("Donner taille du tableau=:"))
    return n

# procédure  pour remplir le tableau avec des valeurs saisies par l'utilisateur
def remplir(t,n):
    for i in range(0,n):
        t[i]=int(input("t["+str(i)+"]=:"))
 
# procédure de tri utilisant l'algorithme de tri par sélection
def tri(t,n):
    for i in range(n):
        for j in range(i+1,n):
            if t[i]>t[j]:
                aux=t[j]
                t[j]=t[i]
                t[i]=aux
    
            
# procédure pour afficher les éléments du tableau séparés par "|"
def afficher(t,n):
    for i in range(0,n):
        print(t[i],end="|")
   
 
# Programme Principal
n=sasir()  # Saisie de la taille du tableau
t=array([int()]*n)  # Création du tableau avec NumPy
remplir(t,n)  # Remplissage du tableau

# Affichage du tableau avant le tri
print("le tableau avant le tri")
afficher(t,n)
print()

tri(t,n)  # Tri du tableau

# Affichage du tableau après le tri
print("le tableau aprés le tri")
afficher(t,n)
