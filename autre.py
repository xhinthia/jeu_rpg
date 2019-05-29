import random
from sorts import *

def tuto_detail(nom):
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
	print ("- la vitesse : vous jouez plus vite")
	continuer=input("[enter]")
	print (" ")
	print ("Vous pouvez jouer une fois que votre jauge d'attaque dépasse les 100%. Cette jauge dépend directement de votre vitesse !)
	print (" ")
	print ("Au plus vous avez de vitesse, au plus votre jauge se remplit vite. Si votre jauge dépasse 100%, vous pouvez jouer et le surplus sera conservé")
	print (" ")
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
	while str(tutoriel)!="1":
		print ("Essayes de taper '1' et d'appuyer sur entrée !")
		print (" ")
		print ("[1] sanguinaire")
		tutoriel=input()
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
	while str(tutoriel)!="2":
		print ("Essayes de taper '2' et d'appuyer sur entrée !")
		print (" ")
		print ("[2] devaster")
		tutoriel=input()
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
	while str(tutoriel)!="3":
		print ("Essayes de taper '3' et d'appuyer sur entrée !")
		print (" ")
		print ("[3] coup de bouclier")
		tutoriel=input()
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
	while str(tutoriel)!="4":
		print ("Essayes de taper '4' et d'appuyer sur entrée !")
		print (" ")
		print ("[4] enchainement")
		tutoriel=input()
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
	while str(tutoriel)!="4":
		print ("Essayes de taper '4' et d'appuyer sur entrée !")
		print (" ")
		print ("[4] enchainement")
		tutoriel=input()
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
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")
