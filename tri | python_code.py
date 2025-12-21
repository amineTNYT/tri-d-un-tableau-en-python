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
 
# Fonction de tri du tableau (tri par sélection)
def tri_seléction(t, n):
    # Parcourir tous les éléments du tableau
    for i in range(n-1):
        # Position du minimum actuel
        pMin = i
        # Chercher le minimum dans la partie non triée
        for j in range(i+1, n):
            if t[j] < t[pMin]:
                pMin = j
        # Échanger les éléments si nécessaire
        if i != pMin:
            aux = t[i]
            t[i] = t[pMin]
            t[pMin] = aux    
            
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
