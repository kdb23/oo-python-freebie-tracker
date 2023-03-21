from .freebie import Freebie

class Company:
    
    all = []

    def __init__(self, name, year):
        self.name = name
        self.year = year
        Company.all.append(self)

    @property
    def freebies(self):
        return [f.item_name for f in Freebie.all if f.company_instance == self]
        # print(Freebie.all)

    @property
    def devs(self):
        return [f.dev_instance.name for f in Freebie.all if f.company_instance == self]
    
    def give_freebie(self, item_name, value, dev):
        return Freebie(item_name, value, dev, self)
    
    @classmethod
    def oldest_company(cls):
        sorted_companies = cls.all.sort()
        return sorted_companies[0]