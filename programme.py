#Projet IA échec (pour coco <3)

from tkinter import *
from tkinter.messagebox import *
from functools import partial

root = Tk()

root['bg']='#A4A4A4'
root.geometry("1000x600+10+10")
root.title('Jeu d\'échec')

echiquier = Canvas(root, width=600, height=600, background='white')
echiquier.pack(side='left')

posX = 0
posY = 0

joueur = "blanc"

capture = False


"""def jouerCoup(case, event):
	if echiquier.itemcget(CURRENT, 'fill')=='blue':
		x=event.x
		y=event.y
		X = (x-44)//64
		Y = (y-44)//64
		pos = lirePosition()
		if coupAutorise(pieceSelect, posX, posY, X, Y) :
			echiquier.coords(CURRENT, X*64+32+marge, Y*64+32+marge, X*64+32+marge, Y*64+32+marge)
			echiquier.update()
			#pos = lirePosition()
			#print(pos==position)
			#marquerCoup(position, pos)
			#print(coups)
			position = pos
			if joueur=="blanc":
				joueur="noir"
			else:
				joueur="blanc"
		else:
			echiquier.coords(CURRENT, posX*64+32+marge, posY*64+32+marge, posX*64+32+marge, posY*64+32+marge)
			echiquier.update()"""

def casesEchiquier(couleur, lat, longi): #lat : lettres et longi : chiffres
	global cases
	cases = []
	nbrecases = 0
	cases.append(echiquier.create_rectangle(lat, longi, lat+64, longi+64, fill=couleur, tags='cases'))
	#echiquier.tag_bind(cases[nbrecases], '<Button-1>', partial(jouerCoup, nbrecases))
	if couleur=="lightgray" and lat!=64*7+marge:
		couleur="white"
	elif couleur=="white" and lat!=64*7+marge:
		couleur="lightgray"
	if lat==64*7+marge:
		lat=marge
		longi+=64
	else:
		lat+=64
	if lat!=marge or longi!=512+marge:
		casesEchiquier(couleur, lat, longi)
	nbrecases+=1

marge = 44
casesEchiquier("white", marge, marge)

tourN = PhotoImage(file="images/tourN.png")
cavalierN = PhotoImage(file="images/cavalierN.png")
fouN = PhotoImage(file="images/fouN.png")
dameN = PhotoImage(file="images/dameN.png")
roiN = PhotoImage(file="images/roiN.png")
pionN = PhotoImage(file="images/pionN.png")
tourB = PhotoImage(file="images/tourB.png")
cavalierB = PhotoImage(file="images/cavalierB.png")
fouB = PhotoImage(file="images/fouB.png")
dameB = PhotoImage(file="images/dameB.png")
roiB = PhotoImage(file="images/roiB.png")
pionB = PhotoImage(file="images/pionB.png")


partie = Canvas(root, width=380, height=600, background='white')
partie.pack(side='right')

def placerPieces():
	global nbrepieces, pieces
	nbrepieces = 0
	pieces = []
	centre = marge + 32
	for ligne in range(0, 8):
		for colonne in range(0, 8):
			if position[ligne][colonne] == "tourN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=tourN, tags="piecesN"))
			elif position[ligne][colonne] == "cavalierN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=cavalierN, tags="piecesN"))
			elif position[ligne][colonne] == "fouN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=fouN, tags="piecesN"))
			elif position[ligne][colonne] == "dameN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=dameN, tags="piecesN"))
			elif position[ligne][colonne] == "roiN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=roiN, tags="piecesN"))
			elif position[ligne][colonne] == "pionN":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=pionN, tags="piecesN"))
			elif position[ligne][colonne] == "tourB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=tourB, tags="piecesB"))
			elif position[ligne][colonne] == "cavalierB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=cavalierB, tags="piecesB"))
			elif position[ligne][colonne] == "fouB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=fouB, tags="piecesB"))
			elif position[ligne][colonne] == "dameB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=dameB, tags="piecesB"))
			elif position[ligne][colonne] == "roiB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=roiB, tags="piecesB"))
			elif position[ligne][colonne] == "pionB":
				pieces.append(echiquier.create_image(centre+colonne*64, centre+ligne*64, image=pionB, tags="piecesB"))
			if position[ligne][colonne] != "R":
				echiquier.tag_bind(pieces[nbrepieces], '<Button-1>', partial(positionDepart, nbrepieces))
				echiquier.tag_bind(pieces[nbrepieces], '<B1-Motion>', partial(deplacerPieces, nbrepieces))
				echiquier.tag_bind(pieces[nbrepieces], '<B1-ButtonRelease>', partial(relacherPieces, nbrepieces))
				nbrepieces+=1

