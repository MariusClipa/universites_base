class Universite:
    def __init__(self, name: object, year: object, city: object, note: object) -> object:
        self.name = name
        self.year = year
        self.city = city
        self.note = note

    def details_universite(self):
        return f"{self.name} lance en {self.year} est situe a {self.city} et a la note : {self.note}"

    def update_note(self, new_note):
        final_note = float((new_note + self.note) / 2)
        self.note = float(final_note)
        return {self.note}
