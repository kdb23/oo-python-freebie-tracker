from .freebie import Freebie

class Dev:
    
    all = []

    def __init__(self, name):
        self.name = name
        Dev.all.append(self)

    @property
    def freebies(self):
        return [f.item_name for f in Freebie.all if f.dev_instance == self]
    
    @property
    def companies(self):
        return [c.company_instance for c in Freebie.all if c.company_instance == self]
    

    def recieved_one(self, item_name):
        if item_name in self.freebies:
            return True
        else:
            return False
        
    def give_away(self, freebie):
        pass