"""def lirePosition():
	global position, coups
	for ligne in range(0,8):
		for colonne in range(0,8):
			tag = echiquier.find_closest(colonne*64+32+marge, ligne*64+32+marge)[0]
			if tag<=64:
				position[ligne][colonne] = "R"
			else:
				if (tag==65 or tag==72) and position[ligne][colonne] != "tourN":
					position[ligne][colonne] = "tourN"
					coups.append(("T", False, colonne, ligne))
				elif (tag==66 or tag==71) and position[ligne][colonne] != "cavalierN":
					position[ligne][colonne] = "cavalierN"
					coups.append(("C", False, colonne, ligne))
				elif (tag==67 or tag==70) and position[ligne][colonne] != "fouN":
					position[ligne][colonne] = "fouN"
					coups.append(("F", False, colonne, ligne))
				elif tag==68 and position[ligne][colonne] != "dameN":
					position[ligne][colonne] = "dameN"
					coups.append(("D", False, colonne, ligne))
				elif tag==69 and position[ligne][colonne] != "roiN": 
					position[ligne][colonne] = "roiN"
					coups.append(("R", False, colonne, ligne))
				elif (tag>=73 and tag<=80) and position[ligne][colonne] != "pionN":
					position[ligne][colonne] = "pionN"
					coups.append(("P", False, colonne, ligne))
				elif (tag==89 or tag==96) and position[ligne][colonne] != "tourB":
					position[ligne][colonne] = "tourB"
					coups.append(("T", False, colonne, ligne))
				elif (tag==90 or tag==95) and position[ligne][colonne] != "cavalierB":
					position[ligne][colonne] = "cavalierB"
					coups.append(("C", False, colonne, ligne))
				elif (tag==91 or tag==94) and position[ligne][colonne] != "fouB":
					position[ligne][colonne] = "fouB"
					coups.append(("F", False, colonne, ligne))
				elif tag==92 and position[ligne][colonne] != "dameB":
					position[ligne][colonne] = "dameB"
					coups.append(("D", False, colonne, ligne))
				elif tag==93 and position[ligne][colonne] != "roiB": 
					position[ligne][colonne] = "roiB"
					coups.append(("R", False, colonne, ligne))
				elif (tag>=81 and tag<=88) and position[ligne][colonne] != "pionB":
					position[ligne][colonne] = "pionB"
					coups.append(("P", False, colonne, ligne))"""

def positionDepart(piece, event):
	global posX, posY, pieceSelect
	posX = (event.x-44)//64
	posY = (event.y-44)//64
	"""for x in range(0,8):
		for y in range(0,8):
			if coupAutorise(piece, posX, posY, x, y):
				print("testA",x, y)
				case = echiquier.find_withtag("cases")[y*8+x]
				echiquier.itemconfig(case, fill="blue")
				pieceSelect = piece"""


def deplacerPieces(piece, event):
    x=event.x
    y=event.y
    echiquier.coords(CURRENT,x,y)
    echiquier.update()

