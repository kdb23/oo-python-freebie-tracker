from .freebie import Freebie

class Dev:
    
    def __init__(self, name):
        self.name = name

    
    @property
    def freebies(self):
        return [f.item_name for f in Freebie.all if f.dev_instance == self]

    @property
    def companies(self):
        return [c.company_instance.name for c in self.freebies]
    
    def recieved_one(self, item_name):
        if item_name in self.freebies:
            return True
        else:
            return False
        
    def give_away(self, dev_accept, freebie):
        if freebie.dev_instance  == self:
            freebie.dev_instance == dev_accept
        else:
            print("thats not yours to give away !")

            # d1.give_away(d2,f1) ---- given away
            # d2.give_away(d1,f1) ---- "thats not yours to give away"