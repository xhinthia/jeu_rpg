import random

def degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang):
	print (" ")
	if int(keltu)==2:
		if int(ritsang)<200:
			degat=(110+vieup+lootpv)*4//10-defensem
		elif int(ritsang)>=200 and int(ritsang)<400:
			degat=(110+vieup+lootpv)*5//10-defensem
		elif int(ritsang)>=400 and int(ritsang)<600:
			degat=(110+vieup+lootpv)*6//10-defensem
		elif int(ritsang)>=600:
			degat=(110+vieup+lootpv)*7//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degpv)<200:
			degat=(110+vieup+lootpv)*3//10-defensem
		elif int(degpv)>=200 and int(degpv)<400:
			degat=(110+vieup+lootpv)*4//10-defensem
		elif int(degpv)>=400 and int(degpv)<600:
			degat=(110+vieup+lootpv)*5//10-defensem
		elif int(degpv)>=600:
			degat=(110+vieup+lootpv)*6//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_force(force,defensem,degfor,norfend,mourne):
	print (" ")
	if int(norfend)==2:
		if int(mourne)<200:
			degat=force*40//10-defensem
		elif int(mourne)>=200 and int(mourne)<400:
			degat=force*44//10-defensem
		elif int(mourne)>=400 and int(mourne)<600:
			degat=force*48//10-defensem
		elif int(mourne)>=600:
			degat=force*52//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degfor)<200:
			degat=force*42//10-defensem
		elif int(degfor)>=200 and int(degfor)<400:
			degat=force*46//10-defensem
		elif int(degfor)>=400 and int(degfor)<600:
			degat=force*50//10-defensem
		elif int(degfor)>=600:
			degat=force*54//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_defense(force,defense,defensem,degdef,exode,war):
	print (" ")
	if int(exode)==2:
		if int(war)<200:
			degat=defense*88//10-defensem
		elif int(war)>=200 and int(war)<400:
			degat=defense*96//10-defensem
		elif int(war)>=400 and int(war)<600:
			degat=defense*104//10-defensem
		elif int(war)>=600:
			degat=defense*112//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degdef)<200:
			degat=defense*80//10-defensem
		elif int(degdef)>=200 and int(degdef)<400:
			degat=defense*88//10-defensem
		elif int(degdef)>=400 and int(degdef)<600:
			degat=defense*96//10-defensem
		elif int(degdef)>=600:
			degat=defense*104//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth):
	print (" ")
	if int(azzin)==2:
		if int(oth)<200:
			degat=vitesse*(84+stackvit)//10-defensem
		elif int(oth)>=200 and int(oth)<400:
			degat=vitesse*(92+stackvit)//10-defensem
		elif int(oth)>=400 and int(oth)<600:
			degat=vitesse*(100+stackvit)//10-defensem
		elif int(oth)>=600:
			degat=vitesse*(108+stackvit)//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degvit)<200:
			degat=vitesse*(76+stackvit)//10-defensem
		elif int(degvit)>=200 and int(degvit)<400:
			degat=vitesse*(84+stackvit)//10-defensem
		elif int(degvit)>=400 and int(degvit)<600:
			degat=vitesse*(92+stackvit)//10-defensem
		elif int(degvit)>=600:
			degat=vitesse*(100+stackvit)//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def coup_demoniaque(forcem,defense):
	degatm=forcem-defense
	if int(degatm)<0:
		degatm=0
	return degatm
def frappe_ombre(forcem,defense):
	degatm=forcem*3//2-defense
	if int(degatm)<0:
		degatm=0
	return degatm
def destru_primo(forcem,defense):
	degatm=forcem*5//2-defense
	if int(degatm)<0:
		degatm=0
	return degatm

def attaque_boss(viem,forcem,defense,choix5):
	if int(choix5)==2:
		degatm=viem//70-defense
	elif int(choix5)==3:
		degatm=forcem*2-defense
	#elif int(choix5)==4:
	#	instabilité up carac au pif
	elif int(choix5)==5:
		degatm=forcem-defense
	if int(degatm)<0:
		degatm=0

def ulti_boss(viem,forcem,defense,choix5):
	if int(choix5)==2:
		degatm=viem//30-defense
	#elif int(choix5)==3:
	#	brutalité up force
	elif int(choix5)==4:
		degatm=forcem*2-defense
	elif int(choix5)==5:
		degatm=forcem*4-defense
	if int(degatm)<0:
		degatm=0

def instabilite_elem(forcem,defensem,vitessem):
	liste = [1,2,3]
	a=random.choice(liste)
	if int(a)==1:
		buff=forcem//12
	elif int(a)==2:
		buff=defensem//15
	elif int(a)==3:
		buff=vitessem//5
	return buff



def rituel_sanglant(viem,defense):
	degatm=viem//100-defense
	if int(degatm)<0:
		degatm=0
	return degatm

def ombreflamme(force,vitesse,ombre):
	if int(ombre)<200:
		degat=(force+vitesse)*10//10
	elif int(ombre)>=200 and int(ombre)<400:
		degat=(force+vitesse)*11//10
	elif int(ombre)>=400 and int(ombre)<600:
		degat=(force+vitesse)*12//10
	elif int(ombre)>=600:
		degat=(force+vitesse)*13//10
	if int(degat)<0:
		degat=0
	return degat

