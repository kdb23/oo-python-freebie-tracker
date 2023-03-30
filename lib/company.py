from .freebie import Freebie

class Company:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company_instance == self]
    #   return [f.item_name for f in Freebie.all if f.company_instance == self]
    
    @property
    def devs(self):
        return [d.dev_instance.name for d in self.freebies]
    