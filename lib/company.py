from .freebie import Freebie

class Company:

    all = []

    def __init__(self, name, year):
        self.name = name
        self.year = year
        Company.all.append(self)

    @property
    def freebies(self):
        return [f for f in Freebie.all if f.company_instance == self]
    #   return [f.item_name for f in Freebie.all if f.company_instance == self]
    
    @property
    def devs(self):
        return [d.dev_instance.name for d in self.freebies]
    

    def give_freebie(self, item, value, dev):
        return Freebie(item, value, dev, self)
    
    @classmethod
    def oldest_company(cls):
        old_time = 3000
        new_string = "No Company Founding Year Found "

        for company in cls.all:
            if company.year < old_time:
                old_time = company.year
                new_string = company
        return new_string.name