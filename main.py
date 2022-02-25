def afficher_info_personnelle(nom, age ):
    print()
    print(" Joueur 1, ton nom est " +nom + ", tu as " + str(age) + " ans.")
    print(" L'an prochain tu auras " + str(age + 1) + " ans")
    if  age == 17:
        print("Vous êtes presque majeur.")
    elif 12 <= age < 18:
        print("Vous êtes adolescent.")
    elif age == 0 or age == 1:
        print("Vous êtes un bébé.")
    elif age == 18 :
        print("Vous êtes tout juste majeur: FELICITATION")
    elif age> 60:
        print("vous êtes donc senior")
    elif age< 10:
        print(" vous êtes un enfant")
    elif age > 18 :
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input(" quel est ton nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne+ " quel est ton âge?")
        try:
            age_int = int(age_str)
        except ValueError :
            print(" ERREUR, vous devez rentrer des chiffres ici")
    return age_int


nom1 = demander_nom()
nom2 = demander_nom()

print("nom1 : " + nom1)
print("nom2 : " + nom2)

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_info_personnelle(nom1, age1)
afficher_info_personnelle(nom2, age2)

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom= "personne"+ str(i+1)
    age = demander_age(nom)
    afficher_info_personnelle(nom,age)
