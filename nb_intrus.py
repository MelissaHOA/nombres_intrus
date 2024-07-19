# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# Exercice 1.a : à la recherche du nombre intrus
# Écrire un programme qui détecte dans une liste contenant des nombres entiers
# non nuls des intrus qui sont des nombres négatifs ;
# le programme doit être composé des versions successives suivantes :
# """
#
#
# """
#     1. Demander à l’utilisateur chaque nombre constituant la liste ; par convention,
#     la saisie de 0 indique que la saisie de la liste est terminée
# """
#
# def intruders_numbers():
#
#     while True:
#         try:
#             number_list = str(input("Trouvez l'intrus : Veuillez saisir une liste de nombre entier séparé d'un espace. Ou saisir 0 pour terminer : "))
#
#             if number_list == "0":
#                 print("Fin du programme. Merci ! ")
#                 break
#
#             if len(number_list) == 0 : #Vérifie si la liste est vide
#                 print("Votre liste est vide", len(number_list))
#                 break
#             else:
#                 #Sépare chaque nombre en utilisant l'espace et crée une liste de valeurs entières
#                 number_list = [int(x) for x in number_list.split(" ")]
#             print("Votre liste est : ", number_list)
#
#
#
#         except ValueError:
#             print("Une des valeurs saisie n'est pas un nombre entier")
#
# intruders_numbers()