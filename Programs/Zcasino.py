# inputs
i_argent = 200
continue_partie = True
print("Bienvenue au casino")

while continue_partie:
    try:
        print("Vous avez", i_argent, "$ sur vous")
        if i_argent > 49:
            i_maxBet = 49
        else:
            i_maxBet = i_argent

        print("Choisissez un numéro entre 0 et",i_maxBet,"ce numéro sera votre mise : ")
        s_mise = input()

        while int(s_mise) not in range(0,i_maxBet+1):
            print("Erreur dans la saisie...")
            print("Argent restant :",i_argent)
            print("Choisissez un numéro entre 0 et", i_maxBet,": ")
            s_mise = input()
        i_mise = int(s_mise)

        from random import randint
        i_rnd = randint(0, 49)  # ou randrange(50)
        print("Le chiffre", i_rnd, "est tombé !")
        if i_rnd == i_mise:
            print("BRAVO ! Vous avez gagné trois fois votre mise :", i_mise * 3,"$")
            i_argent += i_mise + i_mise * 3
        else:
            if i_rnd % 2 == i_mise % 2:
                print("Vous avez gagné la moitié de votre mise :", i_mise / 2.,"$ (arrondi au dollar supérieur)")
                from math import ceil
                i_argent += ceil(i_mise + i_mise / 2.)
            else:
                print("Vous n'avez rien gagné...")

        # Stop
        if i_argent == 0:
            print("Vous n'avez plus d'argent !")
            continue_partie = False
    except ValueError:
        print("Erreur dans la saisie...")



