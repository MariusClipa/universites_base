import class_universite


class BibliothequeUniversite :
    def __init__(self):
        self.universite = []

    def add_universite(self, new_universite):
        universite = self.universite.append(new_universite)
        return universite

    def show_all_universities(self):
        for universite in self.universite:
            print(universite.details_universite())

    def update_nota_for_universite(self, name, notaToUpdate):
        global to_update_universite
        for universite in self.universite:
            if universite.name == name:
                to_update_universite = universite
                to_update_universite.update_nota(notaToUpdate)
                print(f"La note de l'université a été actualisée")
            else:
                to_update_universite = None
                print(f"Erreur : université non trouvée")
