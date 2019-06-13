import random

def degat_pv(force,defensem,degpv,keltu,ritsang):
	print (" ")
	if int(keltu)==2:
		if int(ritsang)<200:
			degat=force*350//100-defensem
		elif int(ritsang)>=200 and int(ritsang)<400:
			degat=force*360//100-defensem
		elif int(ritsang)>=400 and int(ritsang)<600:
			degat=force*370//100-defensem
		elif int(ritsang)>=600:
			degat=force*380//100-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degpv)<200:
			degat=force*345//100-defensem
		elif int(degpv)>=200 and int(degpv)<400:
			degat=force*355//100-defensem
		elif int(degpv)>=400 and int(degpv)<600:
			degat=force*365//100-defensem
		elif int(degpv)>=600:
			degat=force*375//100-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_force(force,defensem,degfor,norfend,mourne):
	print (" ")
	if int(norfend)==2:
		if int(mourne)<200:
			degat=force*405//100-defensem
		elif int(mourne)>=200 and int(mourne)<400:
			degat=force*415//100-defensem
		elif int(mourne)>=400 and int(mourne)<600:
			degat=force*425//100-defensem
		elif int(mourne)>=600:
			degat=force*435//100-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degfor)<200:
			degat=force*400//100-defensem
		elif int(degfor)>=200 and int(degfor)<400:
			degat=force*410//100-defensem
		elif int(degfor)>=400 and int(degfor)<600:
			degat=force*420//100-defensem
		elif int(degfor)>=600:
			degat=force*430//100-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_defense(force,defensem,degdef,exode,war):
	print (" ")
	if int(exode)==2:
		if int(war)<200:
			degat=force*345//100-defensem
		elif int(war)>=200 and int(war)<400:
			degat=force*355//100-defensem
		elif int(war)>=400 and int(war)<600:
			degat=force*365//100-defensem
		elif int(war)>=600:
			degat=force*375//100-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degdef)<200:
			degat=force*340//100-defensem
		elif int(degdef)>=200 and int(degdef)<400:
			degat=force*350//100-defensem
		elif int(degdef)>=400 and int(degdef)<600:
			degat=force*360//100-defensem
		elif int(degdef)>=600:
			degat=force*370//100-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_vitesse(force,stackvit,defensem,degvit,azzin,oth):
	print (" ")
	if int(azzin)==2:
		if int(oth)<200:
			degat=force*(320+22*stackvit)//100-defensem
		elif int(oth)>=200 and int(oth)<400:
			degat=force*(320+27*stackvit)//100-defensem
		elif int(oth)>=400 and int(oth)<600:
			degat=force*(320+32*stackvit)//100-defensem
		elif int(oth)>=600:
			degat=force*(320+35*stackvit)//100-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degvit)<200:
			degat=force*(330+20*stackvit)//100-defensem
		elif int(degvit)>=200 and int(degvit)<400:
			degat=force*(340+20*stackvit)//100-defensem
		elif int(degvit)>=400 and int(degvit)<600:
			degat=force*(350+20*stackvit)//100-defensem
		elif int(degvit)>=600:
			degat=force*(360+20*stackvit)//100-defensem
		if int(degat)<0:
			degat=0
	return degat
def coup_demoniaque(forcem,defense):
	degatm=forcem*200//100-defense
	if int(degatm)<0:
		degatm=0
	return degatm
def frappe_ombre(forcem,defense):
	degatm=forcem*220//100-defense
	if int(degatm)<0:
		degatm=0
	return degatm
def destru_primo(forcem,defense):
	degatm=forcem*300//100-defense
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

def ombreflamme(force,ombre):
	if int(ombre)<200:
		degat=force*350//100
	elif int(ombre)>=200 and int(ombre)<400:
		degat=force*360//100
	elif int(ombre)>=400 and int(ombre)<600:
		degat=force*370//100
	elif int(ombre)>=600:
		degat=force*380//100
	if int(degat)<0:
		degat=0
	return degat

def pacte_sang(defensem,pacte):
	print (" ")
	if int(pacte)<200:
		degat=defensem
	elif int(pacte)>=200 and int(pacte)<400:
		degat=defensem*95//100
	elif int(pacte)>=400 and int(pacte)<600:
		degat=defensem*90//100
	elif int(pacte)>=600:
		degat=defensem*85//100
	if int(degat)<0:
		degat=0
	return degat

