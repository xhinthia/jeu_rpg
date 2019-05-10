import os
import os.path
import random
import sys
from sorts import *

print ("Avez-vous une sauvegarde ? [oui]/[non]")
pml=input()
if pml=="oui":
	sauveg = []
	with open("sauv.txt","r") as f_read:
		for line in f_read:
			line=line.strip()
			sauveg.append(line)
	f_read.close()
	nom=sauveg[0]
	lvl=int(sauveg[1])
	exp=int(sauveg[2])
	vieup=int(sauveg[3])
	forceup=int(sauveg[4])
	defenseup=int(sauveg[5])
	vitesseup=int(sauveg[6])
	pal=int(sauveg[7])
	lootpv=int(sauveg[8])
	lootforce=int(sauveg[9])
	lootdefense=int(sauveg[10])
	lootvitesse=int(sauveg[11])
	degpv=int(sauveg[12])
	degfor=int(sauveg[13])
	degdef=int(sauveg[14])
	degvit=int(sauveg[15])
	keltu=int(sauveg[16])
	immortal=int(sauveg[17])
	norfend=int(sauveg[18])
	amedemo=int(sauveg[19])
	exode=int(sauveg[20])
	armudemo=int(sauveg[21])
	azzin=int(sauveg[22])
	agilistack=int(sauveg[23])
	corrup=int(sauveg[24])
	chassedemo=int(sauveg[25])
	ritsang=int(sauveg[26])
	mourne=int(sauveg[27])
	war=int(sauveg[28])
	oth=int(sauveg[29])
	ombre=int(sauveg[30])
	pacte=int(sauveg[31])
	trans=int(sauveg[32])
	abso=int(sauveg[33])
	poigne=int(sauveg[34])
	renfo=int(sauveg[35])
	anean=int(sauveg[36])
	onde=int(sauveg[37])
	veng=int(sauveg[38])
	souffle=int(sauveg[39])
	serie=int(sauveg[40])
	drain=int(sauveg[41])
	feu=int(sauveg[42])
	ame=int(sauveg[43])
	tuto=int(sauveg[44])
	quete2=int(sauveg[45])
	expmax=int(sauveg[46])
	if int(quete2)==1:
		paldemo=int(sauveg[47])
		palimmo=int(sauveg[48])
		palbarb=int(sauveg[49])
		palelem=int(sauveg[50])
		palfufu=int(sauveg[51])
	print (" __________________")
	print ("()_________________)")
	print ("|                 |")
	print ("|      BONNE      |")
	print ("|   CONTINUATION  |")
	print ("|_________________|")
	print ("()________________)")
	print (" ")
	print (" ")