def relacherPieces(piece, event):
	global joueur, position, nbreCoups, coups, capture
	x=event.x
	y=event.y
	X = (x-44)//64
	Y = (y-44)//64
	if X<0 or X>7 or Y<0 or Y>7 or (X==posX and Y==posY):		#pour que les pièces ne débordent pas de l'échiquier ou que le joueur ne reste pas sur place
		echiquier.coords(CURRENT, posX*64+32+marge, posY*64+32+marge)
		echiquier.update()
	else:
		posiTemp = position[Y][X]
		position[Y][X] = position[posY][posX]
		position[posY][posX] = "R"
		if coupLegal():
			position[posY][posX] = position[Y][X]
			position[Y][X] = posiTemp
			if coupAutorise(piece, posX, posY, X, Y):
				position[Y][X] = position[posY][posX]
				position[posY][posX] = "R"
				coups.append((position[Y][X][0], capture, posX, posY, X, Y))
				capture = False
				echiquier.coords(CURRENT, X*64+32+marge, Y*64+32+marge)
				echiquier.update()
				if joueur=="blanc":
					joueur="noir"
				else:
					joueur="blanc"
				if not(coupLegal()):
					showwarning('Alerte!', 'Echec! :)')
			else:
				echiquier.coords(CURRENT, posX*64+32+marge, posY*64+32+marge)
				echiquier.update()
		else:
			position[posY][posX] = position[Y][X]
			position[Y][X] = posiTemp
			echiquier.coords(CURRENT, posX*64+32+marge, posY*64+32+marge)
			echiquier.update()

def capturePiece(X, Y):
	global capture
	piece = echiquier.find_enclosed(X*64+32+marge-32, Y*64+32+marge-32, X*64+32+marge+32, Y*64+32+marge+32)[0] #detecte la piece aux coords X, Y
	echiquier.delete(piece)
	capture = True
	print("done!")