def transfert(defense,trans):
	print (" ")
	if int(trans)<200:
		buff=defense*200//100
	elif int(trans)>=200 and int(trans)<400:
		buff=defense*220//100
	elif int(trans)>=400 and int(trans)<600:
		buff=defense*240//100
	elif int(trans)>=600:
		buff=defense*260//100
	if int(buff)<0:
		buff=0
	return buff

def absorption(force,defensem,bloodstack,abso):
	print (" ")
	if int(abso)<200:
		degat=force*(300+25*bloodstack)//100-defensem
	elif int(abso)>=200 and int(abso)<400:
		degat=force*(300+30*bloodstack)//100-defensem
	elif int(abso)>=400 and int(abso)<600:
		degat=force*(300+35*bloodstack)//100-defensem
	elif int(abso)>=600:
		degat=force*(300+40*bloodstack)//100-defensem
	return degat

def poigne_mort(forcem,poigne):
	print (" ")
	if int(poigne)<200:
		debuff=forcem*10//100
	elif int(poigne)>=200 and int(poigne)<400:
		debuff=forcem*12//100
	elif int(poigne)>=400 and int(poigne)<600:
		debuff=forcem*14//100
	elif int(poigne)>=600:
		debuff=forcem*16//100
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

def aneantissement(force,defensem,anean):
	print (" ")
	if int(anean)<200:
		degat=force*500//100-defensem
	elif int(anean)>=200 and int(anean)<400:
		degat=force*515//100-defensem
	elif int(anean)>=400 and int(anean)<600:
		degat=force*530//100-defensem
	elif int(anean)>=600:
		degat=force*545//100-defensem
	if int(degat)<0:
		degat=0
	return degat	

def onde_choc(force,defensem,onde):
	print (" ")
	if int(onde)<200:
		degat=force*300//100-defensem
	elif int(onde)>=200 and int(onde)<400:
		degat=force*310//100-defensem
	elif int(onde)>=400 and int(onde)<600:
		degat=force*320//10-defensem
	elif int(onde)>=600:
		degat=force*330//100-defensem
	if int(degat)<0:
		degat=0
	return degat
 
def vengeance(degveng,veng):
	print (" ")
	if int(veng)<200:
		degat=degveng*30//100
	elif int(veng)>=200 and int(veng)<400:
		degat=degveng*32//100
	elif int(veng)>=400 and int(veng)<600:
		degat=degveng*35//100
	elif int(veng)>=600:
		degat=degveng*37//100
	if int(degat)<0:
		degat=0
	return degat

def mur_protecteur(defense,souffle):
	print (" ")
	if int(souffle)<200:
		buff=defense*150//100
	elif int(souffle)>=200 and int(souffle)<400:
		buff=defense*160//100
	elif int(souffle)>=400 and int(souffle)<600:
		buff=defense*170//100
	elif int(souffle)>=600:
		buff=defense*180//100
	return buff

def serie_meurtriere(force,stackvit,defensem,serie):
	print (" ")
	if int(serie)<200:
		degat=force*(150+40*stackvit)//100-defensem
	elif int(serie)>=200 and int(serie)<400:
		degat=force*(150+45*stackvit)//100-defensem
	elif int(serie)>=400 and int(serie)<600:
		degat=force*(150+50*stackvit)//100-defensem
	elif int(serie)>=600:
		degat=force*(150+55*stackvit)//100-defensem
	if int(serie)<0:
		degat=0
	return degat

def drainage(force,drain):
	print (" ")
	if int(drain)<200:
		degat=force*250//100
	elif int(drain)>=200 and int(drain)<400:
		degat=force*260//100
	elif int(drain)>=400 and int(drain)<600:
		degat=force*270//100
	elif int(drain)>=600:
		degat=force*280//100
	return degat

def feu_ame(force,feu):
	print (" ")
	if int(feu)<200:
		degat=force*450//100
	elif int(feu)>=200 and int(feu)<400:
		degat=force*465//100
	elif int(feu)>=400 and int(feu)<600:
		degat=force*480//100
	elif int(feu)>=600:
		degat=force*500//100
	return degat
