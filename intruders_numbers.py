#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercice 1.a : à la recherche du nombre intrus
Écrire un programme qui détecte dans une liste contenant des nombres entiers
non nuls des intrus qui sont des nombres négatifs ;
le programme doit être composé des versions successives suivantes :
"""


"""
    1. Demander à l’utilisateur chaque nombre constituant la liste ; par convention, 
    la saisie de 0 indique que la saisie de la liste est terminée
"""

def intruders_nbr():

    user_number_list = []

    while True :
        try:

            user_number = int(input("Trouvez l'intrus : Veuillez saisir un nombre entier : "))

            # if user_number != 0:
            #     user_number_list.append(user_number)
            #
            # else:
            #     print(user_number_list)
            #     break
            #
            # if user_number < 0:
            #     print("Un intrus a été détecté : ", user_number)

            if user_number == 0:
                break
            elif user_number < 0:
                print("Un intrus a été détecté : ", user_number)







        except ValueError:
            print("La valeur saisie n'est pas valide")

intruders_nbr()