
class Freebie:
    
    all = []

    def __init__(self, item_name, value, dev_instance, company_instance):
        self.item_name = item_name
        self.value = value
        self.dev_instance = dev_instance
        self.company_instance = company_instance
        Freebie.all.append(self)

    
    