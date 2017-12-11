# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:26:32 2017

@author: User
"""

#Lokaverlefni
#23.11.17 - 11.12.17
#Ari Jonsson
# -*- coding: utf-8 -*-

import random

# klassin fyrir dýrin
class Nagdyr:
    def __init__(self, T=0, S=0, A=0):
        self.tegund = T #0=mus, 1=rotta, 2=hamstur
        self.stadsetning = S
        self.afl = A

# fall prentar töflu með stöðu dýranna eftir að öll hafa kastað
def prenta_stada(stada):
    for i in range (1,101):
        print(stada[i], end=" ")
        if i%10==0:
            print ("")

# fall setur stöðu dýranna í töflu
def stada_keppenda(mus, rotta1, rotta2, rotta3, hamstur):
    stada_reita=[]
    for i in range(200):
        stada_reita.append("ttttt") # t þýðir ekkert dýr
        
    # musin sett á sinn stað
    s=mus.stadsetning
    stada_reita[s]="mtttt"
    
    
    # rotta1 settar a sinna stað
    s=rotta1.stadsetning
    stada_reita[s] = stada_reita[s][:1]+"r"+stada_reita[s][2:5]
    
    
    # rotta2 settar a sinna stað
    s=rotta2.stadsetning
    stada_reita[s] = stada_reita[s][:2]+"r"+stada_reita[s][3:5]
    
    
    # rotta3 settar a sinna stað
    s=rotta3.stadsetning
    stada_reita[s] = stada_reita[s][:3]+"r"+stada_reita[s][4:5]
    
    
    # hamstur settur á sinn stað
    s=hamstur.stadsetning
    stada_reita[s] = stada_reita[s][:4]+"h"
    print("")
    print ("músin er á reit nr. ", mus.stadsetning, "í töflunni fyrir neðan:") 
    prenta_stada (stada_reita)



### Her eru gerð byrjunagildi ###
# musin
s=random.randint(1,6)
a=2*random.randint(1,3)
mus=Nagdyr(0,s,a)

# rottur
s=random.randint(1,6)
a=2*random.randint(1,3)
rotta1=Nagdyr(1,s,a)

s=random.randint(1,6)
a=2*random.randint(1,3)
rotta2=Nagdyr(1,s,a)

s=random.randint(1,6)
a=2*random.randint(1,3)
rotta3=Nagdyr(1,s,a)


# hamstur
s=random.randint(1,6)
a=2*random.randint(1,3)
hamstur=Nagdyr(2,s,a)


stada_keppenda(mus, rotta1, rotta2, rotta3, hamstur)

sm=mus.stadsetning
musateljari=1
while sm<=100: 

    #músin kastar fyrst og ber saman við hvar allir eru
    
    #############################################
    ### Regla 1: mús að komast framhjá rottum ###
    #############################################
    #Músin leggur af stað og teningnum er kastað
    musateljari = musateljari + 1
    supphaf=mus.stadsetning
    sendir=supphaf+random.randint(1,6) # fundið út hve langt músin kemst sjálf ef enginn stoppar eða hjálpar
    
    #regla 1: Mús fer af stað, rottur slást við hana og hamstur kastar áfram
    rotta = False
    for si in range(supphaf,sendir+1):
        
        
        
        # athugað hvort það er rotta í staðsetningu si:
        if rotta1.stadsetning==si or rotta2.stadsetning==si or rotta3.stadsetning==si: 
            rotta = True # það er a.m.k. eins rotta í staðsetningu si
            
        #hamstur og mús, ef hamstur kastar þá fer músin yfir rotturnar og þarf ekki að slást annars verður hún að slást við rottur
       
        if hamstur.stadsetning == si : 
                    mus.stadsetning == hamstur.afl+ sendir
                    hamstur.stadsetning=hamstur.stadsetning+hamstur.afl/2
                    print("hamstur kastar mús")
                    break # if hamstur kastar þá fer músin lengra en loopan og þá er loopan stoppuð
        elif rotta:   
            rotta=False # nulla rottuna aftur 
            print("mús lendir á rottu og þarf að slást")
            #Músin og rotta 1
            if rotta1.stadsetning==si:
                if mus.afl>rotta1.afl:      #músin vinnur slaginn og hoppar áfram
                    mus.stadsetning=sendir
                elif mus.afl==rotta1.afl:    # jafntefli og músin er kjurr
                    mus.stadsetning=si
                elif mus.afl<rotta1.afl:                       # rottan vinnur slaginn og músin þarf að bakka um afli hjá rottunni
                    mus.stadsetning=max(si-rotta1.afl,1) # mús fer aldrei neðar en á byrjunarreitin
                    print("rotta1 kastar til baka!")
            #Músin og rotta 2
            if rotta2.stadsetning==si:
                if mus.afl>rotta2.afl:      #músin vinnur slaginn og hoppar áfram
                    mus.stadsetning=sendir
                elif mus.afl==rotta2.afl:    # jafntefli og músin er kjurr
                    mus.stadsetning=si
                elif mus.afl<rotta2.afl:    # rottan vinnur slaginn og músin þarf að bakka um afli hjá rottunni
                    mus.stadsetning=max(si-rotta2.afl,1)
                    print("rotta2 kastar til baka!")
                    
            #músin og rotta3
            if rotta3.stadsetning==si:
                if mus.afl>rotta3.afl:      #músin vinnur slaginn og hoppar áfram
                    mus.stadsetning=sendir
                elif mus.afl==rotta3.afl:    # jafntefli og músin er kjurr
                    mus.stadsetning=si
                elif mus.afl<rotta3.afl:                       # rottan vinnur slaginn og músin þarf að bakka um afli hjá rottunni
                    mus.stadsetning=max(si-rotta3.afl,1)
                    print("rotta3 kastar til baka!")
        else: #ef það er ekki rotta eða hamstur í staðsetningunni þá tekur músin eitt skref áfram
            mus.stadsetning=si
    sm=mus.stadsetning

  
    ###################################    
    ### Regla 2: Rottur hoppa áfram ###
    ###################################
    supphaf=rotta1.stadsetning
    sendir=supphaf+random.randint(1,6) # fundið út hve rottan kemst sjálf
    for si in range(supphaf, sendir+1):
        if mus.stadsetning==si:
                if rotta1.afl>mus.afl:      
                    rotta1.stadsetning=si+1  # rotta1 vinnur slaginn og hoppar áfram um 1, músin kjurr
                elif mus.afl==rotta1.afl:    
                    rotta1.stadsetning=si    # jafntefli og rottan1 er kjurr
                elif rotta1.afl<mus.afl:    
                    mus.stadsetning=si+2     # músin vinnur, slaginn. rottan kjurr músin fer áfram um 2
                elif rotta1.stadsetning == hamstur.stadsetning:
                    rotta1.stadsetning = max(rotta1.stadsetning-1,1)
                    hamstur.stadsetning=hamstur.stadsetning+1
        else:
                rotta1.stadsetning=si
                
    supphaf=rotta2.stadsetning
    sendir=supphaf+random.randint(1,6) # fundið út hve rottan kemst sjálf
    for si in range(supphaf, sendir+1):                
        if mus.stadsetning==si:
                if rotta2.afl>mus.afl:      
                    rotta2.stadsetning=si+1  # rotta1 vinnur slaginn og hoppar áfram um 1, músin kjurr
                elif mus.afl==rotta2.afl:    
                    rotta2.stadsetning=si    # jafntefli og rottan1 er kjurr
                elif rotta2.afl<mus.afl:    
                    mus.stadsetning=si+2     # músin vinnur, slaginn. rottan kjurr músin fer áfram um 2 
                elif rotta2.stadsetning == hamstur.stadsetning:
                    rotta2.stadsetning = max(rotta2.stadsetning-1,1)
                    hamstur.stadsetning=hamstur.stadsetning+1
        else:
                rotta2.stadsetning=si
    
    supphaf=rotta3.stadsetning
    sendir=supphaf+random.randint(1,6) # fundið út hve rottan kemst sjálf
    for si in range(supphaf, sendir+1):                
        if mus.stadsetning==si:
                if rotta3.afl>mus.afl:      
                    rotta3.stadsetning=si+1  # rotta1 vinnur slaginn og hoppar áfram um 1, músin kjurr
                elif mus.afl==rotta3.afl:    
                    rotta3.stadsetning=si    # jafntefli og rottan1 er kjurr
                elif rotta3.afl<mus.afl:    
                    mus.stadsetning=si+2     # músin vinnur, slaginn. rottan kjurr músin fer áfram um 2 
                elif rotta3.stadsetning == hamstur.stadsetning:
                    rotta3.stadsetning = max(rotta3.stadsetning-1,1)
                    hamstur.stadsetning=hamstur.stadsetning+1
        else:
               rotta3.stadsetning=si
    sm=mus.stadsetning
    
    #####################################           
    ### Regla 3: Hamstur hoppar áfram ###
    #####################################
    supphaf=int(hamstur.stadsetning)
    sendir=int(supphaf+random.randint(1,6)) # fundið út hve rottan kemst sjálf
    for si in range(supphaf, sendir+1): 
        hamstur.stadsetning=si               
        if mus.stadsetning==si:
                hamstur.stadsetning=si      
                break # ef hamstur lendir á mús þá fer hann ekki lengra
        elif hamstur.stadsetning==rotta1.stadsetning:
            rotta1.stadsetning = max(rotta1.stadsetning-1,1)
            hamstur.stadsetning=hamstur.stadsetning+1
       
        elif hamstur.stadsetning==rotta2.stadsetning:
            rotta2.stadsetning = max(rotta2.stadsetning-1,1)
            hamstur.stadsetning=hamstur.stadsetning+1

        if hamstur.stadsetning==rotta3.stadsetning:
            rotta3.stadsetning = max(rotta3.stadsetning-1,1)
            hamstur.stadsetning=hamstur.stadsetning+1
    stada_keppenda(mus, rotta1, rotta2, rotta3, hamstur)


print("")
print ("Staða keppendanna í síðustu töflunni:")
print("")
print ("Músin er á reit nr. ", mus.stadsetning)
print("Hún þurfti að kasta teningnum ", musateljari, "sinnum til þess að komast yfir 100")
print ("rotta1 er á reit nr. ", rotta1.stadsetning)
print ("rotta2 er á reit nr. ", rotta2.stadsetning)
print ("rotta3 er á reit nr. ", rotta3.stadsetning)
print ("hamstur er á reit nr. ", hamstur.stadsetning)




