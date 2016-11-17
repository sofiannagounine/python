#!usr/bin/env python3

#import de la lib sys
import sys

print(sys.version_info)
print(sys.version)

print(sys.platform)

print("hello")

print('world')


print("c'est moi!")

print("tiens prend ton chemin : http://www.coucou.fr")

print("""coucou

        la la suite

      cest fou""")

str = "spam"

print(str)

#list: créé une liste, ex: l = list(str) -> l = ['z', '', 'b', 'o', 'u', 'b']

#find: booléen si trouvé 1 sinon 0, ex: str.find("pa") -> 1

#replace: remplace l'élément 1 par l'élément 2 dans une chae de caractère, ex: str.replace('pa','xyz') -> 'sxyzm'

#isalpha: Retourne True si tous les caractères sont des lettres et qu'il y a au moins un caractère. Sinon False

#isalnum: Retourne True si tous les caractères sont des alphanumérique. Sinon False

#rstrip: enleve les espace et les retour chariot/tab à droite de la chaîne de caractères

#pop: sort l'élément indiqué de la liste

i = 5
mykey = "temps"
fois = 20

#formatage d'une chaîne de caractère pour afficher des variables

print('la valeur %d et le mot \'%s\' apparaissent %d fois, ' % (i, mykey, fois))
print('la valeur %2.2f et le mot \'%s\' apparaissent %d fois, ' % (i, mykey, fois))
print('la valeur {} et le mot \'{}\' apparaissent {} fois, '.format(i, mykey, fois))


valeur = "cat"
if valeur == "cat" :
    print("OK")
elif valeur == "dog" :
    print("dog OK")
else:
    print("inconnu")


valeur="Toto"
valeur2="Poussin"

if valeur == "Toto" and valeur2 == "Poussin" :
    print("OK")


seq = [1,2,3,4]
a,b,c,d=seq
print(a)

for letter in "spam":
    print("current letter", letter)

fruits = ['banane','pomme','mangue']
for fruit in fruits:
    print(" mon fruit", fruit)

for num in range(1,10):
    print (num)
    if num == 5:
        continue
    if num == 6:
        break



var = 10
while True:
    var -= 1
    if var == 6:
        continue
    print(var)
    if var == 0:
        break
print ("end loop")

#exemple de liste de comprehension
a = [1,2,3,4,5,6,7,8,9,10]
#Attention resultat avant le for!
squares = [x**2 for x in a]
print(squares)

# on a deux variable temps et distance et il faut calculer la vitesse
temps = 6.896
distance = 19.7
vitesse = distance/temps
print('la valeur de la vitesse est de: {} km/h'.format(vitesse))
#ou
print('la valeur de la vitesse est de: {:.2f} km/h'.format(vitesse))
#ou
msg="la vitesse est = {:.2f} metre par seconde"
print(msg.format(vitesse))


# en utilisant la fonction range
# afficher les entier de 0 à 3
range(3)
# autre afficher de 4 à 7
range(4,8)
# avec une boucle for afficher les caractère de la chaîne suivante
msg = "c'est la formation Devops"
for c in msg:
    print(c)
# sur la liste suivante faire les actions suivantes
liste = [17,38,10,25,72]
# triez et affichez la liste
liste.sort()
print(liste)
# ajoutez l'élément 12 et afficher la liste
liste.append(12)
print(liste)
# afficher l'indice de l'élément 17
print(liste.index(17))
# enlevez l'élément 38 et afficher la liste
liste.remove(38)
print(liste)
# afficher la sous-liste du 3ème élément jusqu'à la fin de la liste
print(liste[2:])
# ajouter a GIT
#test youyouyou