elif pml=="non":
	if os.path.isfile("sauv.txt")=="true":
		os.remove("sauv.txt")
	nom=input("Quel est ton nom ? ")
	print (" _________________")
	print ("()________________)")
	print ("|                |")
	print ("|    BIENVENUE   |")
	print ("|       ET       |")
	print ("|  BONNE CHANCE  |")
	print ("|________________|")
	print ("()_______________)")
	print (" ")
	print (" ")
	lvl=1
	exp=0
	vieup=1
	forceup=1
	defenseup=1
	vitesseup=1
	pal=0
	lootpv=0
	lootforce=0
	lootdefense=0
	lootvitesse=0
	degpv=0
	degfor=0
	degdef=0
	degvit=0
	keltu=0
	immortal=0
	norfend=0
	amedemo=0
	exode=0
	armudemo=0
	azzin=0
	agilistack=0
	corrup=0
	chassedemo=0
	ritsang=0
	mourne=0
	war=0
	oth=0
	ombre=0
	pacte=0
	trans=0
	abso=0
	poigne=0
	renfo=0
	anean=0
	onde=0
	veng=0
	souffle=0
	serie=0
	drain=0
	feu=0
	ame=0
	tuto=0
	quete2=0
	expmax=5*lvl+lvl*lvl
	if int(tuto)==0:
		print ("Vous voici dans le tutoriel, vous allez apprendre les bases du jeu...")
		print (" ")
		print (" ")
		print ("Afin d'intéragir dans le jeu merci de remplir uniquement les renseignements demandés entre crochets")
		print (" ")
		print ("Par exemple : [enter] à la vue de ceci, pour continuer vous n'avez qu'à appuyer sur 'Entrée'")
		continuer=input("[enter]")
		print (" ")
		print ("Ou encore : [1] frappe pour effectuer une frappe il vous suffit de renseigner '1' et d'appuyer sur 'Entrée'")
		continuer=input("[1]")
		print (" ")
		print (" ")
		print ("votre personnage dispose de 4 caractéristiques différentes :")
		print (" ")
		print ("- la vie : si elle tombe à 0 vous êtes mort")
		print ("- la force : permet d'augmenter vos dégats")
		print ("- la defense : permet de réduire les dégats subis")
		print ("- la vitesse : augmente vos chances de jouer")
		continuer=input("[enter]")
		print (" ")
		print ("A chaque nouveau tour, la vitesse (celle du monstre et la votre) determine vos chances de jouer")
		print (" ")
		print ("Cela reste statistique, il est tout à fait possible donc de jouer 3 fois de suite avec une vitesse égale à celle du monstre et inversement")
		continuer=input("[enter]")
		print (" ")
		print ("Quand vous réussissez un combat, vous récupérez tous vos PV (points de vie) ainsi que de l'expérience qui dépend du niveau du monstre")
		print (" ")
		print ("Une fois que vous avez récolté suffisamment d'expérience, vous montez d'un niveau")
		print (" ")
		print ("vous avez alors le choix d'augmenter une de vos 4 caractéristiques")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		print ("une sauvegarde automatique enregistre votre progression à chaque fin de combat")
		print (" ")
		print ("9 monstres de niveaux progressifs vous sont proposés ainsi qu'un boss de palier")
		continuer=input("[enter]")
		print (" ")
		print ("progressez en battant les monstres de plus en plus fort pour essayer de vaincre le boss et ainsi passer au palier supérieur")
		print (" ")
		print ("Si vous tuez le boss, vous aurez le droit d'ouvrir son coffre qui renferme de puissants objets")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		print (" ")
		print ("Bon voyons un peu comment vous vous débrouillez en combat !")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		nomm="poutch"
		viem=1000
		forcem=5
		defensem=5
		vitessem=1
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		print (" ")
		print ("[1] sanguinaire")
		tutoriel=input()
		if int(tutoriel)==1:
			print (" ")
			print (" ")
			print (str(nomm)+" perd 20 PV !")
			viem=viem-20
			print (" ")
			print (" ")
			print (str(nom)+" gagne 5 PV !")
			print (" ")
			continuer=input("[enter]")
			print (" ")
			print (" ")
			print ("Bien joué ! Vous venez d'utiliser votre premier sort !")
			print (" ")
			print ("sanguinaire est un sort très fort, il cause des dégats selon vos points de vie max")
			print (" ")
			print ("Et vous fait regagner une partie des dégats infligés sous forme de PV !")
			print (" ")
			print (" ")
			print ("Essayons le prochain sort !")
			print (" ")
			continuer=input("[enter]")
			print (" ")
			print (" ")
			print ("[2] devaster")
			tutoriel=input()
			if int(tutoriel)==2:
				print (" ")				
				print (" ")
				print (str(nomm)+" perd 25 PV !")
				viem=viem-25
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				print ("Bravo ! vous avez utiliser votre deuxième compétence !")
				print (" ")
				print ("devaster est un sort qui inflige beaucoup de dégats en fonction de votre force")
				print (" ")
				print (" ")
				print ("Suivant !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				print ("[3] coup de bouclier")
				tutoriel=input()
				if int(tutoriel)==3:
					print (" ")
					print (" ")
					print (str(nomm)+" perd 17 PV !")
					viem=viem-17
					print (" ")
					print (" ")
					print (str(nomm)+" perd 4 de defense !")
					defensem=defensem-2
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					print ("coup de bouclier permet d'effectuer des dégats en fonction de votre force et de votre defense")
					print (" ")
					print ("tout en diminuant la defense de votre adversaire !")
					print (" ")
					print ("comme votre defense réduit les dégats ennemis, vos dégats sont réduits par la defense des monstres")
					print (" ")
					print (" ")
					print ("Le dernier sort !")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					print ("[4] enchainement")
					tutoriel=input()
					if int(tutoriel)==4:
						print (" ")
						print (" ")
						print (str(nomm)+"perd 13 PV !")
						viem=viem-13
						print (" ")
						print (" ")
						print ("Votre combo passe à 2")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print ("Euh... C'est quoi ce sort nul ?")
						print (" ")
						print ("Relances le !")
						print (" ")
						print (" ")
						print ("[4] enchainement")
						tutoriel=input()
						if int(tutoriel)==4:
							print (" ")
							print (" ")
							print (str(nomm)+" perd 21 PV !")
							viem=viem-21
							print (" ")
							print (" ")
							print ("votre combo passe à 3")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print ("C'est bien mieux !")
							print (" ")
							print ("Et ca sera de plus en plus fort... Au plus ton combo monte au plus enchainement fait de dégats !")
							print (" ")
							print ("Un sort puissant si tu as beaucoup de vitesse, en plus ses dégats augmentent en fonction de ta vitesse et de ta force!")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print ("Le tutoriel s'achève ici, tu es prêt à commencer ton ascension dans les paliers !")
							print (" ")
							print ("Ah oui une derniere chose ! Quand tu fais un sort, celui-ci monte d'un niveau...")
							print (" ")
							print ("Et arrivé à un certain niveau, ton sort devient plus fort !")
							print (" ")
							continuer=input("[enter] Terminer le tutoriel")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							print (" ")
							tuto=1


	print ("Nos plus grands champions vous proposent des défis pour prouver votre détermination")
	print (" ")
	print ("Courage héro, la récompense sera à la hauteur du défi...")
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print (nom)
	print (lvl)
	print ("PV = "+str(96+32*vieup+lootpv))
	print ("force = "+str(32+8*forceup+lootforce))
	print ("defense = "+str(16+4*defenseup+lootdefense))
	print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print ("vous ne pouvez choisir qu'une quête, alors choisissez bien...")
	print (" ")
	print ("[1] quête : Le sort d'immortalité de Kel'Thuzad (pour ceux qui aiment les PV)")
	print ("[2] quête : Libérer Frostmourne en Norfendre (pour ceux qui aiment la force)")
	print ("[3] quête : L'exode de Thrall des terres arides (pour ceux qui aiment la defense)")
	print ("[4] quête : Maîtriser les Lames d'Azzinoth (pour ceux qui aiment la vitesse)")
	print ("[5] quête : Eradiquer la corruption de Gul'Dan (pour ceux qui ne savent pas se décider...)")
	quete=input()
	print (" ")
	print (" ")
	print (" ")
	if int(quete)==1:
		keltu=1
		print ("Montrez la preuve de votre immortalité... (gagner 300 000 PV)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		immortal=0
		print ("Egaler la vie de Kel'Thuzad... (atteindre 2450 PV)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif int(quete)==2:
		norfend=1
		print ("Augmenter votre force pour manier Frostmourne... (atteindre 700 force)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Arracher l'âme d'un puissant demon pour nourrir Frostmourne... (tuer le demon primordial lvl 50)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		amedemo=0
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif int(quete)==3:
		exode=1
		print ("Detruire les armures démoniaques... (enlever 75 000 defense)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		armudemo=0
		print ("Forger une armure légendaire pour Thrall... (atteindre 300 defense)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif int(quete)==4:
		azzin=1
		print ("Deplacer vous plus vite qu'Illidan... (atteindre 300 vitesse)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Prouver votre agilité au combat... (effectuer 8 000 combos)")
		print (" ")
		continuer=input("[enter]")
		agilistack=0
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif int(quete)==5:
		corrup=1
		print ("Eliminer des demons pour chasser la corruption... (tuer 13 000 demons)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		chassedemo=0
		print ("Terroriser Gul'Dan par votre puissance... (atteindre 750 PV, 180 force, 80 defense et 80 vitesse)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
else:
	exit()

while int(pal)<250:
	totalpv=96+32*vieup+lootpv
	frost=32+8*forceup+lootforce
	armuleg=16+4*defenseup+lootdefense
	vitilli=16+4*vitesseup+lootvitesse
	gulpv=96+32*vieup+lootpv
	gulfor=32+8*forceup+lootforce
	guldef=16+4*defenseup+lootdefense
	gulvit=16+4*vitesseup+lootvitesse
	if int(keltu)==1:
		print ("quête : "+str(immortal)+"/300 000 PV gagnés")
		print ("quête : "+str(totalpv)+"/2450 PV atteint")
	elif int(norfend)==1:
		print ("quête : "+str(amedemo)+"/1 demon primordial lvl 50 tué")
		print ("quête : "+str(frost)+"/700 force atteinte")
	elif int(exode)==1:
		print ("quête : "+str(armudemo)+"/75 000 defense enlevée")
		print ("quête : "+str(armuleg)+"/300 defense atteinte")
	elif int(azzin)==1:
		print ("quête : "+str(vitilli)+"/300 vitesse atteinte")
		print ("quête : "+str(agilistack)+"/8 000 stack")
	elif int(corrup)==1:
		print ("quête : "+str(chassedemo)+"/13 000 démons tués")
		print ("quête : "+str(gulpv)+"/750 PV atteint")
		print ("quête : "+str(gulfor)+"/180 force atteinte")
		print ("quête : "+str(guldef)+"/80 defense atteinte")
		print ("quête : "+str(gulvit)+"/80 vitesse atteinte")
	print (" ")
	print (" ")

	print ("[1] demon lvl "+str(1+pal)+"							PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
	print ("[2] demon lvl "+str(2+pal)+"							force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
	print ("[3] demon lvl "+str(3+pal)+"							defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
	print ("[4] demon lvl "+str(4+pal)+"							vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
	print ("[5] demon lvl "+str(5+pal))
	print ("[6] demon lvl "+str(6+pal)+"							niveau = "+str(lvl))
	print ("[7] demon lvl "+str(7+pal)+"							expérience = "+str(exp)+" / "+str(expmax))
	print ("[8] demon lvl "+str(8+pal))
	print ("[9] demon lvl "+str(9+pal))
	if int(pal)==240:
		print ("[10] demon primordial lvl "+str(10+pal)+" , gardien de la porte")
	else:
		print ("[10] demon primordial lvl "+str(10+pal))
	print ("[0] quitter")
	choix1=input()
	if int(choix1)==0:
		exit()
	elif int(choix1)==1:
		lvlm=1+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=31+8*lvlm
		defensem=15+3*lvlm
		vitessem=14+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !			"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							if int(force)<0:
								force=0
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==2:
		lvlm=2+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=107+24*lvlm
		forcem=32+8*lvlm
		defensem=15+3*lvlm
		vitessem=14+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==3:
		lvlm=3+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=109+24*lvlm
		forcem=33+8*lvlm
		defensem=16+3*lvlm
		vitessem=14+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==4:
		lvlm=4+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=111+24*lvlm
		forcem=34+8*lvlm
		defensem=16+3*lvlm
		vitessem=14+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")	
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==5:
		lvlm=5+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=113+24*lvlm
		forcem=35+8*lvlm
		defensem=17+3*lvlm
		vitessem=15+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==6:
		lvlm=6+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=115+24*lvlm
		forcem=35+8*lvlm
		defensem=16+3*lvlm
		vitessem=17+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==7:
		lvlm=7+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=117+24*lvlm
		forcem=37+6*lvlm
		defensem=18+3*lvlm
		vitessem=15+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")							
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==8:
		lvlm=8+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=119+24*lvlm
		forcem=38+6*lvlm
		defensem=18+3*lvlm
		vitessem=15+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")							
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")	
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==9:
		lvlm=9+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon lvl "+str(lvlm)
		viem=121+24*lvlm
		forcem=39+6*lvlm
		defensem=19+3*lvlm
		vitessem=16+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")	
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==10:
		lvlm=10+pal
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		nomm="demon primordial" 
		viem=125+30*lvlm
		forcem=41+10*lvlm
		defensem=20+5*lvlm
		vitessem=16+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=75:
							print ("[2] pacte de sang")
						if int(lvl)>=80:
							print ("[3] transfert")
						if int(lvl)>=90:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=75:
							print ("[2] poigne de la mort")
						if int(lvl)>=80:
							print ("[3] renforcement")
						if int(lvl)>=90:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=75:
							print ("[2] onde de choc")
						if int(lvl)>=80:
							print ("[3] berserker")
						if int(lvl)>=90:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=75:
							print ("[2] préméditation")
						if int(lvl)>=80:
							print ("[3] serie meutriere")
						if int(lvl)>=90:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=80:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=90:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=75:
							print ("[2] drainage")
						if int(lvl)>=80:
							print ("[3] conversion")
						if int(lvl)>=90:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=75:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=80:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=90:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=90 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")					
					lot=input("vous ouvrez le coffre de loot...")
					print (" ")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					loot = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
					lootchoice=random.choice(loot)
					if int(lootchoice)==1:
						print ("vous gagnez le coeur de Kel'Thuzad !")
						print (" ")
						print ("+ "+str(40+pal)+" PV !")
						lootpv=lootpv+40+pal
					elif int(lootchoice)==2:
						print ("vous gagnez la lame d'Arthas !")
						print (" ")
						print ("+ "+str(9+pal//4)+" force !")
						lootforce=lootforce+9+pal//4
					elif int(lootchoice)==3:
						print ("vous gagnez l'armure de Thrall !")
						print (" ")
						print ("+ "+str(4+pal//8)+" defense !")
						lootdefense=lootdefense+4+pal//8
					elif int(lootchoice)==4:
						print ("vous gagnez les ailes d'Illidan !")
						print (" ")
						print ("+ "+str(4+pal//8)+" vitesse !")
						lootvitesse=lootvitesse+4+pal//8
					elif int(lootchoice)==5:
						print ("vous gagnez le crâne de Gul'dan !")
						print (" ")
						print ("+ "+str(10+pal//3)+" PV !")
						print ("+ "+str(3+pal//5)+" force !")
						print ("+ "+str(1+pal//10)+" defense !")
						print ("+ "+str(1+pal//10)+" vitesse !")
						lootpv=lootpv+10+pal//3
						lootforce=lootforce+3+pal//5
						lootdefense=lootdefense+1+pal//10
						lootvitesse=lootvitesse+1+pal//10
					elif int(lootchoice)==6:
						print ("|===================|")
						print ("|                   |")
						print ("| ORBE PRIMORDIALE  |")
						print ("|     LEGENDAIRE    |")
						print ("|                   |")
						print ("|===================|")
						print (" ")
						print (" ")
						print ("Quelle caractéristique voulez-vous augmenter ?")
						print (" ")
						print ("[1] PV")
						print ("[2] force")
						print ("[3] defense")
						print ("[4] vitesse")
						print ("[5] les 4")
						leg=input()
						print (" ")
						print (" ")
						if int(leg)==1:
							print ("+"+str(40+pal)+" PV !")
							lootpv=lootpv+40+pal
						elif int(leg)==2:
							print ("+"+str(9+pal//4)+" force !")
							lootforce=lootforce+9+pal//4
						elif int(leg)==3:
							print ("+ "+str(4+pal//8)+" defense !")
							lootdefense=lootdefense+4+pal//8
						elif int(leg)==4:
							print ("+ "+str(4+pal//8)+" vitesse !")
							lootvitesse=lootvitesse+4+pal//8
						elif int(leg)==5:
							print ("+ "+str(10+pal//3)+" PV !")
							print ("+ "+str(3+pal//5)+" force !")
							print ("+ "+str(1+pal//10)+" defense !")
							print ("+ "+str(1+pal//10)+" vitesse !")
							lootpv=lootpv+10+pal//3
							lootforce=lootforce+3+pal//5
							lootdefense=lootdefense+1+pal//10
							lootvitesse=lootvitesse+1+pal//10
					print (" ")
					print (" ")
					continuer=input("[enter]")
					if int(pal)==40:
						amedemo=1
					pal=pal+10
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						print (" ")
						print (" ")
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						if int(keltu)==2 or int(norfend)==2 or int(exode)==2 or int(azzin)==2 or int(corrup)==2:
							if int(lvl)==75 or int(lvl)==80 or int(lvl)==90:
								print ("vous maîtrisez une nouvelle puissance !!!!!")
								print (" ")
					print (" ")
					print (" ")
					print ("  _________________")
					print (" ()________________)")
					print ("  |               |")
					print ("  |     PALIER    |")
					print ("  |     SUIVANT   |")
					print ("  |_______________|")
					print (" ()________________)")
					print (" ")
					print (" ")
					continuer=input("[enter]")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				boss = [1,1,1,2]
				capa=random.choice(boss)
				if int(capa)==1:
					degatm=frappe_ombre(forcem,defense)
					vie=vie-degatm
					print (" ")
					print (" ")
					print (str(nomm)+" utilise frappe de l'ombre...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(capa)==2:
					degatm=destru_primo(forcem,defense)
					vie=vie-degatm
					print (" ")
					print (" ")
					print (str(nomm)+" utilise destruction primordiale !")
					print (str(nomm)+" concentre toute sa puissance dans une orbe démoniaque et vous la lance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass


	if os.path.isfile("sauv.txt")=="true":
		os.remove("sauv.txt")
	fw = open("sauv.txt","w")
	fw.write(str(nom))
	fw.write("\n")
	fw.write(str(lvl))
	fw.write("\n")
	fw.write(str(exp))
	fw.write("\n")
	fw.write(str(vieup))
	fw.write("\n")
	fw.write(str(forceup))
	fw.write("\n")
	fw.write(str(defenseup))
	fw.write("\n")
	fw.write(str(vitesseup))
	fw.write("\n")
	fw.write(str(pal))
	fw.write("\n")
	fw.write(str(lootpv))
	fw.write("\n")
	fw.write(str(lootforce))
	fw.write("\n")
	fw.write(str(lootdefense))
	fw.write("\n")
	fw.write(str(lootvitesse))
	fw.write("\n")
	fw.write(str(degpv))
	fw.write("\n")
	fw.write(str(degfor))
	fw.write("\n")
	fw.write(str(degdef))
	fw.write("\n")
	fw.write(str(degvit))
	fw.write("\n")
	fw.write(str(keltu))
	fw.write("\n")
	fw.write(str(immortal))
	fw.write("\n")
	fw.write(str(norfend))
	fw.write("\n")
	fw.write(str(amedemo))
	fw.write("\n")
	fw.write(str(exode))
	fw.write("\n")
	fw.write(str(armudemo))
	fw.write("\n")
	fw.write(str(azzin))
	fw.write("\n")
	fw.write(str(agilistack))
	fw.write("\n")
	fw.write(str(corrup))
	fw.write("\n")
	fw.write(str(chassedemo))
	fw.write("\n")
	fw.write(str(ritsang))
	fw.write("\n")
	fw.write(str(mourne))
	fw.write("\n")
	fw.write(str(war))
	fw.write("\n")
	fw.write(str(oth))
	fw.write("\n")
	fw.write(str(ombre))
	fw.write("\n")
	fw.write(str(pacte))
	fw.write("\n")
	fw.write(str(trans))
	fw.write("\n")
	fw.write(str(abso))
	fw.write("\n")
	fw.write(str(poigne))
	fw.write("\n")
	fw.write(str(renfo))
	fw.write("\n")
	fw.write(str(anean))
	fw.write("\n")
	fw.write(str(onde))
	fw.write("\n")
	fw.write(str(veng))
	fw.write("\n")
	fw.write(str(souffle))
	fw.write("\n")
	fw.write(str(serie))
	fw.write("\n")
	fw.write(str(drain))
	fw.write("\n")
	fw.write(str(feu))
	fw.write("\n")
	fw.write(str(ame))
	fw.write("\n")
	fw.write(str(tuto))
	fw.write("\n")
	fw.write(str(quete2))
	fw.write("\n")
	fw.write(str(expmax))
	fw.close()
	
	if int(immortal)>=300000 and int(totalpv)>=2450 and int(keltu)==1:
		keltu=2
		immortal=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Kel'Thuzad !!!")
		print (" ")
		print ("Pour vous recompenser, Kel'Thuzad vous transforme en liche...")
		print (" ")
		print ("passif : convertis une partie de vos PV en force, defense et vitesse")
		print (" ")
		print (" ")
		lootforce=lootforce+(96+32*vieup+lootpv)//20
		lootdefense=lootdefense+(96+32*vieup+lootpv)//50
		lootvitesse=lootvitesse+(96+32*vieup+lootpv)//55
		lootpv=lootpv-(96+32*vieup+lootpv)//20-(96+32*vieup+lootpv)//50-(96+32*vieup+lootpv)//55
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		kel=input("[enter]")
		print (" ")
		print (" ")
	elif int(frost)>=700 and int(amedemo)==1 and int(norfend)==1:
		norfend=2
		amedemo=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Frostmourne !!!")
		print (" ")
		print ("Pour vous recompenser, vous vous transformez en chevalier de la mort...")
		print (" ")
		print ("passif : convertis une partie de votre force en vie, defense et vitesse")
		print (" ")
		print (" ")
		lootpv=lootpv+(32+8*forceup+lootforce)*5//8
		lootdefense=lootdefense+(32+8*forceup+lootforce)//13
		lootvitesse=lootvitesse+(32+8*forceup+lootforce)//16
		lootforce=lootforce-(32+8*forceup+lootforce)*5//8-(32+8*forceup+lootforce)//13-(32+8*forceup+lootforce)//16
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		nor=input("[enter]")
		print (" ")
		print (" ")
	elif int(armudemo)>=75000 and int(armuleg)>=300 and int(exode)==1:
		exode=2
		armudemo=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Thrall !!!")
		print (" ")
		print ("Pour vous recompenser, Thrall vous transforme en guerrier...")
		print (" ")
		print ("passif = convertis une partie de votre defense en vie, force et vitesse")
		print (" ")
		print (" ")
		lootpv=lootpv+(16+4*defenseup+lootdefense)*5//4
		lootforce=lootforce+(16+4*defenseup+lootdefense)*4//9
		lootvitesse=lootvitesse+(16+4*defenseup+lootdefense)//8
		lootdefense=lootdefense-(16+4*defenseup+lootdefense)*5//4-(16+4*defenseup+lootdefense)*4//9-(16+4*defenseup+lootdefense)//8
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		exo=input("[enter]")
		print (" ")
		print (" ")
	elif int(vitilli)>=300 and int(agilistack)>=8000 and int(azzin)==1:
		azzin=2
		agilistack=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête d'Illidan !!!")
		print (" ")
		print ("Pour vous recompenser, Illidan vous transforme en chasseur de démons...")
		print (" ")
		print ("passif = convertis une partie de votre vitesse en vie, force et defense")
		print (" ")
		print (" ")
		lootpv=lootpv+(16+4*vitesseup+lootvitesse)*5//4
		lootforce=lootforce+(16+4*vitesseup+lootvitesse)*4//9
		lootdefense=lootdefense+(16+4*vitesseup+lootvitesse)//8
		lootvitesse=lootvitesse-(16+4*vitesseup+lootvitesse)*5//4-(16+4*vitesseup+lootvitesse)*4//9-(16+4*vitesseup+lootvitesse)//8
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		azz=input("[enter]")
		print (" ")
		print (" ")
	elif int(chassedemo)>=13000 and int(gulpv)>=750 and int(gulfor)>=180 and int(guldef)>=80 and int(gulvit)>=80 and int(corrup)==1:
		corrup=2
		chassedemo=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Gul'Dan !!!")
		print (" ")
		print ("Pour vous recompenser, Gul'Dan vous transforme en démoniste...")
		print (" ")
		print ("vous devenez corrompu, vos attaques ignorent la defense de l'adversaire")
		print (" ")
		print (" ")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		corr=input("[enter]")
		print (" ")
		print (" ")
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
if int(quete2)==0:
	print (" ")
	print ("Felicitation, vous avez vaincu le demon qui gardait la porte des mondes !")
	print (" ")
	print ("Vous avez désormais accès à l'ensemble des mondes de cette terre...")
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print ("Vous traversez la porte et vous vous retrouvez face à 4 portails")
	print (" ")
	print ("une ombre apparait et alors que vous sortez votre épée, un simple geste de sa main vous paralyse de la tête au pied !")
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print ("'Chuuut, doucement humain. Je ne te veux aucun mal, je suis le passeur'")
	print (" ")
	print ("'Je suis là pour guider les héros à travers les portails'")
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print ("'Tu as plusieurs choix qui s'offrent à toi...'")
	print (" ")
	print ("'Tu peux continuer à te battre contre les demons et affronter les plus puissants d'entre eux'")
	print ("'Emprunter le premier portail vers le lac des immortels'")
	print ("'Emprunter le deuxième portail vers les terres barbares'")
	print ("'Emprunter le troisième portail vers les montagnes des elementaires'")
	print ("'Emrpunter le quatrième portail vers les îles des pirates'")
	print (" ")
	print (" ")
	print ("'Ne t'inquiète pas tu peux voyager sans limite à travers les portails...'")
	print (" ")
	paldemo=250
	palimmo=250
	palbarb=250
	palelem=250
	palfufu=250
	quete2=1
	continuer=input("[enter]")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
while int(pal)<1000000:
	print ("[1] royaume des démons (caractéristiques équilibrées)")
	print ("[2] lac des immortels (conseil : avoir beaucoup de PV)")
	print ("[3] terres des barbares (conseil : avoir beaucoup d'armure)")
	print ("[4] montagnes des elementaires (conseil : avoir beaucoup de force)")
	print ("[5] îles des pirates (conseil : avoir beaucoup de vitesse)")
	print ("[0] quitter")
	choix5=input()
	if int(choix5)==0:
		palvar=1
		if os.path.isfile("sauv.txt")=="true":
			os.remove("sauv.txt")
		fw = open("sauv.txt","w")
		fw.write(str(nom))
		fw.write("\n")
		fw.write(str(lvl))
		fw.write("\n")
		fw.write(str(exp))
		fw.write("\n")
		fw.write(str(vieup))
		fw.write("\n")
		fw.write(str(forceup))
		fw.write("\n")
		fw.write(str(defenseup))
		fw.write("\n")
		fw.write(str(vitesseup))
		fw.write("\n")
		fw.write(str(pal))
		fw.write("\n")
		fw.write(str(lootpv))	
		fw.write("\n")
		fw.write(str(lootforce))
		fw.write("\n")
		fw.write(str(lootdefense))
		fw.write("\n")
		fw.write(str(lootvitesse))
		fw.write("\n")
		fw.write(str(degpv))
		fw.write("\n")
		fw.write(str(degfor))
		fw.write("\n")
		fw.write(str(degdef))
		fw.write("\n")
		fw.write(str(degvit))
		fw.write("\n")
		fw.write(str(keltu))
		fw.write("\n")
		fw.write(str(immortal))
		fw.write("\n")
		fw.write(str(norfend))
		fw.write("\n")
		fw.write(str(amedemo))
		fw.write("\n")
		fw.write(str(exode))
		fw.write("\n")
		fw.write(str(armudemo))
		fw.write("\n")
		fw.write(str(azzin))
		fw.write("\n")
		fw.write(str(agilistack))
		fw.write("\n")
		fw.write(str(corrup))
		fw.write("\n")
		fw.write(str(chassedemo))
		fw.write("\n")
		fw.write(str(ritsang))
		fw.write("\n")
		fw.write(str(mourne))
		fw.write("\n")
		fw.write(str(war))
		fw.write("\n")
		fw.write(str(oth))
		fw.write("\n")
		fw.write(str(ombre))
		fw.write("\n")
		fw.write(str(pacte))
		fw.write("\n")
		fw.write(str(trans))
		fw.write("\n")
		fw.write(str(abso))
		fw.write("\n")
		fw.write(str(poigne))
		fw.write("\n")
		fw.write(str(renfo))
		fw.write("\n")
		fw.write(str(anean))
		fw.write("\n")
		fw.write(str(onde))
		fw.write("\n")
		fw.write(str(veng))
		fw.write("\n")
		fw.write(str(souffle))
		fw.write("\n")
		fw.write(str(serie))
		fw.write("\n")
		fw.write(str(drain))
		fw.write("\n")
		fw.write(str(feu))
		fw.write("\n")
		fw.write(str(ame))
		fw.write("\n")
		fw.write(str(tuto))
		fw.write("\n")
		fw.write(str(quete2))
		fw.write("\n")
		fw.write(str(expmax))
		fw.write("\n")
		fw.write(str(palvar))
		fw.write("\n")
		fw.write(str(paldemo))
		fw.write("\n")
		fw.write(str(palimmo))
		fw.write("\n")
		fw.write(str(palbarb))
		fw.write("\n")
		fw.write(str(palelem))
		fw.write("\n")
		fw.write(str(palfufu))
		fw.close()
		exit()
	retour=0
	while int(retour)==0:
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
	if int(choix5)==1:
		print ("[1] demon malsain lvl "+str(1+pal)+"             PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
		print ("[2] demon malsain lvl "+str(2+pal)+"             force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
		print ("[3] demon malsain lvl "+str(3+pal)+"             defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
		print ("[4] demon malsain lvl "+str(4+pal)+"             vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
		print ("[5] demon malsain lvl "+str(5+pal))
		print ("[6] demon malsain lvl "+str(6+pal))
		print ("[7] demon malsain lvl "+str(7+pal))
		print ("[8] demon malsain lvl "+str(8+pal))
		print ("[9] demon malsain lvl "+str(9+pal))
		print ("[10] maître demoniaque lvl "+str(10+pal))
		print ("[0] changer de portail")
	elif int(choix5)==2:
		print ("[1] garde immortel lvl "+str(1+pal)+"             PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
		print ("[2] garde immortel lvl "+str(2+pal)+"             force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
		print ("[3] garde immortel lvl "+str(3+pal)+"             defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
		print ("[4] garde immortel lvl "+str(4+pal)+"             vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
		print ("[5] garde immortel lvl "+str(5+pal))
		print ("[6] garde immortel lvl "+str(6+pal))
		print ("[7] garde immortel lvl "+str(7+pal))
		print ("[8] garde immortel lvl "+str(8+pal))
		print ("[9] garde immortel lvl "+str(9+pal))
		print ("[10] roi immortel lvl "+str(10+pal))
		print ("[0] changer de portail")
	elif int(choix5)==3:
		print ("[1] guerrier barbare lvl "+str(1+pal)+"             PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
		print ("[2] guerrier barbare lvl "+str(2+pal)+"             force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
		print ("[3] guerrier barbare lvl "+str(3+pal)+"             defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
		print ("[4] guerrier barbare lvl "+str(4+pal)+"             vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
		print ("[5] guerrier barbare lvl "+str(5+pal))
		print ("[6] guerrier barbare lvl "+str(6+pal))
		print ("[7] guerrier barbare lvl "+str(7+pal))
		print ("[8] guerrier barbare lvl "+str(8+pal))
		print ("[9] guerrier barbare lvl "+str(9+pal))
		print ("[10] seigneur barbare lvl "+str(10+pal))
		print ("[0] changer de portail")
	elif int(choix5)==4:
		print ("[1] elementaire de pierre lvl "+str(1+pal)+"             PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
		print ("[2] elementaire de pierre lvl "+str(2+pal)+"             force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
		print ("[3] elementaire de pierre lvl "+str(3+pal)+"             defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
		print ("[4] elementaire de pierre lvl "+str(4+pal)+"             vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
		print ("[5] elementaire de pierre lvl "+str(5+pal))
		print ("[6] elementaire de pierre lvl "+str(6+pal))
		print ("[7] elementaire de pierre lvl "+str(7+pal))
		print ("[8] elementaire de pierre lvl "+str(8+pal))
		print ("[9] elementaire de pierre  lvl "+str(9+pal))
		print ("[10] elementaire instable lvl "+str(10+pal))
		print ("[0] changer de portail")
	elif int(choix5)==5:
		print ("[1] contrebandier lvl "+str(1+pal)+"             PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
		print ("[2] contrebandier lvl "+str(2+pal)+"             force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
		print ("[3] contrebandier lvl "+str(3+pal)+"             defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
		print ("[4] contrebandier lvl "+str(4+pal)+"             vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
		print ("[5] contrebandier lvl "+str(5+pal))
		print ("[6] contrebandier lvl "+str(6+pal))
		print ("[7] contrebandier lvl "+str(7+pal))
		print ("[8] contrebandier lvl "+str(8+pal))
		print ("[9] contrebandier lvl "+str(9+pal))
		print ("[10] capitaine lvl "+str(10+pal))
		print ("[0] changer de portail")
	choix1=input()
	if int(choix1)==0:
		retour=1
		pass
	elif int(choix1)==1:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=105+30*lvlm
			forcem=31+8*lvlm
			defensem=15+5*lvlm
			vitessem=15+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=1500+650*lvlm
			forcem=5+2*lvlm
			defensem=10+3*lvlm
			vitessem=15+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=105+115*lvlm
			forcem=120+5*lvlm
			defensem=20+2*lvlm
			vitessem=15+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=105+30*lvlm
			forcem=30+6*lvlm
			defensem=20+8*lvlm
			vitessem=15+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=105+30*lvlm
			forcem=33+4*lvlm
			defensem=16+2*lvlm
			vitessem=20+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !			"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							if int(force)<0:
								force=0
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==2:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=135+30*lvlm
			forcem=39+8*lvlm
			defensem=20+5*lvlm
			vitessem=16+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=2150+650*lvlm
			forcem=7+2*lvlm
			defensem=13+3*lvlm
			vitessem=16+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=220+115*lvlm
			forcem=125+5*lvlm
			defensem=22+2*lvlm
			vitessem=16+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=135+30*lvlm
			forcem=36+6*lvlm
			defensem=28+8*lvlm
			vitessem=16+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=135+30*lvlm
			forcem=37+4*lvlm
			defensem=18+2*lvlm
			vitessem=24+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==3:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=165+30*lvlm
			forcem=47+8*lvlm
			defensem=25+5*lvlm
			vitessem=17+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=2800+650*lvlm
			forcem=9+2*lvlm
			defensem=16+3*lvlm
			vitessem=17+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=335+115*lvlm
			forcem=130+5*lvlm
			defensem=24+2*lvlm
			vitessem=17+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=165+30*lvlm
			forcem=42+6*lvlm
			defensem=36+8*lvlm
			vitessem=17+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=165+30*lvlm
			forcem=41+4*lvlm
			defensem=20+2*lvlm
			vitessem=28+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==4:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=195+30*lvlm
			forcem=55+8*lvlm
			defensem=30+5*lvlm
			vitessem=18+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=3450+650*lvlm
			forcem=11+2*lvlm
			defensem=19+3*lvlm
			vitessem=18+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=450+115*lvlm
			forcem=135+5*lvlm
			defensem=26+2*lvlm
			vitessem=18+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=195+30*lvlm
			forcem=48+6*lvlm
			defensem=44+8*lvlm
			vitessem=18+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=195+30*lvlm
			forcem=45+4*lvlm
			defensem=22+2*lvlm
			vitessem=32+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")	
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==5:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=225+30*lvlm
			forcem=63+8*lvlm
			defensem=35+5*lvlm
			vitessem=19+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=4100+650*lvlm
			forcem=13+2*lvlm
			defensem=22+3*lvlm
			vitessem=19+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=565+115*lvlm
			forcem=140+5*lvlm
			defensem=28+2*lvlm
			vitessem=19+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=225+30*lvlm
			forcem=54+6*lvlm
			defensem=52+8*lvlm
			vitessem=19+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=225+30*lvlm
			forcem=49+4*lvlm
			defensem=24+2*lvlm
			vitessem=36+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass
	elif int(choix1)==6:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=255+30*lvlm
			forcem=71+8*lvlm
			defensem=40+5*lvlm
			vitessem=20+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=4750+650*lvlm
			forcem=15+2*lvlm
			defensem=25+3*lvlm
			vitessem=20+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=680+115*lvlm
			forcem=145+5*lvlm
			defensem=30+2*lvlm
			vitessem=20+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=255+30*lvlm
			forcem=60+6*lvlm
			defensem=60+8*lvlm
			vitessem=20+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=255+30*lvlm
			forcem=53+4*lvlm
			defensem=26+2*lvlm
			vitessem=40+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==7:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=285+30*lvlm
			forcem=79+8*lvlm
			defensem=45+5*lvlm
			vitessem=21+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=5400+650*lvlm
			forcem=17+2*lvlm
			defensem=28+3*lvlm
			vitessem=21+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=795+115*lvlm
			forcem=150+5*lvlm
			defensem=32+2*lvlm
			vitessem=21+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=285+30*lvlm
			forcem=66+6*lvlm
			defensem=68+8*lvlm
			vitessem=21+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=285+30*lvlm
			forcem=57+4*lvlm
			defensem=28+2*lvlm
			vitessem=44+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")							
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==8:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=315+30*lvlm
			forcem=87+8*lvlm
			defensem=50+5*lvlm
			vitessem=22+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=6050+650*lvlm
			forcem=19+2*lvlm
			defensem=31+3*lvlm
			vitessem=22+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=810+115*lvlm
			forcem=155+5*lvlm
			defensem=34+2*lvlm
			vitessem=22+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=315+30*lvlm
			forcem=72+6*lvlm
			defensem=76+8*lvlm
			vitessem=22+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=315+30*lvlm
			forcem=61+4*lvlm
			defensem=30+2*lvlm
			vitessem=48+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")							
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")	
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==9:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="demon malsain lvl "+str(lvlm)
			viem=345+30*lvlm
			forcem=95+8*lvlm
			defensem=55+5*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==2:
			nomm="garde immortel lvl "+str(lvlm)
			viem=6700+650*lvlm
			forcem=21+2*lvlm
			defensem=34+3*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==3:
			nomm="guerrier barbare lvl "+str(lvlm)
			viem=925+115*lvlm
			forcem=160+5*lvlm
			defensem=36+2*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire de pierre lvl "+str(lvlm)
			viem=345+30*lvlm
			forcem=78+6*lvlm
			defensem=84+8*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==5:
			nomm="contrebandier lvl "+str(lvlm)
			viem=345+30*lvlm
			forcem=65+4*lvlm
			defensem=32+2*lvlm
			vitessem=52+4*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					print (" ")	
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if int(choix5)==1:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous frappe avec une puissance obscure...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==2:
					degatm=rituel_sanglant(viem,defense)
					vie=vie-degatm
					print (str(nomm)+" lance rituel sanglant...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					viem=viem+degatm//3
					print (str(nomm)+" gagne "+str(degatm//3)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==3:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous met un violent coup de hache !")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print ("Vous saignez...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(vie//45)+" PV !")
					vie=vie-vie//45
					print (" ")
					print (" ")
				elif int(choix5)==4:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous lance un rocher...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				elif int(choix5)==5:
					degatm=coup_demoniaque(forcem,defense)
					vie=vie-degatm
					print (str(nomm)+" vous poignarde...")
					print (" ")
					print (" ")
					print (str(nom)+" perd "+str(degatm)+" PV !")
					print (" ")
					print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	elif int(choix1)==10:
		if int(choix5)==1:
			lvlm=1+paldemo
		elif int(choix5)==2:
			lvlm=1+palimmo
		elif int(choix5)==3:
			lvlm=1+palbarb
		elif int(choix5)==4:
			lvlm=1+palelem
		elif int(choix5)==5:
			lvlm=1+palfufu
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(choix5)==1:
			nomm="maître démoniaque lvl "+str(lvlm)
			viem=345+35*lvlm
			forcem=95+10*lvlm
			defensem=55+6*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==2:
			nomm="roi immortel lvl "+str(lvlm)
			viem=6700+750*lvlm
			forcem=21+2*lvlm
			defensem=34+3*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==3:
			nomm="seigneur barbare lvl "+str(lvlm)
			viem=925+120*lvlm
			forcem=160+7*lvlm
			defensem=36+2*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==4:
			nomm="elementaire instable lvl "+str(lvlm)
			viem=345+30*lvlm
			forcem=78+6*lvlm
			defensem=84+10*lvlm
			vitessem=23+1*lvlm
		elif int(choix5)==5:
			nomm="capitaine lvl "+str(lvlm)
			viem=345+30*lvlm
			forcem=65+4*lvlm
			defensem=32+2*lvlm
			vitessem=52+6*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		while int(vie)>0 and int(viem)>0:
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print ("                                                                           ")
			print ("					"+str(nomm)+"                     "+str(nom))
			print ("					PV = "+str(viem)+"                         PV = "+str(vie))
			print ("					force = "+str(forcem)+"                    force = "+str(force))
			print ("					defense = "+str(defensem)+"                defense = "+str(defense))
			print ("					vitesse = "+str(vitessem)+"                vitesse = "+str(vitesse))
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			vit_liste = []
			i=0
			a=vitesse//10
			b=vitessem//10
			while i<a:
				i=i+1
				vit_liste.append(1)
			i=0
			while i<b:
				i=i+1
				vit_liste.append(2)
			a=random.choice(vit_liste)
			jeu=0
			tour=tour+1
			if int(a)==1:
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] toucher sanglant")
						if int(lvl)>=120:
							print ("[2] pacte de sang")
						if int(lvl)>=140:
							print ("[3] transfert")
						if int(lvl)>=160:
							print ("[4] absorption")
						choix3=input()
						if int(choix3)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//3)+" PV !")
							vie=vie+degat//3
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-----------------------------------------------------------------------------------------")
								print ("                              TOUCHER SANGLANT LVL UP !!!                              ")
								print ("-----------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("-------------------------------------------------------------------------------------------")
								print ("                              "+str(ritsang)+"e TOUCHER SANGLANT !                       ")
								print ("-------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							print (" ")
							print (" ")
							vie=vie-degat
							print (str(nom)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem)+" de defense !")
							defensem=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              PACTE DE SANG LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("------------------------------------------------------------------------------------------")
								print ("                             "+str(pacte)+"e PACTE DE SANG !                              ")
								print ("------------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							print (" ")
							print (" ")
							vie=vie+buff
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense)+" de defense !")
							defense=0
							jeu=1
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              TRANSFERT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(trans)+"e TRANSFERT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ABSO)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(norfend)==2:
						print ("[1] frappe du fléau")
						if int(lvl)>=120:
							print ("[2] poigne de la mort")
						if int(lvl)>=140:
							print ("[3] renforcement")
						if int(lvl)>=160:
							print ("[4] aneantissement")
						choix3=input()
						if int(choix3)==1:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//10)+" de force !")
							force=force+degat//10
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FRAPPE DU FLEAU LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(mourne)+"e FRAPPE DU FLEAU !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2//5
							print (str(nom)+" gagne "+str(debuff*2//5)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              POIGNE DE LA MORT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(poigne)+"e POIGNE DE LA MORT !            ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*4
							defense=defense+buff*7//4
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff*4)+" PV !		"+str(nom)+" gagne "+str(buff*7//4)+" de defense !")
							print (" ")
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print (str(nom)+" perd "+str(buff*2)+" de force !")
							jeu=1
							print (" ")
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              RENFORCEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(renfo)+"e RENFORCEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=aneantissement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str(degat//10)+" de force !")
							force=force-degat//10
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ANEANTISSEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(anean)+"e ANEANTISSEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(exode)==2:
						print ("[1] heurt de bouclier")
						if int(lvl)>=120:
							print ("[2] onde de choc")
						if int(lvl)>=140:
							print ("[3] berserker")
						if int(lvl)>=160:
							print ("[4] dernier souffle")
						choix3=input()
						if int(choix3)==1:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//8)+" de defense !")
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              HEURT DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(war)+"e HEURT DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ONDE DE CHOC LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(onde)+"e ONDE DE CHOC !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              VENGEANCE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(veng)+"e VENGEANCE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(defense//4)+" de defense !")
							vie=vie+buff
							defense=defense-defense//4
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DERNIER SOUFFLE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e DERNIER SOUFFLE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] préméditation")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DANSE DE L'OMBRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(oth)+"e DANSE DE L'OMBRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print (" ")
							print ("Vous planifiez votre prochain coup mais pendant votre réflexion votre vitesse diminue...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(stackvit*stackvit)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous utilisez vos points de combo pour infliger un coup surpuissant !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=0
							print ("Votre combo retombe à "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SERIE MEURTRIERE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(serie)+"e SERIE MEURTRIERE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							vie=vie+vitesse*4
							force=force+vitesse*13//10
							defense=defense+vitesse*3//4
							print (str(nom)+" gagne "+str(vitesse*4)+" PV !		"+str(nom)+" gagne "+str(vitesse*13//10)+" de force !		"+str(nom)+" gagne "+str(vitesse*3//4)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str(vitesse*3//4)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							jeu=1
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] conversion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              OMBREFLAMME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(ombre)+"e OMBREFLAMME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DRAINAGE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(drain)+"e DRAINAGE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((96+32*vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous canalisez la puissance de toutes les âmes dans votre poing...")
							print ("Vous brûlez l'adversaire avec des flammes noires !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							ame=0
							print("Votre stock d'âme démoniaque passe à "+str(ame))
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              FEU DE L'AME LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(feu)+"e FEU DE L'AME !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")		
					else:
						print ("[1] sanguinaire")
						print ("[2] devaster")
						print ("[3] coup de bouclier")
						print ("[4] enchainement")
						choix2=input()
						if int(choix2)==1:
							degat=degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print (" ")
							jeu=1
							print (" ")
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              SANGUINAIRE LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degpv)+"e SANGUINAIRE !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              DEVASTER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degfor)+"e DEVASTER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")	
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat//10)+" de defense !")
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              COUP DE BOUCLIER LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degdef)+"e COUP DE BOUCLIER !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							stackvit=stackvit+1
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ENCHAINEMENT LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(degvit)+"e ENCHAINEMENT !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
				if int(viem)<=0:
					print (" ")
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(lvl)>=160 and int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")					
					lot=input("vous ouvrez le coffre de loot...")
					print (" ")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					loot = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
					lootchoice=random.choice(loot)
					if int(choix5)==1:
						if int(lootchoice)==1:
							print ("vous gagnez un coeur de demon !")
							print (" ")
							print ("+ "+str(80+paldemo)+" PV !")
							lootpv=lootpv+80+paldemo
						elif int(lootchoice)==2:
							print ("vous gagnez un bras de demon !")
							print (" ")
							print ("+ "+str(18+paldemo//4)+" force !")
							lootforce=lootforce+18+paldemo//4
						elif int(lootchoice)==3:
							print ("vous gagnez un os de demon !")
							print (" ")
							print ("+ "+str(8+paldemo//8)+" defense !")
							lootdefense=lootdefense+8+paldemo//8
						elif int(lootchoice)==4:
							print ("vous gagnez une jambe de demon !")
							print (" ")
							print ("+ "+str(8+paldemo//8)+" vitesse !")
							lootvitesse=lootvitesse+8+paldemo//8
						elif int(lootchoice)==5:
							print ("vous gagnez une tête de demon !")
							print (" ")
							print ("+ "+str(20+paldemo//3)+" PV !")
							print ("+ "+str(6+paldemo//5)+" force !")
							print ("+ "+str(2+paldemo//10)+" defense !")
							print ("+ "+str(2+paldemo//10)+" vitesse !")
							lootpv=lootpv+20+paldemo//3
							lootforce=lootforce+4+paldemo//5
							lootdefense=lootdefense+2+paldemo//10
							lootvitesse=lootvitesse+2+paldemo//10
						elif int(lootchoice)==6:
							print ("|===================|")
							print ("|                   |")
							print ("|  ORBE DEMONIAQUE  |")
							print ("|     LEGENDAIRE    |")
							print ("|                   |")
							print ("|===================|")
							print (" ")
							print (" ")
							print ("Quelle caractéristique voulez-vous augmenter ?")
							print (" ")
							print ("[1] PV")
							print ("[2] force")
							print ("[3] defense")
							print ("[4] vitesse")
							print ("[5] les 4")
							leg=input()
							print (" ")
							print (" ")
							if int(leg)==1:
								print ("+"+str(80+paldemo)+" PV !")
								lootpv=lootpv+80+paldemo
							elif int(leg)==2:
								print ("+"+str(18+paldemo//4)+" force !")
								lootforce=lootforce+18+paldemo//4
							elif int(leg)==3:
								print ("+ "+str(8+paldemo//8)+" defense !")
								lootdefense=lootdefense+8+paldemo//8
							elif int(leg)==4:
								print ("+ "+str(8+paldemo//8)+" vitesse !")
								lootvitesse=lootvitesse+8+paldemo//8
							elif int(leg)==5:
								print ("+ "+str(20+paldemo//3)+" PV !")
								print ("+ "+str(6+paldemo//5)+" force !")
								print ("+ "+str(2+paldemo//10)+" defense !")
								print ("+ "+str(2+paldemo//10)+" vitesse !")
								lootpv=lootpv+20+paldemo//3
								lootforce=lootforce+6+paldemo//5
								lootdefense=lootdefense+2+paldemo//10
								lootvitesse=lootvitesse+2+paldemo//10
					if int(choix5)==2:
						if int(lootchoice)==1:
							print ("vous gagnez une goutte d'eau enchantée !")
							print (" ")
							print ("+ "+str(80+palimmo*3//2)+" PV !")
							lootpv=lootpv+80+palimmo*3//2
						elif int(lootchoice)==2:
							print ("vous gagnez une épée enchantée !")
							print (" ")
							print ("+"+str(20+palimmo//3)+" PV !")
							print ("+ "+str(6+palimmo//5)+" force !")
							lootpv=lootpv+20+palimmo//3
							lootforce=lootforce+6+palimmo//5
						elif int(lootchoice)==3:
							print ("vous gagnez un bouclier enchantée !")
							print (" ")
							print ("+"+str(20+palimmo//3)+" PV !")
							print ("+ "+str(2+palimmo//10)+" defense !")
							lootpv=lootpv+20+palimmo//3
							lootdefense=lootdefense+2+palimmo//10
						elif int(lootchoice)==4:
							print ("vous gagnez une plume enchantée !")
							print (" ")
							print ("+"+str(20+palimmo//3)+" PV !")
							print ("+ "+str(2+palimmo//10)+" vitesse !")
							lootpv=lootpv+20+palimmo//3
							lootvitesse=lootvitesse+2+palimmo//10
						elif int(lootchoice)==5:
							print ("vous gagnez une bague divine !")
							print (" ")
							print ("+ "+str(20+palimmo//2)+" PV !")
							print ("+ "+str(6+palimmo//6)+" force !")
							print ("+ "+str(2+palimmo//11)+" defense !")
							print ("+ "+str(2+palimmo//11)+" vitesse !")
							lootpv=lootpv+20+palimmo//2
							lootforce=lootforce+6+palimmo//6
							lootdefense=lootdefense+2+palimmo//11
							lootvitesse=lootvitesse+2+palimmo//11
						elif int(lootchoice)==6:
							print ("|====================|")
							print ("|                    |")
							print ("|  PHYLACTERE DIVIN  |")
							print ("|     LEGENDAIRE     |")
							print ("|                    |")
							print ("|====================|")
							print (" ")
							print (" ")
							print ("Quelle caractéristique voulez-vous augmenter ?")
							print (" ")
							print ("[1] PV")
							print ("[2] force")
							print ("[3] defense")
							print ("[4] vitesse")
							print ("[5] les 4")
							leg=input()
							print (" ")
							print (" ")
							if int(leg)==1:
								print ("+"+str(80+palimmo*3//2)+" PV !")
								lootpv=lootpv+80+palimmo*3//2
							elif int(leg)==2:
								print ("+"+str(18+palimmo//4)+" force !")
								lootforce=lootforce+18+pal//4
							elif int(leg)==3:
								print ("+ "+str(8+palimmo//8)+" defense !")
								lootdefense=lootdefense+8+pal//8
							elif int(leg)==4:
								print ("+ "+str(8+palimmo//8)+" vitesse !")
								lootvitesse=lootvitesse+8+pal//8
							elif int(leg)==5:
								print ("+ "+str(20+palimmo//2)+" PV !")
								print ("+ "+str(6+palimmo//6)+" force !")
								print ("+ "+str(2+palimmo//11)+" defense !")
								print ("+ "+str(2+palimmo//11)+" vitesse !")
								lootpv=lootpv+20+palimmo//2
								lootforce=lootforce+6+palimmo//6
								lootdefense=lootdefense+2+palimmo//11
								lootvitesse=lootvitesse+2+palimmo//11
					if int(choix5)==3:
						if int(lootchoice)==1:
							print ("vous gagnez une fiole de sang barbare !")
							print (" ")
							print ("+ "+str(80+palbarb//2)+" PV !")
							print ("+"+str(6+palbarb//5)+" force !")
							lootpv=lootpv+80+palbarb//2
							lootforce=lootforce+6+palbarb//5
						elif int(lootchoice)==2:
							print ("vous gagnez une hache barbare !")
							print (" ")
							print ("+ "+str(6+palbarb*2//5)+" force !")
							lootforce=lootforce+6+palbarb*2//5
						elif int(lootchoice)==3:
							print ("vous gagnez une peau de bête épaisse !")
							print (" ")
							print ("+ "+str(2+palbarb//10)+" defense !")
							print ("+"+str(6+palbarb//5)+" force !")
							lootdefense=lootdefense+2+palbarb//10
							lootforce=lootforce+6+palbarb//5
						elif int(lootchoice)==4:
							print ("vous gagnez des bottes légères en cuir !")
							print (" ")
							print ("+ "+str(2+palbarb//10)+" vitesse !")
							print ("+"+str(6+palbarb//5)+" force !")
							lootvitesse=lootvitesse+2+palbarb//10
							lootforce=lootforce+6+palbarb//5
						elif int(lootchoice)==5:
							print ("vous gagnez la tresse du seigneur barbare  !")
							print (" ")
							print ("+ "+str(20+palbarb//4)+" PV !")
							print ("+ "+str(6+palbarb//4)+" force !")
							print ("+ "+str(2+palbarb//11)+" defense !")
							print ("+ "+str(2+palbarb//11)+" vitesse !")
							lootpv=lootpv+20+palbarb//4
							lootforce=lootforce+6+palbarb//4
							lootdefense=lootdefense+2+palbarb//11
							lootvitesse=lootvitesse+2+palbarb//11
						elif int(lootchoice)==6:
							print ("|====================|")
							print ("|                    |")
							print ("|  COURONNE BARBARE  |")
							print ("|     LEGENDAIRE     |")
							print ("|                    |")
							print ("|====================|")
							print (" ")
							print (" ")
							print ("Quelle caractéristique voulez-vous augmenter ?")
							print (" ")
							print ("[1] PV")
							print ("[2] force")
							print ("[3] defense")
							print ("[4] vitesse")
							print ("[5] les 4")
							leg=input()
							print (" ")
							print (" ")
							if int(leg)==1:
								print ("+"+str(80+palbarb)+" PV !")
								lootpv=lootpv+80+palbarb
							elif int(leg)==2:
								print ("+"+str(6+palbarb*2//5)+" force !")
								lootforce=lootforce+6+palbarb*2//5
							elif int(leg)==3:
								print ("+ "+str(8+palbarb//8)+" defense !")
								lootdefense=lootdefense+8+palbarb//8
							elif int(leg)==4:
								print ("+ "+str(8+palbarb//8)+" vitesse !")
								lootvitesse=lootvitesse+8+palbarb//8
							elif int(leg)==5:
								print ("+ "+str(20+palbarb//4)+" PV !")
								print ("+ "+str(6+palbarb//4)+" force !")
								print ("+ "+str(2+palbarb//11)+" defense !")
								print ("+ "+str(2+palbarb//11)+" vitesse !")
								lootpv=lootpv+20+palbarb//4
								lootforce=lootforce+6+palbarb//4
								lootdefense=lootdefense+2+palbarb//11
								lootvitesse=lootvitesse+2+palbarb//11
					if int(choix5)==4:
						if int(lootchoice)==1:
							print ("vous gagnez fragment elementaire aquatique !")
							print (" ")
							print ("+ "+str(80+palelem//2)+" PV !")
							print ("+"+str(2+palelem//10)+" defense !")
							lootpv=lootpv+80+palelem//2
							lootdefense=lootdefense+2+palelem//10
						elif int(lootchoice)==2:
							print ("vous gagnez fragment elementaire flamboyant!")
							print (" ")
							print ("+ "+str(6+palelem//5)+" force !")
							print ("+"+str(2+palelem//10)+" defense !")
							lootforce=lootforce+6+palelem//5
							lootdefense=lootdefense+2+palelem//10
						elif int(lootchoice)==3:
							print ("vous gagnez fragment elementaire rocheux!")
							print (" ")
							print ("+ "+str(2+palelem*2//13)+" defense !")
							lootdefense=lootdefense+2+palelem*2//13
						elif int(lootchoice)==4:
							print ("vous gagnez fragment elementaire venteux!")
							print (" ")
							print ("+ "+str(2+palelem//10)+" vitesse !")
							print ("+"+str(2+palelem//10)+" defense !")
							lootvitesse=lootvitesse+2+palelem//10
							lootdefense=lootdefense+2+palelem//10
						elif int(lootchoice)==5:
							print ("vous gagnez fragment elementaire magique!")
							print (" ")
							print ("+ "+str(20+palelem//4)+" PV !")
							print ("+ "+str(6+palelem//6)+" force !")
							print ("+ "+str(2+palelem//9)+" defense !")
							print ("+ "+str(2+palelem//11)+" vitesse !")
							lootpv=lootpv+20+palelem//4
							lootforce=lootforce+6+palelem//5
							lootdefense=lootdefense+2+palelem//9
							lootvitesse=lootvitesse+2+palelem//11
						elif int(lootchoice)==6:
							print ("|====================|")
							print ("|                    |")
							print ("|  CRISTAL INSTABLE  |")
							print ("|     LEGENDAIRE     |")
							print ("|                    |")
							print ("|====================|")
							print (" ")
							print (" ")
							print ("Quelle caractéristique voulez-vous augmenter ?")
							print (" ")
							print ("[1] PV")
							print ("[2] force")
							print ("[3] defense")
							print ("[4] vitesse")
							print ("[5] les 4")
							leg=input()
							print (" ")
							print (" ")
							if int(leg)==1:
								print ("+"+str(80+palelem)+" PV !")
								lootpv=lootpv+80+palelem
							elif int(leg)==2:
								print ("+"+str(18+palelem//4)+" force !")
								lootforce=lootforce+18+palelem//4
							elif int(leg)==3:
								print ("+ "+str(2+palelem*2//13)+" defense !")
								lootdefense=lootdefense+2+palelem*2//13
							elif int(leg)==4:
								print ("+ "+str(8+palelem//8)+" vitesse !")
								lootvitesse=lootvitesse+8+palelem//8
							elif int(leg)==5:
								print ("+ "+str(20+palelem//4)+" PV !")
								print ("+ "+str(6+palelem//6)+" force !")
								print ("+ "+str(2+palelem//9)+" defense !")
								print ("+ "+str(2+palelem//11)+" vitesse !")
								lootpv=lootpv+20+palelem//4
								lootforce=lootforce+6+palelem//6
								lootdefense=lootdefense+2+palelem//9
								lootvitesse=lootvitesse+2+palelem//11
					if int(choix5)==5:
						if int(lootchoice)==1:
							print ("vous gagnez une emmeraude !")
							print (" ")
							print ("+ "+str(80+palfufu//2)+" PV !")
							print ("+"+str(2+palfufu//10)+" vitesse !")
							lootpv=lootpv+80+palfufu//2
							lootvitesse=lootvitesse+2+palfufu
						elif int(lootchoice)==2:
							print ("vous gagnez un rubis !")
							print (" ")
							print ("+ "+str(6+palfufu//5)+" force !")
							print ("+"+str(2+palfufu//10)+" vitesse !")
							lootforce=lootforce+6+palfufu//5
							lootvitesse=lootvitesse+2+palfufu
						elif int(lootchoice)==3:
							print ("vous gagnez un saphir !")
							print (" ")
							print ("+ "+str(2+palfufu//10)+" defense !")
							print ("+"+str(2+palfufu//10)+" vitesse !")
							lootdefense=lootdefense+2+palfufu//10
							lootvitesse=lootvitesse+2+palfufu
						elif int(lootchoice)==4:
							print ("vous gagnez une topaze !")
							print (" ")
							print ("+ "+str(2+palfufu*2//13)+" vitesse !")
							lootvitesse=lootvitesse+2+palfufu*2//13
						elif int(lootchoice)==5:
							print ("vous gagnez une obsidienne !")
							print (" ")
							print ("+ "+str(20+palfufu//4)+" PV !")
							print ("+ "+str(6+palfufu//6)+" force !")
							print ("+ "+str(2+palfufu//11)+" defense !")
							print ("+ "+str(2+palfufu//9)+" vitesse !")
							lootpv=lootpv+20+palfufu//4
							lootforce=lootforce+6+palfufu//6
							lootdefense=lootdefense+2+palfufu//11
							lootvitesse=lootvitesse+2+palfufu//9
						elif int(lootchoice)==6:
							print ("|===================|")
							print ("|                   |")
							print ("|  DIAMANT PARFAIT  |")
							print ("|     LEGENDAIRE    |")
							print ("|                   |")
							print ("|===================|")
							print (" ")
							print (" ")
							print ("Quelle caractéristique voulez-vous augmenter ?")
							print (" ")
							print ("[1] PV")
							print ("[2] force")
							print ("[3] defense")
							print ("[4] vitesse")
							print ("[5] les 4")
							leg=input()
							print (" ")
							print (" ")
							if int(leg)==1:
								print ("+"+str(80+palfufu)+" PV !")
								lootpv=lootpv+80+palfufu
							elif int(leg)==2:
								print ("+"+str(18+palfufu//4)+" force !")
								lootforce=lootforce+18+palfufu//4
							elif int(leg)==3:
								print ("+ "+str(8+palfufu//8)+" defense !")
								lootdefense=lootdefense+8+palfufu//8
							elif int(leg)==4:
								print ("+ "+str(2+palfufu*2//13)+" vitesse !")
								lootvitesse=lootvitesse+2+palfufu*2//13
							elif int(leg)==5:
								print ("+ "+str(20+palfufu//4)+" PV !")
								print ("+ "+str(6+palfufu//6)+" force !")
								print ("+ "+str(2+palfufu//11)+" defense !")
								print ("+ "+str(2+palfufu//9)+" vitesse !")
								lootpv=lootpv+20+palfufu//4
								lootforce=lootforce+6+palfufu//6
								lootdefense=lootdefense+2+palfufu//11
								lootvitesse=lootvitesse+2+palfufu//9
					print (" ")
					print (" ")
					continuer=input("[enter]")
					if int(choix5)==1:
						paldemo=paldemo+10
					elif int(choix5)==2:
						palimmo=palimmo+10
					elif int(choix5)==3:
						palbarb=palbarb+10
					elif int(choix5)==4:
						palelem=palelem+10
					elif int(choix5)==5:
						palfufu=palfufu+10
					exp=exp+lvlm
					expmax=5*lvl+lvl*lvl
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=0
						print ("[1] +32 PV")
						print ("[2] +8 force")
						print ("[3] +4 defense")
						print ("[4] +4 vitesse")
						carac=input()
						print (" ")
						print (" ")
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
					print (" ")
					print (" ")
					print ("  _________________")
					print (" ()________________)")
					print ("  |               |")
					print ("  |     PALIER    |")
					print ("  |     SUIVANT   |")
					print ("  |_______________|")
					print (" ()________________)")
					print (" ")
					print (" ")
					continuer=input("[enter]")
			elif int(a)==2:
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				boss = [1,1,1,2]
				capa=random.choice(boss)
				if int(choix5)==1:
					if int(capa)==1:
						degatm=frappe_ombre(forcem,defense)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise frappe de l'ombre...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
					elif int(capa)==2:
						degatm=destru_primo(forcem,defense)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise destruction primordiale !")
						print (str(nomm)+" concentre toute sa puissance dans une orbe démoniaque et vous la lance...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
				elif int(choix5)==2:
					if int(capa)==1:
						degatm=attaque_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise transfusion magique...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
						print (str(nomm)+" gagne "+str(degatm//2)+" PV !")
						viem=viem+degatm//2
						print (" ")
						print (" ")
					elif int(capa)==2:
						degatm=ulti_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise pêché immortel !")
						print (str(nomm)+" concentre son sang magique au creux de sa main...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degatm//2)+" PV !")
						viem=viem-degatm//2
						print (" ")
						print (" ")
				elif int(choix5)==3:
					if int(capa)==1:
						degatm=attaque_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" vous met un coup brutal...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
					elif int(capa)==1:
						print (" ")
						print (" ")
						print (str(nomm)+" utilise rage berserker !")
						print ("Un afflux sanguin important renforce ses muscles...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nomm)+" gagne "+str(forcem//5))
						forcem=forcem+forcem//5
						print (" ")
						print (" ")
				elif int(choix5)==4:
					if int(capa)==1:
						buff=instabilite_elem(forcem,defensem,vitessem)
						print (" ")
						print (" ")
						print (str(nomm)+" utilise instabilité elementaire...")
						print (" ")
						print (" ")
						print (str(nomm)+" gagne "+str(buff)+" de force !")
						print (str(nomm)+" gagne "+str(buff)+" de defense !")
						print (str(nomm)+" gagne "+str(buff)+" de vitesse !")
						forcem=forcem+buff
						defensem=defensem+buff
						vitessem=vitessem+buff
						print (" ")
						print (" ")
					elif int(capa)==2:
						degatm=ulti_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" explosion elementaire !")
						print (str(nomm)+" absorbe les elements aux alentours et se decharge sur vous...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
				elif int(choix5)==5:
					if int(capa)==1:
						degatm=attaque_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise attaque pernicieuse...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
					elif int(capa)==2:
						degatm=ulti_boss(viem,forcem,defense,choix5)
						vie=vie-degatm
						print (" ")
						print (" ")
						print (str(nomm)+" utilise eventration !")
						print (str(nomm)+" vous plaque au sol et vous ouvre le ventre avec sa dague...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					print (" ")
					mort=input("[enter]")
					print (" ")
					print (" ")
					pass

	if os.path.isfile("sauv.txt")=="true":
		os.remove("sauv.txt")
	fw = open("sauv.txt","w")
	fw.write(str(nom))
	fw.write("\n")
	fw.write(str(lvl))
	fw.write("\n")
	fw.write(str(exp))
	fw.write("\n")
	fw.write(str(vieup))
	fw.write("\n")
	fw.write(str(forceup))
	fw.write("\n")
	fw.write(str(defenseup))
	fw.write("\n")
	fw.write(str(vitesseup))
	fw.write("\n")
	fw.write(str(pal))
	fw.write("\n")
	fw.write(str(lootpv))
	fw.write("\n")
	fw.write(str(lootforce))
	fw.write("\n")
	fw.write(str(lootdefense))
	fw.write("\n")
	fw.write(str(lootvitesse))
	fw.write("\n")
	fw.write(str(degpv))
	fw.write("\n")
	fw.write(str(degfor))
	fw.write("\n")
	fw.write(str(degdef))
	fw.write("\n")
	fw.write(str(degvit))
	fw.write("\n")
	fw.write(str(keltu))
	fw.write("\n")
	fw.write(str(immortal))
	fw.write("\n")
	fw.write(str(norfend))
	fw.write("\n")
	fw.write(str(amedemo))
	fw.write("\n")
	fw.write(str(exode))
	fw.write("\n")
	fw.write(str(armudemo))
	fw.write("\n")
	fw.write(str(azzin))
	fw.write("\n")
	fw.write(str(agilistack))
	fw.write("\n")
	fw.write(str(corrup))
	fw.write("\n")
	fw.write(str(chassedemo))
	fw.write("\n")
	fw.write(str(ritsang))
	fw.write("\n")
	fw.write(str(mourne))
	fw.write("\n")
	fw.write(str(war))
	fw.write("\n")
	fw.write(str(oth))
	fw.write("\n")
	fw.write(str(ombre))
	fw.write("\n")
	fw.write(str(pacte))
	fw.write("\n")
	fw.write(str(trans))
	fw.write("\n")
	fw.write(str(abso))
	fw.write("\n")
	fw.write(str(poigne))
	fw.write("\n")
	fw.write(str(renfo))
	fw.write("\n")
	fw.write(str(anean))
	fw.write("\n")
	fw.write(str(onde))
	fw.write("\n")
	fw.write(str(veng))
	fw.write("\n")
	fw.write(str(souffle))
	fw.write("\n")
	fw.write(str(serie))
	fw.write("\n")
	fw.write(str(drain))
	fw.write("\n")
	fw.write(str(feu))
	fw.write("\n")
	fw.write(str(ame))
	fw.write("\n")
	fw.write(str(tuto))
	fw.write("\n")
	fw.write(str(quete2))
	fw.write("\n")
	fw.write(str(expmax))
	fw.write("\n")
	fw.write(str(paldemo))
	fw.write("\n")
	fw.write(str(palimmo))
	fw.write("\n")
	fw.write(str(palbarb))
	fw.write("\n")
	fw.write(str(palelem))
	fw.write("\n")
	fw.write(str(palfufu))
	fw.close()