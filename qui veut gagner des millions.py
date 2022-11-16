import random
import time


def menu():
        print("\nBienvenue dans ce jeu")
        time.sleep(1)
        print("\nLe jeu ne ce joue qu'avec le Pavé numérique (1, 2, 3, 4 ...)")
        time.sleep(1)
        print("\nVoici les actions possibles :")
        time.sleep(1)
        print("\n")
        print("Choix 1 = Jouer au jeu\n")
        time.sleep(1)
        print("Choix 2 = Ajouter une nouvelle question (en construction)\n")
        time.sleep(2)
        utilisateur = int(input("Choisissez une action parmi les suivantes : "))
        if utilisateur == 1 :
            print("\nVous allez devoir répondre à une série de 15 questions")
            time.sleep(2)
            print("\nQuel thème choisissez-vous ?")
            time.sleep(1)
            print("\n1 - Culture Générale\n")
            time.sleep(1)
            print("\n2 - Histoire\n")
            time.sleep(1)
            print("\n3 - Géographie \n")
            time.sleep(1)
            choix_theme = int(input("\n Votre choix : "))
            if choix_theme == 1 :
                question_culture_generale()
            elif choix_theme == 2:
                question_histoire()
            elif choix_theme == 3:
                question_geographie()
            else: 
                print("\n C'est en construction, Vous devez choisir un theme disponible !")
                menu()

def question_culture_generale():
    print("\nBienvenue dans l'émission : 'Qui veut gagner des millions ?'")
    time.sleep(2)
    Utilisateur = input("Quel est votre prénom / surnom ? : ")
    print("\nJe suis Jean-Pierre Foucault, et tout de suite, nous jouons pour...'")
    time.sleep(2)
    print("\n200€")
    time.sleep(1)
    print("\nTou Tou Touuuuuuuuum.....")
    time.sleep(3)
    print("\n*musique de suspense*'")
    time.sleep(2)
    print("\nVoici tout de suite, la 1ère question")
    time.sleep(1)
    question = 1                                                                                                         #random.randint(0, 1)
    if question == 1:
#####################################################################################################################################################################
        print("Question 1 : Sous quel logiciel a été codé ce Jeu ?\n 1 - Jupyter\n 2 - HTML\n 3 - Python\n 4 - Jupyter")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Python...\n Vous nous quittez avec les simples sous que vous avez dans les poches...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 200€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 2 : Sur un clavier numérique français, Quel lettre vient après AZERTY ?\n 1 - La lettre H\n 2 - La lettre U\n 3 - La lettre F\n 4 - La lettre K")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était U... En effet, il vous suffisait de regarder votre clavier numérique.\n Vous nous quittez avec 200€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
        time.sleep(2)
        print("Vous avez atteint le premier palier ! Désormais, si vous perdez, vous repartirez avec 300€ quoi qu'il en soit !\n")
        time.sleep(3)
