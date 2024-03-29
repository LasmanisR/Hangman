import random
import string
import sys


def Dzivibas(Nepareizi): #Funkcija pasaka cik dzīvības spēlētājam atlikušas
       DzivibasAtlikums = KluduLimits - Nepareizi
       print("Tev ir", DzivibasAtlikums, "atlikusas dzivibas.")

def BildesNum(Nepareizi): #Šī funkcija veido Hangman bildi, pēc katra gājiena
       if Nepareizi == 1: 
           print(Bilde1)
       if Nepareizi == 2:
           print(Bilde2)
       if Nepareizi == 3:
           print(Bilde3)
       if Nepareizi == 4:
           print(Bilde4)
       if Nepareizi == 5:
           print(Bilde5)
       if Nepareizi == 6:
           print(Bilde6)
       if Nepareizi == 7:
           print(Bilde7)

def Hint(Nepareizi, WordChoice): #Funkcija iedod hintu kad paliek pēdejāš divas dzīvības
       if Nepareizi == 6:
           WordChoice = list(WordChoice)
           WordHint = random.choice(WordChoice)
           WordChoice = "".join(WordChoice)
           print("Hints - Vārdā ir burts: ", WordHint)


List1 = ["tabula","serfosana","anglija","parize","pukes","laptops","smiltis","klase", "blonds", "zvaigzne", "zils", "cepure", "sniegs", "tetris", "gala", "palma","internets","kiegeli", "putns", "megabits", "ckaste", "jezus", "zabaks", "skolotajs", "tablete", "pisotle", "auto", "beigas", "zale", "logs", "zirneklis", "labi", "lol", "bezdibenis", "janoga", "neruna"] #These are all the words that can possibly be taken
KluduLimits = 7 #Spēlētāja dzīvību/kļūdu limits
Infinity = 9999999999999999999999999999999999 #Loopu daudzums
Bilde1 = ('''
     +---+
     |   |
         |
         |
         |
         |
=========''')
Bilde2 = ('''
     +---+
     |   |
     O   |
         |
         |
         |
=========''')
Bilde3 = ('''
     +---+
     |   |
     O   |
     |   |
         |
         |
=========''')
Bilde4 = ('''
     +---+
     |   |
     O   |
    /|   |
         |
         |
=========''')
Bilde5 = ('''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
=========''')
Bilde6 = ('''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
=========''')
Bilde7 = ('''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
=========''') #Hangmana attēli


Nepareizi = 0 
List2 = [] 

input("Spied \"Enter\" lai saktu speli." + "\n")


for i in range(Infinity):
       WordChoice = (random.choice(List1)) #Random izvēlas vārdu no listes 1
       BurtuSkaits = len(WordChoice) 
       print("<-----[JAUNA SPĒLE]----->\n")
       print("Vards ir", BurtuSkaits, "burtu garumā.") #Printē vardu burtu skaitu
       if BurtuSkaits == 1: #Printe varda garumu ar apaksvitram
           L = ("_")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 2:
           L = ("__")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 3:
           L = ("___")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 4:
           L = ("____")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 5:
           L = ("_____")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 6:
           L = ("______")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 7:
           L = ("_______")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 8:
           L = ("________")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 9:
           L = ("_________")
           print(L.replace("", " ")[1: -1], "\n")
       if BurtuSkaits == 10:
           L = ("__________")
           print(L.replace("", " ")[1: -1], "\n")

       GuessLists = list(L) 
       DzivibasAtlikums = KluduLimits - Nepareizi #Skaita atlikušās dzīvības

       for i in range(Infinity): 
           if GuessLists == WordChoice:
               break

           Hint(Nepareizi, WordChoice) 

           for i in range(Infinity): 
               Guess1 = input("Mini burtu: ") #Spēletaja burtu atminējums
               GuessLength = len(Guess1)
               if GuessLength > 1:
                   print("Ievadi tikai vienu burtu!") #Atkartoti prasa ievadīt burtu ja ievaditi divi vai vairāk burti
               elif Guess1 == "":
                   print("Ievadi burtu tu neko neierakstiji.") #Atkartoti prasa ievadīt burtu ja nekas netika ievadits
               else:
                   break

           Guess1 = Guess1.lower() 
           List2.append(Guess1) 

           if WordChoice.find(Guess1) >= 0: #Booleans kas atrod vai burts ir varda
               GuessLists = list(GuessLists) 
               for x, y in enumerate(WordChoice): #Aiizvieto apakšsvītru ar pareizo burtu
                   if Guess1 == y:
                       GuessLists[x] = y
               print("Burts", Guess1.upper(), "bija pareizs.") #Ziņa kas pasaka, ka burts bija pareizs
               GuessLists = "".join(GuessLists) 
           else:
               Nepareizi += 1 
               print("Nepareizi.")
               GuessLists = "".join(GuessLists) 
               BildesNum(Nepareizi) 
               Dzivibas(Nepareizi) 

           List2 = "".join(List2) #
           print("Minētie burti: ",List2.upper()) #Printē spēlētāja minētos burtus
           List2 = list(List2) 
           List2.append(", ") 
           print(GuessLists.replace("", " ")[1: -1], "\n") 

           if GuessLists == WordChoice: #Nosaka vai spēlētājs ir uzvarējis 
               print("LOL tu uzminēji? APSVEICU!")
               Nepareizi = 0 
               List2 = []
               GuessLists = []
               JaunaSpele = input("Gribi spēlēt atkal? [J]ā, [N]ē: \n")
               if JaunaSpele == "J":
                   break
               else:
                   sys.exit()

           if Nepareizi == 7: #Nosaka vai spēlētājs ir zaudējis
               print("LOL zaudēji.")
               print("Vārds bija: ", WordChoice + ".")
               Nepareizi = 0 
               List2 = []
               GuessLists = []
               JaunaSpele = input("Gribi spēlēt atkal? [J]ā, [N]ē: \n")
               if JaunaSpele == "J":           
                   break
               else:
                   sys.exit()