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
	if int(tuto)==0:
		print ("Vous voici dans le tutoriel, vous allez apprendre les bases du jeu...")
		print ("Afin d'intéragir dans le jeu merci de remplir uniquement les renseignements demandés entre crochets")
		print ("Par exemple : [enter] à la vue de ceci, pour continuer vous n'avez qu'à appuyer sur 'Entrée'")
		print ("Ou encore : [1] frappe pour effectuer une frappe il vous suffit de renseigner '1' et d'appuyer sur 'Entrée'")
		print ("votre personnage dispose de 4 caractéristiques différentes :")
		print ("- la vie : si elle tombe à 0 vous êtes mort")
		print ("- la force : permet d'augmenter vos dégats")
		print ("- permet de réduire les dégats subis")
		print ("- la vitesse : augmente vos chances de jouer")
		print ("A chaque nouveau tour, vos vitesses (celle du monstre et la votre) determine vos chances de jouer")
		print ("Cela reste statistique, il est tout à fait possible donc de jouer 3 fois de suite avec une vitesse égale à celle du monstre et inversement")
		print ("Quand vous réussissez un combat, vous récupérez tous vos PV (points de vie) ainsi que de l'expérience qui dépend du niveau du monstre")
		print ("Une fois que vous avez récolté suffisamment d'expérience, vous montez d'un niveau")
		print ("vous avez alors le choix d'augmenter une de vos 4 caractéristiques")
		print ("une sauvegarde automatique enregistre votre progression à chaque fin de combat")
		print ("9 monstres de niveaux progressifs vous sont proposés ainsi qu'un boss de palier")
		print ("progressez en battant les monstres de plus en plus fort pour essayer de vaincre le boss et ainsi passer au palier supérieur")
		print ("Si vous tuez le boss, vous aurez le droit d'ouvrir son coffre qui renferme de puissants objets")
		print ("Bon voyons un peu comment vous vous débrouillez en combat !")
		continuer=input("[enter]")
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
		print ("[1] sanguinaire")
		tutoriel=input()
		if int(tutoriel)==1:
			print ("- 20 PV !")
			viem=viem-20
			print ("PV ("+str(nomm)+") = "+str(viem))
			print (" ")
			print ("vous récupérez 5 PV !")
			print ("PV ("+str(nom)+") = 505")
			continuer=input("[enter]")
			print (" ")
			print ("Bien joué ! Vous venez d'utiliser votre premier sort !")
			print ("sanguinaire est un sort très fort, il cause des dégats selon vos points de vie max")
			print ("Et vous fait regagner une partie des dégats infligés sous forme de PV !")
			print ("Essayons le prochain sort !")
			continuer=input("[enter]")
			print ("[2] devaster")
			tutoriel=input()
			if int(tutoriel)==2:
				print ("- 25 PV !")
				viem=viem-25
				print ("PV ("+str(nomm)+") = "+str(viem))
				continuer=input("[enter]")
				print (" ")
				print ("Bravo ! vous avez utiliser votre deuxième compétence !")
				print ("devaster est un sort qui inflige beaucoup de dégats en fonction de votre force")
				print ("Suivant !")
				continuer=input("[enter]")
				print ("[3] coup de bouclier")
				tutoriel=input()
				if int(tutoriel)==3:
					print ("- 17 PV !")
					viem=viem-17
					print ("PV ("+str(nomm)+") = "+str(viem))
					print (" ")
					print ("l'armure de l'ennemi diminue de 2 !")
					defensem=defensem-2
					print ("defense ("+str(nomm)+") = "+str(defensem))
					continuer=input("[enter]")
					print (" ")
					print ("coup de bouclier permet d'effectuer des dégats en fonction de votre force et de votre defense")
					print ("tout en diminuant la defense de votre adversaire !")
					print ("comme votre defense réduit les dégats ennemis, vos dégats sont réduits par la defense des monstres")
					print ("Le dernier sort !")
					continuer=input("[enter]")
					print ("[4] enchainement")
					tutoriel=input()
					if int(tutoriel)==4:
						print ("- 13 PV !")
						viem=viem-13
						print ("PV ("+str(nomm)+") = "+str(viem))
						print (" ")
						print ("combo = 2")
						continuer=input("[enter]")
						print (" ")
						print ("Euh... C'est quoi ce sort nul ?")
						print ("Relances le !")
						print ("[4] enchainement")
						tutoriel=input()
						if int(tutoriel)==4:
							print ("-21 PV !")
							viem=viem-21
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("combo = 3")
							continuer=input("[enter]")
							print (" ")
							print ("C'est bien mieux !")
							print ("Et ca sera de plus en plus fort... Au plus ton combo monte au plus enchainement fait de dégats !")
							print ("Un sort puissant si tu as beaucoup de vitesse, en plus ses dégats augmentent en fonction de ta vitesse et de ta force!")
							print ("Le tutoriel s'achève ici, tu es prêt à commencer ton ascension dans les paliers !")
							print ("Ah oui une derniere chose ! Quand tu fais un sort, celui-ci monte d'un niveau...")
							print ("Et arrivé à un certain niveau, ton sort devient plus fort !")
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
	print ("Courage héro, la récompense sera à la hauteur du défi...")
	continuer=input("[enter]")
	print (" ")
	print (nom)
	print (lvl)
	print ("PV = "+str(96+32*vieup+lootpv))
	print ("force = "+str(32+8*forceup+lootforce))
	print ("defense = "+str(16+4*defenseup+lootdefense))
	print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
	print (" ")
	continuer=input("[enter]")
	print ("vous ne pouvez choisir qu'une quête, alors choisissez bien...")
	print (" ")
	print ("[1] quête : Le sort d'immortalité de Kel'Thuzad (pour ceux qui aiment les PV)")
	print ("[2] quête : Libérer Frostmourne en Norfendre (pour ceux qui aiment la force)")
	print ("[3] quête : L'exode de Thrall des terres arides (pour ceux qui aiment la defense)")
	print ("[4] quête : Maîtriser les Lames d'Azzinoth (pour ceux qui aiment la vitesse)")
	print ("[5] quête : Eradiquer la corruption de Gul'Dan (pour ceux qui ne savent pas se décider...)")
	quete=input()
	print (" ")
	if int(quete)==1:
		keltu=1
		print ("Montrez la preuve de votre immortalité... (gagner 400 000 PV)")
		immortal=0
		print ("Egaler la vie de Kel'Thuzad... (atteindre 2750 PV)")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
	elif int(quete)==2:
		norfend=1
		print ("Augmenter votre force pour manier Frostmourne... (atteindre 730 force)")
		print ("Arracher l'âme d'un puissant demon pour nourrir Frostmourne... (tuer le demon primordial lvl70)")
		amedemo=0
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
	elif int(quete)==3:
		exode=1
		print ("Detruire les armures démoniaques... (enlever 100 000 defense)")
		armudemo=0
		print ("Forger une armure légendaire pour Thrall... (atteindre 350 defense)")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
	elif int(quete)==4:
		azzin=1
		print ("Deplacer vous plus vite qu'Illidan... (atteindre 350 vitesse)")
		print ("Prouver votre agilité au combat... (effectuer 10 000 combos)")
		agilistack=0
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
	elif int(quete)==5:
		corrup=1
		print ("Eliminer des demons pour chasser la corruption... (tuer 15 000 demons)")
		chassedemo=0
		print ("Terroriser Gul'Dan par votre puissance... (atteindre 800 PV, 210 force, 100 defense et 100 vitesse")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