#####################################################################################################################################################################
        print("\nQuestion 3 : Guido van Rossum, créateur de Python est né en 1956, il a sorti la première version de Python à l'âge de 35 ans...\n En quelle année est sortie la première version du logiciel Python ?\n 1 - 2002\n 2 - 1984\n 3 - 1973\n 4 - 1991")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était 1991... En effet, il ne s'attendait pas à un tel succès !.\n Vous nous quittez malheureusement avec seulement 300€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 4 : Quelle est la plus petite planète du système solaire ?\n 1 - Mercure\n 2 - La Lune\n 3 - Jupiter\n 4 - Saturne")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Mercure... En effet, Mercure est la planète la plus proche du Soleil et la moins massive du Système solaire !.\n Vous nous quittez malheureusement avec seulement 500€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 800€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 5 : En physique, Quelle unité est utilisée pour mesurer la tension électrique ?\n 1 - Le Watt\n 2 - Le Hertz\n 3 - Le Volt\n 4 - le Hertz")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Le Volt... En effet, Le Volt est l'unité de mesure de la tension électrique dans un circuit entre un point A et un point B !.\n Vous nous quittez malheureusement avec seulement 800€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 1.500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 6 : Parmis ces 4 plats italiens, Lequel d'entre eux n'est pas un dessert ?\n 1 - Le Panettone\n 2 - Le Cannoli\n 3 - La Crostata\n 4 - La Bruschetta")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était La Bruschetta... En effet, Il s'agit traditionnellement d'une tartine de pain de campagne frotté à l'ail et assaisonné d'huile d'olive !.\n Vous nous quittez malheureusement avec seulement 1.500€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 3.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 7 : Lequel de ces 4 mots de la langue française est mal orthographié ?\n 1 - Trottinette\n 2 - Gaufre\n 3 - Intermittance\n 4 - Inondation")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Intermittance ... En effet, Gaufre désigne un gâteau formé d'alvéoles de cire que fabriquent les abeilles, les autres réponses sont bien orthographiées !.\n Vous nous quittez malheureusement avec 3.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 6.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 8 : Les 4 pays qui ont disputé les demi-finales de la coupe du monde de football en 1998 sont la France, le Brésil, La Croatie et... ?\n 1 - L'Allemagne\n 2 - L'Argentine\n 3 - Le Chili\n 4 - Les Pays-Bas")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Les Pays-Bas... En effet, La France avait gagné la coupe du monde 2 buts à 1 face à la Croatie !.\n Vous nous quittez malheureusement avec 6.000€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 12.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 9 : Dans quelle partie du corps humain trouve t-on le nerf dit pudendal ?\n 1 - Dans le Bassin\n 2 - Dans la Cheville\n 3 - Dans l'épaule\n 4 - Dans la Cuisse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était dans le bassin... En effet, Le nerf Pendudal est l'un des nerfs principaux qui innerve le périnée !.\n Vous nous quittez malheureusement avec 12.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 24.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 10 : Ou se situe la ville française de Kourou ?\n 1 - Martinique\n 2 - Guadeloupe\n 3 - Corse\n 4 - Guyane")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était La Guyane... En effet, Kourou est une ville et un district sur la côte atlantique de la Guyane Française ! !.\n Vous nous quittez malheureusement avec 24.000€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 48.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 11 : Dans la Grèce Antique, on déconseillait aux femmes de participer aux Jeux Olympiques, sauf à une épreuve... Laquelle ?\n 1 - La Course De Char\n 2 - La Course à Pied\n 3 - La Lutte\n 4 - La Natation")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était La course de Char... En effet, La distinction entre propriétaire et conducteur du char explique que les femmes pouvaient techniquement gagner la course.\n Vous nous quittez malheureusement avec 48.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 72.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 12 : Au musée Grévin, La statue de cire de Barack Obama porte une cravate... ?\n 1 - A Carreaux Rouges\n 2 - Avec une étoile bleue\n 3 - A rayures rouges\n 4 - Avec un rond bleu")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Une cravate a rayures rouges !... En effet, Le 29 Juin 2009, la statue de Barack Obama vêtu d’un costume sombre orné sur son revers d’un pin’s représentant le drapeau américain arriva au musée Grévin !.\n Vous nous quittez malheureusement avec 72.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 100.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 13 : Sur la couverture de l'album de Tintin 'L'étoile mystérieuse' Tintin et Milou sont effrayés par... ? ?\n 1 - Une Momie\n 2 - Une étoile\n 3 - Un Champignon\n 4 - Un Fantôme")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Un Champignon... En effet, On peut apercevoir Tintin qui se tient devant un champignon blanc à pois rouges faisant presque 2 fois sa taille !.\n Vous nous quittez malheureusement avec seulement [Cagnotte]€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 150.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 14 : Que désigne la climacophobie ?\n 1 - La peur des Escaliers\n 2 - La peur des Forêts\n 3 - La peur du climat\n 4 - La peur de la boue")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était La peur des escaliers... En effet, La climacophobie désigne la peur phobique des escaliers, de tomber dans les escaliers. !.\n Vous nous quittez malheureusement avec 150.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 15 : Avec quel pays la France partage t-elle sa plus grande frontière terrestre ?\n 1 - Monaco\n 2 - Bresil\n 3 - Espagne\n 4 - Belgique")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Le Brésil... En effet, La France possède aussi des territoires outre-mer !.\n Vous nous quittez malheureusement avec 300.000€... \n et cela vaut bien des applaudissements !")
            time.sleep(2)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            exit()
        elif Reponse == 2:
            print("Bravo, Bonne réponse !")
            time.sleep(2)
            print(Utilisateur, "Vous venez actuellement de remporter 1 MILLION D'EUROS")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################



