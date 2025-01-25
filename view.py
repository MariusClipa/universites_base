
import controler_universite


#creer la bibliotheque
Bibliotheque1 = controler_universite.creer_notre_bibliotheque()


#key : 1/2/3


while True:
    print(f"Bonjour, appuyer \n 1. Si vous voulez voir les universites d’une bibliotheque \n"
          f"2. Si vous voulez ajouter une universite \n"
          f"3. Si » vous voulez noter l’universite de 1 a 10")
    key = int(input())
    if key == 1:
        controler_universite.afficher_bibliotheque(Bibliotheque1)
        print("1")
    elif key == 2:
        nom_universite = input("Quel est le nom de l’université?") 
        annee_universite = input("Quelle est l’année où elle a été fondée?") 
        ville_universite = input("Dans quelle ville se situe cette université?") 
        note_universite = float(input("Quelle note donnez-vous à cette université?"))
        universite = controler_universite.creer_universite(nom_universite, annne_universite, ville_universite, note_universite)
        controler_universite.ajouter_universite_dans_bibliotheque(Bibliotheque1, universite)
    elif key == 3:
        nom_universite = input(‘Le nom d'universite : ')
        nouvelle_note = float(input(‘La nouvelle note de l’universite : '))
        controler_universite.modifions_note_universite_specifique(Bibliotheque1, nom_universite, note_universite)
    else:
        break