def coupLegal():
	x = 0
	y = 0
	danger = False
	if joueur=="blanc":
		####Première étape, trouver le roi####
		while y<=7 and position[y][x] != "roiB":
			x += 1
			if x==8:
				x=0
				y+=1
		if y==8:
			print(position)
			print("Erreur")
			return True

		####Scanne la ligne####
		if x!=0:
			for i in range(0, x):
				if position[y][i] == "tourN" or position[y][i] == "dameN" or (position[y][i] == "roiN" and i==x-1):
					danger = True
				elif position[y][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x != 7:
			x1=x+1
			while x1<=7 and position[y][x1] == "R":
				x1+=1
			if x1!=8 and (position[y][x1] == "dameN" or position[y][x1] == "tourN" or (position[y][x1] == "roiN" and x1==x+1)):
				return False

		####Scanne la colonne####
		if y!=0:
			for i in range(0, y):
				if position[i][x] == "tourN" or position[i][x] == "dameN" or (position[i][x] == "roiN" and i==y-1):
					danger = True
				elif position[i][x] != "R":
					danger = False
		if danger:
			return not(danger)
		if y != 7:
			y1 = y+1
			while y1<=7 and position[y1][x] == "R":
				y1+=1
			if y1!=8 and (position[y1][x] == "dameN" or position[y1][x] == "tourN" or (position[y1][x] == "roiN" and y1==y+1)):
				return False

		####Scanne la diagonale####
		if x!=0 and y!=0:
			if x>y:
				debut = x-y
			else:
				debut = 0
			for i in range(debut, x):
				if position[y-x+i][i] == "fouN" or position[y-x+i][i] == "dameN" or (position[y-x+i][i] == "roiN" and i==x-1) or (position[y-x+i][i] == "pionN" and i==x-1):
					danger = True
				elif position[y-x+i][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x!=7 and y!=7:
			x1 = x+1
			while y-x+x1<=7 and x1<=7 and position[y-x+x1][x1] == "R":
				x1+=1
			if y-x+x1!=8 and x1!=8 and (position[y-x+x1][x1] == "fouN" or position[y-x+x1][x1] == "dameN" or (position[y-x+x1][x1] == "roiN" and x1==x+1)):
				return False

		####Scanne l'autre diagonale####
		if x!=0 and y!=7:
			if y+x>7:
				debut = y+x-7
			else:
				debut = 0
			for i in range(debut, x):
				if position[y+x-i][i] == "fouN" or position[y+x-i][i] == "dameN" or (position[y+x-i][i] == "roiN" and i==x-1):
					danger = True
				elif position[y+x-i][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x!=7 and y!=0:
			x1 = x+1
			while y+x-x1>=0 and x1<=7 and position[y+x-x1][x1] == "R":
				x1+=1
			if y+x-x1!=-1 and x1!=8 and (position[y+x-x1][x1] == "fouN" or position[y+x-x1][x1] == "dameN" or (position[y+x-x1][x1] == "roiN" and x1==x+1) or (position[y+x-x1][x1] == "pionN" and x1==x+1)):
				return False
		####Scanne le cavalier#####
		if y>=2 and x<=6 and position[y-2][x+1] == "cavalierN":
			return False
		elif y>=1 and x<=5 and position[y-1][x+2] == "cavalierN":
			return False
		elif y<=6 and x<=5 and position[y+1][x+2] == "cavalierN":
			return False
		elif y<=5 and x<=6 and position[y+2][x+1] == "cavalierN":
			return False
		elif y<=5 and x>=1 and position[y+2][x-1] == "cavalierN":
			return False
		elif y<=6 and x>=2 and position[y+1][x-2] == "cavalierN":
			return False
		elif y>=1 and x>=2 and position[y-1][x-2] == "cavalierN":
			return False
		elif y>=2 and x>=1 and position[y-2][x-1] == "cavalierN":
			return False


	elif joueur=="noir":
		####Première étape, trouver le roi####
		while y<=7 and position[y][x] != "roiN":
			x += 1
			if x==8:
				x=0
				y+=1
		if y==8:
			print(position)
			print("Erreur")
			return True

		####Scanne la ligne####
		if x!=0:
			for i in range(0, x):
				if position[y][i] == "tourB" or position[y][i] == "dameB" or (position[y][i] == "roiB" and i==x-1):
					danger = True
				elif position[y][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x != 7:
			x1=x+1
			while x1<=7 and position[y][x1] == "R":
				x1+=1
			if x1!=8 and (position[y][x1] == "dameB" or position[y][x1] == "tourB" or (position[y][x1] == "roiB" and x1==x+1)):
				return False

		####Scanne la colonne####
		if y!=0:
			for i in range(0, y):
				if position[i][x] == "tourB" or position[i][x] == "dameB" or (position[i][x] == "roiB" and i==y-1):
					danger = True
				elif position[i][x] != "R":
					danger = False
		if danger:
			return not(danger)
		if y != 7:
			y1 = y+1
			while y1<=7 and position[y1][x] == "R":
				y1+=1
			if y1!=8 and (position[y1][x] == "dameB" or position[y1][x] == "tourB" or (position[y1][x] == "roiB" and y1==y+1)):
				return False

		####Scanne la diagonale####
		if x!=0 and y!=0:
			if x>y:
				debut = x-y
			else:
				debut = 0
			for i in range(debut, x):
				if position[y-x+i][i] == "fouB" or position[y-x+i][i] == "dameB" or (position[y-x+i][i] == "roiB" and i==x-1):
					danger = True
				elif position[y-x+i][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x!=7 and y!=7:
			x1 = x+1
			while y-x+x1<=7 and x1<=7 and position[y-x+x1][x1] == "R":
				x1+=1
			if y-x+x1!=8 and x1!=8 and (position[y-x+x1][x1] == "fouB" or position[y-x+x1][x1] == "dameB" or (position[y-x+x1][x1] == "roiB" and x1==x+1)  or (position[y-x+x1][x1] == "pionB" and x1==x+1)):
				return False

		####Scanne l'autre diagonale####
		if x!=0 and y!=7:
			if y+x>7:
				debut = y+x-7
			else:
				debut = 0
			for i in range(debut, x):
				if position[y+x-i][i] == "fouB" or position[y+x-i][i] == "dameB" or (position[y+x-i][i] == "roiB" and i==x-1)  or (position[y+x-i][i] == "pionB" and i==x-1):
					danger = True
				elif position[y+x-i][i] != "R":
					danger = False
		if danger:
			return not(danger)
		if x!=7 and y!=0:
			x1 = x+1
			while y+x-x1>=0 and x1<=7 and position[y+x-x1][x1] == "R":
				x1+=1
			if y+x-x1!=-1 and x1!=8 and (position[y+x-x1][x1] == "fouB" or position[y+x-x1][x1] == "dameB" or (position[y+x-x1][x1] == "roiB" and x1==x+1)):
				return False
		####Scanne le cavalier#####
		if y>=2 and x<=6 and position[y-2][x+1] == "cavalierB":
			return False
		elif y>=1 and x<=5 and position[y-1][x+2] == "cavalierB":
			return False
		elif y<=6 and x<=5 and position[y+1][x+2] == "cavalierB":
			return False
		elif y<=5 and x<=6 and position[y+2][x+1] == "cavalierB":
			return False
		elif y<=5 and x>=1 and position[y+2][x-1] == "cavalierB":
			return False
		elif y<=6 and x>=2 and position[y+1][x-2] == "cavalierB":
			return False
		elif y>=1 and x>=2 and position[y-1][x-2] == "cavalierB":
			return False
		elif y>=2 and x>=1 and position[y-2][x-1] == "cavalierB":
			return False


	return True



def coupAutorise(piece, posX, posY, X, Y):
#----------------------------------------------------Trait aux blancs----------------------------------------------------#
#
#
	if piece>15 and piece<=31:
		if joueur == "noir":
			#showwarning("Alerte", "C'est aux noirs de jouer") #showwarning/showerror à voir ###Showwarning fait buguer echiquier.coords ???
			return False
		else:

###################################################TOUR BLANCHE#########################################################

			if piece==24 or piece==31:
				for ligne in range(min(posY, Y), max(posY, Y)+1):
					for colonne in range(min(posX, X), max(posX, X)+1):
						if position[ligne][colonne] != "R" and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
							return False
				if position[Y][X] == "R":
					return X==posX or Y==posY
				elif position[Y][X][-1] == "N" and (X==posX or Y==posY):
					capturePiece(X, Y)
					return True
				else:
					return False

###################################################CAVALIER BLANC#######################################################

			elif piece==25 or piece==30:
				if position[Y][X] == "R":
					return (abs(posX-X)==2 and abs(posY-Y)==1) or (abs(posX-X)==1 and abs(posY-Y)==2)
				elif position[Y][X][-1] == "N":
					if (abs(posX-X)==2 and abs(posY-Y)==1) or (abs(posX-X)==1 and abs(posY-Y)==2):
						capturePiece(X, Y)
						return True
					else:
						return False
				else:
					return False

###################################################FOU BLANC############################################################

			elif piece==26 or piece==29:
				if (X>posX and Y>posY) or (X<posX and Y<posY):
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							#print(ligne, colonne, ligne-min(posY,Y), colonne-min(posX,X), position[ligne][colonne], "\n")
							if position[ligne][colonne] != "R" and (ligne-min(posY,Y)==colonne-min(posX,X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				else:
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							#print(ligne, colonne, ligne+colonne, max(posY, Y)+min(posX, X), position[ligne][colonne], "\n")
							if position[ligne][colonne] != "R" and (ligne+colonne==max(posY, Y)+min(posX, X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				if position[Y][X][-1] == "N" and abs(posX-X)==abs(posY-Y):
					capturePiece(X, Y)
					return True
				else:
					return position[Y][X] == "R" and abs(posX-X)==abs(posY-Y)

###################################################DAME BLANCHE##########################################################

			elif piece==27:
				if (X==posX or Y==posY):
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							if position[ligne][colonne] != "R" and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				else:
					if (X>posX and Y>posY) or (X<posX and Y<posY):
						for ligne in range(min(posY, Y), max(posY, Y)+1):
							for colonne in range(min(posX, X), max(posX, X)+1):
								if position[ligne][colonne] != "R" and (ligne-min(posY,Y)==colonne-min(posX,X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
									return False
					else:
						for ligne in range(min(posY, Y), max(posY, Y)+1):
							for colonne in range(min(posX, X), max(posX, X)+1):
								if position[ligne][colonne] != "R" and (ligne+colonne==max(posY, Y)+min(posX, X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
									return False
				if position[Y][X][-1] == "N" and ((abs(posX-X)==abs(posY-Y)) or (X==posX or Y==posY)):
					capturePiece(X, Y)
					return True
				return position[Y][X] == "R" and (abs(posX-X)==abs(posY-Y)) or (X==posX or Y==posY)

###################################################ROI BLANC############################################################

			elif piece==28:
				if position[Y][X] != "R" and position[Y][X][-1] != "N":
					return False
				elif abs(posX-X)<=1 and abs(posY-Y)<=1 and position[Y][X][-1] == "N":
					capturePiece(X, Y)
					return True
				if Y==7 and X==2 and position[Y][0]=="tourB" and position[Y][1]=="R" and position[Y][2]=="R" and position[Y][3]=="R" and position[Y][4] =="roiB":
					position[Y][3] = "roiB"
					position[Y][4] =  "R"
					if coupLegal():
						position[Y][3] = "R"
						position[Y][4] = "roiB"
						coup = 0
						nbreCoups = len(coups)-2
						print(nbreCoups)
						while coup!=nbreCoups and (coups[coup][0]!="t" or coups[coup][2]!=0 or coups[coup][3]!=Y) and (coups[coup][0]!="r"):
							coup+=2
						if coup==nbreCoups:
							piece = echiquier.find_enclosed(0*64+32+marge-32, Y*64+32+marge-32, 0*64+32+marge+32, Y*64+32+marge+32)[0]
							echiquier.coords(piece, 3*64+32+marge, 7*64+32+marge)
							position[7][0] = "R"
							position[7][3] = "tourB"
							return True
					else:
						position[Y][3] = "R"
						position[Y][4] = "roiB"
				elif Y==7 and X==6 and position[Y][4]=="roiB" and position[Y][5]=="R" and position[Y][6]=="R" and position[Y][7] =="tourB":
					position[Y][5] = "roiB"
					position[Y][4] =  "R"
					if coupLegal():
						position[Y][5] = "R"
						position[Y][4] = "roiB"
						coup = 0
						nbreCoups = len(coups)-2
						print(nbreCoups)
						while coup!=nbreCoups and (coups[coup][0]!="t" or coups[coup][2]!=7 or coups[coup][3]!=Y) and (coups[coup][0]!="r"):
							coup+=2
						if coup==nbreCoups:
							piece = echiquier.find_enclosed(7*64+32+marge-32, 7*64+32+marge-32, 7*64+32+marge+32, 7*64+32+marge+32)[0]
							echiquier.coords(piece, 5*64+32+marge, 7*64+32+marge)
							position[7][7] = "R"
							position[7][5] = "tourB"
							return True
					else:
						position[Y][5] = "R"
						position[Y][4] = "roiB"

				return abs(posX-X)<=1 and abs(posY-Y)<=1

###################################################PIONS BLANCS##########################################################

			elif piece>=16 and piece<=23:
				if position[Y][X][-1] == "N" and posY-Y==1 and abs(posX-X)==1:
					capturePiece(X, Y)
					return True
				for ligne in range(Y, posY):
					if position[ligne][X] != "R":
						return False
				if Y==2 and coups[-1][0] == "p" and coups[-1][4] == X and coups[-1][3]+2==coups[-1][5] and posY==3 and abs(posX-X)==1:
					position[Y+1][X] = "R"
					capturePiece(X, (Y+1))
					return True
				if posY==6:
					return (posY-Y<=2 and posY>Y and posX==X)
				else:
					return (posY-Y<=1 and posY>Y and posX==X)



#----------------------------------------------------Trait aux noirs----------------------------------------------------#
#
#
	elif piece>=0 and piece<=15:
		if joueur == "blanc":
			#showinfo("Alerte", "C'est aux blancs de jouer")
			return False
		else:

###################################################TOUR NOIRE###########################################################

			if piece==0 or piece==7:
				for ligne in range(min(posY, Y), max(posY, Y)+1):
					for colonne in range(min(posX, X), max(posX, X)+1):
						if position[ligne][colonne] != "R" and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
							return False
				if position[Y][X] == "R":
					return X==posX or Y==posY
				elif position[Y][X][-1] == "B" and (X==posX or Y==posY):
					capturePiece(X, Y)
					return True
				else:
					return False

###################################################CAVALIER NOIR########################################################

			elif piece==1 or piece==6:
				if position[Y][X] == "R":
					return (abs(posX-X)==2 and abs(posY-Y)==1) or (abs(posX-X)==1 and abs(posY-Y)==2)
				elif position[Y][X][-1] == "B":
					if (abs(posX-X)==2 and abs(posY-Y)==1) or (abs(posX-X)==1 and abs(posY-Y)==2):
						capturePiece(X, Y)
						return True
					else:
						return False
				else:
					return False

####################################################FOU NOIR############################################################

			elif piece==2 or piece==5:
				if (X>posX and Y>posY) or (X<posX and Y<posY):
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							#print(ligne, colonne, ligne-min(posY,Y), colonne-min(posX,X), position[ligne][colonne], "\n")
							if position[ligne][colonne] != "R" and (ligne-min(posY,Y)==colonne-min(posX,X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				else:
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							#print(ligne, colonne, ligne+colonne, max(posY, Y)+min(posX, X), position[ligne][colonne], "\n")
							if position[ligne][colonne] != "R" and (ligne+colonne==max(posY, Y)+min(posX, X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				if position[Y][X][-1] == "B" and abs(posX-X)==abs(posY-Y):
					capturePiece(X, Y)
					return True
				else:
					return position[Y][X] == "R" and abs(posX-X)==abs(posY-Y)

###################################################DAME NOIRE###########################################################

			elif piece==3:
				if (X==posX or Y==posY):
					for ligne in range(min(posY, Y), max(posY, Y)+1):
						for colonne in range(min(posX, X), max(posX, X)+1):
							if position[ligne][colonne] != "R" and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
								return False
				else:
					if (X>posX and Y>posY) or (X<posX and Y<posY):
						for ligne in range(min(posY, Y), max(posY, Y)+1):
							for colonne in range(min(posX, X), max(posX, X)+1):
								if position[ligne][colonne] != "R" and (ligne-min(posY,Y)==colonne-min(posX,X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
									return False
					else:
						for ligne in range(min(posY, Y), max(posY, Y)+1):
							for colonne in range(min(posX, X), max(posX, X)+1):
								if position[ligne][colonne] != "R" and (ligne+colonne==max(posY, Y)+min(posX, X)) and (ligne!=posY or colonne!=posX) and (ligne!=Y or colonne!=X):
									return False
				if position[Y][X][-1] == "B" and ((abs(posX-X)==abs(posY-Y)) or (X==posX or Y==posY)):
					capturePiece(X, Y)
					return True
				return position[Y][X] == "R" and (abs(posX-X)==abs(posY-Y)) or (X==posX or Y==posY)

###################################################ROI NOIR#############################################################

			elif piece==4:
				if position[Y][X] != "R" and position[Y][X][-1] != "B":
					return False
				elif abs(posX-X)<=1 and abs(posY-Y)<=1 and position[Y][X][-1] == "B":
					capturePiece(X, Y)
					return True
				return abs(posX-X)<=1 and abs(posY-Y)<=1

###################################################PIONS NOIRS##########################################################

			elif piece>=8 and piece<=15:
				if position[Y][X][-1] == "B" and Y-posY==1 and abs(posX-X)==1:
					capturePiece(X, Y)
					return True
				for ligne in range(posY+1, Y+1):
					if position[ligne][X] != "R":
						return False
				if Y==5 and coups[-1][0] == "p" and coups[-1][4] == X and coups[-1][3]==coups[-1][5]+2 and posY==4 and abs(posX-X)==1:
					position[Y-1][X] = "R"
					capturePiece(X, (Y-1))
					return True
				if posY==1:
					return (Y-posY<=2 and Y>posY and posX==X)
				else:
					return (Y-posY<=1 and Y>posY and posX==X)

	

def nouvellePartie():
	global position, coups
	#showinfo("Début en cours", "Une nouvelle partie est sur le point de débuter")
	position = [["tourN","cavalierN","fouN","dameN","roiN","fouN","cavalierN","tourN"],["pionN","pionN","pionN","pionN","pionN","pionN","pionN","pionN"],["R","R","R","R","R","R","R","R"],["R","R","R","R","R","R","R","R"],["R","R","R","R","R","R","R","R"],["R","R","R","R","R","R","R","R"],["pionB","pionB","pionB","pionB","pionB","pionB","pionB","pionB"],["tourB","cavalierB","fouB","dameB","roiB","fouB","cavalierB","tourB"]]
	coups = []
	placerPieces()

def lancement():
	nouvellePartie()


lancement()
root.mainloop()