def question_histoire():
    print("\nBienvenue dans l'émission : 'Qui veut gagner des millions ?'")
    time.sleep(2)
    Utilisateur = input("Quel est votre prénom / surnom ? : ")
    print("Je suis Jean-Pierre Foucault, et tout de suite, nous jouons pour...'")
    time.sleep(2)
    print("200€")
    time.sleep(1)
    print("Tou Tou Touuuuuuuuum.....")
    time.sleep(3)
    print("*musique de suspense*'")
    time.sleep(2)
    print(" Voici tout de suite, la 1ère question")
    time.sleep(1)
    question = 1                                                                                                         #random.randint(0, 1)
    if question == 1:
#####################################################################################################################################################################
        print("Question 1 : Quelle est la couleur du cheval blanc d'Henri IV ?\n 1 - Noire\n 2 - Gris\n 3 - Blanc\n 4 - Rouge a pois vert")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Blanc...\n Vous nous quittez avec les simples sous que vous avez dans les poches...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 200€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 2 : Quelle était la nationalité du général Charles de Gaulle ?\n 1 - Américaine\n 2 - Française\n 3 - Anglaise\n 4 - Belge")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Française... Le quiz est de niveau CM1.\n Vous nous quittez avec 200€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()
        time.sleep(2)
        print("Vous avez atteint le premier palier ! Désormais, si vous perdez, vous repartirez avec 300€ quoi qu'il en soit !\n")
        time.sleep(3)
