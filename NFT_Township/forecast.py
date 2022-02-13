# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:07:51 2022

@author: Puckster
"""

import random
import numpy as np
import matplotlib as plt


global CardList 
global EmpirePopulation
global NameArray
global lengthOfArray
global UpgradeArray
global wallets
global startingTownsPeople
global cardIndex


EmpirePopulation = []

TownpersonCardList = []
ShopOwnerCardList = []
TradesmanCardList = []
GuildLeaderCardList = []
VillageElderCardList = []
NobleCardList = []
KnightCardList = []
BaronCardList = []
ViscountCardList = []
EarlCardList = []
MarquessCardList = []
DukeCardList = []
ArchdukeCardList = []
PrincessCardList = []
PrinceCardList = []
QueenCardList = []
KingCardList = []



startingTownsPeople = 5000

startingTPAddition = 0.001
TPaddition = 0.5

Upgrade1 = 0.01
Upgrade2 = 0.001
Upgrade3 = 0.0001
Upgrade4 = 0.00001
Upgrade5 = 0.000001

InitialUpgrade1 = .001
InitialUpgrade2 = .0001
InitialUpgrade3 = .00001
InitialUpgrade4 = .000001
InitialUpgrade5 = .0000001

UpgradeArray = []
IncreaseInTownsPeoplePerDay = 0.1;

cardIndex = 0


CardList = []



TownPopulation_Array = np.array([16])

    

class Character:
    def __init__(self,_type,_id,_owner):
        self.type = _type
        self.ID = _id
        self.owner = _owner
    
def CreateCard(_type, _id, _owner):
    
    
    newCard = Character(_type, _id, _owner)
    temp = "Type: " + str(newCard.type) + " \nID: " + str(newCard.ID) + "\nOwner: " + newCard.owner
    #print(temp)
    
    return newCard
    
def ClearCardList():
    # Cleared cardlist
    CardList = []
    
 
def InitFirstSetOfCards():
    global cardIndex
    global TownpersonCardList
    
    
    x = 0
    i = 0
    Owners = ["me", "Jake", "Myles", "Jeremy", "Rob", "CJ", "Kris", "Dakota"]
    
    for x in range(startingTownsPeople):
        if (i > len(Owners)-1):
            i = 0
        
        newCard =  CreateCard(0,cardIndex, Owners[i])

        TownpersonCardList.append(newCard)
        cardIndex = cardIndex + 1
        i = i + 1
    
    
    
    
    return TownpersonCardList





def createPopulationList():
    global EmpirePopulation
    
    EmpirePopulation = [TownpersonCardList,ShopOwnerCardList,TradesmanCardList,GuildLeaderCardList,
                        VillageElderCardList, NobleCardList, KnightCardList, BaronCardList, ViscountCardList,
                        EarlCardList, MarquessCardList, DukeCardList, ArchdukeCardList, PrincessCardList,
                        PrinceCardList, QueenCardList, KingCardList]






def Simulation_withUsers():
    global EmpirePopulation
    
    Working_EmpirePopulation = EmpirePopulation
    
    totalNumOfClasses = len(Working_EmpirePopulation)
    
    x = 0
    
    for x in range(totalNumOfClasses-1,-1,-1):
    #for x in range(totalNumOfClasses):
        # start of Class and Reading individual personell
        selectedClass = Working_EmpirePopulation[x]
        if (len(selectedClass) > 0):
            y = 0
            for y in range(len(selectedClass)):
                checkForUnitUpgrade(selectedClass[y])
                #print(selectedClass[y].owner)
    





def checkForUnitUpgrade(currentCard):
    global UpgradeArray
    global EmpirePopulation
    global cardIndex
    
    upgradeamt = UpgradeArray[currentCard.type][currentCard.type+1]    
    randAmount1 = int(1/ upgradeamt)    
    # print("rand amount1: " + str(randAmount1))
    
    upgradeamt = UpgradeArray[currentCard.type][currentCard.type+2]    
    randAmount2 = int(1/ upgradeamt)    
    # print("rand amount2: " + str(randAmount2))
    
    if (random.randint(1, randAmount1) == 1):
        NextPopClass = EmpirePopulation[currentCard.type +1]
        newCard = CreateCard(currentCard.type +1,cardIndex,currentCard.owner)
        cardIndex = cardIndex + 1
        temp = " New Card Created:\nType: " + str(newCard.type) + "\nIndex: " + str(newCard.ID) + "\nOwner: " + newCard.owner
        #print(temp)
        
        NextPopClass.append(newCard)
        EmpirePopulation[currentCard.type +1] = NextPopClass
    
    elif (random.randint(1, randAmount2) == 1):
      NextPopClass = EmpirePopulation[currentCard.type +2]
      newCard = CreateCard(currentCard.type +2,cardIndex,currentCard.owner)
      cardIndex = cardIndex + 1
      temp = " New Card Created:\nType: " + str(newCard.type) + "\nIndex: " + str(newCard.ID) + "\nOwner: " + newCard.owner
      #print(temp)
      
      NextPopClass.append(newCard)
      EmpirePopulation[currentCard.type +2] = NextPopClass  
    
    if (currentCard.type > 0):   
        TPRAmount = UpgradeArray[currentCard.type][0]
        randTPAmound = int(1/TPRAmount)
        if (random.randint(1, randTPAmound) == 1):
            newCard = CreateCard(0, cardIndex, currentCard.owner)
            cardIndex = cardIndex + 1
            TPPopClass = EmpirePopulation[0]
            TPPopClass.append(newCard)
            EmpirePopulation[0] = TPPopClass  

def init_function():
    
    NameArray = ["Townsperson","Shop owner","Tradesman","Guild Leader","Village Elder",
                "Noble", "Knight","Baron", "Viscount", "Earl", "Marquess", "Duke",
                "Archduke", "Princess","Prince", "Queen", "King"]
      
    lengthOfArray = len(NameArray)
    
    # EmpirePopulation = [0 for i in range(lengthOfArray)] 
    # EmpirePopulation[0] = startingTownsPeople
    # print(EmpirePopulation)
    
    
    global UpgradeArray
    
    UpgradeArray = []
    
    UpgradeArray = [[0 for i in range(lengthOfArray)] for j in range(lengthOfArray)]
          
    x = 0
    y = 0
      
    for y in range(lengthOfArray):
      if (y != 0):        
          for x in range(lengthOfArray):
              if (x == 0):
                  if (y == 1):
                      UpgradeArray[y][x] = startingTPAddition
                  else:
                      UpgradeArray[y][x] = UpgradeArray[y-1][x] /TPaddition
                    
                      
              if (x == y+1):
                  UpgradeArray[y][x] = UpgradeArray[y-1][x-1] * Upgrade1
              elif (x == y + 2):
                  UpgradeArray[y][x] = UpgradeArray[y-1][x-1] * Upgrade2
              elif (x == y + 3):
                  UpgradeArray[y][x] = UpgradeArray[y-1][x-1] * Upgrade3
              elif (x == y + 4):
                  UpgradeArray[y][x] = UpgradeArray[y-1][x-1] * Upgrade4
              elif (x == y + 5):
                  UpgradeArray[y][x] = UpgradeArray[y-1][x-1] * Upgrade5
      else:       
          for x in range(lengthOfArray):
              if (x == y+1):
                  UpgradeArray[y][x] = InitialUpgrade1  
              if (x == y + 2):
                  UpgradeArray[y][x] = InitialUpgrade2  
              if (x == y + 3):
                  UpgradeArray[y][x] = InitialUpgrade3                                        
              if (x == y + 4):
                  UpgradeArray[y][x] = InitialUpgrade4  
              if (x == y + 5):
                  UpgradeArray[y][x] = InitialUpgrade5  

    
          
    

cardIndex = 0
ClearCardList()
TownpersonCardList = InitFirstSetOfCards()

print("CardIndex: " + str(cardIndex))

init_function()
    
createPopulationList()
# GroupCards = EmpirePopulation[0]
# print(str(GroupCards[2].owner))

years = 5
dayInYear = 365

p = 0
for p in range(int(years * dayInYear)):
    print("Day: " + str(p) + " out of " + str(int(years * dayInYear)))
    Simulation_withUsers()



lenTP = len(EmpirePopulation[0])
lenSO = len(EmpirePopulation[1])
lenTR = len(EmpirePopulation[2])
lenGL = len(EmpirePopulation[3])
lenVE = len(EmpirePopulation[4])
lenNob = len(EmpirePopulation[5])
lenKni = len(EmpirePopulation[6])
lenBar = len(EmpirePopulation[7])
lenVis = len(EmpirePopulation[8])
lenEarl = len(EmpirePopulation[9])
lenMar = len(EmpirePopulation[10])
lenDuke = len(EmpirePopulation[11])
lenArkD = len(EmpirePopulation[12])
lenPrincess = len(EmpirePopulation[13])
lenPrince = len(EmpirePopulation[14])
lenQueen = len(EmpirePopulation[15])
lenKing = len(EmpirePopulation[16])

print ("TP: " + str(lenTP))
print ("SO: " + str(lenSO))
print ("TR: " + str(lenTR))
print ("GL: " + str(lenGL))
print ("VE: " + str(lenVE))
print ("Nob: " + str(lenNob))
print ("Knight: " + str(lenKni))
print ("Bar: " + str(lenBar))
print ("Vis: " + str(lenVis))
print ("Earl: " + str(lenEarl))
print ("Mar: " + str(lenMar))
print ("Duke: " + str(lenDuke))
print ("ArkDuke: " + str(lenArkD))
print ("Princess: " + str(lenPrincess))
print ("Prince: " + str(lenPrince))
print ("Queen: " + str(lenQueen))
print ("King: " + str(lenKing))





# PulledCardList = PopulationList[0]
# print (str(PulledCardList[0]))

MeList = []
for y in range(15):
    PopList = EmpirePopulation[y]
    MeList = [p for p in PopList if p.owner == "me"]    
    print("Me List Count: " + str(len(MeList)))
    
    
    







# print (EmpirePopulation)

# CreateCard("Townsperson", 1, "me")




# years = 5
# daysInYear = 365

# numofIterations = years * daysInYear

# for numofIterations in range(numofIterations,-1,-1):
#     print("Running Day: "  + str(numofIterations))
#     simulation()
#     print (EmpirePopulation)

# np.sum(EmpirePopulation)
# print (str(np.sum(EmpirePopulation)))


# print (EmpirePopulation)














# def simulation():
#     y = 16
    
    
#     for y in range(16,-1,-1):
#         # print (str(y))
#         # check if update occurs    
#         if (EmpirePopulation[y] > 0):
#             numofPeople = EmpirePopulation[y]
#             # print(numofPeople)
#             for p in range(numofPeople):
#                 upgradeNum = int(1/UpgradeArray[y][y+1])
#                 randomNumber = random.randint(1, upgradeNum)
#                 if (randomNumber == 1):
#                     # print("Got 1")
#                     # EmpirePopulation[y] = EmpirePopulation[y] - 1
#                     EmpirePopulation[y + 1] = EmpirePopulation[y + 1] + 1
#                     numofPeople = EmpirePopulation[y]
                
#             for p in range(numofPeople):
#                         upgradeNum = int(1/UpgradeArray[y][y+2])
#                         randomNumber = random.randint(1, upgradeNum)
#                         if (randomNumber == 1):
#                             # print("Got 2")
#                             # EmpirePopulation[y] = EmpirePopulation[y] - 1
#                             EmpirePopulation[y + 2] = EmpirePopulation[y + 2] + 1
#                             numofPeople = EmpirePopulation[y]        
#         if (y > 0):
#             if (EmpirePopulation[y] > 0):
#                 numofPeople = EmpirePopulation[y]
#                 for p in range(numofPeople):
#                     upgradeNum = int(1/UpgradeArray[y][0])
#                     randomNumber = random.randint(1, upgradeNum)  
#                     if (randomNumber == 1):
#                         EmpirePopulation[0] = EmpirePopulation[0] + 1
