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

profDictionary['Professori'] = dati
print(profDictionary)

field_names = ['Nome', 'Cognome', 'ClasseProf']
newProf = {'Nome': 'Samuele', 'Cognome': 'Maranghi', 'ClasseProf': '4I1'}

with open('prova.csv', 'a') as f_object:
    dictwriter_oggetto = DictWriter(f_object, fieldnames=field_names)
    dictwriter_oggetto.writerow(newProf)
    f_object.close()

print("")
print(profDictionary)