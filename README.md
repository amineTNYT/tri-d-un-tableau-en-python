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
ALGORITHME:
Procedure tri_selection (@t:tab; n:entier)
Début
    Pour i de 0 à n-2 faire
        pMin ← i
        Pour j de i+1 à n-1 faire
            Si (t[j] < t[pMin]) alors
                pMin ← j
            Fin si
        Fin pour
        Si (i ≠ pMin) alors
            aux ← t[i]
            t[i] ← t[pMin]
            t[pMin] ← aux
        Fin si
    Fin pour                                                      
Fin
