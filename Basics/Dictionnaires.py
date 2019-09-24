# renferment des objets à l'instar des listes mais associent chaque objet à une clé

mon_dictionnaire = dict()  # nouvelle classe
# ou
new_dictionnaire = {}
new_dictionnaire["presentation"] = "coucou"
autre_dictionnaire = {'nom' : 'jerome', 'date' : 15051993 }
autre_dictionnaire[2] = "test"
print(autre_dictionnaire[2])
echiquier = {}
echiquier['a',1] = "tour"  # tuples !! ('a',1)
print(echiquier['a',1])

# stocker des fonctions
fonctions = {}
def fete():
    print("c'est ma fonction")
fonctions["cle_fete"] = fete
fonctions["cle_fete"]()

# parcours
for cle in autre_dictionnaire.keys(): # même chose pour les valeurs avec values()
    print(cle)
for cle,valeur in autre_dictionnaire.items():
    print("clé : {}, sa valeur : {}.".format(cle,valeur))

#parametres de fonctions
# récupération des paramètres nommés
def fonction_random(*entree,**param_inconnus):
    print("les paramètres sont {}:", format(entree))
    print("les paramètres nommées sont : {}".format(param_inconnus))
fonction_random()
fonction_random('un param',p=4,y=5)