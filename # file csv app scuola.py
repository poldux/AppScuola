# file csv app scuola 

import csv
ProfDictionary={}


fileIn=open("C:\\Users\\giacomopoldi\\Desktop\\prova.csv", "r", encoding="utf-8")
reader = csv.DictReader(fileIn)
dati = []
for prova in reader:
    #print(prova)
    dati.append(prova)
fileIn.close()



ProfDictionary['Professori'] = dati
print(ProfDictionary)


