# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables
          # et de fonctions utiles pour dialoguer avec votre
          # syst�me d'exploitation

from Fonctions import test_max # import des fonctions d�finies mais �galement du script

if __name__ == "__main__":
    test = test_max(16)
    os.system("pause")

