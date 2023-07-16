sudoku = [[ 0 , 4 , 0 , 8 , 0 , 0 , 6 , 0 , 0],
          [ 0 , 0 , 0 , 0 , 5 , 0 , 0 , 9 , 0],
          [ 0 , 5 , 9 , 4 , 0 , 0 , 0 , 3 , 0],
          [ 0 , 0 , 3 , 0 , 9 , 0 , 0 , 1 , 0],
          [ 0 , 9 , 0 , 0 , 1 , 0 , 0 , 7 , 0],
          [ 0 , 2 , 0 , 0 , 4 , 0 , 5 , 0 , 0],
          [ 9 , 0 , 4 , 6 , 0 , 7 , 2 , 5 , 0],
          [ 0 , 6 , 0 , 0 , 3 , 0 , 0 , 4 , 0],
          [ 0 , 0 , 5 , 0 , 0 , 4 , 0 , 8 , 0]]

# sudoku représente cette grille :              Numérotation des blocs          Numérotation des chiffres       Numérotation ligne/colonne      Position
#                                                                                                                   0 1 2 3 4 5 6 7 8
#           0 0 0   0 0 0   3 0 0                                                   0 1 2                       0                               0  1  2      3  4  5     6  7  8
#           0 0 0   0 0 9   0 6 0                   0       1       2               3 4 5                       1                               9 10 11     12 13 14    15 16 17
#           7 0 1   2 0 0   5 0 0                                                   6 7 8                       2
#                                                                                               
#           1 7 0   0 0 0   0 0 0                                                                               3
#           8 9 6   7 0 0   0 4 0                   3       4       5                                           4
#           0 0 0   5 0 0   0 0 0                                                                               5
#
#           0 2 0   0 0 0   0 0 8                                                                               6
#           9 0 0   0 5 0   2 0 0                   6       7       8                                           7
#           0 0 3   0 0 6   0 9 0                                                                               8                               72 73 74    75 76 77    78 79 80

# Vocabulaire : grille = ensemble de 9 blocs, constitués de 9 chiffres.

# Préparation des lignes
sudoku_ligne = sudoku.copy()

# Test absent sur ligne
# Renvoi Vrai si absent sur la ligne
def absentSurLigne(grille, numero_ligne, valeur):
    if valeur in grille[numero_ligne]:
        return False
    return True

def absentSurColonne(grille, numero_colonne, valeur):
    for numero_ligne in range(9):
        if valeur == grille[numero_ligne][numero_colonne]:
            return False
    return True

def absentDansBloc(grille, numero_bloc, valeur):
    debut_ligne = int(numero_bloc/3)*3
    fin_ligne = int(numero_bloc/3)*3 + 3
    debut_colonne = numero_bloc%3 * 3
    fin_colonne = numero_bloc%3 * 3 + 3
    for numero_ligne in range(debut_ligne, fin_ligne ):
        for numero_colonne in range( debut_colonne, fin_colonne ):
            if valeur == grille[numero_ligne][numero_colonne]:
                return False
    return True

def affiche(grille):
    for i in range(9):
        print(grille[i])
        if (i+1) % 3 == 0:
            print()

iteration = 0

# On va  utiliser le retour de la fonction pour nous indiquer si la grille est valide ou non.
# position = position du chiffre : de 0 à 80. ligne 0 de 0 à 8 etc...
def estValide(grille, position):
    global iteration
    iteration = iteration + 1
    # Si on est à la 82e case (on sort du tableau)
    if (position == 9*9):
        print("Arrivée en position finale : ")
        affiche(grille)
        return True
    
    # On récupère les coordonnées du chiffre
    i = int(position/9) # ligne de 0 à 8
    j = position % 9 # colonne de 0 à 8

    # on calcule le numéro de bloc
    numerobloc = int(i/3)*3 + int(j/3)

    # Si la case n'est pas vide, on passe à la suivante (appel récursif)
    if (grille[i][j] != 0):
        return estValide(grille, position + 1)
    
    # il nous faut énumérer tous les chiffres possibles, 
    # puis tester chaque solution éventuelle pour vérifier si elle nous amène à une solution correcte, ou bien à un blocage.
    # Mais attention ! 
    # Pour que les tests sur la grille puissent fonctionner, 
    # il faut veiller à actualiser la grille au cours de le descente récursive. 
    # Et c'est là que beaucoup se font piéger : il ne suffit pas d'enregistrer le choix effectué dans la grille avant de passer à l'appel suivant, 
    #  il faut aussi réinitialiser le chiffre de la case à zéro en cas d'échec.

    # énumération des valeurs possibles
    for k in [1,2,3,4,5,6,7,8,9]:
        # Si la valeur est absente, elle est donc autorisée
        if absentSurLigne(grille, i, k):
            if absentSurColonne(grille, j, k):
                if absentDansBloc(grille, numerobloc, k): 
                    # On enregistre k dans la grille
                    grille[i][j] = k
                    # On appelle récursivement la fonction estValide(), pour voir si ce choix est bon par la suite
                    if ( estValide(grille, position+1) ):
                        return True  # Si le choix est bon, plus la peine de continuer, on renvoie true :)
    # Tous les chiffres ont été testés, aucun n'est bon, on réinitialise la case
    grille[i][j] = 0
    # Puis on retourne false :(
    return False

print(estValide(sudoku, 0))

