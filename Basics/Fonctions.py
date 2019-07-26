# Function


# definition
# ------------------------------------------------------
def test_max(nb):
    max = 10
    if nb >= max:
        print("trop grand")


# appel : test_max(9)


# paramètre par défaut + redéfinition de la fonction
def test_max(nb, max = 10, min = 1):
    if nb >= max:
        print("trop grand")
    if nb <= min:
        print("trop petit")
    return nb


# appel : test = test_max(12)
# ou reset du max : test = test_max(12,15)

# ------------------------------------------------------
# fonctions lambda
f = lambda x: x * x
print(f(5))

f2 = lambda x,y: x * y
print(f2(2,3))

# ------------------------------------------------------
# Fonctions utiles
# function type (donne le type d'une variable)
a = 3
print("typage a :",type(a))


# function print
b = 5
c = 2
print("b = ", b, "et c = ", c)


# function input (permet la saisie)
donnee = input("Saisissez une donnee : ")
print("Vous avez saisi :",donnee)