def pacte_sang(defensem,pacte):
	print (" ")
	if int(pacte)<200:
		degat=defensem
	elif int(pacte)>=200 and int(pacte)<400:
		degat=defensem*9//10
	elif int(pacte)>=400 and int(pacte)<600:
		degat=defensem*8//10
	elif int(pacte)>=600:
		degat=defensem*7//10
	if int(degat)<0:
		degat=0
	return degat

def transfert(defense,trans):
	print (" ")
	if int(trans)<200:
		buff=defense*10
	elif int(trans)>=200 and int(trans)<400:
		buff=defense*11
	elif int(trans)>=400 and int(trans)<600:
		buff=defense*12
	elif int(trans)>=600:
		buff=defense*13
	if int(buff)<0:
		buff=0
	return buff

def absorption(lvl,vie,defensem,bloodstack,abso):
	print (" ")
	imax=(bloodstack*lvl)//10
	liste = [47,49,51,53,55]
	impec= [1,2,3,4,5,6,7,8,9]	
	i=0
	degat=0
	while int(i)<int(imax):
		a=random.choice(liste)
		b=random.choice(impec)
		if int(b)==1:
			print ("-"+str(a)+" PV !")
		elif int(b)==2:
			print ("	-"+str(a)+" PV !")
		elif int(b)==3:
			print ("		-"+str(a)+" PV !")
		elif int(b)==4:
			print ("			-"+str(a)+" PV !")
		elif int(b)==5:
			print ("				-"+str(a)+" PV !")
		elif int(b)==6:
			print ("					-"+str(a)+" PV !")
		elif int(b)==7:
			print ("						-"+str(a)+" PV !")
		elif int(b)==8:
			print ("							-"+str(a)+" PV !")
		elif int(b)==9:
			print ("								-"+str(a)+" PV !")
		i=i+1
		degat=degat+a
	return degat

def poigne_mort(forcem,poigne):
	print (" ")
	if int(poigne)<200:
		debuff=forcem//10
	elif int(poigne)>=200 and int(poigne)<400:
		debuff=forcem//9
	elif int(poigne)>=400 and int(poigne)<600:
		debuff=forcem//8
	elif int(poigne)>=600:
		debuff=forcem//6
	if int(debuff)<0:
		debuff=0
	return debuff

def renforcement(force,renfo):
	print (" ")
	if int(renfo)<200:
		buff=force//6
	elif int(renfo)>=200 and int(renfo)<400:
		buff=force//4
	elif int(renfo)>=400 and int(renfo)<600:
		buff=force//2
	elif int(renfo)>=600:
		buff=force
	if int(buff)<0:
		buff=0
	return buff

def aneantissement(force,forcem,defensem,anean):
	print (" ")
	if int(anean)<200:
		degat=force*200//40-defensem
	elif int(anean)>=200 and int(anean)<400:
		degat=force*210//40-defensem
	elif int(anean)>=400 and int(anean)<600:
		degat=force*220//40-defensem
	elif int(anean)>=600:
		degat=force*230//40-defensem
	if int(degat)<0:
		degat=0
	return degat	

def onde_choc(defense,defensem,onde):
	print (" ")
	if int(onde)<200:
		degat=defense-defensem
	elif int(onde)>=200 and int(onde)<400:
		degat=defense*115//100-defensem
	elif int(onde)>=400 and int(onde)<600:
		degat=defense*13//10-defensem
	elif int(onde)>=600:
		degat=defense*3//2-defensem
	if int(degat)<0:
		degat=0
	return degat
 
def vengeance(degveng,veng):
	print (" ")
	if int(veng)<200:
		degat=degveng//4
	elif int(veng)>=200 and int(veng)<400:
		degat=degveng*2//7
	elif int(veng)>=400 and int(veng)<600:
		degat=degveng*2//5
	elif int(veng)>=600:
		degat=degveng*10//15
	if int(degat)<0:
		degat=0
	return degat

def dernier_souffle(defense,souffle):
	print (" ")
	if int(souffle)<200:
		buff=defense*2
	elif int(souffle)>=200 and int(souffle)<400:
		buff=defense*21//10
	elif int(souffle)>=400 and int(souffle)<600:
		buff=defense*23//10
	elif int(souffle)>=600:
		buff=defense*25//10
	if int(buff)<0:
		buff=0
	return buff

def serie_meurtriere(stackvit,defensem,serie):
	print (" ")
	if int(serie)<200:
		degat=(stackvit*stackvit*stackvit)
	elif int(serie)>=200 and int(serie)<400:
		degat=(stackvit*stackvit*stackvit)*11//10
	elif int(serie)>=400 and int(serie)<600:
		degat=(stackvit*stackvit*stackvit)*12//10
	elif int(serie)>=600:
		degat=(stackvit*stackvit*stackvit)*13//10
	if int(serie)<0:
		degat=0
	return degat

def drainage(force,drain):
	print (" ")
	if int(drain)<200:
		degat=force//2
	elif int(drain)>=200 and int(drain)<400:
		degat=force*4//7
	elif int(drain)>=400 and int(drain)<600:
		degat=force*2//3
	elif int(drain)>=600:
		degat=force*4//5
	if int(serie)<0:
		degat=0
	return degat

def feu_ame(magie,ame,lvlm,feu):
	print (" ")
	if int(feu)<200:
		degat=force*ame//lvlm
	elif int(feu)>=200 and int(feu)<400:
		degat=(force*5//4)*ame//lvlm
	elif int(feu)>=400 and int(feu)<600:
		degat=(force*3//2)*ame//lvlm
	elif int(feu)>=600:
		degat=force*2*ame//lvlm
	if int(serie)<0:
		degat=0
	return degat
