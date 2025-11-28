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
ALGORITHME de tri:


## Tableau de Déclaration des Objets locaux (TDOL)

| Objet | Type/Nature |                          |
|-------|-------------|-------------------------------|
| i     | entier |     
| j     | entier | 
| pMin  | entier |     
| aux   | entier | 
**Note Importante sur la Variable `aux` :**

La déclaration de `aux` **dépend du type des éléments dans le tableau `t`**.

Si `t` contient :
- **Entiers** → `aux` doit être `entier`
- **Caractères** → `aux` doit être `caractère`
- **Chaînes de caractères** → `aux` doit être `chaine`
- **Nombres réels** → `aux` doit être `réel`
- **Objets personnalisés** → `aux` doit correspondre au type d'objet

**Exemple :**
```pascal
// Pour un tableau d'entiers
aux: entier

// Pour un tableau de caractères
aux: caractère

// Pour un tableau de nombres réels
aux: réel
```

**Toujours déclarer `aux` avec le même type de données que les éléments du tableau** pour éviter les erreurs de type lors des opérations d'échange.


