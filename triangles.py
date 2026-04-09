import module_triangle_prof

def generer_tous_les_triangles(n, afficher=False):
    """
    Génère tous les triangles binaires possibles de taille n.

    Paramètres :
        n (int) : Taille des triangles (doit être >= 2)
        afficher (bool) : Si True, affiche chaque triangle généré

    Retour :
        list : Liste contenant tous les triangles générés
    """
    assert isinstance(n, int) and n >= 2, "n doit être un entier >= 2"
    triangles = []
    lignes = listes_n(n)

    for ligne in lignes:
        triangle = generer_triangle(ligne)
        triangles.append(triangle)

        if afficher:
            print("Triangle pour :", ligne)
            afficher_triangle(triangle)

    return triangles
    
def listes_n(n):
    '''
    génère tous les listes binaires de longueurs n
    :param n (int)
    Exemple:
    >>> listes_n(1)
    [[0],[1]]
    '''
    Longueur=[]
    N=2**n
    for i in range(0,N):
       Longueur.append(rempli(bin(i),n))
    return Longueur

def rempli(bin,n):
    '''
    retourne la liste de nombre binaire bin de longueur n
    :param bin (str)
    :param n (int)
    Exemple:
        >>> rempli("Ob1001",5)
        [0,1,0,0,1]
    '''
    assert type(bin) == str, "On attend un paramètre de type str"
    assert type(n) == int, "On attend un paramètre de type int"
    L=[]
    if len(bin[2:])< n:
        for i in range(0,n-len(bin[2:])):
            L.append(0)
    for j in bin[2:]:
        L.append(int(j))
    return L

def est_complet(triangle):
    """
    Indique si un triangle binaire est complet
    Un triangle est complet si le nombre total de 0 et de 1 dans toutes les lignes est égal.
    Parametre :
        ligne : Liste contenant uniquement des 0 et des 1 représentant
        la première ligne du triangle, la base.
    Return :
        True : Si le triangle est complet
        False : Si le triangle est incomplet
   
    Exemple :
        >>> est_complet([1,0])
        Le triangle n'est pas complet
        >>> est_complet([1,1,1])
        Triangle complet
    """
    assert isinstance(ligne, list), "Le paramètre doit être une liste"
    assert len(ligne) >= 1, "La liste doit contenir au moins un élément"
    for i in range(len(liste)):
        assert liste[i] in (0,1), "Votre liste doit contenir uniquement des 0"




    cpmt_gen_0 = 0
    cpmt_gen_1 = 0
    for ligne in triangle:
        u = compteur_0_1(ligne)
        cpmt_gen_0 += u[0]
        cpmt_gen_1 += u[1]
    if cpmt_gen_0 == cpmt_gen_1:
        print("Triangle complet")
        return True
    else:
        print("Le triangle n'est pas complet")
        return False


def compteur_0_1(liste):
    """
    Compte le nombre de 0 et de 1 dans une liste binaire.
    Parametre :
        liste : Liste contenant uniquement des 0 et des 1.
    Return :
        tuple : (nombre_de_0, nombre_de_1)


    Exemple :
        >>> compteur_0_1([1,0,0,0,0,0,1,1,1])
        (5, 4)
        >>> compteur_0_1([0,0,0])
        (3, 0)
    """
    assert isinstance(liste, list), "Le paramètre doit être une liste"
    assert len(liste) >= 1, "La liste doit contenir au moins un élément"
    for i in range(len(liste)):
        assert liste[i] in (0,1), "Votre liste doit contenir uniquement des 0"


    cpmt_0 = 0
    cpmt_1 = 0
    for val in liste:
        if val == 0:
            cpmt_0 += 1
        else:
            cpmt_1 += 1
    return cpmt_0, cpmt_1

def trian_complet(n):
    '''
    retourne tous les triangles binaires complets de longueur n
    :param n (int)
    '''
    assert type(n) == int, "On attend un paramètre int"

    L= generer_tous_les_triangles(n, afficher=False)
    for list in L:
        if est_complet(list):
            afficher_triangle(list)

