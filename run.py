import os
import os.path
import random
import sys
from sorts import *
from autre import *

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
		wb=int(sauveg[52])
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
	vieup=0
	forceup=0
	defenseup=0
	vitesseup=0
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
	expmax=7*lvl
	if int(tuto)==0:
		tuto_detail(nom)
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
	print ("PV = "+str(1200+vieup+lootpv))
	print ("force = "+str(800+forceup+lootforce))
	print ("defense = "+str(400+defenseup+lootdefense))
	print ("vitesse = "+str(400+vitesseup+lootvitesse))
	print (" ")
	continuer=input("[enter]")
	print (" ")
	print (" ")
	print ("vous ne pouvez choisir qu'une quête, alors choisissez bien...")
	print (" ")
	print (" ")
	print ("[1] quête : Le sort d'immortalité de Kel'Thuzad (pour ceux qui aiment les PV)")
	print ("[2] quête : Libérer Frostmourne en Norfendre (pour ceux qui aiment la force)")
	print ("[3] quête : L'exode de Thrall des terres arides (pour ceux qui aiment la defense)")
	print ("[4] quête : Maîtriser les Lames d'Azzinoth (pour ceux qui aiment la vitesse)")
	print ("[5] quête : Eradiquer la corruption de Gul'Dan (pour ceux qui ne savent pas se décider...)")
	quete=input()
	while str(quete)!="1" and str(quete)!="2" and str(quete)!="3" and str(quete)!="4" and str(quete)!="5":
		print (" ")
		print (" ")
		print ("[1] quête : Le sort d'immortalité de Kel'Thuzad (pour ceux qui aiment les PV)")
		print ("[2] quête : Libérer Frostmourne en Norfendre (pour ceux qui aiment la force)")
		print ("[3] quête : L'exode de Thrall des terres arides (pour ceux qui aiment la defense)")
		print ("[4] quête : Maîtriser les Lames d'Azzinoth (pour ceux qui aiment la vitesse)")
		print ("[5] quête : Eradiquer la corruption de Gul'Dan (pour ceux qui ne savent pas se décider...)")
		print (" ")
		quete=input("Choisissez une quête en tapant le chiffre correspondant entre '1' et '5' : ")
	print (" ")
	print (" ")
	print (" ")
	if str(quete)=="1":
		keltu=1
		print ("Montrez la preuve de votre immortalité... (gagner 100 000 PV)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		immortal=0
		print ("Egaler la vie de Kel'Thuzad... (atteindre 5250 PV)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif str(quete)=="2":
		norfend=1
		print ("Augmenter votre force pour manier Frostmourne... (atteindre 3500 force)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Arracher l'âme d'un puissant demon pour nourrir Frostmourne... (tuer le demon primordial lvl 30)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print (" ")
		amedemo=0
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif str(quete)=="3":
		exode=1
		print ("Detruire les armures démoniaques... (enlever 100 000 defense)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		armudemo=0
		print ("Forger une armure légendaire pour Thrall... (atteindre 1750 defense)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif str(quete)=="4":
		azzin=1
		print ("Deplacer vous plus vite qu'Illidan... (atteindre 1750 vitesse)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Prouver votre agilité au combat... (effectuer 2 000 combos)")
		print (" ")
		continuer=input("[enter]")
		agilistack=0
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
	elif str(quete)=="5":
		corrup=1
		print ("Eliminer des demons pour chasser la corruption... (tuer 200 demons)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		chassedemo=0
		print ("Terroriser Gul'Dan par votre puissance... (atteindre 4800 PV, 3200 force, 1600 defense et 1600 vitesse)")
		print (" ")
		continuer=input("[enter]")
		print (" ")
		print ("Si vous finissez cette quête, votre classe changera...")
		print (" ")
		print (" ")
		print (" ")
else:
	exit()

while int(pal)<100:
	totalpv=1200+vieup+lootpv
	frost=800+forceup+lootforce
	armuleg=400+defenseup+lootdefense
	vitilli=400+vitesseup+lootvitesse
	gulpv=1200+vieup+lootpv
	gulfor=800+forceup+lootforce
	guldef=400+defenseup+lootdefense
	gulvit=400+vitesseup+lootvitesse
	if int(keltu)==1:
		print ("Quête : "+str(immortal)+"/100 000 PV gagnés")
		print ("Quête : "+str(totalpv)+"/5250 PV atteint")
	elif int(norfend)==1:
		print ("Quête : "+str(amedemo)+"/1 demon primordial lvl 30 tué")
		print ("Quête : "+str(frost)+"/3500 force atteinte")
	elif int(exode)==1:
		print ("Quête : "+str(armudemo)+"/100 000 defense enlevée")
		print ("Quête : "+str(armuleg)+"/1750 defense atteinte")
	elif int(azzin)==1:
		print ("Quête : "+str(vitilli)+"/1750 vitesse atteinte")
		print ("Quête : "+str(agilistack)+"/2 000 stack")
	elif int(corrup)==1:
		print ("Quête : "+str(chassedemo)+"/2 000 démons tués")
		print ("Quête : "+str(gulpv)+"/4800 PV atteint")
		print ("Quête : "+str(gulfor)+"/3200 force atteinte")
		print ("Quête : "+str(guldef)+"/1600 defense atteinte")
		print ("Quête : "+str(gulvit)+"/1600 vitesse atteinte")
	print (" ")
	print (" ")
	expmax=7*lvl
	if int(immortal)>=100000 and int(totalpv)>=5250 and int(keltu)==1:
		keltu=2
		immortal=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Kel'Thuzad !!!")
		print (" ")
		print ("Pour vous recompenser, Kel'Thuzad vous transforme en liche...")
		print (" ")
		print ("Convertis une partie de vos PV en force, defense et vitesse")
		print (" ")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		kel=input("[enter]")
		print (" ")
		print (" ")
	elif int(frost)>=3500 and int(amedemo)==1 and int(norfend)==1:
		norfend=2
		amedemo=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Frostmourne !!!")
		print (" ")
		print ("Pour vous recompenser, vous vous transformez en chevalier de la mort...")
		print (" ")
		print ("Convertis une partie de votre force en vie, defense et vitesse")
		print (" ")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		nor=input("[enter]")
		print (" ")
		print (" ")
	elif int(armudemo)>=100000 and int(armuleg)>=1750 and int(exode)==1:
		exode=2
		armudemo=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête de Thrall !!!")
		print (" ")
		print ("Pour vous recompenser, Thrall vous transforme en guerrier...")
		print (" ")
		print ("Convertis une partie de votre defense en vie, force et vitesse")
		print (" ")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		exo=input("[enter]")
		print (" ")
		print (" ")
	elif int(vitilli)>=1750 and int(agilistack)>=2000 and int(azzin)==1:
		azzin=2
		agilistack=0
		print (" ")
		print (" ")
		print ("Vous avez terminé la quête d'Illidan !!!")
		print (" ")
		print ("Pour vous recompenser, Illidan vous transforme en chasseur de démons...")
		print (" ")
		print ("Convertis une partie de votre vitesse en vie, force et defense")
		print (" ")
		print (" ")
		print ("Continuer votre progression pour pouvoir utiliser l'ensemble de vos nouveaux pouvoirs !")
		print (" ")
		azz=input("[enter]")
		print (" ")
		print (" ")
	elif int(chassedemo)>=200 and int(gulpv)>=3200 and int(gulfor)>=3200 and int(guldef)>=1600 and int(gulvit)>=1600 and int(corrup)==1:
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
	if int(keltu)==2:
		print ("[1] Demon lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
		print ("[2] Demon lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
		print ("[3] Demon lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
		print ("[4] Demon lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
	elif int(norfend)==2:
		print ("[1] Demon lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
		print ("[2] Demon lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
		print ("[3] Demon lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
		print ("[4] Demon lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
	elif int(exode)==2:
		print ("[1] Demon lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
		print ("[2] Demon lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
		print ("[3] Demon lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
		print ("[4] Demon lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
	elif int(azzin)==2:
		print ("[1] Demon lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+vitesseup+lootvitesse)*9//2)+")")
		print ("[2] Demon lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
		print ("[3] Demon lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
		print ("[4] Demon lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
	else:
		print ("[1] Demon lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
		print ("[2] Demon lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
		print ("[3] Demon lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
		print ("[4] Demon lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

	print ("[5] Demon lvl "+str(5+pal))
	print ("[6] Demon lvl "+str(6+pal)+"				Niveau = "+str(lvl))
	print ("[7] Demon lvl "+str(7+pal)+"				Expérience = "+str(exp)+" / "+str(expmax))
	print ("[8] Demon lvl "+str(8+pal))
	print ("[9] Demon lvl "+str(9+pal))
	if int(pal)==90:
		print ("[10] Demon infernal, gardien des portails")
	else:
		print ("[10] Demon primordial lvl "+str(10+pal))
	print ("[0] quitter")
	choix1=input()
	while str(choix1)!="1" and str(choix1)!="2" and str(choix1)!="3" and str(choix1)!="4" and str(choix1)!="5" and str(choix1)!="6" and str(choix1)!="7" and str(choix1)!="8" and str(choix1)!="9" and str(choix1)!="10" and str(choix1)!="0":
		print (" ")
		choix1=input("Merci de taper un chiffre entre '1' et '10' pour sélectionner le monstre à combattre ou taper '0' pour quitter : ")
		print (" ")
	if str(choix1)=="0":
		exit()
	elif str(choix1)=="1":
		lvlm=1+pal
	elif str(choix1)=="2":
		lvlm=2+pal
	elif str(choix1)=="3":
		lvlm=3+pal
	elif str(choix1)=="4":
		lvlm=4+pal
	elif str(choix1)=="5":
		lvlm=5+pal
	elif str(choix1)=="6":
		lvlm=6+pal
	elif str(choix1)=="7":
		lvlm=7+pal
	elif str(choix1)=="8":
		lvlm=8+pal
	elif str(choix1)=="9":
		lvlm=9+pal
	elif str(choix1)=="10":
		lvlm=10+pal
	if str(choix1)=="10":
		if int(pal)==90:
			nomm="Demon infernal, gardien des portails"
			viem=14175+1575*lvlm
			forcem=225+35*lvlm
			defensem=630+70*lvlm
			vitessem=72+8*lvlm
		else:
			nomm="Demon primordial lvl "+str(lvlm)
			viem=11813+1312*lvlm
			forcem=270+33*lvlm
			defensem=630+70*lvlm
			vitessem=153+17*lvlm
	else:
		nomm="Demon lvl "+str(lvlm)
		viem=9450+1050*lvlm
		forcem=288+32*lvlm
		defensem=630+70*lvlm
		vitessem=315+35*lvlm
	tour=0
	stackvit=1
	bloodstack=0
	degveng=0
	if int(keltu)==2:
		vie=1200+vieup+lootpv
		force=800+forceup+lootforce+(1200+vieup+lootpv)//25
		defense=400+defenseup+lootdefense+(1200+vieup+lootpv)//64
		vitesse=400+vitesseup+lootvitesse+(1200+vieup+lootpv)//64
	elif int(norfend)==2:
		vie=1200+vieup+lootpv+(800+forceup+lootforce)//9
		force=800+forceup+lootforce
		defense=400+defenseup+lootdefense+(800+forceup+lootforce)//45
		vitesse=400+vitesseup+lootvitesse+(800+forceup+lootforce)//45
	elif int(exode)==2:
		vie=1200+vieup+lootpv+(400+defenseup+lootdefense)*9//2
		force=800+forceup+lootforce+(400+defenseup+lootdefense)//9
		defense=400+defenseup+lootdefense
		vitesse=400+vitesseup+lootvitesse+(400+defenseup+lootdefense)*2//45
	elif int(azzin)==2:
		vie=1200+vieup+lootpv+(400+vitesseup+lootvitesse)*9//2
		force=800+forceup+lootforce+(400+vitesseup+lootvitesse)//9
		defense=400+defenseup+lootdefense+(400+vitesseup+lootvitesse)*2//45
		vitesse=400+vitesseup+lootvitesse
	else:
		vie=1200+vieup+lootpv
		force=800+forceup+lootforce
		defense=400+defenseup+lootdefense
		vitesse=400+vitesseup+lootvitesse
	maladie=0
	atb=0
	atbm=0
	atbmax=10000
	while int(vie)>0 and int(viem)>0:
		while int(atb)<int(atbmax) and int(atbm)<int(atbmax):
			atb=atb+vitesse
			atbm=atbm+vitessem
		bat=atb*100//atbmax
		batm=atbm*100//atbmax
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print ("___________________________________________________________________________________________________________________________________")
		print (" ")
		print ("			"+str(nom))
		print ("			PV = "+str(vie))
		print ("			Force = "+str(force))
		print ("			Defense = "+str(defense))
		print ("			Vitesse = "+str(vitesse))
		print ("			Jauge d'Attaque = "+str(bat)+"%")
		print ("___________________________________________________________________________________________________________________________________")
		print (" ")
		print ("									"+str(nomm))
		print ("									PV = "+str(viem))
		print ("									Force = "+str(forcem))
		print ("									Defense = "+str(defensem))
		print ("									Vitesse = "+str(vitessem))
		print ("									Jauge d'Attaque = "+str(batm)+"%")
		print ("___________________________________________________________________________________________________________________________________")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		if int(atb)>=int(atbmax):
			jeu=0
			atb=atb-atbmax
			print (" ")
			print ("A vous de jouer !")
			print (" ")
			while int(jeu)==0:
				if int(keltu)==2:
					print ("[1] Toucher sanglant")
					if int(pal)>=40:
						print ("[2] Pacte de sang")
					if int(pal)>=50:
						print ("[3] Transfert")
					if int(pal)>=60:
						print ("[4] Absorption")
					choix3=input()
					while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
						print (" ")
						choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix3)=="1":
						degat=degat_pv(force,defensem,degpv,keltu,ritsang)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str((1200+vieup+lootpv)*8//100)+" PV !")
						vie=vie+(1200+vieup+lootpv)*8//100
						print (" ")
						print (" ")
						bloodstack=bloodstack+1
						print ("Stack de sang = "+str(bloodstack))
						print (" ")
						print (" ")
						jeu=1
						ritsang=ritsang+1
						if int(ritsang)==200 or int(ritsang)==400 or int(ritsang)==600:
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
					elif str(choix3)=="2" and int(pal)>=40:
						degat=pacte_sang(defensem,pacte)
						print (" ")
						print (" ")
						print ("Vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
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
						print ("Stack de sang = "+str(bloodstack))
						print (" ")
						print (" ")
						pacte=pacte+1
						if int(pacte)==200 or int(pacte)==400 or int(pacte)==600:
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
					elif str(choix3)=="3" and int(pal)>=50:
						buff=transfert(defense,trans)
						print (" ")
						print (" ")
						print ("Vous sacrifiez votre armure pour augmenter votre vie !")
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
						print ("Stack de sang = "+str(bloodstack))	
						print (" ")
						print (" ")
						trans=trans+1
						if int(trans)==200 or int(trans)==400 or int(trans)==600:
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
					elif str(choix3)=="4" and int(pal)>=60:
						degat=absorption(force,defensem,bloodstack,abso)
						print (" ")
						print (" ")
						print ("Vous absorbez toutes les stacks de sang dans votre poing...")
						print ("Et dans un coup violent, faites bouillir le sang de votre adversaire !!!")
						print (" ")
						coup=input("[enter]")
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						bloodstack=0
						print ("Stack de sang = "+str(bloodstack))
						print (" ")
						print (" ")
						abso=abso+1
						jeu=1
						if int(abso)==200 or int(abso)==400 or int(abso)==600:
							print ("--------------------------------------------------------------------------------------")
							print ("                              ABSORPTION LVL UP !!!                              ")
							print ("--------------------------------------------------------------------------------------")
							print (" ")
							print (" ")
						else:
							print ("--------------------------------------------------------------------------------------")
							print ("                              "+str(abso)+"e ABSORPTION !                              ")
							print ("--------------------------------------------------------------------------------------")
							print (" ")
							print (" ")
						continuer=input("[enter]")
					else:
						pass
				elif int(norfend)==2:
					print ("[1] Frappe du fléau")
					if int(pal)>=40:
						print ("[2] Poigne de la mort")
					if int(pal)>=50:
						print ("[3] Renforcement")
					if int(pal)>=60:
						print ("[4] Aneantissement")
					choix3=input()
					while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
						print (" ")
						choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix3)=="1":
						degat=degat_force(force,defensem,degfor,norfend,mourne)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						maladie=maladie+degat//10
						print (str(nomm)+" souffre d'une maladie (-"+str(maladie)+" PV)")
						jeu=1
						print (" ")
						print (" ")
						mourne=mourne+1
						if int(mourne)==200 or int(mourne)==400 or int(mourne)==600:
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
					elif str(choix3)=="2" and int(pal)>=40:
						debuff=poigne_mort(forcem,poigne)
						forcem=forcem-debuff
						if int(forcem)<0:
							forcem=0
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(debuff)+" de force !")
						print (" ")
						print (" ")
						force=force+debuff*2
						print (str(nom)+" gagne "+str(debuff*2)+" de force !")
						print (" ")
						jeu=1
						print (" ")
						poigne=poigne+1
						if int(poigne)==200 or int(poigne)==400 or int(poigne)==600:
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
					elif str(choix3)=="3" and int(pal)>=50:
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str(force*30//100)+" de force !")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((400+vitesseup+lootvitesse)//2)+" de vitesse !")
						force=force+force*30//100
						vitesse=vitesse-(400+vitesseup+lootvitesse)//2
						if int(vitesse)<=0:
							vitesse=1
						jeu=1
						continuer=input("[enter]")
					elif str(choix3)=="4" and int(pal)>=60:
						degat=aneantissement(force,defensem,anean)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						jeu=1
						print (" ")
						print (str(nom)+" perd "+str((800+forceup+lootforce)*20//100)+" de force !")
						force=force-(800+forceup+lootforce)*20//100
						if int(force)<0:
							force=0
						print (" ")
						print (" ")
						anean=anean+1
						if int(anean)==200 or int(anean)==400 or int(anean)==600:
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
					else:
						pass
				elif int(exode)==2:
					print ("[1] Heurt de bouclier")
					if int(pal)>=40:
						print ("[2] Onde de choc")
					if int(pal)>=50:
						print ("[3] Berserker")
					if int(pal)>=60:
						print ("[4] Mur protecteur")
					choix3=input()
					while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
						print (" ")
						choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix3)=="1":
						degat=degat_defense(force,defensem,degdef,exode,war)
						viem=viem-degat
						degveng=degveng+degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(defensem*20//100)+" de defense !")
						defensem=defensem-defensem*20//100
						jeu=1
						print (" ")
						print (" ")
						war=war+1
						if int(war)==200 or int(war)==400 or int(war)==600:
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
					elif str(choix3)=="2" and int(pal)>=40:
						degat=onde_choc(force,defensem,onde)
						viem=viem-degat
						degveng=degveng+degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(vitessem*20//100)+" de vitesse !")
						vitessem=vitessem-vitessem*20//100
						print (" ")
						jeu=1
						print (" ")
						onde=onde+1
						if int(onde)==200 or int(onde)==400 or int(onde)==600:
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
					elif str(choix3)=="3" and int(pal)>=50:
						degat=vengeance(degveng,veng)
						viem=viem-degat
						print (" ")
						print (" ")
						print ("Vos blessures infligées à l'adversaire vous font enrager !")
						print ("Vous utilisez toute cette rage dans un coup destructeur...")
						print (" ")
						coup=input("[enter]")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !!")
						print (" ")
						print (" ")
						print ("Vous subissez le contrecoup...")
						print (" ")
						print (str(nom)+" perd "+str(degveng-defense)+" PV !")
						vie=vie-(degveng-defense)
						print (" ")
						degveng=0
						jeu=1
						print (" ")
						veng=veng+1
						if int(veng)==200 or int(veng)==400 or int(veng)==600:
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
					elif str(choix3)=="4" and int(pal)>=60:
						print (" ")
						print (" ")
						buff=mur_protecteur(defense,souffle)
						print ("Vous sacrifiez votre vie pour gagner de la défense !")
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str(buff)+" de defense !")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((1200+vieup+lootpv)*40//100)+" PV !")
						defense=defense+buff
						vie=vie-(1200+vieup+lootpv)*40//100
						print (" ")
						jeu=1
						print (" ")
						souffle=souffle+1
						if int(souffle)==200 or int(souffle)==400 or int(souffle)==600:
							print ("--------------------------------------------------------------------------------------")
							print ("                              MUR PROTECTEUR LVL UP !!!                              ")
							print ("--------------------------------------------------------------------------------------")
							print (" ")
							print (" ")
						else:
							print ("--------------------------------------------------------------------------------------")
							print ("                              "+str(souffle)+"e MUR PROTECTEUR !                              ")
							print ("--------------------------------------------------------------------------------------")
							print (" ")
							print (" ")
						continuer=input("[enter]")
					else:
						pass
				elif int(azzin)==2:
					print ("[1] Danse de l'ombre")
					if int(pal)>=40:
						print ("[2] Préméditation")
					if int(pal)>=50:
						print ("[3] Serie meutriere")
					if int(pal)>=60:
						print ("[4] Transformation")
					choix3=input()
					while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
						print (" ")
						choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix3)=="1":
						degat=degat_vitesse(force,stackvit,defensem,degvit,azzin,oth)
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
						if int(oth)==200 or int(oth)==400 or int(oth)==600:
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
					elif str(choix3)=="2" and int(pal)>=40:
						print (" ")
						print (" ")
						print ("Vous sacrifiez votre vitesse pour augmenter grandement votre combo...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((400+vitesseup+lootvitesse)*45//100)+" de vitesse !")
						print (" ")
						print (" ")
						vitesse=vitesse-(400+vitesseup+lootvitesse)*45//100
						stackvit=stackvit*2
						print ("Votre combo passe à "+str(stackvit))
						jeu=1
						print (" ")
						print (" ")
						continuer=input("[enter]")
					elif str(choix3)=="3" and int(pal)>=50:
						degat=serie_meurtriere(force,stackvit,defensem,serie)
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
						if int(serie)==200 or int(serie)==400 or int(serie)==600:
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
					elif str(choix3)=="4" and int(pal)>=60:
						print (" ")
						print (" ")
						print ("Vous canalisez une puissance démoniaque...")
						print ("Vous vous transformez en démon !")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str((400+defenseup+lootdefense)*25//100)+" de force !				"+str(nom)+" gagne "+str((400+defenseup+lootdefense)*25//100)+" de vitesse !")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((400+defenseup+lootdefense)*50//100)+" de defense !")
						print (" ")
						print (" ")
						vitesse=vitesse+(400+defenseup+lootdefense)*25//100
						force=force+(400+defenseup+lootdefense)*25//100
						defense=defense-(400+defenseup+lootdefense)*50//100
						jeu=1
						continuer=input("[enter]")
					else:
						pass
				elif int(corrup)==2:
					print ("[1] Ombreflamme")
					if int(pal)>=40:
						print ("[2] Drainage")
					if int(pal)>=50:
						print ("[3] Conversion")
					if int(pal)>=60:
						print ("[4] Feu de l'âme")
					choix3=input()
					while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
						print (" ")
						choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix3)=="1":
						degat=ombreflamme(force,ombre)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						jeu=1
						ombre=ombre+1
						if int(ombre)==200 or int(ombre)==400 or int(ombre)==600:
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
					elif str(choix3)=="2" and int(pal)>=40:
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
						if int(drain)==200 or int(drain)==400 or int(drain)==600:
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
					elif str(choix3)=="3" and int(pal)>=50:
						vie=vie-(1200+vieup+lootpv)*15//100
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((1200+vieup+lootpv)*20//100)+" PV !")
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str(force*20//100)+" de force !")
						print (" ")
						force=force+force*20//100
						print (" ")
						jeu=1
						continuer=input("[enter]")
					elif str(choix3)=="4" and int(pal)>=60:
						degat=feu_ame(force,feu)
						viem=viem-degat
						print (" ")
						print (" ")
						print ("Vous puisez dans votre âme pour générer une flamme maléfique...")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str((1200+vieup+lootpv)*25//100)+" PV !")
						vie=vie-(1200+vieup+lootpv)*25//100
						print (" ")
						print (" ")
						jeu=1
						feu=feu+1
						if int(feu)==200 or int(feu)==400 or int(feu)==600:
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
						pass
				else:
					print ("[1] Sanguinaire")
					print ("[2] Devaster")
					print ("[3] Coup de bouclier")
					print ("[4] Enchainement")
					choix2=input()
					while str(choix2)!="1" and str(choix2)!="2" and str(choix2)!="3" and str(choix2)!="4":
						print (" ")
						choix2=input("Taper le bon chiffre pour effectuer votre sort : ")
						print (" ")
					if str(choix2)=="1":
						degat=degat_pv(force,defensem,degpv,keltu,ritsang)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nom)+" gagne "+str((1200+vieup+lootpv)*5//100)+" PV !")
						vie=vie+(1200+vieup+lootpv)*5//100
						print (" ")
						jeu=1
						print (" ")
						if int(keltu)==1:
							immortal=immortal+(1200+vieup+lootpv)*5//100
						degpv=degpv+1
						if int(degpv)==200 or int(degpv)==400 or int(degpv)==600:
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
					elif str(choix2)=="2":
						degat=degat_force(force,defensem,degfor,norfend,mourne)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						jeu=1
						print (" ")
						degfor=degfor+1
						if int(degfor)==200 or int(degfor)==400 or int(degfor)==600:
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
					elif str(choix2)=="3":
						degat=degat_defense(force,defensem,degdef,exode,war)
						viem=viem-degat
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(degat)+" PV !")
						print (" ")
						print (" ")
						print (str(nomm)+" perd "+str(defensem*20//100)+" de defense !")
						defensem=defensem-defensem*20//100
						if int(defensem)<0:
							defensem=0
						print (" ")
						jeu=1
						print (" ")
						if int(exode)==1:
							armudemo=armudemo+defensem*20//100
						degdef=degdef+1
						if int(degdef)==200 or int(degdef)==400 or int(degdef)==600:
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
					elif str(choix2)=="4":
						degat=degat_vitesse(force,stackvit,defensem,degvit,azzin,oth)
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
						if int(degvit)==200 or int(degvit)==400 or int(degvit)==600:
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
				print ("Vous avez vaincu "+str(nomm)+" !!!")
				print (" ")
				print ("Vous gagnez "+str(lvlm)+" points d'experiences !")
				print (" ")
				print (" ")
				exp=exp+lvlm
				expmax=7*lvl				
				if int(exp)>=int(expmax):
					lvl=lvl+1
					print ("<><><><><><><><>")
					print ("              ")
					print ("   NIVEAU "+str(lvl)+"   ")
					print ("              ")
					print ("<><><><><><><><>")
					print (" ")
					print (" ")
					exp=exp-expmax
					if keltu==1 or keltu==2:
						print ("+135 PV")
						print ("+70 Force")
						print ("+35 Defense")
						print ("+35 Vitesse")
						vieup=vieup+135
						forceup=forceup+70
						defenseup=defenseup+35
						vitesseup=vitesseup+35
						print (" ")
						print (" ")
					if norfend==1 or norfend==2:
						print ("+105 PV")
						print ("+90 Force")
						print ("+35 Defense")
						print ("+35 Vitesse")
						vieup=vieup+105
						forceup=forceup+90
						defenseup=defenseup+35
						vitesseup=vitesseup+35
						print (" ")
						print (" ")
					if exode==1 or exode==2:
						print ("+105 PV")
						print ("+70 Force")
						print ("+45 Defense")
						print ("+35 Vitesse")
						vieup=vieup+105
						forceup=forceup+70
						defenseup=defenseup+45
						vitesseup=vitesseup+35
						print (" ")
						print (" ")
					if azzin==1 or azzin==2:
						print ("+105 PV")
						print ("+70 Force")
						print ("+35 Defense")
						print ("+45 Vitesse")
						vieup=vieup+105
						forceup=forceup+70
						defenseup=defenseup+35
						vitesseup=vitesseup+45
						print (" ")
						print (" ")
					if corrup==1 or corrup==2:
						print ("+120 PV")
						print ("+80 Force")
						print ("+40 Defense")
						print ("+40 Vitesse")
						vieup=vieup+120
						forceup=forceup+80
						defenseup=defenseup+40
						vitesseup=vitesseup+40
						print (" ")
						print (" ")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if str(choix1)=="10":
					if int(pal)==20:
						amedemo=1
					pal=pal+10
					lot=input("Vous ouvrez le coffre de loot...")
					print (" ")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
					loot = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
					lootchoice=random.choice(loot)
					if int(lootchoice)==1:
						print ("Vous gagnez le coeur de Kel'Thuzad !")
						print (" ")
						print ("+"+str(250+5*pal//2)+" PV !")
						lootpv=lootpv+250+5*pal//2
					elif int(lootchoice)==2:
						print ("Vous gagnez la lame d'Arthas !")
						print (" ")
						print ("+"+str(170+17*pal//10)+" force !")
						lootforce=lootforce+170+17*pal//10
					elif int(lootchoice)==3:
						print ("Vous gagnez l'armure de Thrall !")
						print (" ")
						print ("+"+str(90+9*pal//10)+" defense !")
						lootdefense=lootdefense+90+9*pal//10
					elif int(lootchoice)==4:
						print ("Vous gagnez les ailes d'Illidan !")
						print (" ")
						print ("+"+str(90+9*pal//10)+" vitesse !")
						lootvitesse=lootvitesse+90+9*pal//10
					elif int(lootchoice)==5:
						print ("Vous gagnez le crâne de Gul'dan !")
						print (" ")
						print ("+"+str(180+18*pal//10)+" PV !")
						print ("+"+str(50+5*pal//10)+" force !")
						print ("+"+str(25+25*pal//100)+" defense !")
						print ("+"+str(25+25*pal//100)+" vitesse !")
						lootpv=lootpv+180+18*pal//10
						lootforce=lootforce+50+5*pal//10
						lootdefense=lootdefense+25+25*pal//100
						lootvitesse=lootvitesse+25+25*pal//100
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
						print ("[2] Force")
						print ("[3] Defense")
						print ("[4] Vitesse")
						print ("[5] Les 4")
						leg=input()
						while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
							print (" ")
							leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
							print (" ")
						print (" ")
						print (" ")
						if str(leg)=="1":
							print ("+"+str(250+5*pal//2)+" PV !")
							lootpv=lootpv+250+5*pal//2
						elif str(leg)=="2":
							print ("+"+str(170+17*pal//10)+" Force !")
							lootforce=lootforce+170+17*pal//10
						elif str(leg)=="3":
							print ("+"+str(90+9*pal//10)+" Defense !")
							lootdefense=lootdefense+90+9*pal//10
						elif str(leg)=="4":
							print ("+"+str(90+9*pal//10)+" Vitesse !")
							lootvitesse=lootvitesse+90+9*pal//10
						elif str(leg)=="5":
							print ("+"+str(180+18*pal//10)+" PV !")
							print ("+"+str(50+5*pal//10)+" Force !")
							print ("+"+str(25+25*pal//100)+" Defense !")
							print ("+"+str(25+25*pal//100)+" Vitesse !")
							lootpv=lootpv+180+18*pal//10
							lootforce=lootforce+50+5*pal//10
							lootdefense=lootdefense+25+25*pal//100
							lootvitesse=lootvitesse+25+25*pal//100
					print (" ")
					print (" ")
					continuer=input("[enter]")
					if int(pal)==40 or int(pal)==50 or int(pal)==60:
						print ("Vous maîtrisez une nouvelle puissance...")
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
		elif int(atbm)>=int(atbmax):
			if int(maladie)!=0:
				print (" ")
				print (" ")
				print (str(nomm)+" perd "+str(maladie)+" PV à cause de la maladie...")
				maladie=0
				print (" ")
				continuer=input("[enter]")
			tour=tour+1
			atbm=atbm-atbmax
			print (" ")
			print (" ")
			print (str(nomm)+" va jouer !")
			print (" ")
			continuer=input("[enter]")
			print (" ")
			print (" ")
			if str(choix1)=="10":
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
					continuer=input("[enter]")
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
					continuer=input("[enter]")
			else:
				degatm=coup_demoniaque(forcem,defense)
				vie=vie-degatm
				print (str(nomm)+" vous frappe avec une puissance obscure...")
				print (" ")
				print (" ")
				print (str(nom)+" perd "+str(degatm)+" PV !")
				print (" ")
				print (" ")
				continuer=input("[enter]")
			if int(vie)<=0:
				print (" ")
				print ("Vous êtes mort...")
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
	print ("Une ombre apparait et alors que vous sortez votre épée, un simple geste de sa main vous paralyse de la tête au pied !")
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
	paldemo=100
	palimmo=100
	palbarb=100
	palelem=100
	palfufu=100
	quete2=1
	wb=0
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
	expmax=7*lvl
	print ("[1] Royaume des démons (caractéristiques équilibrées)")
	print ("[2] Lac des immortels (conseil : avoir beaucoup de PV)")
	print ("[3] Terres des barbares (conseil : avoir beaucoup d'armure)")
	print ("[4] Montagnes des elementaires (conseil : avoir beaucoup de force)")
	print ("[5] Iles des pirates (conseil : avoir beaucoup de vitesse)")
	if int(wb)==1:
		print ("[6] World Boss")
	print ("[0] Quitter")
	choix5=input()
	while str(choix5)!="1" and str(choix5)!="2" and str(choix5)!="3" and str(choix5)!="4" and str(choix5)!="5" and str(choix5)!="0":
		print (" ")
		choix5=input("Vous devez choisir un chiffre entre '0' et '5' : ")
		print (" ")
	if str(choix5)=="0":
		exit()
	elif str(choix5)=="1":
		if int(keltu)==2:
			print ("[1] Demon malsain lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Demon malsain lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
			print ("[3] Demon malsain lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
			print ("[4] Demon malsain lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
		elif int(norfend)==2:
			print ("[1] Demon malsain lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
			print ("[2] Demon malsain lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Demon malsain lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
			print ("[4] Demon malsain lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
		elif int(exode)==2:
			print ("[1] Demon malsain lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
			print ("[2] Demon malsain lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
			print ("[3] Demon malsain lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Demon malsain lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
		elif int(azzin)==2:
			print ("[1] Demon malsain lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str(400+vitesseup+lootvitesse)*9//2+")")
			print ("[2] Demon malsain lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
			print ("[3] Demon malsain lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
			print ("[4] Demon malsain lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
		else:
			print ("[1] Demon malsain lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Demon malsain lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Demon malsain lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Demon malsain lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

		print ("[5] Demon malsain lvl "+str(5+pal))
		print ("[6] Demon malsain lvl "+str(6+pal)+"				Niveau = "+str(lvl))
		print ("[7] Demon malsain lvl "+str(7+pal)+"				Experience = "+str(exp)+" / "+str(expmax))
		print ("[8] Demon malsain lvl "+str(8+pal))
		print ("[9] Demon malsain lvl "+str(9+pal))
		print ("[10] Maître demoniaque lvl "+str(10+pal))
		print ("[0] Changer de portail")
	elif str(choix5)=="2":
		if int(keltu)==2:
			print ("[1] Garde immortel lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Garde immortel lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
			print ("[3] Garde immortel lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
			print ("[4] Garde immortel lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
		elif int(norfend)==2:
			print ("[1] Garde immortel lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
			print ("[2] Garde immortel lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Garde immortel lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
			print ("[4] Garde immortel lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
		elif int(exode)==2:
			print ("[1] Garde immortel lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
			print ("[2] Garde immortel lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
			print ("[3] Garde immortel lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Garde immortel lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
		elif int(azzin)==2:
			print ("[1] Garde immortel lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str(400+vitesseup+lootvitesse)*9//2+")")
			print ("[2] Garde immortel lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
			print ("[3] Garde immortel lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
			print ("[4] Garde immortel lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
		else:
			print ("[1] Garde immortel lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Garde immortel lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Garde immortel lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Garde immortel lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

		print ("[5] Garde immortel lvl "+str(5+pal))
		print ("[6] Garde immortel lvl "+str(6+pal)+"				Niveau = "+str(lvl))
		print ("[7] Garde immortel lvl "+str(7+pal)+"				Experience = "+str(exp)+" / "+str(expmax))
		print ("[8] Garde immortel lvl "+str(8+pal))
		print ("[9] Garde immortel lvl "+str(9+pal))
		print ("[10] Roi immortel lvl "+str(10+pal))
		print ("[0] Changer de portail")

	elif str(choix5)=="3":
		if int(keltu)==2:
			print ("[1] Guerrier barbare lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Guerrier barbare lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
			print ("[3] Guerrier barbare lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
			print ("[4] Guerrier barbare lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
		elif int(norfend)==2:
			print ("[1] Guerrier barbare lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
			print ("[2] Guerrier barbare lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Guerrier barbare lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
			print ("[4] Guerrier barbare lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
		elif int(exode)==2:
			print ("[1] Guerrier barbare lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
			print ("[2] Guerrier barbare lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
			print ("[3] Guerrier barbare lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Guerrier barbare lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
		elif int(azzin)==2:
			print ("[1] Guerrier barbare lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str(400+vitesseup+lootvitesse)*9//2+")")
			print ("[2] Guerrier barbare lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
			print ("[3] Guerrier barbare lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
			print ("[4] Guerrier barbare lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
		else:
			print ("[1] Guerrier barbare lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Guerrier barbare lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Guerrier barbare lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Guerrier barbare lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

		print ("[5] Guerrier barbare lvl "+str(5+pal))
		print ("[6] Guerrier barbare lvl "+str(6+pal)+"				Niveau = "+str(lvl))
		print ("[7] Guerrier barbare lvl "+str(7+pal)+"				Experience = "+str(exp)+" / "+str(expmax))
		print ("[8] Guerrier barbare lvl "+str(8+pal))
		print ("[9] Guerrier barbare lvl "+str(9+pal))
		print ("[10] Seigneur barbare lvl "+str(10+pal))
		print ("[0] Changer de portail")

	elif str(choix5)=="4":
		if int(keltu)==2:
			print ("[1] Elementaire de pierre lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Elementaire de pierre lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
			print ("[3] Elementaire de pierre lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
			print ("[4] Elementaire de pierre lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
		elif int(norfend)==2:
			print ("[1] Elementaire de pierre lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
			print ("[2] Elementaire de pierre lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Elementaire de pierre lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
			print ("[4] Elementaire de pierre lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
		elif int(exode)==2:
			print ("[1] Elementaire de pierre lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
			print ("[2] Elementaire de pierre lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
			print ("[3] Elementaire de pierre lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Elementaire de pierre lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
		elif int(azzin)==2:
			print ("[1] Elementaire de pierre lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str(400+vitesseup+lootvitesse)*9//2+")")
			print ("[2] Elementaire de pierre lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
			print ("[3] Elementaire de pierre lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
			print ("[4] Elementaire de pierre lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
		else:
			print ("[1] Elementaire de pierre lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Elementaire de pierre lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Elementaire de pierre lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Elementaire de pierre lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

		print ("[5] Elementaire de pierre lvl "+str(5+pal))
		print ("[6] Elementaire de pierre lvl "+str(6+pal)+"				Niveau = "+str(lvl))
		print ("[7] Elementaire de pierre lvl "+str(7+pal)+"				Experience = "+str(exp)+" / "+str(expmax))
		print ("[8] Elementaire de pierre lvl "+str(8+pal))
		print ("[9] Elementaire de pierre lvl "+str(9+pal))
		print ("[10] Elementaire instable lvl "+str(10+pal))
		print ("[0] Changer de portail")

	elif str(choix5)=="5":
		if int(keltu)==2:
			print ("[1] Contrebandier lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Contrebandier lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((1200+vieup+lootpv)//25)+")")
			print ("[3] Contrebandier lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((1200+vieup+lootpv)//64)+")")
			print ("[4] Contrebandier lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((1200+vieup+lootpv)//64)+")")
		elif int(norfend)==2:
			print ("[1] Contrebandier lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((800+forceup+lootforce)//9)+")")
			print ("[2] Contrebandier lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Contrebandier lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((800+forceup+lootforce)//45)+")")
			print ("[4] Contrebandier lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((800+forceup+lootforce)//45)+")")
		elif int(exode)==2:
			print ("[1] Contrebandier lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str((400+defenseup+lootdefense)*9//2)+")")
			print ("[2] Contrebandier lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+defenseup+lootdefense)//9)+")")
			print ("[3] Contrebandier lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Contrebandier lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse)+" (+"+str((400+defenseup+lootdefense)*2//45)+")")
		elif int(azzin)==2:
			print ("[1] Contrebandier lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv)+" (+"+str(400+vitesseup+lootvitesse)*9//2+")")
			print ("[2] Contrebandier lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce)+" (+"+str((400+vitesseup+lootvitesse)//9)+")")
			print ("[3] Contrebandier lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense)+" (+"+str((400+vitesseup+lootvitesse)*2//45)+")")
			print ("[4] Contrebandier lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))
		else:
			print ("[1] Contrebandier lvl "+str(1+pal)+"				PV ("+str(nom)+") = "+str(1200+vieup+lootpv))
			print ("[2] Contrebandier lvl "+str(2+pal)+"				Force ("+str(nom)+") = "+str(800+forceup+lootforce))
			print ("[3] Contrebandier lvl "+str(3+pal)+"				Defense ("+str(nom)+") = "+str(400+defenseup+lootdefense))
			print ("[4] Contrebandier lvl "+str(4+pal)+"				Vitesse ("+str(nom)+") = "+str(400+vitesseup+lootvitesse))

		print ("[5] Contrebandier lvl "+str(5+pal))
		print ("[6] Contrebandier lvl "+str(6+pal)+"				Niveau = "+str(lvl))
		print ("[7] Contrebandier lvl "+str(7+pal)+"				Experience = "+str(exp)+" / "+str(expmax))
		print ("[8] Contrebandier lvl "+str(8+pal))
		print ("[9] Contrebandier lvl "+str(9+pal))
		print ("[10] Capitaine lvl "+str(10+pal))
		print ("[0] Changer de portail")

	choix1=input()
	while str(choix1)!="0" and str(choix1)!="1" and str(choix1)!="2" and str(choix1)!="3" and str(choix1)!="4" and str(choix1)!="5" and str(choix1)!="6" and str(choix1)!="7" and str(choix1)!="8" and str(choix1)!="9" and str(choix1)!="10":
		print (" ")
		choix1=input("Vous devez choisir un chiffre entre '0' et '10' : ")
		print (" ")
	if str(choix1)=="0":
		pass
	elif str(choix1)=="10":
		if str(choix5)=="1":
			lvlm=10+paldemo
			nomm="Maître démoniaque lvl "+str(lvlm)
			viem=11900+1392*lvlm
			forcem=270+35*lvlm
			defensem=630+71*lvlm
			vitessem=155+18*lvlm
		elif str(choix5)=="2":
			lvlm=10+palimmo
			nomm="Roi immortel lvl "+str(lvlm)
			viem=15625+12687*lvlm
			forcem=254+32*lvlm
			defensem=10+1*lvlm
			vitessem=20+2*lvlm
		elif str(choix5)=="3":
			lvlm=10+palbarb
			nomm="Seigneur barbare lvl "+str(lvlm)
			viem=13230+1540*lvlm
			forcem=522+69*lvlm
			defensem=330+34*lvlm
			vitessem=76+9*lvlm
		elif str(choix5)=="4":
			lvlm=10+palelem
			nomm="Elementaire instable lvl "+str(lvlm)
			viem=11812+1375*lvlm
			forcem=140+17*lvlm
			defensem=1207+141*lvlm
			vitessem=157+18*lvlm
		elif str(choix5)=="5":
			lvlm=10+palfufu
			nomm="Capitaine lvl "+str(lvlm)
			viem=13230+1540*lvlm
			forcem=71+9*lvlm
			defensem=150+16*lvlm
			vitessem=625+67*lvlm
	else:
		if str(choix5)=="1":
			if str(choix1)=="1":
				lvlm=1+paldemo
			elif str(choix1)=="2":
				lvlm=2+paldemo
			elif str(choix1)=="3":
				lvlm=3+paldemo
			elif str(choix1)=="4":
				lvlm=4+paldemo
			elif str(choix1)=="5":
				lvlm=5+paldemo
			elif str(choix1)=="6":
				lvlm=6+paldemo
			elif str(choix1)=="7":
				lvlm=7+paldemo
			elif str(choix1)=="8":
				lvlm=8+paldemo
			elif str(choix1)=="9":
				lvlm=9+paldemo
			nomm="Demon malsain lvl "+str(lvlm)
			viem=9450+1100*lvlm
			forcem=290+34*lvlm
			defensem=630+71*lvlm
			vitessem=315+36*lvlm
		elif str(choix5)=="2":
			if str(choix1)=="1":
				lvlm=1+palimmo
			elif str(choix1)=="2":
				lvlm=2+palimmo
			elif str(choix1)=="3":
				lvlm=3+palimmo
			elif str(choix1)=="4":
				lvlm=4+palimmo
			elif str(choix1)=="5":
				lvlm=5+palimmo
			elif str(choix1)=="6":
				lvlm=6+palimmo
			elif str(choix1)=="7":
				lvlm=7+palimmo
			elif str(choix1)=="8":
				lvlm=8+palimmo
			elif str(choix1)=="9":
				lvlm=9+palimmo
			nomm="Garde immortel lvl "+str(lvlm)
			viem=12500+10150*lvlm
			forcem=287+30*lvlm
			defensem=10+1*lvlm
			vitessem=42+4*lvlm
		elif str(choix5)=="3":
			if str(choix1)=="1":
				lvlm=1+palbarb
			elif str(choix1)=="2":
				lvlm=2+palbarb
			elif str(choix1)=="3":
				lvlm=3+palbarb
			elif str(choix1)=="4":
				lvlm=4+palbarb
			elif str(choix1)=="5":
				lvlm=5+palbarb
			elif str(choix1)=="6":
				lvlm=6+palbarb
			elif str(choix1)=="7":
				lvlm=7+palbarb
			elif str(choix1)=="8":
				lvlm=8+palbarb
			elif str(choix1)=="9":
				lvlm=9+palbarb
			nomm="Guerrier barbare lvl "+str(lvlm)
			viem=10584+1232*lvlm
			forcem=545+68*lvlm
			defensem=330+34*lvlm
			vitessem=155+18*lvlm
		elif str(choix5)=="4":
			if str(choix1)=="1":
				lvlm=1+palelem
			elif str(choix1)=="2":
				lvlm=2+palelem
			elif str(choix1)=="3":
				lvlm=3+palelem
			elif str(choix1)=="4":
				lvlm=4+palelem
			elif str(choix1)=="5":
				lvlm=5+palelem
			elif str(choix1)=="6":
				lvlm=6+palelem
			elif str(choix1)=="7":
				lvlm=7+palelem
			elif str(choix1)=="8":
				lvlm=8+palelem
			elif str(choix1)=="9":
				lvlm=9+palelem
			nomm="Elementaire de pierre lvl "+str(lvlm)
			viem=9450+1100*lvlm
			forcem=140+15*lvlm
			defensem=1210+140*lvlm
			vitessem=315+36*lvlm
		elif str(choix5)=="5":
			if str(choix1)=="1":
				lvlm=1+palfufu
			elif str(choix1)=="2":
				lvlm=2+palfufu
			elif str(choix1)=="3":
				lvlm=3+palfufu
			elif str(choix1)=="4":
				lvlm=4+palfufu
			elif str(choix1)=="5":
				lvlm=5+palfufu
			elif str(choix1)=="6":
				lvlm=6+palfufu
			elif str(choix1)=="7":
				lvlm=7+palfufu
			elif str(choix1)=="8":
				lvlm=8+palfufu
			elif str(choix1)=="9":
				lvlm=9+palfufu
			nomm="Contrebandier lvl "+str(lvlm)
			viem=10584+1232*lvlm
			forcem=145+16*lvlm
			defensem=150+16*lvlm
			vitessem=615+61*lvlm
		tour=0
		stackvit=1
		bloodstack=0
		degveng=0
		if int(keltu)==2:
			vie=1200+vieup+lootpv
			force=800+forceup+lootforce+(1200+vieup+lootpv)//25
			defense=400+defenseup+lootdefense+(1200+vieup+lootpv)//64
			vitesse=400+vitesseup+lootvitesse+(1200+vieup+lootpv)//64
		elif int(norfend)==2:
			vie=1200+vieup+lootpv+(800+forceup+lootforce)//9
			force=800+forceup+lootforce
			defense=400+defenseup+lootdefense+(800+forceup+lootforce)//45
			vitesse=400+vitesseup+lootvitesse+(800+forceup+lootforce)//45
		elif int(exode)==2:
			vie=1200+vieup+lootpv+(400+defenseup+lootdefense)*9//2
			force=800+forceup+lootforce+(400+defenseup+lootdefense)//9
			defense=400+defenseup+lootdefense
			vitesse=400+vitesseup+lootvitesse+(400+defenseup+lootdefense)*2//45
		elif int(azzin)==2:
			vie=1200+vieup+lootpv+(400+vitesseup+lootvitesse)*9//2
			force=800+forceup+lootforce+(400+vitesseup+lootvitesse)//9
			defense=400+defenseup+lootdefense+(400+vitesseup+lootvitesse)*2//45
			vitesse=400+vitesseup+lootvitesse
		else:
			vie=1200+vieup+lootpv
			force=800+forceup+lootforce
			defense=400+defenseup+lootdefense
			vitesse=400+vitesseup+lootvitesse
		atb=0
		atbm=0
		atbmax=10000
		maladie=0
		while int(vie)>0 and int(viem)>0:
			while int(atb)<int(atbmax) and int(atbm)<int(atbmax):
				atb=atb+vitesse
				atbm=atbm+vitessem
			bat=atb*100//atbmax
			batm=atbm*100//atbmax
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print ("			"+str(nom))
			print ("			PV = "+str(vie))
			print ("			Force = "+str(force))
			print ("			Defense = "+str(defense))
			print ("			Vitesse = "+str(vitesse))
			print ("			Jauge d'Attaque = "+str(bat)+"%")
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print ("									"+str(nomm))
			print ("									PV = "+str(viem))
			print ("									Force = "+str(forcem))
			print ("									Defense = "+str(defensem))
			print ("									Vitesse = "+str(vitessem))
			print ("									Jauge d'Attaque = "+str(batm)+"%")
			print ("___________________________________________________________________________________________________________________________________")
			print (" ")
			print (" ")
			print (" ")
			print (" ")
			if int(atb)>=int(atbmax):
				jeu=0
				atb=atb-atbmax
				print (" ")
				print ("A vous de jouer !")
				print (" ")
				while int(jeu)==0:
					if int(keltu)==2:
						print ("[1] Toucher sanglant")
						if int(pal)>=40:
							print ("[2] Pacte de sang")
						if int(pal)>=50:
							print ("[3] Transfert")
						if int(pal)>=60:
							print ("[4] Absorption")
						choix3=input()
						while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
							print (" ")
							choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix3)=="1":
							degat=degat_pv(force,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str((1200+vieup+lootpv)*8//100)+" PV !")
							vie=vie+(1200+vieup+lootpv)*8//100
							print (" ")
							print (" ")
							bloodstack=bloodstack+1
							print ("Stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							jeu=1
							ritsang=ritsang+1
							if int(ritsang)==200 or int(ritsang)==400 or int(ritsang)==600:
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
						elif str(choix3)=="2" and int(pal)>=40:
							degat=pacte_sang(defensem,pacte)
							print (" ")
							print (" ")
							print ("Vous sacrifiez une partie de votre vie pour détruire l'armure de l'adversaire !")
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
							print ("Stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							pacte=pacte+1
							if int(pacte)==200 or int(pacte)==400 or int(pacte)==600:
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
						elif str(choix3)=="3" and int(pal)>=50:
							buff=transfert(defense,trans)
							print (" ")
							print (" ")
							print ("Vous sacrifiez votre armure pour augmenter votre vie !")
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
							print ("Stack de sang = "+str(bloodstack))	
							print (" ")
							print (" ")
							trans=trans+1
							if int(trans)==200 or int(trans)==400 or int(trans)==600:
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
						elif str(choix3)=="4" and int(pal)>=60:
							degat=absorption(force,defensem,bloodstack,abso)
							print (" ")
							print (" ")
							print ("Vous absorbez toutes les stacks de sang dans votre poing...")
							print ("Et dans un coup violent, faites bouillir le sang de votre adversaire !!!")
							print (" ")
							coup=input("[enter]")
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							bloodstack=0
							print ("Stack de sang = "+str(bloodstack))
							print (" ")
							print (" ")
							abso=abso+1
							jeu=1
							if int(abso)==200 or int(abso)==400 or int(abso)==600:
								print ("--------------------------------------------------------------------------------------")
								print ("                              ABSORPTION LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(abso)+"e ABSORPTION !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
					elif int(norfend)==2:
						print ("[1] Frappe du fléau")
						if int(pal)>=40:
							print ("[2] Poigne de la mort")
						if int(pal)>=50:
							print ("[3] Renforcement")
						if int(pal)>=60:
							print ("[4] Aneantissement")
						choix3=input()
						while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
							print (" ")
							choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix3)=="1":
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							maladie=maladie+degat//10
							print (str(nomm)+" souffre d'une maladie (-"+str(maladie)+" PV)")
							jeu=1
							print (" ")
							print (" ")
							mourne=mourne+1
							if int(mourne)==200 or int(mourne)==400 or int(mourne)==600:
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
						elif str(choix3)=="2" and int(pal)>=40:
							debuff=poigne_mort(forcem,poigne)
							forcem=forcem-debuff
							if int(forcem)<0:
								forcem=0
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(debuff)+" de force !")
							print (" ")
							print (" ")
							force=force+debuff*2
							print (str(nom)+" gagne "+str(debuff*2)+" de force !")
							print (" ")
							jeu=1
							print (" ")
							poigne=poigne+1
							if int(poigne)==200 or int(poigne)==400 or int(poigne)==600:
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
						elif str(choix3)=="3" and int(pal)>=50:
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*30//100)+" de force !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((400+vitesseup+lootvitesse)//2)+" de vitesse !")
							force=force+force*30//100
							vitesse=vitesse-(400+vitesseup+lootvitesse)//2
							if int(vitesse)<=0:
								vitesse=1
							jeu=1
							continuer=input("[enter]")
						elif str(choix3)=="4" and int(pal)>=60:
							degat=aneantissement(force,defensem,anean)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							print (str(nom)+" perd "+str((800+forceup+lootforce)*20//100)+" de force !")
							force=force-(800+forceup+lootforce)*20//100
							if int(force)<0:
								force=0
							print (" ")
							print (" ")
							anean=anean+1
							if int(anean)==200 or int(anean)==400 or int(anean)==600:
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
						else:
							pass
					elif int(exode)==2:
						print ("[1] Heurt de bouclier")
						if int(pal)>=40:
							print ("[2] Onde de choc")
						if int(pal)>=50:
							print ("[3] Berserker")
						if int(pal)>=60:
							print ("[4] Mur protecteur")
						choix3=input()
						while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
							print (" ")
							choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix3)=="1":
							degat=degat_defense(force,defensem,degdef,exode,war)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem*20//100)+" de defense !")
							defensem=defensem-defensem*20//100
							jeu=1
							print (" ")
							print (" ")
							war=war+1
							if int(war)==200 or int(war)==400 or int(war)==600:
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
						elif str(choix3)=="2" and int(pal)>=40:
							degat=onde_choc(force,defensem,onde)
							viem=viem-degat
							degveng=degveng+degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(vitessem*20//100)+" de vitesse !")
							vitessem=vitessem-vitessem*20//100
							print (" ")
							jeu=1
							print (" ")
							onde=onde+1
							if int(onde)==200 or int(onde)==400 or int(onde)==600:
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
						elif str(choix3)=="3" and int(pal)>=50:
							degat=vengeance(degveng,veng)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vos blessures infligées à l'adversaire vous font enrager !")
							print ("Vous utilisez toute cette rage dans un coup destructeur...")
							print (" ")
							coup=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !!")
							print (" ")
							print (" ")
							print ("Vous subissez le contrecoup...")
							print (" ")
							print (str(nom)+" perd "+str(degveng-defense)+" PV !")
							vie=vie-(degveng-defense)
							print (" ")
							degveng=0
							jeu=1
							print (" ")
							veng=veng+1
							if int(veng)==200 or int(veng)==400 or int(veng)==600:
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
						elif str(choix3)=="4" and int(pal)>=60:
							print (" ")
							print (" ")
							buff=mur_protecteur(defense,souffle)
							print ("Vous sacrifiez votre vie pour gagner de la défense !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(buff)+" de defense !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((1200+vieup+lootpv)*40//100)+" PV !")
							defense=defense+buff
							vie=vie-(1200+vieup+lootpv)*40//100
							print (" ")
							jeu=1
							print (" ")
							souffle=souffle+1
							if int(souffle)==200 or int(souffle)==400 or int(souffle)==600:
								print ("--------------------------------------------------------------------------------------")
								print ("                              MUR PROTECTEUR LVL UP !!!                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							else:
								print ("--------------------------------------------------------------------------------------")
								print ("                              "+str(souffle)+"e MUR PROTECTEUR !                              ")
								print ("--------------------------------------------------------------------------------------")
								print (" ")
								print (" ")
							continuer=input("[enter]")
						else:
							pass
					elif int(azzin)==2:
						print ("[1] Danse de l'ombre")
						if int(pal)>=40:
							print ("[2] Préméditation")
						if int(pal)>=50:
							print ("[3] Serie meutriere")
						if int(pal)>=60:
							print ("[4] Transformation")
						choix3=input()
						while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
							print (" ")
							choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix3)=="1":
							degat=degat_vitesse(force,stackvit,defensem,degvit,azzin,oth)
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
							if int(oth)==200 or int(oth)==400 or int(oth)==600:
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
						elif str(choix3)=="2" and int(pal)>=40:
							print (" ")
							print (" ")
							print ("Vous sacrifiez votre vitesse pour augmenter grandement votre combo...")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((400+vitesseup+lootvitesse)*45//100)+" de vitesse !")
							print (" ")
							print (" ")
							vitesse=vitesse-(400+vitesseup+lootvitesse)*45//100
							stackvit=stackvit*2
							print ("Votre combo passe à "+str(stackvit))
							jeu=1
							print (" ")
							print (" ")
							continuer=input("[enter]")
						elif str(choix3)=="3" and int(pal)>=50:
							degat=serie_meurtriere(force,stackvit,defensem,serie)
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
							if int(serie)==200 or int(serie)==400 or int(serie)==600:
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
						elif str(choix3)=="4" and int(pal)>=60:
							print (" ")
							print (" ")
							print ("Vous canalisez une puissance démoniaque...")
							print ("Vous vous transformez en démon !")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str((400+defenseup+lootdefense)*25//100)+" de force !				"+str(nom)+" gagne "+str((400+defenseup+lootdefense)*25//100)+" de vitesse !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((400+defenseup+lootdefense)*50//100)+" de defense !")
							print (" ")
							print (" ")
							vitesse=vitesse+(400+defenseup+lootdefense)*25//100
							force=force+(400+defenseup+lootdefense)*25//100
							defense=defense-(400+defenseup+lootdefense)*50//100
							jeu=1
							continuer=input("[enter]")
						else:
							pass
					elif int(corrup)==2:
						print ("[1] Ombreflamme")
						if int(pal)>=40:
							print ("[2] Drainage")
						if int(pal)>=50:
							print ("[3] Conversion")
						if int(pal)>=60:
							print ("[4] Feu de l'âme")
						choix3=input()
						while str(choix3)!="1" and str(choix3)!="2" and str(choix3)!="3" and str(choix3)!="4":
							print (" ")
							choix3=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix3)=="1":
							degat=ombreflamme(force,ombre)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							jeu=1
							ombre=ombre+1
							if int(ombre)==200 or int(ombre)==400 or int(ombre)==600:
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
						elif str(choix3)=="2" and int(pal)>=40:
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
							if int(drain)==200 or int(drain)==400 or int(drain)==600:
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
						elif str(choix3)=="3" and int(pal)>=50:
							vie=vie-(110+vieup+lootpv)//5
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((110+vieup+lootpv)//5)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str(force*3//2)+" de force !")
							print (" ")
							force=force*3//2
							print (" ")
							jeu=1
							continuer=input("[enter]")
						elif str(choix3)=="4" and int(pal)>=60:
							degat=feu_ame(force,feu)
							viem=viem-degat
							print (" ")
							print (" ")
							print ("Vous puisez dans votre âme pour générer une flamme maléfique...")
							print (" ")
							continuer=input("[enter]")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" perd "+str((1200+vieup+lootpv)*25//100)+" PV !")
							vie=vie-(1200+vieup+lootpv)*25//100
							print (" ")
							print (" ")
							jeu=1
							feu=feu+1
							if int(feu)==200 or int(feu)==400 or int(feu)==600:
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
							pass
					else:
						print ("[1] Sanguinaire")
						print ("[2] Devaster")
						print ("[3] Coup de bouclier")
						print ("[4] Enchainement")
						choix2=input()
						while str(choix2)!="1" and str(choix2)!="2" and str(choix2)!="3" and str(choix2)!="4":
							print (" ")
							choix2=input("Taper le bon chiffre pour effectuer votre sort : ")
							print (" ")
						if str(choix2)=="1":
							degat=degat_pv(force,defensem,degpv,keltu,ritsang)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nom)+" gagne "+str((1200+vieup+lootpv)*5//100)+" PV !")
							vie=vie+(1200+vieup+lootpv)*5//100
							print (" ")
							jeu=1
							print (" ")
							if int(keltu)==1:
								immortal=immortal+(1200+vieup+lootpv)*5//100
							degpv=degpv+1
							if int(degpv)==200 or int(degpv)==400 or int(degpv)==600:
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
						elif str(choix2)=="2":
							degat=degat_force(force,defensem,degfor,norfend,mourne)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							jeu=1
							print (" ")
							degfor=degfor+1
							if int(degfor)==200 or int(degfor)==400 or int(degfor)==600:
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
						elif str(choix2)=="3":
							degat=degat_defense(force,defensem,degdef,exode,war)
							viem=viem-degat
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(degat)+" PV !")
							print (" ")
							print (" ")
							print (str(nomm)+" perd "+str(defensem*20//100)+" de defense !")
							defensem=defensem-defensem*20//100
							if int(defensem)<0:
								defensem=0
							print (" ")
							jeu=1
							print (" ")
							if int(exode)==1:
								armudemo=armudemo+defensem*20//100
							degdef=degdef+1
							if int(degdef)==200 or int(degdef)==400 or int(degdef)==600:
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
						elif str(choix2)=="4":
							degat=degat_vitesse(force,stackvit,defensem,degvit,azzin,oth)
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
							if int(degvit)==200 or int(degvit)==400 or int(degvit)==600:
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
					print ("Vous avez vaincu "+str(nomm)+" !!!")
					print (" ")
					print ("Vous gagnez "+str(lvlm)+" points d'experiences !")
					print (" ")
					print (" ")
					if int(corrup)==2:
						ame=ame+1
						print ("Votre stock d'âme passe à "+str(ame))
						print (" ")
						print (" ")
					if str(choix1)=="10":
						lot=input("Vous ouvrez le coffre de loot...")
						print (" ")
						print (" ")
						continuer=input("[enter]")
						print (" ")
						print (" ")
						loot = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
						lootchoice=random.choice(loot)
						if str(choix5)=="1":
							if int(lootchoice)==1:
								print ("Vous gagnez un coeur de demon !")
								print (" ")
								print ("+"+str(250+3*paldemo)+" PV !")
								lootpv=lootpv+250+3*paldemo
							elif int(lootchoice)==2:
								print ("Vous gagnez un bras de demon !")
								print (" ")
								print ("+"+str(170+20*paldemo//10)+" force !")
								lootforce=lootforce+170+20*paldemo//10
							elif int(lootchoice)==3:
								print ("Vous gagnez un os de demon !")
								print (" ")
								print ("+"+str(90+10*paldemo//10)+" defense !")
								lootdefense=lootdefense+90+10*paldemo//10
							elif int(lootchoice)==4:
								print ("Vous gagnez une jambe de demon !")
								print (" ")
								print ("+"+str(90+10*paldemo//10)+" vitesse !")
								lootvitesse=lootvitesse+90+10*paldemo//10
							elif int(lootchoice)==5:
								print ("Vous gagnez une tête de demon !")
								print (" ")
								print ("+"+str(180+5*paldemo//4)+" PV !")
								print ("+"+str(80+17*paldemo//20)+" force !")
								print ("+"+str(40+9*paldemo//20)+" defense !")
								print ("+"+str(40+9*paldemo//20)+" vitesse !")
								lootpv=lootpv+180+5*paldemo//4
								lootforce=lootforce+80+17*paldemo//20
								lootdefense=lootdefense+40+9*paldemo//20
								lootvitesse=lootvitesse+40+9*paldemo//20
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
								print ("[2] Force")
								print ("[3] Defense")
								print ("[4] Vitesse")
								print ("[5] Les 4")
								leg=input()
								while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
									print (" ")
									leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
									print (" ")
								print (" ")
								print (" ")
								if str(leg)=="1":
									print ("+"+str(250+5*paldemo//2)+" PV !")
									lootpv=lootpv+250+5*paldemo//2
								elif str(leg)=="2":
									print ("+"+str(170+17*paldemo//10)+" force !")
									lootforce=lootforce+170+17*paldemo//10
								elif str(leg)=="3":
									print ("+"+str(90+paldemo*9//10)+" defense !")
									lootdefense=lootdefense+90+paldemo*9//10
								elif str(leg)=="4":
									print ("+"+str(90+paldemo*9//10)+" vitesse !")
									lootvitesse=lootvitesse+90+paldemo*9//10
								elif str(leg)=="5":
									print ("+"+str(180+5*paldemo//4)+" PV !")
									print ("+"+str(80+paldemo*17//20)+" force !")
									print ("+"+str(40+paldemo*9//20)+" defense !")
									print ("+"+str(40+paldemo*9//20)+" vitesse !")
									lootpv=lootpv+180+5*paldemo//4
									lootforce=lootforce+80+paldemo*17//20
									lootdefense=lootdefense+40+paldemo*9//20
									lootvitesse=lootvitesse+40+paldemo*9//20
						if str(choix5)=="2":
							if int(lootchoice)==1:
								print ("Vous gagnez une goutte d'eau enchantée !")
								print (" ")
								print ("+"+str(310+312*palimmo//100)+" PV !")
								lootpv=lootpv+310+312*palimmo//100
							elif int(lootchoice)==2:
								print ("Vous gagnez une épée enchantée !")
								print (" ")
								print ("+"+str(127+palimmo*127//100)+" de force !")
								print ("+"+str(62+palimmo*62//100)+" PV !")
								lootforce=lootforce+127+palimmo*127//100
								lootpv=lootpv+62+62*palimmo//100
							elif int(lootchoice)==3:
								print ("Vous gagnez un bouclier enchantée !")
								print (" ")
								print ("+"+str(67+67*palimmo//100)+" de defense !")
								print ("+"+str(62+62*palimmo//100)+" PV !")
								lootdefense=lootdefense+67+palimmo*67//100
								lootpv=lootpv+62+62*palimmo//100
							elif int(lootchoice)==4:
								print ("Vous gagnez une plume enchantée !")
								print (" ")
								print ("+"+str(67+67*palimmo//100)+" de vitesse !")
								print ("+"+str(62+62*palimmo//100)+" PV !")
								lootvitesse=lootvitesse+67+67*palimmo//100
								lootpv=lootpv+62+62*palimmo//100
							elif int(lootchoice)==5:
								print ("Vous gagnez une bague divine !")
								print (" ")
								print ("+"+str(310+312*palimmo//200)+" PV !")
								print ("+"+str(127+127*palimmo//200)+" force !")
								print ("+"+str(67+67*palimmo//200)+" defense !")
								print ("+"+str(67+67*palimmo//200)+" vitesse !")
								lootpv=lootpv+310+312*palimmo//200
								lootforce=lootforce+127+127*palimmo//200
								lootdefense=lootdefense+67+67*palimmo//200
								lootvitesse=lootvitesse+67+67*palimmo//200
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
								print ("[2] Force")
								print ("[3] Defense")
								print ("[4] Vitesse")
								print ("[5] Les 4")
								leg=input()
								while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
									print (" ")
									leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
									print (" ")
								print (" ")
								print (" ")
								if str(leg)=="1":
									print ("+"+str(250+5*palimmo//2)+" PV !")
									lootpv=lootpv+200+5*palimmo//2
								elif str(leg)=="2":
									print ("+"+str(170+17*palimmo//10)+" force !")
									lootforce=lootforce+170+palimmo//10
								elif str(leg)=="3":
									print ("+"+str(90+9*palimmo//10)+" defense !")
									lootdefense=lootdefense+90+9*palimmo//10
								elif str(leg)=="4":
									print ("+"+str(90+9*palimmo//10)+" vitesse !")
									lootvitesse=lootvitesse+90+9*palimmo//10
								elif str(leg)=="5":
									print ("+"+str(180+5*palimmo//4)+" PV !")
									print ("+"+str(80+17*palimmo//20)+" force !")
									print ("+"+str(40+9*palimmo//20)+" defense !")
									print ("+"+str(40+9*palimmo//20)+" vitesse !")
									lootpv=lootpv+180+5*palimmo//4
									lootforce=lootforce+80+17*palimmo//20
									lootdefense=lootdefense+40+9*palimmo//20
									lootvitesse=lootvitesse+40+9*palimmo//20
						if str(choix5)=="3":
							if int(lootchoice)==1:
								print ("Vous gagnez une fiole de sang barbare !")
								print (" ")
								print ("+"+str(187+187*palbarb//100)+" PV !")
								print ("+"+str(42+42*palbarb//100)+" force !")
								lootpv=lootpv+187+187*palbarb//100
								lootforce=lootforce+42+42*palbarb//100
							elif int(lootchoice)==2:
								print ("Vous gagnez une hache barbare !")
								print (" ")
								print ("+"+str(212+212*palbarb//100)+" force !")
								lootforce=lootforce+212+212*palbarb//100
							elif int(lootchoice)==3:
								print ("Vous gagnez une peau de bête épaisse !")
								print (" ")
								print ("+"+str(67+67*palbarb//100)+" defense !")
								print ("+"+str(42+42*palbarb//100)+" force !")
								lootdefense=lootdefense+67+67*palbarb//100
								lootforce=lootforce+42+42*palbarb//100
							elif int(lootchoice)==4:
								print ("Vous gagnez des bottes légères en cuir !")
								print (" ")
								print ("+"+str(67+67*palbarb//100)+" vitesse !")
								print ("+"+str(42+42*palbarb//100)+" force !")
								lootvitesse=lootvitesse+67+67*palbarb//100
								lootforce=lootforce+42+42*palbarb//100
							elif int(lootchoice)==5:
								print ("Vous gagnez la tresse du seigneur barbare  !")
								print (" ")
								print ("+"+str(187+187*palbarb//200)+" PV !")
								print ("+"+str(212+212*palbarb//200)+" force !")
								print ("+"+str(67+67*palbarb//200)+" defense !")
								print ("+"+str(67+67*palbarb//200)+" vitesse !")
								lootpv=lootpv+187+187*palbarb//200
								lootforce=lootforce+212+212*palbarb//200
								lootdefense=lootdefense+67+67*palbarb//200
								lootvitesse=lootvitesse+67+67*palbarb//200
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
								print ("[2] Force")
								print ("[3] Defense")
								print ("[4] Vitesse")
								print ("[5] Les 4")
								leg=input()
								while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
									print (" ")
									leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
									print (" ")
								print (" ")
								print (" ")
								if str(leg)=="1":
									print ("+"+str(250+5*palbarb//2)+" PV !")
									lootpv=lootpv+250+5*palbarb//2
								elif str(leg)=="2":
									print ("+"+str(170+17*palbarb//10)+" force !")
									lootforce=lootforce+170+17*palbarb//10
								elif str(leg)=="3":
									print ("+"+str(90+9*palbarb//10)+" defense !")
									lootdefense=lootdefense+90+9*palbarb//10
								elif str(leg)=="4":
									print ("+"+str(90+9*palbarb//10)+" vitesse !")
									lootvitesse=lootvitesse+90+9*palbarb//10
								elif str(leg)=="5":
									print ("+"+str(180+5*palbarb//4)+" PV !")
									print ("+"+str(80+17*palbarb//20)+" force !")
									print ("+"+str(40+9*palbarb//20)+" defense !")
									print ("+"+str(40+9*palbarb//20)+" vitesse !")
									lootpv=lootpv+180+5*palbarb//4
									lootforce=lootforce+80+17*palbarb//20
									lootdefense=lootdefense+40+9*palbarb//20
									lootvitesse=lootvitesse+40+9*palbarb//20
						if str(choix5)=="4":
							if int(lootchoice)==1:
								print ("Vous gagnez fragment elementaire aquatique !")
								print (" ")
								print ("+"+str(187+187*palelem//100)+" PV !")
								print ("+"+str(22+22*palelem//100)+" defense !")
								lootpv=lootpv+187+187*palelem//100
								lootdefense=lootdefense+22+22*palelem//100
							elif int(lootchoice)==2:
								print ("Vous gagnez fragment elementaire flamboyant!")
								print (" ")
								print ("+"+str(127+127*palelem//100)+" force !")
								print ("+"+str(22+22*palelem//100)+" defense !")
								lootforce=lootforce+127+127*palelem//100
								lootdefense=lootdefense+22+22*palelem//100
							elif int(lootchoice)==3:
								print ("Vous gagnez fragment elementaire rocheux!")
								print (" ")
								print ("+"+str(112+112*palelem//100)+" defense !")
								lootdefense=lootdefense+112+112*palelem//100
							elif int(lootchoice)==4:
								print ("Vous gagnez fragment elementaire venteux!")
								print (" ")
								print ("+"+str(67+67*palelem//100)+" vitesse !")
								print ("+"+str(22+22*palelem//100)+" defense !")
								lootvitesse=lootvitesse+67+67*palelem//100
								lootdefense=lootdefense+22+22*palelem//100
							elif int(lootchoice)==5:
								print ("Vous gagnez fragment elementaire magique!")
								print (" ")
								print ("+"+str(187+187*palelem//200)+" PV !")
								print ("+"+str(127+127*palelem//200)+" force !")
								print ("+"+str(112+112*palelem//200)+" defense !")
								print ("+"+str(67+67*palelem//200)+" vitesse !")
								lootpv=lootpv+187+187*palelem//200
								lootforce=lootforce+127+127*palelem//200
								lootdefense=lootdefense+112+112*palelem//200
								lootvitesse=lootvitesse+67+67*palelem//200
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
								print ("[2] Force")
								print ("[3] Defense")
								print ("[4] Vitesse")
								print ("[5] Les 4")
								leg=input()
								while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
									print (" ")
									leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
									print (" ")
								print (" ")
								print (" ")
								if str(leg)=="1":
									print ("+"+str(250+5*palelem//2)+" PV !")
									lootpv=lootpv+250+5*palelem//2
								elif str(leg)=="2":
									print ("+"+str(170+17*palelem//10)+" force !")
									lootforce=lootforce+170+17*palelem//10
								elif str(leg)=="3":
									print ("+"+str(90+palelem*9//10)+" defense !")
									lootdefense=lootdefense+90+palelem*9//10
								elif str(leg)=="4":
									print ("+"+str(90+palelem*9//10)+" vitesse !")
									lootvitesse=lootvitesse+90+palelem*9//10
								elif str(leg)=="5":
									print ("+"+str(180+5*palelem//4)+" PV !")
									print ("+"+str(80+17*palelem//20)+" force !")
									print ("+"+str(40+9*palelem//20)+" defense !")
									print ("+"+str(40+9*palelem//20)+" vitesse !")
									lootpv=lootpv+180+5*palelem//4
									lootforce=lootforce+80+17*palelem//20
									lootdefense=lootdefense+40+9*palelem//20
									lootvitesse=lootvitesse+40+9*palelem//20
						if str(choix5)=="5":
							if int(lootchoice)==1:
								print ("Vous gagnez une emmeraude !")
								print (" ")
								print ("+"+str(187+187*palfufu//100)+" PV !")
								print ("+"+str(22+22*palfufu//100)+" vitesse !")
								lootpv=lootpv+187+187*palfufu//100
								lootvitesse=lootvitesse+22+22*palfufu//100
							elif int(lootchoice)==2:
								print ("Vous gagnez un rubis !")
								print (" ")
								print ("+"+str(127+127*palfufu//100)+" force !")
								print ("+"+str(22+22*palfufu//100)+" vitesse !")
								lootforce=lootforce+127+127*palfufu//100
								lootvitesse=lootvitesse+22+22*palfufu//100
							elif int(lootchoice)==3:
								print ("Vous gagnez un saphir !")
								print (" ")
								print ("+"+str(67+67*palfufu//100)+" defense !")
								print ("+"+str(22+22*palfufu//100)+" vitesse !")
								lootdefense=lootdefense+67+67*palfufu//100
								lootvitesse=lootvitesse+22+22*palfufu//100
							elif int(lootchoice)==4:
								print ("Vous gagnez une topaze !")
								print (" ")
								print ("+"+str(112+112*palfufu//100)+" vitesse !")
								lootvitesse=lootvitesse+112+112*palfufu//100
							elif int(lootchoice)==5:
								print ("Vous gagnez une obsidienne !")
								print (" ")
								print ("+"+str(187+187*palfufu//200)+" PV !")
								print ("+"+str(127+127*palfufu//200)+" force !")
								print ("+"+str(67+67*palfufu//200)+" defense !")
								print ("+"+str(112+112*palfufu//200)+" vitesse !")
								lootpv=lootpv+187+187*palfufu//200
								lootforce=lootforce+127+127*palfufu//200
								lootdefense=lootdefense+67+67*palfufu//200
								lootvitesse=lootvitesse+112+112*palfufu//200
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
								print ("[2] Force")
								print ("[3] Defense")
								print ("[4] Vitesse")
								print ("[5] Les 4")
								leg=input()
								while str(leg)!="1" and str(leg)!="2" and str(leg)!="3" and str(leg)!="4" and str(leg)!="5":
									print (" ")
									leg=input("Vous devez choisir un chiffre entre '1' et '5' : ")
									print (" ")
								print (" ")
								print (" ")
								if str(leg)=="1":
									print ("+"+str(250+5*palfufu//2)+" PV !")
									lootpv=lootpv+250+5*palfufu//2
								elif str(leg)=="2":
									print ("+"+str(170+17*palfufu//10)+" force !")
									lootforce=lootforce+170+17*palfufu//10
								elif str(leg)=="3":
									print ("+"+str(90+9*palfufu//10)+" defense !")
									lootdefense=lootdefense+90+9*palfufu//10
								elif str(leg)=="4":
									print ("+"+str(90+9*palfufu//10)+" vitesse !")
									lootvitesse=lootvitesse+90+palfufu*9//10
								elif str(leg)=="5":
									print ("+"+str(180+5*palfufu//4)+" PV !")
									print ("+"+str(80+17*palfufu//20)+" force !")
									print ("+"+str(40+9*palfufu//20)+" defense !")
									print ("+"+str(40+9*palfufu//20)+" vitesse !")
									lootpv=lootpv+180+5*palfufu//4
									lootforce=lootforce+80+17*palfufu//20
									lootdefense=lootdefense+40+9*palfufu//20
									lootvitesse=lootvitesse+40+9*palfufu//20
						print (" ")
						print (" ")
						continuer=input("[enter]")
						if str(choix5)=="1":
							paldemo=paldemo+10
						elif str(choix5)=="2":
							palimmo=palimmo+10
						elif str(choix5)=="3":
							palbarb=palbarb+10
						elif str(choix5)=="4":
							palelem=palelem+10
						elif str(choix5)=="5":
							palfufu=palfufu+10
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
						if int(paldemo)==150 or int(palimmo)==150 or int(palbarb)==150 or int(palelem)==150 or int(palfufu)==150:
							wb=1
							print ("Vos exploits attirent des adversaires légendaires...")
							print (" ")
							print ("Préparez-vous, le combat sera rude !")
							print (" ")
					exp=exp+lvlm
					expmax=7*lvl					
					if int(exp)>=int(expmax):
						lvl=lvl+1
						print ("<><><><><><><><>")
						print ("              ")
						print ("   NIVEAU "+str(lvl)+"   ")
						print ("              ")
						print ("<><><><><><><><>")
						print (" ")
						print (" ")
						exp=exp-expmax
						if keltu==1 or keltu==2:
							print ("+135 PV")
							print ("+70 Force")
							print ("+35 Defense")
							print ("+35 Vitesse")
							vieup=vieup+135
							forceup=forceup+70
							defenseup=defenseup+35
							vitesseup=vitesseup+35
							print (" ")
							print (" ")
						if norfend==1 or norfend==2:
							print ("+105 PV")
							print ("+90 Force")
							print ("+35 Defense")
							print ("+35 Vitesse")
							vieup=vieup+105
							forceup=forceup+90
							defenseup=defenseup+35
							vitesseup=vitesseup+35
							print (" ")
							print (" ")
						if exode==1 or exode==2:
							print ("+105 PV")
							print ("+70 Force")
							print ("+45 Defense")
							print ("+35 Vitesse")
							vieup=vieup+105
							forceup=forceup+70
							defenseup=defenseup+45
							vitesseup=vitesseup+35
							print (" ")
							print (" ")
						if azzin==1 or azzin==2:
							print ("+105 PV")
							print ("+70 Force")
							print ("+35 Defense")
							print ("+45 Vitesse")
							vieup=vieup+105
							forceup=forceup+70
							defenseup=defenseup+35
							vitesseup=vitesseup+45
							print (" ")
							print (" ")
						if corrup==1 or corrup==2:
							print ("+120 PV")
							print ("+80 Force")
							print ("+40 Defense")
							print ("+40 Vitesse")
							vieup=vieup+120
							forceup=forceup+80
							defenseup=defenseup+40
							vitesseup=vitesseup+40
							print (" ")
							print (" ")
					print (" ")
					continuer=input("[enter]")
					print (" ")
					print (" ")
			elif int(atbm)>=int(atbmax):
				if int(maladie)!=0:
					print (" ")
					print (" ")
					print (str(nomm)+" perd "+str(maladie)+" PV à cause de la maladie...")
					maladie=0
					print (" ")
					continuer=input("[enter]")
				atbm=atbm-atbmax
				tour=tour+1
				print (" ")
				print (" ")
				print (str(nomm)+" va jouer !")
				print (" ")
				continuer=input("[enter]")
				print (" ")
				print (" ")
				if str(choix1)=="10":
					boss = [1,1,1,2]
					capa=random.choice(boss)
					if str(choix5)=="1":
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
						continuer=input("[enter]")
					elif str(choix5)=="2":
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
							print (str(nomm)+" gagne "+str((15625+12687*lvlm)*10//100)+" PV !")
							viem=viem+(15625+12687*lvlm)*10//100
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
							print (str(nomm)+" perd "+str((15625+12687*lvlm)*20//100)+" PV !")
							viem=viem-(15625+12687*lvlm)*20//100
							print (" ")
							print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="3":
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
							print (str(nomm)+" gagne "+str(forcem*25//100)+" de force !")
							forcem=forcem+forcem*25//100
							print (" ")
							print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="4":
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
						continuer=input("[enter]")
					elif str(choix5)=="5":
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
						continuer=input("[enter]")
				else:
					if str(choix5)=="1":
						degatm=coup_demoniaque(forcem,defense)
						vie=vie-degatm
						print (str(nomm)+" vous frappe avec une puissance obscure...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="2":
						degatm=coup_demoniaque(forcem,defense)
						vie=vie-degatm
						print (str(nomm)+" utilise rituel sanglant...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (str(nomm)+" gagne "+str((12500+10150*lvlm)*8//100)+" PV !")
						viem=viem+(12500+10150*lvlm)*8//100
						print (" ")
						print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="3":
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
						print (str(nom)+" perd "+str(vie*5//100)+" PV !")
						vie=vie-vie*5//100
						print (" ")
						print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="4":
						degatm=coup_demoniaque(forcem,defense)
						vie=vie-degatm
						print (str(nomm)+" vous lance un rocher...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
						continuer=input("[enter]")
					elif str(choix5)=="5":
						degatm=coup_demoniaque(forcem,defense)
						vie=vie-degatm
						print (str(nomm)+" vous poignarde...")
						print (" ")
						print (" ")
						print (str(nom)+" perd "+str(degatm)+" PV !")
						print (" ")
						print (" ")
						continuer=input("[enter]")
				if int(vie)<=0:
					print (" ")
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
	fw.write("\n")
	fw.write(str(wb))
	fw.close()

