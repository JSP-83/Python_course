import scipy as sc
import numpy as np
import random as rd
import matplotlib.pyplot as plt

#MAJ coord enzymes
def moveEnzyme(coord):
    rx = rd.randint(0,1)
    ry = rd.randint(0,1)

    if rx == 1:
        if coord[0] == 9:
            coord[0] = 9
        else:
            coord[0]+=1

    else:
        if coord[0] == 0:
            coord[0] = 0
        else:
            coord[0]-=1

    if ry == 1:
        if coord[1] == 9:
            coord[1] = 9
        else:
            coord[1] += 1

    else:
        if coord[1] == 0:
            coord[1] = 0
        else:
            coord[1] -= 1

    return coord

#MAJ Matrice de peau
def updateMatrix(inhibiteurs,activateurs,matrix):
    for x, y in inhibiteurs:
        for x2, y2 in activateurs:
            if (x, y) == (x2, y2):
                matrix[x, y] = 1

    return matrix

#MAJ Enzymes
def updateEnzyme(inhibiteurs,activateurs):

    for i,coordI in enumerate(inhibiteurs):
        coordI = moveEnzyme(coordI)

    for i,coordA in enumerate(activateurs):
        coordA = moveEnzyme(coordA)

    return inhibiteurs,activateurs

#--------paramètres d'entrées--------
matrix = sc.zeros((10, 10))  # matrice des taches
inhibiteurs = np.array([[1, 2], [8, 8], [8, 7]])
activateurs = np.array([[1, 2], [8, 7]])

#update à t0
matrix = updateMatrix(inhibiteurs, activateurs, matrix)
(inhibiteurs,activateurs) = updateEnzyme(inhibiteurs,activateurs)

# dispersion
for time in range(0,10):
    #dispersion
    nhibiteurs, activateurs = updateEnzyme(inhibiteurs,activateurs)
    matrix = updateMatrix(inhibiteurs, activateurs, matrix)

plt.matshow(matrix,cmap='Oranges')
plt.show()




