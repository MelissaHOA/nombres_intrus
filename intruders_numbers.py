#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 1.a : à la recherche du nombre intrus
# Écrire un programme qui détecte dans une liste contenant des nombres entiers
# non nuls des intrus qui sont des nombres négatifs
#
# Exercice 1.b : mise en fonction de la recherche du nombre intrus
# Il sera continué dans le même projet PyCharm et hébergé par le même dépôt Git.
#

def input_list_numbers():
    """Fonction pour saisir une liste de nombres entiers de départ, (0 pour terminer) """
    user_number_list = []
    while True:
        try:
            user_number = int(input("Trouvez l'intrus : Veuillez saisir un nombre entier : (0 pour terminer) : "))
            if user_number == 0:
                break
            user_number_list.append(user_number)
        except ValueError:
            print("La valeur saisie n'est pas valide. Veuillez saisir un nombre entier. ")
    return user_number_list


def detect_numbers_intruder(user_number_list):
    """Fonction pour détecter et afficher les intrus, et retourner la liste sans intrus."""
    count_intruders = 0
    intruders_list = []
    number_positif_list = []

    for user_number in user_number_list:
        if user_number > 0:
            number_positif_list.append(user_number)
        elif user_number < 0:
            count_intruders += 1
            intruders_list.append(user_number)

    if count_intruders == 0:
        print(f"Vous n'avez pas trouvé d'intrus. Voici les nombres saisi : {user_number_list}")
    else:
        print(f"Le nombre d'intrus détecté est de : {count_intruders} , voici la liste : {intruders_list}")
    print(f"Les nombres sans intrus sont : {number_positif_list}")
    print(f"Tous les nombres saisi sont : {user_number_list}")

    return number_positif_list


def main():
    """ Jeux trouver l'intrus : fonction principal  """
    user_number_list = input_list_numbers()
    detect_numbers_intruder(user_number_list)


if __name__ == "__main__":
    main()

# def game_find_intruder():
#     """ Jeux trouver l'intrus : fonction principal  """
#     user_number_list = input_list_numbers()
#     detect_numbers_intruder(user_number_list)
#
#
# if __name__ == "__main__":
#     game_find_intruder()
#
#
# ______________________________________________
#

#
# def intruders_nbr():
#     user_number_list = []
#     count_intruders = 0
#     intruders_list = []
#     number_positif_list = []
#
#     """Demande à l'utilisateur de saisir un entier et de trouver l'intrus.
#
#         :param user-number : message d'invite à la saisie
#         :param user_number_list : liste de tous les nombres saisi
#         :param number_positif_list : liste de tous les nombres positifs saisis
#         :param intruders_list : Liste de tous les intrus saisis
#         :param count_intruders : compteurs des intrus
#         :return: les détails saisis
#
#     """
#
#     while True:
#         try:
#             user_number = int(input("Trouvez l'intrus : Veuillez saisir un nombre entier : "))
#
#             # Stock les nombres
#             if user_number != 0:
#                 user_number_list.append(user_number)
#
#                 # Stock les nombres
#                 if user_number > 0:
#                     number_positif_list.append(user_number)
#
#                 # Stock les nombres et compte
#                 elif user_number < 0:
#                     count_intruders = count_intruders + 1
#                     intruders_list.append(user_number)
#
#             else:
#                 if count_intruders == 0:
#                     print(f"Vous n'avez pas trouvé d'intrus. Voici les nombres saisis : {user_number_list}")
#                 else:
#                     print(f"Le nombre d'intrus détecté est de : {count_intruders},
#                     voici la liste : {intruders_list}")
#                     print(f"Les nombres sans intrus sont : {number_positif_list}")
#                     print(f"Tous les nombres saisi sont : {user_number_list}")
#
#         except ValueError:
#             print("La valeur saisie n'est pas valide")
#
#
# intruders_nbr()
