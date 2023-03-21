from .freebie import Freebie

class Company:
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @property
    def freebies(self):
        return [f.item_name for f in Freebie.all if f.company_instance == self]
        # print(Freebie.all)

    @property
    def devs(self):
        return [f.dev_instance.name for f in Freebie.all if f.company_instance == self]