#####################################################################################################################################################################
        print("\nQuestion 3 : A quel moment a debuter la préhistoire ?\n 1 - La disparition des dinosaures\n 2 - A l'age de l'or\n 3 - 1973\n 4 - L'apparition de l'homme")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était L'apparation de l'homme... En effet, La préhistoire débute à l’apparition de l’homme à 3 millions d’années av. J.-C. !.\n Vous nous quittez malheureusement avec seulement 300€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 4 : Que signifie Charlemagne ?\n 1 - Charles le Grand\n 2 - Charles le Magnifique\n 3 - Charles le conquérant\n 4 - Charles le Prompt")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Charles le grand... En effet, Charlemagne, en latin Carolus Magnus, signifie Charles le Grand !\n Vous nous quittez malheureusement avec seulement 500€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 800€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 5 : Quand Adolf Hitler est-il au pouvoir en Allemagne ?\n 1 - Entre 1922 et 1943\n 2 - Entre 1924 et 1953\n 3 - Entre 1933 et 1945\n 4 - Entre 1939 et 1950")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Entre 1933 et 1945... Il prend le pouvoir en Allemagne en 1933 et instaure une dictature totalitaire, impérialiste, antisémite, raciste et xénophobe !.\n Vous nous quittez malheureusement avec seulement 800€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 1.500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 6 : Quel peuple est exterminé en 1915-1916 ?\n 1 - Les Hereros\n 2 - Les Amerindiens\n 3 - Les Inuits\n 4 - Les Armeniens")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Les Armeniens... En effet, Ce peuple a été exterminé, on parle même de génocide !.\n Vous nous quittez malheureusement avec seulement 1.500€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 3.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 7 : Qui était surnommé le Petit Père des Peuples ?\n 1 - Staline\n 2 - Napoléon\n 3 - Lénine\n 4 - Hitler")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Staline... En effet, L'appellation Père des peuples a été utilisée en Russie tsariste puis en URSS à des fins de culte de la personnalité et de propagande !.\n Vous nous quittez malheureusement avec 150.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 6.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 8 : Quelle superpuissance domine le monde après 1989  ?\n 1 - Le Japon\n 2 - La Chine\n 3 - Le L'URSS\n 4 - Les Etats-Unis")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Les Etats-Unis... En effet, Les États-Unis dominent scientifiquement, militairement, économiquement et culturellement !.\n Vous nous quittez malheureusement avec 6.000€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 12.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 9 : Qu’appelle-t-on les Trente Glorieuses ?\n 1 - Une période de prospérité de 1945 à 1975\n 2 -  Les années 1830\n 3 -  Les années 1930\n 4 -  Une période de prospérité de 1845 à 1875")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Une période de prospérité de 1945 à 1975... En effet, Les Trente Glorieuses sont la période de forte croissance économique et d'augmentation du niveau de vie !.\n Vous nous quittez malheureusement avec 12.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 24.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 10 : En quelle année, la guerre d’Algérie a-t-elle pris fin ?\n 1 - 1948 \n 2 - 1962\n 3 - 1956\n 4 - 1973")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était 1962... En effet, La Guerre d'indépendance de l'Algérie a pris fin le 19 mars 1962 !.\n Vous nous quittez malheureusement avec 24.000€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 48.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 11 : En quelle année, le Mur de Berlin est-il tombé ?\n 1 - 1989\n 2 - 1988\n 3 - 1990\n 4 - 1991")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était 1989... En effet, La chute du mur de Berlin a lieu dans la nuit du 9 novembre 1989.\n Vous nous quittez malheureusement avec 48.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 72.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 12 : Quel écrivain français du XIXe siècle, farouche opposant à la peine de mort, a écrit « Le Dernier jour d’un Condamné » ? ?\n 1 - Lamartine\n 2 - Balzac\n 3 - Victor Hugo\n 4 - Flaubert")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Victor Hugo... En effet, Le Dernier Jour d’un condamné est un roman à thèse de Victor Hugo publié en 1829  !.\n Vous nous quittez malheureusement avec 72.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 100.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 13 : Quel homme politique a obtenu le prix Nobel de Littérature ?\n 1 - Le général de Gaulle\n 2 - Konrad Adenauer\n 3 - Winston Churchill\n 4 - Thomas Jefferson")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Winston Churchill... En effet, Le Prix Nobel de littérature lui est décerné le 15 octobre 1953.\n Vous nous quittez malheureusement avec seulement 100.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 150.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 14 : Qu’est-ce qu’un armistice ?\n 1 - La fin de la guerre\n 2 - Une capitulation\n 3 - La fin des combats\n 4 - Une alliance")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était La fin des combats ... En effet, La signature de l'armistice est synonyme de suspension des combats, de cessez-le-feu ou de trêve !.\n Vous nous quittez malheureusement avec 3.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 15 : En janvier 2012, combien de pays faisaient partie de l'Europe ?\n 1 - 15\n 2 - 27\n 3 - 23\n 4 - 30")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était 27... En effet, Les pays sont l'Allemagne, l'Autriche, la Belgique, la Bulgarie, Chypre, la Croatie, le Danemark, l'Espagne, l'Estonie, la Finlande, la France, la Grèce, la Hongrie et bien d'autres... .\n Vous nous quittez malheureusement avec 300.000€... \n et cela vaut bien des applaudissements !")
            time.sleep(2)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            exit()
        elif Reponse == 2:
            print("\nBravo, Bonne réponse !")
            time.sleep(2)
            print(Utilisateur, "\nVous venez actuellement de remporter 1 MILLION D'EUROS")
        else:
            print("\nVous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()


#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################

def question_geographie():
    print("\nBienvenue dans l'émission : 'Qui veut gagner des millions ?'")
    time.sleep(2)
    Utilisateur = input("Quel est votre prénom / surnom ? : ")
    print("Je suis Jean-Pierre Foucault, et tout de suite, nous jouons pour...'")
    time.sleep(2)
    print("200€")
    time.sleep(1)
    print("Tou Tou Touuuuuuuuum.....")
    time.sleep(3)
    print("*musique de suspense*'")
    time.sleep(2)
    print(" Voici tout de suite, la 1ère question")
    time.sleep(1)
    question = 1                                                                                                         #random.randint(0, 1)
    if question == 1:
#####################################################################################################################################################################
        print("Question 1 : Dans quelle ville se trouve la Statue de la Liberté ?\n 1 - New York\n 2 - Washington\n 3 - Chicago\n 4 - Los Angeles")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était New York... En effet, La statue de la Liberté, en plus d'être un monument très important de la ville de New York, est devenue l'un des symboles des États-Unis \n Vous nous quittez avec les simples sous que vous avez dans les poches...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 200€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 2 : Sur quel continent le Nil coule-t-il ?\n 1 - L'Océanie\n 2 - L'Afrique\n 3 - L'Europe\n 4 - L'Amérique")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était L'Afrique... En effet, Le Nil est un fleuve d'Afrique. Avec une longueur d'environ 6 700 km , c'est avec le fleuve Amazone, le plus long fleuve du monde..\n Vous nous quittez avec 200€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()
        time.sleep(2)
        print("Vous avez atteint le premier palier ! Désormais, si vous perdez, vous repartirez avec 300€ quoi qu'il en soit !\n")
        time.sleep(3)
#####################################################################################################################################################################
        print("\nQuestion 3 : Quel fleuve traverse la ville de Lyon ?\n 1 - La Garonne\n 2 - La Seine\n 3 - Le Rhin\n 4 - Le Rhône")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Le Rhône... En effet, Le Rhône est un fleuve d'Europe, long de 812 kilomètres. Il prend sa source dans le glacier du Rhône, en Suisse !.\n Vous nous quittez malheureusement avec seulement 300€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 4 : Quelle est la deuxième langue officielle parlée en Irlande ?\n 1 - L'anglais\n 2 - Le Celte\n 3 - Le Français\n 4 - L'Allemand")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était L'anglais... En effet, 3 langues sont parlées en Irlande : L'irlandais, L'anglais et le scots d'Ulster parlée dans la province d'Ulster !\n Vous nous quittez malheureusement avec seulement 500€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 800€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 5 : Quelles couleurs figurent sur le drapeau allemand ?\n 1 - Noir - vert - jaune\n 2 - Noir - rouge - jaune\n 3 - Noir - orange - blanc\n 4 - Noir - rouge - blanc")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Noir - rouge - jaune...  C'est un drapeau tricolore composé de trois bandes horizontales égales aux couleurs nationales de l'Allemagne : noir, rouge et jaune !.\n Vous nous quittez malheureusement avec seulement 800€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 1.500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 6 : Dans quel département français se trouve la ville de Pont-Aven ?\n 1 - La Loire-Atlantique\n 2 - Le Morbihan\n 3 - Les Côtes-d'Armor\n 4 - Le Finistère")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Le Finistère... En effet, Le Finistère est un département français situé en région Bretagne !.\n Vous nous quittez malheureusement avec seulement 1.500€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 3.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 7 : Où siège la Cour de Justice de l’Union européenne ?\n 1 - Luxembourg\n 2 - La Haye\n 3 - Maastricht\n 4 - Amsterdam")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Luxembourg... En effet, Cette ville regroupe deux juridictions : la Cour de justice et le Tribunal !.\n Vous nous quittez malheureusement avec 150.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 6.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 8 : Quelle superficie occupe l'océan Pacifique ?\n 1 - 152 342 000 km²\n 2 - 166 241 700 km²\n 3 - 172 490 650 km²\n 4 - 186 457 250 km²")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était 166 241 700 km²... En effet, Le Pacifique s'étend sur une surface de 166 241 700 km2, soit environ un tiers de la surface totale de la Terre!.\n Vous nous quittez malheureusement avec 6.000€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 12.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 9 : Quelle est la capitale des Philippines ?\n 1 - Manille\n 2 - Séoul\n 3 - Jakarta\n 4 - Wellington")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Manille... En effet, Manille, capitale des Philippines, est une ville très peuplée qui fait face à la baie, sur l'île de Luçon !.\n Vous nous quittez malheureusement avec 12.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 24.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 10 : Quelle est la capitale des États-Unis d'Amérique ?\n 1 - Miami \n 2 - Washington DC\n 3 - New York\n 4 - Detroit")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Washington DC... En effet, Washington, la capitale des États-Unis, est une ville dense située sur les rives du Potomac, à la frontière des États du Maryland et de Virginie !\n Vous nous quittez malheureusement avec 24.000€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 48.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 11 : Quel département français a pour code géographique le 16 ?\n 1 - La Charente\n 2 - L'Aveyron\n 3 - L'Aude\n 4 - Le Cantal")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était La Charente... En effet, La Charente est un département français situé dans le Sud-Ouest de la France, dans la moitié nord de la région Nouvelle-Aquitaine.\n Vous nous quittez malheureusement avec 48.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 72.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 12 : À quelle région est rattaché le département de l'Yonne ?\n 1 - Le Nord-Pas-de-Calais\n 2 - La Basse-Normandie\n 3 - La Bourgogne\n 4 - La Picardie")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était La Bourgogne... En effet, La Bourgogne est une région administrative située dans le Centre-Est de la France. !\n Vous nous quittez malheureusement avec 72.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 100.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 13 : Hormis le Tigre, quel est le nom du deuxième grand fleuve d'Irak ?\n 1 - Le Gange\n 2 - Le Nil\n 3 - L'Euphrate\n 4 - L'Ebre")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était L'Euphrate... En effet, L'Euphrate est un fleuve d'Asie de 2 780 km de long. Il forme, avec le Tigre, dans sa partie basse, la Mésopotamie, l'un des berceaux de la civilisation.\n Vous nous quittez malheureusement avec seulement 100.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 150.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 14 : Quel est la capital du Kurdistan ?\n 1 - Ankawa\n 2 - Nass City\n 3 - Erbil\n 4 - Pirrash")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Erbil ... En effet, Erbil est la capitale du Gouvernement régional du Kurdistan. Elle est aussi la capitale de la province d'Erbil !.\n Vous nous quittez malheureusement avec 150.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 15 : Quel pays a pour capitale Vientiane ?\n 1 - Birmanie\n 2 - Laos\n 3 - San Salvador\n 4 - Israël")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Laos... En effet, Vientiane, la capitale du Laos, allie architecture coloniale française et temples bouddhistes comme le Pha That Luang du XVIe siècle, un symbole national .\n Vous nous quittez malheureusement avec 300.000€... \n ")
            time.sleep(2)
            print("et cela vaut bien des applaudissements !")
            time.sleep(2)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            exit()
        elif Reponse == 2:
            print("\nBravo, Bonne réponse !")
            time.sleep(2)
            print(Utilisateur, "\nVous venez actuellement de remporter 1 MILLION D'EUROS")
        else:
            print("\nVous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()

#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################

def question_a_venir():
    print("\nBienvenue dans l'émission : 'Qui veut gagner des millions ?'")
    time.sleep(2)
    Utilisateur = input("Quel est votre prénom / surnom ? : ")
    print("Je suis Jean-Pierre Foucault, et tout de suite, nous jouons pour...'")
    time.sleep(2)
    print("200€")
    time.sleep(1)
    print("Tou Tou Touuuuuuuuum.....")
    time.sleep(3)
    print("*musique de suspense*'")
    time.sleep(2)
    print(" Voici tout de suite, la 1ère question")
    time.sleep(1)
    question = 1                                                                                                         #random.randint(0, 1)
    if question == 1:
#####################################################################################################################################################################
        print("Question 1 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] \n Vous nous quittez avec les simples sous que vous avez dans les poches...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 200€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 2 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation].\n Vous nous quittez avec 200€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()
        time.sleep(2)
        print("Vous avez atteint le premier palier ! Désormais, si vous perdez, vous repartirez avec 300€ quoi qu'il en soit !\n")
        time.sleep(3)
#####################################################################################################################################################################
        print("\nQuestion 3 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec seulement 300€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 4 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumention] !\n Vous nous quittez malheureusement avec seulement 500€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 800€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 5 : [Argumentation] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... [Argumentation] !.\n Vous nous quittez malheureusement avec seulement 800€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 1.500€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 6 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec seulement 1.500€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 3.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 7 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec 150.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 6.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 8 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 3 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation]!.\n Vous nous quittez malheureusement avec 6.000€...")
            exit()
        elif Reponse == 4:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 12.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 9 : [Question] ?\n 1 - Reponse\n 2 -  Reponse\n 3 - Reponse\n 4 -  Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec 12.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 24.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 10 : [Question] ?\n 1 - Reponse \n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec 24.000€...")
            exit()
        elif Reponse == 2:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 48.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 11 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 2 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation].\n Vous nous quittez malheureusement avec 48.000€...")
            exit()
        elif Reponse == 1:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 72.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 12 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation]  !.\n Vous nous quittez malheureusement avec 72.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 100.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 13 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation].\n Vous nous quittez malheureusement avec seulement 100.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 150.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 14 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 2 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse ... En effet, [Argumentation] !.\n Vous nous quittez malheureusement avec 3.000€...")
            exit()
        elif Reponse == 3:
            print("Bonne réponse ! Votre cagnotte s'éléve désormais à 300.000€ !")
        else:
            print("Vous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !\n")
            exit()
        time.sleep(2)
