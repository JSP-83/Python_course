import scipy as sc
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def updateSurface(surface,inhibiteurs,activateurs):
	for i in range(0,int((len(activateurs)/2)),2):
		if inhibiteurs[i] == activateurs[i]:
			if inhibiteurs[i+1] == activateurs[i+1]:
				surface[inhibiteurs[i],inhibiteurs[i+1]] = 1
	return surface	

def updateEnzymeRandom(tabEnzyme,inputDim):

	i = 0
	for coord in tabEnzyme:
		
		r = rd.randint(0,1)
		if r == 1:
			if coord == inputDim-1:
				coord = inputDim-1
			else:
				coord += 1
		else:
			if coord == 0:
				coord = 0
			else:
				coord -= 1

		tabEnzyme[i] = coord
		i = i+1

	return tabEnzyme

def updateEnzymes(inhibiteurs, activateurs, inputDim, testCoeff,coeff):

	if testCoeff == -1:
		inhibiteurs = updateEnzymeRandom(inhibiteurs, inputDim)
		activateurs = updateEnzymeRandom(activateurs, inputDim)

	elif testCoeff == 0:
		i = 0
		while(i<coeff):
			inhibiteurs = updateEnzymeRandom(inhibiteurs, inputDim)
			i+=1
		activateurs = updateEnzymeRandom(activateurs, inputDim)

	elif testCoeff == 1:
		i = 0
		while(i<coeff):
			activateurs = updateEnzymeRandom(activateurs, inputDim)
			i+=1
		inhibiteurs = updateEnzymeRandom(inhibiteurs, inputDim)	
		

	print("coordonnées inhibiteurs : ",inhibiteurs)
	print("coordonnées activateurs : ",activateurs)

def updateImage(*args):
	updateEnzymes(inhibiteurs, activateurs, inputDim, testCoeff, coeff)
	updateSurface(grille,inhibiteurs, activateurs)	
	print("surface après :",round((time.time()-t0)),"secondes")
	image.set_data(grille)
	return image

def addCoordEnzyme(inhibiteurs,activateurs,grille,firstPointX,firstPointY):
	inhibiteurs = np.insert(inhibiteurs, 0, np.array([firstPointX, firstPointY]))
	activateurs = np.insert(activateurs, 0, np.array([firstPointX, firstPointY]))
	grille[firstPointX,firstPointY] = 1
	return inhibiteurs,activateurs

def inputParameters():
	global inputDim, inhibiteurs, activateurs, grille, image, t0, fig, testCoeff, coeff
	# paramètres d'entrée
	inputDim = input("Entrez une dimension (entier) : ")
	inputDim = int(inputDim)

	# grille
	fig, ax = plt.subplots()
	grille = np.zeros((inputDim,inputDim),dtype=int)

	# premières tâches
	stop = 0
	while(stop == 0):
		firstPointX = input("Entrez une abscisse (entier) : ")
		firstPointX = int(firstPointX)
		while(not firstPointX >= 0 or not firstPointX <= (inputDim-1)):
			firstPointX = input("La valeur est hors des dimensions de la surface, rééssayez : ")
			firstPointX = int(firstPointX)
		firstPointY = input("Entrez une ordonnée (entier) : ")
		firstPointY = int(firstPointY)
		while(not firstPointY >= 0 or not firstPointY <= (inputDim-1)):
			firstPointY = input("La valeur est hors des dimensions de la surface, rééssayez : ")
			firstPointY = int(firstPointY)

		#Enzymes
		if ('testStop' in locals()):
			inhibiteurs,  activateurs =  addCoordEnzyme(inhibiteurs,activateurs,grille,firstPointX,firstPointY)	
		else:
			inhibiteurs = np.array([firstPointX, firstPointY])
			activateurs = np.array([firstPointX, firstPointY])
			grille[firstPointX,firstPointY] = 1
			

		testStop = input("Voulez-vous entrer une nouvelle tâche ? [y/n] : ")
		while (not testStop in ['n','N','Y','y']):
			testStop = input("Je n'ai pas compris, rééssayez : [y/n] : ")

		if testStop in ['n','N']:
			stop = 1

	testCoeff = input("Voulez-vous appliquer un coefficient sur un enzyme ? [y/n]")
	while (not testCoeff in ['n','N','Y','y']):
		testCoeff = input("Je n'ai pas compris, rééssayez : [y/n] : ")

	if testCoeff in ['y','Y']:
		testCoeff = input("Sur les inhibiteurs[0] ou activateurs[1] ? [0/1]")
		while (not testCoeff in ['0','1']):
			testCoeff = input("Je n'ai pas compris, rééssayez : [0/1] : ")
		testCoeff = int(testCoeff)

		coeff = input("Entrez un coefficient positif (entier) : ")
		coeff = int(coeff)
		while(not coeff >= 0):
			coeff = input("Erreur, entrez un coefficient positif (entier) : ")
			coeff = int(coeff)
	else :
		testCoeff = -1
		coeff = -1

	#création de l'image
	image = ax.imshow(grille, interpolation='nearest',cmap='Oranges')
	print("A l'initiale : ")
	print(grille)
	t0 = time.time()

inputParameters()

# animation
ani = animation.FuncAnimation(fig, updateImage, fargs=(image,grille,inputDim,inhibiteurs,activateurs,t0,testCoeff,coeff), frames = inputDim, interval=2000, save_count=50) 
plt.show()
