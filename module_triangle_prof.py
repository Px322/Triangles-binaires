# _*_ coding: utf-8 _*_
'''
    génération et affichage d'un triangle binaire
'''
def generer_triangle(ligne_depart):
    ''' 
    renvoie un triangle binaire complet à partir de la ligne de départ passée en paramètre
    : param ligne_depart(list)
    Exemple :
        >>> generer_triangle([1,0])
        [[1,0],[1]]
        >>> generer_triangle([0,0,0])
        [[0,0,0],[0,0],[0]]
    '''
    assert type(ligne_depart) == list, "On attend un paramètre de type list"
    assert len(ligne_depart) >= 2, "La liste doit contenir au moins deux éléments"
    for i in ligne_depart :
        assert (i == 0 or i == 1),"La liste doit contenir des zéros ou des uns"
   
    triangle = [ligne_depart]
    ligne_courante = ligne_depart
    while (len(ligne_courante) >= 2) :
        ligne_courante = __generer_ligne_suivante(ligne_courante)
        triangle.append(ligne_courante)
    return triangle
        
 

def afficher_triangle(triangle):
    '''
    affiche le triangle dans la console
    : param triangle(list)
    : pas de return, pas d'effet de bord
    '''
    '''assert isinstance(triangle,list), "on attend un paramètre de type list"
    for ligne_triangle in triangle :
        for valeur in ligne_triangle :
            assert valeur == 0 or valeur == 1,"La liste doit contenir des 0 ou 1"
    '''
    try :
        for ligne in triangle :
            print(ligne)
    except :
        raise Exception("paramètre incorrect")
        
def __ou_exclusif(bit1, bit2):
    '''
    renvoie le résultat du ou exclusif sur deux bits
    bit1, bit2 : 0 ou 1
    sortie bit_res : 0 ou 1
    Exemples :
        >>> ou_exclusif(0,0)
        0
        >>> ou_exclusif(1,0)
        1
        >>> ou_exclusif(1,1)
        0
    '''
    return (bit1 + bit2)%2

def __generer_ligne_suivante(ligne_precedente):
    ''' 
    renvoie la ligne suivante dans un triangle binaire
    ligne_precedente : liste de 0 ou 1, de taille supérieure ou égale à 2
    ligne_suivante : une liste de 0 ou 1
    Exemples :
        >>> generer_ligne_suivante([0,1,0,1])
        [1,1,1]
        >>> generer_ligne_suivante([0,0,0,1,1,1])
        [0,0,1,0,0]
    '''
    ligne_suivante = []
    for i in range(len(ligne_precedente)-1):
        ligne_suivante.append(__ou_exclusif(ligne_precedente[i],ligne_precedente[i+1]))
    return ligne_suivante
                              
                              
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    triangle1 = generer_triangle([0,0,1,0,0,1,1,0,1,0,0])
    afficher_triangle(triangle1)
        
    
    