#####################################################################################################################################################################
        print("\nQuestion 15 : [Question] ?\n 1 - Reponse\n 2 - Reponse\n 3 - Reponse\n 4 - Reponse")
        Reponse = int(input("Inscrivez votre reponse : "))
        if Reponse == 1 or Reponse == 3 or Reponse == 4 :
            print("Vous avez perdu... La réponse était Reponse... En effet, [Argumentation] .\n Vous nous quittez malheureusement avec 300.000€... \n et cela vaut bien des applaudissements !")
            time.sleep(2)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            time.sleep(1)
            print("*Appaudissement*")
            exit()
        elif Reponse == 2:
            print("\nBravo, Bonne réponse !")
            time.sleep(2)
            print(Utilisateur, "\nVous venez actuellement de remporter 1 MILLION D'EUROS")
        else:
            print("\nVous n'avez pas entrer une bonne valeur ! Vous avez essayé de tricher, Fin du Jeu !")
            exit()




def hesitation():
    hesiter = random.randint(0,10)
    if hesitation == 5 :
        time.sleep(3)
        print("\nPrenez votre temps pour réfléchir...\n")
        time.sleep(2)
        print("\nPour rappel, vous bénéficiez de Jokers")
    else:
        pass

def joker():
    print("\nVous bénéficiez de plusieurs Jokers, voici la liste : " )
    time.sleep(2)
    print("\nChoix n°1 : Le 50 / 50 : L'ordinateur enlèvera 2 réponses qui sont fausses, ainsi il ne vous restera plus qu'une mauvaise réponse et une bonne réponse")
    time.sleep(2)
    print("\nChoix n°2 : L'appel à un ami : Vous appellez un ami que vous jugez spécialiste dans le domaine de la question posée")
    time.sleep(2)
    print("\nChoix n°3 : L'avis du public : Le public se muni de petites télécommandes et vous obtiendrez alors le pourcentage de réponses pour chaque choix")
    time.sleep(1)
    joker_reponse = int(input("Inscrivez un numéro entre 1 et 3 représentant votre choix : "))
    if joker_reponse == 1 or joker_reponse == 2 or joker_reponse == 3 :
        theme_actuel = int(input("\nEntrez le numéro de votre thème choisi ( Culture Général = 1; Géographie = 2; Histoire = 3 ) : "))
        question_actuelle = int(input("\nInscrivez le numéro de votre question actuelle : "))
        print("Ordinateur... ")
        time.sleep(1)
        print("Enlevez 2 mauvaises réponses !")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        if theme_actuel == 1 and question_actuelle == 1 : 
            print("Tadam ! il ne reste plus que Python et HTML")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 2 : 
            print("Tadam ! il ne reste plus que La lettre U et la lettre H")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 3 : 
            print("Tadam ! il ne reste plus que 1991 et 2002")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 4 : 
            print("Tadam ! il ne reste plus que La lune et Mercure ")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 5 : 
            print("Tadam ! il ne reste plus que Le Hertz et le Volt")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 6 : 
            print("Tadam ! il ne reste plus que La Crostata et la Bruschetta")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 7 : 
            print("Tadam ! il ne reste plus que Trottinette et Intermittance")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 8 : 
            print("Tadam ! il ne reste plus que Les Pays-Bas et L'Allemagne ")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 9 : 
            print("Tadam ! il ne reste plus que Dans le Bassin ou dans L'Epaule")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 10 : 
            print("Tadam ! il ne reste plus que la Guyane et la Guadeloupe")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 11 : 
            print("Tadam ! il ne reste plus que La Course de Char ou La Lutte !")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 12 : 
            print("Tadam ! il ne reste plus que Avec une étoile bleue ou à rayures rouges")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 13 : 
            print("Tadam ! il ne reste plus que un Champignon ou une Etoile")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 14 : 
            print("Tadam ! il ne reste plus que La peur des Escaliers ou la peur des Forêts")
            joker1 = 1
        elif theme_actuel == 1 and question_actuelle == 15 : 
            print("Tadam ! il ne reste plus que Le Bresil ou Monaco ! ")
            joker1 = 1
        else:
            print("\nVous avez entrer un numéro invalide, veuillez réessayer")
        time.sleep(1)
    elif joker_reponse == 2:
        theme_actuel = int(input("\nEntrez le numéro de votre thème choisi ( Culture Général = 1; Géographie = 2; Histoire = 3 ) : "))
        question_actuelle = int(input("\nInscrivez le numéro de votre question actuelle : "))
        time.sleep(1)
        Personne = int(input("\nTrès bien, Maintenant, qui décidez-vous d'appeler ? (Mère = 1; Père = 2; Frère = 3; Soeur = 4) : "))
        if Personne == 1:
            print("\n Très bien, Vous avez décidé d'appeler votre mère... ")
        elif Personne == 2:
            print("\n Très bien, Vous avez décidé d'appeler votre père... ")
        elif Personne == 3:
            print("\n Très bien, Vous avez décidé d'appeler votre frère... ")
        elif Personne == 4: 
            print("\n Très bien, Vous avez décidé d'appeler votre Soeur... ")
            time.sleep(2)
            print("\n*biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiip*")
            time.sleep(2)
            print("\n*biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiip*")
            time.sleep(1)
            print("\n*biiiiiiiiiiiiiiiiiiiiiiiiii* Oui allô ? ")
            time.sleep(1)
            print("\nBonjour, c'est Jean-Pierre Foucault à l'appareil.")
            time.sleep(1)
            print("\nJe vous appelle car " "est actuellement en difficulté sur la question ", question_actuelle)
            time.sleep(2)
            print("\nJe vous lis tout de suite la question : ")
        if theme_actuel == 1 and question_actuelle == 1 :
             print("Sous quel logiciel a été codé ce Jeu ?")
             time.sleep(1)
             print("\nmmmmh, Si je me souviens bien, dans les anciennes émissions, le jeu était codé sous Python...")
        elif theme_actuel == 1 and question_actuelle == 2 :
            print("Sur un clavier numérique français, Quel lettre vient après AZERTY ?")
            time.sleep(1)
            print("C'est la lettre U... Oui c'est cela !")
        elif theme_actuel == 1 and question_actuelle == 3 :
            print("Guido van Rossum, créateur de Python est né en 1956, il a sorti la première version de Python à l'âge de 35 ans...\n En quelle année est sortie la première version du logiciel Python ?")
            time.sleep(1)
            print("Tout est une question de calcul ! Normalement, la réponse est 1991")
        elif theme_actuel == 1 and question_actuelle == 4 :
            print("Quelle est la plus petite planète du système solaire ?")
            time.sleep(1)
            print("Si je me souviens bien la lune n'est pas considéré comme une planète mais comme un astre ! Donc pour moi ce serait beaucoup plus logqiue que ce soit mercure!")
menu()