else:
	exit()

while int(pal)!=210000:
	totalpv=96+32*vieup+lootpv
	frost=32+8*forceup+lootforce
	armuleg=16+4*defenseup+lootdefense
	vitilli=16+4*vitesseup+lootvitesse
	gulpv=96+32*vieup+lootpv
	gulfor=32+8*forceup+lootforce
	guldef=16+4*defenseup+lootdefense
	gulvit=16+4*vitesseup+lootvitesse
	if int(keltu)==1:
		print ("quête : "+str(immortal)+"/400 000 PV gagnés")
		print ("quête : "+str(totalpv)+"/2750 PV atteint")
	elif int(norfend)==1:
		print ("quête : "+str(amedemo)+"/1 demon primordial lvl60 tué")
		print ("quête : "+str(frost)+"/730 force atteinte")
	elif int(exode)==1:
		print ("quête : "+str(armudemo)+"/100 000 defense enlevée")
		print ("quête : "+str(armuleg)+"/350 defense atteinte")
	elif int(azzin)==1:
		print ("quête : "+str(vitilli)+"/350 vitesse atteinte")
		print ("quête : "+str(agilistack)+"/10 000 stack")
	elif int(corrup)==1:
		print ("quête : "+str(chassedemo)+"/15 000 démons tués")
		print ("quête : "+str(gulpv)+"/800 PV atteint")
		print ("quête : "+str(gulfor)+"/210 force atteinte")
		print ("quête : "+str(guldef)+"/100 defense atteinte")
		print ("quête : "+str(gulvit)+"/100 vitesse atteinte")
	print (" ")
