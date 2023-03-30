from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name

    
    @property
    def freebies(self):
        return [f for f in Freebie.all if f.dev_instance == self]
    #   return [f.item_name for f in Freebie.all if f.dev_instance == self]

    @property
    def companies(self):
        return [c.company_instance.name for c in self.freebies]