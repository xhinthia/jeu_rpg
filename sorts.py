def degat_pv(force,vieup,lootpv,defensem,degpv,keltu,ritsang):
	print (" ")
	if int(keltu)==2:
		if int(ritsang)<200:
			degat=(110+vieup+lootpv)*12//10-defensem
		elif int(ritsang)>=200 and int(ritsang)<400:
			degat=(110+vieup+lootpv)*13//10-defensem
		elif int(ritsang)>=400 and int(ritsang)<600:
			degat=(110+vieup+lootpv)*14//10-defensem
		elif int(ritsang)>=600:
			degat=(110+vieup+lootpv)*15//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degpv)<200:
			degat=(110+vieup+lootpv)-defensem
		elif int(degpv)>=200 and int(degpv)<400:
			degat=(110+vieup+lootpv)*11//10-defensem
		elif int(degpv)>=400 and int(degpv)<600:
			degat=(110+vieup+lootpv)*12//10-defensem
		elif int(degpv)>=600:
			degat=(110+vieup+lootpv)*13//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_force(force,defensem,degfor,norfend,mourne):
	print (" ")
	if int(norfend)==2:
		if int(mourne)<500:
			degat=force*50//10-defensem
		elif int(mourne)>=500 and int(mourne)<2000:
			degat=force*54//10-defensem
		elif int(mourne)>=2000 and int(mourne)<5000:
			degat=force*58//10-defensem
		elif int(mourne)>=5000:
			degat=force*62//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degfor)<500:
			degat=force*42//10-defensem
		elif int(degfor)>=500 and int(degfor)<2000:
			degat=force*46//10-defensem
		elif int(degfor)>=2000 and int(degfor)<5000:
			degat=force*50//10-defensem
		elif int(degfor)>=5000:
			degat=force*54//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_defense(force,defense,defensem,degdef,exode,war):
	print (" ")
	if int(exode)==2:
		if int(war)<500:
			degat=defense*96//10-defensem
		elif int(war)>=500 and int(war)<2000:
			degat=defense*104//10-defensem
		elif int(war)>=2000 and int(war)<5000:
			degat=defense*112//10-defensem
		elif int(war)>=5000:
			degat=defense*120//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degdef)<500:
			degat=defense*80//10-defensem
		elif int(degdef)>=500 and int(degdef)<2000:
			degat=defense*88//10-defensem
		elif int(degdef)>=2000 and int(degdef)<5000:
			degat=defense*96//10-defensem
		elif int(degdef)>=5000:
			degat=defense*104//10-defensem
		if int(degat)<0:
			degat=0
	return degat
def degat_vitesse(force,vitesse,stackvit,defensem,degvit,azzin,oth):
	print (" ")
	if int(azzin)==2:
		if int(oth)<500:
			degat=vitesse*(92+stackvit)//10-defensem
		elif int(oth)>=500 and int(oth)<2000:
			degat=vitesse*(100+stackvit)//10-defensem
		elif int(oth)>=2000 and int(oth)<5000:
			degat=vitesse*(108+stackvit)//10-defensem
		elif int(oth)>=5000:
			degat=vitesse*(116+stackvit)//10-defensem
		if int(degat)<0:
			degat=0
	else:
		if int(degvit)<500:
			degat=vitesse*(76+stackvit)//10-defensem
		elif int(degvit)>=500 and int(degvit)<2000:
			degat=vitesse*(84+stackvit)//10-defensem
		elif int(degvit)>=2000 and int(degvit)<5000:
			degat=vitesse*(92+stackvit)//10-defensem
		elif int(degvit)>=5000:
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
	if int(ombre)<500:
		degat=(force+vitesse)*10//10
	elif int(ombre)>=500 and int(ombre)<2000:
		degat=(force+vitesse)*11//10
	elif int(ombre)>=2000 and int(ombre)<5000:
		degat=(force+vitesse)*12//10
	elif int(ombre)>=5000:
		degat=(force+vitesse)*13//10
	if int(degat)<0:
		degat=0
	return degat

def pacte_sang(defensem,pacte):
	print (" ")
	if int(pacte)<500:
		degat=defensem
	elif int(pacte)>=500 and int(pacte)<2000:
		degat=defensem*95//100
	elif int(pacte)>=2000 and int(pacte)<5000:
		degat=defensem*88//100
	elif int(pacte)>=5000:
		degat=defensem*78//100
	if int(degat)<0:
		degat=0
	return degat

def transfert(defense,trans):
	print (" ")
	if int(trans)<500:
		buff=defense*3
	elif int(trans)>=500 and int(trans)<2000:
		buff=defense*35//10
	elif int(trans)>=2000 and int(trans)<5000:
		buff=defense*40/10
	elif int(trans)>=5000:
		buff=defense*5
	if int(buff)<0:
		buff=0
	return buff

