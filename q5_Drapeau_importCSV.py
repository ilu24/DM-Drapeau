import csv, sys

def flagsort(tab,ind):
    b = 0
    r = len(tab)-1
    w = 0
    R = False
    
    while R == False:
        if tab[w][ind] == "1":
            tab[w], tab[b] = tab[b], tab[w]
            w += 1
            b += 1
        if tab[w][ind] == "2":
            w +=1
        if tab[w][ind] == "3":
            tab[r], tab[w] = tab[w], tab[r]
            r -= 1
        if w >= r:
            R = True
            
# importation du fichier csv "BDN2" dans la variable "tableau"
# mise en forme dans un tableau et 
# choix / validation de la variable de tri du tableau
try:
    with open('BDN2.csv') as csvfile :
        fichier = csv.reader(csvfile)
        tableau = []
        for ligne in fichier:
            tableau.append(ligne)
except FileNotFoundError :
    print('Fichier csv non trouvé.')
    exit()

# importation dans liste de listes, séparation descripteurs - enrtegistrements          
variables = tableau[0]
tableau.pop(0)

# affichage des choix possibles
print('\nListe des variables :')
for var in variables :
    print(var, end=' ')
print('\n\nConsulte le dictionnaire des variables avant de faire ton choix.')

while True :
    choix = input('\nSur quelle variable faire le tri ? ')
    if choix not in variables :
        print("Cette variable n'est pas dans la liste.")
    elif variables.index(choix) not in [1,3,4,8,9,10,11,13,17,22,23,24,25]:
        print("Cette variable n'a pas trois états.")
    else :
        break


flagsort(tableau, variables.index(choix))

print(len(tableau))


