import bibliotheque_universites
import class_universite 


# controler - gerer les objets 


def creer_notre_bibliotheque():
    NotreBibliotheque = bibliotheque_des_universites.BibliothequeUniversite()
    return NotreBibliotheque

def ajouter_universite_dans_bibliotheque(bibliotheque, universite):
    return bibliotheque.ajouter_universite(universite)

# Pour afficher toutes les universites 

def afficher_bibliotheque(bibliotheque):
    bibliotheque.show_all_universities()   

def modifions_note_universite_specifique(bibliotheque, nom_universite, nouvelle_note):
    if nouvelle_note <= 0:
        print(f"erreur, introduisez une autre note")
    elif nouvelle_note > 10:
        print(f"La note est tres grande, reintroduisez la note")
    else:
        bibliotheque.update_nota_for_universite(nom_universite, nouvelle_note)

def creer_universite(name, year, city, note):
    if note <= 0:
        print(f"erreur, introduisez une note valide")
    elif note > 10:
        print(f"La note est très grande, reintroduisez la note")
    else:
        universite = class_universite.Universite(name, year, city, note)
        return universite