def absorption(vie,defensem,bloodstack,abso):
	print (" ")
	if i+nt(abso)<500:
		degat=bloodstack*100*bloodstack-defensem
	elif int(abso)>=500 and int(abso)<2000:
		degat=bloodstack*102*bloodstack-defensem
	elif int(abso)>=2000 and int(abso)<5000:
		degat=bloodstack*104*bloodstack-defensem
	elif int(abso)>=5000:
		degat=bloodstack*107*bloodstack-defensem
	if int(degat)<0:
		degat=0
	return degat

def poigne_mort(forcem,poigne):
	print (" ")
	if int(poigne)<500:
		debuff=forcem//10
	elif int(poigne)>=500 and int(poigne)<2000:
		debuff=forcem//9
	elif int(poigne)>=2000 and int(poigne)<5000:
		debuff=forcem//8
	elif int(poigne)>=5000:
		debuff=forcem//6
	if int(debuff)<0:
		debuff=0
	return debuff

def renforcement(force,renfo):
	print (" ")
	if int(renfo)<500:
		buff=force//6
	elif int(renfo)>=500 and int(renfo)<2000:
		buff=force//4
	elif int(renfo)>=2000 and int(renfo)<5000:
		buff=force//2
	elif int(renfo)>=5000:
		buff=force
	if int(buff)<0:
		buff=0
	return buff

def aneantissement(force,forcem,defensem,anean):
	print (" ")
	if int(anean)<500:
		degat=force*9//5-defensem
	elif int(anean)>=500 and int(anean)<2000:
		degat=force*2-defensem
	elif int(anean)>=2000 and int(anean)<5000:
		degat=force*215//100-defensem
	elif int(anean)>=5000:
		degat=force*235//100-defensem
	if int(degat)<0:
		degat=0
	return degat	

def onde_choc(defense,defensem,onde):
	print (" ")
	if int(onde)<500:
		degat=defense-defensem
	elif int(onde)>=500 and int(onde)<2000:
		degat=defense*115//100-defensem
	elif int(onde)>=2000 and int(onde)<5000:
		degat=defense*13//10-defensem
	elif int(onde)>=5000:
		degat=defense*3//2-defensem
	if int(degat)<0:
		degat=0
	return degat
 
def vengeance(degveng,veng):
	print (" ")
	if int(veng)<500:
		degat=degveng//4
	elif int(veng)>=500 and int(veng)<2000:
		degat=degveng*2//7
	elif int(veng)>=2000 and int(veng)<5000:
		degat=degveng*2//5
	elif int(veng)>=5000:
		degat=degveng*10//15
	if int(degat)<0:
		degat=0
	return degat

def dernier_souffle(defense,souffle):
	print (" ")
	if int(souffle)<500:
		buff=defense*2
	elif int(souffle)>=500 and int(souffle)<2000:
		buff=defense*21//10
	elif int(souffle)>=2000 and int(souffle)<5000:
		buff=defense*225//100
	elif int(souffle)>=5000:
		buff=defense*25//10
	if int(buff)<0:
		buff=0
	return buff

def serie_meurtriere(stackvit,defensem,serie):
	print (" ")
	if int(serie)<500:
		degat=(stackvit*stackvit*stackvit)
	elif int(serie)>=500 and int(serie)<2000:
		degat=(stackvit*stackvit*stackvit)*11//10
	elif int(serie)>=2000 and int(serie)<5000:
		degat=(stackvit*stackvit*stackvit)*12//10
	elif int(serie)>=5000:
		degat=(stackvit*stackvit*stackvit)*135//100
	if int(serie)<0:
		degat=0
	return degat

def drainage(force,drain):
	print (" ")
	if int(drain)<500:
		degat=force//2
	elif int(drain)>=500 and int(drain)<2000:
		degat=force*4//7
	elif int(drain)>=2000 and int(drain)<5000:
		degat=force*2//3
	elif int(drain)>=5000:
		degat=force*4//5
	if int(serie)<0:
		degat=0
	return degat

def feu_ame(magie,ame,lvlm,feu):
	print (" ")
	if int(feu)<500:
		degat=force*ame//lvlm
	elif int(feu)>=500 and int(feu)<2000:
		degat=(force*5//4)*ame//lvlm
	elif int(feu)>=2000 and int(feu)<5000:
		degat=(force*3//2)*ame//lvlm
	elif int(feu)>=5000:
		degat=force*2*ame//lvlm
	if int(serie)<0:
		degat=0
	return degat
