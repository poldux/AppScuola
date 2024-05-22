# file csv app scuola 

import csv



fileIn=open("C:\\Users\\giacomopoldi\\Desktop\\prova.csv", "r", encoding="utf-8")
reader = csv.DictReader(fileIn)
dati = []
for prova in reader:
    #print(prova)
    dati.append(prova)
fileIn.close()

print("\nPrimo Prof")
print(dati[0]["Nome"])
print(dati[0]["Cognome"])
print(dati[0]["ClasseProf"])

print("\nSecondo Prof")
print(dati[1]["Nome"])
print(dati[1]["Cognome"])
print(dati[1]["ClasseProf"])


print("\nTerzo Prof")
print(dati[2]["Nome"])
print(dati[2]["Cognome"])
print(dati[2]["ClasseProf"])