#	if int(pal)>=210:
#		if int(keltu)==2:
#			print ("[11] garde de Kel'Thuzad")
#		elif int(norfend)==2:
#			print ("[11] garde d'Arthas")
#		elif int(exode)==2:
#			print ("[11] garde de Thrall")
#		elif int(azzin)==2:
#			print ("[11] garde d'Illidan")
#		print ("[0] quitter")
#	else:
	print ("[1] demon lvl "+str(1+pal)+"                            PV ("+str(nom)+") = "+str(96+32*vieup+lootpv))
	print ("[2] demon lvl "+str(2+pal)+"                            force ("+str(nom)+") = "+str(32+8*forceup+lootforce))
	print ("[3] demon lvl "+str(3+pal)+"                            defense ("+str(nom)+") = "+str(16+4*defenseup+lootdefense))
	print ("[4] demon lvl "+str(4+pal)+"                            vitesse ("+str(nom)+") = "+str(16+4*vitesseup+lootvitesse))
	print ("[5] demon lvl "+str(5+pal))
	print ("[6] demon lvl "+str(6+pal))
	print ("[7] demon lvl "+str(7+pal))
	print ("[8] demon lvl "+str(8+pal))
	print ("[9] demon lvl "+str(9+pal))
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
		forcem=33+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous canalisez une puissance démoniaque...")
							print ("elle vous enveloppe et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")			
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
						else:
							pass
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==2:
		lvlm=2+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==3:
		lvlm=3+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==4:
		lvlm=4+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==5:
		lvlm=5+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==6:
		lvlm=6+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==7:
		lvlm=7+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==8:
		lvlm=8+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==9:
		lvlm=9+pal
		tour=0
		stackvit=1
		nomm="demon lvl "+str(lvlm)
		viem=105+24*lvlm
		forcem=32+6*lvlm
		defensem=16+3*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
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
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (" ")
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print ("-"+str(degatm)+" PV !")
				print ("PV ("+str(nom)+") = "+str(vie))
				print (" ")
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
					pass

	elif int(choix1)==10:
		lvlm=10+pal
		tour=0
		stackvit=1
		nomm="demon primordial" 
		viem=105+30*lvlm
		forcem=32+8*lvlm
		defensem=16+5*lvlm
		vitessem=20+1*lvlm
		vie=96+32*vieup+lootpv
		force=32+8*forceup+lootforce
		defense=16+4*defenseup+lootdefense
		vitesse=16+4*vitesseup+lootvitesse
		print (" ")
		print (nomm)
		print ("PV = "+str(viem))
		print ("force = "+str(forcem))
		print ("defense = "+str(defensem))
		print ("vitesse = "+str(vitessem))
		print (" ")
		while int(vie)>0 and int(viem)>0:
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//3)+" PV !")
				
							vie=vie+degat//3
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							ritsang=ritsang+1
							if int(ritsang)==500 or int(ritsang)==2000 or int(ritsang)==5000:
								print ("-------------------------------------")
								print ("|==> TOUCHER SANGLANT LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ toucher sanglant passe au niveau "+str(ritsang)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print ("vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
							vie=vie-degat
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							pacte=pacte+1
							if int(pacte)==500 or int(pacte)==2000 or int(pacte)==5000:
								print ("----------------------------------")
								print ("|==> PACTE DE SANG LVL UP !!! <==|")
								print ("----------------------------------")
								print (" ")
							else:
								print ("[ pacte de sang passe au niveau "+str(pacte)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=transfert(defense,trans)
							print (" ")
							print ("vous sacrifiez votre armure pour augmenter votre vie !")
							vie=vie+buff
							print ("+"+str(buff)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							defense=0
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							bloodstack=bloodstack+1
							print ("stack de sang = "+str(bloodstack))	
							print (" ")
							trans=trans+1
							if int(trans)==500 or int(trans)==2000 or int(trans)==5000:
								print ("------------------------------")
								print ("|==> TRANSFERT LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ transfert passe au niveau "+str(trans)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=absorption(vie,defensem,bloodstack,abso)
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("et infligez un coup dévastateur à votre adversaire !!!")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							bloodstack=0
							print (" ")
							print ("stack de sang = "+str(bloodstack))
							print (" ")
							abso=abso+1
							if int(abso)==500 or int(abso)==2000 or int(abso)==5000:
								print ("-------------------------------")
								print ("|==> ABSORPTION LVL UP !!! <==|")
								print ("-------------------------------")
								print (" ")
							else:
								print ("[ absorption passe au niveau "+str(abso)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre force augmente de "+str(degat//10))
							force=force+degat//10
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							mourne=mourne+1
							if int(mourne)==500 or int(mourne)==2000 or int(mourne)==5000:
								print ("------------------------------------")
								print ("|==> FRAPPE DU FLEAU LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ frappe du fléau passe au niveau "+str(mourne)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print ("-"+str(debuff)+" de force !")
							print ("force ("+str(nomm)+") = "+str(forcem))
							print (" ")
							force=force+debuff//2
							print ("+"+str(debuff//2)+" de force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==500 or int(poigne)==2000 or int(poigne)==5000:
								print ("--------------------------------------")
								print ("|==> POIGNE DE LA MORT LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ poigne de la mort passe au niveau "+str(poigne)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							buff=renforcement(force,renfo)
							vie=vie+buff*3
							defense=defense+buff*3//2
							print (" ")
							print ("+"+str(buff*3)+" PV !")
							print ("+"+str(buff*3//2)+" de defense !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							print (" ")
							force=force-buff*2
							if int(force)<0:
								force=0
							print ("-"+str(buff*2)+" force !")
							print ("force ("+str(nom)+") = "+str(force))
							jeu=1
							print (" ")
							renfo=renfo+1
							if int(renfo)==500 or int(renfo)==2000 or int(renfo)==5000:
								print ("---------------------------------")
								print ("|==> RENFORCEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ renforcement passe au niveau "+str(renfo)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							degat=renforcement(force,forcem,defensem,anean)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							anean=anean+1
							if int(anean)==500 or int(anean)==2000 or int(anean)==5000:
								print ("-----------------------------------")
								print ("|==> ANEANTISSEMENT LVL UP !!! <==|")
								print ("-----------------------------------")
								print (" ")
							else:
								print ("[ aneantissement passe au niveau "+str(anean)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//8))
							defensem=defensem-degat//8
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							war=war+1
							if int(war)==500 or int(war)==2000 or int(war)==5000:
								print ("--------------------------------------")
								print ("|==> HEURT DE BOUCLIER LVL UP !!! <==|")
								print ("--------------------------------------")
								print (" ")
							else:
								print ("[ heurt de bouclier passe au niveau "+str(war)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=onde_choc(defense,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("-"+str(vitessem//10)+" de vitesse !")
							vitessem=vitessem-vitessem//10
							print ("vitesse ("+str(nomm)+") = "+str(vitessem))
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==500 or int(onde)==2000 or int(onde)==5000:
								print ("---------------------------------")
								print ("|==> ONDE DE CHOC LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ onde de choc passe au niveau "+str(onde)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print ("vos blessures infligées à l'adversaire vous font enrager !")
							print ("vous deversez toute cette puissance dans un coup destructeur...")
							coup=input("[enter]")
							print ("-"+str(degat)+" PV !!")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous subissez le contrecoup...")
							print ("-"+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print ("PV ("+str(nom)+") = "+str(vie))
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==500 or int(veng)==2000 or int(veng)==5000:
								print ("------------------------------")
								print ("|==> BERSERKER LVL UP !!! <==|")
								print ("------------------------------")
								print (" ")
							else:
								print ("[ berserker passe au niveau "+str(veng)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							buff=dernier_souffle(defense,souffle)
							print ("vous sacrifiez votre defense pour gagner de la vie !")
							print ("+"+str(buff)+" PV !")
							print ("-"+str(defense//10)+" de defense !")
							vie=vie+buff
							defense=defense-defense//10
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("defense ("+str(nom)+") = "+str(defense))
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==500 or int(souffle)==2000 or int(souffle)==5000:
								print ("------------------------------------")
								print ("|==> DERNIER SOUFFLE LVL UP !!! <==|")
								print ("------------------------------------")
								print (" ")
							else:
								print ("[ dernier souffle passe au niveau "+str(souffle)+" ]")
								print (" ")
					elif int(azzin)==2:
						print ("[1] danse de l'ombre")
						if int(lvl)>=120:
							print ("[2] pas de l'ombre")
						if int(lvl)>=140:
							print ("[3] serie meutriere")
						if int(lvl)>=160:
							print ("[4] transformation")
						choix3=input()
						if int(choix3)==1:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							oth=oth+1
							if int(oth)==500 or int(oth)==2000 or int(oth)==5000:
								print ("-------------------------------------")
								print ("|==> DANSE DE L'OMBRE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ danse de l'ombre passe au niveau "+str(oth)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							print (" ")
							print ("vous sacrifiez un peu de votre vitesse pour surprendre votre adversaire !")
							print ("votre combo augmente grandement...")
							print (" ")
							print ("-"+str(stackvit*stackvit)+" de vitesse !")
							vitesse=vitesse-stackvit*stackvit
							stackvit=stackvit+3
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							degat=serie_meurtriere(stackvit,defensem,serie)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							stackvit=0
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							serie=serie+1
							if int(serie)==500 or int(serie)==2000 or int(serie)==5000:
								print ("-------------------------------------")
								print ("|==> SERIE MEURTRIERE LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ serie meurtriere passe au niveau "+str(serie)+" ]")
								print (" ")
						elif int(choix3)==4 and int(lvl)>=160:
							print (" ")
							print ("vous rassemblez toute la puissance des demons vaincus...")
							print ("elle vous ecrase et vous transforme en chasseur demoniaque !!!")
							print ("une aura maléfique émane de votre corps...")
							continuer=input("[enter]")
							print (" ")
							vie=vie+vitesse*5
							force=force+vitesse*3
							defense=defense+vitesse*2
							print ("+"+str(vitesse*5)+" PV !")
							print ("+"+str(vitesse*3)+" force !")
							print ("+"+str(vitesse*2)+" defense !")
							print ("-"+str(vitesse*3//4)+" vitesse !!")
							print (" ")
							vitesse=vitesse-vitesse*3//4
							print ("PV ("+str(nom)+") = "+str(vie))
							print ("force ("+str(nom)+") = "+str(force))
							print ("defense ("+str(nom)+") = "+str(defense))
							print ("vitesse ("+str(nom)+") = "+str(vitesse))
							jeu=1
							print (" ")
					elif int(corrup)==2:
						print ("[1] ombreflamme")
						if int(lvl)>=120:
							print ("[2] drainage")
						if int(lvl)>=140:
							print ("[3] connexion")
						if int(lvl)>=160:
							print ("[4] feu de l'âme")
						choix3=input()
						if int(choix3)==1:
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==500 or int(ombre)==2000 or int(ombre)==5000:
								print ("--------------------------------")
								print ("|==> OMBREFLAMME LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ ombreflamme passe au niveau "+str(ombre)+" ]")
								print (" ")
						elif int(choix3)==2 and int(lvl)>=120:
							degat=drainage(force,drain)
							viem=viem-degat
							vie=vie+degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("+"+str(degat)+" PV !")
							print ("PV ("+str(nom)+") = "+str(vie))
							print (" ")
							jeu=1
							drain=drain+1
							if int(drain)==500 or int(drain)==2000 or int(drain)==5000:
								print ("-----------------------------")
								print ("|==> DRAINAGE LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ drainage passe au niveau "+str(drain)+" ]")
								print (" ")
						elif int(choix3)==3 and int(lvl)>=140:
							vie=vie-(96+34*vieup+lootpv)//5
							print (" ")
							print ("-"+str((96+34*vieup+lootpv)//5)+" PV !")
							print ("+"+str(force*3//2)+" de force !")
							print ("PV ("+str(nom)+") = "+str(vie))
							force=force*3//2
							print ("force ("+str(nom)+") = "+str(force))
							print (" ")
							jeu=1
						elif int(choix3)==4 and int(lvl)>=160:
							degat=feu_ame(force,ame,lvlm,feu)
							viem=viem-degat
							print (" ")
							print ("vous rassemblez la puissance de toutes les âmes démoniaques au creux de votre main...")
							print ("vous la transformez en une flamme noire démoniaque avant de la lancer sur votre adversaire !!")
							continuer=input("[enter]")
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							ame=0
							print("ame démoniaque = "+str(ame))
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==500 or int(feu)==2000 or int(feu)==5000:
								print ("---------------------------------")
								print ("|==> FEU DE L'AME LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ feu de l'âme passe au niveau "+str(feu)+" ]")
								print (" ")
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
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("vous récupérez "+str(degat//4)+" PV !")
							vie=vie+degat//4
							print ("PV ("+str(nom)+") = "+str(vie))
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+degat//4
							degpv=degpv+1
							if int(degpv)==500 or int(degpv)==2000 or int(degpv)==5000:
								print ("--------------------------------")
								print ("|==> SANGUINAIRE LVL UP !!! <==|")
								print ("--------------------------------")
								print (" ")
							else:
								print ("[ sanguinaire passe au niveau "+str(degpv)+" ]")
								print (" ")
						elif int(choix2)==2:
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==500 or int(degfor)==2000 or int(degfor)==5000:
								print ("-----------------------------")
								print ("|==> DEVASTER LVL UP !!! <==|")
								print ("-----------------------------")
								print (" ")
							else:
								print ("[ devaster passe au niveau "+str(degfor)+" ]")
								print (" ")
						elif int(choix2)==3:
							degat=degat_defense(force,defense,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("l'armure ennemi diminue de "+str(degat//10))
							defensem=defensem-degat//10
							if int(defensem)<0:
								defensem=0
							print ("defense ("+str(nomm)+") = "+str(defensem))
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+degat//10
							degdef=degdef+1
							if int(degdef)==500 or int(degdef)==2000 or int(degdef)==5000:
								print ("-------------------------------------")
								print ("|==> COUP DE BOUCLIER LVL UP !!! <==|")
								print ("-------------------------------------")
								print (" ")
							else:
								print ("[ coup de bouclier passe au niveau "+str(degdef)+" ]")
								print (" ")
						elif int(choix2)==4:
							degat=degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth)
							viem=viem-degat
							print (" ")
							print ("-"+str(degat)+" PV !")
							print ("PV ("+str(nomm)+") = "+str(viem))
							print (" ")
							print ("votre combo augmente...")
							stackvit=stackvit+1
							print ("combo = "+str(stackvit))
							jeu=1
							print (" ")
							if int(azzin)==1:
								agilistack=agilistack+stackvit
							degvit=degvit+1
							if int(degvit)==500 or int(degvit)==2000 or int(degvit)==5000:
								print ("---------------------------------")
								print ("|==> ENCHAINEMENT LVL UP !!! <==|")
								print ("---------------------------------")
								print (" ")
							else:
								print ("[ enchainement passe au niveau "+str(degvit)+" ]")
								print (" ")
				if int(viem)<=0:
					if int(corrup)==1:
						chassedemo=chassedemo+1
					print ("vous avez vaincu "+str(nomm)+" !!!")
					print ("vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					if int(lvl)>=160:
						ame=ame+1
						print ("vous récupérez l'âme du démon vaincu !")
						print ("ame démoniaque = "+str(ame))
						print (" ")
					lot=input("vous ouvrez le coffre de loot...")
					loot = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
					lootchoice=random.choice(loot)
					if int(lootchoice)==1:
						print ("vous gagnez le coeur de Kel'Thuzad !")
						print ("+ "+str(40+pal)+" PV !")
						lootpv=lootpv+40+pal
					elif int(lootchoice)==2:
						print ("vous gagnez la lame d'Arthas !")
						print ("+ "+str(9+pal//4)+" force !")
						lootforce=lootforce+9+pal//4
					elif int(lootchoice)==3:
						print ("vous gagnez l'armure de Thrall !")
						print ("+ "+str(4+pal//8)+" defense !")
						lootdefense=lootdefense+4+pal//8
					elif int(lootchoice)==4:
						print ("vous gagnez les ailes d'Illidan !")
						print ("+ "+str(4+pal//8)+" vitesse !")
						lootvitesse=lootvitesse+4+pal//8
					elif int(lootchoice)==5:
						print ("vous gagnez le crâne de Gul'dan !")
						print ("+ "+str(10+pal//3)+" PV !")
						print ("+ "+str(3+pal//5)+" force !")
						print ("+ "+str(1+pal//10)+" defense !")
						print ("+ "+str(1+pal//10)+" vitesse !")
						lootpv=lootpv+10+pal//3
						lootforce=lootforce+3+pal//5
						lootdefense=lootdefense+1+pal//10
						lootvitesse=lootvitesse+1+pal//10
					elif int(lootchoice)==6:
						print ("|~~~~~~~~~~~~~~~~~~|")
						print ("| ORBE PRIMORDIALE |")
						print ("|    LEGENDAIRE    |")
						print ("|~~~~~~~~~~~~~~~~~~|")
						print ("Quelle caractéristique voulez-vous augmenter ?")
						print ("[1] PV")
						print ("[2] force")
						print ("[3] defense")
						print ("[4] vitesse")
						print ("[5] les 4")
						leg=input()
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
					if int(pal)==60:
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
						if int(carac)==1:
							vieup=vieup+1
						elif int(carac)==2:
							forceup=forceup+1
						elif int(carac)==3:
							defenseup=defenseup+1
						elif int(carac)==4:
							vitesseup=vitesseup+1
						print (" ")
						print ("PV = "+str(96+32*vieup+lootpv))
						print ("force = "+str(32+8*forceup+lootforce))
						print ("defense = "+str(16+4*defenseup+lootdefense))
						print ("vitesse = "+str(16+4*vitesseup+lootvitesse))
						print (" ")
						if int(lvl)==120 or int(lvl)==140 or int(lvl)==160:
							print ("vous maîtrisez une nouvelle puissance...")
					else:
						print ("niveau = "+str(lvl))
						print ("experience = "+str(exp)+"/"+str(expmax))
						print (" ")
			elif int(a)==2:
				boss = [1,1,1,2]
				capa=random.choice(boss)
				if int(capa)==1:
					degatm=frappe_ombre(forcem,defense)
					vie=vie-degatm
					print (" ")
					print (str(nomm)+" utilise frappe de l'ombre...")
					print ("-"+str(degatm)+" PV !")
					print ("PV ("+str(nom)+") = "+str(vie))
					print (" ")
				elif int(capa)==2:
					degatm=destru_primo(forcem,defense)
					vie=vie-degatm
					print (" ")
					print (str(nomm)+" utilise destruction primordiale !")
					print ("-"+str(degatm)+" PV !")
					print ("PV ("+str(nom)+") = "+str(vie))
					print (" ")
				
				if int(vie)<=0:
					print ("vous êtes mort...")
					mort=input()
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
	fw.close()
	
	if int(immortal)>=400000 and int(totalpv)>=2750 and int(keltu)==1:
		keltu=2
		immortal=0
		print (" ")
		print ("Vous avez terminé la quête de Kel'Thuzad !!!")
		print ("Pour vous recompenser, Kel'Thuzad vous transforme en liche...")
		print ("passif : convertis une partie de vos PV en force, defense et vitesse")
		lootforce=lootforce+(96+32*vieup+lootpv)//20
		lootdefense=lootdefense+(96+32*vieup+lootpv)//50
		lootvitesse=lootvitesse+(96+32*vieup+lootpv)//55
		lootpv=lootpv-(96+32*vieup+lootpv)//20-(96+32*vieup+lootpv)//50-(96+32*vieup+lootpv)//55
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		kel=input("[enter]")
		print (" ")
	elif int(frost)>=730 and int(amedemo)==1 and int(norfend)==1:
		norfend=2
		amedemo=0
		print (" ")
		print ("Vous avez terminé la quête de Frostmourne !!!")
		print ("Pour vous recompenser, vous vous transformez en chevalier de la mort...")
		print ("passif : convertis une partie de votre force en vie, defense et vitesse")
		lootpv=lootpv+(32+8*forceup+lootforce)*5//8
		lootdefense=lootdefense+(32+8*forceup+lootforce)//13
		lootvitesse=lootvitesse+(32+8*forceup+lootforce)//16
		lootforce=lootforce-(32+8*forceup+lootforce)*5//8-(32+8*forceup+lootforce)//13-(32+8*forceup+lootforce)//16
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		nor=input("[enter]")
		print (" ")
	elif int(armudemo)>=100000 and int(armuleg)>=350 and int(exode)==1:
		exode=2
		armudemo=0
		print (" ")
		print ("Vous avez terminé la quête de Thrall !!!")
		print ("Pour vous recompenser, Thrall vous transforme en guerrier...")
		print ("passif = convertis une partie de votre defense en vie, force et vitesse")
		lootpv=lootpv+(16+4*defenseup+lootdefense)*5//4
		lootforce=lootforce+(16+4*defenseup+lootdefense)*4//9
		lootvitesse=lootvitesse+(16+4*defenseup+lootdefense)//8
		lootdefense=lootdefense-(16+4*defenseup+lootdefense)*5//4-(16+4*defenseup+lootdefense)*4//9-(16+4*defenseup+lootdefense)//8
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		exo=input("[enter]")
		print (" ")
	elif int(vitilli)>=350 and int(agilistack)>=10000 and int(azzin)==1:
		azzin=2
		agilistack=0
		print (" ")
		print ("Vous avez terminé la quête d'Illidan !!!")
		print ("Pour vous recompenser, Illidan vous transforme en chasseur de démons...")
		print ("passif = +50 vitesse")
		lootpv=lootpv+(16+4*vitesseup+lootvitesse)*5//4
		lootforce=lootforce+(16+4*vitesseup+lootvitesse)*4//9
		lootdefense=lootdefense+(16+4*vitesseup+lootvitesse)//8
		lootvitesse=lootvitesse-(16+4*vitesseup+lootvitesse)*5//4-(16+4*vitesseup+lootvitesse)*4//9-(16+4*vitesseup+lootvitesse)//8
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		azz=input("[enter]")
		print (" ")
	elif int(chassedemo)>=15000 and int(gulpv)>=800 and int(gulfor)>=210 and int(guldef)>=100 and int(gulvit)>=100 and int(corrup)==1:
		corrup=2
		chassedemo=0
		print (" ")
		print ("Vous avez terminé la quête de Gul'Dan !!!")
		print ("Pour vous recompenser, Gul'Dan vous transforme en démoniste...")
		print ("vous devenez corrompu, vos attaques ignorent la defense de l'adversaire")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		corr=input("[enter]")
		print (" ")

	#if int(pal)

	#if int(quete2)==0 and int(pal)==210:
	#	if int(keltu)==2:
	#		print ("Comment ? vous avez réussi à tuer le demon qui gardait la porte des mondes ?")
	#		print ("Et vous avez encore soif de pouvoir...")
	#		print ("Désormais, vous pouvez traverser le portail et decouvrir de nouveaux mondes !")

#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

