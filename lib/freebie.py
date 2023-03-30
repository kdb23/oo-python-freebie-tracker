
class Freebie:
    
    all = []

    def __init__(self, item_name, value, dev_instance, company_instance):
        self.item_name = item_name
        self.value = value
        self.dev_instance = dev_instance
        self.company_instance = company_instance
        Freebie.all.append(self)

    @property
    def print_details(self):
        print(f"{self.dev_instance.name} owns a {self.item_name} from {self.company_instance.name}")
    