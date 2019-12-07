def updateImage(*args):
	x = rd.randint(0,9)
	y = rd.randint(0,9)
	grille[x,y] = 255
	print("surface après :",round((time.time()-t0)),"secondes")
	image.set_data(grille)
	return image

def inputParameters():
	global inputDim, inhibiteurs, activateurs, grille, image, t0, fig
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
			grille[firstPointX,firstPointY] = 255
			

		testStop = input("Voulez-vous entrer une nouvelle tâche ? [y/n] : ")
		while (not testStop in ['n','N','Y','y']):
			testStop = input("Je n'ai pas compris, rééssayez : [y/n] : ")

		if testStop in ['n','N']:
			stop = 1

	#création de l'image
	image = ax.imshow(grille, interpolation='nearest',cmap='Oranges')
	print("A l'initiale : ")
	print(grille)
	t0 = time.time();

inputParameters()

# animation
ani = animation.FuncAnimation(fig, updateImage, fargs=(image,grille,inputDim,inhibiteurs,activateurs,t0), frames = inputDim, interval=2000, save_count=50) 
plt.show()
