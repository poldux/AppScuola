# file csv app scuola 
import csv
from csv import DictWriter

profDictionary={}

fileIn=open("C:\\Users\\giacomopoldi\\Desktop\\prova.csv", "r", encoding="utf-8")
reader = csv.DictReader(fileIn)

dati = []

for prova in reader:
    #print(prova)
    dati.append(prova)
fileIn.close()


print(dati)

new_prof={'Nome': 'Samuele', 'Cognome': 'Maranghi', 'ClasseProf': '3I1'}
dati.append(new_prof)
print(dati)

with open("C:\\Users\\giacomopoldi\\Desktop\\prof_nuovo.csv","w") as fw:
    #scorre il dizionario
    for element in dati:
        fw.write(element["Nome"]+ " , ")
        fw.write(element["Cognome"]+ " , ")
        fw.write(element["ClasseProf"]+ " , "+ "\n")
        print(element)